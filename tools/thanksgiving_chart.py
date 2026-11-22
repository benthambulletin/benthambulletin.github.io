"""Thanksgiving dinner cost graphic for the Sun Nov 22 Spotlight (Garret, Sat 9:05 p.m.:
"make a really cool chart graphic detailing the increase in meal costs").
Writes data/spotlight/thanksgiving-2026.html, a self-contained block the build drops into the Spotlight.
Every number is from the American Farm Bureau Federation's annual survey releases, checked Sat Nov 21
and again Sun Nov 22 against the fb.org 2026 release:
  2026 $58.63, about $5.86 per person, "more than a 6% increase from 2025"; item prices/changes
  (fb.org news release, Nov 2026; Feedstuffs agrees item by item); the item prices sum to $58.63
  2025 $55.18 (fb.org, Nov 19 2025) · 2024 $58.08 (fb.org 2024 release) · 2023 $61.17 (Iowa Farm Bureau)
  2022 $64.05 record (fb.org) · 2020 $46.90 (Statista, citing AFBF). 2021 deliberately left out (not verified).
  Regions 2026: Northeast $61.57, West $58.74, Midwest $56.89, South $54.33 (AFBF's Northeast includes New York)
  Expanded menu with ham, potatoes and green beans: $81.72 (fb.org 2026)
  Method line: volunteer shoppers, first week of November, all 50 states and Puerto Rico (fb.org 2026)
Worked out here from the figures above, not quoted: up $3.45 from 2025 (58.63 - 55.18);
turkey's share 40% ($23.68 of $58.63); everything else $34.95.
"""
INK, SOFT, RULE, RUST, FOREST, TAN, PAPER = "#24170c", "#664a2c", "#d3b88f", "#9c3216", "#2f5e3e", "#d9b98c", "#f8eedb"
F = "font-family=\"Archivo,Arial,sans-serif\""
LORA = "font-family=\"Lora,Georgia,serif\""

totals = [("2022", 64.05), ("2023", 61.17), ("2024", 58.08), ("2025", 55.18), ("2026", 58.63)]
Y2020 = 46.90
items = [("Turkey, 16 lb", 23.68, 10.1), ("Cranberries", 2.48, 8.8), ("Whole milk, gallon", 4.05, 8.6),
         ("Dinner rolls", 3.81, 7.0), ("Misc. ingredients", 3.84, 6.4), ("Stuffing", 3.91, 5.4),
         ("Sweet potatoes", 4.20, 5.0), ("Pumpkin pie mix", 4.24, 1.9), ("Whipping cream", 1.84, -1.6),
         ("Frozen peas", 1.99, -2.0), ("Pie crusts", 3.28, -2.7), ("Veggie tray", 1.31, -3.7)]
TOTAL = 58.63
assert abs(sum(p for _, p, _ in items) - TOTAL) < 0.005
TURKEY = items[0][1]

def bars():
    # Bars start at zero; a dashed reference line marks 2020 so the five-year dip reads against the pre-surge level.
    W, H, B, T = 360, 168, 24, 34
    bw, gap = 48, 12
    x0 = W - (len(totals) * bw + (len(totals) - 1) * gap) - 2   # leaves a left gutter for the 2020 label
    top = max(v for _, v in totals)
    Y = lambda v: T + (H - T - B) * (1 - v / top)
    o = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Bar chart: cost of Thanksgiving dinner for ten. 2022 $64.05, the record; 2023 $61.17; 2024 $58.08; 2025 $55.18; 2026 $58.63. In 2020 it was $46.90." style="display:block;width:100%;height:auto">']
    for i, (yr, v) in enumerate(totals):
        x = x0 + i * (bw + gap); cx = x + bw / 2; last = yr == "2026"
        o.append(f'<rect x="{x:.1f}" y="{Y(v):.1f}" width="{bw}" height="{H-B-Y(v):.1f}" fill="{RUST if last else TAN}" rx="2"/>')
        o.append(f'<text x="{cx:.1f}" y="{Y(v)-6:.1f}" {F} font-size="{15 if last else 13.5}" font-weight="{800 if last else 700}" fill="{RUST if last else INK}" text-anchor="middle">${v:.2f}</text>')
        o.append(f'<text x="{cx:.1f}" y="{H-6}" {F} font-size="13.5" font-weight="{800 if last else 600}" fill="{INK if last else SOFT}" text-anchor="middle">{yr}</text>')
        if yr == "2022":
            o.append(f'<text x="{cx:.1f}" y="{Y(v)-23:.1f}" {F} font-size="11" font-weight="800" letter-spacing="1" fill="{SOFT}" text-anchor="middle">RECORD</text>')
    y20 = Y(Y2020)
    o.append(f'<line x1="{x0-6}" x2="{W-2}" y1="{y20:.1f}" y2="{y20:.1f}" stroke="{INK}" stroke-opacity=".75" stroke-width="1.3" stroke-dasharray="4 3"/>')
    o.append(f'<text x="2" y="{y20-4:.1f}" {F} font-size="12.5" font-weight="800" fill="{INK}">2020</text>')
    o.append(f'<text x="2" y="{y20+13:.1f}" {F} font-size="12.5" font-weight="600" fill="{SOFT}">$46.90</text>')
    o.append(f'<line x1="0" x2="{W}" y1="{H-B}" y2="{H-B}" stroke="{INK}" stroke-width="1.2"/>')
    o.append('</svg>')
    return "".join(o)

