#!/usr/bin/env python3
"""Mark payment rows as told to Garret so the NEEDS GARRET digest doesn't repeat them.
usage: python3 tools/mark_told.py ID [ID ...]   (ids as printed by score.py's NEEDS GARRET lines)"""
import json, os, sys
from datetime import datetime, timezone
P = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "data", "season.json")
ids = set(sys.argv[1:])
if not ids: sys.exit(__doc__)
s = json.load(open(P)); wk = s["weeks"][str(s["currentWeek"])]
today = datetime.now(timezone.utc).strftime("%Y-%m-%d"); n = 0
for x in wk.get("payments", []):
    if x["id"] in ids and not x.get("told"): x["told"] = today; n += 1
json.dump(s, open(P, "w"), indent=2, ensure_ascii=False)
print(f"marked {n} payment(s) told")
