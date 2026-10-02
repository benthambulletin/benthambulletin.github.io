#!/usr/bin/env python3
"""Score the current week of The Sunday Tax.

usage: python3 score.py submissions.json [--final]

submissions.json = the raw result of Tally fetch_submissions for the form,
saved verbatim (the object with "questions" and "submissions").
Reads/writes data/season.json. Prints a plain summary.

Rules (fixed, do not reinterpret):
- A person's latest submission BEFORE each game's kickoff is what counts for that game.
- Submitted after a game started -> that game is void for them, the rest count.
- A tied game counts for nobody.
- Week winner = most correct. Tie -> closest to the MNF combined total. Still tied -> split.
- Blank tiebreaker = worst possible guess.
- Submissions dated before the week's opensAt are ignored (they were for an earlier slate).
- Names: trimmed, case-insensitive, then mapped through season.aliases (lowercase key -> display name).
- Picks are only written to season.json for games that have kicked off. Future picks never leave this script.
"""
import json, sys
from datetime import datetime, timezone

HERE = __import__("os").path.dirname(__import__("os").path.abspath(__file__))
SEASON = f"{HERE}/data/season.json"

def P(s): return datetime.fromisoformat(s.replace("Z", "+00:00"))
def now(): return datetime.now(timezone.utc)

