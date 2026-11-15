#!/usr/bin/env python3
"""Gate for the Porta Potty board. Usage: python3 deals/tools/validate.py [new or changed item id ...]
Checks the shape of every item in deals/board.json, and holds the ids named on the command
line to the full rules in CHECK.md (evidence, second check, the 10% rule for a "buy").
Prints OK, or the list of failures and exits 1. Run it before every commit of board.json."""
import json, re, sys
from pathlib import Path

b = json.loads((Path(__file__).resolve().parents[1] / "board.json").read_text())
strict, bad = set(sys.argv[1:]), []
words = lambda t: len(str(t or "").split())
items = b.get("items", [])
ids = [i.get("id") for i in items]
if len(ids) != len(set(ids)): bad.append("duplicate item ids")
if len(items) > 80: bad.append("more than 80 items")
if set(ids) & {s.get("id") for s in b.get("skipped", [])}: bad.append("an id is in both items and skipped")
for lst in ("claimed", "queued", "skipped"):
    for c in b.get(lst, []):
        if c.get("link") and not re.match(r"https?://[^\s?]+$", c["link"]): bad.append(f"{lst} {c.get('id')}: link is not a clean http link")
        if set(c) - {"id", "link", "at", "quiet"}: bad.append(f"{lst} {c.get('id')}: unexpected fields")
missing = strict - set(ids)
if missing: bad.append("not in items: " + ", ".join(sorted(missing)))
for i in items:
    e = lambda m: bad.append(f"{i.get('id')}: {m}")
    v = i.get("verdict")
    if v not in ("buy", "wait", "shit"): e("verdict must be buy, wait or shit")
    if words(i.get("headline")) == 0 or words(i.get("headline")) > 14: e("headline must be 1 to 14 words")
    rs = i.get("reasons") or []
    if not 1 <= len(rs) <= 3: e("needs 1 to 3 reasons")
    for r in rs:
        if words(r) > 12: e(f"reason over 12 words: {r}")
    if words(i.get("instead")) > 18: e("instead over 18 words")
    if words(i.get("product")) == 0 or words(i.get("product")) > 10: e("product must be 1 to 10 words")
    if v in ("wait", "shit") and not i.get("instead"): e("wait/shit needs instead")
    if i.get("instead_link") and not str(i["instead_link"]).startswith("https://"): e("instead_link must be https")
    if i.get("instead_link") and not i.get("instead"): e("instead_link without instead")
    link = i.get("link")
    if link and not re.match(r"https?://[^\s?#]+$", link): e("link must be a clean http link with no ?query")
    if i.get("pasted") != link: e("pasted must equal link")
    if i.get("image") != f"img/{i.get('id')}.jpg": e("image must be img/<id>.jpg")
    if i.get("image_src") and not str(i["image_src"]).startswith("https://"): e("image_src must be https")
    if not re.search(r"-0[45]:00$", str(i.get("checked") or "")): e("checked needs an Eastern offset")
    for k in ("price", "was"):
        if i.get(k) is not None and not isinstance(i[k], (int, float)): e(f"{k} must be a number or null")
    text = " ".join([str(i.get("headline") or ""), str(i.get("instead") or "")] + [str(r) for r in rs]).lower()
    if re.search(r"\b(fake|scam|scams|fraud|lie|lies|lying)\b", text): e("never call a discount fake, a scam or a lie")
    if i.get("target") is not None and (v != "wait" or not isinstance(i["target"], (int, float)) or (isinstance(i.get("price"), (int, float)) and i["target"] >= i["price"])): e("target is for a wait, a number below today's price")
    if i.get("id") not in strict: continue
    if i.get("price") is None: e("no price: skip it instead")
    if i.get("reviewed") not in (True, "self"): e("no independent second check recorded (reviewed)")
    ev = i.get("evidence") or []
    if not 2 <= len(ev) <= 6: e("needs 2 to 6 evidence entries")
    for x in ev:
        if x.get("kind") not in ("today", "history", "other-store", "last-year", "product", "sale-dates"): e("evidence kind is wrong")
        if words(x.get("what")) == 0 or words(x.get("what")) > 12: e("evidence 'what' must be 1 to 12 words")
        if x.get("url") and not str(x["url"]).startswith("http"): e("evidence url must be http(s) or null")
        if x.get("date") and not re.match(r"\d{4}-\d{2}-\d{2}$", str(x["date"])): e("evidence date must be YYYY-MM-DD")
    if not any(x.get("kind") == "today" for x in ev): e("needs a 'today' evidence entry")
    hist = [x for x in ev if x.get("kind") == "history" and x.get("date") and isinstance(x.get("price"), (int, float))]
    if v == "buy":
        if not hist: e("a buy needs a dated earlier price (kind history, with date and price); otherwise it is a wait")
        elif isinstance(i.get("price"), (int, float)) and i["price"] > 1.10 * min(x["price"] for x in hist):
            e(f"price is more than 10% above its dated low of {min(x['price'] for x in hist)}: that is a wait")
        cheaper = [x for x in ev if x.get("kind") == "other-store" and isinstance(x.get("price"), (int, float)) and isinstance(i.get("price"), (int, float)) and x["price"] < 0.97 * i["price"]]
        if cheaper: e("cheaper at another store in your own evidence: not a buy")
if bad:
    print("FAIL"); [print(" -", m) for m in bad]; sys.exit(1)
print("OK")
