#!/usr/bin/env python3
"""Score the current week of The Sunday Tax.

usage: python3 score.py submissions.json [--venmo venmo.json] [--final]

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
- Paid weeks (wk.buyIn > 0): only players with a recorded $buyIn payment (ok or manual) can win the week, the crown,
  or the pot; everyone still plays and is ranked by record. Pot = buyIn x paid players (during the week, filed or not; at --final, paid sheets only — no sheet means refund).
  --venmo venmo.json = [{id, at, payer, amount, note, dkim}] written by the run from Gmail; payer and note never
  reach season.json (only id, at, amt, who, status). Matching is deterministic: note first, then payer.
"""
import json, sys, re, hashlib, unicodedata
from datetime import datetime, timezone

HERE = __import__("os").path.dirname(__import__("os").path.abspath(__file__))
SEASON = f"{HERE}/data/season.json"

def P(s): return datetime.fromisoformat(s.replace("Z", "+00:00"))
def now(): return datetime.now(timezone.utc)

def clean_text(t, cap=280):
    t = "".join(ch for ch in str(t) if unicodedata.category(ch)[0] != "C" or ch in "\n")
    t = t.strip()
    return t if len(t) <= cap else t[:cap - 1].rstrip() + "…"

def vhash(name):
    return hashlib.sha256(re.sub(r"\s+", " ", str(name).strip().lower()).encode()).hexdigest()[:16]

def record_payments(season, wk, items, known):
    """Add new Venmo payments to wk['payments']. known = {lowercase name or alias -> display name}."""
    pays = wk.setdefault("payments", [])
    # an unmatched payment gets matched again every run (the payer may have filed or been aliased since)
    retold = {x["id"]: x.get("told") for x in pays if x["status"] == "unmatched"}
    pays[:] = [x for x in pays if x["status"] != "unmatched"]
    seen = {x["id"] for x in pays}
    for ow in season["weeks"].values():   # a payment already booked to another week stays there
        if ow is not wk: seen |= {x["id"] for x in ow.get("payments", [])}
    buy = wk.get("buyIn", 0)
    vnames = season.get("venmoNames", {})
    opens = P(wk["opensAt"]) if wk.get("opensAt") else None
    payby = P(wk["payBy"]) if wk.get("payBy") else None
    firsts = {}
    for k, v in known.items():
        ks = re.sub(r"[^a-z0-9&' ]+", " ", k).split()
        if ks: firsts.setdefault(ks[0], set()).add(v)
    for it in sorted(items, key=lambda x: x.get("at", "")):
        if not it.get("id") or it["id"] in seen: continue
        seen.add(it["id"])
        row = {"id": it["id"], "at": it.get("at"), "amt": it.get("amount"), "who": None, "status": "unmatched", "told": None}
        try: amt = float(it.get("amount"))
        except Exception: amt = None
        at = P(it["at"]) if it.get("at") else None
        if it.get("dkim") is False:
            row["status"] = "odd"; pays.append(row); continue
        if opens and at and at < opens:
            row["status"] = "early"; pays.append(row); continue
        # 1) the note: whole-word names; exactly one person
        note = " " + re.sub(r"[^a-z0-9&' ]+", " ", str(it.get("note") or "").lower()) + " "
        norm = lambda k: " ".join(re.sub(r"[^a-z0-9&' ]+", " ", k).split())
        hits = {v for k, v in known.items() if norm(k) and f" {norm(k)} " in note}
        if not hits:
            hits = set().union(*[firsts[w] for w in note.split() if w in firsts and len(firsts[w]) == 1]) if note.strip() else set()
        who = None
        if len(hits) == 1: who = next(iter(hits))
        elif len(hits) > 1: row["status"] = "odd"
        # 2) the payer: confirmed Venmo names (hashed), then exact name, then a unique first name
        if who is None and row["status"] != "odd":
            payer = str(it.get("payer") or "").strip()
            h = vhash(payer) if payer else None
            if h and h in vnames: who = vnames[h]
            elif payer.lower() in known: who = known[payer.lower()]
            elif payer:
                f1 = re.sub(r"[^a-z0-9&']+", "", payer.split()[0].lower())
                if len(firsts.get(f1, ())) == 1: who = next(iter(firsts[f1]))
        row["who"] = who
        if who and row["status"] != "odd":
            if amt is None or abs(amt - buy) > 0.001: row["status"] = "odd"
            elif any((x["who"] or "").lower() == who.lower() and x["status"] in ("ok", "manual") for x in pays): row["status"] = "dup"
            elif payby and at and at > payby: row["status"] = "late"
            else: row["status"] = "ok"
        if row["status"] == "unmatched" and retold.get(row["id"]): row["told"] = retold[row["id"]]
        pays.append(row)
    pays.sort(key=lambda x: x.get("at") or "")
    return pays

