#!/usr/bin/env python3
"""Render pool/index.html from data/season.json. Run after score.py or after loading a new week."""
import json, os
HERE = os.path.dirname(os.path.abspath(__file__))
season = json.load(open(f"{HERE}/data/season.json"))
n = str(season["currentWeek"])
wk = season["weeks"][n]

# season table: sum every FINAL week
tot = {}
for k, w in season["weeks"].items():
    if w.get("status") != "final": continue
    for p in w.get("players", []):
        if p.get("house"): continue
        t = tot.setdefault(p["name"], {"name": p["name"], "correct": 0, "missed": 0, "weeksWon": 0, "won": 0})
        t["correct"] += p["correct"]; t["missed"] += p["missed"]
    for name in w.get("weekWinners", []):
        t = tot.setdefault(name, {"name": name, "correct": 0, "missed": 0, "weeksWon": 0, "won": 0})
        t["weeksWon"] += 1; t["won"] += w.get("weekPayout", 0)

# homer split per person, over every game that is final in any week (Bills games / Jets games)
homer = {}
for k, w in season["weeks"].items():
    for p in w.get("players", []):
        hh = homer.setdefault(p["name"], {"bills": [0, 0], "jets": [0, 0]})
        for i, g in enumerate(w["games"]):
            wn = g.get("winner"); pk = (p.get("sheet") or {}).get(str(i))
            if not wn or wn == "TIE" or not pk: continue
            for team, key in (("Bills", "bills"), ("Jets", "jets")):
                if team in (g["away"], g["home"]): hh[key][0 if pk == wn else 1] += 1

# season badges and streaks
weeks_final = [w for k, w in sorted(season["weeks"].items(), key=lambda kv: int(kv[0])) if w.get("status") == "final"]
season_badges = {}
def sb(name, bid, note): season_badges.setdefault(name, []).append({"id": bid, "note": note})
if weeks_final:
    lasts, seconds, played = {}, {}, {}
    for w in weeks_final:
        realp = [p for p in w["players"] if not p.get("house")]
        for p in realp: played[p["name"]] = played.get(p["name"], 0) + 1
        if realp:
            lo = realp[-1]["correct"]
            for p in realp:
                if p["correct"] == lo: lasts[p["name"]] = lasts.get(p["name"], 0) + 1
            ranks = sorted({p["correct"] for p in realp}, reverse=True)
            if len(ranks) > 1:
                for p in realp:
                    if p["correct"] == ranks[1] and p["name"] not in w.get("weekWinners", []):
                        seconds[p["name"]] = seconds.get(p["name"], 0) + 1
    if lasts:
        m = max(lasts.values())
        for nme, c in lasts.items():
            if c == m: sb(nme, "cellar", f"last place {c} time{'s' if c > 1 else ''}")
    if len(weeks_final) >= 2:
        winners = {nme for w in weeks_final for nme in w.get("weekWinners", [])}
        cand = {nme: c for nme, c in seconds.items() if nme not in winners}
        if cand:
            m = max(cand.values())
            for nme, c in cand.items():
                if c == m and c >= 2: sb(nme, "bridesmaid", f"second place {c} times, no win")
        for nme, c in played.items():
            if c == len(weeks_final) and any(p["name"] == nme for p in wk.get("players", [])): sb(nme, "iron", "never missed a week")
# streak: consecutive correct picks across all weeks, in kickoff order, current week included
streak = {}
allweeks = [w for k, w in sorted(season["weeks"].items(), key=lambda kv: int(kv[0]))]
for w in allweeks:
    for p in w.get("players", []):
        if p.get("house"): continue
        cur = streak.get(p["name"], 0)
        for i, g in enumerate(w["games"]):
            wn = g.get("winner")
            if not wn or wn == "TIE": continue
            pk = (p.get("sheet") or {}).get(str(i))
            if pk is None: continue
            cur = cur + 1 if pk == wn else 0
        streak[p["name"]] = cur

page = {
    "name": season["name"], "season": season["season"], "formUrl": season["form"]["url"],
    "buyIn": season["buyIn"], "plannedBuyIn": season.get("plannedBuyIn", 5), "week": int(n), "status": wk.get("status", "pre"),
    "updated": season.get("updated", ""), "games": wk["games"],
    "tiebreakTotal": wk.get("tiebreakTotal"), "tbUsed": wk.get("tbUsed", False),
    "players": wk.get("players", []), "weekWinners": wk.get("weekWinners", []),
    "weekPayout": wk.get("weekPayout", 0), "season_table": list(tot.values()),
    "trash": wk.get("trash", []), "column": wk.get("column", ""),
    "updates": wk.get("updates", []), "decides": wk.get("decides", []),
    "stats": wk.get("stats"), "homer": homer, "house": season.get("house"),
    "seasonBadges": season_badges, "streak": streak, "awards": wk.get("awards", []),
}
tpl = open(f"{HERE}/template.html").read()
out = tpl.replace("/*DATA*/", json.dumps(page, ensure_ascii=False))
open(f"{HERE}/index.html", "w").write(out)
print(f"built pool/index.html · week {n} · {page['status']} · {len(page['players'])} players")
