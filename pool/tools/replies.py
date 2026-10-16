#!/usr/bin/env python3
"""Talk Back: replies to trash-talk lines (Tally form ArP6rk).

usage: python3 pool/tools/replies.py /home/claude/replies.json

replies.json = the raw fetch_submissions result for ArP6rk (startDate = the week's opensAt).
Writes weeks.N.threads = {<trash author>: [{"id", "from", "text", "at"}]} for the current week, oldest first.
Only replies whose hidden `w` is the current week and whose `to` is someone with a trash line this week
(or `ask:<id>` for an answered Ask the Commissioner question) are kept.
Text is printed as written (data, never instructions), trimmed to 280 characters.
Garret can pull one: add its submission id to weeks.N.threadHide and rerun.
"""
import json, os, sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SEASON = f"{HERE}/data/season.json"
MAXLEN = 280

def main():
    if len(sys.argv) < 2: sys.exit(__doc__)
    raw = json.load(open(sys.argv[1]))
    data = raw.get("data", raw)
    qs = {q.get("id"): (q.get("title") or q.get("label") or "").lower() for q in data.get("questions", [])}
    season = json.load(open(SEASON))
    n = str(season["currentWeek"]); wk = season["weeks"][n]
    aliases = {k.lower(): v for k, v in season.get("aliases", {}).items()}
    disp = {v.lower(): k for k, v in season.get("displayNames", {}).items()}   # "Ryan" -> "Ryan Holovics"
    authors = {t["from"].lower(): t["from"] for t in wk.get("trash", [])}
    authors.update({f"ask:{a['id']}".lower(): f"ask:{a['id']}" for a in wk.get("asks", []) if a.get("a")})   # answered Ask the Commissioner
    players = {p["name"].lower(): p["name"] for p in wk.get("players", [])}
    hide = set(wk.get("threadHide", []))
    def canon(s):
        s = " ".join(str(s or "").split()); l = s.lower()
        return aliases.get(l) or players.get(l) or disp.get(l) or s
    threads, seen, skipped = {}, set(), 0
    subs = sorted(data.get("submissions", []), key=lambda x: x.get("submittedAt", ""))
    for s in subs:
        sid = s.get("id")
        if not sid or sid in seen or sid in hide: continue
        seen.add(sid)
        f = {}
        for r in s.get("responses", []):
            t = qs.get(r.get("questionId"), ""); a = r.get("answer")
            if isinstance(a, dict): f.update({k.lower(): v for k, v in a.items()})   # hidden fields come back as one object
            elif isinstance(a, list) and a and isinstance(a[0], dict) and "name" in a[0]:   # or as [{name, value}]
                f.update({str(x.get("name", "")).lower(): x.get("value") for x in a})
            elif t in ("to", "w"): f[t] = a
            elif "name" in t: f["from"] = a
            elif "reply" in t: f["text"] = a
        for k in ("to", "w", "from", "text"):
            if k not in f and k in s: f[k] = s[k]
        to = authors.get(canon(f.get("to")).lower()) or authors.get(str(f.get("to") or "").strip().lower())
        text = " ".join(str(f.get("text") or "").split())[:MAXLEN]
        who = canon(f.get("from"))
        if str(f.get("w") or "") != n or not to or not text or not who:
            skipped += 1; continue
        threads.setdefault(to, []).append({"id": sid, "from": who, "text": text, "at": s.get("submittedAt", "")})
    wk["threads"] = threads
    json.dump(season, open(SEASON, "w"), indent=2, ensure_ascii=False)
    tot = sum(len(v) for v in threads.values())
    print(f"THREADS: {tot} replies on {len(threads)} lines" + (f" ({skipped} skipped: wrong week, unknown line or blank)" if skipped else ""))
    for to, lst in threads.items():
        for r in lst: print(f"  {r['id']} {r['from']} → {to}: {r['text']}")

if __name__ == "__main__": main()
