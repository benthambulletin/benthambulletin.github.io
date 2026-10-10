#!/usr/bin/env python3
"""Hourly barometer log for the Barograph.

Run by .github/workflows/pressure.yml every three hours. Pulls the last
several hours of METAR observations for KIAG (North Tonawanda), KDKK
(Dunkirk) and KROC (Scottsville) from the FAA/NWS Aviation Weather API,
merges them into data/pressure-log.csv (deduped on station+time), and
rewrites data/pressure-summary.json with the numbers the morning build
needs: latest reading per station, the 3/6/12/24-hour change, trend word,
and the last seven days at hourly resolution.

If the log is empty (first run) it backfills from the Iowa Environmental
Mesonet ASOS archive from Sept 1, 2026.

Conventions: `slp_mb` is sea-level pressure in millibars (what the paper
calls the reading, MSL). `altim_inhg` is the altimeter setting in inches,
the number phone weather apps show. Times are UTC in the CSV.
"""
import csv
import json
import sys
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LOG = ROOT / "data" / "pressure-log.csv"
SUMMARY = ROOT / "data" / "pressure-summary.json"
STATIONS = ["KIAG", "KDKK", "KROC"]
TOWN = {"KIAG": "North Tonawanda", "KDKK": "Dunkirk", "KROC": "Scottsville"}
FIELDS = ["time_utc", "station", "altim_inhg", "slp_mb", "temp_c"]
BACKFILL_FROM = datetime(2026, 9, 1, tzinfo=timezone.utc)
AWC = "https://aviationweather.gov/api/data/metar?ids={ids}&format=json&hours={hours}"
IEM = ("https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py"
       "?station={st}&data=alti&data=mslp&data=tmpc"
       "&year1={y1}&month1={m1}&day1={d1}&year2={y2}&month2={m2}&day2={d2}"
       "&tz=Etc/UTC&format=onlycomma&latlon=no&elev=no&missing=empty&trace=empty"
       "&direct=no&report_type=3")


def get(url, timeout=60):
    req = urllib.request.Request(url, headers={"User-Agent": "bentham-bulletin-barograph"})
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read().decode("utf-8", "replace")


def read_log():
    rows = {}
    if LOG.exists():
        with LOG.open(newline="") as f:
            for r in csv.DictReader(f):
                rows[(r["station"], r["time_utc"])] = r
    return rows


def write_log(rows):
    LOG.parent.mkdir(parents=True, exist_ok=True)
    with LOG.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for key in sorted(rows, key=lambda k: (k[1], k[0])):
            w.writerow({k: rows[key].get(k, "") for k in FIELDS})


def fmt(x, nd):
    return "" if x in (None, "") else f"{float(x):.{nd}f}"


