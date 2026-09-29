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
"""
import json, sys
from datetime import datetime, timezone

HERE = __import__("os").path.dirname(__import__("os").path.abspath(__file__))
SEASON = f"{HERE}/data/season.json"

def P(s): return datetime.fromisoformat(s.replace("Z", "+00:00"))

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

    # group submissions by normalized name, oldest first
    by = {}
    for s in raw["data"]["submissions"] if "data" in raw else raw["submissions"]:
        if not s.get("isCompleted", True): continue
        if wk.get("opensAt") and P(s["submittedAt"]) < P(wk["opensAt"]): continue  # earlier week's sheet
        resp = {r["questionId"]: r["answer"] for r in s["responses"]}
        rawname = str(resp.get(q["name"], "")).strip()
        if not rawname: continue
        key = rawname.lower()
        by.setdefault(key, []).append({"at": P(s["submittedAt"]), "r": resp, "raw": rawname})
    for lst in by.values(): lst.sort(key=lambda x: x["at"])
    # one display name per person: the alias if set, else how they spelled it most recently
    by = {aliases.get(k, lst[-1]["raw"]): lst for k, lst in by.items()}

    def pick_for(lst, qid, kickoff):
        valid = [x for x in lst if x["at"] < P(kickoff)]
        if not valid: return None, True
        a = valid[-1]["r"].get(qid)
        if isinstance(a, list): a = a[0] if a else None
        return a, False

    mnf = games[-1]
    players, trash = [], []
    for g in games: g["hits"], g["misses"] = [], []
    for name, lst in by.items():
        correct = missed = 0
        for i, g in enumerate(games):
            pick, void = pick_for(lst, q["games"][i], g["kickoff"])
            w = g.get("winner")
            if void or not pick or not w or w == "TIE": continue
            if pick == w: correct += 1; g["hits"].append(name)
            else: missed += 1; g["misses"].append(name)
        tb, _ = pick_for(lst, q["tiebreak"], mnf["kickoff"])
        try: tb = int(tb) if tb not in (None, "") else None
        except Exception: tb = None
        players.append({"name": name, "correct": correct, "missed": missed, "tb": tb})
        t = lst[-1]["r"].get(q["trash"])
        if t and str(t).strip(): trash.append({"from": name, "text": str(t).strip()})

    wk["players"] = sorted(players, key=lambda p: (-p["correct"], p["missed"], p["name"]))
    wk["trash"] = trash
    wk["pot"] = season["buyIn"] * len(players)
    wk["weekWinners"], wk["weekPayout"], wk["tbUsed"] = [], 0, False

    scored = sum(1 for g in games if g.get("winner"))
    if final:
        if scored < len(games): sys.exit(f"--final but only {scored}/{len(games)} games have a winner")
        if players:
            best = max(p["correct"] for p in players)
            lead = [p for p in players if p["correct"] == best]
            if len(lead) > 1 and wk.get("tiebreakTotal") is not None:
                T = wk["tiebreakTotal"]
                for p in lead: p["_d"] = abs(p["tb"] - T) if p["tb"] is not None else 10**9
                m = min(p["_d"] for p in lead)
                near = [p for p in lead if p["_d"] == m]
                if len(near) < len(lead): lead, wk["tbUsed"] = near, True
                for p in players: p.pop("_d", None)
            wk["weekWinners"] = [p["name"] for p in lead]
            wk["weekPayout"] = wk["pot"] / len(lead)
        wk["status"] = "final"
    else:
        wk["status"] = "live" if scored else "pre"

    season["updated"] = datetime.now(timezone.utc).isoformat()
    json.dump(season, open(SEASON, "w"), indent=2, ensure_ascii=False)

    print(f"Week {season['currentWeek']} · {wk['status']} · {scored}/{len(games)} games decided · {len(players)} entries · pot ${wk['pot']}")
    for p in wk["players"]: print(f"  {p['name']:<14}{p['correct']:>2}-{p['missed']:<3} tb={p['tb']}")
    if final: print("WINNER:", " & ".join(wk["weekWinners"]), f"${wk['weekPayout']:g}", "(tiebreaker)" if wk["tbUsed"] else "")
    if trash: print("TRASH:", *[f"{t['from']}: {t['text']}" for t in trash], sep="\n  ")

if __name__ == "__main__": main()
