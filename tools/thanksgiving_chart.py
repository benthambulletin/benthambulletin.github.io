"""Thanksgiving dinner cost graphic for the Sun Nov 22 Spotlight (Garret, Sat 9:05 p.m.:
"make a really cool chart graphic detailing the increase in meal costs").
Writes data/spotlight/thanksgiving-2026.html, a self-contained block the build drops into the Spotlight.
Every number is from the American Farm Bureau Federation's annual survey releases, checked Sat Nov 21:
  2026 $58.63 and item prices/changes (fb.org news release, Nov 2026; Feedstuffs agrees item by item)
  2025 $55.18 (fb.org, Nov 19 2025) · 2024 $58.08 (fb.org 2024 release) · 2023 $61.17 (Iowa Farm Bureau)
  2022 $64.05 record (fb.org) · 2020 $46.90 (Statista, citing AFBF)
  Regions 2026: Northeast $61.57, West $58.74, Midwest $56.89, South $54.33
"""
INK, SOFT, RULE, RUST, FOREST, TAN, PAPER = "#24170c", "#664a2c", "#d3b88f", "#9c3216", "#2f5e3e", "#d9b98c", "#f8eedb"
F = "font-family=\"Archivo,Arial,sans-serif\""
SERIF = "font-family=\"Playfair Display,Georgia,serif\""

totals = [("2022", 64.05), ("2023", 61.17), ("2024", 58.08), ("2025", 55.18), ("2026", 58.63)]
items = [("Turkey, 16 lb", 23.68, 10.1), ("Cranberries", 2.48, 8.8), ("Whole milk, gallon", 4.05, 8.6),
         ("Dinner rolls", 3.81, 7.0), ("Odds and ends", 3.84, 6.4), ("Stuffing", 3.91, 5.4),
         ("Sweet potatoes", 4.20, 5.0), ("Pumpkin pie mix", 4.24, 1.9), ("Whipping cream", 1.84, -1.6),
         ("Frozen peas", 1.99, -2.0), ("Pie crusts", 3.28, -2.7), ("Veggie tray", 1.31, -3.7)]

def bars():
    W, H, L, B, T = 360, 210, 8, 26, 30
    bw, gap = 50, 20
    x0 = (W - (len(totals) * bw + (len(totals) - 1) * gap)) / 2
    top = 70.0
    Y = lambda v: T + (H - T - B) * (1 - v / top)
    o = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Bar chart: cost of Thanksgiving dinner for ten, 2022 to 2026" style="display:block;width:100%;height:auto">']
    for i, (yr, v) in enumerate(totals):
        x = x0 + i * (bw + gap); last = yr == "2026"; rec = yr == "2022"
        fill = RUST if last else TAN
        o.append(f'<rect x="{x:.1f}" y="{Y(v):.1f}" width="{bw}" height="{H-B-Y(v):.1f}" fill="{fill}" rx="2"/>')
        o.append(f'<text x="{x+bw/2:.1f}" y="{Y(v)-6:.1f}" {F} font-size="{14 if last else 12}" font-weight="700" fill="{RUST if last else INK}" text-anchor="middle">${v:.2f}</text>')
        o.append(f'<text x="{x+bw/2:.1f}" y="{H-8}" {F} font-size="12" font-weight="{800 if last else 600}" fill="{INK if last else SOFT}" text-anchor="middle">{yr}</text>')
        if rec:
            o.append(f'<text x="{x+bw/2:.1f}" y="{Y(v)-21:.1f}" {F} font-size="9.5" font-weight="800" letter-spacing="1" fill="{SOFT}" text-anchor="middle">RECORD</text>')
        if last:
            o.append(f'<text x="{x+bw/2:.1f}" y="{Y(v)-23:.1f}" {F} font-size="10" font-weight="800" fill="{RUST}" text-anchor="middle">UP 6%</text>')
    y20 = Y(46.90)
    o.append(f'<line x1="{L}" x2="{W-L}" y1="{y20:.1f}" y2="{y20:.1f}" stroke="{INK}" stroke-width="1.3" stroke-dasharray="4 3"/>')
    o.append(f'<line x1="{L}" x2="{W-L}" y1="{H-B}" y2="{H-B}" stroke="{INK}" stroke-width="1.2"/>')
    o.append('</svg>')
    o.append(f'<div style="font-family:Archivo,Arial,sans-serif;font-size:.68rem;color:{SOFT};margin:.15rem 0 0"><span style="letter-spacing:1px;color:{INK};font-weight:800">- - -</span> 2020, before the jump: $46.90</div>')
    return "".join(o)

