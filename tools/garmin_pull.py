#!/usr/bin/env python3
"""Nightly Garmin pull for the Barograph.

Runs from .github/workflows/garmin.yml every morning. Signs in to Garmin
Connect with GARMIN_EMAIL / GARMIN_PASSWORD (repository secrets), pulls the
last several days of sleep, Body Battery, stress, resting heart rate and
(when the device provides it) HRV, and merges them into
data/garmin-daily.csv. Also writes data/garmin-summary.json with last
night's numbers and the flag the paper uses.

The watch-based risk rule (from the Oct 10, 2026 analysis of 40 attacks):
a Body Battery high under 70 at wake, or a night more than ~30 minutes
shorter than the person's usual, flags the NEXT day. The paper prints the
numbers and the flag, nothing clinical.
"""
import csv
import json
import os
import sys
from datetime import date, datetime, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CSV = ROOT / "data" / "garmin-daily.csv"
SUMMARY = ROOT / "data" / "garmin-summary.json"
FIELDS = ["date", "sleep_h", "bedtime", "wake", "sleep_score", "deep_h", "rem_h",
          "awake_h", "bb_high", "bb_low", "stress", "rhr", "hrv", "resp"]
DAYS_BACK = int(os.environ.get("GARMIN_DAYS_BACK", "7"))
BB_FLAG = 70
SLEEP_SHORT_H = 0.5  # shorter than the 60-day median by this much flags


def hm(ms):
    """Local wall-clock 'h:mm AM' from Garmin's *Local* epoch-ms fields."""
    if not ms:
        return ""
    return datetime.utcfromtimestamp(ms / 1000).strftime("%-I:%M %p")


def read_csv():
    rows = {}
    if CSV.exists():
        with CSV.open(newline="") as f:
            for r in csv.DictReader(f):
                rows[r["date"]] = {k: r.get(k, "") for k in FIELDS}
    return rows


def write_csv(rows):
    with CSV.open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=FIELDS)
        w.writeheader()
        for d in sorted(rows):
            w.writerow({k: rows[d].get(k, "") for k in FIELDS})


def pull(client, day):
    out = {"date": day.isoformat()}
    ds = day.isoformat()
    try:
        s = client.get_sleep_data(ds) or {}
        d = s.get("dailySleepDTO") or {}
        secs = d.get("sleepTimeSeconds")
        if secs:
            out["sleep_h"] = f"{secs / 3600:.2f}"
            out["bedtime"] = hm(d.get("sleepStartTimestampLocal"))
            out["wake"] = hm(d.get("sleepEndTimestampLocal"))
            for k, src in (("deep_h", "deepSleepSeconds"), ("rem_h", "remSleepSeconds"),
                           ("awake_h", "awakeSleepSeconds")):
                if d.get(src) is not None:
                    out[k] = f"{d[src] / 3600:.2f}"
            sc = ((d.get("sleepScores") or {}).get("overall") or {}).get("value")
            if sc is not None:
                out["sleep_score"] = str(sc)
            if d.get("averageRespirationValue") is not None:
                out["resp"] = f"{d['averageRespirationValue']:.1f}"
    except Exception as e:  # noqa: BLE001
        print(f"{ds} sleep: {e}", file=sys.stderr)
    try:
        for b in client.get_body_battery(ds, ds) or []:
            vals = [v[1] for v in (b.get("bodyBatteryValuesArray") or []) if v and v[1] is not None]
            if vals:
                out["bb_high"] = str(max(vals))
                out["bb_low"] = str(min(vals))
    except Exception as e:  # noqa: BLE001
        print(f"{ds} body battery: {e}", file=sys.stderr)
    try:
        st = client.get_stress_data(ds) or {}
        if st.get("avgStressLevel") not in (None, -1, -2):
            out["stress"] = str(st["avgStressLevel"])
    except Exception as e:  # noqa: BLE001
        print(f"{ds} stress: {e}", file=sys.stderr)
    try:
        r = client.get_rhr_day(ds) or {}
        m = ((r.get("allMetrics") or {}).get("metricsMap") or {}).get("WELLNESS_RESTING_HEART_RATE") or []
        if m and m[0].get("value") is not None:
            out["rhr"] = str(int(m[0]["value"]))
    except Exception as e:  # noqa: BLE001
        print(f"{ds} rhr: {e}", file=sys.stderr)
    try:
        h = client.get_hrv_data(ds) or {}
        v = (h.get("hrvSummary") or {}).get("lastNightAvg")
        if v is not None:
            out["hrv"] = str(v)
    except Exception as e:  # noqa: BLE001
        print(f"{ds} hrv: {e}", file=sys.stderr)
    return out


