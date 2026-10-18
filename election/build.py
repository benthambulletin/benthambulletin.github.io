#!/usr/bin/env python3
"""Render election/index.html from election/data.json.

Usage: python3 election/build.py   (from the repo root)
Every number on the page comes from data.json; nothing is typed into this file.
"""
import json, html, datetime, pathlib

ROOT = pathlib.Path(__file__).resolve().parent
D = json.load(open(ROOT / "data.json"))
e = html.escape

def num(x, nd=1):
    if x is None: return "—"
    x = float(x)
    return f"{x:.{nd}f}".rstrip("0").rstrip(".") if nd else f"{int(round(x))}"

def margin(m):
    if m is None: return "no poll"
    m = float(m)
    if m == 0: return "Tie"
    return f"D +{num(m)}" if m >= 0 else f"R +{num(-m)}"

def net(n):
    n = float(n); return ("+" if n > 0 else "−") + num(abs(n))

def fdate(s, fmt="%b %-d"):
    return datetime.date.fromisoformat(s).strftime(fmt)

today = datetime.date.fromisoformat(D["as_of"])
eday = datetime.date.fromisoformat(D["election_day"])
days = (eday - today).days
ctrl = {r["measure"]: r["value"] for r in D["control"]}
gb = {r["tracker"]: r for r in D["generic_ballot"]}
ap = {r["tracker"]: r for r in D["approval"]}
gov = {r["poll"]: r for r in D["ny_governor"]}

def bar(m, scale=15):
    """Diverging bar for a D−R margin: Democrat lead grows left (blue), Republican lead grows right (red)."""
    if m is None: return '<div class="dv none"><span>No public poll</span></div>'
    m = float(m); w = min(abs(m) / scale * 50, 50)
    side = "d" if m >= 0 else "r"
    return f'<div class="dv" aria-hidden="true"><i class="{side}" style="width:{w:.1f}%"></i></div>'

def chip(rating):
    t = (rating or "").lower()
    k = "tu" if "toss" in t else ("d" if t.endswith(" d") else ("r" if t.endswith(" r") else "nx"))
    return f'<span class="chip {k}">{e(rating)}</span>'

def lead(m):
    if m is None: return '<span class="lead nx">No poll</span>'
    return f'<span class="lead {"nx" if float(m) == 0 else ("d" if float(m) > 0 else "r")}">{margin(m)}</span>'

def lede(text):
    """Bold the short lead-in before a colon ("Texas: ...") — presentation only."""
    k = text.find(": ")
    if 0 < k <= 40: return f"<b>{e(text[:k])}</b>{e(text[k:])}"
    return e(text)

# ---------- sections ----------
bottom = "".join(
    f'<li><span class="ov" aria-hidden="true">{k}</span><div><h3>{e(r["headline"])}</h3><p>{e(r["detail"])}</p></div></li>'
    for k, r in enumerate(sorted(D["bottom_line"], key=lambda r: r["order"]), 1))

changed = ""
if D.get("what_changed"):
    changed = '<h2>What changed since yesterday</h2><ul class="changed">' + "".join(
        f"<li>{lede(c)}</li>" for c in D["what_changed"]) + "</ul>"

sb = gb["Silver Bulletin (all polls)"]; rcp = gb["RealClearPolling average"]; avg = ap["RealClearPolling average"]
eday_short = fdate(D["election_day"]); eday_long = fdate(D["election_day"], "%A, %b %-d")
tiles = f"""
<div class="tiles">
 <div class="tile"><div class="lbl">Generic ballot</div><div class="big d">D +{num(sb["margin"])}</div><div class="sub">Silver Bulletin, {fdate(sb["as_of"])}. RealClearPolling D +{num(rcp["margin"])}.</div></div>
 <div class="tile"><div class="lbl">Trump net approval</div><div class="big">{net(avg["net"])}</div><div class="sub">{num(avg["approve"])}% approve, {num(avg["disapprove"])}% disapprove. RealClearPolling, {e((avg.get("note") or "").replace("Polls ", "", 1))}.</div></div>
 <div class="tile"><div class="lbl">Odds of a Democratic Senate</div><div class="big">{num(ctrl["Polymarket odds of Democratic Senate (%)"],0)}%</div><div class="sub">Polymarket. Democrats need net +{num(ctrl["Net seats Democrats need for 51"],0)}; Cook has {num(ctrl["Toss-up seats (Cook)"],0)} toss-ups.</div></div>
 <div class="tile"><div class="lbl">Days to Election Day</div><div class="big">{days}</div><div class="sub">{eday_long}. Early voting {fdate(D["early_voting"]["start"])} – {fdate(D["early_voting"]["end"])}.</div></div>
</div>"""

