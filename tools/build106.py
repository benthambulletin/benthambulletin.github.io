import json
d=json.load(open('edition-2026-10-07.json')); b=d['body_html']
baro=open('/tmp/claude-0/-home-claude/001a10af-13f9-5479-8fec-28bf86d9c496/scratchpad/baro106.html').read(); baro=baro[:baro.index('<!--')].strip()+'\n'
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
R('No. 105','No. 106')
R('Wednesday &middot; October 7 &middot; 2026','Thursday &middot; October 8 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">65&deg;</div><div class="k">Sunny, cool</div></div>
  <div class="tile"><div class="v">29.83&#8243; &#9650;</div><div class="k">Rising fast</div></div>
  <div class="tile urg"><div class="v">26</div><div class="k">Days to Election Day</div></div>
</div>
''')
S('<div class="plate-wrap">','<h2 class="sec"><span class="o">&#9825;</span>Family Today','')
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>Sweater weather is back.</b> A cool, clear Thursday morning after last night's wind, and the porch cushions can come back out. Twenty-three days to Halloween; the pumpkins have time.
''')
S('<div class="wx">','<div class="towns">','''<div class="wx"><div class="bigtemp">65<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">Bright, cool and settled</span>
Low <b>45&deg;</b> tonight &middot; west 7&ndash;14, gusts to 24<br>A stray shower after 4 p.m., 20 percent</div></div>
''')
S('<div class="towns">','<div class="strip5">','''<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">48<sup>&deg;</sup></div><div class="d">Clear &middot; high 65&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">59<sup>&deg;</sup></div><div class="d">Cloudy &middot; high 64&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">48<sup>&deg;</sup></div><div class="d">Mostly clear &middot; high 65&deg;</div></div>
</div>
''')
S('<div class="strip5">','<h2 class="sec"><span class="o">&#127810;</span>The Turning','''<div class="strip5">
  <div><div class="d">Thu</div><div class="i">&#9728;</div><div class="h">65</div><div class="w">sunny, stray shower late</div></div>
  <div><div class="d">Fri</div><div class="i">&#9728;</div><div class="h">65</div><div class="w">sunny</div></div>
  <div><div class="d">Sat</div><div class="i">&#9728;</div><div class="h">73</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Sun</div><div class="i">&#127782;</div><div class="h">70</div><div class="w">showers likely</div></div>
  <div><div class="d">Mon</div><div class="i">&#9729;</div><div class="h">70</div><div class="w">mostly cloudy</div></div>
</div>
<div class="line"><span class="lbl r">Tonight</span> Mostly clear and crisp, down to 45. <span class="lbl t">Outdoor window</span> Today through Saturday, warmest Saturday at 73. Sunday's showers are likely from 8 a.m. on, 60 percent; rake Saturday.</div>
''')
S('<div class="line"><b>The state','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','''<div class="line"><b>Monroe County is turning fast.</b> This week's state foliage report has Greece past 30 percent color change, the closest reading to Scottsville, and Rochester First says peak is coming quickly. North Tonawanda usually peaks in the last week of October.</div>
''')
R('<b>A sliver</b>, 10 percent lit, in Virgo, rising at 5:05 a.m.<br>','<b>A thin sliver</b>, 5 percent lit, in Virgo, rose at 5:04 a.m.<br>')
R('7:20a &ndash; 6:46p &middot; <b>11h 26m</b>','7:20a &ndash; 6:44p &middot; <b>11h 24m</b>')
S('<div class="line"><span class="lbl r">Tonight</span> Clouds and storms','<div class="stars">','''<div class="line"><span class="lbl r">Tonight</span> Clear skies and almost no moon. Saturn climbs in the east after dark; before dawn, Mars and Jupiter stand high in the east-southeast. Daylight is shrinking by about three minutes a day.</div>
''')
S('<div class="stars">','<div style="font-family','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>Saturn holds in your sign as the Sun across the sky pulls away</b>. Finish something instead of starting something. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>Uranus and Neptune trade a friendly sextile</b>. An odd idea from someone younger turns out to be the right one. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Venus squares Mars in your sign</b>. Charm gets further than pushing today. Ask nicely, twice if needed. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>The moon's last thin days in your sign</b>. Clear the desk before Saturday's new moon. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Mercury catches Venus in your sign</b>. Say the kind thing out loud. Birthday season is close. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
S('<div class="baro-top">','<h2 class="sec"><span class="o">&#10038;</span>The Ledger',baro+'''<div class="line"><span class="lbl t">Rebound</span> 29.83 and climbing fast, up about 6 millibars since the low at 9 last night. Over 24 hours it nets out to nearly flat, so not a big-swing day.</div>
<div class="line"><span class="lbl t">The log</span> Days since the last one: Garret 2, Dad 2, Mom none logged. October so far: Garret 1, Dad 1, Mom 0.</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">October Surprise, 2006</div><div class="big">20&Prime;</div></div>
<div class="txt">Twenty inches of heavy, wet snow fell on Buffalo on the night of Oct. 12, 2006, with the leaves still on the trees. Limbs and power lines came down across the region. Twenty years ago next week.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Tropical','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>Margaret Hamilton Dies at 90</h3><p>The computer scientist led the team that wrote the software that landed Apollo 11 on the moon. She later received the Presidential Medal of Freedom.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>More Time to Cut Student Loan Rates</h3><p>The Education Department pushed back its Sept. 30 deadline so more borrowers can enroll in its interest-rate reduction. The lower rate lasts through June 2028.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Mall of America Plot Charged</h3><p>An 18-year-old Twin Cities man was arrested Tuesday at a meeting set up to buy an assault rifle, accused of planning an attack at the mall later this month. The FBI says he pledged allegiance to ISIS.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>FDA Abortion Pill Review Runs Into 2027</h3><p>The FDA says its safety review of mifepristone, the main abortion pill, will continue into next year. Abortion opponents hoping for new limits condemned the timeline.</p></div></div>
''')
R('<b>27 days</b> to Election Day &middot; early voting Oct 24&ndash;Nov 1 &middot; register by Oct 24','<b>26 days</b> to Election Day &middot; new Marist poll: Hochul leads Blakeman by 11 among registered voters, Blakeman leads upstate &middot; register by Oct 24')
S('<h2 class="sec"><span class="o">&#9962;</span>The Home Wire<span class="o">&#9962;</span></h2>','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<h2 class="sec"><span class="o">&#9962;</span>The Home Wire<span class="o">&#9962;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>Chautauqua &middot; $7.3 Million for Barcelona Harbor</h3><p>The Army Corps of Engineers is working on the West Breakwater at Barcelona Harbor. For years waves there have pushed in large amounts of sediment.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Niagara &middot; Fire Companies Land Nearly $1 Million</h3><p>Four Niagara Region fire departments won close to $1 million in federal FEMA grants. The money comes from the firefighter assistance and staffing programs.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Buffalo &middot; Red Panda Cubs Debut</h3><p>The Buffalo Zoo's two red panda cubs are now out in the habitat with their mom, Himalaya. They're the 14th and 15th red pandas born at the zoo, worth a trip with a three-year-old.</p></div></div>
''')
S('<h2 class="sec"><span class="o">&#9733;</span>The Marquee<span class="o">&#9733;</span></h2>','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron','''<h2 class="sec"><span class="o">&#9733;</span>The Marquee<span class="o">&#9733;</span></h2>
<div class="wire"><div class="num">1</div><div><h3><i>Below</i> Surfaces on Netflix</h3><p>Josh Hartnett plays a fisherman in a remote Newfoundland village in a six-part series about a sea creature big enough to sink ships. <i>Variety</i> calls it exhilarating; <i>The Hollywood Reporter</i>, likably silly.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Rihanna's Vault</h3><p>Rihanna says she has "at least" 170 unreleased songs. A$AP Rocky said she was in the studio in August.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Disney Holds the Line on Tickets</h3><p>Many Disneyland and Disney World ticket tiers are unchanged for 2026&ndash;27. The ones going up are rising by some of the smallest amounts in years.</p></div></div>
''')
R('<div class="touch-head">Five Days to Los Angeles</div>','<div class="touch-head">Four Days to Los Angeles</div>')
S('<div class="line"><b>Bills</b>','<div class="pnote">','''<div class="line"><b>Bills</b> &middot; The Rams on Monday night, 8:15 on ABC, coming off Sunday's 26&ndash;29 loss to New England. Off the field, a new five-part docuseries, <i>Just One Before I Die</i>, follows Bills fans through the hope and the heartbreak.</div>
<div class="line"><b>Jets</b> &middot; Home against Cleveland Sunday at 1:00, and the Jets go in as slight favorites: Sportradar's model gives them a 55 percent chance. A good week to start the climb.</div>
''')
R('first game Thu 8:15 p.m., Bucs at Dallas.</div>','first game tonight, 8:15, Bucs at Dallas. The pot stands at $65.</div>')
R('<div class="touch-head">Four Days to Charlotte</div>','<div class="touch-head">Three Days to Charlotte</div>')
R('Larson brings a 40-point lead over Hamlin into race six.','Hamlin has won four races this year to Larson\'s two, but Larson holds the points lead by 40. Joey Logano sits fourth, 71 back.')
S('<div class="otd">','<h2 class="sec"><span class="o">&#10023;</span>Question','''<div class="otd"><b>October 8, 1871</b> &mdash; The Great Chicago Fire broke out and burned for two days, leveling much of the city. The same night, a wildfire around Peshtigo, Wisconsin, killed far more people, still the deadliest in American history.</div>
''')
S('<div class="qotd">','<div class="dbl">','''<div class="qotd">I have a face but no head, a light inside but no switch, and I sit on the porch every October night. What am I? <i>Answer below the fold.</i></div>
''')
R('<b>Question of the Day:</b> A mushroom.','<b>Question of the Day:</b> A jack-o\'-lantern.')
R('headlines via CBS, NPR, WIVB, WXXI, Niagara Gazette, Deadline, Hollywood Reporter &middot; Bills via CBS Sports &middot; wire from the national desks','headlines via CBS, NPR, BBC, PBS, WKBW, WIVB, Niagara Gazette, Rochester First, Variety, Hollywood Reporter, Billboard, Deadline &middot; scores and standings via Sportradar &middot; wire from the national desks')
d['no']=106; d['headline']='Sweater weather · Pressure rebounds · Monroe County turning · Margaret Hamilton dies at 90'
d['body_html']=b; d['plate_path']=None; d['plate_caption']=None
for k in list(d):
    if isinstance(d[k],str) and '2026-10-07' in d[k]: d[k]=d[k].replace('2026-10-07','2026-10-08')
json.dump(d,open('edition-2026-10-08.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-08.json','w'),ensure_ascii=False,indent=1)
p=json.load(open('site/data/pressure.json')); p=[x for x in p if x['date']!='2026-10-08']
p.append({'date':'2026-10-08','in':29.83,'mb':1010.2,'station':'KIAG','time':'06:53 EDT'}); json.dump(p,open('site/data/pressure.json','w'),indent=1)
print('ok')
# --- review fixes ---
d=json.load(open('edition-2026-10-08.json')); b=d['body_html']
R('Twenty inches of heavy, wet snow fell on Buffalo on the night of Oct. 12, 2006, with the leaves still on the trees.','Twenty inches of heavy, wet snow fell across the region starting the evening of Oct. 12, 2006, with the leaves still on the trees.')
S('<div class="wire"><div class="num">1</div><div><h3>Chautauqua','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; A Slower Fall Market</h3><p>Hilton realtor Tom Fox told Rochester First he expected the usual fall cooling, but says this year is different. He still has homes listed in Pittsford, Penfield and Greece.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Chautauqua &middot; $7.3 Million for Barcelona Harbor</h3><p>The Army Corps of Engineers is working on the West Breakwater at Barcelona Harbor. For years waves there have pushed in large amounts of sediment.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Niagara &middot; Fire Companies Land Nearly $1 Million</h3><p>Four Niagara Region fire departments won close to $1 million in federal FEMA grants. The money comes from the firefighter assistance and staffing programs.</p></div></div>
''')
S('<div class="line">The Bank of America 400','<div class="cards">','''<div class="line">Hamlin has won four races this year to Larson's two, but Larson still leads him by 40 points. Christopher Bell sits third, 55 back, and Joey Logano fourth, 71 back. After Sunday, four races remain before Homestead.</div>
''')
R('Over 24 hours it nets out to nearly flat, so not a big-swing day.','Over 24 hours it nets out nearly flat, but the climb is quick: a moderate day, not a big swing.')
R('Saturn holds in your sign as the Sun across the sky pulls away</b>. Finish','Saturn, settled in your sign, rewards the slow job done right</b>. Finish')
R('Forecast &amp; barometer per NWS Buffalo &middot; Niagara Falls station','Forecast &amp; barometer per NWS Buffalo &middot; Niagara Falls, Dunkirk and Rochester stations')
R('PBS, WKBW, WIVB, Niagara','PBS, WKBW, Niagara')
R("Sunday's 26&ndash;29 loss","Sunday's 29&ndash;26 loss")
R('state foliage report has Greece past','state foliage report has Greece, in Monroe County, past')
d['body_html']=b
json.dump(d,open('edition-2026-10-08.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-08.json','w'),ensure_ascii=False,indent=1)
R('Limbs and power lines came down across the region.','Falling trees took down power lines.')
d['body_html']=b
json.dump(d,open('edition-2026-10-08.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-08.json','w'),ensure_ascii=False,indent=1)
print('fixed')