def fetch_awc(rows, hours=12):
    data = json.loads(get(AWC.format(ids=",".join(STATIONS), hours=hours)))
    added = 0
    for o in data:
        st = o.get("icaoId")
        if st not in STATIONS or o.get("obsTime") is None:
            continue
        t = datetime.fromtimestamp(o["obsTime"], tz=timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
        altim_mb = o.get("altim")
        rec = {
            "time_utc": t,
            "station": st,
            # AWC serves the altimeter in hPa; convert to inches for the paper.
            "altim_inhg": fmt(altim_mb / 33.8639, 2) if altim_mb not in (None, "") else "",
            "slp_mb": fmt(o.get("slp"), 1),
            "temp_c": fmt(o.get("temp"), 1),
        }
        if rec["slp_mb"] == "" and rec["altim_inhg"] == "":
            continue
        if (st, t) not in rows:
            added += 1
        rows[(st, t)] = rec
    return added


def backfill_iem(rows, start, end):
    added = 0
    for st in STATIONS:
        url = IEM.format(st=st, y1=start.year, m1=start.month, d1=start.day,
                         y2=end.year, m2=end.month, d2=end.day)
        text = get(url, timeout=120)
        lines = [l for l in text.splitlines() if l and not l.startswith("#")]
        if not lines:
            continue
        rd = csv.DictReader(lines)
        for r in rd:
            try:
                t = datetime.strptime(r["valid"], "%Y-%m-%d %H:%M").replace(tzinfo=timezone.utc)
            except (KeyError, ValueError):
                continue
            key = (st, t.strftime("%Y-%m-%dT%H:%MZ"))
            if key in rows:
                continue
            rec = {
                "time_utc": key[1],
                "station": st,
                "altim_inhg": fmt(r.get("alti"), 2),
                "slp_mb": fmt(r.get("mslp"), 1),
                "temp_c": fmt(r.get("tmpc"), 1),
            }
            if rec["slp_mb"] == "" and rec["altim_inhg"] == "":
                continue
            rows[key] = rec
            added += 1
    return added


def value_mb(r):
    """Sea-level pressure in mb, falling back to altimeter converted."""
    if r.get("slp_mb"):
        return float(r["slp_mb"])
    if r.get("altim_inhg"):
        return round(float(r["altim_inhg"]) * 33.8639, 1)
    return None


def nearest(series, target, tol=timedelta(minutes=90)):
    best, bd = None, tol
    for t, v in series:
        d = abs(t - target)
        if d <= bd:
            best, bd = v, d
    return best


def trend_word(d3, d24):
    if d3 is None:
        return "steady"
    if d3 <= -1.5:
        return "falling fast"
    if d3 <= -0.6:
        return "falling"
    if d3 >= 1.5:
        return "rising fast"
    if d3 >= 0.6:
        return "rising"
    if d24 is not None and d24 <= -3:
        return "falling, slowly"
    if d24 is not None and d24 >= 3:
        return "rising, slowly"
    return "steady"


def summarize(rows, now):
    out = {"generated_utc": now.strftime("%Y-%m-%dT%H:%MZ"), "stations": {}}
    for st in STATIONS:
        series = []
        for (s, t), r in rows.items():
            if s != st:
                continue
            v = value_mb(r)
            if v is None:
                continue
            series.append((datetime.strptime(t, "%Y-%m-%dT%H:%MZ").replace(tzinfo=timezone.utc), v))
        series.sort()
        if not series:
            continue
        t_last, v_last = series[-1]
        deltas = {}
        for h in (3, 6, 12, 24):
            past = nearest(series, t_last - timedelta(hours=h))
            deltas[f"d{h}h_mb"] = None if past is None else round(v_last - past, 1)
        week = [(t, v) for t, v in series if t >= t_last - timedelta(days=7)]
        last_r = rows[(st, t_last.strftime("%Y-%m-%dT%H:%MZ"))]
        out.setdefault("_obs", {})[st] = series
        out["stations"][st] = {
            "town": TOWN[st],
            "latest_time_utc": t_last.strftime("%Y-%m-%dT%H:%MZ"),
            "latest_mb": v_last,
            "latest_inhg": round(v_last / 33.8639, 2),
            "altim_inhg": float(last_r["altim_inhg"]) if last_r.get("altim_inhg") else None,
            "temp_c": float(last_r["temp_c"]) if last_r.get("temp_c") else None,
            **deltas,
            "trend": trend_word(deltas["d3h_mb"], deltas["d24h_mb"]),
            "week_min_mb": min(v for _, v in week),
            "week_max_mb": max(v for _, v in week),
            "hourly_7d": [[t.strftime("%Y-%m-%dT%H:%MZ"), v] for t, v in week],
        }
    return out


OPEN_METEO = ("https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}"
              "&hourly=pressure_msl&forecast_days=3&timezone=UTC")
FORECAST_POINTS = {"KIAG": (43.0387, -78.8642), "KDKK": (42.4932, -79.3350), "KROC": (43.0245, -77.7467)}
SWING_ALERT_MB = 5.0


def forecast(out, now):
    """Next 48 hours of modeled sea-level pressure per town, plus the biggest
    24-hour move coming and when. Either direction counts: the family log so far
    shows attacks on rises as often as falls, so the paper flags the size of the
    swing, not just drops."""
    out["forecast"] = {}
    for st, (lat, lon) in FORECAST_POINTS.items():
        try:
            d = json.loads(get(OPEN_METEO.format(lat=lat, lon=lon)))
        except Exception as e:  # noqa: BLE001
            print(f"forecast {st} failed: {e}", file=sys.stderr)
            continue
        times = d["hourly"]["time"]
        vals = d["hourly"]["pressure_msl"]
        pts = []
        for t, v in zip(times, vals):
            if v is None:
                continue
            tt = datetime.strptime(t, "%Y-%m-%dT%H:%M").replace(tzinfo=timezone.utc)
            if now - timedelta(hours=1) <= tt <= now + timedelta(hours=48):
                pts.append((tt, float(v)))
        if len(pts) < 25:
            continue
        # biggest 24h change ending at any forecast hour, and biggest 3h move
        best24 = (0.0, None, None)
        best3 = (0.0, None, None)
        idx = {t: v for t, v in pts}
        for t, v in pts:
            p24 = idx.get(t - timedelta(hours=24))
            if p24 is None:
                # fall back on the observed log for the start of the window
                p24 = nearest(out.get("_obs", {}).get(st, []), t - timedelta(hours=24))
            if p24 is not None and abs(v - p24) > abs(best24[0]):
                best24 = (round(v - p24, 1), (t - timedelta(hours=24)), t)
            p3 = idx.get(t - timedelta(hours=3))
            if p3 is not None and abs(v - p3) > abs(best3[0]):
                best3 = (round(v - p3, 1), (t - timedelta(hours=3)), t)
        fmt_t = lambda x: x.strftime("%Y-%m-%dT%H:%MZ") if x else None  # noqa: E731
        out["forecast"][st] = {
            "town": TOWN[st],
            "source": "Open-Meteo pressure_msl, hourly",
            "next48h": [[fmt_t(t), v] for t, v in pts],
            "max_24h_change_mb": best24[0],
            "max_24h_window": [fmt_t(best24[1]), fmt_t(best24[2])],
            "max_3h_change_mb": best3[0],
            "max_3h_window": [fmt_t(best3[1]), fmt_t(best3[2])],
            "swing_alert": abs(best24[0]) >= SWING_ALERT_MB or abs(best3[0]) >= 1.5,
            "end48h_mb": pts[-1][1],
            "change_to_end48h_mb": round(pts[-1][1] - pts[0][1], 1),
        }
    out.pop("_obs", None)
    return out


def main():
    now = datetime.now(timezone.utc)
    rows = read_log()
    was_empty = not rows
    if was_empty:
        try:
            n = backfill_iem(rows, BACKFILL_FROM, now)
            print(f"backfill: {n} rows from IEM")
        except Exception as e:  # noqa: BLE001
            print(f"backfill failed: {e}", file=sys.stderr)
    import os
    bf = os.environ.get("BACKFILL_FROM", "").strip()
    if bf:
        start = datetime.strptime(bf, "%Y-%m-%d").replace(tzinfo=timezone.utc)
        n = backfill_iem(rows, start, now)
        print(f"manual backfill from {bf}: {n} rows from IEM")
    added = fetch_awc(rows, hours=12 if not was_empty else 150)
    print(f"awc: {added} new rows, {len(rows)} total")
    write_log(rows)
    SUMMARY.write_text(json.dumps(forecast(summarize(rows, now), now), indent=1) + "\n")
    print(f"wrote {LOG.name} and {SUMMARY.name}")


if __name__ == "__main__":
    main()
