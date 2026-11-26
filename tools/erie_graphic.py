"""Lake Erie graphic for the Weather Glass (Garret, Nov 25: "Bake in an image of Lake Erie showing lake temp,
ice cover % and seiche deets"). Inline SVG at 390px, the paper's palette.

    from erie_graphic import erie_block
    html = erie_block(json.load(open('data/climate.json')), erie_temp_f=52, temp_day='Tuesday')

Data: water temperature off Buffalo (forecast.json lakes, NWS Buffalo); ice cover (climate.json erie_ice,
NOAA GLERL; no column for the season yet = no ice yet); seiche (climate.json erie_levels, NOAA CO-OPS:
Buffalo 9063020 minus Toledo 9063085, IGLD 1985, hourly, last 24 hours; wind at the Buffalo gauge).
Returns '' if the level data is missing, so the paper never runs a half-empty graphic."""
import math
from datetime import datetime, timedelta

RUST, INK, SOFT, GREEN, BLUE, PAPER = '#9c3216', '#24170c', '#664a2c', '#2f5e3e', '#5b87a8', '#f8eedb'
# Simplified Lake Erie shoreline (lon, lat), west end first, north shore then south shore.
SHORE = [(-83.45, 41.73), (-83.15, 42.04), (-82.65, 41.98), (-82.50, 41.91), (-82.40, 42.02), (-81.85, 42.25),
         (-81.30, 42.55), (-80.70, 42.62), (-80.40, 42.57), (-80.05, 42.55), (-80.25, 42.66), (-79.75, 42.80),
         (-79.30, 42.87), (-78.92, 42.90), (-78.88, 42.86), (-79.05, 42.70), (-79.33, 42.49), (-79.75, 42.27),
         (-80.10, 42.14), (-80.55, 41.98), (-81.10, 41.80), (-81.70, 41.50), (-82.05, 41.48), (-82.50, 41.40),
         (-82.75, 41.48), (-83.05, 41.62), (-83.45, 41.73)]
TOWNS = {'Toledo': (-83.47, 41.69), 'Cleveland': (-81.69, 41.50), 'Erie, Pa.': (-80.09, 42.13), 'Dunkirk': (-79.33, 42.48),
         'Buffalo': (-78.88, 42.89)}
W = 380

def _xy(lon, lat):
    x0, x1, y0, y1 = -83.7, -78.6, 43.05, 41.30
    return round(14 + (lon - x0) / (x1 - x0) * (W - 28), 1), round(84 + (y0 - lat) / (y0 - y1) * 120, 1)