def senate_row(r):
    held = {"D": "Democratic", "R": "Republican"}.get(r["held_by"], r["held_by"])
    src = (e(r["pollster"]) + (", " + e(r["dates"]) if r["dates"] else "")) if r["pollster"] else ""
    return f"""<li class="race">
 <div class="rh"><h3>{e(r["state"])}</h3>{chip(r["cook_rating"])}{lead(r["margin"])}</div>
 {bar(r["margin"])}
 <p class="who"><span class="p d">{e(r["democrat"])}</span> <span class="vs">vs</span> <span class="p r">{e(r["republican"])}</span></p>
 <p class="meta">{e(r["race"])}, {held} seat.{(" Poll: " + src + ".") if src else ""}</p>
 {f'<p class="note">{e(r["note"])}</p>' if r.get("note") else ""}
</li>"""
senate_rows = "".join(senate_row(r) for r in sorted(D["senate"], key=lambda r: (r["margin"] is None, -(r["margin"] or 0))))

def gov_row(r):
    m = float(r["margin"]); who = f'Hochul +{num(m)}' if m >= 0 else f'Blakeman +{num(-m)}'
    sample = f', {e(r["sample"])}' if r["sample"] and r["sample"] != "—" else ""
    note = f'<p class="note">{e(r["note"])}</p>' if r.get("note") and r["note"] != "Aggregate" else ""
    return f"""<li class="poll">
 <div class="rh"><h3>{e(r["poll"])}</h3><span class="lead {"d" if m >= 0 else "r"}">{who}</span></div>
 <div class="split" aria-hidden="true"><i class="d" style="width:{float(r["hochul"]):.1f}%"></i><i class="r" style="width:{float(r["blakeman"]):.1f}%"></i></div>
 <p class="who"><span class="p d">Hochul {num(r["hochul"])}%</span> <span class="p r">Blakeman {num(r["blakeman"])}%</span></p>
 <p class="meta">{e(r["dates"])}{sample}</p>{note}
</li>"""
gov_rows = "".join(gov_row(r) for r in D["ny_governor"])

def house_row(r):
    pc = r["party"].lower()
    poll = (f' Latest poll: {e(r["pollster"])}, {e(r["dates"] or "")}, {num(r["dem_pct"])}–{num(r["rep_pct"])}.') if r["pollster"] else ""
    return f"""<li class="race">
 <div class="rh"><h3>{e(r["district"])}</h3>{chip(r["rating"])}{lead(r["margin"]) if r["margin"] is not None else ""}</div>
 <p class="who"><span class="p {pc}">{e(r["incumbent"])} ({e(r["party"])}, inc.)</span> <span class="vs">vs</span> <span class="p {"r" if pc == "d" else "d"}">{e(r["challenger"])}</span></p>
 <p class="meta">{e(r["area"])}. Rating: {e(r["rating_source"])}.{poll}</p>
 {f'<p class="note">{e(r["note"])}</p>' if r.get("note") else ""}
</li>"""
house_rows = "".join(house_row(r) for r in D["ny_house"])
pa_rows = "".join(house_row(r) for r in D.get("pa_bellwethers", []))
pa_block = (f'<h3 class="sub-h">Pennsylvania: four seats that tell you early</h3>'
            f'<p class="intro">Pennsylvania counts fast, and these four districts cover every kind of swing seat. Democrats flipping all four is a wave; none means the polls were wrong; two or three is the expected night.</p>'
            f'<ul class="races">{pa_rows}</ul>') if pa_rows else ""

