import json
d=json.load(open('edition-2026-10-19.json')); b=d['body_html']
baro=open('/tmp/claude-0/-home-claude/001a10af-13f9-5479-8fec-28bf86d9c496/scratchpad/baro118.html').read(); baro=baro[:baro.index('<!--')].strip()+'\n'
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
R('No. 117','No. 118')
R('Monday &middot; October 19 &middot; 2026','Tuesday &middot; October 20 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">63&deg;</div><div class="k">Mostly sunny</div></div>
  <div class="tile"><div class="v">30.41&#8243; &#9650;</div><div class="k">Slides Wednesday</div></div>
  <div class="tile urg"><div class="v">14</div><div class="k">Days to Election Day</div></div>
</div>
''')
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>Birthday week.</b> Claire's birthday is Friday, and Garret and Ariel share theirs on Sunday. Early voting opens Saturday.
''')
S('<div class="wx">','<h2 class="sec"><span class="o">&#127810;</span>The Turning','''<div class="wx"><div class="bigtemp">63<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">Another sunny day, and the first frost of the week tonight</span>
Low <b>33&deg;</b> tonight, with patchy frost after 4 a.m. &middot; light northeast wind today<br>Dry and sunny through Saturday</div></div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">39<sup>&deg;</sup></div><div class="d">Clear &middot; high 63&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">36<sup>&deg;</sup></div><div class="d">Partly cloudy &middot; high 63&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">39<sup>&deg;</sup></div><div class="d">Clear &middot; high 61&deg;</div></div>
</div>
<div class="strip5">
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">63</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#9728;</div><div class="h">62</div><div class="w">sunny</div></div>
  <div><div class="d">Thu</div><div class="i">&#9728;</div><div class="h">62</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Fri</div><div class="i">&#9728;</div><div class="h">57</div><div class="w">sunny</div></div>
  <div><div class="d">Sat</div><div class="i">&#9728;</div><div class="h">60</div><div class="w">sunny</div></div>
</div>
<div class="line"><span class="lbl r">Frost</span> North Tonawanda and Scottsville both drop to 33 tonight; bring in tender plants. Scottsville is back to 33 Friday night, Claire's birthday. <span class="lbl t">Outdoor window</span> Every day through Saturday.</div>
''')
S('<div class="line"><b>Report day is Wednesday.</b>','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','''<div class="line"><b>New numbers tomorrow.</b> Last week's report, still the latest, had Niagara Falls at 50 percent color, Chautauqua Institution at 70 and Greece, in Monroe County, at 30. The new report runs here Thursday; North Tonawanda usually peaks the last week of October.</div>
''')
S('<div class="sky">','<div class="stars">','''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 0 50 96 A18 46 0 0 0 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>A waxing gibbous</b>, 69 percent lit, in Aquarius, rises at 3:52 p.m. and sets at 2:23 a.m.<br>
<span class="lbl t">Sun</span> 7:34a &ndash; 6:24p &middot; <b>10h 50m</b><br>
<span class="lbl t">Hunter's Moon</span> Mon, Oct 26 &middot; <span class="lbl t">New moon</span> Mon, Nov 9</div></div>
<div class="line"><span class="lbl r">Tonight</span> Clear and cold. At 8 p.m. the moon is a third of the way up the south-southeast sky, with Saturn lower in the east-southeast.</div>
''')
S('<div class="stars">','<div style="font-family','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>Mars trines Saturn in your sign</b>. Slow, steady work gets the job done. Finish what you started. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>Uranus sextiles Neptune</b>. A new idea arrives quietly. Write it down. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>The moon opposes Jupiter in your sign</b>. Big feelings, big plans. Go easy on promises today. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>The moon squares Mercury</b>. Words come out sideways. Read the text twice before you send it. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Venus in your sign squares Pluto</b>. A tender subject runs deep. Give it a day before you settle it. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
S('<div class="baro-top">','<h2 class="sec"><span class="o">&#10038;</span>The Ledger',baro+'''<div class="line"><span class="lbl r">Big swing coming</span> 30.41 and rising this morning. It holds steady through tonight, then slides about a sixth of an inch from late tonight to late Wednesday, the fastest part between noon and 3.</div>
<div class="line"><span class="lbl t">The log</span> Days since the last one: Garret 14, Dad 14, Mom 11. October so far: one each.</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">Ryan Holovics's Sunday Tax winnings</div><div class="big">$190</div></div>
<div class="txt">Ryan Holovics took Week 6 on the tiebreaker, his second straight $95 pot. Nobody else has won two.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Update: Four Dead','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>Alberta Stays</h3><p>Voters in Alberta overwhelmingly backed remaining in Canada, early results show, a boost for Prime Minister Mark Carney, who called it "a clear choice" for national unity. The vote was not on independence itself, but a yes would have started a process toward possible separation.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>TikTok Warnings Went Unheeded</h3><p>TikTok staff raised alarms about child safety, and court records show executives failed to act, NPR reports. The warnings surfaced in a trove of court records not reported before.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Flamingo Thief Convicted</h3><p>A Canadian tourist was found guilty of animal cruelty for stealing Peachy, a flamingo, from its enclosure at the Flamingo hotel and casino in Las Vegas. He testified he had drunk 30 to 40 beers and meant no harm.</p></div></div>
''')
S('<div class="ballot">','<h2 class="sec"><span class="o">&#9962;</span>The Home Wire','''<div class="ballot">&#9745; The Ballot &middot; <b>14 days</b> to Election Day &middot; early voting opens Saturday, Oct 24, and runs through Nov 1 &middot; Democrats favored for the House; the Senate close, tilting Democratic &middot; every race: <a href="https://benthambulletin.github.io/election/">benthambulletin.github.io/election</a></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Downtown Housing','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<div class="wire"><div class="num">1</div><div><h3>Niagara Falls &middot; A Look Before Goodyear Leaves</h3><p>Goodyear is closing its chemical plant in Niagara Falls, and Niagara County lawmakers plan to back environmental activists who want the state to take a close look at the plant's operation. The <i>Niagara Gazette</i> reports they want that review before the plant closes and after.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Pomfret &middot; Against the Cameras</h3><p>The Pomfret town board is weighing a resolution against Flock Safety cameras, the <i>Observer</i> reports. Board member Mike Lee, running for the Chautauqua County Legislature, has made the cameras a central issue, arguing they are too intrusive and their data can be misused.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Sinclairville &middot; A School's Own Forest</h3><p>Cassadaga Valley Central School has finished a research forest with Cornell University, the only one at a New York State school. Cornell representatives will lead a tour later this month.</p></div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Apu Speaks','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron','''<div class="wire"><div class="num">1</div><div><h3><i>Street Fighter</i> Wins in Britain</h3><p>Paramount's <i>Street Fighter</i> opened at No. 1 at the U.K. and Ireland box office with &pound;2.3 million, about $3.1 million, Variety reports. Universal's animated <i>Forgotten Island</i> was second with $1.8 million.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Dana Carvey Shrugs</h3><p>The <i>SNL</i> alum says he "didn't understand the kerfuffle" over Shane Gillis's Oct. 10 monologue mocking women at the gym. Carvey said he "just saw it" as "a joke."</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>New Boss for Disney in Asia</h3><p>Carol Choi becomes president of The Walt Disney Company Asia Pacific on Dec. 1, replacing Luke Kang, who is stepping down after 16 years. A 20-year Disney veteran, she will oversee studios, streaming and consumer products across the region.</p></div></div>
''')
S('<div class="touch-head">Monday Morning Quarterback</div>','<h2 class="sec"><span class="o">&#9873;</span>The Chase','''<div class="touch-head">Bye Week</div>
<div class="line"><b>Bills</b> &middot; A week off at 5&ndash;1, first in the AFC East, and a chance to heal before Baltimore comes to Orchard Park on Nov. 1. The Ravens lost in Cleveland on Sunday and are 4&ndash;2.</div>
<div class="line"><b>Jets</b> &middot; Home Sunday at 1:00 against Miami, still looking for its first win. The Jets are 2&ndash;4; a win would be their third.</div>
<div class="pnote"><b>The Sunday Tax &middot; Week 7.</b> Week 6 went to Ryan Holovics, who takes the $95 pot for the second week running. Picks at <a href="https://tally.so/r/RGOakJ">tally.so/r/RGOakJ</a>; standings at <a href="https://benthambulletin.github.io/pool/">benthambulletin.github.io/pool</a>. $5 a week, straight-up winners, the pot to the best record. Anyone with the link can play. Sheets lock at each kickoff; first game Thu 8:15 p.m., Patriots at Chicago.</div>
<table class="tbl"><tr><th>AFC East</th><th class="n">W</th><th class="n">L</th><th class="n">PCT</th></tr>
<tr><td style="color:var(--red)">Buffalo</td><td class="n">5</td><td class="n">1</td><td class="n">.833</td></tr>
<tr><td>New England</td><td class="n">4</td><td class="n">2</td><td class="n">.667</td></tr>
<tr><td style="color:var(--red)">N.Y. Jets</td><td class="n">2</td><td class="n">4</td><td class="n">.333</td></tr>
<tr><td>Miami</td><td class="n">0</td><td class="n">5</td><td class="n">.000</td></tr></table>
<div class="line"><b>Around the league.</b> San Francisco beat Washington 23&ndash;17 Monday night. Eagles quarterback Jalen Hurts is expected to miss the rest of the season with blood clots in his lungs, the AP reports.</div>
''')
S('<div class="touch-head">Reddick Wins Phoenix</div>','<h2 class="sec"><span class="o">&#9790;</span>On This Day','''<div class="touch-head">Talladega Sunday</div>
<div class="line">Three races left in the Cup Series. Kyle Larson leads Christopher Bell by 5 points, with Chase Briscoe 24 back, Denny Hamlin 31 and Ryan Blaney 40. Talladega is Sunday, then Martinsville and Homestead.</div>
''')
S('<div class="otd">','<h2 class="sec"><span class="o">&#10023;</span>Question of the Day','''<div class="otd"><b>October 20, 1803</b> &mdash; The U.S. Senate ratified the Louisiana Purchase, buying some 828,000 square miles from France and roughly doubling the size of the country.</div>
''')
S('<div class="qotd">I have a neck','<div class="dbl">','''<div class="qotd">I fly without wings and cry without eyes. What am I? <i>Answer below the fold.</i></div>
''')
R("<b>Question of the Day:</b> A sweater.","<b>Question of the Day:</b> A cloud.")
S('<div class="s">Forecast per NWS','<div class="sig">','''<div class="s">Forecast per NWS Buffalo &middot; barometer forecast via Open-Meteo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; sky computed for 14120 &middot; election summary from the paper's election tracker &middot; headlines via CBS, BBC, NPR, AP, Niagara Gazette, Dunkirk Observer, Spectrum News, Variety, Hollywood Reporter &middot; scores, standings and NASCAR points via Sportradar</div>
''')
d['no']=118; d['date']='2026-10-20'
d['headline']="Bills on bye · Frost tonight · Ryan Holovics, twice · Alberta stays"
d['body_html']=b; d['plate_path']=None; d['plate_caption']=None
json.dump(d,open('edition-2026-10-20.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-20.json','w'),ensure_ascii=False,indent=1)
p=json.load(open('site/data/pressure.json')); p=[x for x in p if x['date']!='2026-10-20']
p.append({'date':'2026-10-20','in':30.41,'mb':1029.8,'station':'KIAG','time':'06:53 EDT'}); json.dump(p,open('site/data/pressure.json','w'),indent=1)
m=json.load(open('site/data/migraines.json')); m['updated']='2026-10-20'; json.dump(m,open('site/data/migraines.json','w'),indent=1)
print('built')
# --- review fixes ---
d=json.load(open('edition-2026-10-20.json')); b=d['body_html']
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">Volunteer firefighter tax credit</div><div class="big">$800</div></div>
<div class="txt">New York's volunteer firefighters and EMS workers get $800 off their state income taxes starting next tax year, up from $200. It is the first raise since the credit began in 2006.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Niagara Falls &middot;','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<div class="wire"><div class="num">1</div><div><h3>North Tonawanda &middot; Gas at Walmart?</h3><p>Walmart's North Tonawanda superstore is looking to add its own gas station and convenience store. Few other Walmart locations in the state have one, the <i>Niagara Gazette</i> reports.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Rochester &middot; Planetarium Gets $1.7 Million</h3><p>State Sen. Samra Brouk and Assemblymember Harry Bronson secured $1.7 million for upgrades at the RMSC Strasenburgh Planetarium, Rochester First reports. Money from community donors helped it reach its $2.11 million goal.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Niagara Falls &middot; A Look Before Goodyear Leaves</h3><p>Goodyear is closing its chemical plant in Niagara Falls, and Niagara County lawmakers plan to back environmental activists who want the state to take a close look at the plant's operation. The <i>Niagara Gazette</i> reports they want that review done before the plant closes.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>Pomfret &middot; Against the Cameras</h3><p>The Pomfret town board is weighing a resolution against Flock Safety cameras, the <i>Observer</i> reports. Board member Mike Lee, running for the Chautauqua County Legislature, has made the cameras a central issue, arguing they are too intrusive and their data can be misused.</p></div></div>
''')
R('<div class="line"><b>Jets</b> &middot; Home Sunday at 1:00 against Miami, still looking for its first win. The Jets are 2&ndash;4; a win would be their third.</div>','<div class="line"><b>Jets</b> &middot; Home Sunday at 1:00 against Miami, which is 0&ndash;5. A win would put the Jets at 3&ndash;4 heading into November.</div>')
R("and a chance to heal before Baltimore comes to Orchard Park on Nov. 1. The Ravens lost in Cleveland on Sunday and are 4&ndash;2.","with a chance to heal. Safety C.J. Gardner-Johnson was suspended one game without pay for spitting toward a Raiders player, WIVB reports. Baltimore, 4&ndash;2, visits Nov. 1 at 1:00.")
R('<b>New numbers tomorrow.</b>','<b>Report day is tomorrow.</b>')
R('Another sunny day, and the first frost of the week tonight','Sweater-weather sun again, and frost on the windshields by morning')
R('30.41&#8243; &#9650;','30.41&#8243; &#9660;')
S('<div class="touch-head">Talladega Sunday</div>','<h2 class="sec"><span class="o">&#9790;</span>On This Day','''<div class="touch-head">Talladega Sunday</div>
<div class="line">Three races left; Larson leads Bell by 5 going to the big track in Alabama.</div>
''')
R('<h3>Alberta Stays</h3>','<h3>Update: Alberta Stays</h3>')
R('The warnings surfaced in a trove of court records not reported before.',"“I have been fighting about fixing this for months with people who didn't think the harms are severe enough,” one staffer wrote.")
R('''<p>The <i>SNL</i> alum says he "didn't understand the kerfuffle" over Shane Gillis's Oct. 10 monologue mocking women at the gym. Carvey said he "just saw it" as "a joke."</p>''','''<p>Comedian Shane Gillis drew outrage opening his Oct. 10 <i>SNL</i> hosting stint by mocking women at the gym. <i>SNL</i> alum Dana Carvey says he "didn't understand the kerfuffle" and "just saw it" as "a joke."</p>''')
R('with Saturn lower in the east-southeast.</div>','with Saturn lower in the east-southeast. Sunset is 6:24, two minutes earlier than yesterday.</div>')
R('headlines via CBS, BBC, NPR, AP, Niagara Gazette, Dunkirk Observer, Spectrum News,','headlines via CBS, BBC, NPR, AP, WIVB, Rochester First, Niagara Gazette, Dunkirk Observer, Spectrum News,')
d['body_html']=b
json.dump(d,open('edition-2026-10-20.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-20.json','w'),ensure_ascii=False,indent=1)
print('fixed')
