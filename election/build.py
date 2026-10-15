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
    """A diverging bar for a D−R margin, as a tiny table-free HTML."""
    if m is None: return '<span class="nopoll">no public poll</span>'
    m = float(m); w = min(abs(m) / scale * 50, 50)
    side = "d" if m >= 0 else "r"
    return (f'<span class="bar"><span class="half">{"" if side=="d" else f"<i class=r style=width:{w}%></i>"}</span>'
            f'<span class="half">{f"<i class=d style=width:{w}%></i>" if side=="d" else ""}</span></span>')

# ---------- sections ----------
bottom = "".join(
    f'<li><b>{e(r["headline"])}</b><span>{e(r["detail"])}</span></li>'
    for r in sorted(D["bottom_line"], key=lambda r: r["order"]))

changed = ""
if D.get("what_changed"):
    changed = '<h2>What changed since yesterday</h2><ul class="changed">' + "".join(
        f"<li>{e(c)}</li>" for c in D["what_changed"]) + "</ul>"

sb = gb["Silver Bulletin (all polls)"]; rcp = gb["RealClearPolling average"]; avg = ap["Average of trackers"]
tiles = f'''
<div class="tiles">
 <div class="tile"><div class="lbl">Generic ballot</div><div class="big">D +{num(sb["margin"])}</div><div class="sub">Silver Bulletin, {fdate(sb["as_of"])} · RCP D +{num(rcp["margin"])}</div></div>
 <div class="tile"><div class="lbl">Trump net approval</div><div class="big">{net(avg["net"])}</div><div class="sub">{num(avg["approve"])}% approve · {num(avg["disapprove"])}% disapprove</div></div>
 <div class="tile"><div class="lbl">Odds of a Democratic Senate</div><div class="big">{num(ctrl["Polymarket odds of Democratic Senate (%)"],0)}%</div><div class="sub">Polymarket · {num(ctrl["Toss-up seats (Cook)"],0)} Cook toss-ups · Dems need net +{num(ctrl["Net seats Democrats need for 51"],0)}</div></div>
 <div class="tile"><div class="lbl">Days to Election Day</div><div class="big">{days}</div><div class="sub">Nov 3 · early voting {fdate(D["early_voting"]["start"])}–{fdate(D["early_voting"]["end"])}</div></div>
</div>'''

senate_rows = "".join(f'''<tr><td><b>{e(r["state"])}</b><br><span class="mut">{e(r["cook_rating"])} · held {e(r["held_by"])}</span></td>
<td>{e(r["democrat"])}<br><span class="mut">vs {e(r["republican"])}</span></td>
<td class="barcell">{bar(r["margin"])}<br><span class="mut">{margin(r["margin"])}{(" · " + e(r["pollster"]) + ", " + e(r["dates"])) if r["pollster"] else ""}</span></td></tr>'''
    for r in sorted(D["senate"], key=lambda r: (r["margin"] is None, -(r["margin"] or 0))))
senate_notes = "".join(f'<li><b>{e(r["state"])}:</b> {e(r["note"])}</li>' for r in D["senate"] if r.get("note"))

gov_rows = "".join(f'''<tr><td>{e(r["poll"])}<br><span class="mut">{e(r["dates"])}{(" · " + e(r["sample"])) if r["sample"] and r["sample"] != "—" else ""}</span></td>
<td class="n d">{num(r["hochul"])}%</td><td class="n r">{num(r["blakeman"])}%</td><td class="n"><b>Hochul +{num(r["margin"])}</b></td></tr>''' for r in D["ny_governor"])

house_rows = "".join(f'''<tr><td><b>{e(r["district"])}</b><br><span class="mut">{e(r["area"])}</span></td>
<td><span class="{r["party"].lower()}">{e(r["incumbent"])} ({e(r["party"])})</span><br><span class="mut">vs {e(r["challenger"])}</span></td>
<td>{e(r["rating"])}<br><span class="mut">{("Latest: " + e(r["pollster"]) + " " + num(r["dem_pct"]) + "–" + num(r["rep_pct"])) if r["pollster"] else e(r["note"] or "")}</span></td></tr>''' for r in D["ny_house"])

local_rows = "".join(f'<tr><td><b>{e(r["contest"])}</b><br><span class="mut">{e(r["area"])}</span></td><td>{e(r["candidates"])}<br><span class="mut">{e(r["what_to_know"])}</span></td></tr>' for r in D["local"])

dates_rows = "".join(f'<tr><td>{e(r["event"])}</td><td>{fdate(r["date"], "%a, %b %-d")}</td><td class="mut">{e(r["note"] or "")}</td></tr>' for r in D["key_dates"])

