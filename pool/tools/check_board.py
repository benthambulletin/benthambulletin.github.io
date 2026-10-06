#!/usr/bin/env python3
"""Look at the board the way a phone does and check it against ESPN.

Renders pool/index.html at 390px twice: with the current live.json and with the live feed
blocked (a phone that couldn't load it). Prints problems, exits 1 if any.
Usage: python3 pool/tools/check_board.py   (run from the repo root after build.py)
"""
import json, os, sys, urllib.request
from datetime import datetime, timezone
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
page = os.path.join(ROOT, "index.html")
pj = os.path.join(ROOT, "data", "page.json")
D = json.load(open(pj))
LIVE = "https://raw.githubusercontent.com/benthambulletin/benthambulletin.github.io/pool-live/live.json"
try:
    L = json.load(urllib.request.urlopen(LIVE + "?t=%d" % datetime.now().timestamp(), timeout=20))
except Exception as e:
    L = None; print("WARN live.json unreachable:", e)
lpath = "/tmp/_live_check.json"
if L: json.dump(L, open(lpath, "w"))

now = datetime.now(timezone.utc)
problems = []
espn_in = sum(1 for g in (L or {}).get("games", {}).values() if g.get("state") == "in") if L and L.get("week") == D["week"] else None

def look(with_live):
    with sync_playwright() as p:
        b = p.chromium.launch(); pg = b.new_page(viewport={"width": 390, "height": 800})
        errs = []; pg.on("pageerror", lambda e: errs.append(str(e)))
        if with_live and L:
            pg.route("**/live.json*", lambda r: r.fulfill(path=lpath, headers={"access-control-allow-origin": "*", "content-type": "application/json"}))
        else:
            pg.route("**/live.json*", lambda r: r.abort())
        pg.route("**/page.json*", lambda r: r.fulfill(path=pj, headers={"content-type": "application/json"}))
        pg.goto("file://" + page); pg.wait_for_timeout(2500)
        out = {"errs": errs, "hero": pg.inner_text("#nowL"), "sub": pg.inner_text("#nowS"), "body": pg.inner_text("body")}
        b.close(); return out

for mode in ([True, False] if L else [False]):
    o = look(mode); tag = "with live feed" if mode else "without live feed"
    if o["errs"]: problems.append(f"{tag}: script error {o['errs'][0]}")
    h = o["hero"]
    if "games live" in h:
        n = int(h.split()[0])
        if mode and espn_in is not None and n != espn_in:
            problems.append(f"{tag}: hero says {n} games live, ESPN has {espn_in} in progress")
        if not mode:
            recent = sum(1 for g in D["games"] if not g.get("winner") and 0 <= (now - datetime.fromisoformat(g["kickoff"].replace("Z", "+00:00"))).total_seconds() < 225 * 60)
            if n > recent: problems.append(f"{tag}: hero says {n} games live, only {recent} kicked off in the last 3h45m")
    # a game ESPN calls final must never read as live
    if mode and L:
        for k, g in L.get("games", {}).items():
            gm = D["games"][int(k)]
            if g.get("state") == "post" and g.get("winner") and g["winner"] != "TIE":
                if (gm["away"] + " at " + gm["home"]) in o["body"] and g["winner"] + " " + (g.get("score") or "") not in o["body"]:
                    problems.append(f"{tag}: {gm['away']} at {gm['home']} is final on ESPN ({g['winner']} {g.get('score')}) but the board doesn't show it")

# a sealed game must never show "no pick" (the board read a game as open before its sides were revealed)
for g in D["games"]:
    if g.get("status")=="sealed":
        for mode in ([True, False] if L else [False]):
            pass
_o = look(True) if L else None
if _o:
    for g in D["games"]:
        if g.get("status")=="sealed" and (g["away"]+"@"+g["home"]+" no pick") in _o["body"].replace("\n"," "):
            problems.append(f"with live feed: {g['away']} at {g['home']} is sealed but sheets show 'no pick'")
print("BOARD CHECK:", "clear" if not problems else "PROBLEMS")
for p in problems: print(" -", p)
sys.exit(1 if problems else 0)
