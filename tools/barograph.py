#!/usr/bin/env python3
"""Barograph trace from the hourly log: the last 72 hours at KIAG.

Usage: python3 tools/barograph.py [migraine_iso_times...]
Prints the HTML for the .baro-top dial row and the .baro SVG, using
data/pressure-summary.json. Dial score and trend come from the 3/12/24-hour
changes; migraine times (ISO, local or Z) get a red tick on the trace.
"""
import json, sys
from datetime import datetime, timedelta, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EDT = timezone(timedelta(hours=-4))  # switch to -5 after Nov 1
if datetime.now(timezone.utc) > datetime(2026, 11, 1, 6, tzinfo=timezone.utc):
    EDT = timezone(timedelta(hours=-5))


def build(marks=()):
    s = json.load(open(ROOT / "data" / "pressure-summary.json"))["stations"]["KIAG"]
    pts = [(datetime.strptime(t, "%Y-%m-%dT%H:%MZ").replace(tzinfo=timezone.utc), mb) for t, mb in s["hourly_7d"]]
    end = pts[-1][0]; start = end - timedelta(hours=72)
    pts = [(t, mb * 0.0295300) for t, mb in pts if t >= start]  # mb -> inHg
    lo = min(v for _, v in pts); hi = max(v for _, v in pts)
    lo = min(lo, hi - 0.10); pad = (hi - lo) * 0.12; lo -= pad; hi += pad
    X0, X1, Y0, Y1 = 64, 790, 14, 150
    x = lambda t: X0 + (t - start).total_seconds() / (72 * 3600) * (X1 - X0)
    y = lambda v: Y1 - (v - lo) / (hi - lo) * (Y1 - Y0)
    poly = " ".join(f"{x(t):.0f},{y(v):.0f}" for t, v in pts)
    g = []
    for i in range(4):
        v = hi - (hi - lo) * i / 3; yy = y(v)
        g.append(f'<line x1="{X0}" y1="{yy:.0f}" x2="{X1}" y2="{yy:.0f}" stroke="#d6cbaf"/><text x="12" y="{yy+4:.0f}">{v:.2f}</text>')
    days = []
    d = start.astimezone(EDT).replace(hour=0, minute=0) + timedelta(days=1)
    while d.astimezone(timezone.utc) < end:
        xx = x(d.astimezone(timezone.utc))
        days.append(f'<line x1="{xx:.0f}" y1="{Y0}" x2="{xx:.0f}" y2="{Y1}" stroke="#e6dcc2" stroke-dasharray="3 4"/><text x="{xx+4:.0f}" y="172">{d.strftime("%a")}</text>')
        d += timedelta(days=1)
    mk = []
    for m in marks:
        t = datetime.fromisoformat(m.replace("Z", "+00:00"))
        if t.tzinfo is None: t = t.replace(tzinfo=EDT)
        t = t.astimezone(timezone.utc)
        if start <= t <= end:
            mk.append(f'<line x1="{x(t):.0f}" y1="{Y0}" x2="{x(t):.0f}" y2="{Y1}" stroke="#c8302f" stroke-width="2"/>')
    lt, lv = pts[-1]
    d3, d12, d24 = s["d3h_mb"], s["d12h_mb"], s["d24h_mb"]
    score = min(100, round(abs(d24) * 6 + abs(d12) * 4 + abs(d3) * 6))
    # house rule (CLAUDE.md): a 24-hour fall of 3 mb is MODERATE, 5 mb is HIGH,
    # and a fast fall of 1.5 mb in three hours is HIGH regardless
    if d24 <= -5 or d3 <= -1.5:
        score = max(score, 60)
    elif d24 <= -3:
        score = max(score, 35)
    level = "High" if score >= 60 else "Moderate" if score >= 35 else "Low"
    arrow = "&#8593;" if d12 > 0.8 else "&#8595;" if d12 < -0.8 else "&#8212;"
    word = "rising" if d12 > 0.8 else "falling" if d12 < -0.8 else "steady"
    dial_cls = "dial hi" if level == "High" else "dial"
    top = (f'<div class="baro-top"><div class="{dial_cls}">{level} &middot; {score}/100</div>'
           f'<div class="press">{lv:.2f}&#8243;</div><div class="trend">{arrow} {word} overnight</div></div>')
    svg = (f'<div class="baro"><svg viewBox="0 0 820 180" xmlns="http://www.w3.org/2000/svg">'
           f'<g font-family="AR" font-size="13" fill="#6b5f44">{"".join(g)}{"".join(days)}</g>{"".join(mk)}'
           f'<polyline points="{poly}" fill="none" stroke="#0e8a8a" stroke-width="3" stroke-linejoin="round"/>'
           f'<circle cx="{x(lt):.0f}" cy="{y(lv):.0f}" r="7" fill="#c8302f"/><circle cx="{x(lt):.0f}" cy="{y(lv):.0f}" r="15" fill="none" stroke="#c8302f" stroke-width="2.5"/>'
           f'<text x="{X1}" y="172" font-family="AR" font-size="13" font-weight="700" fill="#c8302f" text-anchor="end">Now {lv:.2f}</text></svg></div>')
    return top, svg, {"latest_utc": lt.strftime("%Y-%m-%dT%H:%MZ"), "in": round(lv, 2), "d3h_mb": d3, "d12h_mb": d12, "d24h_mb": d24, "score": score}


if __name__ == "__main__":
    top, svg, meta = build(sys.argv[1:])
    print(top); print(svg); print("<!--", json.dumps(meta), "-->")
