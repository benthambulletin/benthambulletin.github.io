import json
d=json.load(open('edition-2026-09-30.json')); b=d['body_html']
baro=open('/tmp/claude-0/-home-claude/001a10af-13f9-5479-8fec-28bf86d9c496/scratchpad/baro99.html').read(); baro=baro[:baro.index('<!--')]
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
H=lambda o,t:f'<h2 class="sec"><span class="o">{o}</span>{t}<span class="o">{o}</span></h2>'
R('No. 98','No. 99')
R('Wednesday &middot; September 30 &middot; 2026','Thursday &middot; October 1 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">76&deg;</div><div class="k">Showers, then rain</div></div>
  <div class="tile"><div class="v">29.96&#8243; &#9660;</div><div class="k">Falling ahead of rain</div></div>
  <div class="tile urg"><div class="v">33</div><div class="k">Days to Election Day</div></div>
</div>
''')
R('First light, Wednesday morning.','Luka, zipped into the space-print sleep sack at bedtime.')
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>Luka has the cover</b>, planets and rockets and all, holding out a little longer before bed. October starts warm and wet: 76 today with showers, steady rain tonight into Friday, then a sunny weekend. Halftime at Sunday's Bills game is Natasha Bedingfield.
''')
S('<div class="wx">','<div class="towns">','''<div class="wx"><div class="bigtemp">76<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">Warm, gusty, and the rain moves in</span>
Low <b>59&deg;</b> &middot; Southwest 10&ndash;15, gusts to 26<br>Rain <b>70%</b> today, near certain tonight</div></div>
''')
S('<div class="towns">','<div class="strip5">','''<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">63<sup>&deg;</sup></div><div class="d">Cloudy &middot; high 76&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">66<sup>&deg;</sup></div><div class="d">Light rain &middot; high 76&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">63<sup>&deg;</sup></div><div class="d">Cloudy &middot; high 77&deg;</div></div>
</div>
''')
S('<div class="strip5">','<div class="line"><span class="lbl t">The week turns</span>','''<div class="strip5">
  <div><div class="d">Thu</div><div class="i">&#127783;</div><div class="h">76</div><div class="w">showers, rain tonight</div></div>
  <div><div class="d">Fri</div><div class="i">&#127783;</div><div class="h">66</div><div class="w">rain till 2</div></div>
  <div><div class="d">Sat</div><div class="i">&#9728;</div><div class="h">65</div><div class="w">sunny</div></div>
  <div><div class="d">Sun</div><div class="i">&#9728;</div><div class="h">69</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Mon</div><div class="i">&#9728;</div><div class="h">60</div><div class="w">mostly sunny</div></div>
</div>
''')
S('<div class="line"><span class="lbl t">The week turns</span>','<h2 class="sec"><span class="o">&#127810;</span>The Turning','''<div class="line"><span class="lbl t">Timing</span> Scattered showers today, steady rain after 9 tonight, done by about 2 Friday afternoon. Tonight's low comes early; it warms to about 65 by morning. Then Saturday is sunny and 65 and Monday tops out at 60, the coolest afternoon in a while. <span class="lbl t">Outdoor window</span> Saturday and Sunday.</div>
''')
S('<div class="line"><b>The foliage report comes out this afternoon.</b>','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','''<div class="line"><b>The state's weekly report is all Adirondacks:</b> near peak and some full peak this weekend, with the Catskills at midpoint. Western New York's color usually peaks in the last week of October, so the high country is three weeks ahead of us.</div>
''')
S('<div class="sky">','<div class="stars">','''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 1 50 96 A18 46 0 0 1 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>Seventy-one percent</b> and waning, in Gemini, rising at 9:46 tonight behind the clouds.<br>
<span class="lbl t">Sun</span> 7:12a &ndash; 6:56p &middot; <b>11h 44m</b><br>
<span class="lbl t">Last quarter</span> Sat, Oct 3 &middot; <span class="lbl t">Next new moon</span> Sat, Oct 10</div></div>
<div class="line"><span class="lbl r">Tonight</span> Rain and cloud cover everything. Clear skies return Saturday night, with Saturn up at dusk and Mars and Jupiter before dawn.</div>
''')
S('<div class="stars">','<div style="font-family:','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>The moon in Gemini sextiles Saturn in your sign</b>. Structure and quick thinking line up for once. Make the plan you keep meaning to make. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>The Sun in Libra is opposite Saturn</b>, the yearly tug between what you owe others and what you owe yourself. Today it comes out even. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Mars in Leo trines Neptune almost exactly</b> and squares Mercury. Act on instinct, but give the paperwork a second look. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>Mercury squares Mars to within half a degree</b>, the sharpest point of this week's friction. Short tempers all around; you can be the one who isn't. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Mercury and Venus together in your sign</b>, with Pluto squaring Mercury. You will be persuasive today. Use it on something that matters. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
S('<div class="baro-top">','<div class="line"><span class="lbl t">Calm before the rain</span>',baro)
S('<div class="line"><span class="lbl t">Calm before the rain</span>','<h2 class="sec"><span class="o">&#10038;</span>The Ledger','''<div class="line"><span class="lbl t">The drop has started</span> 29.96 this morning, down 3 millibars since yesterday morning and still sliding as the rain moves in. That is the size of fall that can set off a headache, so the dial is at moderate today. It should bottom out with the rain tonight and climb back Saturday.</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">Niagara County opioid money left unspent</div><div class="big">$4M</div></div>
<div class="txt">Of $8 million received over three years to fight addiction, the county spent less than half, while overdose deaths kept rising.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>U.S. Forces Leave Iraq','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>Tennessee Execution Fails; Governor Halts the Rest</h3><p>Christa Pike survived two doses of the lethal drug Wednesday and is in the hospital. Gov. Bill Lee stopped the state's remaining executions for the year.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Pilot Stabbed in Cockpit, Flight Diverted</h3><p>A flydubai co-pilot is accused of stabbing the captain on a Dubai&ndash;Tel Aviv flight, which landed in Saudi Arabia. Israel says the motive is not yet known.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Sonderling Confirmed at Labor</h3><p>The Senate confirmed Keith Sonderling as labor secretary; he had been running the department since Lori Chavez-DeRemer left in April.</p></div></div>
''')
R('<b>34 days</b>','<b>33 days</b>')
S('<h2 class="sec"><span class="o">&#9962;</span>The Home Wire','<h2 class="sec"><span class="o">&#9733;</span>The Marquee',H('&#9962;','The Home Wire')+'''
<div class="wire"><div class="num">1</div><div><h3>Lewiston &middot; A Month of "Haunted Lewiston"</h3><p>The village has something spooky planned nearly every day of October.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Chautauqua &middot; Jamestown OTB Closing Oct. 31</h3><p>Western New York Off-Track Betting is cutting its branches from eight to two, a month after a record payout to the county.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Rochester &middot; Neighbors Weigh In on the Zoning Rewrite</h3><p>The first of four district meetings on the city's zoning code overhaul took comments from the northeast side.</p></div></div>
''')
S('<h2 class="sec"><span class="o">&#9733;</span>The Marquee','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron',H('&#9733;','The Marquee')+'''
<div class="wire"><div class="num">1</div><div><h3>A Record for Jordan's "Last Dance" Jersey</h3><p>A Michael Jordan jersey from his final Bulls season sold for $12.3 million, the most ever paid for a piece of his memorabilia.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Florence Pugh in <i>East of Eden</i></h3><p>Netflix's seven-part Steinbeck adaptation, created by Zoe Kazan, is drawing strong early reviews, most of them for Pugh.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>The Chicks Open Their Anniversary Tour</h3><p>Opening night in Detroit: <i>Taking the Long Way</i> played in full for its 20th birthday, then the hits.</p></div></div>
''')
S('<div class="touch-head">Four Days to Sunday</div>','<table class="tbl">','''<div class="touch-head">Three Days to Sunday</div>
<div class="line"><b>Bills</b> &middot; Christian Benford (toe), Keon Coleman (ankle) and Joe Andreessen (knee) sat out Wednesday's practice. Josh Allen is not on the report.</div>
<div class="line"><b>Jets</b> &middot; Minkah Fitzpatrick, out since the opener, has "a really good chance" to play Sunday, Aaron Glenn says. Breece Hall, Mason Taylor and Adonai Mitchell are week-to-week; Braelon Allen and Isaiah Davis would carry the run game.</div>
''')
S('<div class="touch-head">Four Days to Las Vegas</div>','<div class="cards">','''<div class="touch-head">Three Days to Las Vegas</div>
<div class="line">Race five of ten Sunday evening. Larson leads Hamlin by 26 and Bell by 50.</div>
''')
S('<div class="otd">','<h2 class="sec"><span class="o">&#10023;</span>Question','''<div class="otd"><b>October 1, 1971</b> &mdash; Walt Disney World opened in Florida, with the Magic Kingdom as its only park. Today it has four, and October is its busiest month for Halloween.</div>
''')
R('What has hands but cannot clap?','What gets wetter the more it dries?')
R('<b>Question of the Day:</b> A clock.','<b>Question of the Day:</b> A towel.')
R('headlines via NPR, CBS, BBC, WKBW, WIVB, Rochester First, Billboard and the Hollywood Reporter','headlines via NPR, CBS, BBC, WIVB, Niagara Gazette, Dunkirk Observer, Rochester First, Variety, Billboard &middot; injury reports via WGR and the Jets')
d.update(date='2026-10-01',no=99,body_html=b,plate_path='/home/claude/plate99.jpg',plate_caption='Luka, zipped into the space-print sleep sack at bedtime',headline="Luka at bedtime · Rain tonight, sun this weekend · Pressure falling · $4M unspent in Niagara County")
json.dump(d,open('site/data/edition-2026-10-01.json','w'),indent=1); json.dump(d,open('edition-2026-10-01.json','w'),indent=1)
p=json.load(open('site/data/pressure.json'))
if p[-1]['date']!='2026-10-01': p.append({"date":"2026-10-01","in":29.96,"mb":1014.4,"station":"KIAG","time":"05:53 EDT"})
json.dump(p,open('site/data/pressure.json','w'),indent=1)
print('ok')
