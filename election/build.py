#!/usr/bin/env python3
"""Render election/index.html from election/data.json.

Usage: python3 election/build.py [data.json] [out.html]   (defaults: election/data.json -> election/index.html)
Every number on the page comes from data.json; nothing is typed into this file.

The page has four tabs, switched client-side by the URL hash:
  #today (default)  dates strip / banner, results (results mode), bottom line, what changed, national numbers, how to read
  #senate           intro, Must hold, Likely pickup, Need N of these M
  #house            New York seats, Pennsylvania four, New York governor
  #ballot           statewide, your town, election night, what the words mean, what could still change this, last days, sources
Every fact lives on exactly one tab.
"""
import json, re, html, datetime, pathlib, sys

ROOT = pathlib.Path(__file__).resolve().parent
DATA = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "data.json"
OUT = pathlib.Path(sys.argv[2]) if len(sys.argv) > 2 else ROOT / "index.html"
D = json.load(open(DATA))
e = html.escape

# ---------- formatting: one margin format everywhere ----------
def num(x, nd=1):
    if x is None: return "—"
    x = float(x)
    if nd == 0: return str(int(abs(x) + 0.5) * (1 if x >= 0 else -1))
    return f"{x:.{nd}f}".rstrip("0").rstrip(".")

def whole(m):
    """Round half up, as a reader would: 2.5 -> 3."""
    return int(abs(float(m)) + 0.5)

TIE = 1.0   # under 1 point = tied, in the badge and in the sentence

def badge_text(m):
    """Race badge: 'D +3', 'R +3', 'Tied'. Whole points."""
    if m is None: return "No poll"
    if abs(float(m)) < TIE: return "Tied"
    return f'{"D" if float(m) > 0 else "R"} +{whole(m)}'

def tracker_margin(m):
    """National trackers keep one decimal (small daily moves matter): 'D +8.9'."""
    m = float(m)
    return f'{"D" if m >= 0 else "R"} +{num(abs(m))}'

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

PARTY_TAG = re.compile(r"\(((?:D|R|Con|WFP)(?:[,/+][^()]*)?)\)")
def tag_text(text):
    """Color the (D), (R), (D, inc.), (R/WFP), (D+R/...) tags written inside free text. Party color only on party tags."""
    def sub(m):
        inner = m.group(1); first = inner[0]
        pc = "d" if first == "D" else "r" if first == "R" else ""
        if "D+R" in inner or "R+D" in inner: pc = "both"
        return f'<span class="pt {pc}">({e(inner)})</span>'
    return PARTY_TAG.sub(sub, e(text))

def bar(m, scale=15):
    """Diverging bar: Democratic lead grows left (blue), Republican lead grows right (red). Nothing when there is no poll."""
    if m is None: return ""
    m = float(m); w = min(abs(m) / scale * 50, 50)
    side = "d" if m >= 0 else "r"
    return f'<div class="dv" aria-hidden="true"><i class="{side}" style="width:{w:.1f}%"></i></div>'

def chip(rating):
    if not rating: return ""
    t = rating.lower()
    k = "tu" if "toss" in t else ("d" if t.endswith(" d") else ("r" if t.endswith(" r") else "nx"))
    label = "Toss-up" if "toss" in t else rating
    return f'<span class="chip {k}">{e(label)}</span>'

def badge(m):
    k = "nx" if m is None or abs(float(m)) < TIE else ("d" if float(m) > 0 else "r")
    return f'<span class="lead {k}">{badge_text(m)}</span>'

def plain_margin(m):
    if m is None: return None
    if abs(float(m)) < TIE: return "tied"
    n = whole(m)
    return f"about {n} point" + ("" if n == 1 else "s")

def lede(text):
    """First sentence normal (bold lead-in before a colon), anything after it muted."""
    m = re.match(r"(.+?[.!?])(\s+.+)?$", text.strip(), re.S)
    first, rest = (m.group(1), (m.group(2) or "").strip()) if m else (text, "")
    k = first.find(": ")
    head = f"<b>{e(first[:k])}</b>{tag_text(first[k:])}" if 0 < k <= 40 else tag_text(first)
    return head + (f' <span class="mut">{tag_text(rest)}</span>' if rest else "")

