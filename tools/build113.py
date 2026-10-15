import json
d=json.load(open('edition-2026-10-14.json')); b=d['body_html']
baro=open('/tmp/claude-0/-home-claude/001a10af-13f9-5479-8fec-28bf86d9c496/scratchpad/baro113.html').read(); baro=baro[:baro.index('<!--')].strip()+'\n'
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
R('No. 112','No. 113')
R('Wednesday &middot; October 14 &middot; 2026','Thursday &middot; October 15 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">61&deg;</div><div class="k">Rain tonight</div></div>
  <div class="tile"><div class="v">30.27&#8243; &#9660;</div><div class="k">Big drop tonight</div></div>
  <div class="tile urg"><div class="v">19</div><div class="k">Days to Election Day</div></div>
</div>
''')
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>Two days to the party.</b> Tonight's rain and Friday's wind clear out in time; Saturday looks mostly sunny and 48. Claire's birthday is a week from Friday.
''')
# drop yesterday's one-day Group Chat box
S('<h2 class="sec"><span class="o">&#9998;</span>From the Group Chat','<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass','')
S('<div class="wx">','<h2 class="sec"><span class="o">&#127810;</span>The Turning','''<div class="wx"><div class="bigtemp">61<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">The calm before a leaf-stripping wind</span>
Low <b>52&deg;</b> tonight, climbing to 63 by morning &middot; southeast gusts to 28<br>Rain after 11 p.m., 100 percent; a quiet, mostly cloudy day first</div></div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">52<sup>&deg;</sup></div><div class="d">Cloudy &middot; high 61&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">52<sup>&deg;</sup></div><div class="d">Cloudy &middot; high 65&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">50<sup>&deg;</sup></div><div class="d">Cloudy &middot; high 59&deg;</div></div>
</div>
<div class="strip5">
  <div><div class="d">Thu</div><div class="i">&#9729;</div><div class="h">61</div><div class="w">mostly cloudy, rain late</div></div>
  <div><div class="d">Fri</div><div class="i">&#127783;</div><div class="h">67</div><div class="w">rain, then windy</div></div>
  <div><div class="d">Sat</div><div class="i">&#127780;</div><div class="h">48</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Sun</div><div class="i">&#9728;</div><div class="h">60</div><div class="w">sunny</div></div>
  <div><div class="d">Mon</div><div class="i">&#9728;</div><div class="h">63</div><div class="w">sunny</div></div>
</div>
<div class="line"><span class="lbl r">The turn</span> Rain starts between 11 p.m. and 1 a.m., a quarter to half an inch overnight. Friday brings rain and a chance of thunder until 2 p.m., another half to three-quarters of an inch, then a west wind gusting to 39 as temperatures fall from the 60s. Saturday night Scottsville dips to 31. <span class="lbl t">Outdoor window</span> Today, then Sunday and Monday, sunny and in the 60s.</div>
''')
# The Turning: no new county numbers found this week; section skipped today
S('<h2 class="sec"><span class="o">&#127810;</span>The Turning','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','')
S('<div class="sky">','<div class="stars">','''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 0 50 96 A25 46 0 0 1 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>A waxing crescent</b>, 23 percent lit, in Sagittarius, sets at 9:12 p.m.<br>
<span class="lbl t">Sun</span> 7:29a &ndash; 6:33p &middot; <b>11h 4m</b><br>
<span class="lbl t">Hunter's Moon</span> Mon, Oct 26</div></div>
<div class="line"><span class="lbl r">Tonight</span> Clouds thicken ahead of the rain, so the crescent will be hard to catch before it sets at 9:12 in the southwest. Sunset comes at 6:33, the earliest yet this fall.</div>
''')
S('<div class="stars">','<div style="font-family','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>Mars trines Saturn in your sign, within half a degree</b>. Effort and patience pull the same way. Start the long job. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>Uranus trines Pluto</b>. An old routine makes room for a better one. Let it. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>The moon trines Jupiter in your sign</b>. Big-hearted and lucky in small ways. Say yes to the invitation. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>The Sun sextiles the moon</b>. Head and heart agree for once. Make the list and trust it. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Venus in your sign squares Pluto</b>. Feelings run deep; not every one needs saying out loud. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
S('<div class="baro-top">','<h2 class="sec"><span class="o">&#10038;</span>The Ledger',baro+'''<div class="line"><span class="lbl r">Big swing coming</span> 30.27 and near the top, up about a third of an inch since yesterday morning. Tonight's storm takes it down about seven-tenths of an inch by Friday morning, and it climbs nearly all the way back by Saturday morning.</div>
<div class="line"><span class="lbl t">The log</span> Days since the last one: Garret 9, Dad 9, Mom 6. October so far: one each.</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">Social Security raise for 2027</div><div class="big">3.6%</div></div>
<div class="txt">The 2027 cost-of-living increase is set at 3.6 percent, tied to inflation, a little more than $900 over the year. Groceries will want most of it back.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Pope Leo','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>Inflation Jumps to 3.7%</h3><p>September's consumer price report showed a 3.7 percent increase, higher than expected. Gas prices jumped 9.1 percent from August and made up more than half of the month's rise.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>School Roof Collapse in Pakistan</h3><p>The roof of a small private school in Peshawar collapsed Thursday, killing at least 28 children and a teacher. More than 50 other people were hurt.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Earhart Searchers Say They're Close</h3><p>American researchers believe they may be days away from finding what remains of Amelia Earhart's plane off a remote South Pacific island. She vanished in 1937.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>A New Cousin for T. Rex</h3><p>A fossil dug up in Britain 100 years ago has been identified as a previously unknown relative of T. rex. One researcher said it "definitely would have chased us."</p></div></div>
''')
S('<div class="ballot">','<h2 class="sec"><span class="o">&#9962;</span>The Home Wire','''<div class="ballot">&#9745; The Ballot &middot; <b>19 days</b> to Election Day &middot; early voting opens in 9 days, Oct 24, the same day registration closes &middot; every race we're watching: <a href="https://benthambulletin.github.io/election/">benthambulletin.github.io/election</a></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Orangutans','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Airport Ranks Again</h3><p>Frederick Douglass Greater Rochester International came in ninth among the country's small airports in USA Today's 10Best readers' poll. It is the fourth straight year on the list.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Sheridan &middot; Flea Market This Weekend</h3><p>The Lakeshore Flea Market is at the VFW post on Route 20 this Friday and Saturday. It usually runs the first full weekend of the month; October's moved because of a scheduling conflict.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>North Tonawanda &middot; The Community Center Case</h3><p>City officials say they have outgrown the small, outdated youth and senior centers and want one community center to replace them. Voters answer the $18 million borrowing question on the Nov. 3 ballot.</p></div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3><i>Girls</i>','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron','''<div class="wire"><div class="num">1</div><div><h3><i>The Lowdown</i> Is Back</h3><p>Ethan Hawke's FX series opened its second season with a new case for his character, Lee. Tommy Lee Jones and Betty Gilpin join the cast.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Alan Mandell Dies at 98</h3><p>The actor helped stage <i>Waiting for Godot</i> inside San Quentin State Prison in 1957, playing Lucky. Decades later he helped Keanu Reeves and Alex Winter with their recent Broadway revival of the play.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3><i>South Park</i> Takes On Looksmaxxing</h3><p>This week's episode sends Ike into an "aura battle," loses Stan in the backrooms of a Sephora and gives Randy a face-lift. Critics called it a peak-season episode.</p></div></div>
''')
S('<div class="touch-head">Sunday: Vegas and Foxborough</div>','<table class="tbl">','''<div class="touch-head">Rousseau Gets His Due</div>
<div class="line"><b>Bills</b> &middot; Greg Rousseau is the AFC's special teams player of the week for blocking the Rams' overtime field goal try Monday, the kick that would have won it for Los Angeles. Next: at Las Vegas Sunday, 4:25.</div>
<div class="line"><b>Jets</b> &middot; New England's secondary is banged up: cornerbacks Carlton Davis and Karon Prunty missed Wednesday's practice, and Christian Gonzalez was limited. The Jets visit Sunday at 1:00.</div>
<div class="pnote"><b>The Sunday Tax &middot; Week 6.</b> Tonight's the first lock: Seahawks at Denver, 8:15 p.m. Picks at <a href="https://tally.so/r/RGOakJ">tally.so/r/RGOakJ</a>; standings at <a href="https://benthambulletin.github.io/pool/">benthambulletin.github.io/pool</a>. $5 a week, straight-up winners, the pot to the best record, and anyone with the link can play. Every other sheet locks at its own kickoff.</div>
''')
S('<div class="touch-head">Phoenix Next</div>','<h2 class="sec"><span class="o">&#9790;</span>On This Day','''<div class="touch-head">Blaney's Track</div>
<div class="line">Ryan Blaney has won the last two Cup races at Phoenix, including this spring's, over Christopher Bell. He comes in off three straight top-five finishes, fifth in the standings with four races left. Sunday at 3 p.m. on USA.</div>
''')
S('<div class="otd">','<h2 class="sec"><span class="o">&#10023;</span>Question of the Day','''<div class="otd"><b>October 15, 1951</b> &mdash; <i>I Love Lucy</i> premiered on CBS, with Lucille Ball and Desi Arnaz as Lucy and Ricky Ricardo.</div>
''')
S('<div class="qotd">I wear a carved grin','<div class="dbl">','''<div class="qotd">The more of me you rake, the more the wind brings back. What am I? <i>Answer below the fold.</i></div>
''')
R("<b>Question of the Day:</b> A jack-o'-lantern.","<b>Question of the Day:</b> Fallen leaves.")
S('<div class="s">Forecast per NWS','<div class="sig">','''<div class="s">Forecast per NWS Buffalo &middot; barometer forecast via Open-Meteo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; sky computed for 14120 &middot; headlines via CBS, NPR, PBS, Rochester First, Dunkirk Observer, WKBW, WIVB, Hollywood Reporter, Variety &middot; Patriots injury report via Pats Pulpit and Yahoo Sports &middot; Phoenix notes via NASCAR.com &middot; scores, standings and NASCAR points via Sportradar</div>
''')
d['no']=113; d['date']='2026-10-15'
d['headline']="Inflation 3.7% · Social Security +3.6% · Rain and wind tonight · Rousseau honored"
d['body_html']=b; d['plate_path']=None; d['plate_caption']=None
json.dump(d,open('edition-2026-10-15.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-15.json','w'),ensure_ascii=False,indent=1)
p=json.load(open('site/data/pressure.json')); p=[x for x in p if x['date']!='2026-10-15']
p.append({'date':'2026-10-15','in':30.27,'mb':1025.2,'station':'KIAG','time':'06:53 EDT'}); json.dump(p,open('site/data/pressure.json','w'),indent=1)
m=json.load(open('site/data/migraines.json')); m['updated']='2026-10-15'; json.dump(m,open('site/data/migraines.json','w'),indent=1)
print('built')
