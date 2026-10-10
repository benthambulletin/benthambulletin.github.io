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


def summarize(rows, today):
    """Last night's numbers plus the flag for the paper."""
    recent = [rows[d] for d in sorted(rows) if d <= today.isoformat()][-60:]
    hours = [float(r["sleep_h"]) for r in recent if r.get("sleep_h")]
    med = sorted(hours)[len(hours) // 2] if hours else None
    last = rows.get(today.isoformat()) or {}
    sleep_h = float(last["sleep_h"]) if last.get("sleep_h") else None
    bb = int(last["bb_high"]) if last.get("bb_high") else None
    reasons = []
    if bb is not None and bb < BB_FLAG:
        reasons.append(f"Body Battery {bb} at wake (under {BB_FLAG})")
    if sleep_h is not None and med is not None and sleep_h < med - SLEEP_SHORT_H:
        reasons.append(f"{sleep_h:.1f} h sleep against a usual {med:.1f}")
    yday = rows.get((today - timedelta(days=1)).isoformat()) or {}
    return {
        "generated_utc": datetime.utcnow().strftime("%Y-%m-%dT%H:%MZ"),
        "night_ending": today.isoformat(),
        "last_night": {k: last.get(k, "") for k in FIELDS if k != "date"},
        "usual_sleep_h_60d": round(med, 2) if med else None,
        "yesterday_stress": yday.get("stress", ""),
        "flag_next_day": bool(reasons),
        "flag_reasons": reasons,
        "rule": "Body Battery under 70 at wake, or a night 30+ min short of usual, flags the next day (Oct 10, 2026 analysis).",
    }


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
    print(f"pulled {pulled} days; {len(rows)} rows in {CSV.name}")


if __name__ == "__main__":
    main()
