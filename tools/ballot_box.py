#!/usr/bin/env python3
"""The daily Ballot (weekdays and Saturdays, the last two weeks to Nov 3; Garret, Oct 21).
Prints HTML built ONLY from election/data.json, so the paper always mirrors the tracker.
Usage: python3 tools/ballot_box.py YYYY-MM-DD   -> replaces the one-line <div class="ballot">.
Sunday keeps the full hand-written Ballot section.
"""
import json, sys, html, datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
d = json.load(open(ROOT / "election" / "data.json"))
today = datetime.date.fromisoformat(sys.argv[1])
eday = datetime.date.fromisoformat(d["election_day"])
ev0 = datetime.date.fromisoformat(d["early_voting"]["start"]); ev1 = datetime.date.fromisoformat(d["early_voting"]["end"])
days = (eday - today).days
e = lambda s: html.escape(s or "", quote=False).replace("–", "&ndash;").replace("—", "&mdash;").replace("·", "&middot;")
md = lambda x: x.strftime("%b %-d").replace("Oct", "Oct.").replace("Nov", "Nov.")

if today < ev0:
    ev = f"Early voting opens {'tomorrow' if (ev0-today).days == 1 else ev0.strftime('%A')}, {md(ev0)}, and runs through {md(ev1)}."
elif today <= ev1:
    left = (ev1 - today).days
    ev = f"Early voting is open now, through {md(ev1)}" + (" &mdash; today is the last day." if left == 0 else f" ({left + 1} days left).")
else:
    ev = "Early voting is over; polls open 6 a.m. to 9 p.m. on Election Day."

bl = {b["order"]: b for b in d["bottom_line"]}
gov = next((b for b in d["bottom_line"] if "Hochul" in b["headline"] or "Hochul" in b["detail"]), None)
house = {h["district"]: h for h in d.get("ny_house", [])}
towns = {t["town"]: t for t in d["your_ballot"]}

def race(town, n=0):
    return e(towns[town]["items"][n]["race"]) if town in towns else ""

lines = []
lines.append(f'<div class="ballot">&#9745; The Ballot &middot; <b>{days} days</b> to Election Day &middot; every race: <a href="https://benthambulletin.github.io/election/">benthambulletin.github.io/election</a></div>')
lines.append(f'<div class="line"><span class="lbl r">Vote early</span> {ev}</div>')
if gov:
    lines.append(f'<div class="line"><span class="lbl t">Governor</span> {e(gov["detail"].split(";")[0].rstrip("."))}.</div>')
nat = " ".join(f'{e(bl[k]["headline"])}.' for k in (1, 2) if k in bl)
lines.append(f'<div class="line"><span class="lbl t">Washington</span> {nat}</div>')
h26 = house.get("NY-26")
r26 = f' {e(h26["rating_source"].split(" (")[0])} rates it {e(h26["rating"])}.' if h26 and h26.get("rating") else ""
lines.append('<div class="line"><span class="lbl t">Our House seats</span> '
             f'<b>NY-26</b> (North Tonawanda): {race("North Tonawanda")}.{r26} '
             f'<b>NY-23</b> (Orchard Park, Dunkirk, Fredonia): {race("Orchard Park")}. '
             f'<b>NY-25</b> (Scottsville): {race("Scottsville (Wheatland)")}.</div>')
if today <= ev1:
    sites = []
    for name, short in (("North Tonawanda", "North Tonawanda"), ("Orchard Park", "Orchard Park"),
                        ("Scottsville (Wheatland)", "Scottsville"), ("Dunkirk", "Dunkirk and Fredonia")):
        if name in towns:
            sites.append(f'<b>{short}:</b> {e(towns[name]["early_voting"]["site"])}')
    lines.append('<div class="line"><span class="lbl t">Where</span> ' + " &middot; ".join(sites) + '</div>')
print("\n".join(lines))
