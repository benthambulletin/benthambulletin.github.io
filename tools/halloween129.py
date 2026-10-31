import json, random
random.seed(1031)
W, H = 600, 320
p = []
p.append(f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="An illustrated Halloween night: glowing jack-o\'-lanterns on a porch step, bats flapping across a dusk sky, falling leaves, and the words Happy Halloween" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;height:auto">')
p.append('<defs><linearGradient id="hsky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1d1430"/><stop offset=".55" stop-color="#4a2a3e"/><stop offset="1" stop-color="#c8642a"/></linearGradient>'
         '<radialGradient id="hglow"><stop offset="0" stop-color="#ffd27a" stop-opacity=".9"/><stop offset="1" stop-color="#ffb347" stop-opacity="0"/></radialGradient></defs>')
p.append(f'<rect width="{W}" height="{H}" fill="url(#hsky)"/>')
# stars
for _ in range(40):
    x, y = random.uniform(0, W), random.uniform(0, 150)
    r = random.uniform(.6, 1.6); d = random.uniform(1.5, 4); b = random.uniform(0, 4)
    p.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.1f}" fill="#fbf5e4"><animate attributeName="opacity" values="1;.25;1" dur="{d:.1f}s" begin="-{b:.1f}s" repeatCount="indefinite"/></circle>')
# hills and bare tree
p.append(f'<path d="M0 250 Q120 215 240 240 T480 232 T600 238 V{H} H0Z" fill="#24170c"/>')
p.append('<path d="M520 245 L522 170 M521 200 L540 182 M521 188 L503 172 M540 182 L552 176 M503 172 L494 164 M521 214 L508 204" stroke="#24170c" stroke-width="5" stroke-linecap="round" fill="none"/>')
# fence
for i in range(9):
    x = 20 + i * 22
    p.append(f'<path d="M{x} 262 V232 l5 -7 l5 7 V262Z" fill="#2b1d10"/>')
p.append('<rect x="18" y="240" width="200" height="5" fill="#2b1d10"/><rect x="18" y="252" width="200" height="5" fill="#2b1d10"/>')
# bats
def bat(cx, cy, s, dur, begin, dx):
    wing = (f'<path fill="#140d1c" d="M0 0 C-6 -6 -14 -6 -20 -2 C-16 0 -14 3 -12 6 C-9 3 -5 3 0 6 C5 3 9 3 12 6 C14 3 16 0 20 -2 C14 -6 6 -6 0 0Z">'
            f'<animateTransform attributeName="transform" type="scale" values="1 1;1 -0.35;1 1" dur=".45s" repeatCount="indefinite"/></path>')
    return (f'<g><animateTransform attributeName="transform" type="translate" values="{cx},{cy}; {cx+dx},{cy-18}; {cx+2*dx},{cy}" dur="{dur}s" begin="-{begin}s" repeatCount="indefinite"/>'
            f'<g transform="scale({s})">{wing}<circle r="3.2" fill="#140d1c"/></g></g>')
p.append(bat(60, 80, 1.1, 9, 2, 260))
p.append(bat(300, 55, .8, 11, 6, -200))
p.append(bat(420, 110, .65, 8, 4, 140))
p.append(bat(150, 130, .55, 10, 1, -120))
# falling leaves
cols = ['#cf6f1a', '#9c3216', '#e8b100', '#c8302f']
for i in range(14):
    x = random.uniform(10, 590); d = random.uniform(7, 13); b = random.uniform(0, 13); c = random.choice(cols)
    sway = random.uniform(15, 40) * random.choice([-1, 1])
    p.append(f'<g><animateTransform attributeName="transform" type="translate" values="{x:.0f},-10; {x+sway:.0f},150; {x:.0f},330" dur="{d:.1f}s" begin="-{b:.1f}s" repeatCount="indefinite"/>'
             f'<g><path d="M0 -6 C5 -3 5 3 0 6 C-5 3 -5 -3 0 -6Z" fill="{c}"/><animateTransform attributeName="transform" type="rotate" from="0" to="{random.choice([360,-360])}" dur="{d/2:.1f}s" repeatCount="indefinite"/></g></g>')
