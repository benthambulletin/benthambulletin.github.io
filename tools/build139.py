import json, re
src = json.load(open('/home/claude/site/data/edition-2026-11-09.json'))['body_html']
def R(a, c, n=1):
    global src
    assert src.count(a) == n, ('R', a[:60], src.count(a)); src = src.replace(a, c)
def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50]); src = src[:i] + new + src[j:]
f = json.load(open('/home/claude/site/data/forecast.json'))
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
         f'<circle cx="{xs[il]:.1f}" cy="{ys[il]:.1f}" r="3" fill="#2f5e3e"/><text x="{lx:.1f}" y="{ys[il]-6:.1f}" text-anchor="{lanc}" font-family="Archivo,Arial" font-size="10" fill="#24170c">{lo}&deg;</text>'
         f'<text x="{P}" y="{H-1}" font-family="Archivo,Arial" font-size="9" fill="#6b5a48">now</text><text x="{W-P}" y="{H-1}" text-anchor="end" font-family="Archivo,Arial" font-size="9" fill="#6b5a48">this time tomorrow</text></svg>\n')

import random
random.seed(139)
pop = ''
for k in range(26):
    x = 20 + k * 28 + random.randint(-8, 8); y = 250 + random.randint(-20, 70); h = 300 - y + random.randint(10, 40)
    sw = f'sw{k%3}'
    pop += (f'<g class="{sw}" style="transform-origin:{x}px 375px"><path d="M{x} 375 Q{x+4} {y+60} {x} {y}" stroke="#4f6b3a" stroke-width="2.4" fill="none"/>'
            f'<g transform="translate({x} {y})"><circle r="11" cx="-6" cy="0" fill="#c8302f"/><circle r="11" cx="6" cy="0" fill="#b4261f"/><circle r="10" cx="0" cy="-7" fill="#d23a2f"/><circle r="4" fill="#24170c"/></g></g>')
gust = ''.join(f'<path class="gu g{i}" d="M-80 {60+i*34} q60 -14 120 0 t120 0" stroke="#fbf5e4" stroke-width="2.2" fill="none" stroke-linecap="round" opacity=".7"/>' for i in range(4))
svg = f'''<svg viewBox="0 0 750 375" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Red poppies bending in a bright, breezy wind under a blue sky" style="display:block;width:100%;height:auto">
<style>.sw0{{animation:sway 2.6s ease-in-out infinite}}.sw1{{animation:sway 3.1s ease-in-out infinite -1s}}.sw2{{animation:sway 2.2s ease-in-out infinite -.5s}}
@keyframes sway{{0%,100%{{transform:rotate(2deg)}}50%{{transform:rotate(9deg)}}}}
.gu{{animation:gust 4s linear infinite}}.g1{{animation-delay:-1s}}.g2{{animation-delay:-2s}}.g3{{animation-delay:-3s}}@keyframes gust{{from{{transform:translateX(0)}}to{{transform:translateX(900px)}}}}
@media (prefers-reduced-motion:reduce){{.sw0,.sw1,.sw2,.gu{{animation:none}}}}</style>
<defs><linearGradient id="bs" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#7fb0d4"/><stop offset="1" stop-color="#d8e8ee"/></linearGradient></defs>
<rect width="750" height="375" fill="url(#bs)"/><circle cx="640" cy="70" r="34" fill="#f6d36b"/>
{gust}
<path d="M0 300 Q200 270 400 290 T750 280 L750 375 L0 375Z" fill="#7d9a55"/>
{pop}
</svg>'''