def race_sentence(dem, rep, margin, held_by, open_seat=False):
    """'Sherrod Brown (D) leads Jon Husted (R) by about 3 points. Republican-held.'"""
    d = f'{e(dem)} <span class="pt d">(D)</span>'; r = f'{e(rep)} <span class="pt r">(R)</span>'
    pm = plain_margin(margin)
    if pm is None: s = f"{d} vs {r}. No public poll yet."
    elif pm == "tied": s = f"{d} and {r} are tied."
    elif float(margin) > 0: s = f"{d} leads {r} by {pm}."
    else: s = f"{r} leads {d} by {pm}."
    if not held_by: return s
    party = "Democratic" if held_by == "D" else "Republican"
    return f"{s} {'Open ' + party + ' seat' if open_seat else party + ' seat'}."

def fold(label, inner, cls=""):
    """The page's one disclosure control. Closed by default."""
    if not inner: return ""
    return f'<details class="fold {cls}"><summary>{label}</summary><div class="fb">{inner}</div></details>'

def race_card(title, area, rating, margin, sentence, polls_text):
    a = f'<p class="area">{e(area)}</p>' if area else ""
    polls = fold("Show the polls", f'<p class="note">{tag_text(polls_text)}</p>') if (margin is not None and polls_text) else ""
    return (f'<li class="race"><div class="rh"><h3>{e(title)}</h3>{chip(rating)}{badge(margin) if margin is not None else ""}</div>{a}'
            f'{bar(margin)}<p class="say">{sentence}</p>{polls}</li>')

# ---------- TODAY ----------
ev = D["early_voting"]
ev_start = datetime.date.fromisoformat(ev["start"]); ev_end = datetime.date.fromisoformat(ev["end"])
eday_row = next((r for r in D["key_dates"] if r["date"] == D["election_day"]), {})
eday_long = fdate(D["election_day"], "%A, %b %-d")
eday_hours = (eday_row.get("note") or "").replace("Polls open ", "").rstrip(".").replace(" – ", "–")
if eday_hours.endswith("p.m"): eday_hours += "."

def town_site(t):
    return t["early_voting"]["site"]

strip = ""
if today < ev_start:
    n = (ev_start - today).days
    strip = (f'<div class="strip">'
             f'<div><b>{days} days</b><span>to Election Day</span></div>'
             f'<div><b>{fdate(ev["start"], "%a, %b %-d")}</b><span>Early voting {"starts tomorrow" if n == 1 else "starts"}, through {fdate(ev["end"])}</span></div>'
             f'<div><b>{fdate(D["election_day"], "%a, %b %-d")}</b><span>Election Day{", polls " + e(eday_hours) if eday_hours else ""}</span></div>'
             f'</div><p class="intro strip-n">Early-voting sites for each town are on the <a href="#ballot">My ballot</a> tab.</p>')
elif ev_start <= today <= eday:
    if today <= ev_end:
        head = f"Early voting is open through {fdate(ev['end'], '%A, %b %-d')}"
        sites = "".join(f'<div class="row"><dt>{e(t["town"])}</dt><dd>{e(town_site(t))}<span class="hrs">{e(ev["hours"].get(t["county"], ""))}</span></dd></div>' for t in D["your_ballot"])
        strip = (f'<section class="banner"><h2 class="bh">{e(head)}</h2>'
                 f'<p class="bs">{days} days to Election Day, {eday_long}.</p><dl>{sites}</dl></section>')
    else:
        when = "today" if today == eday else fdate(D["election_day"], "%A")
        strip = (f'<section class="banner"><h2 class="bh">Election Day is {when}</h2>'
                 f'<p class="bs">{"Polls are open " + e(eday_hours) + ". " if eday_hours else ""}Early voting has closed. Vote at your assigned polling place: '
                 f'<a href="https://voterlookup.elections.ny.gov/">look it up at voterlookup.elections.ny.gov</a>.</p></section>')

bottom = "".join(
    f'<li><span class="ov" aria-hidden="true">{k}</span><div><h3>{e(r["headline"])}</h3><p>{tag_text(r["detail"])}</p></div></li>'
    for k, r in enumerate(sorted(D["bottom_line"], key=lambda r: r["order"]), 1))

