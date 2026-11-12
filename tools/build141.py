import json, re, glob
src = json.load(open('/home/claude/site/data/edition-2026-11-11.json'))['body_html']
def R(a, c, n=1):
    global src
    assert src.count(a) == n, ('R', a[:60], src.count(a)); src = src.replace(a, c)
def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50]); src = src[:i] + new + src[j:]
f = json.load(open('/home/claude/site/data/forecast.json'))
assert f['generated_utc'].startswith('2026-11-12')
assert [f['towns'][n]['observation']['temp_f'] for n in ['North Tonawanda', 'Dunkirk', 'Scottsville']] == [45, 45, 45]
hr = [h['temp'] for h in f['towns']['North Tonawanda']['hourly']][:24]
W, H, P = 320, 62, 12
lo, hi = min(hr), max(hr)
xs = [P + i * (W - 2 * P) / (len(hr) - 1) for i in range(len(hr))]
ys = [H - P - (t - lo) * (H - 2 * P - 10) / max(1, hi - lo) for t in hr]
pts = ' '.join(f'{x:.1f},{y:.1f}' for x, y in zip(xs, ys))
ih, il = hr.index(hi), len(hr) - 1 - hr[::-1].index(lo)
def lab(i, t, col):
    anc = 'start' if i < 3 else ('end' if i > len(hr) - 4 else 'middle')
    return (f'<circle cx="{xs[i]:.1f}" cy="{ys[i]:.1f}" r="3" fill="{col}"/><text x="{xs[i]:.1f}" y="{ys[i]-6:.1f}" text-anchor="{anc}" font-family="Archivo,Arial" font-size="10" fill="#24170c">{t}&deg;</text>')
spark = (f'<div class="line"><span class="lbl t">Next 24 hours</span></div>'
         f'<svg viewBox="0 0 {W} {H}" style="display:block;width:100%;max-width:420px;height:auto;margin:0 auto .4rem" role="img" aria-label="Hourly temperatures for North Tonawanda over the next 24 hours, from {hr[0]} now to a low of {lo}">'
         f'<polyline points="{pts}" fill="none" stroke="#9c3216" stroke-width="2" stroke-linejoin="round"/>'
         + lab(ih, hi, '#9c3216') + lab(il, lo, '#2f5e3e') +
         f'<text x="{P}" y="{H-1}" font-family="Archivo,Arial" font-size="9" fill="#6b5a48">now</text><text x="{W-P}" y="{H-1}" text-anchor="end" font-family="Archivo,Arial" font-size="9" fill="#6b5a48">this time tomorrow</text></svg>\n')

