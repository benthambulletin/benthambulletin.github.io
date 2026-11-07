#!/usr/bin/env python3
"""Column fodder (Garret, Nov 7: "freshen the column"). Read-only; prints material for S6, never for the board.

Only public facts: finished weeks, and this week's games that have kicked off (score.py keeps unplayed picks out
of `sheet`). Prints:
  RECENT BITS   the last columns' heads and openings — don't reuse their jokes, quotes or callbacks
  SEASON        best and worst season records
  RUNS          players finishing in the top or bottom three of the room two or more weeks running
  RIVALS        head-to-head (better weekly record) between season.rivals pairs
  LINE          this week's decided games: who had the underdog that won, who had the favorite that lost
"""
import json, os
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
s = json.load(open(f"{HERE}/data/season.json"))
n = s["currentWeek"]; W = s["weeks"]
finals = sorted([int(k) for k, w in W.items() if w.get("status") == "final"])

print("RECENT BITS (don't repeat these):")
for c in s.get("columnLog", [])[-6:]:
    print(f"  W{c['week']} {c['at'][:16]}  {c.get('head','')}: {c['text'][:160]}…")

tot = {}
for k in finals:
    for p in W[str(k)].get("players", []):
        if p.get("house"): continue
        t = tot.setdefault(p["name"], [0, 0]); t[0] += p["correct"]; t[1] += p["missed"]
rows = sorted(tot.items(), key=lambda kv: -kv[1][0] / max(1, sum(kv[1])))
print("SEASON (finished weeks):", " · ".join(f"{k} {a}–{b}" for k, (a, b) in rows[:3]), "| bottom:", " · ".join(f"{k} {a}–{b}" for k, (a, b) in rows[-3:]))

place = {}   # week -> {name: 'top'|'bottom'}
for k in finals:
    ps = [p for p in W[str(k)].get("players", []) if not p.get("house")]
    if len(ps) < 6: continue
    ps.sort(key=lambda p: (-p["correct"], p["missed"]))
    cut_top = ps[2]["correct"]; cut_bot = ps[-3]["correct"]
    place[k] = {p["name"]: ("top" if p["correct"] >= cut_top else "bottom" if p["correct"] <= cut_bot else "mid") for p in ps}
runs = []
for name in tot:
    for kind in ("top", "bottom"):
        r = 0
        for k in reversed(finals):
            if place.get(k, {}).get(name) == kind: r += 1
            else: break
        if r >= 2: runs.append(f"{name} {kind} three {r} weeks running")
print("RUNS:", "; ".join(runs) or "none")

rivals = s.get("rivals", [])
out = []
for a, b in rivals:
    wa = wb = tie = 0
    for k in finals:
        pp = {p["name"]: p for p in W[str(k)].get("players", [])}
        if a in pp and b in pp:
            x, y = pp[a]["correct"], pp[b]["correct"]
            if x > y: wa += 1
            elif y > x: wb += 1
            else: tie += 1
    if wa + wb + tie: out.append(f"{a} {wa}–{wb} {b}" + (f" ({tie} even)" if tie else ""))
print("RIVALS:", "; ".join(out) or "none set (season.rivals)")

w = W[str(n)]; lines = []
for i, g in enumerate(w.get("games", [])):
    win, fav = g.get("winner"), g.get("fav")
    if not win or win == "TIE" or not fav: continue
    dog_won = win != fav
    who = [p["name"] for p in w.get("players", []) if (p.get("sheet") or {}).get(str(i)) == win]
    if dog_won:
        lines.append(f"{g['away']} at {g['home']}: underdog {win} won ({g.get('line','')}) — had them: {', '.join(who) or 'nobody'}")
print("LINE (this week):", *(lines or ["no underdog wins yet"]), sep="\n  ")