# steadiness line, computed from history — the last item of What changed
steady = ""
hist = D.get("history", [])
if len(hist) >= 2:
    first, last = hist[0], hist[-1]
    span = (datetime.date.fromisoformat(last["date"]) - datetime.date.fromisoformat(first["date"])).days
    ds = [float(last[k]) - float(first[k]) for k in ("generic_ballot", "trump_net", "dem_senate_odds")]
    def delta(dl):
        if abs(dl) < 0.05: return "unchanged"
        return ("up " if dl > 0 else "down ") + num(abs(dl)) + " point" + ("" if abs(dl) == 1 else "s")
    label = "Nationally, little moved" if max(abs(x) for x in ds) < 1 else "Nationally"
    steady = (f'<li><b>{label}</b>: over the past {span} day{"s" if span != 1 else ""} the generic ballot is {delta(ds[0])}, '
              f'Trump\'s net approval is {delta(ds[1])} and the odds of a Democratic Senate are {delta(ds[2])}. '
              f'<span class="mut">Slow movement is normal.</span></li>')
changed_items = "".join(f"<li>{lede(c)}</li>" for c in D.get("what_changed", [])) + steady
changed = f'<h2>What changed</h2><ul class="list">{changed_items}</ul>' if changed_items else ""

sb = gb["Silver Bulletin (all polls)"]; rcp = gb["RealClearPolling average"]; avg = ap["RealClearPolling average"]
odds = ctrl["Polymarket odds of Democratic Senate (%)"]
tiles = f"""<h2>National numbers</h2>
<div class="tiles">
 <div class="tile"><div class="lbl">Generic ballot</div><div class="big {"d" if sb["margin"] >= 0 else "r"}">{tracker_margin(sb["margin"])}</div><div class="sub">Which party people want for Congress. Silver Bulletin average; RealClearPolling has {tracker_margin(rcp["margin"])}.</div></div>
 <div class="tile"><div class="lbl">Trump net approval</div><div class="big">{net(avg["net"])}</div><div class="sub">{num(avg["approve"])}% approve, {num(avg["disapprove"])}% disapprove. RealClearPolling.</div></div>
 <div class="tile"><div class="lbl">Odds of a Democratic Senate</div><div class="big">{num(odds, 0)}%</div><div class="sub">Polymarket betting market.</div></div>
</div>"""

calm = ""
if D.get("how_to_read"):
    h = D["how_to_read"]
    calm = f'<h2>{e(h["title"])}</h2><ul class="list">' + "".join(f"<li>{e(i)}</li>" for i in h["items"]) + "</ul>"

mood = ""
if D.get("mood"):
    m_ = D["mood"]
    mood = (f'<h2>{e(m_["title"])}</h2><p class="intro">{e(m_["intro"])}</p><ul class="list">'
            + "".join(f'<li><b>{e(i["what"])}</b> {e(i["why"])} <span class="mut">({e(i["source"])})</span></li>' for i in m_["items"])
            + f'</ul><p class="mut" style="font-size:.8rem">{e(m_.get("note",""))}</p>')

R = D.get("results") or {}
is_results = D.get("mode") == "results"
def results_block():
    sen, hou = R.get("senate", {}), R.get("house", {})
    tiles_r = f"""<h2>Results</h2><div class="tiles results">
 <div class="tile"><div class="lbl">Senate seats called</div><div class="big"><span class="d">{sen.get("dem","—")}</span><span class="dash">–</span><span class="r">{sen.get("rep","—")}</span></div><div class="sub">51 for control. {e(sen.get("called_note",""))}</div></div>
 <div class="tile"><div class="lbl">House seats called</div><div class="big"><span class="d">{hou.get("dem","—")}</span><span class="dash">–</span><span class="r">{hou.get("rep","—")}</span></div><div class="sub">218 for control.</div></div>
</div>"""
    def race_row(r):
        status = r.get("status", "")
        st = "called" if status.strip().lower() == "called" else "open"
        ld = r.get("leader", "")
        pm = plain_margin(r.get("pct_lead"))
        verb = " wins" if st == "called" else ((" leads by less than a point" if pm == "tied" else f" leads by {pm}") if pm else "")
        lead_ = f'{tag_text(ld)}{verb if ld else ""}'
        return (f'<li class="race res"><div class="rh"><h3>{e(r["race"])}</h3><span class="status {st}">{e(status)}</span></div>'
                f'<p class="say res-l">{lead_}</p><p class="meta">{tag_text(r.get("candidates",""))}{". " + e(r["reporting"]) if r.get("reporting") else ""}</p></li>')
    rows_ = "".join(race_row(r) for r in R.get("races", []))
    local = "".join(race_row(r) for r in R.get("local", []))
    return (tiles_r + (f'<h3 class="sub-h">Races on this page</h3><ul class="races">{rows_}</ul>' if rows_ else "")
            + (f'<h3 class="sub-h">Your towns</h3><ul class="races">{local}</ul>' if local else "")
            + (f'<p class="intro">{e(R.get("source_note",""))}</p>' if R.get("source_note") else ""))