def main():
    if len(sys.argv) < 2: sys.exit(__doc__)
    final = "--final" in sys.argv
    raw = json.load(open(sys.argv[1]))
    season = json.load(open(SEASON))
    wk = season["weeks"][str(season["currentWeek"])]
    q = season["form"]["questions"]
    games = wk["games"]
    if len(games) != len(q["games"]):
        sys.exit(f"season.json has {len(games)} games but the form has {len(q['games'])} game questions")
    aliases = {k.lower(): v for k, v in season.get("aliases", {}).items()}
    T = now()

    # what the page showed before this run, for movement arrows and the ticker
    prev_rank = {p["name"]: p.get("rank") for p in wk.get("players", [])}
    prev_decided = wk.get("decidedAtLastRun", 0)   # winners get written before we run, so remember our own count

    # group submissions by normalized name, oldest first
    by = {}
    subs = raw["data"]["submissions"] if "data" in raw else raw["submissions"]
    for s in subs:
        if not s.get("isCompleted", True): continue
        if wk.get("opensAt") and P(s["submittedAt"]) < P(wk["opensAt"]): continue  # earlier week's sheet
        resp = {r["questionId"]: r["answer"] for r in s["responses"]}
        rawname = str(resp.get(q["name"], "")).strip()
        if not rawname: continue
        by.setdefault(rawname.lower(), []).append({"at": P(s["submittedAt"]), "r": resp, "raw": rawname})
    for lst in by.values(): lst.sort(key=lambda x: x["at"])
    by = {aliases.get(k, lst[-1]["raw"]): lst for k, lst in by.items()}

    # house entry (Claude): seeded random picks stored on the week; filed the moment the week opened
    house = season.get("house") or {}
    hp = wk.get("housePicks")
    house_name = None
    if house.get("enabled") and hp and hp.get("picks"):
        house_name = house.get("name", "Claude")
        resp = {q["games"][int(i)]: [t] for i, t in hp["picks"].items() if int(i) < len(q["games"])}
        resp[q["tiebreak"]] = hp.get("tb")
        if hp.get("trash"): resp[q["trash"]] = hp["trash"]
        by[house_name] = [{"at": P(wk.get("opensAt", "2026-01-01T00:00:00Z")), "r": resp, "raw": house_name}]

    def pick_for(lst, qid, kickoff):
        valid = [x for x in lst if x["at"] < P(kickoff)]
        if not valid: return None, True
        a = valid[-1]["r"].get(qid)
        if isinstance(a, list): a = a[0] if a else None
        return a, False

    mnf = games[-1]
    players, trash = [], []
    for g in games:
        g["hits"], g["misses"] = [], []
        started = P(g["kickoff"]) <= T
        g["status"] = "final" if g.get("winner") else ("live" if started else "sealed")
        g["sides"] = {g["away"]: [], g["home"]: []} if started else None

    for name, lst in by.items():
        correct = missed = void = 0
        remaining = 0
        sheet = {}   # only games that have kicked off
        for i, g in enumerate(games):
            started = P(g["kickoff"]) <= T
            pick, isvoid = pick_for(lst, q["games"][i], g["kickoff"])
            w = g.get("winner")
            if started:
                if isvoid or not pick:
                    void += 1; sheet[i] = None
                else:
                    sheet[i] = pick
                    if pick in g["sides"]: g["sides"][pick].append(name)
            if not w:
                # still to be decided; counts toward max unless void
                if not (started and (isvoid or not pick)): remaining += 1
                continue
            if w == "TIE" or isvoid or not pick: continue
            if pick == w: correct += 1; g["hits"].append(name)
            else: missed += 1; g["misses"].append(name)
        tb, _ = pick_for(lst, q["tiebreak"], mnf["kickoff"])
        try: tb = int(tb) if tb not in (None, "") else None
        except Exception: tb = None
        players.append({"name": name, "house": name == house_name, "correct": correct, "missed": missed, "void": void,
                        "remaining": remaining, "max": correct + remaining, "tb": tb,
                        "sheet": {str(k): v for k, v in sheet.items()},
                        "filedAt": lst[-1]["at"].isoformat(), "firstAt": lst[0]["at"].isoformat()})
        t = lst[-1]["r"].get(q["trash"])
        if t and str(t).strip(): trash.append({"from": name, "text": str(t).strip()})

    # ranks (ties share a rank), movement, alive/out/clinched
    players.sort(key=lambda p: (-p["correct"], p["missed"], p["name"]))
    rank = 0
    for i, p in enumerate(players):
        if i == 0 or (p["correct"], p["missed"]) != (players[i-1]["correct"], players[i-1]["missed"]): rank = i + 1
        p["rank"] = rank
        pr = prev_rank.get(p["name"])
        p["delta"] = (pr - rank) if pr else 0
    real = [p for p in players if not p.get("house")]
    if real:
        lead = real[0]["correct"]
        best_other_max = lambda me: max([o["max"] for o in real if o is not me] or [0])
        for p in players:
            if p.get("house"): p["state"] = "house"
            elif p["correct"] > best_other_max(p): p["state"] = "clinched"
            elif p["max"] < lead: p["state"] = "out"
            else: p["state"] = "alive"

    # what decides it: remaining games where the contenders split
    decides = []
    contenders = [p for p in players if p.get("state") not in ("out", "house")]
    for i, g in enumerate(games):
        if g.get("winner") or not g["sides"]: continue   # sealed games say nothing
        a = [n for n in g["sides"][g["away"]] if n in {c["name"] for c in contenders}]
        h = [n for n in g["sides"][g["home"]] if n in {c["name"] for c in contenders}]
        if a and h: decides.append({"game": i, "away": a, "home": h})
    decides.sort(key=lambda d: -min(len(d["away"]), len(d["home"])))

    # --- by the numbers (only over games that have kicked off; sealed games say nothing)
    stats = {"games": {}, "upsets": 0, "decided": 0, "best": None, "worst": None, "bills": None, "jets": None}
    for i, g in enumerate(games):
        if not g["sides"]: continue
        a, h = g["sides"][g["away"]], g["sides"][g["home"]]
        ra = [n for n in a if n != house_name]; rh = [n for n in h if n != house_name]
        maj, mino = (g["away"], g["home"]) if len(ra) >= len(rh) else (g["home"], g["away"])
        gs = {"away": len(ra), "home": len(rh), "minority": mino, "minorityWho": (rh if mino == g["home"] else ra)}
        w = g.get("winner")
        if w and w != "TIE":
            stats["decided"] += 1
            gs["upset"] = (w == mino and len(ra) != len(rh))
            if gs["upset"]: stats["upsets"] += 1
            right = [n for n in g["hits"] if n != house_name]
            gs["rightN"] = len(right)
            cand = {"game": i, "n": len(right), "who": right}
            if len(right) and (stats["best"] is None or len(right) < stats["best"]["n"]): stats["best"] = cand
            if stats["worst"] is None or len(right) < stats["worst"]["n"]: stats["worst"] = cand
            for team, key in (("Bills", "bills"), ("Jets", "jets")):
                if team in (g["away"], g["home"]):
                    stats[key] = {"game": i, "right": len(right), "wrong": len([n for n in g["misses"] if n != house_name]), "won": w == team}
        stats["games"][str(i)] = gs
    wk["stats"] = stats

    # --- weekly badges (only from games that have kicked off)
    real_names = {p["name"] for p in real}
    house_p = next((p for p in players if p.get("house")), None)
    for p in players: p["badges"] = []
    def award(p, bid, note="", n=None):
        for b in p["badges"]:
            if b["id"] == bid:
                b["n"] = (b.get("n") or 1) + 1
                if note: b["note"] = (b.get("note", "") + "; " + note).strip("; ")
                return
        b = {"id": bid, "note": note}
        if n: b["n"] = n
        p["badges"].append(b)
    byname = {p["name"]: p for p in players}
    # lone wolf, homer tax
    for i, g in enumerate(games):
        w = g.get("winner")
        if not w or w == "TIE": continue
        right = [n for n in g["hits"] if n in real_names]
        if len(right) == 1 and len(real) > 2:
            award(byname[right[0]], "wolf", f"only one with the {w}")
        for team in ("Bills", "Jets"):
            if team in (g["away"], g["home"]):
                for n in g["hits"] + g["misses"]:
                    if n not in real_names: continue
                    pk = byname[n]["sheet"].get(str(i))
                    if pk == team and w != team: award(byname[n], "homer", f"took the {team}, who lost")
    # the coin: currently behind Claude
    if house_p and sum(1 for g in games if g.get("winner")):
        for p in real:
            if p["correct"] < house_p["correct"]: award(p, "coin", f"behind Claude, {p['correct']}–{house_p['correct']}")
    # dead: mathematically out of the week
    for p in real:
        if p["state"] == "out": award(p, "dead", "mathematically out")
    # buzzer beater: first sheet inside the last hour before Thursday kickoff
    if real:
        tnf = P(games[0]["kickoff"])
        for p in real:
            dt = (tnf - P(p.get("firstAt") or p["filedAt"])).total_seconds()
            if 0 <= dt <= 3600: award(p, "buzzer", "filed inside the last hour before Thursday kickoff")
    # porta potty: last place this week, once games have been decided
    if len(real) > 2 and sum(1 for g in games if g.get("winner")):
        worst = min(p["correct"] for p in real)
        if worst < max(p["correct"] for p in real):
            for p in real:
                if p["correct"] == worst: award(p, "cellar", "last place this week")
    wk["players"] = players
    wk["trash"] = trash
    wk["pot"] = season["buyIn"] * len(real)
    wk["decides"] = decides[:4]
    wk["weekWinners"], wk["weekPayout"], wk["tbUsed"] = [], 0, False

    decided = sum(1 for g in games if g.get("winner"))
    if final:
        if decided < len(games): sys.exit(f"--final but only {decided}/{len(games)} games have a winner")
        if real:
            best = max(p["correct"] for p in real)
            lead = [p for p in real if p["correct"] == best]
            if len(lead) > 1 and wk.get("tiebreakTotal") is not None:
                Tt = wk["tiebreakTotal"]
                for p in lead: p["_d"] = abs(p["tb"] - Tt) if p["tb"] is not None else 10**9
                m = min(p["_d"] for p in lead)
                near = [p for p in lead if p["_d"] == m]
                if len(near) < len(lead): lead, wk["tbUsed"] = near, True
                for p in players: p.pop("_d", None)
            wk["weekWinners"] = [p["name"] for p in lead]
            wk["weekPayout"] = wk["pot"] / len(lead)
            for p in lead: award(p, "crown", "won the week" + (" on the tiebreaker" if wk["tbUsed"] else ""))
        wk["status"] = "final"
    else:
        wk["status"] = "live" if (decided or any(g.get("status") != "sealed" for g in wk["games"])) else "pre"
        if decided and real:
            best = max(p["correct"] for p in real)
            if best > 0:
                for p in real:
                    if p["correct"] == best: award(p, "crown", "leading the week")

    # ticker: one line whenever the decided count changes (or the week finalizes)
    wk.setdefault("updates", [])
    stamp = T.isoformat()
    if real and (decided != prev_decided or final):
        top = [p for p in real if p["correct"] == real[0]["correct"]]
        rec = f"{top[0]['correct']}–{top[0]['missed']}"
        if final:
            w = wk['weekWinners']
            note = f"Final: {' & '.join(w)} take{'s' if len(w)==1 else ''} Week {season['currentWeek']}" + (" on the tiebreaker." if wk["tbUsed"] else ".")
        else:
            if len(top) == 1: lead_txt = f"{top[0]['name']} leads at {rec}"
            elif len(top) == 2: lead_txt = f"{top[0]['name']} and {top[1]['name']} tied at {rec}"
            else: lead_txt = f"{len(top)} tied at {rec}"
            note = f"{decided} of {len(games)} final. {lead_txt}."
            already_out = set(wk.get("outAtLastRun", []))
            new_out = [p["name"] for p in real if p["state"] == "out" and p["name"] not in already_out]
            if new_out: note += f" Out of it: {', '.join(new_out)}."
            clinched = [p["name"] for p in real if p["state"] == "clinched"]
            if clinched: note += f" {clinched[0]} has clinched."
        wk["updates"].append({"at": stamp, "note": note})
        wk["updates"] = wk["updates"][-12:]

    wk["decidedAtLastRun"] = decided
    wk["outAtLastRun"] = [p["name"] for p in players if p.get("state") == "out"]
    season["updated"] = stamp
    json.dump(season, open(SEASON, "w"), indent=2, ensure_ascii=False)

    print(f"Week {season['currentWeek']} · {wk['status']} · {decided}/{len(games)} decided · {len(players)} entries")
    for p in players: print(f"  {p['rank']:>2} {p['name']:<14}{p['correct']:>2}-{p['missed']:<3} left={p['remaining']:<2} max={p['max']:<2} {p['state']:<8} tb={p['tb']}")
    if decides: print("DECIDES:", *[f"{games[d['game']]['away']}@{games[d['game']]['home']}: {d['away']} vs {d['home']}" for d in decides], sep="\n  ")
    if final: print("WINNER:", " & ".join(wk["weekWinners"]), f"${wk['weekPayout']:g}" if season["buyIn"] else "", "(tiebreaker)" if wk["tbUsed"] else "")
    if trash: print("TRASH:", *[f"{t['from']}: {t['text']}" for t in trash], sep="\n  ")

if __name__ == "__main__": main()