trend = ""
if len(D.get("history", [])) > 1:
    pts = D["history"]
    trend = '<h2>Trend</h2><table class="plain"><tr><th>Date</th><th class="n">Generic ballot</th><th class="n">Trump net</th><th class="n">D Senate odds</th><th class="n">Hochul margin</th></tr>' + "".join(
        f'<tr><td>{fdate(p["date"])}</td><td class="n">D +{num(p["generic_ballot"])}</td><td class="n">{net(p["trump_net"])}</td><td class="n">{num(p["dem_senate_odds"],0)}%</td><td class="n">+{num(p["hochul_margin"])}</td></tr>'
        for p in pts[-14:]) + "</table>"

page = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="robots" content="noindex">
<meta name="description" content="2026 midterm tracker — national polling, the Senate, and New York's races, refreshed every morning.">
<meta property="og:title" content="The Ballot — 2026 Midterm Tracker">
<meta property="og:description" content="Democrats lead the generic ballot by {num(sb["margin"])}; {num(ctrl["Toss-up seats (Cook)"],0)} Senate toss-ups; Hochul up {num(gov["Emerson College / PIX11"]["margin"])} in New York. Updated {today.strftime("%b %-d")}.">
<meta property="og:url" content="https://benthambulletin.github.io/election/">
<meta property="og:type" content="website">
<meta http-equiv="Cache-Control" content="no-cache">
<link rel="icon" href="/assets/favicon.svg">
<title>The Ballot — 2026 Midterm Tracker</title>
<style>
@font-face{{font-family:'PF';src:url(/assets/fonts/PlayfairDisplay.ttf);font-weight:100 900;font-display:swap}}
@font-face{{font-family:'LO';src:url(/assets/fonts/Lora.ttf);font-weight:100 900;font-display:swap}}
@font-face{{font-family:'AR';src:url(/assets/fonts/Archivo.ttf);font-weight:100 900;font-display:swap}}
:root{{--paper:#fbf5e4;--ink:#1c170f;--red:#c8302f;--blue:#2e5fa3;--gold:#e8b100;--soft:#5f5238;--rule:#d6cbaf;--wash:#f3ead2}}
*{{box-sizing:border-box}}
html{{background:#ece4d1}}
body{{margin:0;background:var(--paper);color:var(--ink);font-family:'LO',Georgia,serif;font-size:1.05rem;line-height:1.45;font-weight:480;-webkit-text-size-adjust:100%;font-variant-numeric:tabular-nums}}
.page{{max-width:44rem;margin:0 auto;padding:1.1rem 1.1rem 2.4rem}}
a{{color:inherit}}
.kicker{{display:flex;justify-content:space-between;gap:1rem;font-family:'AR';font-size:.58rem;letter-spacing:.12em;text-transform:uppercase;color:var(--soft);font-weight:600;margin-bottom:.4rem}}
.dbl .a{{height:3px;background:var(--ink)}}.dbl .b{{height:1px;background:var(--ink);margin-top:3px}}.dbl{{margin:.5rem 0 .9rem}}
h1{{margin:.5rem 0 0;text-align:center;font-family:'PF';font-weight:800;font-size:clamp(2rem,9vw,3.2rem);line-height:.95;letter-spacing:-.01em}}
.tag{{text-align:center;font-family:'AR';font-weight:700;font-size:.66rem;letter-spacing:.14em;text-transform:uppercase;color:var(--soft);margin-top:.45rem}}
.orn{{text-align:center;color:var(--gold);font-size:1rem;letter-spacing:.9em;margin:.5rem 0 .4rem}}
h2{{font-family:'AR';font-weight:700;font-size:.72rem;letter-spacing:.14em;text-transform:uppercase;color:var(--soft);margin:1.6rem 0 .5rem;padding-bottom:.25rem;border-bottom:1px solid var(--ink)}}
.bottom{{list-style:none;margin:0;padding:0;counter-reset:n}}
.bottom li{{position:relative;padding:.45rem 0 .45rem 2.1rem;border-bottom:1px solid var(--rule);counter-increment:n}}
.bottom li::before{{content:counter(n);position:absolute;left:0;top:.5rem;width:1.5rem;height:1.5rem;border-radius:50%;background:var(--ink);color:var(--paper);font-family:'AR';font-weight:700;font-size:.8rem;display:flex;align-items:center;justify-content:center}}
.bottom b{{display:block;font-family:'PF';font-weight:700;font-size:1.08rem;line-height:1.2}}
.bottom span{{display:block;color:var(--soft);font-size:.92rem;margin-top:.1rem}}
.tiles{{display:grid;grid-template-columns:repeat(2,1fr);gap:.6rem;margin-top:.9rem}}
.tile{{background:var(--wash);border:1px solid var(--rule);padding:.6rem .7rem;min-width:0}}
.tile .lbl{{font-family:'AR';font-size:.58rem;letter-spacing:.1em;text-transform:uppercase;color:var(--soft);font-weight:600}}
.tile .big{{font-family:'PF';font-weight:800;font-size:2rem;line-height:1.05;margin:.15rem 0}}
.tile .sub{{font-size:.78rem;color:var(--soft);line-height:1.3}}
table{{width:100%;border-collapse:collapse;font-size:.92rem}}
td,th{{padding:.45rem .3rem;border-bottom:1px solid var(--rule);vertical-align:top;text-align:left}}
th{{font-family:'AR';font-size:.6rem;letter-spacing:.1em;text-transform:uppercase;color:var(--soft);font-weight:600}}
td.n,th.n{{text-align:right;white-space:nowrap}}
.mut{{color:var(--soft);font-size:.8rem}}
.d{{color:var(--blue)}}.r{{color:var(--red)}}
.barcell{{min-width:9rem}}
.bar{{display:flex;width:100%;height:.7rem;margin:.2rem 0 .15rem}}
.bar .half{{flex:1;position:relative;border-left:1px solid var(--rule)}}
.bar .half:first-child{{border-left:0;border-right:1px solid var(--ink)}}
.bar i{{position:absolute;top:0;bottom:0;display:block}}
.bar i.d{{left:0;background:var(--blue)}}.bar i.r{{right:0;background:var(--red)}}
.nopoll{{color:var(--soft);font-size:.8rem;font-style:italic}}
.notes{{font-size:.88rem;color:var(--soft);padding-left:1.1rem;margin:.5rem 0 0}}
.notes li{{margin:.2rem 0}}
.changed{{padding-left:1.1rem;margin:0}}.changed li{{margin:.25rem 0}}
.legend{{font-size:.78rem;color:var(--soft);margin:.3rem 0 .2rem}}
.legend i{{display:inline-block;width:.7rem;height:.7rem;vertical-align:middle;margin-right:.3rem}}
.foot{{font-size:.8rem;color:var(--soft);margin-top:1.8rem;line-height:1.4}}
.foot a{{text-decoration:underline}}
@media(max-width:380px){{.tiles{{grid-template-columns:1fr 1fr}}.tile .big{{font-size:1.7rem}}}}
</style>
</head>
<body><div class="page">
<div class="kicker"><span>The Bentham Bulletin</span><span>Updated {today.strftime("%A, %B %-d, %Y")}</span></div>
<div class="dbl"><div class="a"></div><div class="b"></div></div>
<h1>The Ballot</h1>
<div class="tag">2026 Midterm Tracker · Refreshed every morning through Nov 3</div>
<div class="orn">✦ ✦ ✦</div>

<h2>The bottom line</h2>
<ol class="bottom">{bottom}</ol>
{changed}
{tiles}

<h2>Senate battleground</h2>
<div class="legend"><i style="background:var(--blue)"></i>Democrat ahead &nbsp; <i style="background:var(--red)"></i>Republican ahead &nbsp; · latest public poll or average</div>
<table>{senate_rows}</table>
<ul class="notes">{senate_notes}</ul>

<h2>New York governor</h2>
<table><tr><th>Poll</th><th class="n">Hochul</th><th class="n">Blakeman</th><th class="n">Margin</th></tr>{gov_rows}</table>
<p class="mut">Blakeman leads Upstate and among independents; Hochul's margin comes from New York City.</p>

<h2>House seats we watch</h2>
<table>{house_rows}</table>

<h2>Niagara County &amp; North Tonawanda</h2>
<table>{local_rows}</table>

<h2>Key dates</h2>
<table>{dates_rows}</table>
{trend}

<div class="foot">Sources: Silver Bulletin, RealClearPolling, Cook Political Report, Sabato's Crystal Ball, Emerson College, Marist, NYT/Siena, CNN, WRAL/SurveyUSA, Trafalgar, Pollsmax, PoliAgg/VoteHub, Polymarket, Kalshi; local coverage from the Ken-Ton Bee, WGRZ and the Niagara Gazette. Polls are snapshots with margins of error of 3–5 points; a lead inside that range is a coin flip. Compiled by the Bulletin's editor each morning; <a href="/election/data.json">the underlying numbers</a> carry a source link per row. <a href="/">Back to the Bulletin</a>.</div>
</div></body></html>'''

open(ROOT / "index.html", "w").write(page)
print("built election/index.html", len(page), "bytes; days to election:", days)