def main():
    if len(sys.argv) < 2: sys.exit(__doc__)
    final = "--final" in sys.argv
    venmo = None
    if "--venmo" in sys.argv:
        venmo = json.load(open(sys.argv[sys.argv.index("--venmo") + 1]))
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
    merged = {}
    hname = ((season.get("house") or {}).get("name") or "Claude")
    for k, lst in by.items():
        disp = aliases.get(k, lst[-1]["raw"])
        if disp.lower() == hname.lower(): disp = disp + " (player)"   # the house name is reserved
        merged.setdefault(disp, []).extend(lst)                         # two spellings, one person: merge, don't overwrite
    for lst in merged.values(): lst.sort(key=lambda x: x["at"])
    by = merged

    # house entry (Claude): seeded random picks stored on the week; filed the moment the week opened
    house = season.get("house") or {}
    hp = dict(wk.get("housePicks") or {})
    if house.get("enabled") and not hp.get("picks"):
        import hashlib, random
        rng = random.Random(int(hashlib.sha256(f"sundaytax-2026-w{season['currentWeek']}".encode()).hexdigest(), 16))
        hp["picks"] = {str(i): rng.choice([g["away"], g["home"]]) for i, g in enumerate(games)}
        hp["tb"] = rng.randint(37, 52)
    if "housePicks" in wk:   # keep only the trash line on disk; the picks stay sealed
        wk["housePicks"] = {"trash": hp.get("trash", "")}
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
        tb, _ = pick_for(lst, q["tiebreak"], wk.get("tbLockAt") or mnf["kickoff"])  # tbLockAt: Week 4 only, see CLAUDE.md
        if tb in (None, "") and wk.get("tbLockAt"):
            # first sheet came in after the lock: their first tiebreaker stands, later changes don't
            tb, _ = pick_for(lst[:1], q["tiebreak"], mnf["kickoff"])
        try: tb = int(tb) if tb not in (None, "") else None
        except Exception: tb = None
        players.append({"name": name, "house": name == house_name, "correct": correct, "missed": missed, "void": void,
                        "remaining": remaining, "max": correct + remaining, "tb": tb,
                        "sheet": {str(k): v for k, v in sheet.items()},
                        "filedAt": lst[-1]["at"].isoformat(), "firstAt": lst[0]["at"].isoformat()})
        t = lst[-1]["r"].get(q["trash"])
        if t and str(t).strip(): trash.append({"from": name, "text": clean_text(t)})

    # ranks (ties share a rank), movement, alive/out/clinched
    players.sort(key=lambda p: (-p["correct"], p["missed"], p["name"]))
    rank = 0
    for i, p in enumerate(players):
        if i == 0 or (p["correct"], p["missed"]) != (players[i-1]["correct"], players[i-1]["missed"]): rank = i + 1
        p["rank"] = rank
        pr = prev_rank.get(p["name"])
        p["delta"] = (pr - rank) if pr else 0
    real = [p for p in players if not p.get("house")]
    for p in players:
        if p.get("house"): p["state"] = "house"   # set even when no one else has filed yet
    if real:
        lead = real[0]["correct"]
        best_other_max = lambda me: max([o["max"] for o in real if o is not me] or [0])
        for p in players:
            if p.get("house"): p["state"] = "house"
            elif p["correct"] > best_other_max(p): p["state"] = "clinched"
            elif p["max"] < lead: p["state"] = "out"
            else: p["state"] = "alive"

    # paid weeks: record payments, mark paid players, decide who can win
    buy = wk.get("buyIn", 0)
    if buy:
        known = {}
        for w in season["weeks"].values():
            for pl in w.get("players", []):
                if not pl.get("house"): known[pl["name"].lower()] = pl["name"]
        for k, v in aliases.items(): known[k] = v
        for p in real: known[p["name"].lower()] = p["name"]
        if venmo is not None: record_payments(season, wk, venmo, known)
        canon = lambda nm: aliases.get(str(nm or "").strip().lower(), str(nm or "").strip()).lower()
        paid = {canon(x["who"]) for x in wk.get("payments", []) if x["status"] in ("ok", "manual")}
        # season.autoPaid: the commissioner's own sheet (his Venmo is the pot) counts as paid the moment he files
        for nm in season.get("autoPaid", []):
            if any(canon(p["name"]) == canon(nm) for p in real): paid.add(canon(nm))
        for p in players: p["paid"] = (not p.get("house")) and canon(p["name"]) in paid
        eligible = [p for p in real if p["paid"]]
        if eligible:
            elead = max(p["correct"] for p in eligible)
            for p in real:
                if not p["paid"]: p["state"] = "alive"; continue
                others = [o["max"] for o in eligible if o is not p] or [0]
                p["state"] = "clinched" if p["correct"] > max(others) else ("out" if p["max"] < elead else "alive")
        else:
            for p in real: p["state"] = "alive"
    else:
        eligible = real; paid = set()
        for p in players: p.pop("paid", None)

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
    MIN_DECIDED = 3   # crown, coin and porta potty wait for three final games (Garret, Oct 2)
    n_decided = sum(1 for g in games if g.get("winner"))
    if house_p and n_decided >= MIN_DECIDED:
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
    if len(real) > 2 and n_decided >= MIN_DECIDED:
        worst = min(p["correct"] for p in real)
        if worst < max(p["correct"] for p in real):
            for p in real:
                if p["correct"] == worst: award(p, "cellar", "last place this week")
    wk["players"] = players
    wk["trash"] = trash
    # during the week the pot counts everyone who has paid, filed or not (people pay first, then file);
    # at --final it is paid sheets only — a payment with no sheet is refunded
    npaid = len(eligible) if final else len(paid)
    wk["pot"] = buy * npaid if buy else 0
    wk["paidN"] = npaid if buy else 0
    wk["decides"] = decides[:4]
    wk["weekWinners"], wk["weekPayout"], wk["tbUsed"] = [], 0, False

    decided = sum(1 for g in games if g.get("winner"))
    if final:
        if decided < len(games): sys.exit(f"--final but only {decided}/{len(games)} games have a winner")
        if buy and wk.get("payments") is not None:
            canon = lambda nm: aliases.get(str(nm or "").strip().lower(), str(nm or "").strip()).lower()
            sheets = {canon(p["name"]) for p in real}
            for x in wk["payments"]:
                if x["status"] == "ok" and canon(x["who"]) not in sheets: x["status"] = "nosheet"
        if eligible:
            best = max(p["correct"] for p in eligible)
            lead = [p for p in eligible if p["correct"] == best]
            if len(lead) > 1 and buy and wk.get("tiebreakTotal") is None:
                sys.exit("--final: paid leaders are tied and tiebreakTotal is not set")
            if len(lead) > 1 and wk.get("tiebreakTotal") is not None:
                Tt = wk["tiebreakTotal"]
                for p in lead: p["_d"] = abs(p["tb"] - Tt) if p["tb"] is not None else 10**9
                m = min(p["_d"] for p in lead)
                near = [p for p in lead if p["_d"] == m]
                if len(near) < len(lead): lead, wk["tbUsed"] = near, True
                for p in players: p.pop("_d", None)
            wk["weekWinners"] = [p["name"] for p in lead]
            wk["weekPayout"] = int(wk["pot"] * 100 / len(lead)) / 100
            for p in lead: award(p, "crown", "won the week" + (" on the tiebreaker" if wk["tbUsed"] else ""))
            # the week's winner ranks first on the final board; everyone else keeps record order behind them
            W = set(wk["weekWinners"])
            players.sort(key=lambda p: (p["name"] not in W, -p["correct"], p["missed"], p["name"]))
            rank = 0
            for i, p in enumerate(players):
                key = (p["name"] in W, p["correct"], p["missed"])
                prev = (players[i-1]["name"] in W, players[i-1]["correct"], players[i-1]["missed"]) if i else None
                if p["name"] in W: rank = 1
                elif key != prev: rank = i + 1
                p["rank"] = rank
        wk["status"] = "final"
    else:
        wk["status"] = "live" if (decided or any(g.get("status") != "sealed" for g in wk["games"])) else "pre"
        if decided >= MIN_DECIDED and eligible:
            best = max(p["correct"] for p in eligible)
            if best > 0:
                for p in eligible:
                    if p["correct"] == best: award(p, "crown", "leading the week")

    # ticker: one line whenever the decided count changes (or the week finalizes)
    wk.setdefault("updates", [])
    stamp = T.isoformat()
    if real and (decided != prev_decided or final):
        pool_ = eligible if (buy and eligible) else real
        top = [p for p in pool_ if p["correct"] == pool_[0]["correct"]]
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
    # sealed: tiebreaker guesses never leave the script before Monday night kicks off
    if P(mnf["kickoff"]) > T:
        for p in players: p["tb"] = None
    season["updated"] = stamp
    json.dump(season, open(SEASON, "w"), indent=2, ensure_ascii=False)

    print(f"Week {season['currentWeek']} · {wk['status']} · {decided}/{len(games)} decided · {len(players)} entries")
    for p in players: print(f"  {p['rank']:>2} {p['name']:<14}{p['correct']:>2}-{p['missed']:<3} left={p['remaining']:<2} max={p['max']:<2} {p['state']:<8} tb={p['tb']}")
    if decides: print("DECIDES:", *[f"{games[d['game']]['away']}@{games[d['game']]['home']}: {d['away']} vs {d['home']}" for d in decides], sep="\n  ")
    if final: print("WINNER:", " & ".join(wk["weekWinners"]) or "none (nobody paid)", f"${wk['weekPayout']:g}" if buy else "", "(tiebreaker)" if wk["tbUsed"] else "")
    if buy:
        from collections import Counter
        pays = wk.get("payments", [])
        c = Counter(x["status"] for x in pays)
        print(f"PAY: pot ${wk['pot']:g} · {wk['paidN']} paid · " + ", ".join(f"{k} {v}" for k, v in sorted(c.items())))
        need = [x for x in pays if x["status"] in ("odd", "unmatched", "dup", "late", "early", "nosheet") and not x.get("told")]
        for x in need: print(f"  NEEDS GARRET: {x['status']} id={x['id']} who={x['who']} amt={x['amt']}")
        if final:
            for x in pays:
                if x["status"] in ("late", "nosheet", "dup"): print(f"  REFUND: {x['status']} who={x['who']} amt={x['amt']} id={x['id']}")
                elif x["status"] in ("unmatched", "odd", "early"): print(f"  UNRESOLVED: {x['status']} who={x['who']} amt={x['amt']} id={x['id']}")
    if trash: print("TRASH:", *[f"{t['from']}: {t['text']}" for t in trash], sep="\n  ")

if __name__ == "__main__": main()