def rows(items):
    return "".join(f'<div class="row"><dt>{e(i["office"])}</dt><dd>{e(i["race"])}</dd></div>' for i in items)
def town_block(t, open_):
    body = rows(t["items"]) + f'<div class="row ev"><dt>Early voting</dt><dd>{e(t["early_voting"]["site"])}</dd></div>'
    return (f'<details class="town"{" open" if open_ else ""}><summary><span class="tn">{e(t["town"])}</span><span class="cty">{e(t["county"])} County</span></summary>'
            f'<dl>{body}</dl></details>')
ballot_boxes = "".join(town_block(t, k == 0) for k, t in enumerate(D["your_ballot"]))
statewide = rows(D["statewide"])

# Countdown line, then the early-voting banner from the first day of early voting, then Election Day
ev = D["early_voting"]
ev_start = datetime.date.fromisoformat(ev["start"]); ev_end = datetime.date.fromisoformat(ev["end"])
eday_row = next((r for r in D["key_dates"] if r["date"] == D["election_day"]), {})
banner = ""
if today < ev_start:
    n = (ev_start - today).days
    banner = (f'<p class="count"><b>{days} days to Election Day</b>, {eday_long}. Early voting starts {"tomorrow" if n == 1 else f"in {n} days"} '
              f'({fdate(ev["start"], "%a, %b %-d")} – {fdate(ev["end"], "%a, %b %-d")}); sites for each town are in the Your ballot box below.</p>')
elif ev_start <= today <= eday:
    if today <= ev_end:
        head = f"Early voting is open through {fdate(ev['end'], '%A, %b %-d')}"
        sites = "".join(f'<div class="row"><dt>{e(t["town"])}</dt><dd>{e(t["early_voting"]["site"])}<span class="hrs">{e(ev["hours"].get(t["county"], ""))}</span></dd></div>' for t in D["your_ballot"])
        banner = (f'<section class="banner"><h2 class="bh">{e(head)}</h2>'
                  f'<p class="bs">{days} days to Election Day, {eday_long}.</p><dl>{sites}</dl></section>')
    else:
        when = "today" if today == eday else fdate(D["election_day"], "%A")
        hours = e((eday_row.get("note") or "").rstrip("."))
        banner = (f'<section class="banner"><h2 class="bh">Election Day is {when}</h2>'
                  f'<p class="bs">{hours + ". " if hours else ""}Early voting has closed. Vote at your assigned polling place: '
                  f'<a href="https://voterlookup.elections.ny.gov/">look it up at voterlookup.elections.ny.gov</a>.</p></section>')

def date_row(r):
    d = datetime.date.fromisoformat(r["date"])
    state = "past" if d < today else ("now" if d == today else "")
    return (f'<li class="{state}"><span class="dt"><b>{d.strftime("%b %-d")}</b>{d.strftime("%a")}</span>'
            f'<span class="ev">{e(r["event"])}{f"<small>{e(r["note"])}</small>" if r["note"] else ""}</span></li>')
dates_rows = "".join(date_row(r) for r in D["key_dates"])

trend = ""
if len(D.get("history", [])) > 1:
    pts = D["history"]
    trend = '<h2>Trend</h2><div class="scroll"><table class="trend"><thead><tr><th>Date</th><th>Generic ballot</th><th>Trump net</th><th>D Senate odds</th><th>Hochul margin</th></tr></thead><tbody>' + "".join(
        f'<tr><td>{fdate(p["date"])}</td><td>D +{num(p["generic_ballot"])}</td><td>{net(p["trump_net"])}</td><td>{num(p["dem_senate_odds"],0)}%</td><td>+{num(p["hochul_margin"])}</td></tr>'
        for p in reversed(pts[-14:])) + "</tbody></table></div>"

