#!/usr/bin/env python3
"""Pool watchdog (Garret, Nov 7): spot a run that didn't land. Reads pool/data/season.json only.

Prints one PROBLEM line per thing that looks missed, or OK. The watchdog workflow turns PROBLEM lines into a
GitHub issue (so Garret gets an email) and closes it once the board catches up. Never reveals picks.
"""
import json, os, sys
from datetime import datetime, timezone, timedelta
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = lambda s: datetime.fromisoformat(s.replace("Z", "+00:00"))

def et(now):   # Eastern: EDT until the first Sunday of November, then EST (good enough for a watchdog)
    y = now.year
    nov1 = datetime(y, 11, 1, 6, tzinfo=timezone.utc); dst_end = nov1 + timedelta(days=(6 - nov1.weekday()) % 7)
    mar8 = datetime(y, 3, 8, 7, tzinfo=timezone.utc); dst_start = mar8 + timedelta(days=(6 - mar8.weekday()) % 7)
    return now + timedelta(hours=-4 if dst_start <= now < dst_end else -5)

def main():
    now = datetime.now(timezone.utc)
    if len(sys.argv) > 1: now = P(sys.argv[1])   # for testing
    s = json.load(open(f"{HERE}/data/season.json")); n = str(s["currentWeek"]); w = s["weeks"][n]
    games = w.get("games", []); probs = []
    upd = P(s["updated"]) if s.get("updated") else None
    if w.get("status") != "final":
        for g in games:
            ko = P(g["kickoff"])
            if now - ko > timedelta(minutes=45) and g.get("status") == "sealed":
                probs.append(f"Week {n}: {g['away']} at {g['home']} kicked off at {et(ko):%a %-I:%M %p} ET but was never locked")
        if games:
            thu = games[0]; tko = P(thu["kickoff"])
            if now - tko > timedelta(hours=5) and not w.get("thuDone") and not thu.get("winner"):
                probs.append(f"Week {n}: the Thursday final ({thu['away']} at {thu['home']}) never posted")
            mko = P(games[-1]["kickoff"])
            if now - mko > timedelta(hours=7):
                probs.append(f"Week {n}: Monday's game ended hours ago and the week was never scored")
        e = et(now)
        gap = 3 if e.weekday() in (0, 3, 6) else 8   # hourly on game days (Mon, Thu, Sun); three runs a day otherwise (Nov 12)
        if upd and 9 <= e.hour <= 23 and now - upd > timedelta(hours=gap):
            probs.append(f"Week {n}: no board update since {et(upd):%a %-I:%M %p} ET (the hourly refresh looks stalled)")
    else:
        e = et(now)
        # final week, and it's Tuesday 5 a.m. ET or later (or Wednesday on): the new-week run didn't land
        if (e.weekday() == 1 and e.hour >= 5) or e.weekday() in (2, 3):
            probs.append(f"Week {int(n) + 1} isn't up yet (the Tuesday new-week run didn't land)")
    for p in probs: print("PROBLEM:", p)
    if not probs: print("OK")

if __name__ == "__main__": main()