def share():
    # One stacked bar: the turkey against the other eleven items.
    pct = TURKEY / TOTAL * 100
    rest = TOTAL - TURKEY
    lab = "font-family:Archivo,Arial,sans-serif;font-size:.8rem;font-weight:700;line-height:1.15;padding:.35rem .45rem"
    return (f'<div style="display:flex;border:1px solid {INK};margin:.1rem 0 0">'
            f'<div style="flex:0 0 {pct:.1f}%;background:{RUST};color:{PAPER};{lab}">Turkey<br>${TURKEY:.2f} &middot; {pct:.0f}%</div>'
            f'<div style="flex:1;background:{TAN};color:{INK};{lab}">The other 11 items<br>${rest:.2f} &middot; {100-round(pct)}%</div></div>')

def items_chart():
    W, rh, T = 360, 24, 18
    H = T + rh * len(items) + 3
    price_r, mid, scale = 170, 242, 6.4   # price column right edge; zero line; px per percent
    o = [f'<svg viewBox="0 0 {W} {H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Price of each item in 2026 and how it changed from 2025" style="display:block;width:100%;height:auto">']
    cap = f'{F} font-size="10.5" font-weight="800" letter-spacing=".8" fill="{SOFT}"'
    o.append(f'<text x="{price_r}" y="11" {cap} text-anchor="end">PRICE</text>')
    o.append(f'<text x="{mid-6}" y="11" {cap} fill="{FOREST}" text-anchor="end">CHEAPER</text>')
    o.append(f'<text x="{mid+6}" y="11" {cap} fill="{RUST}">PRICIER</text>')
    o.append(f'<line x1="{mid}" x2="{mid}" y1="{T-3}" y2="{H-1}" stroke="{INK}" stroke-width="1"/>')
    for i, (name, price, ch) in enumerate(items):
        y = T + i * rh; cy = y + rh / 2 + 4.5
        if i % 2 == 0:
            o.append(f'<rect x="0" y="{y}" width="{W}" height="{rh}" fill="{RULE}" fill-opacity=".2"/>')
        bold = ' font-weight="700"' if i == 0 else ''
        o.append(f'<text x="3" y="{cy:.1f}" {LORA} font-size="13.5" fill="{INK}"{bold}>{name}</text>')
        o.append(f'<text x="{price_r}" y="{cy:.1f}" {F} font-size="13" font-weight="600" fill="{SOFT}" text-anchor="end">${price:.2f}</text>')
        w = abs(ch) * scale; up = ch > 0
        x = mid if up else mid - w
        o.append(f'<rect x="{x:.1f}" y="{y+5}" width="{w:.1f}" height="{rh-10}" fill="{RUST if up else FOREST}" rx="1.5"/>')
        tx = mid + w + 4 if up else mid - w - 4
        o.append(f'<text x="{tx:.1f}" y="{cy:.1f}" {F} font-size="12.5" font-weight="700" fill="{RUST if up else FOREST}" text-anchor="{"start" if up else "end"}">{"+" if up else "&#8722;"}{abs(ch):.1f}%</text>')
    o.append('</svg>')
    return "".join(o)

def regions():
    reg = [("Northeast", 61.57), ("West", 58.74), ("Midwest", 56.89), ("South", 54.33)]
    cells = "".join(f'<div style="flex:1;text-align:center;padding:.35rem .1rem;{"background:rgba(156,50,22,.08);" if n=="Northeast" else ""}{"" if n=="South" else f"border-right:1px solid {RULE}"}"><div style="font-family:Archivo,Arial,sans-serif;font-size:.68rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:{FOREST}">{n}</div><div style="font-family:\'Playfair Display\',Georgia,serif;font-size:1.15rem;font-weight:700;color:{RUST if n=="Northeast" else INK}">${v:.2f}</div></div>' for n, v in reg)
    return f'<div style="display:flex;border-top:1px solid {INK};border-bottom:1px solid {INK};margin:.3rem 0 .2rem">{cells}</div>'

def head(t, top=".9rem"):
    return f'<div style="font-family:Archivo,Arial,sans-serif;font-size:.7rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:{FOREST};margin:{top} 0 .3rem">{t}</div>'

html = f'''<div class="tgchart" style="border:1px solid {RULE};border-top:3px double {INK};padding:.8rem .75rem .6rem;margin:.6rem 0 1rem;background:rgba(255,255,255,.25)">
<div style="font-family:Archivo,Arial,sans-serif;font-size:.7rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;color:{FOREST}">Thanksgiving dinner for ten</div>
<div style="display:flex;align-items:baseline;gap:.6rem;flex-wrap:wrap;margin:.15rem 0 .5rem"><span style="font-family:'Playfair Display',Georgia,serif;font-size:2.6rem;font-weight:900;line-height:1;color:{RUST}">$58.63</span><span style="font-family:Lora,Georgia,serif;font-style:italic;color:{INK};font-size:.95rem;line-height:1.35">About $5.86 a plate. Up $3.45 from last year, about 6%, the first rise since the 2022 record.</span></div>
{bars()}
{head("Where the money goes")}
{share()}
{head("What moved, 2025 to 2026")}
{items_chart()}
{head("By region &middot; ours pays the most")}
{regions()}
<div style="font-family:Lora,Georgia,serif;font-style:italic;font-size:.8rem;color:{SOFT};margin-top:.45rem;line-height:1.4">The classic meal for ten; add ham, potatoes and green beans and it&rsquo;s $81.72. American Farm Bureau Federation volunteers priced it in all 50 states and Puerto Rico the first week of November.</div>
</div>'''
open('/home/claude/site/data/spotlight/thanksgiving-2026.html', 'w').write(html)
print(len(html))