tab_today = (strip + (results_block() if is_results else "")
             + f'<h2>Bottom line</h2><ol class="bottom">{bottom}</ol>'
             + changed + ("" if is_results else tiles) + calm + mood)

# ---------- SENATE ----------
def senate_card(r):
    open_seat = (r.get("race") or "").lower().startswith("open")
    src = (r["pollster"] + (", " + r["dates"] if r["dates"] else "")) if r["pollster"] else ""
    polls = (("Based on the " + src + ". ") if src else "") + (r.get("note") or "")
    return race_card(r["state"], None, r["cook_rating"], r["margin"],
                     race_sentence(r["democrat"].replace(" (inc.)", ""), r["republican"].replace(" (inc.)", ""), r["margin"], r["held_by"], open_seat),
                     polls)

def by_margin(rows): return sorted(rows, key=lambda r: (r["margin"] is None, -(r["margin"] or 0)))
sen = D["senate"]
holds = [r for r in sen if r["held_by"] == "D"]
safe_flip = [r for r in sen if r["held_by"] == "R" and re.match(r"(likely|solid|safe) d", (r["cook_rating"] or "").lower())]
chase = [r for r in sen if r["held_by"] == "R" and r not in safe_flip]
need_net = int(ctrl["Net seats Democrats need for 51"])
need = need_net - len(safe_flip)
cards = lambda rows, closest_first=False: '<ul class="races">' + "".join(senate_card(r) for r in (by_margin(rows)[::-1] if closest_first else by_margin(rows))) + "</ul>"
flip_names = " and ".join(r["state"] for r in safe_flip)
tab_senate = (f'<h2>Senate</h2><p class="intro">{e(D.get("senate_intro",""))} Labels are Cook Political Report ratings.</p>'
              f'<h3 class="sub-h">Must hold</h3><p class="intro">Democratic seats. Lose one and Democrats need one more flip.</p>{cards(holds, True)}'
              + (f'<h3 class="sub-h">Likely pickup</h3><p class="intro">A Republican seat Democrats are well ahead in.</p>{cards(safe_flip)}' if safe_flip else "")
              + f'<h3 class="sub-h">Need {need} of these {len(chase)}</h3>'
              + f'<p class="intro">Republican seats. {f"Counts {e(flip_names)} as a flip; without it, Democrats need {need_net} of these." if safe_flip else ""}</p>{cards(chase)}')

# ---------- HOUSE ----------
def house_card(r):
    pc = r["party"].lower()
    inc, chal = r["incumbent"], re.sub(r"\s*\([^)]*\)\s*$", "", r["challenger"])
    dem, rep = (inc, chal) if pc == "d" else (chal, inc)
    poll = (f'Latest poll: {r["pollster"]}, {r["dates"] or ""}, {num(r["dem_pct"])}–{num(r["rep_pct"])}. ') if r["pollster"] else ""
    return race_card(r["district"], r["area"], r["rating"], r["margin"],
                     race_sentence(dem, rep, r["margin"], r["party"]), poll + (r.get("note") or ""))
ny_cards = "".join(house_card(r) for r in D["ny_house"])
pa_cards = "".join(house_card(r) for r in D.get("pa_bellwethers", []))

gov_rows = D["ny_governor"]
g = next((r for r in gov_rows if r.get("headline")), gov_rows[0])
def gov_line(r):
    sample = f', {r["sample"]}' if r.get("sample") and r["sample"] != "—" else ""
    return f'{r["poll"]} ({r["dates"]}{sample}): Hochul {num(r["hochul"])}, Blakeman {num(r["blakeman"])}.' + (f' {r["note"]}' if r.get("note") else "")
gov_polls = "".join(f'<p class="note">{tag_text(gov_line(r))}</p>' for r in gov_rows)
gov_card = (f'<ul class="races"><li class="race"><div class="rh"><h3>Hochul vs Blakeman</h3>{badge(g["margin"])}</div>{bar(g["margin"])}'
            f'<p class="say">{race_sentence("Hochul", "Blakeman", g["margin"], None)} '
            f'<span class="mut">{e(g["poll"].split(" (")[0])}, {e(g["dates"])}.</span></p>'
            f'{fold("Show the polls", gov_polls)}</li></ul>')

