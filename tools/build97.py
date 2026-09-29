import json
d=json.load(open('edition-2026-09-28.json')); b=d['body_html']
baro=open('/tmp/claude-0/-home-claude/001a10af-13f9-5479-8fec-28bf86d9c496/scratchpad/baro97.html').read()
baro=baro[:baro.index('<!--')]
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
H=lambda o,t:f'<h2 class="sec"><span class="o">{o}</span>{t}<span class="o">{o}</span></h2>'
R('No. 96','No. 97')
R('Monday &middot; September 28 &middot; 2026','Tuesday &middot; September 29 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile good"><div class="v">73&deg;</div><div class="k">Fog early, then sun</div></div>
  <div class="tile good"><div class="v">30.02&#8243; &#9650;</div><div class="k">Rising again</div></div>
  <div class="tile urg"><div class="v">35</div><div class="k">Days to Election Day</div></div>
</div>
''')
R('Luka, bright-eyed on a Monday.','Last light over Port Bay, Saturday evening.')
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>Port Bay has the cover</b>, Saturday's sunset over the water. The warm stretch starts today: 73, then 74 and 77 before the rain returns Thursday night. If there is anything to get done outside this week, today through Thursday afternoon is the window.
''')
S('<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass','<div class="towns">',H('&#9788;','The Weather Glass')+'''
<div class="wx"><div class="bigtemp">73<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">The warm three days begin</span>
Low <b>56&deg;</b> &middot; Light west wind<br>Rain <b>None</b> until Thursday night</div></div>
''')
S('<div class="towns">','<div class="strip5">','''<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">61<sup>&deg;</sup></div><div class="d">Cloudy, patchy fog &middot; high 73&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">61<sup>&deg;</sup></div><div class="d">Fog, then partly sunny &middot; high 70&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">57<sup>&deg;</sup></div><div class="d">Mostly cloudy &middot; high 70&deg;</div></div>
</div>
''')
S('<div class="strip5">','<div class="line"><span class="lbl t">Outdoor window','''<div class="strip5">
  <div><div class="d">Tue</div><div class="i">&#9925;</div><div class="h">73</div><div class="w">partly sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#9729;</div><div class="h">74</div><div class="w">mostly cloudy</div></div>
  <div><div class="d">Thu</div><div class="i">&#9925;</div><div class="h">77</div><div class="w">rain at night</div></div>
  <div><div class="d">Fri</div><div class="i">&#127783;</div><div class="h">68</div><div class="w">showers likely</div></div>
  <div><div class="d">Sat</div><div class="i">&#9728;</div><div class="h">66</div><div class="w">mostly sunny</div></div>
</div>
''')
S('<div class="line"><span class="lbl t">Outdoor window','<h2 class="sec"><span class="o">&#127810;</span>The Turning','''<div class="line"><span class="lbl t">The rain</span> Thursday night and Friday, 70% both times, a tenth to a quarter of an inch. Thursday afternoon turns gusty, up to 25 mph. Friday night drops to 48, the coolest in a week. <span class="lbl t">Outdoor window</span> Today through Thursday afternoon.</div>
''')
S('<div class="line"><b>Wednesday is the next report.</b>','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','''<div class="line"><b>Tomorrow afternoon is the next foliage report.</b> Three warm days with sun in them will not hurry the maples much; the cool nights behind Friday's rain will.</div>
''')
S('<div class="sky">','<div class="stars">','''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 1 50 96 A32 46 0 0 1 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>Eighty-nine percent</b> and waning, in Taurus, up at 8:12 tonight.<br>
<span class="lbl t">Sun</span> 7:10a &ndash; 7:00p &middot; <b>11h 50m</b><br>
<span class="lbl t">Last quarter</span> Sat, Oct 3 &middot; <span class="lbl t">Next new moon</span> Sat, Oct 10</div></div>
<div class="line"><span class="lbl r">Tonight</span> <b>Saturn</b> rises at 7:16 and is the bright steady light low in the east after dark. <b>Mars</b> is up at 1:27 a.m. and <b>Jupiter</b> at 3:04. Mercury crosses into Scorpio tomorrow morning.</div>
''')
S('<div class="stars">','<div style="font-family:','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>Mars, your ruler, is trine Neptune</b>, sitting in your sign at three degrees. The push is gentle today and goes further for it. A good day to help someone without making a thing of it. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>The moon in Taurus is your quiet ally</b> this week, easy and unhurried. With Mars gone from your sign, the house can run at half speed. Let it. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Mars in Leo is opposite Pluto</b>, a standoff between your new energy and someone else's hold on the rules. Pick the fight you would still want next month. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>Mercury, your ruler, spends its last day in Libra</b>, square Mars, before moving into Scorpio tomorrow. Finish the conversation today; tomorrow it gets more guarded. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Mercury arrives in your sign tomorrow</b>, joining Venus. For the next few weeks you will say what you mean and be listened to. Today, rehearse. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
S('<div class="baro-top">','<div class="line"><span class="lbl t">The slide has nearly stopped</span>',baro)
S('<div class="line"><span class="lbl t">The slide has nearly stopped</span>','<h2 class="sec"><span class="o">&#10038;</span>The Ledger','''<div class="line"><span class="lbl t">Climbing back</span> 30.02 at dawn, up about a tenth since Sunday morning's low. The chart now shows every hour of the last three days, not just the mornings: the weekend slide, the flat Monday, and the slow climb overnight. A gentle rise like this is the easy kind.</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">Canadian imports now barred</div><div class="big">$1B</div></div>
<div class="txt">Nearly a billion dollars' worth, including alcohol, dairy and motorcycles, under a U.S. ban that took effect this morning. The border is twenty minutes from the front door.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Trump Expects','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>OpenAI Pulls Its New Model Over Safety</h3><p>The company decided not to release GPT-6.1 Astra, saying it "didn't quite meet the bar," and gave an update on incidents in which its models got into Australian government systems.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Jack Smith Testifies Today</h3><p>The former special counsel goes before the Senate Judiciary Committee, which is investigating his two cases against the president.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Senate Passes a College Sports Bill</h3><p>The Protect College Sports Act, backed by the NCAA, aims to set national rules on eligibility, transfers and pay. Its future in the House is unclear.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>The Nor'easter Uncovered a Shipwreck</h3><p>Sand stripped away on Nantucket exposed what may be the Warren Sawyer, which ran aground in 1884 carrying cotton and scrap iron to Boston.</p></div></div>
''')
R('<b>36 days</b>','<b>35 days</b>')
S('<h2 class="sec"><span class="o">&#9962;</span>The Home Wire','<h2 class="sec"><span class="o">&#9733;</span>The Marquee',H('&#9962;','The Home Wire')+'''
<div class="wire"><div class="num">1</div><div><h3>Town of Tonawanda &middot; A 3.9% Tax Levy Increase Proposed</h3><p>Supervisor John Flynn put it on the table at Monday's town board meeting, citing inflation, labor costs and public safety.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Statewide &middot; Unemployment Filing Goes Dark in November</h3><p>The Labor Department will shut down unemployment insurance services for nine to twelve days starting Nov. 2 to replace its 50-year-old system.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Rochester &middot; A Vacant Lot Becomes a Forest</h3><p>The former Family Dollar site on the city's west side is being planted as a small urban forest.</p></div></div>
''')
S('<h2 class="sec"><span class="o">&#9733;</span>The Marquee','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron',H('&#9733;','The Marquee')+'''
<div class="wire"><div class="num">1</div><div><h3>Goo Goo Dolls Come Home Again</h3><p>Two benefit shows at the Town Ballroom, Nov. 20 and 21, for FeedMore Western New York. Tickets go on sale Friday at 10.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>McCartney on the Years After the Beatles</h3><p><i>Man on the Run</i>, Morgan Neville's documentary on Paul McCartney's first decade after the band, screened at the Academy Museum.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>The BBC's Boss Watched an A.I. <i>Doctor Who</i></h3><p>Matt Brittin says someone sent him a fully A.I.-generated episode and it was "pretty good," though "not going to replace humans."</p></div></div>
''')
S('<h2 class="sec"><span class="o">&#127944;</span>The Gridiron','<h2 class="sec"><span class="o">&#9873;</span>The Chase',H('&#127944;','The Gridiron')+'''
<div class="touch-head">Five Days to Sunday</div>
<div class="line"><b>Bills</b> &middot; 3&ndash;0 and home to the Patriots Sunday at one. New England is 1&ndash;2 after a 35&ndash;6 loss in Jacksonville. The week's job is simple: hold on to the ball.</div>
<div class="line"><b>Jets</b> &middot; at Chicago Sunday at one. The Bears looked sharp last night, beating Philadelphia 27&ndash;7 and handing the Eagles their first loss. A tough trip, and a chance to show Sunday's comeback was no accident.</div>
<table class="tbl"><tr><th>AFC East</th><th class="n">W</th><th class="n">L</th><th class="n">PCT</th></tr>
<tr><td style="color:var(--red)">Buffalo</td><td class="n">3</td><td class="n">0</td><td class="n">1.000</td></tr>
<tr><td style="color:var(--red)">N.Y. Jets</td><td class="n">1</td><td class="n">2</td><td class="n">.333</td></tr>
<tr><td>New England</td><td class="n">1</td><td class="n">2</td><td class="n">.333</td></tr>
<tr><td>Miami</td><td class="n">0</td><td class="n">3</td><td class="n">.000</td></tr></table>
''')
S('<div class="touch-head">Larson Takes Kansas</div>','<div class="cards">','''<div class="touch-head">Larson Up 26</div>
<div class="line">Five races into ten, Kyle Larson leads Denny Hamlin by 26 points and Christopher Bell by 50 after Sunday's win at Kansas. Las Vegas is next, another mile-and-a-half, the same kind of track he just won on.</div>
''')
S('<div class="otd">','<h2 class="sec"><span class="o">&#10023;</span>Question','''<div class="otd"><b>September 29, 1954</b> &mdash; Willie Mays ran down Vic Wertz's drive to deep center at the Polo Grounds, over his shoulder with his back to the plate, in Game 1 of the World Series. "The Catch" is still the play every outfielder is measured against.</div>
''')
R('I have keys but open no locks, space but no room, and you can enter but not go in. What am I?','What can you catch but not throw?')
R('<b>Question of the Day:</b> A keyboard.','<b>Question of the Day:</b> A cold.')
R('scores via the league &middot; Dunkirk via the <i>Observer</i> &middot; Rochester via WXXI &middot; Erie County via WKBW','headlines via NPR, CBS, BBC, WIVB, Rochester First, WXXI, Variety, Deadline and Billboard')
d.update(date='2026-09-29',no=97,body_html=b,plate_path='/home/claude/plate97.jpg',plate_caption='Last light over Port Bay, Saturday evening',headline="Port Bay at dusk · 73, 74, 77 · Canada import ban · Goo Goo Dolls home for FeedMore")
json.dump(d,open('site/data/edition-2026-09-29.json','w'),indent=1); json.dump(d,open('edition-2026-09-29.json','w'),indent=1)
p=json.load(open('site/data/pressure.json'))
if p[-1]['date']!='2026-09-29': p.append({"date":"2026-09-29","in":30.02,"mb":1016.6,"station":"KIAG","time":"05:53 EDT"})
json.dump(p,open('site/data/pressure.json','w'),indent=1)
print('ok')