# ---------- main body: polls until election night, results after ----------
polls_main = f"""
<h2>Senate battleground</h2>
<p class="intro">Latest public poll or polling average. Bars run from even in the middle: <span class="p d">Democrat ahead</span> to the left, <span class="p r">Republican ahead</span> to the right. <span class="chip tu">Toss Up</span> ratings are Cook's.{(" " + e(D["senate_intro"])) if D.get("senate_intro") else ""}</p>
<ul class="races">{senate_rows}</ul>

<h2>New York governor</h2>
<p class="intro">Each bar is the full electorate: <span class="p d">Hochul</span> from the left, <span class="p r">Blakeman</span> from the right, undecided in the gap.</p>
<ul class="races">{gov_rows}</ul>

<h2>House seats we watch</h2>
<ul class="races">{house_rows}</ul>
{pa_block}"""

R = D.get("results") or {}
def results_main():
    sen, hou = R.get("senate", {}), R.get("house", {})
    tiles_r = f"""<h2>Results</h2><div class="tiles results">
 <div class="tile"><div class="lbl">Senate seats called</div><div class="big"><span class="d">{sen.get("dem","—")}</span><span class="dash">–</span><span class="r">{sen.get("rep","—")}</span></div><div class="sub">51 for a majority. {e(sen.get("called_note",""))}</div></div>
 <div class="tile"><div class="lbl">House seats called</div><div class="big"><span class="d">{hou.get("dem","—")}</span><span class="dash">–</span><span class="r">{hou.get("rep","—")}</span></div><div class="sub">218 for a majority.</div></div>
</div>"""
    def race_row(r):
        status = r.get("status", "")
        st = "called" if status.strip().lower() == "called" else "open"
        lead_ = f'{e(r.get("leader",""))}{(" +" + num(r.get("pct_lead"))) if r.get("pct_lead") is not None else ""}'
        return (f'<li class="race res"><div class="rh"><h3>{e(r["race"])}</h3><span class="status {st}">{e(status)}</span></div>'
                f'<p class="who"><b>{lead_}</b></p><p class="meta">{e(r.get("candidates",""))}. {e(r.get("reporting",""))}</p></li>')
    rows_ = "".join(race_row(r) for r in R.get("races", []))
    local = "".join(race_row(r) for r in R.get("local", []))
    return tiles_r + f"""
<h3 class="sub-h">Races we watched</h3>
<ul class="races">{rows_}</ul>
<h3 class="sub-h">Your towns</h3>
<ul class="races">{local}</ul>
<p class="intro">{e(R.get("source_note",""))}</p>"""

is_results = D.get("mode") == "results"
main = results_main() if is_results else polls_main
numbers = main if is_results else f"<h2>The numbers</h2>{tiles}"
# ---------- calm box, steadiness line, election night ----------
calm = ""
if D.get("how_to_read"):
    h = D["how_to_read"]
    calm = (f'<details class="town state-h calm" open><summary><span class="tn">{e(h["title"])}</span></summary><ul class="changed">'
            + "".join(f"<li>{e(i)}</li>" for i in h["items"]) + "</ul></details>")

steady = ""
hist = D.get("history", [])
if len(hist) >= 2:
    first, last = hist[0], hist[-1]
    span = (datetime.date.fromisoformat(last["date"]) - datetime.date.fromisoformat(first["date"])).days
    def delta(a, b, unit=""):
        dlt = float(b) - float(a)
        if abs(dlt) < 0.05: return "unchanged"
        return ("up " if dlt > 0 else "down ") + num(abs(dlt)) + unit
    steady = (f'<p class="intro steady">Over the past {span} day{"s" if span != 1 else ""} the generic ballot is '
              f'{delta(first["generic_ballot"], last["generic_ballot"], " pts")}, Trump\'s net approval is '
              f'{delta(first["trump_net"], last["trump_net"], " pts")}, and the odds of a Democratic Senate are '
              f'{delta(first["dem_senate_odds"], last["dem_senate_odds"], " pts")}. Slow movement is the normal state.</p>')

enight = ""
if D.get("election_night"):
    n = D["election_night"]
    enight = (f'<h2>{e(n["title"])}</h2><p class="intro">{e(n["intro"])}</p><ul class="changed">'
              + "".join(f'<li><b>{e(i["when"])}</b>: {e(i["what"])}</li>' for i in n["items"]) + "</ul>")