tab_house = (f'<h2>New York House seats</h2><p class="intro">Labels are Cook Political Report ratings.</p><ul class="races">{ny_cards}</ul>'
             + (f'<h2>Pennsylvania House seats</h2><p class="intro">Pennsylvania counts fast, and these four cover every kind of swing seat. '
                f'Democrats flipping all four is a wave; none means the polls were wrong; two or three is the expected night.</p><ul class="races">{pa_cards}</ul>' if pa_cards else "")
             + f'<h2>New York governor</h2>{gov_card}')

# ---------- MY BALLOT ----------
def rows(items):
    return "".join(f'<div class="row"><dt>{e(i["office"])}</dt><dd>{tag_text(i["race"])}</dd></div>' for i in items)
def town_block(t):
    hrs = ev["hours"].get(t["county"], "")
    body = rows(t["items"]) + f'<div class="row ev"><dt>Early voting</dt><dd>{e(t["early_voting"]["site"])}{f"<span class=hrs>{e(hrs)}</span>" if hrs else ""}</dd></div>'
    return fold(f'<span class="tn">{e(t["town"])}</span><span class="cty">{e(t["county"])} County</span>', f"<dl>{body}</dl>", "town")

enight = ""
if D.get("election_night"):
    n = D["election_night"]
    enight = (f'<h2>{e(n["title"])}</h2><p class="intro">{e(n["intro"])}</p><ul class="list">'
              + "".join(f'<li><b>{e(i["when"])}</b>: {tag_text(i["what"])}</li>' for i in n["items"]) + "</ul>")

glossary = ""
if D.get("glossary"):
    glossary = ('<h2>What the words mean</h2><dl class="gloss">'
                + "".join(f'<dt>{e(x["term"])}</dt><dd>{e(x["text"])}</dd>' for x in D["glossary"]) + "</dl>")

outlook = ""
if D.get("outlook"):
    o = D["outlook"]
    outlook = f'<h2>{e(o["title"])}</h2><p class="body">{e(o["text"])} <span class="mut">Judgment, not polling.</span></p>'

trend = ""
pts = D.get("history", [])[-3:]
if len(pts) > 1:
    trend = (f'<h2>Last {len(pts)} days</h2><table class="trend"><thead><tr><th>Date</th><th>Generic ballot</th><th>Trump net</th><th>Senate odds (D)</th><th>Hochul</th></tr></thead><tbody>'
             + "".join(f'<tr><td>{fdate(p["date"])}</td><td>{tracker_margin(p["generic_ballot"])}</td><td>{net(p["trump_net"])}</td><td>{num(p["dem_senate_odds"],0)}%</td><td>{badge_text(p["hochul_margin"])}</td></tr>'
                       for p in reversed(pts)) + "</tbody></table>")

sources = ('<div class="foot">Sources: Silver Bulletin, RealClearPolling, Cook Political Report, Sabato\'s Crystal Ball, Emerson College, Marist, Siena, Pollfinity, NYT/Siena, CNN, WRAL/SurveyUSA, Trafalgar, Pollsmax, PoliAgg/VoteHub, Polymarket, Kalshi; '
           'ballot details from The Ballot Brief (NYS BOE Sept 4 certification), the Erie, Niagara, Monroe and Chautauqua boards of elections, WXXI, WKBW and Chautauqua Today. '
           'Polls are snapshots with margins of error of 3–5 points; a lead inside that range is a coin flip. Compiled each morning; '
           '<a href="/election/data.json">the underlying numbers</a> carry a source link per row.</div>')

tab_ballot = (f'<h2>Statewide</h2><p class="intro">On every New York ballot.</p><dl class="plain">{rows(D["statewide"])}</dl>'
              f'<h2>Your town</h2><p class="intro">Tap a town for what it votes on and where to vote early. Nobody polls these races.</p>'
              + "".join(town_block(t) for t in D["your_ballot"])
              + enight + glossary + outlook + trend + sources)

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
h1,h2,h3,.lbl,.chip,.lead,.status,dt,summary,.tile .big,.strip b,.ov,.tabs a{font-family:var(--sans)}
.mut{color:var(--soft)}