# cover: an umbrella in a cold November rain
import random
random.seed(141)
rain = ''.join(f'<line class="rn141 r{k%4}" x1="{random.randint(0,760)}" y1="{random.randint(-60,330)}" x2="0" y2="0" stroke="#dfe8ee" stroke-width="2" stroke-linecap="round" opacity=".75"/>' for k in range(70))
rain = re.sub(r'x1="(\d+)" y1="(-?\d+)" x2="0" y2="0"', lambda m: f'x1="{m.group(1)}" y1="{m.group(2)}" x2="{int(m.group(1))-9}" y2="{int(m.group(2))+26}"', rain)
svg = f'''<svg viewBox="0 0 750 375" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A red umbrella standing open in a gray, slanting November rain" style="display:block;width:100%;height:auto">
<defs><linearGradient id="sky141" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5d6b78"/><stop offset="1" stop-color="#a9b4ba"/></linearGradient></defs>
<style>.rn141{{animation:rn141 1.1s linear infinite}}.r1{{animation-delay:-.3s}}.r2{{animation-delay:-.6s}}.r3{{animation-delay:-.85s}}@keyframes rn141{{from{{transform:translate(14px,-40px)}}to{{transform:translate(-14px,40px)}}}}.um141{{animation:um141 4s ease-in-out infinite alternate;transform-origin:375px 330px}}@keyframes um141{{from{{transform:rotate(-2deg)}}to{{transform:rotate(3deg)}}}}</style>
<rect width="750" height="375" fill="url(#sky141)"/>
<path d="M0 318 Q190 300 380 314 T750 306 V375 H0z" fill="#6f7f76"/>
<ellipse cx="375" cy="345" rx="150" ry="10" fill="#8fa0a6" opacity=".7"/>
<g class="um141"><path d="M375 150 V318 q0 16 -16 16" stroke="#3b2a1c" stroke-width="6" fill="none" stroke-linecap="round"/>
<path d="M235 190 Q375 40 515 190 Q480 172 445 190 Q410 172 375 190 Q340 172 305 190 Q270 172 235 190Z" fill="#c8302f"/>
<path d="M305 190 Q330 100 375 82 Q420 100 445 190 Q410 172 375 190 Q340 172 305 190Z" fill="#b4261f"/><circle cx="375" cy="80" r="5" fill="#3b2a1c"/></g>
{rain}
</svg>'''
S('<svg viewBox="0 0 750 375"', '</div>\n<div class="plate-cap">', svg)
R('<div class="plate-sub">Veterans Day morning, 32 degrees at dawn</div>', '<div class="plate-sub">A raw, rainy Thursday</div>')
R('No. 140', 'No. 141'); R('Wednesday &middot; November 11 &middot; 2026', 'Thursday &middot; November 12 &middot; 2026')
S('<div class="tiles">', '<div class="plate-wrap">', '''<div class="tiles">
  <div class="tile"><div class="v">46&deg;</div><div class="k">Rain</div></div>
  <div class="tile"><div class="v">4:54</div><div class="k">Sunset</div></div>
  <div class="tile urg"><div class="v">14</div><div class="k">Days to Thanksgiving</div></div>
</div>
''')
S('<div class="wire lead">', '<div class="part"><span>The Almanac</span></div>', '''<div class="wire lead"><div><span class="kick">The Lead</span><h3>Brooklyn Building Collapses</h3>
<p>A three-story apartment building on Flatbush Avenue in Brooklyn collapsed just after 4 p.m. Wednesday, killing at least six people and injuring 19, CBS reports. The side of the building next door was torn off as it fell.</p>
<p>People were living in the building at the time, police said, and the lot beside the two buildings was a construction site; people from both were trapped. More than 250 firefighters and medics responded, and the first fire company, already in the neighborhood, arrived in less than a minute.</p>
<p>The cause is under investigation.</p>
</div></div>
<h2 class="sec">The National Wire</h2>
<div class="wire"><div class="num">1</div><div><h3>A Democrat Wins in Mississippi</h3><p>Democrat Scott Colom, a 43-year-old district attorney, defeated Republican Sen. Cindy Hyde-Smith in a race that took more than a week to settle, CBS projects. It is the eighth Senate seat Democrats have taken from Republicans this fall, and Colom will be Mississippi's first Black senator since Reconstruction, the years just after the Civil War.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>A Great Liner Goes Under on Purpose</h3><p>The SS <i>United States</i>, the 1,000-foot ocean liner that set a transatlantic speed record in 1952 that still stands, was deliberately sunk Wednesday about 20 nautical miles off Florida's Gulf Coast, CBS reports. She will become the world's largest artificial reef, a man-made home for fish and a draw for divers.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Found After Six Days in the Bush</h3><p>A 17-year-old with autism who vanished on a camping trip east of Melbourne, Australia, was found alive Thursday, asleep on a flat rock beside a creek, by a police helicopter crew, CBS reports. He was sunburned but mostly healthy; "I'm just over the moon that he's alive," his mother said.</p></div></div>
<h2 class="sec">The Home Wire</h2>
<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; High Falls Park Breaks Ground</h3><p>Work on the first phase of High Falls State Park begins with a groundbreaking Wednesday, Nov. 18, WXXI reports: High Falls Terrace, on the eastern edge of the gorge, with a Heritage Walk and Memorial Wall telling the stories of people who came to the Rochester area. The 85-acre park around the gorge would be the first state park in the city.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Hanover &middot; A Memorial and a Time Capsule</h3><p>The Chautauqua County town of Hanover dedicated its new Veterans Memorial on Wednesday and buried a time capsule to be opened July 4, 2076, the nation's 300th birthday, WKBW reports. "This memorial was built for you," Town Clerk Elizabeth VanCheri, who led the project, told the veterans there.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>North Tonawanda &middot; Lowry School Deal Falls Through</h3><p>The plan for the county land bank to take over the empty Lowry Middle School and pass it to developers has fallen through, WKBW reports; the owners, 621 Payne LLC, say they will develop it themselves. The land bank's plan called for several dozen apartments in the school and lots for new homes where Vetter Stadium stood.</p></div></div>
<h2 class="sec">The Marquee</h2>
<div class="wire"><div class="num">1</div><div><h3>Anthony Clark of <i>Yes, Dear</i> Dies at 62</h3><p>Anthony Clark, the comedian who starred in the CBS sitcom <i>Yes, Dear</i>, has died, his manager told Us Weekly; Deadline reports the cause was complications of pneumonia. Co-star Mike O'Malley, a longtime friend, announced the death.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Frankie Muniz Walks Away From a Crash</h3><p>The <i>Malcolm in the Middle</i> star, who took up racing in 2023, was taken to a hospital Wednesday after a practice crash at Daytona International Speedway and released the same day, E! News reports. "I am a little sore," he said, sorry to miss the Veterans Day race he was there to run.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>France Honors Nicole Kidman</h3><p>Nicole Kidman will receive an honorary C&eacute;sar, the highest award in French film, for her life's work at the ceremony in Paris in February, the Hollywood Reporter says. The French film academy called her "a Hollywood star and a major figure in auteur cinema," meaning films shaped by a director's personal vision.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>The Sabres Draft a Dog</h3><p>The Buffalo Sabres introduced this season's team dog: Ralph, an 8-month-old Samoyed named for Ralph Wilson, the Bills' original owner, WKBW reports. He will train to be a service dog for a local veteran through WNY Heroes' Pawsitive for Heroes program.</p></div></div>
<h2 class="sec">The Gridiron</h2>
<div class="wire"><div><h3>Bills Ease Into Jets Week</h3><p>Four starting offensive linemen were limited in Wednesday's practice, the first of the week, though every Bill took part, Buffalo Rumblings reports. New safety Amani Hooker, who came from a 1&ndash;7 Tennessee team, had one word for joining a 7&ndash;1 one: "amazing," ProFootballTalk reports.</p></div></div>
<div class="wire"><div><h3>Jets Add a Big Lineman</h3><p>The Jets signed defensive lineman Isaiahh Loudermilk, a 6-foot-7 former Steeler, to their practice squad, Gang Green Nation reports.</p></div></div>
<div class="wire"><div><h3>The Sunday Tax &middot; Week 10</h3><p>Last call: the first sheet locks tonight at 8:15, Commanders at Giants. Picks at <a href="https://tally.so/r/RGOakJ">tally.so/r/RGOakJ</a>, standings at <a href="https://benthambulletin.github.io/pool/">benthambulletin.github.io/pool</a>; $5 a week, straight-up winners, pot to the best record, and anyone with the link can play.</p></div></div>
''')
S('<p class="wlede">', '<div class="line"><span class="lbl t">Next 24 hours</span>', '''<p class="wlede">Rain through early afternoon on a raw northeast wind</p>
<div class="wxrow">
  <div class="wxc"><div class="k">Tonight</div><div class="v">32&deg;</div><div class="s">cloudy</div></div>
  <div class="wxc"><div class="k">Wind</div><div class="v">26 mph</div><div class="s">NE gusts</div></div>
  <div class="wxc"><div class="k">Rain</div><div class="v">9 to 2</div><div class="s">80% today</div></div>
  <div class="wxc"><div class="k">Normal</div><div class="v">49&deg;</div><div class="s">for the date</div></div>
</div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">45<sup>&deg;</sup></div><div class="d">Cloudy<br>high 46&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">45<sup>&deg;</sup></div><div class="d">Partly cloudy<br>high 47&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">45<sup>&deg;</sup></div><div class="d">Cloudy<br>high 46&deg;</div></div>
</div>
<div class="towns lakes">
  <div class="town"><div class="n">Lake Erie</div><div class="t">57<sup>&deg;</sup></div><div class="d">off Buffalo, Wednesday</div></div>
  <div class="town"><div class="n">Lake Ontario</div><div class="t">57<sup>&deg;</sup></div><div class="d">off Rochester, Wednesday</div></div>
</div>
<div class="strip5">
  <div><div class="d">Thu</div><div class="i">&#127783;</div><div class="h">46</div><div class="w">rain</div></div>
  <div><div class="d">Fri</div><div class="i">&#127784;</div><div class="h">41</div><div class="w">rain, snow showers</div></div>
  <div><div class="d">Sat</div><div class="i">&#127784;</div><div class="h">43</div><div class="w">snow, rain showers</div></div>
  <div><div class="d">Sun</div><div class="i">&#9729;</div><div class="h">46</div><div class="w">mostly cloudy</div></div>
  <div><div class="d">Mon</div><div class="i">&#9729;</div><div class="h">47</div><div class="w">mostly cloudy</div></div>
</div>
''')
S('<div class="line"><span class="lbl t">Next 24 hours</span>', '<h2 class="sec">The Almanac Sky</h2>', spark + '''<div class="line"><span class="lbl t">Outdoor window</span> Slim: steady rain from 9 to 2, and showers possible until 5.</div>
<div class="line"><span class="lbl t">Snow watch</span> A slight chance of snow showers Friday before 10 a.m., then rain and snow showers; lows of 32 tonight and 31 Friday night.</div>
''')
S('<h2 class="sec">The Almanac Sky</h2>', '<h2 class="sec">Coming Up</h2>', '''<h2 class="sec">The Almanac Sky</h2>
<div class="wxrow">
  <div class="wxc"><div class="k">Moon</div><svg class="moonmini" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#5a4d3b"/><path d="M50 4 A46 46 0 0 1 50 96 A36.1 46 0 0 0 50 4Z" fill="#f4e5b4"/></svg><div class="s">waxing crescent</div></div>
  <div class="wxc"><div class="k">Sunrise</div><div class="v">7:03</div><div class="s">a.m.</div></div>
  <div class="wxc"><div class="k">Daylight</div><div class="v">9h 51m</div><div class="s">2 min less</div></div>
</div>
<p class="skynote"><b>Tonight:</b> an 11 percent crescent in Sagittarius sets at 6:57, behind cloud for most of us. Saturn is the only planet up through the evening, highest in the south around 9; Mars and Jupiter rise just before midnight. Twelve days to the full Beaver Moon.</p>
<div class="touch-head">The Stars &middot; for fun</div>
<div class="stars slim">
<div class="star"><span class="sgn">Aries</span> <span class="who">Kaylani, Luka</span><br>Plenty of go, a little fog on the details. Read it twice before you agree to it.</div>
<div class="star"><span class="sgn">Cancer</span> <span class="who">Gregg</span><br>Still calm overhead for you. A good day to make soup.</div>
<div class="star"><span class="sgn">Leo</span> <span class="who">Leah, Tommy</span><br>The sky is in your corner. Ask for the thing you want.</div>
<div class="star"><span class="sgn">Virgo</span> <span class="who">Derek, Joanne</span><br>Crossed wires again. Fix one small thing and call it a win.</div>
<div class="star"><span class="sgn">Scorpio</span> <span class="who">Ariel, Claire, Garret</span><br>No push and no pull. Be kind to somebody for no reason.</div>
</div>
''')
S('<h2 class="sec">Coming Up</h2>', '<div class="dbl"><div class="a">', '''<h2 class="sec">Coming Up</h2>
<div class="calbox"><div class="calrow"><div class="cd">Sun</div><div>Bills at Jets, 1:00</div></div>
<div class="calrow"><div class="cd">Nov 22</div><div>Dolphins at Bills, 1:00; Jets at Chargers, 4:05</div></div>
<div class="calrow"><div class="cd">Nov 26</div><div>Thanksgiving; Chiefs at Bills, 8:20</div></div>
</div>
<h2 class="sec">The Ledger</h2>
<div class="ledger"><div class="num"><div class="cap">watched the Bills beat the Vikings on Monday night</div><div class="big">21.7 million</div></div>
<div class="txt">That is ESPN's count across ABC, ESPN and its other channels, ProFootballTalk reports.</div></div>
<h2 class="sec">On This Day</h2>
<div class="otd"><b>November 12, 1954</b> &mdash; Ellis Island closed. More than 12 million immigrants had passed through the station in New York Harbor since 1892.</div>
<h2 class="sec">Question of the Day</h2>
<div class="qotd">I fall without getting hurt, I'm measured in inches, and I can close a school without saying a word. What am I? <i>Answer below the fold.</i></div>
''')
R('<b>Question of the Day:</b> Daylight.', '<b>Question of the Day:</b> Snow.')
S('headlines via ', ' &middot; scores and stats via Sportradar', 'headlines via CBS, WXXI, WKBW, Us Weekly, Deadline, E! News, the Hollywood Reporter, Buffalo Rumblings, ProFootballTalk, Gang Green Nation')
allold = ''
for g in sorted(glob.glob('/home/claude/site/data/edition-2026-*.json')):
    if g.endswith('11-12.json'): continue
    o = json.load(open(g))['body_html']; allold += o
    if g[-10:-5] in ('11-09', '11-10', '11-11'):
        for w in ['Colom', 'United States</i>', 'Flatbush', 'Melbourne', 'High Falls', 'Hanover', 'Lowry', 'Anthony Clark', 'Muniz', 'Kidman', 'Samoyed', 'Loudermilk', '21.7', 'Ellis', 'Hooker']:
            if w in o: print('PRIOR', g[-10:-5], w)
print('snow riddle before:', 'Question of the Day:</b> Snow' in allold, '| Ellis before:', 'Ellis Island' in allold)
assert 'No. 140' not in src and 'November 11 &middot;' not in src and 'Wednesday &middot;' not in src
ed = {"date": "2026-11-12", "no": 141, "body_html": src, "plate_path": None, "plate_caption": "A raw, rainy Thursday",
      "headline": "Brooklyn building collapses · A Democrat wins in Mississippi · The Sabres draft a dog"}
for p in ['/home/claude/site/data/edition-2026-11-12.json', '/home/claude/edition-2026-11-12.json']:
    json.dump(ed, open(p, 'w'), indent=1)
print('built', len(src))
