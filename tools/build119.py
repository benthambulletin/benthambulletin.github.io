import json
d=json.load(open('edition-2026-10-20.json')); b=d['body_html']
baro=open('/tmp/claude-0/-home-claude/001a10af-13f9-5479-8fec-28bf86d9c496/scratchpad/baro119.html').read(); baro=baro[:baro.index('<!--')].strip()+'\n'
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
R('No. 118','No. 119')
R('Tuesday &middot; October 20 &middot; 2026','Wednesday &middot; October 21 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">60&deg;</div><div class="k">Sunny</div></div>
  <div class="tile"><div class="v">30.37&#8243; &#9660;</div><div class="k">Dips this afternoon</div></div>
  <div class="tile urg"><div class="v">13</div><div class="k">Days to Election Day</div></div>
</div>
''')
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>Garret headed to Long Island yesterday.</b> Claire's birthday is Friday, Garret and Ariel share theirs on Sunday, and early voting opens Saturday.
''')
S('<div class="wx">','<h2 class="sec"><span class="o">&#127810;</span>The Turning','''<div class="wx"><div class="bigtemp">60<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">A frosty start, then another blue-sky afternoon</span>
Low <b>36&deg;</b> tonight &middot; light northeast wind<br>No rain in the forecast through Sunday</div></div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">34<sup>&deg;</sup></div><div class="d">Clear &middot; high 60&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">28<sup>&deg;</sup></div><div class="d">Clear &middot; high 58&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">32<sup>&deg;</sup></div><div class="d">Sunny today &middot; high 59&deg;</div></div>
</div>
<div class="strip5">
  <div><div class="d">Wed</div><div class="i">&#9728;</div><div class="h">60</div><div class="w">sunny</div></div>
  <div><div class="d">Thu</div><div class="i">&#9728;</div><div class="h">60</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Fri</div><div class="i">&#9728;</div><div class="h">56</div><div class="w">sunny</div></div>
  <div><div class="d">Sat</div><div class="i">&#9728;</div><div class="h">62</div><div class="w">sunny</div></div>
  <div><div class="d">Sun</div><div class="i">&#9728;</div><div class="h">64</div><div class="w">sunny</div></div>
</div>
<div class="line"><span class="lbl r">Frost</span> Friday night is the coldest of the week: 32 in North Tonawanda and 29 in Scottsville, on Claire's birthday. <span class="lbl t">Outdoor window</span> Every day through Sunday, the warmest day of the stretch at 64.</div>
''')
S('<div class="line"><b>Report day is tomorrow.</b>','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','''<div class="line"><b>Report day is today.</b> The state's spotters file this afternoon, and their numbers run here tomorrow. Last week Niagara Falls was at 50 percent color and Chautauqua Institution at 70.</div>
''')
S('<div class="sky">','<div class="stars">','''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 0 50 96 A26 46 0 0 0 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>A waxing gibbous</b>, 78 percent lit, in Pisces, rises at 4:14 p.m. and sets at 3:31 a.m.<br>
<span class="lbl t">Sun</span> 7:36a &ndash; 6:23p &middot; <b>10h 47m</b><br>
<span class="lbl t">Hunter's Moon</span> Mon, Oct 26 &middot; <span class="lbl t">New moon</span> Mon, Nov 9</div></div>
<div class="line"><span class="lbl r">Tonight</span> Clear and cold again. At 8 p.m. the moon is a third of the way up the south-southeast sky, five nights from full.</div>
''')
S('<div class="stars">','<div style="font-family','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>Neptune in your sign sextiles Pluto</b>. A dream from long ago comes back into focus. Give it a look. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>The moon trines the sun</b>. An easy, even day. Let it be easy. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Mercury squares Jupiter in your sign</b>. Big talk comes easily. Check the facts before you repeat them. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>The moon squares Uranus</b>. Plans shift without warning. Roll with it. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>The moon trines Venus in your sign</b>. Kindness comes back around. Birthday week starts on a sweet note. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
S('<div class="baro-top">','<h2 class="sec"><span class="o">&#10038;</span>The Ledger',baro+'''<div class="line"><span class="lbl r">Big swing coming</span> 30.37 and steady at dawn. It drops about a tenth of an inch by evening, most of it between noon and 3, then climbs back Thursday night into Friday.</div>
<div class="line"><span class="lbl t">The log</span> Days since the last one: Garret 15, Dad 15, Mom 12. October so far: one each.</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">Buffalo police overtime, last fiscal year</div><div class="big">$17M</div></div>
<div class="txt">Buffalo police overtime is up more than a third in five years and cost taxpayers $17 million last fiscal year, WKBW reports.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Update: Alberta Stays','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>Russia Frees an American Teacher</h3><p>Stephen Hubbard, a former teacher jailed in Russia since 2022, has been released, U.S. envoy Steve Witkoff says. President Trump says he is on his way home and that no prisoner swap was required.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Tesla and SpaceX, One Company?</h3><p>Elon Musk confirmed he is considering merging Tesla and SpaceX, and both companies have formed special committees to look at it. It would be the biggest merger in history.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>A Shark in the Canal</h3><p>Huge crowds in South Korea watched rescuers try for a third time to guide a stranded shark, nearly 10 feet long, from a canal back to the open sea, the BBC reports.</p></div></div>
''')
S('<div class="ballot">','<h2 class="sec"><span class="o">&#9962;</span>The Home Wire','''<div class="ballot">&#9745; The Ballot &middot; <b>13 days</b> to Election Day &middot; early voting opens Saturday, Oct 24, and runs through Nov 1 &middot; Democrats favored for the House; the Senate close, tilting Democratic &middot; every race: <a href="https://benthambulletin.github.io/election/">benthambulletin.github.io/election</a></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>North Tonawanda &middot; Gas at Walmart?','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; $20 Million to Take Down the Terrence Building</h3><p>Rochester City Council voted unanimously Tuesday night to accept state funding to demolish the Terrence Building, Rochester First reports. The council approved $20 million toward the job.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Fredonia &middot; Sweep of Dunkirk</h3><p>Fredonia swept Dunkirk 25&ndash;20, 25&ndash;8, 25&ndash;19 in volleyball Tuesday. Londyn Wilmot, Maddie Krakowiak, Jordan Morris and Elly Saunders combined for 33 kills.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Dunkirk &middot; Tennis Club Open House</h3><p>The Chautauqua Tennis Club holds an open house Saturday from 1 to 3 p.m. at Floral Hall at the Chautauqua County Fairgrounds, the <i>Observer</i> reports.</p></div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3><i>Street Fighter</i>','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron','''<div class="wire"><div class="num">1</div><div><h3>Ozzy, "Flying High" to the End</h3><p>Sharon Osbourne says Ozzy's final "Back to the Beginning" concert kept him "flying high" until the day he died. She spoke at a London screening of the concert film <i>Ozzy &amp; Black Sabbath: Back to the Beginning</i>.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Sam Fender Goes Big</h3><p>Sam Fender will play a 2027 stadium tour of the U.K. and Ireland, including nights at Wembley, Billboard reports. Wunderhorse will open the U.K. shows.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>An Honor for John Leguizamo</h3><p>Leguizamo, a star of Christopher Nolan's <i>The Odyssey</i>, will be honored at the São Paulo International Film Festival in Brazil. The festival's 50th edition runs through Oct. 29.</p></div></div>
''')
S('<div class="touch-head">Bye Week</div>','<div class="pnote">','''<div class="touch-head">Four Days to Sunday</div>
<div class="line"><b>Bills</b> &middot; Off this week at 5&ndash;1. Baltimore visits Nov. 1 at 1:00.</div>
<div class="line"><b>Jets</b> &middot; Miami, 0&ndash;5, comes to MetLife Sunday at 1:00. Sportradar gives the Jets a 68 percent chance to win.</div>
''')
R("Week 6 went to Ryan Holovics, who takes the $95 pot for the second week running. ","")
R('<div class="line"><b>Around the league.</b> San Francisco beat Washington 23&ndash;17 Monday night. Eagles quarterback Jalen Hurts is expected to miss the rest of the season with blood clots in his lungs, the AP reports.</div>','<div class="line"><b>Around the league.</b> The Eagles will not be disciplined over how they handled Jalen Hurts&rsquo;s blood clots, a source told the AP. Thursday night opens Week 7: New England at Chicago, 8:15.</div>')
S('<div class="touch-head">Talladega Sunday</div>','<h2 class="sec"><span class="o">&#9790;</span>On This Day','''<div class="touch-head">Talladega Sunday</div>
<div class="line">Larson leads Bell by 5 with three races left; the big Alabama track can scramble any lead.</div>
''')
S('<div class="otd">','<h2 class="sec"><span class="o">&#10023;</span>Question of the Day','''<div class="otd"><b>October 21, 1879</b> &mdash; Thomas Edison tested a light bulb with a carbonized cotton-thread filament in his Menlo Park lab; it glowed for about 13 hours.</div>
''')
S('<div class="qotd">I fly without wings','<div class="dbl">','''<div class="qotd">What has one eye but can't see a thing? <i>Answer below the fold.</i></div>
''')
R("<b>Question of the Day:</b> A cloud.","<b>Question of the Day:</b> A needle.")
S('<div class="s">Forecast per NWS','<div class="sig">','''<div class="s">Forecast per NWS Buffalo &middot; barometer forecast via Open-Meteo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; sky computed for 14120 &middot; election summary from the paper's election tracker &middot; headlines via CBS, BBC, NPR, AP, WKBW, Rochester First, Dunkirk Observer, Variety, Billboard, Deadline &middot; scores, standings, odds and NASCAR points via Sportradar</div>
''')
d['no']=119; d['date']='2026-10-21'
d['headline']="Frosty start, sunny week · Russia frees Stephen Hubbard · Jets host Miami Sunday"
d['body_html']=b; d['plate_path']=None; d['plate_caption']=None
json.dump(d,open('edition-2026-10-21.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-21.json','w'),ensure_ascii=False,indent=1)
p=json.load(open('site/data/pressure.json')); p=[x for x in p if x['date']!='2026-10-21']
p.append({'date':'2026-10-21','in':30.37,'mb':1028.5,'station':'KIAG','time':'06:53 EDT'}); json.dump(p,open('site/data/pressure.json','w'),indent=1)
m=json.load(open('site/data/migraines.json')); m['updated']='2026-10-21'; json.dump(m,open('site/data/migraines.json','w'),indent=1)
print('built')