/* masthead: optical-scan timing marks across the top, like the edge of a ballot */
.marks{height:.6rem;margin:0 -1rem;background:repeating-linear-gradient(90deg,var(--ink) 0 1.1rem,transparent 1.1rem 1.9rem)}
header{padding:1.3rem 0 .9rem}
.upd{font-family:var(--sans);font-size:.8rem;font-weight:500;color:var(--soft);display:flex;justify-content:space-between;gap:.5rem;flex-wrap:wrap}
h1{font-size:clamp(2.9rem,15vw,4.6rem);font-weight:850;font-stretch:118%;letter-spacing:-.035em;line-height:.9;margin:.45rem 0 .55rem}
.dek{font-size:1rem;color:var(--ink);max-width:34em}

/* tabs: sticky, four equal, active underlined */
.tabs{position:sticky;top:0;z-index:5;display:grid;grid-template-columns:repeat(4,1fr);background:var(--paper);border-bottom:2px solid var(--ink);margin:0 -1rem;padding:0 .5rem}
.tabs a{display:flex;align-items:center;justify-content:center;min-height:3rem;text-align:center;text-decoration:none;font-weight:700;font-size:.92rem;color:var(--soft);border-bottom:4px solid transparent;margin-bottom:-2px;line-height:1.15;padding:0 .2rem}
.tabs a.on{color:var(--ink);border-bottom-color:var(--purple)}
.tab[hidden]{display:none}

/* section heads: inverted bars, like the office headers on a ballot */
h2{margin:1.8rem -1rem .9rem;padding:.55rem 1rem .5rem;background:var(--ink);color:var(--paper);font-size:1.05rem;font-weight:700;font-stretch:105%;letter-spacing:.005em;line-height:1.25}
.tab>h2:first-child{margin-top:1.2rem}
h3{margin:0;font-weight:700;font-size:1.05rem;line-height:1.25}
.intro{font-size:.9rem;color:var(--soft);margin:-.2rem 0 .8rem}
.body{font-size:1rem}
.sub-h{margin:1.5rem 0 .5rem;font-size:1.1rem;padding-bottom:.35rem;border-bottom:2px solid var(--ink)}
.sub-h+.intro{margin-top:0}

/* dates strip */
.strip{display:grid;grid-template-columns:repeat(3,1fr);margin-top:1.2rem;border:1px solid var(--rule);background:var(--tint)}
.strip div{padding:.65rem .6rem .7rem;border-left:1px solid var(--rule);min-width:0}
.strip div:first-child{border-left:0}
.strip b{display:block;font-size:1.05rem;font-weight:800;font-stretch:88%;line-height:1.15}
.strip div:first-child b{color:var(--purple);font-size:1.3rem}
.strip span{display:block;font-size:.8rem;color:var(--soft);line-height:1.3;margin-top:.2rem}
.strip-n{margin:.5rem 0 0}

/* bottom line: filled ballot ovals, ranked */
.bottom{list-style:none;margin:0;padding:0}
.bottom li{display:grid;grid-template-columns:2.3rem 1fr;gap:.2rem .6rem;padding:.75rem 0;border-bottom:1px solid var(--rule)}
.bottom li:last-child{border-bottom:0}
.ov{width:2.05rem;height:1.3rem;border-radius:50%;background:var(--ink);color:var(--paper);font-size:.78rem;font-weight:700;display:flex;align-items:center;justify-content:center;margin-top:.12rem}
.bottom h3{font-size:1.12rem;font-weight:750;font-stretch:96%}
.bottom p{font-size:.98rem;margin-top:.2rem}

/* numbers */
.tiles{display:grid;grid-template-columns:1fr;border-top:1px solid var(--rule);border-left:1px solid var(--rule)}
.tiles:not(.results) .tile{display:grid;grid-template-columns:1fr auto;column-gap:.8rem;align-items:center}
.tiles:not(.results) .tile .big{grid-column:2;grid-row:1/3;margin:0;font-size:2rem}
@media(min-width:34rem){.tiles:not(.results){grid-template-columns:repeat(3,1fr)}.tiles:not(.results) .tile{display:block}.tiles:not(.results) .tile .big{margin:.35rem 0}}
.tiles.results{grid-template-columns:1fr 1fr}
.tile{padding:.65rem .55rem .75rem;border-right:1px solid var(--rule);border-bottom:1px solid var(--rule);min-width:0}
.lbl{font-size:.85rem;font-weight:700;color:var(--ink);line-height:1.25}
.tile .big{font-size:1.75rem;font-weight:800;font-stretch:78%;line-height:1;margin:.35rem 0 .35rem;white-space:nowrap}
.tile .big.d,.big .d{color:var(--blue)}.tile .big.r,.big .r{color:var(--red)}
.tile .sub{font-size:.78rem;color:var(--soft);line-height:1.4}
.tiles.results .big{font-size:clamp(1.8rem,10vw,2.6rem)}
.dash{color:var(--soft);font-weight:400;padding:0 .2rem}