NEW = '''<div class="tiles">
  <div class="tile"><div class="v">60&deg;</div><div class="k">Sunny, Windy</div></div>
  <div class="tile"><div class="v">4:56</div><div class="k">Sunset</div></div>
  <div class="tile urg"><div class="v">5</div><div class="k">Days to Bills&ndash;Jets</div></div>
</div>
<div class="calbox"><div class="ch">Coming Up</div>
<div class="calrow"><div class="cd">Wed</div><div>Veterans Day</div></div>
<div class="calrow"><div class="cd">Thu</div><div>Sunday Tax sheets start locking, 8:15</div></div>
<div class="calrow"><div class="cd">Sun</div><div>Bills at Jets, 1:00</div></div>
</div>
<div class="plate-wrap"><div class="frame"><span class="tick tl"></span><span class="tick tr"></span><span class="tick bl"></span><span class="tick br"></span>
''' + svg + '''</div>
<div class="plate-cap">Plate I &middot; The Family Album</div>
<div class="plate-sub">Poppies in the wind, the day before Veterans Day</div></div>
<div class="dbl-tight"><div class="a"></div><div class="b"></div></div>
<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass<span class="o">&#9788;</span></h2>
<div class="wx slim"><div class="bigtemp">60<sup>&deg;</sup></div><div class="wxtext"><span class="lede">Mostly sunny and windy, ten degrees above normal</span></div></div>
<div class="wxrow">
  <div class="wxc"><div class="k">Tonight</div><div class="v">37&deg;</div><div class="s">partly cloudy</div></div>
  <div class="wxc"><div class="k">Wind</div><div class="v">35 mph</div><div class="s">W gusts</div></div>
  <div class="wxc"><div class="k">Rain</div><div class="v">2%</div><div class="s">dry today</div></div>
  <div class="wxc"><div class="k">Normal</div><div class="v">50&deg;</div><div class="s">for the date</div></div>
</div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">50<sup>&deg;</sup></div><div class="d">Mostly clear<br>high 60&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">46<sup>&deg;</sup></div><div class="d">Clear<br>high 57&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">45<sup>&deg;</sup></div><div class="d">Mostly cloudy<br>high 61&deg;</div></div>
</div>
<div class="towns lakes">
  <div class="town"><div class="n">Lake Erie</div><div class="t">57<sup>&deg;</sup></div><div class="d">off Buffalo, Monday</div></div>
  <div class="town"><div class="n">Lake Ontario</div><div class="t">57<sup>&deg;</sup></div><div class="d">off Rochester, Monday</div></div>
</div>
<div class="strip5">
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">60</div><div class="w">sunny, windy</div></div>
  <div><div class="d">Wed</div><div class="i">&#9925;</div><div class="h">55</div><div class="w">showers late</div></div>
  <div><div class="d">Thu</div><div class="i">&#127783;</div><div class="h">48</div><div class="w">rain</div></div>
  <div><div class="d">Fri</div><div class="i">&#127783;</div><div class="h">42</div><div class="w">chance of showers</div></div>
  <div><div class="d">Sat</div><div class="i">&#127784;</div><div class="h">44</div><div class="w">morning snow showers</div></div>
</div>
''' + spark + '''<div class="line"><span class="lbl t">Outdoor window</span> Today, the last dry 60 in the forecast.</div>
<div class="line"><span class="lbl t">Snow watch</span> Friday night rain turns to a chance of snow showers, low around 31, with snow showers possible Saturday morning.</div>
<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky<span class="o">&#9790;</span></h2>
<div class="wxrow">
  <div class="wxc"><div class="k">Moon</div><svg class="moonmini" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#5a4d3b"/><path d="M50 4 A46 46 0 0 1 50 96 A44.1 46 0 0 0 50 4Z" fill="#f4e5b4"/></svg><div class="s">thin crescent</div></div>
  <div class="wxc"><div class="k">Sunrise</div><div class="v">7:01</div><div class="s">a.m.</div></div>
  <div class="wxc"><div class="k">Sunset</div><div class="v">4:56</div><div class="s">p.m.</div></div>
  <div class="wxc"><div class="k">Daylight</div><div class="v">9h 56m</div><div class="s">2 min less</div></div>
</div>
<p class="skynote"><b>Tonight:</b> a 2 percent crescent, the first after Monday's new moon, follows the sun down at 5:21, too thin and low to catch for most. Saturn holds the southern sky around 10. The Beaver Moon is full Tuesday, Nov. 24.</p>
<div class="touch-head">The Stars &middot; for fun</div>
<div class="stars slim">
<div class="star"><span class="sgn">Aries</span> <span class="who">Kaylani, Luka</span><br>Easy, steady energy. The hard thing on the list gets done today.</div>
<div class="star"><span class="sgn">Cancer</span> <span class="who">Gregg</span><br>A quiet day in the sky for you. Quiet is underrated.</div>
<div class="star"><span class="sgn">Leo</span> <span class="who">Leah, Tommy</span><br>Good fun and good company line up. Say yes to the plan.</div>
<div class="star"><span class="sgn">Virgo</span> <span class="who">Derek, Joanne</span><br>Plans and moods bump into each other. Bend a little.</div>
<div class="star"><span class="sgn">Scorpio</span> <span class="who">Ariel, Claire, Garret</span><br>The moon has moved on from your sign, and so can you. Let yesterday's thing go.</div>
</div>
<h2 class="sec"><span class="o">&#10038;</span>The Ledger<span class="o">&#10038;</span></h2>
<div class="ledger"><div class="num"><div class="cap">Gordon Ramsay's new age, as of Sunday</div><div class="big">60</div></div>
<div class="txt">The chef marked it with a shirtless workout photo and "Day 2 of being 60," E! News reports. He shares the birthday with his daughter Tilly, who turned 25.</div></div>
<h2 class="sec"><span class="o">&#10038;</span>The National Wire<span class="o">&#10038;</span></h2>
<div class="wire lead"><div><span class="kick">The Lead</span><h3>Gas Drops Below $4</h3>
<p>The national average for a gallon of regular fell to about $3.98 on Tuesday, the first time it has been under $4 in nearly four months, AAA says, CBS reports. It peaked at $4.56 earlier this year.</p>
<p>The fall is mostly seasonal: from Sept. 15, stations may sell a cheaper "winter blend" of gasoline, and people drive less once vacation season ends. Patrick De Haan of GasBuddy, which tracks pump prices, expects prices to keep easing into Thanksgiving travel.</p>
<div class="pull">Fuel prices "will continue to ease into the Thanksgiving holidays," GasBuddy predicts.</div>
</div></div>
<div class="wire"><div class="num">2</div><div><h3>Update: Dana Says No</h3><p>UFC chief Dana White stepped up to the White House briefing-room podium Monday and turned down the press secretary job, Us Weekly reports. "I have zero political aspirations," he said.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Update: The FBI and Nvidia's Boss</h3><p>President Trump said the FBI is looking into Nvidia chief Jensen Huang's affair with a woman U.S. agencies suspect was a Chinese spy, the BBC reports. Trump said Huang told him, "I had no idea she was a spy," and that he believes him; China calls the allegations "entirely groundless."</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>Ukraine Talks Resume</h3><p>American, Ukrainian and Russian negotiators began two days of talks in Abu Dhabi on Tuesday aimed at ending the war Russia started in 2022, the first such meeting since February, CBS reports. They will focus on security guarantees, promises of protection Ukraine wants against a future attack.</p></div></div>
<h2 class="sec"><span class="o">&#9962;</span>The Home Wire<span class="o">&#9962;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>New York &middot; Regents Exams Stay Until 2030</h3><p>The Board of Regents pushed back the end of the state's Regents exams to 2030, WXXI reports. Students will still take one each in English, math, science and social studies, but the tests won't decide whether they graduate.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Dunkirk &middot; Pomfret Water Brings Money</h3><p>Homes and businesses in Pomfret east and south of the Routes 20 and 60 roundabout moved off Fredonia's troubled water system on Friday and now get Dunkirk's water through the North County Water District, the <i>Observer</i> reports. "That will be extra income for the city of Dunkirk," Public Works Director Randy Woodbury said.</p></div></div>
<h2 class="sec"><span class="o">&#9733;</span>The Marquee<span class="o">&#9733;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>Billy Joel Plans a Return</h3><p>Billy Joel will answer students' questions and play "a little music" at Florida Atlantic University on Dec. 14, his first official appearance since he was diagnosed with normal pressure hydrocephalus, a brain disorder, and left the stage last year, Rolling Stone reports. Tickets go only to enrolled students.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Johnny Depp's Scrooge</h3><p>Early reactions to <i>Ebenezer</i>, Johnny Depp's take on <i>A Christmas Carol</i>, are mostly warm, Variety reports, with critics calling it a "wickedly fun holiday treat" and a strong comeback for its star.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Fall Out Boy Hit the Road</h3><p>Fall Out Boy announced a 36-date 2027 stadium-and-arena tour of Europe and North America with The Offspring and Good Charlotte, and released "ACES," their first new song in more than three years, Billboard reports.</p></div></div>
<h2 class="sec"><span class="o">&#127944;</span>The Gridiron<span class="o">&#127944;</span></h2>
<div class="line"><b>Bills 23, Vikings 6</b> &middot; Buffalo held the ball for 42 minutes to Minnesota's 17 and wore the Vikings down. Josh Allen threw a 25-yard touchdown pass late in the first half, James Cook ran one in from 5 in the fourth, and Tyler Bass made all three field goals, the longest from 52. The defense intercepted two passes and held Minnesota to 178 yards. The Bills are 7&ndash;1.</div>
<div class="line"><b>Jets</b> &middot; Ahead of today's 4 p.m. trade deadline, the Jets sent backup safety Andre Cisco to Detroit for a 2028 sixth-round pick, Gang Green Nation reports. Pass rusher Will McDonald has asked for a trade, though coach Aaron Glenn suggested the team isn't looking to move him. Sunday they host the Bills at 1:00.</div>
<div class="pnote"><b>The Sunday Tax &middot; Week 10.</b> Picks at <a href="https://tally.so/r/RGOakJ">tally.so/r/RGOakJ</a>; standings at <a href="https://benthambulletin.github.io/pool/">benthambulletin.github.io/pool</a>. $5 a week, straight-up winners, the pot to the best record. Anyone with the link can play. Sheets lock at each kickoff; first game Thursday at 8:15. Week 9 went to Devin, a perfect 15&ndash;0, for the $95 pot.</div>
<h2 class="sec"><span class="o">&#9790;</span>On This Day<span class="o">&#9790;</span></h2>
<div class="otd"><b>November 10, 1975</b> &mdash; The ore freighter <i>Edmund Fitzgerald</i> went down in a November gale on Lake Superior with all 29 of her crew.</div>
<h2 class="sec"><span class="o">&#10023;</span>Question of the Day<span class="o">&#10023;</span></h2>
<div class="qotd">I fly without wings, I climb highest on a windy day, and if you let go of my string, I'm gone. What am I? <i>Answer below the fold.</i></div>
'''
R('No. 138', 'No. 139')
R('Monday &middot; November 9 &middot; 2026', 'Tuesday &middot; November 10 &middot; 2026')
S('<div class="tiles">', '<div class="dbl"><div class="a"></div><div class="b"></div></div>\n<div class="colo">', NEW)
R("<b>Question of the Day:</b> A snow shovel.", "<b>Question of the Day:</b> A kite.")
S('<div class="s">Forecast, lake temperatures', '<div class="ask">',
'''<div class="s">Forecast, lake temperatures and radar per NWS Buffalo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; normals from NOAA &middot; sky computed for 14120 &middot; headlines via CBS, the BBC, Us Weekly, WXXI, the Dunkirk <i>Observer</i>, E! News, Rolling Stone, Variety, Billboard, Gang Green Nation &middot; scores and stats via Sportradar &middot; pool from the Sunday Tax standings</div>
''')
ed = {"date": "2026-11-10", "no": 139, "body_html": src, "plate_path": None, "plate_caption": "Poppies in the wind, the day before Veterans Day",
      "headline": "Gas drops below $4 · Bills 23, Vikings 6 · Billy Joel plans a return"}
for p in ['/home/claude/edition-2026-11-10.json', '/home/claude/site/data/edition-2026-11-10.json']:
    json.dump(ed, open(p, 'w'), ensure_ascii=False, indent=1)
print('ok', lo, hi)
