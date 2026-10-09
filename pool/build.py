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

# season badges: none right now (the badges are all weekly, plus the streak below)
season_badges = {}

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

def _iso(u):
    """whole seconds + Z, which every browser's Date.parse accepts (Safari balks at microseconds)"""
    from datetime import datetime, timezone
    try: return datetime.fromisoformat(u.replace("Z", "+00:00")).astimezone(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    except Exception: return u

# every build stamps the board, so a phone holding an older copy always picks up a hand edit (Oct 6: the
# mugshot went up without season.updated moving, and phones kept the old page)
from datetime import datetime as _dt, timezone as _tz
_BUILT = _dt.now(_tz.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
import hashlib as _hl
_TPLV = _hl.md5(open(f"{HERE}/template.html", "rb").read()).hexdigest()[:10]   # the page reloads itself when this changes
def make_page(k, w, archive=False):
    return {
        "name": season["name"], "season": season["season"], "formUrl": season["form"]["url"],
        "buyIn": w.get("buyIn", 0), "plannedBuyIn": season.get("plannedBuyIn", 5),
        "pot": w.get("pot", 0), "rollIn": w.get("rollIn", 0), "rollOut": w.get("rollOut", 0), "paidN": w.get("paidN", 0), "payBy": w.get("payBy"),
        "venmo": season.get("venmo"), "venmoUrl": season.get("venmoUrl"),
        "anyPaid": any(x.get("buyIn", 0) for x in season["weeks"].values()), "week": int(k), "status": w.get("status", "pre"),
        "updated": _iso(season.get("updated", "")) if archive else _BUILT, "games": w["games"],
        "tiebreakTotal": w.get("tiebreakTotal"), "tbUsed": w.get("tbUsed", False),
        "players": w.get("players", []), "weekWinners": w.get("weekWinners", []),
        "weekPayout": w.get("weekPayout", 0), "season_table": list(tot.values()),
        "trash": w.get("trash", []), "replies": w.get("replies", {}), "bot": _bot(w), "botTally": bot_tally, "qa": [x for x in w.get("asks", []) if x.get("a")], "column": w.get("column", ""), "columnHead": w.get("columnHead", ""), "displayNames": _dn(season),
        "seasonFrom": min([int(x) for x, ww in season["weeks"].items() if ww.get("status") == "final"] or [0]),
        "updates": w.get("updates", []), "decides": w.get("decides", []),
        "stats": w.get("stats"), "face": w.get("face"), "homer": homer, "house": season.get("house"),
        "seasonBadges": season_badges, "streak": streak, "awards": w.get("awards", []),
        "pastWeeks": past, "archive": archive, "tpl": _TPLV,
    }

def _dn(season):
    """Board names players chose; if two people chose the same one, both show their record names instead."""
    dn = dict(season.get("displayNames", {})); seen = {}
    for k, v in dn.items(): seen.setdefault(v.lower(), []).append(k)
    for v, ks in seen.items():
        if len(ks) > 1:
            for k in ks: dn.pop(k, None)
    return dn

tpl = open(f"{HERE}/template.html").read()
def render(page): return tpl.replace("/*DATA*/", json.dumps(page, ensure_ascii=False).replace("<", "\\u003c"))

# past weeks: every final week except the one on the board gets its own frozen page at /pool/weeks/<N>/
def _bot(w):
    """Beat the Bot weeks: Claude's public picks with reasons and the Lock of the Week."""
    if not w.get("bot"): return None
    hp = w.get("housePicks") or {}
    return {"picks": hp.get("picks", {}), "why": hp.get("why", {}), "lock": hp.get("lock"), "lockWhy": hp.get("lockWhy", "")}
# Beat the Bot tally: weeks each player finished with a better record than Claude (final bot weeks only)
bot_tally = {}
for k, w in season["weeks"].items():
    if w.get("status") != "final" or not w.get("bot"): continue
    hs = [p for p in w.get("players", []) if p.get("house")]
    if not hs: continue
    for p in w.get("players", []):
        if not p.get("house") and p["correct"] > hs[0]["correct"]: bot_tally[p["name"]] = bot_tally.get(p["name"], 0) + 1
past = sorted([int(k) for k, w in season["weeks"].items() if w.get("status") == "final" and k != n], reverse=True)
def _champ(k):
    w = season["weeks"][str(k)]; W = w.get("weekWinners", [])
    wp = next((p for p in w.get("players", []) if p["name"] in W), None)
    return {"week": k, "winners": W, "record": f"{wp['correct']}–{wp['missed']}" if wp else None,
            "tbUsed": w.get("tbUsed", False), "payout": w.get("weekPayout", 0) if w.get("buyIn", 0) else 0}
past = [_champ(k) for k in past]
for pw in past:
    k = str(pw["week"]); os.makedirs(f"{HERE}/weeks/{k}", exist_ok=True)
    open(f"{HERE}/weeks/{k}/index.html", "w").write(render(make_page(k, season["weeks"][k], archive=True)))

page = make_page(n, wk)
# guard: no tiebreaker number may be published while the Monday game is still sealed
from datetime import datetime as _D, timezone as _tz
if wk["games"] and _D.fromisoformat(wk["games"][-1]["kickoff"].replace("Z", "+00:00")) > _D.now(_tz.utc):
    leak = [p["name"] for p in page["players"] if p.get("tb") is not None]
    if leak: raise SystemExit(f"REFUSING TO BUILD: tiebreaker numbers present before Monday kickoff for {leak}")
open(f"{HERE}/index.html", "w").write(render(page))
json.dump(page, open(f"{HERE}/data/page.json", "w"), ensure_ascii=False)

# calendar: this week's pick deadlines (first kickoff, first Sunday kickoff), each with a reminder an hour before
from datetime import datetime, timezone
def _dt(iso): return datetime.fromisoformat(iso.replace("Z", "+00:00")).astimezone(timezone.utc)
games = wk["games"]
locks = []
if games:
    locks.append(games[0])
    sun = sorted([g for g in games[1:] if not g["when"].startswith("Thu")], key=lambda g: g["kickoff"])
    if sun: locks.append(sun[0])
now_utc = datetime.now(timezone.utc)
locks = [g for g in locks if _dt(g["kickoff"]) > now_utc]   # only deadlines still ahead
stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
ics = ["BEGIN:VCALENDAR", "VERSION:2.0", "PRODID:-//The Sunday Tax//Pool//EN", "CALSCALE:GREGORIAN", "METHOD:PUBLISH"]
for i, g in enumerate(locks):
    st = _dt(g["kickoff"])
    title = f"Sunday Tax: {g['away']} at {g['home']} locks — get your picks in"
    ics += ["BEGIN:VEVENT", f"UID:sundaytax-2026-w{n}-{g['away']}-{g['home']}@benthambulletin.github.io", f"DTSTAMP:{stamp}",
            "DTSTART:" + st.strftime("%Y%m%dT%H%M%SZ"), "DURATION:PT15M",
            f"SUMMARY:{title}", "URL:" + season["form"]["url"],
            "DESCRIPTION:Each game locks at its own kickoff. Picks: " + season["form"]["url"] + "\\nStandings: https://benthambulletin.github.io/pool/",
            "BEGIN:VALARM", "ACTION:DISPLAY", "DESCRIPTION:" + title, "TRIGGER:-PT1H", "END:VALARM", "END:VEVENT"]
ics.append("END:VCALENDAR")
open(f"{HERE}/week.ics", "w", newline="").write("\r\n".join(ics) + "\r\n")

print(f"built pool/index.html · week {n} · {page['status']} · {len(page['players'])} players · {len(past)} past weeks · {len(locks)} calendar locks")