/* plain bulleted lists */
.list{margin:0;padding:0;list-style:none}
.list li{padding:.6rem 0 .6rem 1.1rem;border-bottom:1px solid var(--rule);position:relative}
.list li:last-child{border-bottom:0}
.list li::before{content:"";position:absolute;left:0;top:1.2rem;width:.5rem;height:.32rem;border-radius:50%;background:var(--ink)}
.list b{font-family:var(--sans);font-weight:700}
.list .mut{font-size:.92rem}

/* race cards: one shape everywhere */
.races{list-style:none;margin:0;padding:0}
.race{padding:.85rem 0 .9rem;border-bottom:1px solid var(--rule)}
.races li:last-child{border-bottom:0}
.rh{display:flex;align-items:center;gap:.45rem;flex-wrap:wrap}
.rh h3{font-size:1.2rem;font-weight:750;margin-right:auto}
.area{font-family:var(--sans);font-size:.82rem;font-weight:500;color:var(--soft);margin-top:.1rem}
.chip{font-size:.75rem;font-weight:650;padding:.12rem .5rem;border-radius:1rem;white-space:nowrap;background:var(--tint);color:var(--ink)}
.chip.tu{background:var(--purple-t);color:var(--purple)}.chip.d{background:var(--blue-t);color:var(--blue)}.chip.r{background:var(--red-t);color:var(--red)}
.lead{font-size:1.05rem;font-weight:800;font-stretch:85%;white-space:nowrap;min-width:3.4rem;text-align:right}
.lead.d{color:var(--blue)}.lead.r{color:var(--red)}.lead.nx{color:var(--soft);font-weight:600;font-size:.9rem}
.dv{position:relative;height:.65rem;margin:.55rem 0 .45rem;background:linear-gradient(90deg,transparent calc(50% - 1px),var(--ink) calc(50% - 1px),var(--ink) calc(50% + 1px),transparent calc(50% + 1px)),var(--tint)}
.dv i{position:absolute;top:0;bottom:0}
.dv i.d{right:50%;background:var(--blue)}.dv i.r{left:50%;background:var(--red)}
.pt{font-family:var(--sans);font-weight:700;font-size:.78em;letter-spacing:.02em}.pt.d{color:var(--blue)}.pt.r{color:var(--red)}.pt.both{color:var(--purple)}
.say{font-size:1rem;line-height:1.5;margin-top:.35rem}
.say .mut{font-size:.88rem}
.res-l{font-family:var(--sans);font-weight:700;font-size:1.05rem}
.meta{font-size:.82rem;color:var(--soft);margin-top:.2rem;line-height:1.45}
.note{font-size:.88rem;line-height:1.5}
.note+.note{margin-top:.45rem}
.status{font-size:.75rem;font-weight:650;padding:.12rem .55rem;border-radius:1rem;border:1.5px solid var(--purple);color:var(--purple);white-space:nowrap}
.status.called{background:var(--ink);border-color:var(--ink);color:var(--paper)}

/* the one disclosure control */
.fold summary{cursor:pointer;list-style:none;display:flex;align-items:center;gap:.45rem;min-height:2.4rem;font-size:.85rem;font-weight:600;color:var(--soft)}
.fold summary::-webkit-details-marker{display:none}
.fold summary::after{content:"";width:.45rem;height:.45rem;border-right:2px solid currentColor;border-bottom:2px solid currentColor;transform:translateY(-25%) rotate(45deg);transition:transform .15s;flex:none}
.fold[open]>summary::after{transform:translateY(20%) rotate(-135deg)}
.fold .fb{padding:.1rem 0 .3rem}
.race .fold{margin-top:.15rem}
.race .fold summary{min-height:2rem}
.fold.town{border-bottom:1px solid var(--rule)}
.fold.town:first-of-type{border-top:1px solid var(--rule)}
.fold.town summary{min-height:3.1rem;color:var(--ink);align-items:baseline;padding-top:.85rem}
.fold.town summary::after{margin-left:auto;align-self:center}
.tn{font-weight:700;font-size:1.05rem}
.cty{font-size:.82rem;color:var(--soft);font-weight:500}
.fold.town dl{margin:0 0 .5rem}