outlook = ""
if D.get("outlook"):
    o = D["outlook"]
    outlook = (f'<h2>{e(o["title"])}</h2><p class="intro" style="font-size:1rem;color:var(--ink)">{e(o["lede"])}</p>'
               '<ul class="changed">' + "".join(f'<li><b>{e(i["what"])}</b>: {e(i["why"])}</li>' for i in o["items"]) + '</ul>'
               f'<p class="intro">{e(o["noise"])} <span class="mut">Editor\'s read, {fdate(o["as_of"])}; this is judgment, not polling.</span></p>')
glossary = ""
if D.get("glossary"):
    glossary = ('<h2>What the words mean</h2><details class="town state-h" open><summary><span class="tn">Plain-English guide to the numbers above</span></summary><dl>'
                + "".join(f'<dt>{e(g["term"])}</dt><dd>{e(g["text"])}</dd>' for g in D["glossary"]) + "</dl></details>")

CSS = """
@font-face{font-family:'Archivo';src:url(/assets/fonts/Archivo.ttf) format('truetype');font-weight:100 900;font-stretch:62% 125%;font-display:swap}
@font-face{font-family:'Lora';src:url(/assets/fonts/Lora.ttf) format('truetype');font-weight:400 700;font-display:swap}
@font-face{font-family:'Lora';src:url(/assets/fonts/Lora-Italic.ttf) format('truetype');font-weight:400 700;font-style:italic;font-display:swap}
:root{color-scheme:light;--paper:#f7f7f2;--surround:#e6e7e0;--ink:#1b1f2a;--soft:#555b66;--rule:#d3d5cc;--tint:#edeee7;
--blue:#2559a6;--blue-t:#dfe7f4;--red:#bf3a2f;--red-t:#f6e1de;--purple:#674694;--purple-t:#ebe5f4;
--sans:'Archivo',system-ui,sans-serif;--serif:'Lora',Georgia,serif}
*{box-sizing:border-box}
html{background:var(--surround);-webkit-text-size-adjust:100%;text-size-adjust:100%}
@supports (font:-apple-system-body){html{font:-apple-system-body}}
body{margin:0;background:var(--surround);color:var(--ink);font-family:var(--serif);font-size:1rem;line-height:1.55;font-variant-numeric:lining-nums tabular-nums}
.page{max-width:42rem;margin:0 auto;background:var(--paper);min-height:100vh;padding:0 1rem 2.5rem;position:relative}
a{color:var(--ink);text-decoration-thickness:1px;text-underline-offset:.15em}
a:focus-visible,summary:focus-visible{outline:3px solid var(--purple);outline-offset:2px}
p{margin:0}
h1,h2,h3,.lbl,.chip,.lead,.status,dt,summary,.tile .big,.dt,.count b,.ov{font-family:var(--sans)}

/* masthead: optical-scan timing marks across the top, like the edge of a ballot */
.marks{height:.6rem;margin:0 -1rem;background:repeating-linear-gradient(90deg,var(--ink) 0 1.1rem,transparent 1.1rem 1.9rem)}
header{padding:1.5rem 0 1.1rem;border-bottom:2px solid var(--ink)}
.upd{font-family:var(--sans);font-size:.8rem;font-weight:500;color:var(--soft);display:flex;justify-content:space-between;gap:.5rem;flex-wrap:wrap}
h1{font-size:clamp(2.9rem,15vw,4.6rem);font-weight:850;font-stretch:118%;letter-spacing:-.035em;line-height:.9;margin:.45rem 0 .55rem}
.dek{font-size:1.02rem;color:var(--ink);max-width:34em}
.count{margin:1rem 0 0;padding:.75rem .9rem;background:var(--tint);border-left:4px solid var(--purple);font-size:.95rem}
.count b{font-weight:700}

/* section heads: inverted bars, like the office headers on a ballot */
h2{margin:2.2rem -1rem .9rem;padding:.55rem 1rem .5rem;background:var(--ink);color:var(--paper);font-size:1.05rem;font-weight:700;font-stretch:105%;letter-spacing:.005em;line-height:1.25}
h3{margin:0;font-weight:700;font-size:1.05rem;line-height:1.25}
.intro{font-size:.9rem;color:var(--soft);margin:-.2rem 0 .8rem}

/* bottom line: filled ballot ovals, ranked */
.bottom{list-style:none;margin:0;padding:0}
.bottom li{display:grid;grid-template-columns:2.3rem 1fr;gap:.2rem .6rem;padding:.8rem 0;border-bottom:1px solid var(--rule)}
.bottom li:last-child{border-bottom:0}
.ov{width:2.05rem;height:1.3rem;border-radius:50%;background:var(--ink);color:var(--paper);font-size:.78rem;font-weight:700;display:flex;align-items:center;justify-content:center;margin-top:.12rem}
.bottom h3{font-size:1.15rem;font-weight:750;font-stretch:96%;letter-spacing:-.005em}
.bottom p{color:var(--soft);font-size:.95rem;margin-top:.2rem}

/* numbers */
.tiles{display:grid;grid-template-columns:1fr 1fr;border-top:1px solid var(--rule);border-left:1px solid var(--rule)}
.tile{padding:.75rem .75rem .85rem;border-right:1px solid var(--rule);border-bottom:1px solid var(--rule);min-width:0}
.lbl{font-size:.78rem;font-weight:600;color:var(--soft);line-height:1.25}
.tile .big{font-size:2.3rem;font-weight:800;font-stretch:80%;line-height:1;margin:.3rem 0 .35rem;letter-spacing:-.01em;white-space:nowrap}
.tile .sub{font-size:.8rem;color:var(--soft);line-height:1.4}
@media(min-width:44rem){.tiles:not(.results){grid-template-columns:repeat(4,1fr)}}

.changed{margin:0;padding:0;list-style:none}
.changed li{padding:.6rem 0 .6rem 1.1rem;border-bottom:1px solid var(--rule);position:relative}
.changed li:last-child{border-bottom:0}
.changed li::before{content:"";position:absolute;left:0;top:1.2rem;width:.5rem;height:.32rem;border-radius:50%;background:var(--ink)}
.changed b{font-family:var(--sans);font-weight:700}

/* race rows */
.races{list-style:none;margin:0;padding:0}
.race,.poll{padding:.9rem 0 1rem;border-bottom:1px solid var(--rule)}
.races li:last-child{border-bottom:0}
.rh{display:flex;align-items:center;gap:.45rem;flex-wrap:wrap}
.rh h3{font-size:1.2rem;font-weight:750;margin-right:auto}
.poll .rh h3{font-size:1rem;font-weight:650}
.chip{font-size:.75rem;font-weight:650;padding:.12rem .5rem;border-radius:1rem;white-space:nowrap;background:var(--tint);color:var(--ink)}
.chip.tu{background:var(--purple-t);color:var(--purple)}.chip.d{background:var(--blue-t);color:var(--blue)}.chip.r{background:var(--red-t);color:var(--red)}
.lead{font-size:1.05rem;font-weight:800;font-stretch:85%;white-space:nowrap;min-width:3.6rem;text-align:right}
.lead.d{color:var(--blue)}.lead.r{color:var(--red)}.lead.nx{color:var(--soft);font-weight:500;font-size:.85rem}
.dv{position:relative;height:.65rem;margin:.55rem 0 .45rem;background:linear-gradient(90deg,transparent calc(50% - 1px),var(--ink) calc(50% - 1px),var(--ink) calc(50% + 1px),transparent calc(50% + 1px)),var(--tint)}
.dv i{position:absolute;top:0;bottom:0}
.dv i.d{right:50%;background:var(--blue)}.dv i.r{left:50%;background:var(--red)}
.dv.none{background:repeating-linear-gradient(135deg,var(--tint) 0 6px,transparent 6px 10px);height:1.05rem;display:flex;align-items:center;justify-content:center}
.dv.none span{font-family:var(--sans);font-size:.72rem;font-weight:600;color:var(--soft);background:var(--paper);padding:0 .4rem;line-height:1.2}
.split{display:flex;justify-content:space-between;height:.65rem;margin:.55rem 0 .4rem;background:var(--tint)}
.split i.d{background:var(--blue)}.split i.r{background:var(--red)}
.who{font-family:var(--sans);font-size:.95rem;font-weight:550;margin-top:.15rem}
.vs{color:var(--soft);font-weight:400;padding:0 .1rem}
.p::before{content:"";display:inline-block;width:.55rem;height:.55rem;border-radius:2px;margin-right:.3rem;vertical-align:.05em}
.p.d::before{background:var(--blue)}.p.r::before{background:var(--red)}
.poll .who{display:flex;justify-content:space-between}
.meta{font-size:.82rem;color:var(--soft);margin-top:.2rem;line-height:1.45}
.note{font-size:.88rem;margin-top:.35rem;line-height:1.5}
.res .who{font-size:1.15rem;margin-top:.3rem}
.status{font-size:.75rem;font-weight:650;padding:.12rem .55rem;border-radius:1rem;border:1.5px solid var(--purple);color:var(--purple);white-space:nowrap}
.status.called{background:var(--ink);border-color:var(--ink);color:var(--paper)}
.tiles.results .big{font-size:clamp(1.8rem,10vw,2.6rem)}
.dash{color:var(--soft);font-weight:400;padding:0 .2rem}
.sub-h{margin:1.6rem 0 .1rem;font-size:1.1rem;padding-bottom:.35rem;border-bottom:2px solid var(--ink)}

/* your ballot */
.town{border:1px solid var(--rule);background:#fff;margin:0 0 .5rem;border-radius:.3rem}
.town summary{cursor:pointer;list-style:none;display:flex;align-items:baseline;gap:.5rem;padding:.8rem 2.6rem .8rem .9rem;min-height:3rem;position:relative}
.town summary::-webkit-details-marker{display:none}
.town summary::after{content:"";position:absolute;right:1rem;top:50%;width:.55rem;height:.55rem;border-right:2px solid var(--ink);border-bottom:2px solid var(--ink);transform:translateY(-70%) rotate(45deg);transition:transform .15s}
.town dd+dt{margin-top:.65rem}
.town[open] summary::after{transform:translateY(-30%) rotate(-135deg)}
.town[open] summary{border-bottom:1px solid var(--rule)}
.tn{font-weight:700;font-size:1.05rem}
.cty{font-size:.82rem;color:var(--soft);font-weight:500}
.town dl{margin:0;padding:.2rem .9rem .5rem}
.row{display:grid;grid-template-columns:minmax(5.5rem,30%) 1fr;gap:.75rem;padding:.5rem 0;border-bottom:1px solid var(--tint)}
.row:last-child{border-bottom:0}
dt{font-size:.8rem;font-weight:650;color:var(--soft);line-height:1.35;padding-top:.12rem;overflow-wrap:anywhere}
dd{margin:0;font-size:.92rem;line-height:1.45}
.row.ev dt{color:var(--purple)}
.state-h .tn{font-stretch:105%}

/* banner */
.banner{margin:1rem -1rem 0;padding:1.1rem 1rem 1rem;background:var(--purple);color:#fff}
.banner .bh{margin:0;padding:0;background:none;color:#fff;font-size:1.45rem;font-weight:800;font-stretch:95%;line-height:1.15}
.banner .bs{margin-top:.4rem;font-size:.95rem}
.banner a{color:#fff}
.banner dl{margin:.8rem 0 0;background:var(--paper);color:var(--ink);border-radius:.3rem;padding:.2rem .85rem}
.hrs{display:block;font-size:.82rem;color:var(--soft);margin-top:.15rem}

/* key dates: a real sequence */
.dates{list-style:none;margin:0;padding:0}
.dates li{display:grid;grid-template-columns:4.6rem 1fr;gap:.8rem;padding:.65rem 0;border-bottom:1px solid var(--rule)}
.dates li:last-child{border-bottom:0}
.dt{font-size:.8rem;color:var(--soft);line-height:1.2}.dt b{display:block;font-size:1.05rem;color:var(--ink);font-weight:750}
.ev small{display:block;font-size:.85rem;color:var(--soft)}
.dates li.past{opacity:.55}.dates li.now .dt b{color:var(--purple)}

.scroll{overflow-x:auto;-webkit-overflow-scrolling:touch}
.trend{border-collapse:collapse;width:100%;font-family:var(--sans);font-size:.85rem}
.trend th,.trend td{padding:.45rem .5rem;border-bottom:1px solid var(--rule);text-align:right;white-space:nowrap}
.trend th{font-weight:600;color:var(--soft);font-size:.75rem;white-space:normal;vertical-align:bottom}
.trend th:first-child,.trend td:first-child{text-align:left;padding-left:0}

.foot{font-size:.8rem;color:var(--soft);margin-top:2.4rem;padding-top:1rem;border-top:2px solid var(--ink);line-height:1.55}
@media(min-width:44rem){.page{padding:0 2rem 3rem}.marks{margin:0 -2rem}h2,.banner{margin-left:-2rem;margin-right:-2rem;padding-left:2rem;padding-right:2rem}}
@media(prefers-reduced-motion:reduce){*{transition:none!important}}
"""

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#1b1f2a">
<meta name="description" content="2026 midterm tracker — national polling, the Senate, and New York's races, refreshed every morning.">
<meta property="og:title" content="The Ballot — 2026 Midterm Tracker">
<meta property="og:description" content="Democrats lead the generic ballot by {num(sb["margin"])}; {num(ctrl["Toss-up seats (Cook)"],0)} Senate toss-ups; Hochul up {num(gov["Emerson College / PIX11"]["margin"])} in New York. Updated {today.strftime("%b %-d")}.">
<meta property="og:url" content="https://benthambulletin.github.io/election/">
<meta property="og:type" content="website">
<meta http-equiv="Cache-Control" content="no-cache">
<link rel="icon" href="/assets/favicon.svg">
<link rel="preload" href="/assets/fonts/Archivo.ttf" as="font" type="font/ttf" crossorigin>
<title>The Ballot — 2026 Midterm Tracker</title>
<style>{CSS}</style>
</head>
<body><div class="page">
<div class="marks" aria-hidden="true"></div>
<header>
<p class="upd"><span>2026 midterms</span><span>Updated {today.strftime("%A, %B %-d")}</span></p>
<h1>The Ballot</h1>
<p class="dek">National polling, the Senate map and New York's races, explained plainly and refreshed every morning through {eday_short}.</p>
</header>
{banner}