def _median(xs):
    xs = sorted(xs)
    return xs[len(xs) // 2] if xs else None


def _hm_to_h(txt):
    try:
        t = datetime.strptime(txt, "%I:%M %p")
        return t.hour + t.minute / 60
    except Exception:  # noqa: BLE001
        return None


def score_day(rows, day):
    """Experimental risk score for the day after `day`'s morning reading.
    Inputs (Oct 10, 2026 audit, logging-window data): wake earlier than usual,
    Body Battery high this morning, resting HR above usual, yesterday's stress,
    a short night. No 'days since last attack' term — it points the wrong way.
    Max 10. Returns (score, flags, detail) or (None, [], detail) if last night
    is missing."""
    ds = day.isoformat()
    r = rows.get(ds) or {}
    hist = [rows[d] for d in sorted(rows) if d < ds][-60:]
    usual_wake = _median([_hm_to_h(x["wake"]) for x in hist if x.get("wake") and _hm_to_h(x["wake"])])
    usual_sleep = _median([float(x["sleep_h"]) for x in hist if x.get("sleep_h")])
    usual_rhr = _median([float(x["rhr"]) for x in hist if x.get("rhr")])
    y = rows.get((day - timedelta(days=1)).isoformat()) or {}
    wake = _hm_to_h(r["wake"]) if r.get("wake") else None
    sleep_h = float(r["sleep_h"]) if r.get("sleep_h") else None
    bb = int(r["bb_high"]) if r.get("bb_high") else None
    rhr = float(r["rhr"]) if r.get("rhr") else None
    stress = float(y["stress"]) if y.get("stress") else None
    detail = {
        "wake": r.get("wake", ""), "usual_wake_h": round(usual_wake, 2) if usual_wake else None,
        "wake_dev_min": round((wake - usual_wake) * 60) if (wake and usual_wake) else None,
        "sleep_h": sleep_h, "usual_sleep_h": round(usual_sleep, 2) if usual_sleep else None,
        "bb_high": bb, "rhr": rhr, "usual_rhr": usual_rhr, "stress_yday": stress,
    }
    if sleep_h is None and bb is None:
        return None, [], detail
    sc, flags = 0, []
    if detail["wake_dev_min"] is not None:
        if detail["wake_dev_min"] <= -25:
            sc += 3; flags.append("woke early")
        elif detail["wake_dev_min"] <= -15:
            sc += 1; flags.append("woke a bit early")
    if bb is not None:
        if bb < BB_FLAG:
            sc += 3; flags.append("Body Battery low")
        elif bb < 80:
            sc += 1; flags.append("Body Battery so-so")
    if stress is not None:
        if stress >= 40:
            sc += 2; flags.append("stressful yesterday")
        elif stress >= 35:
            sc += 1; flags.append("stress elevated yesterday")
    if rhr is not None and usual_rhr is not None and rhr >= usual_rhr + 2:
        sc += 1; flags.append("resting HR up")
    if sleep_h is not None and usual_sleep is not None and sleep_h < usual_sleep - SLEEP_SHORT_H:
        sc += 1; flags.append("short night")
    return min(sc, 10), flags, detail


def summarize(rows, today):
    """Last night's numbers plus the experimental score, for the dashboard only."""
    last = rows.get(today.isoformat()) or {}
    sc, flags, detail = score_day(rows, today)
    return {
        "generated_utc": datetime.utcnow().strftime("%Y-%m-%dT%H:%MZ"),
        "night_ending": today.isoformat(),
        "last_night": {k: last.get(k, "") for k in FIELDS if k != "date"},
        "score": sc, "flags": flags, "detail": detail,
        "experimental": True,
        "rule": "Experimental 0-10 score: early waking, low Body Battery, yesterday's stress, resting HR, short night. Judged by the scoreboard, not assumed.",
    }


def log_scores(rows, today):
    """Append today's score to data/runway-log.json (one entry per date) so the
    dashboard can keep an honest hit/miss record."""
    path = ROOT / "data" / "runway-log.json"
    log = {}
    if path.exists():
        try:
            for e in json.loads(path.read_text()):
                log[e["date"]] = e
        except Exception:  # noqa: BLE001
            pass
    for i in range(3):  # today and two catch-up days, in case a pull was late
        d = today - timedelta(days=i)
        sc, flags, detail = score_day(rows, d)
        if sc is None:
            continue
        if d.isoformat() in log and log[d.isoformat()].get("score") is not None and i > 0:
            continue
        log[d.isoformat()] = {"date": d.isoformat(), "score": sc, "flags": flags,
                              "wake_dev_min": detail["wake_dev_min"], "bb_high": detail["bb_high"],
                              "stress_yday": detail["stress_yday"]}
    path.write_text(json.dumps([log[k] for k in sorted(log)], indent=1) + "\n")


def main():
    from garminconnect import Garmin  # installed by the workflow

    email, pw = os.environ.get("GARMIN_EMAIL"), os.environ.get("GARMIN_PASSWORD")
    if not (email and pw):
        print("GARMIN_EMAIL / GARMIN_PASSWORD not set", file=sys.stderr)
        sys.exit(1)
    tokens = ROOT / ".garmin-tokens"  # cached by the workflow between runs
    client = Garmin(email, pw)
    try:
        client.login(str(tokens)) if tokens.exists() else client.login()
    except Exception:  # noqa: BLE001
        client = Garmin(email, pw)
        client.login()
    try:
        client.garth.dump(str(tokens))
    except Exception:  # noqa: BLE001
        pass

    rows = read_csv()
    today = date.today()
    pulled = 0
    for i in range(DAYS_BACK):
        day = today - timedelta(days=i)
        rec = pull(client, day)
        if len(rec) > 1:
            cur = rows.get(rec["date"], {})
            cur.update({k: v for k, v in rec.items() if v != ""})
            rows[rec["date"]] = cur
            pulled += 1
    write_csv(rows)
    SUMMARY.write_text(json.dumps(summarize(rows, today), indent=1) + "\n")
    log_scores(rows, today)
    print(f"pulled {pulled} days; {len(rows)} rows in {CSV.name}")


if __name__ == "__main__":
    main()
