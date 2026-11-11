import json, re, glob
src = json.load(open('/home/claude/site/data/edition-2026-11-10.json'))['body_html']
def R(a, c, n=1):
    global src
    assert src.count(a) == n, ('R', a[:60], src.count(a)); src = src.replace(a, c)
def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50]); src = src[:i] + new + src[j:]
f = json.load(open('/home/claude/site/data/forecast.json'))
assert f['generated_utc'].startswith('2026-11-11')
ob = {n: f['towns'][n]['observation'] for n in f['towns']}
assert ob['North Tonawanda']['temp_f'] == 32 and ob['Dunkirk']['temp_f'] == 36 and ob['Scottsville']['temp_f'] == 36
# frost claim: coldest North Tonawanda dawn reading in every earlier edition this fall
mins = {}
for g in sorted(glob.glob('/home/claude/site/data/edition-2026-*.json')):
    b = json.load(open(g))['body_html']
    for n, t in re.findall(r'<div class="n">(North Tonawanda|Dunkirk|Scottsville)</div><div class="t">(\d+)<sup>', b):
        mins.setdefault(n, []).append((int(t), g[-15:-5]))
print({n: sorted(v)[:3] for n, v in mins.items()})
assert min(mins['North Tonawanda'])[0] == 34
hr = [h['temp'] for h in f['towns']['North Tonawanda']['hourly']][:24]
W, H, P = 320, 62, 12
lo, hi = min(hr), max(hr)
xs = [P + i * (W - 2 * P) / (len(hr) - 1) for i in range(len(hr))]
ys = [H - P - (t - lo) * (H - 2 * P - 10) / max(1, hi - lo) for t in hr]
pts = ' '.join(f'{x:.1f},{y:.1f}' for x, y in zip(xs, ys))
ih, il = hr.index(hi), hr.index(lo)
lanc = 'start' if il < len(hr) / 2 else 'end'; lx = xs[il] + (5 if lanc == 'start' else -5)
spark = (f'<div class="line"><span class="lbl t">Next 24 hours</span></div>'
         f'<svg viewBox="0 0 {W} {H}" style="display:block;width:100%;max-width:420px;height:auto;margin:0 auto .4rem" role="img" aria-label="Hourly temperatures for North Tonawanda over the next 24 hours, from {hr[0]} now to a high of {hi} and a low of {lo}">'
         f'<polyline points="{pts}" fill="none" stroke="#9c3216" stroke-width="2" stroke-linejoin="round"/>'
         f'<circle cx="{xs[ih]:.1f}" cy="{ys[ih]:.1f}" r="3" fill="#9c3216"/><text x="{xs[ih]:.1f}" y="{ys[ih]-6:.1f}" text-anchor="middle" font-family="Archivo,Arial" font-size="10" fill="#24170c">{hi}&deg;</text>'
         f'<circle cx="{xs[il]:.1f}" cy="{ys[il]:.1f}" r="3" fill="#2f5e3e"/><text x="{lx+4:.1f}" y="{ys[il]+3:.1f}" text-anchor="{lanc}" font-family="Archivo,Arial" font-size="10" fill="#24170c">{lo}&deg;</text>'
         f'<text x="{P}" y="{H-1}" font-family="Archivo,Arial" font-size="9" fill="#6b5a48">now</text><text x="{W-P}" y="{H-1}" text-anchor="end" font-family="Archivo,Arial" font-size="9" fill="#6b5a48">this time tomorrow</text></svg>\n')

