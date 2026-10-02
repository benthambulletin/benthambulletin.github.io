#!/usr/bin/env python3
"""Live NFL scores for the current pool week, from ESPN's public scoreboard.

Run by .github/workflows/pool-live.yml every few minutes. Prints live.json to stdout,
or exits 3 when no game of the current week is inside its window (no need to publish).
Never guesses: a game ESPN doesn't list is left out.
"""
import json, os, sys, urllib.request
from datetime import datetime, timedelta, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
season = json.load(open(os.path.join(HERE, "..", "data", "season.json")))
wk = season["weeks"][str(season["currentWeek"])]
games = wk["games"]
now = datetime.now(timezone.utc)
force = "--force" in sys.argv

def P(s): return datetime.fromisoformat(s.replace("Z", "+00:00"))

# a game is "in window" from 20 minutes before kickoff to 5 hours after
active = [g for g in games if P(g["kickoff"]) - timedelta(minutes=20) <= now <= P(g["kickoff"]) + timedelta(hours=5)]
if not active and not force:
    sys.exit(3)

# ESPN dates are US Eastern calendar days
def et_day(dt): return (dt - timedelta(hours=4 if dt.month in range(3, 11) else 5)).strftime("%Y%m%d")
days = sorted({et_day(P(g["kickoff"])) for g in (games if force else active)})

events = []
for d in days:
    url = f"https://site.api.espn.com/apis/site/v2/sports/football/nfl/scoreboard?dates={d}"
    req = urllib.request.Request(url, headers={"User-Agent": "sunday-tax-pool/1.0"})
    with urllib.request.urlopen(req, timeout=20) as r:
        events += json.load(r).get("events", [])

def names(team):
    return {team.get(k, "") for k in ("shortDisplayName", "name", "displayName")} - {""}

out = {"updated": now.strftime("%Y-%m-%dT%H:%M:%SZ"), "week": season["currentWeek"], "games": {}}
for i, g in enumerate(games):
    for e in events:
        comp = e["competitions"][0]
        side = {c["homeAway"]: c for c in comp["competitors"]}
        if "home" not in side or "away" not in side: continue
        if g["home"] not in names(side["home"]["team"]) or g["away"] not in names(side["away"]["team"]): continue
        st = comp.get("status") or e.get("status") or {}
        typ = st.get("type", {})
        state = typ.get("state")                     # pre / in / post
        a, h = int(side["away"].get("score") or 0), int(side["home"].get("score") or 0)
        detail = typ.get("shortDetail") or typ.get("detail") or ""
        rec = {"state": state, "away": a, "home": h, "detail": detail}
        if state == "in":
            lead = f"{g['away']} {a}–{h}" if a > h else f"{g['home']} {h}–{a}" if h > a else f"Tied {a}–{h}"
            rec["line"] = f"{lead} · {detail}" if detail else lead
        if state == "post" and typ.get("completed", True):
            rec["winner"] = g["away"] if a > h else g["home"] if h > a else "TIE"
            rec["score"] = f"{max(a, h)}–{min(a, h)}"
            rec["line"] = f"Final · {rec['winner'] if rec['winner'] != 'TIE' else 'Tied'} {max(a, h)}–{min(a, h)}" + (" (OT)" if "OT" in detail else "")
        out["games"][str(i)] = rec
        break

print(json.dumps(out, ensure_ascii=False, indent=1))
