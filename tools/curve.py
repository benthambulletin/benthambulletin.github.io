"""The 24-hour curve for the Weather Glass (Garret, Nov 14: the old sparkline was "bare").
from curve import curve; curve(forecast['towns']['North Tonawanda']['hourly'], sunrise_minutes, sunset_minutes)
Returns the <svg> with data-start set; the generator adds the NOW ring and the motion."""
import json, datetime
def curve(hourly, rise_min, set_min):
    h = hourly[:24]; T = [x['temp'] for x in h]; n = len(T)
    st = datetime.datetime.fromisoformat(h[0]['start']).hour
    W, H = 340, 150; L, Rr, top, base = 14, 14, 26, 96   # plot box; bars and axis below
    lo, hi = min(T), max(T); span = max(4, hi - lo)
    X = lambda i: L + i * (W - L - Rr) / (n - 1)
    Y = lambda t: base - (t - lo) * (base - top) / span
    pts = ' '.join(f'{X(i):.1f},{Y(t):.1f}' for i, t in enumerate(T))
    o = [f'<svg viewBox="0 0 {W} {H}" style="display:block;width:100%;max-width:460px;height:auto;margin:0 auto .5rem" data-start="{st}" role="img" aria-label="Hourly temperatures and rain chances for North Tonawanda over the next 24 hours, high {hi}, low {lo}">']
    # after-dark shading, one rect per run of dark hours
    def hr_of(i): return (st + i) % 24
    dark = [not (rise_min <= hr_of(i) * 60 + 30 <= set_min) for i in range(n - 1)]
    i = 0
    while i < n - 1:
        if dark[i]:
            j = i
            while j < n - 1 and dark[j]: j += 1
            o.append(f'<rect x="{X(i):.1f}" y="{top-14}" width="{X(j)-X(i):.1f}" height="{base-top+14}" fill="#24170c" opacity=".07"/>')
            i = j
        else: i += 1
    # freezing line
    if lo <= 32 <= hi:
        o.append(f'<line x1="{L}" y1="{Y(32):.1f}" x2="{W-Rr}" y2="{Y(32):.1f}" stroke="#0e6a8a" stroke-width="1" stroke-dasharray="2 4"/>')
    # area + line
    o.append(f'<polygon points="{X(0):.1f},{base} {pts} {X(n-1):.1f},{base}" fill="#9c3216" opacity=".10"/>')
    o.append(f'<polyline points="{pts}" fill="none" stroke="#9c3216" stroke-width="2.2" stroke-linejoin="round" stroke-linecap="round"/>')
    # rain chance bars from the forecast wording
    def bar(x):   # height 0-15: the feed's percent when it has one, else the forecast wording
        if x.get('pop') is not None: return round(x['pop'] * 15 / 100) if x['pop'] >= 15 else 0
        s = x['short']
        if not any(k in s for k in ('Rain', 'Shower', 'Snow', 'Drizzle', 'Storm', 'Sleet')): return 0
        return 5 if 'Slight Chance' in s else 10 if 'Chance' in s else 15
    bw = (W - L - Rr) / (n - 1) * .62
    for i, x in enumerate(h):
        v = bar(x)
        if v: o.append(f'<rect x="{X(i)-bw/2:.1f}" y="{base+22-v:.1f}" width="{bw:.1f}" height="{v}" rx="1" fill="{"#b9c7d6" if "Snow" in x["short"] and "Rain" not in x["short"] else "#7fb2c9"}"/>')
    o.append(f'<line x1="{L}" y1="{base+22}" x2="{W-Rr}" y2="{base+22}" stroke="#d3b88f" stroke-width="1"/>')
    # every three hours: dot, temperature, clock label
    def clk(hh): return 'noon' if hh == 12 else 'mid' if hh == 0 else f'{hh % 12 or 12}{"a" if hh < 12 else "p"}'
    for i in range(0, n, 3):
        o.append(f'<circle cx="{X(i):.1f}" cy="{Y(T[i]):.1f}" r="2.4" fill="#f8eedb" stroke="#9c3216" stroke-width="1.4"/>'
                 f'<text x="{X(i):.1f}" y="{Y(T[i])-7:.1f}" text-anchor="middle" font-family="Archivo,Arial" font-size="9.5" font-weight="700" fill="#24170c">{T[i]}&deg;</text>'
                 f'<text x="{X(i):.1f}" y="{base+34}" text-anchor="middle" font-family="Archivo,Arial" font-size="8.5" fill="#6b5a48">{clk(hr_of(i))}</text>')
    o.append(f'<text x="{W-Rr}" y="{H-3}" text-anchor="end" font-family="Archivo,Arial" font-size="7.5" fill="#4d8aa6" letter-spacing=".8">BARS: CHANCE OF RAIN OR SNOW &middot; SHADED: AFTER DARK' + (' &middot; DOTTED: 32&deg;' if lo <= 32 <= hi else '') + '</text></svg>\n')
    return ''.join(o)
if __name__ == '__main__':
    f = json.load(open('/home/claude/site/data/forecast.json'))
    print(curve(f['towns']['North Tonawanda']['hourly'], 426, 1012))