# cover: a flag at a cold, clear dawn
stripes = ''.join(f'<path d="M0 {i*10} q45 -7 90 0 t90 0 v10 q-45 7 -90 0 t-90 0z" fill="{"#c8302f" if i%2==0 else "#fbf5e4"}"/>' for i in range(13))
stars = ''.join(f'<circle cx="{8+c*13}" cy="{9+r*13}" r="2.2" fill="#fbf5e4"/>' for r in range(5) for c in range(6))
grass = ''.join(f'<path d="M{x} 375 l3 -{14+(x*7)%13} l3 {14+(x*7)%13}z" fill="#dfe8e2"/>' for x in range(0, 750, 9))
svg = f'''<svg viewBox="0 0 750 375" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="An American flag on a pole at a cold, clear dawn, with pale frosted grass below" style="display:block;width:100%;height:auto">
<defs><linearGradient id="dawn140" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#31506f"/><stop offset=".55" stop-color="#e9b58a"/><stop offset="1" stop-color="#f6dfb4"/></linearGradient></defs>
<style>.fl140{{animation:fl140 5s ease-in-out infinite alternate;transform-origin:372px 70px}}@keyframes fl140{{from{{transform:skewY(-2deg) scaleX(1)}}to{{transform:skewY(3deg) scaleX(.96)}}}}.sun140{{animation:sun140 9s ease-in-out infinite alternate}}@keyframes sun140{{from{{opacity:.75}}to{{opacity:1}}}}</style>
<rect width="750" height="375" fill="url(#dawn140)"/>
<circle class="sun140" cx="150" cy="330" r="46" fill="#f4c56a"/>
<path d="M0 330 Q180 300 380 322 T750 312 V375 H0z" fill="#b9c9bd"/>
<path d="M0 350 Q200 330 420 346 T750 338 V375 H0z" fill="#cfdcd3"/>
{grass}
<rect x="366" y="48" width="6" height="290" fill="#6b5a48"/><circle cx="369" cy="46" r="7" fill="#e8b100"/>
<g class="fl140"><g transform="translate(372 60)">{stripes}<rect width="84" height="70" fill="#1f3a5f"/>{stars}</g></g>
</svg>'''
S('<svg viewBox="0 0 750 375"', '</div>\n<div class="plate-cap">', svg)
R('<div class="plate-sub">Poppies in the wind, the day before Veterans Day</div>', '<div class="plate-sub">Veterans Day morning, 32 degrees at dawn</div>')

R('No. 139', 'No. 140'); R('Tuesday &middot; November 10 &middot; 2026', 'Wednesday &middot; November 11 &middot; 2026')
S('<div class="tiles">', '<div class="plate-wrap">', '''<div class="tiles">
  <div class="tile"><div class="v">55&deg;</div><div class="k">Mostly Cloudy</div></div>
  <div class="tile"><div class="v">4:55</div><div class="k">Sunset</div></div>
  <div class="tile urg"><div class="v">15</div><div class="k">Days to Thanksgiving</div></div>
</div>
''')