/* definition rows: ballot, banner, glossary */
dl{margin:0}
.row{display:grid;grid-template-columns:minmax(5.5rem,32%) 1fr;gap:.75rem;padding:.5rem 0;border-bottom:1px solid var(--tint)}
.row:last-child{border-bottom:0}
dt{font-size:.8rem;font-weight:650;color:var(--soft);line-height:1.35;padding-top:.12rem;overflow-wrap:anywhere}
dd{margin:0;font-size:.92rem;line-height:1.45}
.row.ev dt{color:var(--purple)}
.hrs{display:block;font-size:.82rem;color:var(--soft);margin-top:.15rem}
.gloss dt{font-size:.88rem;color:var(--ink);font-weight:700;padding-top:0}
.gloss dd{font-size:.95rem;margin:.15rem 0 .9rem}

/* banner (early voting, Election Day) */
.banner{margin:1rem -1rem 0;padding:1.1rem 1rem 1rem;background:var(--purple);color:#fff}
.banner .bh{margin:0;padding:0;background:none;color:#fff;font-size:1.45rem;font-weight:800;font-stretch:95%;line-height:1.15}
.banner .bs{margin-top:.4rem;font-size:.95rem}
.banner a{color:#fff}
.banner dl{margin:.8rem 0 0;background:var(--paper);color:var(--ink);border-radius:.3rem;padding:.2rem .85rem}

.trend{border-collapse:collapse;width:100%;font-family:var(--sans);font-size:.85rem}
.trend th,.trend td{padding:.45rem .3rem;border-bottom:1px solid var(--rule);text-align:right}
.trend th{font-weight:600;color:var(--soft);font-size:.75rem;vertical-align:bottom}
.trend th:first-child,.trend td:first-child{text-align:left;padding-left:0}

.foot{font-size:.8rem;color:var(--soft);margin-top:2.4rem;padding-top:1rem;border-top:2px solid var(--ink);line-height:1.55}
@media(min-width:44rem){.page{padding:0 2rem 3rem}.marks,.tabs{margin:0 -2rem}.tabs{padding:0 1.5rem}h2,.banner{margin-left:-2rem;margin-right:-2rem;padding-left:2rem;padding-right:2rem}}
@media(prefers-reduced-motion:reduce){*{transition:none!important}}
"""

JS = """(function(){var T=['today','senate','house','ballot'],nav=document.querySelector('.tabs');
function cur(){var h=location.hash.slice(1);return T.indexOf(h)<0?'today':h}
function show(scroll){var t=cur();document.querySelectorAll('.tab').forEach(function(s){s.hidden=s.getAttribute('data-tab')!==t});
document.querySelectorAll('.tabs a').forEach(function(a){var on=a.getAttribute('data-tab')===t;a.classList.toggle('on',on);if(on)a.setAttribute('aria-current','page');else a.removeAttribute('aria-current')});
if(scroll&&window.scrollY>nav.offsetTop)window.scrollTo(0,nav.offsetTop)}
window.addEventListener('hashchange',function(){show(true)});show(false)})();"""

sb_m = sb["margin"]
TABS = [("today", "Today", tab_today), ("senate", "Senate", tab_senate), ("house", "House", tab_house), ("ballot", "My ballot", tab_ballot)]
nav = "".join(f'<a href="#{k}" data-tab="{k}"{" class=\"on\" aria-current=\"page\"" if k == "today" else ""}>{label}</a>' for k, label, _ in TABS)
sections = "".join(f'<section class="tab" data-tab="{k}" aria-label="{label}">{body}</section>' for k, label, body in TABS)

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex">
<meta name="theme-color" content="#1b1f2a">
<meta name="description" content="2026 midterm tracker — national polling, the Senate, and New York's races, refreshed every morning.">
<meta property="og:title" content="The Ballot — 2026 Midterm Tracker">
<meta property="og:description" content="Generic ballot {tracker_margin(sb_m)}; {num(ctrl["Toss-up seats (Cook)"],0)} Senate toss-ups; Hochul ahead by about {whole(g["margin"])} in New York. Updated {today.strftime("%b %-d")}.">
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
<p class="dek">National polling, the Senate map and New York's races, explained plainly and refreshed every morning through {fdate(D["election_day"])}.</p>
</header>
<nav class="tabs" aria-label="Sections">{nav}</nav>
{sections}
</div>
<script>{JS}</script>
</body></html>'''

open(OUT, "w").write(page)
print("built", OUT, len(page), "bytes; days to election:", days)
