import json, shutil
src = json.load(open('/home/claude/site/data/edition-2026-11-06.json'))['body_html']

def R(a, c, n=1):
    global src
    assert src.count(a) == n, ('R', a[:60], src.count(a))
    src = src.replace(a, c)

def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50])
    src = src[:i] + new + src[j:]

shutil.copy('/home/claude/site/spool/next/plate.jpg', '/home/claude/plate136.jpg')
cap = open('/home/claude/site/spool/next/caption.txt').read().strip()
f = json.load(open('/home/claude/site/data/forecast.json'))
hr = [h['temp'] for h in f['towns']['North Tonawanda']['hourly']][:24]

# sparkline of the next 24 hourly temps (starts ~7 a.m.)
W, H, P = 320, 62, 12
lo, hi = min(hr), max(hr)
xs = [P + i * (W - 2 * P) / (len(hr) - 1) for i in range(len(hr))]
ys = [H - P - (t - lo) * (H - 2 * P - 10) / max(1, hi - lo) for t in hr]
pts = ' '.join(f'{x:.1f},{y:.1f}' for x, y in zip(xs, ys))
ih, il = hr.index(hi), len(hr) - 1 - hr[::-1].index(lo)
spark = (f'<div class="line"><span class="lbl t">Next 24 hours</span></div>'
         f'<svg viewBox="0 0 {W} {H}" style="display:block;width:100%;max-width:420px;height:auto;margin:0 auto .4rem" role="img" aria-label="Hourly temperatures for North Tonawanda over the next 24 hours, from {hr[0]} now to a high of {hi} and a low of {lo}">'
         f'<polyline points="{pts}" fill="none" stroke="#9c3216" stroke-width="2" stroke-linejoin="round"/>'
         f'<circle cx="{xs[ih]:.1f}" cy="{ys[ih]:.1f}" r="3" fill="#9c3216"/><text x="{xs[ih]:.1f}" y="{ys[ih]-6:.1f}" text-anchor="middle" font-family="Archivo,Arial" font-size="10" fill="#24170c">{hi}&deg;</text>'
         f'<circle cx="{xs[il]:.1f}" cy="{ys[il]:.1f}" r="3" fill="#2f5e3e"/><text x="{xs[il]-5:.1f}" y="{ys[il]-6:.1f}" text-anchor="end" font-family="Archivo,Arial" font-size="10" fill="#24170c">{lo}&deg;</text>'
         f'<text x="{P}" y="{H-1}" font-family="Archivo,Arial" font-size="9" fill="#6b5a48">now</text><text x="{W-P}" y="{H-1}" text-anchor="end" font-family="Archivo,Arial" font-size="9" fill="#6b5a48">this time tomorrow</text></svg>\n')

lead = '''<div class="wire lead"><div><span class="kick">The Lead</span><h3>The Warmest Lake Erie on Record for November</h3>
<p>Lake Erie hit 60 degrees off Buffalo on Thursday, the warmest it has ever been this deep into November, WKBW reports; the old mark was 58. It was still 59 this morning, the National Weather Service says, with Lake Ontario at 58 off Rochester. Last week's record warm air did it.</p>
<p><b>What it means for winter.</b> Lake-effect snow comes from bitter air crossing warm water, and the bigger the gap, the heavier the bands. A 60-degree lake is a loaded battery: the first real arctic blast could set off an unusually intense storm. Until that cold arrives, early bands tend to fall as rain or slush, and no long cold spell shows up in the forecast models yet, WBLK notes. A lake this warm also freezes late, or barely at all, which can keep lake-effect going deep into winter.</p>
<p><b>Where it lands.</b> On southwest winds, Erie's bands hit the Southtowns and Chautauqua County hardest, Dunkirk and Fredonia included. North Tonawanda gets the big totals only when the wind lines up just so. The cover shows what that looked like on Nov. 14, 2014.</p>
<div class="pull">A 60-degree lake is a loaded battery.</div>
</div></div>
'''

R('No. 135', 'No. 136')
R('Friday &middot; November 6 &middot; 2026', 'Saturday &middot; November 7 &middot; 2026')