def _compass(d):
    return ['N', 'NNE', 'NE', 'ENE', 'E', 'ESE', 'SE', 'SSE', 'S', 'SSW', 'SW', 'WSW', 'W', 'WNW', 'NW', 'NNW'][int((d + 11.25) % 360 // 22.5)]

def _et(t):
    dt = datetime.strptime(t, '%Y-%m-%d %H:%M') - timedelta(hours=5)
    h = dt.hour % 12 or 12
    return f"{h}{'a' if dt.hour < 12 else 'p'}"

def erie_block(climate, erie_temp_f, temp_day):
    lv = climate.get('erie_levels') or {}
    tilt = [x for x in (lv.get('tilt_ft') or []) if x[0].endswith(':00')] or (lv.get('tilt_ft') or [])
    if len(tilt) < 6:
        return ''
    ice = climate.get('erie_ice') or {}
    ice_txt = f"{ice['last']['pct']:.0f}%" if ice.get('last') else '0%'
    ice_sub = f"as of {ice['last']['row']}" if ice.get('last') else 'no ice yet'
    now_t, now_ft = tilt[-1]
    inch = round(now_ft * 12)
    wind = lv.get('buffalo_wind') or {}
    o = [f'<svg viewBox="0 0 {W} 412" width="100%" style="max-width:{W}px;display:block;margin:.4rem auto 0" '
         f'xmlns="http://www.w3.org/2000/svg" font-family="Archivo,Arial,sans-serif" role="img" '
         f'aria-label="Lake Erie: water temperature, ice cover and how the lake is tilting between Toledo and Buffalo">']
    o.append(f'<text x="14" y="22" font-size="14" font-weight="800" fill="{INK}">Lake Erie this morning</text>')
    # three stat cells
    cells = [(f'{erie_temp_f}&#176;', 'water off Buffalo', temp_day), (ice_txt, 'ice cover', ice_sub)]
    if wind.get('dir_deg') is not None:
        mph = round(wind['speed_kn'] * 1.15078)
        g = f", gusts {round(wind['gust_kn'] * 1.15078)}" if wind.get('gust_kn') else ''
        cells.append((f"{_compass(wind['dir_deg'])} {mph}", 'mph wind', f"Buffalo gauge, {_et(wind['t'])}{g}"))
    cw = (W - 28) / len(cells)
    for i, (v, k, s) in enumerate(cells):
        x = 14 + i * cw + cw / 2
        o.append(f'<text x="{x}" y="46" font-size="17" font-weight="800" fill="{INK}" text-anchor="middle" font-family="Playfair Display,Georgia,serif">{v}</text>')
        o.append(f'<text x="{x}" y="58" font-size="8.5" font-weight="700" fill="{GREEN}" text-anchor="middle" letter-spacing=".06em">{k.upper()}</text>')
        o.append(f'<text x="{x}" y="69" font-size="8.5" fill="{SOFT}" text-anchor="middle">{s}</text>')
    # the lake
    pts = ' '.join(f'{x},{y}' for x, y in (_xy(*p) for p in SHORE))
    o.append(f'<polygon points="{pts}" fill="rgba(91,135,168,.28)" stroke="{BLUE}" stroke-width="1.5" stroke-linejoin="round"/>')
    for n, (lon, lat) in TOWNS.items():
        x, y = _xy(lon, lat)
        big = n in ('Toledo', 'Buffalo')
        o.append(f'<circle cx="{x}" cy="{y}" r="{4 if big else 2.5}" fill="{RUST if big else INK}"/>')
        dy = -8 if n in ('Buffalo',) else 13
        anchor = 'end' if n == 'Buffalo' else ('start' if n == 'Toledo' else 'middle')
        o.append(f'<text x="{x + (-6 if n=="Buffalo" else 0)}" y="{y + dy}" font-size="{10 if big else 9}" font-weight="{700 if big else 400}" fill="{INK}" text-anchor="{anchor}">{n}</text>')
    # wind arrow over the lake, pointing the way the wind blows
    if wind.get('dir_deg') is not None:
        cx, cy = _xy(-81.2, 42.2)
        a = math.radians((wind['dir_deg'] + 180) % 360)
        dx, dy = 30 * math.sin(a), -30 * math.cos(a)
        o.append(f'<defs><marker id="ew" markerWidth="8" markerHeight="8" refX="4" refY="4" orient="auto"><path d="M0,0 L8,4 L0,8z" fill="{INK}"/></marker></defs>')
        o.append(f'<line x1="{cx - dx:.1f}" y1="{cy - dy:.1f}" x2="{cx + dx:.1f}" y2="{cy + dy:.1f}" stroke="{INK}" stroke-width="2.5" marker-end="url(#ew)"/>')
        o.append(f'<text x="{cx:.1f}" y="{cy + 24:.1f}" font-size="8.5" fill="{INK}" text-anchor="middle">wind</text>')
    # seesaw: Buffalo minus Toledo
    y0 = 248
    o.append(f'<text x="14" y="{y0}" font-size="11" font-weight="800" fill="{INK}">The slosh (a seiche)</text>')
    if abs(inch) < 1:
        line = 'Level: Buffalo and Toledo within an inch.'
    else:
        line = f"Buffalo&#8217;s end is {abs(inch)} inch{'es' if abs(inch) != 1 else ''} {'higher' if inch > 0 else 'lower'} than Toledo&#8217;s."
    o.append(f'<text x="14" y="{y0 + 15}" font-size="10.5" fill="{INK}">{line}</text>')
    # 24-hour tilt chart, inches, zero line
    gx0, gx1, gy0, gy1 = 44, W - 16, y0 + 30, y0 + 112
    vals = [v * 12 for _, v in tilt]
    lim = max(6, math.ceil(max(abs(v) for v in vals) / 6) * 6)
    def gy(v): return gy0 + (lim - v) / (2 * lim) * (gy1 - gy0)
    def gx(i): return gx0 + i / (len(vals) - 1) * (gx1 - gx0)
    o.append(f'<rect x="{gx0}" y="{gy0}" width="{gx1 - gx0}" height="{gy(0) - gy0:.1f}" fill="rgba(156,50,22,.06)"/>')
    o.append(f'<rect x="{gx0}" y="{gy(0):.1f}" width="{gx1 - gx0}" height="{gy1 - gy(0):.1f}" fill="rgba(91,135,168,.08)"/>')
    o.append(f'<line x1="{gx0}" y1="{gy(0):.1f}" x2="{gx1}" y2="{gy(0):.1f}" stroke="{SOFT}" stroke-width="1" stroke-dasharray="3 3"/>')
    for v in (lim, 0, -lim):
        o.append(f'<text x="{gx0 - 4}" y="{gy(v) + 3:.1f}" font-size="8.5" fill="{SOFT}" text-anchor="end">{("+" if v > 0 else "") + str(v)}"</text>')
    o.append(f'<text x="{gx0 + 4}" y="{gy0 + 10}" font-size="8.5" fill="{RUST}">piled up at Buffalo</text>')
    o.append(f'<text x="{gx0 + 4}" y="{gy1 - 4}" font-size="8.5" fill="{BLUE}">piled up at Toledo</text>')
    path = ' '.join(f'{"M" if i == 0 else "L"}{gx(i):.1f},{gy(v):.1f}' for i, v in enumerate(vals))
    o.append(f'<path d="{path}" fill="none" stroke="{INK}" stroke-width="2"/>')
    o.append(f'<circle cx="{gx(len(vals) - 1):.1f}" cy="{gy(vals[-1]):.1f}" r="3.5" fill="{RUST}"/>')
    for i in (0, len(vals) // 2, len(vals) - 1):
        o.append(f'<text x="{gx(i):.1f}" y="{gy1 + 12}" font-size="8.5" fill="{SOFT}" text-anchor="{"start" if i == 0 else ("end" if i == len(vals) - 1 else "middle")}">{_et(tilt[i][0])}</text>')
    o.append(f'<text x="14" y="{gy1 + 30}" font-size="9" fill="{INK}">Southwest winds pile water at Buffalo; northeast winds push it to Toledo.</text>')
    o.append(f'<text x="14" y="{gy1 + 42}" font-size="9" fill="{INK}">When the wind quits, the lake sloshes back for hours.</text>')
    o.append('</svg>')
    cap = ('<div style="font-size:.78rem;font-style:italic;color:var(--soft,#664a2c);margin:.2rem 0 .6rem">'
           'Buffalo&#8217;s gauge minus Toledo&#8217;s, last 24 hours, in inches. Levels and wind: NOAA; water temperature: NWS Buffalo; ice: NOAA GLERL.</div>')
    return ''.join(o) + cap
