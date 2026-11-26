"""Thursday No. 155 Turkey Trot box. Run at build: python3 spool/thursday/make_box.py > /home/claude/box155.html
Reads data/forecast.json (North Tonawanda point; downtown point isn't in the feed, so the label says so).
Prints the box HTML to stdout and the facts used to stderr. The 'Since yesterday' line compares with No. 154:
rain after 1 p.m., 90%, gusts 37, quarter to half inch by dark."""
import json, re, sys, os
here = os.path.dirname(os.path.abspath(__file__))
f = json.load(open(os.path.join(here, '..', '..', 'data', 'forecast.json')))
nt = f['towns']['North Tonawanda']
P = {p['name']: p for p in nt['periods']}
day = next(p for p in nt['periods'] if 'Thanksgiving' in p['name'] or p['name'] in ('Today', 'This Afternoon'))
night = nt['periods'][nt['periods'].index(day) + 1]
d, n = day['detail'], night['detail']
def grab(rx, s, default='?'):
    m = re.search(rx, s); return m.group(1) if m else default
wind = grab(r'(\w+ wind [\d to]+ mph)', d)
gust = grab(r'gusts as high as (\d+)', d)
pop = grab(r'precipitation is (\d+)%', d)
amt = grab(r'amounts between (.*?) possible', d)
when = grab(r'^(Rain[^.]*?)\.', d, 'Rain later')
ngust = grab(r'gusts as high as (\d+)', n); nlow = grab(r'low around (\d+)', n); namt = grab(r'amounts between (.*?) possible', n)
hrs = [h for h in nt['hourly'] if '2026-11-26T06' <= h['start'][:13] <= '2026-11-26T12']
print('FACTS', when, wind, gust, pop, amt, '| night', ngust, nlow, namt, '| hours', [(h['start'][11:13], h['temp'], h['pop']) for h in hrs], file=sys.stderr)
def lbl(hh):
    hh = int(hh); return f"{hh if hh <= 12 else hh-12}{'a' if hh < 12 else 'p'}"
cells = ''
for h in hrs:
    hh = h['start'][11:13]; start = hh == '09'
    sky = h['short'].replace('Slight Chance ', '').replace('Chance ', '').replace('Mostly ', '').replace('Partly ', 'part ').lower()
    bg = 'background:rgba(156,50,22,.14);border-radius:4px;' if start else ''
    cells += (f'<div style="flex:1;text-align:center;padding:.25rem 0;{bg}"><div style="font-family:Archivo,Arial,sans-serif;font-size:.58rem;font-weight:800;letter-spacing:.08em">{"START" if start else lbl(hh)}</div>'
              f'<div style="font-family:\'Playfair Display\',Georgia,serif;font-weight:700;font-size:1.05rem">{h["temp"]}&deg;</div>'
              f'<div style="font-size:.62rem;line-height:1.1">{sky}</div><div style="font-size:.62rem;color:var(--soft,#664a2c)">{h["pop"]}%</div></div>')
start_t = next((h['temp'] for h in hrs if h['start'][11:13] == '09'), None)
amt_s = amt.replace(' and ', ' to ').replace('three quarters of an inch', 'three-quarters of an inch')
rain_hr = 'after noon' if 'noon' in when else ('after 1 p.m.' if '1pm' in when else when.lower())
box = f'''<div class="trotbox" style="border:2px solid var(--rust,#9c3216);border-radius:6px;padding:.8rem .95rem .7rem;margin:1rem 0 1.2rem;background:rgba(156,50,22,.05)">
<div style="font-family:Archivo,Arial,sans-serif;font-size:.68rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--rust,#9c3216)">Turkey Trot &middot; Today, 9 a.m., Franklin St. &middot; North Tonawanda forecast</div>
<div style="font-family:'Playfair Display',Georgia,serif;font-weight:700;font-size:1.35rem;line-height:1.15;margin:.25rem 0 .5rem">{start_t} at the gun. Dry, gray, windy. Rain {rain_hr}.</div>
<div style="display:flex;gap:2px;margin:.2rem 0 .55rem;border-top:1px solid var(--rule,#d3b88f);border-bottom:1px solid var(--rule,#d3b88f)">{cells}</div>
<ul style="margin:0 0 .5rem 1.1rem;padding:0;line-height:1.45">
<li><b>Wind:</b> {wind.lower()}, gusts as high as {gust}. Feels colder than it reads.</li>
<li><b>Rain:</b> {rain_hr}, {pop}% chance, {amt_s} by dark.</li>
<li><b>Tonight:</b> rain, {namt.replace(' and ', ' to ')}, gusts to {ngust}, low {nlow}. Easy on the drive home from Derek&rsquo;s.</li>
<li><b>Wear:</b> layers, gloves, hats; the wind guard on Luka&rsquo;s stroller; dry clothes in the car.</li>
</ul>
<div style="font-style:italic;font-size:.92rem">SINCE_YESTERDAY &mdash; Margo</div>
<div style="font-weight:700;margin-top:.45rem">Good luck, Ariel, Tommy, Claire, Garret, Kaylani and Luka.</div>
</div>'''
print(box)
