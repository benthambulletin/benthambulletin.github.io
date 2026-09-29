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
        t = tot.setdefault(p["name"], {"name": p["name"], "correct": 0, "missed": 0, "weeksWon": 0, "won": 0})
        t["correct"] += p["correct"]; t["missed"] += p["missed"]
    for name in w.get("weekWinners", []):
        t = tot.setdefault(name, {"name": name, "correct": 0, "missed": 0, "weeksWon": 0, "won": 0})
        t["weeksWon"] += 1; t["won"] += w.get("weekPayout", 0)

page = {
    "name": season["name"], "season": season["season"], "formUrl": season["form"]["url"],
    "buyIn": season["buyIn"], "plannedBuyIn": season.get("plannedBuyIn", 5), "week": int(n), "status": wk.get("status", "pre"),
    "updated": season.get("updated", ""), "games": wk["games"],
    "tiebreakTotal": wk.get("tiebreakTotal"), "tbUsed": wk.get("tbUsed", False),
    "players": wk.get("players", []), "weekWinners": wk.get("weekWinners", []),
    "weekPayout": wk.get("weekPayout", 0), "season_table": list(tot.values()),
    "trash": wk.get("trash", []), "column": wk.get("column", ""),
}
tpl = open(f"{HERE}/template.html").read()
out = tpl.replace("/*DATA*/", json.dumps(page, ensure_ascii=False))
open(f"{HERE}/index.html", "w").write(out)
print(f"built pool/index.html · week {n} · {page['status']} · {len(page['players'])} players")