<h2>The bottom line</h2>
<ol class="bottom">{bottom}</ol>
{numbers}
{steady}
{calm}
{glossary}
{changed}
{outlook}
{"" if is_results else main}

<h2>Your ballot</h2>
<p class="intro">Tap a town. Beyond the statewide races, what it votes on {eday_short} — nobody polls these.</p>
<details class="town state-h" open><summary><span class="tn">Every New York ballot</span></summary><dl>{statewide}</dl></details>
{ballot_boxes}

{enight}

<h2>Key dates</h2>
<ol class="dates">{dates_rows}</ol>
{trend}

<div class="foot">Sources: Silver Bulletin, RealClearPolling, Cook Political Report, Sabato's Crystal Ball, Emerson College, Marist, Siena, Pollfinity, NYT/Siena, CNN, WRAL/SurveyUSA, Trafalgar, Pollsmax, PoliAgg/VoteHub, Polymarket, Kalshi; ballot details from The Ballot Brief (NYS BOE Sept 4 certification), the Erie, Niagara, Monroe and Chautauqua boards of elections, WXXI, WKBW and Chautauqua Today. Polls are snapshots with margins of error of 3–5 points; a lead inside that range is a coin flip. Compiled each morning; <a href="/election/data.json">the underlying numbers</a> carry a source link per row.</div>
</div></body></html>'''

open(ROOT / "index.html", "w").write(page)
print("built election/index.html", len(page), "bytes; days to election:", days)