def items_chart():
    W, rh, T = 360, 23, 6
    H = T + rh * len(items) + 4
    lab, mid, scale = 108, 238, 8.0   # label column; zero line; px per percent
    o = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="How each item changed in price from 2025 to 2026" style="display:block;width:100%;height:auto">']
    o.append(f'<line x1="{mid}" x2="{mid}" y1="{T-2}" y2="{H-2}" stroke="{INK}" stroke-width="1"/>')
    for i, (name, price, ch) in enumerate(items):
        y = T + i * rh; cy = y + rh / 2
        if i % 2 == 0:
            o.append(f'<rect x="0" y="{y}" width="{W}" height="{rh}" fill="{RULE}" fill-opacity=".18"/>')
        bold = ' font-weight="700"' if i == 0 else ''
        o.append(f'<text x="4" y="{cy+4:.1f}" font-family="Lora,Georgia,serif" font-size="12.5" fill="{INK}"{bold}>{name}</text>')
        o.append(f'<text x="{lab+52}" y="{cy+4:.1f}" {F} font-size="11.5" fill="{SOFT}" text-anchor="end">${price:.2f}</text>')
        w = abs(ch) * scale; up = ch > 0
        x = mid if up else mid - w
        o.append(f'<rect x="{x:.1f}" y="{y+5}" width="{w:.1f}" height="{rh-10}" fill="{RUST if up else FOREST}" rx="1.5"/>')
        tx = mid + w + 4 if up else mid - w - 4
        o.append(f'<text x="{tx:.1f}" y="{cy+4:.1f}" {F} font-size="11" font-weight="700" fill="{RUST if up else FOREST}" text-anchor="{"start" if up else "end"}">{"+" if up else "&#8722;"}{abs(ch):.1f}%</text>')
    o.append('</svg>')
    return "".join(o)

def regions():
    reg = [("Northeast", 61.57), ("West", 58.74), ("Midwest", 56.89), ("South", 54.33)]
    cells = "".join(f'<div style="flex:1;text-align:center;padding:.35rem .1rem;{"background:rgba(156,50,22,.08);" if n=="Northeast" else ""}border-right:1px solid {RULE}"><div style="font-family:Archivo,Arial,sans-serif;font-size:.6rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:{FOREST}">{n}</div><div style="font-family:\'Playfair Display\',Georgia,serif;font-size:1.05rem;font-weight:700;color:{RUST if n=="Northeast" else INK}">${v:.2f}</div></div>' for n, v in reg)
    return f'<div style="display:flex;border-top:1px solid {INK};border-bottom:1px solid {INK};margin:.3rem 0 .2rem">{cells}</div>'

def head(t):
    return f'<div style="font-family:Archivo,Arial,sans-serif;font-size:.62rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:{FOREST};margin:.9rem 0 .3rem">{t}</div>'

html = f'''<div class="tgchart" style="border:1px solid {RULE};border-top:3px double {INK};padding:.8rem .75rem .6rem;margin:.6rem 0 1rem;background:rgba(255,255,255,.25)">
<div style="font-family:Archivo,Arial,sans-serif;font-size:.62rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:{FOREST}">The bill for ten</div>
<div style="display:flex;align-items:baseline;gap:.6rem;flex-wrap:wrap;margin:.15rem 0 .1rem"><span style="font-family:'Playfair Display',Georgia,serif;font-size:2.6rem;font-weight:900;line-height:1;color:{RUST}">$58.63</span><span style="font-family:Lora,Georgia,serif;font-style:italic;color:{SOFT};font-size:.95rem">about $5.86 a plate &middot; up 6% from last year, first rise since the 2022 record</span></div>
{bars()}
{head("What moved, 2025 to 2026")}
{items_chart()}
{head("By region &middot; we pay the most")}
{regions()}
<div style="font-family:Lora,Georgia,serif;font-style:italic;font-size:.75rem;color:{SOFT};margin-top:.45rem;line-height:1.35">The classic meal for ten. Prices checked by volunteer shoppers in all 50 states the first week of November. American Farm Bureau Federation.</div>
</div>'''
open('/home/claude/site/data/spotlight/thanksgiving-2026.html', 'w').write(html)
print(len(html))