S('<h2 class="sec">The National Wire</h2>', '<div class="part"><span>The Almanac</span></div>', '''<div class="wire lead"><div><span class="kick">The Lead</span><h3>The First Freeze, at Last</h3>
<p>The thermometer at Niagara Falls airport, the reading this paper uses for North Tonawanda, stood at 32 under a clear sky at 6:35 this morning. It is the first dawn reading at freezing there this fall; until today the coldest had been 34, on Oct. 21 and 22.</p>
<p>Dunkirk and Scottsville got there three weeks ago, with 28 at Dunkirk and 32 at the Rochester airport on Oct. 21. Both stood at 36 this morning, which is the normal low for Nov. 11.</p>
<p>Late, but not the latest. In 2017 Buffalo and Rochester both waited until Nov. 8 for a first freeze, the Northeast Regional Climate Center at Cornell says, giving Rochester its second-longest frost-free season in records back to 1872 and Buffalo its fifth-longest since 1874.</p>
<p>More cold is lined up behind it: rain tonight, rain mixing with snow late Thursday, and a low of 31 on Friday night.</p>
</div></div>
<h2 class="sec">The National Wire</h2>
<div class="wire"><div class="num">1</div><div><h3>Hegseth Impeachment Blocked</h3><p>The House voted 211&ndash;204 on Tuesday to send articles of impeachment, the formal charges that begin the process of removing an official, against Defense Secretary Pete Hegseth to a committee, which kills the effort for now, CBS and the BBC report. Republican Thomas Massie of Kentucky brought them, accusing Hegseth of waging war on Iran without Congress's approval; Hegseth called it a "farce."</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Kennedys Sue Over the Arch</h3><p>Nine members of the Kennedy family sued to stop the 250-foot triumphal arch President Trump plans for Washington, arguing it would block the view of John F. Kennedy's grave and the graves of thousands of veterans at Arlington National Cemetery, the BBC reports. A judge temporarily halted the project last week, and the White House called the family's move "unfortunate."</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Ebola Passes 11,000 Cases</h3><p>Congo's Ebola outbreak has reached 11,042 cases and 5,387 deaths, the country's health ministry said Wednesday, NPR reports. It is the deadliest outbreak of the virus Congo has had.</p></div></div>
<h2 class="sec">The Home Wire</h2>
<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; County Tax Rate Cut Again</h3><p>Monroe County Executive Adam Bello proposed a $1.6 billion budget for 2027 that lowers the property tax rate by 25 cents, to an average of $5.42 per $1,000 of assessed value, his seventh cut in a row, WXXI reports. The plan draws $33 million from reserves, and Bello warned that the rising costs of pensions, health care and state and federal mandates "are simply not sustainable over the long term."</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Dunkirk &middot; Breakwater Finished</h3><p>The Army Corps of Engineers' Buffalo District finished rebuilding the outer breakwater at Dunkirk Harbor on Oct. 19, the <i>Observer</i> reports. The breakwater is the barrier that protects the harbor and the community around it from Lake Erie.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Niagara Falls &middot; A National Hero of the Classroom</h3><p>Britini D'Angelo, a special education teacher at Henry J. Kalfas Elementary in Niagara Falls, was named Kleenex's National Hero of the Classroom, an award with cash prizes for her and the school, WKBW reports. Diagnosed with autism at 22 months and nonverbal as a small child, she has taught there three years: "This is what I am meant to do for the rest of my life."</p></div></div>
<h2 class="sec">The Marquee</h2>
<div class="wire"><div class="num">1</div><div><h3>Stacy Keach Dies at 85</h3><p>Stacy Keach, the stage actor best known as television's scruffy private eye Mike Hammer, died Tuesday at his home in Poland, CBS reports. His wife said he died "after a long and difficult battle with a serious heart condition and heart failure."</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Coachella Names Its Headliners</h3><p>Dua Lipa, Tame Impala and SZA will top the bill at the Coachella festival in Indio, California, on the weekends of April 9&ndash;11 and 16&ndash;18, 2027, Rolling Stone reports. Madonna plays the Friday under Dua Lipa, and Phoebe Bridgers and Weezer join Tame Impala's Saturday.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>A Shock on <i>Dancing With the Stars</i></h3><p>Jenna Dewan and partner Val Chmerkovskiy were voted off at the end of Tuesday's "Grammy Night," finishing seventh, one round short of the semifinals, Page Six reports. Dewan, a former professional dancer, had been expected to reach the finale; "Honestly, all love," she said.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3><i>You've Got Mail</i>, Again</h3><p>Warner Bros. is developing a new <i>You've Got Mail</i>, the Hollywood Reporter says. It will tell a new story rather than remake the 1998 Tom Hanks and Meg Ryan romance, with Jason Orley directing.</p></div></div>
<h2 class="sec">The Gridiron</h2>
<div class="wire"><div><h3>Bills Trade for a Safety</h3><p>About two hours before Tuesday's deadline the Bills got safety Amani Hooker from Tennessee, sending the Titans a second-round pick in next year's draft and getting a fifth-round pick back, the Associated Press reports. Hooker, 28 and in his eighth season, has started since 2021 and already has a career-high five interceptions this year.</p></div></div>
<div class="wire"><div><h3>Jets Stand Pat</h3><p>The deadline passed with pass rusher Will McDonald still a Jet, despite his trade request and reported interest from other teams, Gang Green Nation reports. The Cisco deal was the team's only move.</p></div></div>
<div class="wire"><div><h3>The Sunday Tax &middot; Week 10</h3><p>Week 10 sheets are open at <a href="https://tally.so/r/RGOakJ">tally.so/r/RGOakJ</a>, with the standings at <a href="https://benthambulletin.github.io/pool/">benthambulletin.github.io/pool</a>. It costs $5, you pick the winners straight up, the best record takes the pot, and each game locks at its kickoff.</p></div></div>
''')
i = src.index('<div class="part"><span>The News</span></div>\n') + len('<div class="part"><span>The News</span></div>\n')
assert src[i:].startswith('<div class="wire lead">')