NEW = '''<div class="tiles">
  <div class="tile"><div class="v">52&deg;</div><div class="k">Showers Likely</div></div>
  <div class="tile"><div class="v">5:00</div><div class="k">Sunset</div></div>
  <div class="tile urg"><div class="v">2</div><div class="k">Days to Bills&ndash;Vikings</div></div>
</div>
<div class="calline"><b>Coming up</b> Sun &middot; Jets at KC, 1:00; NASCAR finale at Homestead &middot; Mon &middot; Bills at MIN, 8:15 &middot; Wed &middot; Veterans Day<br><b>Migraine log</b> Garret, Nov. 2&ndash;3; no one since</div>
<div class="plate-wrap"><div class="frame"><span class="tick tl"></span><span class="tick tr"></span><span class="tick bl"></span><span class="tick br"></span>
<img src="__PLATE__" alt="A towering gray wall of lake-effect snow rolling over the Buffalo Southtowns under a clear sky, seen from high above the city"></div>
<div class="plate-cap">Plate I &middot; The Family Album</div>
<div class="plate-sub">''' + cap + '''</div></div>
<div class="dbl-tight"><div class="a"></div><div class="b"></div></div>
<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass<span class="o">&#9788;</span></h2>
<div class="wx"><div class="bigtemp">52<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">A gray, showery Saturday at 52, about normal for the date; a windy Sunday follows</span>
Low <b>38&deg;</b> tonight &middot; showers likely before midnight<br>Rain today, 60% &middot; normal high 51&deg;</div></div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">39<sup>&deg;</sup></div><div class="d">Cloudy<br>high 52&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">43<sup>&deg;</sup></div><div class="d">Cloudy<br>high 52&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">43<sup>&deg;</sup></div><div class="d">Cloudy<br>high 52&deg;</div></div>
</div>
<div class="strip5">
  <div><div class="d">Sat</div><div class="i">&#127783;</div><div class="h">52</div><div class="w">showers likely</div></div>
  <div><div class="d">Sun</div><div class="i">&#127788;</div><div class="h">56</div><div class="w">sunny, gusty</div></div>
  <div><div class="d">Mon</div><div class="i">&#9925;</div><div class="h">54</div><div class="w">morning showers</div></div>
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">60</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#9925;</div><div class="h">54</div><div class="w">partly sunny</div></div>
</div>
''' + spark + '''<div class="line"><span class="lbl t">Sunday wind</span> Southwest gusts as high as 44 mph, with showers likely again Sunday night. <span class="lbl t">Outdoor window</span> Tuesday, mostly sunny and 60.</div>
<div class="line"><span class="lbl t">The lakes</span> Erie 59&deg; off Buffalo, Ontario 58&deg; off Rochester.</div>
''' + lead + '''<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky<span class="o">&#9790;</span></h2>
<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 0 50 96 A43.5 46 0 0 1 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>The last sliver</b>, 3 percent lit, in Virgo; rose at 5:19 a.m., sets at 3:48 p.m.<br>
<span class="lbl t">Sun</span> 6:57a &ndash; 5:00p &middot; <b>10h 3m</b>; from tomorrow, sunset comes before 5 p.m.<br>
<span class="lbl t">Planets</span> Saturn, high in the south around 10 p.m., if the clouds break.<br>
<span class="lbl t">New moon</span> Mon, Nov 9 &middot; <span class="lbl t">Beaver Moon</span> Tue, Nov 24</div></div>
<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>The moon in Libra sits opposite your sign, beside Venus.</b> Someone close wants your attention; give it. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>The moon in Libra squares your sign.</b> A rainy-day standoff over plans. Let the other side pick. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>The moon in Libra sextiles your sign and Jupiter in it.</b> Lucky, social, a little extravagant. Make the dinner reservation. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>The moon in Libra, beside Venus, sits just past your sign.</b> The list can wait a day; the couch can't. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>The moon reaches the edge of your sign by evening.</b> Quiet Saturday, sharp instincts. Trust the second thought. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
<div style="font-family:'LOI';font-style:italic;font-size:.8rem;color:var(--soft);margin-top:.4rem">The sky is real; the readings are for fun.</div>
<h2 class="sec"><span class="o">&#10038;</span>The Ledger<span class="o">&#10038;</span></h2>
<div class="ledger"><div class="num"><div class="cap">Josephine Rippo's birthday this week, at home in Niagara Falls</div><div class="big">108</div></div>
<div class="txt">She has lived there since the early 1950s, the <i>Niagara Gazette</i> reports, and the family has been throwing parties for her every year since she turned 99.</div></div>
<h2 class="sec"><span class="o">&#10038;</span>The National Wire<span class="o">&#10038;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>A New Chief of Staff</h3><p>President Trump named longtime aide Stephen Miller his White House chief of staff Friday, replacing Susie Wiles in the biggest shake-up of his team since Republicans' midterm losses, CBS reports. "I wanted to make a change," the president said, calling Miller "one of my most trusted advisors."</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>A Better Jobs Month</h3><p>Employers added 165,000 jobs in October, more than expected, PBS NewsHour reports, and the August and September numbers were revised up by a combined 84,000. The good news comes as questions grow about how long the boom in artificial-intelligence spending can last.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>The Pope Goes Home, Sort Of</h3><p>Pope Leo XIV, 71, told reporters he is "in pretty good health" as he began a 12-day Latin America tour, three weeks after surgery for lung cancer, the BBC reports. The trip runs through Uruguay and Argentina to Peru, where he lived and worked for years, which the Vatican calls a "homecoming."</p></div></div>
<h2 class="sec"><span class="o">&#9962;</span>The Home Wire<span class="o">&#9962;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>Dunkirk &middot; The Fire Chief on Battery Farms</h3><p>Battery energy storage systems, big banks of batteries that soak up power from the grid and release it when demand is high, carry "unique hazards," Dunkirk Fire Chief Nicholas Barter told Revitalize Dunkirk, the <i>Observer</i> reports. "Everything has risk," he said; the department is working with developers to plan for them before one arrives.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Newfane &middot; 67 Years Behind the Chair</h3><p>Bob Eadie put away his clippers for good on Oct. 30 after 67 years as Newfane's barber, the <i>Lockport Journal</i> reports. For generations of families, a trip to his shop was a chance to catch up and swap stories as much as a haircut.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Niagara Falls &middot; Veterans Day Ceremonies</h3><p>The Niagara Falls Veterans Monument Commission holds its annual Veterans Day ceremony at the monument in Hyde Park on Wednesday, and the Town of Niagara holds its own the same day, the <i>Niagara Gazette</i> reports. It's one of several gatherings planned across Niagara County.</p></div></div>
<h2 class="sec"><span class="o">&#9733;</span>The Marquee<span class="o">&#9733;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>Pattinson or Hoult for Bond?</h3><p>Robert Pattinson and Nicholas Hoult both screen-tested to play the next James Bond for director Denis Villeneuve, Variety reports. Insiders tell Deadline they join Jack Lowden, Josh O'Connor and Callum Turner on the shortlist; nothing is confirmed.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Tiger and Elin, Together for Charlie</h3><p>Tiger Woods and his ex-wife, Elin Nordegren, came together at their 17-year-old son Charlie's high school signing day in Florida, Us Weekly reports. Charlie is headed to Florida State to play golf.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>C&eacute;line Dion, Metalhead</h3><p>C&eacute;line Dion was caught on fan video playing air bass from a suite at Metallica's residency at the Sphere in Las Vegas on Thursday, Billboard reports. The "My Heart Will Go On" singer looked like she knew every riff.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>The Knicks Defend Taylor Swift</h3><p>After Knicks guard Tyler Kolek called Taylor Swift a "very performative" fan, the team's spokesperson thanked her for "many years" of support, Deadline reports. So much for that.</p></div></div>
<h2 class="sec"><span class="o">&#127944;</span>The Gridiron<span class="o">&#127944;</span></h2>
<div class="touch-head">Injury Reports</div>
<div class="line"><b>Bills</b> &middot; Tackle Dion Dawkins and Alec Anderson are still out ahead of Monday night at Minnesota, while tight end Dalton Kincaid was upgraded to full practice, Buffalo Rumblings reports. The Vikings are starting Carson Wentz at quarterback over Kyler Murray.</div>
<div class="line"><b>Jets</b> &middot; Garrett Wilson, still in the concussion protocol, will miss Sunday's game at Kansas City, Gang Green Nation reports. The good news: Breece Hall, David Bailey and Mason Taylor were all full participants in Thursday's practice.</div>
<h2 class="sec"><span class="o">&#9873;</span>The Chase<span class="o">&#9873;</span></h2>
<div class="line">Tomorrow at Homestead decides the title. Larson 2,469; Bell 2,402; Hamlin 2,399.</div>
<h2 class="sec"><span class="o">&#9790;</span>On This Day<span class="o">&#9790;</span></h2>
<div class="otd"><b>November 7, 1940</b> &mdash; In a 40-mph wind, the brand-new Tacoma Narrows Bridge in Washington twisted, rippled and fell into Puget Sound. Engineers still study "Galloping Gertie."</div>
<h2 class="sec"><span class="o">&#10023;</span>Question of the Day<span class="o">&#10023;</span></h2>
<div class="qotd">I'm warmer in November than in May, and I make snow without ever leaving my bed. What am I? <i>Answer below the fold.</i></div>
'''
S('<div class="tiles">', '<div class="dbl"><div class="a"></div><div class="b"></div></div>\n<div class="colo">', NEW)
R("<b>Question of the Day:</b> An umbrella.", "<b>Question of the Day:</b> Lake Erie.")
S('<div class="s">Forecast per', '<div class="ask">',
'''<div class="s">Forecast, lake temperatures and radar per NWS Buffalo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; normals from NOAA &middot; sky computed for 14120 &middot; headlines via CBS, PBS NewsHour, BBC, WKBW, WBLK, the <i>Niagara Gazette</i>, the <i>Lockport Journal</i>, the Dunkirk <i>Observer</i>, Variety, Deadline, Us Weekly, Billboard, Buffalo Rumblings, Gang Green Nation &middot; NASCAR points via Sportradar</div>
''')

ed = {"date": "2026-11-07", "no": 136, "body_html": src, "plate_path": "/home/claude/plate136.jpg",
      "plate_caption": cap,
      "headline": "The warmest Lake Erie on record · Miller in, Wiles out · Bond screen tests"}
for p in ['/home/claude/edition-2026-11-07.json', '/home/claude/site/data/edition-2026-11-07.json']:
    json.dump(ed, open(p, 'w'), ensure_ascii=False, indent=1)
print('ok', hr[:3], lo, hi)