# jack-o-lanterns
def jack(cx, cy, r, face, flick):
    s = [f'<circle cx="{cx}" cy="{cy}" r="{r*1.9:.0f}" fill="url(#hglow)"><animate attributeName="opacity" values=".85;.55;.95;.7;.85" dur="{flick}s" repeatCount="indefinite"/></circle>']
    s.append(f'<rect x="{cx-3}" y="{cy-r-9}" width="6" height="11" rx="2" fill="#2f5e3e"/>')
    for k, w in ((-0.55, .62), (0.55, .62), (0, .7)):
        s.append(f'<ellipse cx="{cx + k*r:.1f}" cy="{cy}" rx="{r*w:.1f}" ry="{r*.92:.1f}" fill="#cf6f1a" stroke="#9c3216" stroke-width="1.5"/>')
    lit = f'<animate attributeName="fill" values="#ffd27a;#ffb347;#ffe39a;#ffd27a" dur="{flick}s" repeatCount="indefinite"/>'
    e = r * .28
    if face == 0:
        s.append(f'<path d="M{cx-r*.45:.1f} {cy-r*.15:.1f} l{e:.1f} {-e:.1f} l{e:.1f} {e:.1f}Z M{cx+r*.45:.1f} {cy-r*.15:.1f} l{-e:.1f} {-e:.1f} l{-e:.1f} {e:.1f}Z" fill="#ffd27a">{lit}</path>')
        s.append(f'<path d="M{cx-r*.55:.1f} {cy+r*.2:.1f} Q{cx} {cy+r*.75:.1f} {cx+r*.55:.1f} {cy+r*.2:.1f} l-{r*.18:.1f} {r*.12:.1f} l-{r*.14:.1f} -{r*.1:.1f} l-{r*.14:.1f} {r*.12:.1f} l-{r*.14:.1f} -{r*.1:.1f} l-{r*.14:.1f} {r*.12:.1f}Z" fill="#ffd27a">{lit}</path>')
    else:
        s.append(f'<circle cx="{cx-r*.33:.1f}" cy="{cy-r*.2:.1f}" r="{e*.7:.1f}" fill="#ffd27a">{lit}</circle><circle cx="{cx+r*.33:.1f}" cy="{cy-r*.2:.1f}" r="{e*.7:.1f}" fill="#ffd27a">{lit}</circle>')
        s.append(f'<ellipse cx="{cx}" cy="{cy+r*.35:.1f}" rx="{r*.22:.1f}" ry="{r*.26:.1f}" fill="#ffd27a">{lit}</ellipse>')
    return ''.join(s)
p.append('<rect x="300" y="268" width="300" height="52" fill="#3a2716"/><rect x="300" y="268" width="300" height="4" fill="#5a3d22"/>')
p.append(jack(370, 250, 26, 0, 1.3))
p.append(jack(450, 256, 19, 1, 1.7))
p.append(jack(515, 249, 27, 0, 1.1))
p.append('<text x="300" y="70" text-anchor="middle" font-family="PF, Georgia, serif" font-style="italic" font-size="22" fill="#e8b100">Happy</text>')
p.append('<text x="300" y="120" text-anchor="middle" font-family="PF, Georgia, serif" font-weight="800" font-size="52" fill="#fbf5e4" letter-spacing="1">Halloween</text>')
p.append('</svg>')
svg = ''.join(p)

block = ('<div class="plate-wrap"><div class="frame"><span class="tick tl"></span><span class="tick tr"></span><span class="tick bl"></span><span class="tick br"></span>\n'
         + svg + '</div>\n<div class="plate-cap">Plate I &middot; The Family Album</div>\n<div class="plate-sub">Happy Halloween</div></div>\n')
P = ['/home/claude/edition-2026-10-31.json', '/home/claude/site/data/edition-2026-10-31.json']
e = json.load(open(P[1])); b = e['body_html']
assert 'plate-wrap' not in b
i = b.find('</div>\n<div class="dbl-tight">', b.find('<div class="tiles">'))
assert i > 0
i += len('</div>\n')
b = b[:i] + block + b[i:]
e['body_html'] = b; e['plate_caption'] = 'Happy Halloween'; e['plate_path'] = None
for x in P: json.dump(e, open(x, 'w'), ensure_ascii=False, indent=1)
print('ok', len(svg))