S('<p class="wlede">', '<div class="towns">', '''<p class="wlede">A freezing, clear dawn, then clouds; rain by late evening</p>
<div class="wxrow">
  <div class="wxc"><div class="k">Tonight</div><div class="v">40&deg;</div><div class="s">rain</div></div>
  <div class="wxc"><div class="k">Wind</div><div class="v">5 mph</div><div class="s">southeast</div></div>
  <div class="wxc"><div class="k">Rain</div><div class="v">After 7</div><div class="s">p.m., 90%</div></div>
  <div class="wxc"><div class="k">Normal</div><div class="v">50&deg;</div><div class="s">for the date</div></div>
</div>
''')
S('<div class="towns">', '<div class="line"><span class="lbl t">Next 24 hours</span>', '''<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">32<sup>&deg;</sup></div><div class="d">Clear<br>high 55&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">36<sup>&deg;</sup></div><div class="d">Fog<br>high 55&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">36<sup>&deg;</sup></div><div class="d">Clear<br>high 55&deg;</div></div>
</div>
<div class="towns lakes">
  <div class="town"><div class="n">Lake Erie</div><div class="t">57<sup>&deg;</sup></div><div class="d">off Buffalo, Wednesday</div></div>
  <div class="town"><div class="n">Lake Ontario</div><div class="t">57<sup>&deg;</sup></div><div class="d">off Rochester, Wednesday</div></div>
</div>
<div class="strip5">
  <div><div class="d">Wed</div><div class="i">&#9729;</div><div class="h">55</div><div class="w">mostly cloudy</div></div>
  <div><div class="d">Thu</div><div class="i">&#127783;</div><div class="h">45</div><div class="w">rain</div></div>
  <div><div class="d">Fri</div><div class="i">&#127784;</div><div class="h">42</div><div class="w">snow, rain showers</div></div>
  <div><div class="d">Sat</div><div class="i">&#127784;</div><div class="h">44</div><div class="w">rain, snow showers</div></div>
  <div><div class="d">Sun</div><div class="i">&#9729;</div><div class="h">46</div><div class="w">mostly cloudy</div></div>
</div>
''')
S('<div class="line"><span class="lbl t">Next 24 hours</span>', '<h2 class="sec">The Almanac Sky</h2>', spark + '''<div class="line"><span class="lbl t">Outdoor window</span> Daylight today; the showers hold off until after 7.</div>
<div class="line"><span class="lbl t">Snow watch</span> Thursday night's rain may mix with snow between 10 and 1, low around 34, with a chance of snow showers Friday before 10 a.m.</div>
''')
S('<h2 class="sec">The Almanac Sky</h2>', '<h2 class="sec">Coming Up</h2>', '''<h2 class="sec">The Almanac Sky</h2>
<div class="wxrow">
  <div class="wxc"><div class="k">Moon</div><svg class="moonmini" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#5a4d3b"/><path d="M50 4 A46 46 0 0 1 50 96 A40.8 46 0 0 0 50 4Z" fill="#f4e5b4"/></svg><div class="s">waxing crescent</div></div>
  <div class="wxc"><div class="k">Sunrise</div><div class="v">7:02</div><div class="s">a.m.</div></div>
  <div class="wxc"><div class="k">Daylight</div><div class="v">9h 53m</div><div class="s">2 min less</div></div>
</div>
<p class="skynote"><b>Tonight:</b> a 6 percent crescent sits low in the southwest after sunset and is gone by 6:05, if the clouds leave a gap. Saturn is highest in the south around 9. Full Beaver Moon: Nov. 24.</p>
<div class="touch-head">The Stars &middot; for fun</div>
<div class="stars slim">
<div class="star"><span class="sgn">Aries</span> <span class="who">Kaylani, Luka</span><br>The moon is on your side. Start the thing you keep circling.</div>
<div class="star"><span class="sgn">Cancer</span> <span class="who">Gregg</span><br>Nothing is pulling at you today. Take the long way home.</div>
<div class="star"><span class="sgn">Leo</span> <span class="who">Leah, Tommy</span><br>A friendly sky. Someone laughs before you finish the joke.</div>
<div class="star"><span class="sgn">Virgo</span> <span class="who">Derek, Joanne</span><br>The day argues with your list. Let the list lose one.</div>
<div class="star"><span class="sgn">Scorpio</span> <span class="who">Ariel, Claire, Garret</span><br>A plain, level day. Better for finishing than for starting.</div>
</div>
''')
S('<h2 class="sec">Coming Up</h2>', '<div class="dbl"><div class="a">', '''<h2 class="sec">Coming Up</h2>
<div class="calbox"><div class="calrow"><div class="cd">Today</div><div>Veterans Day</div></div>
<div class="calrow"><div class="cd">Thu</div><div>Commanders at Giants, 8:15; Sunday Tax sheets start locking</div></div>
<div class="calrow"><div class="cd">Sun</div><div>Bills at Jets, 1:00</div></div>
</div>
<h2 class="sec">The Ledger</h2>
<div class="ledger"><div class="num"><div class="cap">since Lightship 82 sank in Lake Erie</div><div class="big">113 years</div></div>
<div class="txt">The Coast Guard honored the lightship's crew in Buffalo on Tuesday, WIVB and WGRZ report. She was one of a dozen ships that went down in the Great Lakes storm of November 1913, remembered as the White Hurricane.</div></div>
<h2 class="sec">On This Day</h2>
<div class="otd"><b>November 11, 1918</b> &mdash; The guns of the First World War fell silent at 11 a.m., the eleventh hour of the eleventh day of the eleventh month. Armistice Day became Veterans Day in 1954.</div>
<h2 class="sec">Question of the Day</h2>
<div class="qotd">I get a little shorter every day this month, though nobody ever catches me shrinking, and I start growing again four days before Christmas. What am I? <i>Answer below the fold.</i></div>
''')
R('<b>Question of the Day:</b> A kite.', '<b>Question of the Day:</b> Daylight.')
S('headlines via ', ' &middot; scores and stats via Sportradar', 'headlines via CBS, the BBC, NPR, WXXI, WKBW, WIVB, WGRZ, the Dunkirk <i>Observer</i>, Rolling Stone, Page Six, the Hollywood Reporter, Gang Green Nation, Buffalo Rumblings, AP &middot; frost history from the Northeast Regional Climate Center')
# repeats check against the last three editions
for d in ['2026-11-08', '2026-11-09', '2026-11-10']:
    old = json.load(open(f'/home/claude/site/data/edition-{d}.json'))['body_html']
    for w in ['Hegseth', 'Ebola', 'Kennedy', 'Keach', 'Coachella', 'Hooker', 'Dewan', 'Got Mail', 'Bello', 'Angelo', 'breakwater', 'Lightship', 'Armistice', 'Daylight.</div>', 'McDonald', 'White']:
        if w in old: print('PRIOR', d, w)
assert '139' not in src and 'November 10' not in src and 'Tuesday &middot;' not in src
ed = {"date": "2026-11-11", "no": 140, "body_html": src, "plate_path": None, "plate_caption": "Veterans Day morning, 32 degrees at dawn",
      "headline": "The first freeze, at last · Bills trade for a safety · Stacy Keach dies at 85"}
for p in ['/home/claude/site/data/edition-2026-11-11.json', '/home/claude/edition-2026-11-11.json']:
    json.dump(ed, open(p, 'w'), indent=1)
print('built', len(src))
