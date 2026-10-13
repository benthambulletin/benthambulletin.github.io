import json
d=json.load(open('edition-2026-10-12.json')); b=d['body_html']
baro=open('/tmp/claude-0/-home-claude/001a10af-13f9-5479-8fec-28bf86d9c496/scratchpad/baro111.html').read(); baro=baro[:baro.index('<!--')].strip()+'\n'
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
R('No. 110','No. 111')
R('Monday &middot; October 12 &middot; 2026','Tuesday &middot; October 13 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">75&deg;</div><div class="k">Storms, then sun</div></div>
  <div class="tile"><div class="v">29.80&#8243; &#9650;</div><div class="k">Big climb coming</div></div>
  <div class="tile urg"><div class="v">21</div><div class="k">Days to Election Day</div></div>
</div>
''')
S('<div class="plate-wrap">','<h2 class="sec"><span class="o">&#9825;</span>Family Today','')
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>Both teams won.</b> The Jets on Sunday, the Bills in overtime last night in Los Angeles. One last warm, summery day before October remembers itself: showers this morning, sun this afternoon, then a raw weekend with Saturday stuck in the 40s. The family birthday party is Saturday.
''')
R('<li><span class="dt">Tonight</span><span>Bills at Rams &mdash; 8:15, ABC</span></li>\n','')
S('<div class="wx">','<div class="towns">','''<div class="wx"><div class="bigtemp">75<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">Summer's last word, in a southwest wind</span>
Low <b>58&deg;</b> tonight &middot; southwest 10&ndash;18, gusts to 33<br>Showers and storms likely before noon, 60 percent</div></div>
''')
S('<div class="towns">','<div class="strip5">','''<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">64<sup>&deg;</sup></div><div class="d">Cloudy &middot; high 75&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">66<sup>&deg;</sup></div><div class="d">Mostly cloudy &middot; high 77&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">63<sup>&deg;</sup></div><div class="d">Light rain &middot; high 79&deg;</div></div>
</div>
''')
S('<div class="strip5">','<h2 class="sec"><span class="o">&#127810;</span>The Turning','''<div class="strip5">
  <div><div class="d">Tue</div><div class="i">&#9928;</div><div class="h">75</div><div class="w">storms a.m., then sun</div></div>
  <div><div class="d">Wed</div><div class="i">&#9729;</div><div class="h">66</div><div class="w">mostly cloudy</div></div>
  <div><div class="d">Thu</div><div class="i">&#9925;</div><div class="h">60</div><div class="w">partly sunny</div></div>
  <div><div class="d">Fri</div><div class="i">&#127783;</div><div class="h">60</div><div class="w">rain, storms, windy</div></div>
  <div><div class="d">Sat</div><div class="i">&#9925;</div><div class="h">49</div><div class="w">chilly, partly sunny</div></div>
</div>
<div class="line"><span class="lbl r">The turn</span> Rain Thursday night into Friday with gusts to 36, then Friday night drops to 35 and Saturday tops out at 49. <span class="lbl t">Outdoor window</span> This afternoon and Wednesday.</div>
''')
S('<div class="line"><b>Two days to new numbers.</b>','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','''<div class="line"><b>New county numbers tomorrow.</b> The state foliage report comes out Wednesday afternoon; Monroe County was past 30 percent last week.</div>
''')
R('<b>A thin crescent</b>, 4 percent lit, in Scorpio, sets at 7:13 p.m.<br>','<b>A growing crescent</b>, 9 percent lit, in Scorpio, sets at 7:45 p.m.<br>')
R('7:25a &ndash; 6:37p &middot; <b>11h 12m</b>','7:26a &ndash; 6:36p &middot; <b>11h 10m</b>')
S('<div class="line"><span class="lbl r">Tonight</span> If the clouds break','<div class="stars">','''<div class="line"><span class="lbl r">Tonight</span> Skies clear after the morning storms: look west-southwest after sunset for the crescent moon, setting at 7:45. Daylight is down to 11 hours 10 minutes.</div>
''')
S('<div class="stars">','<div style="font-family','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>Mars trines Saturn in your sign, closer today</b>. Finish the hard thing; it will stick. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>Neptune sextiles Pluto, nearly exact</b>. A long-running worry quietly loosens its grip. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>The moon squares Jupiter in your sign</b>. A generous mood. Mind the wallet. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>The Sun sextiles Jupiter</b>. The luck is modest but real. Take the small win. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>The moon leaves your sign tonight</b>. Say what needed saying today. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
S('<div class="baro-top">','<h2 class="sec"><span class="o">&#10038;</span>The Ledger',baro+'''<div class="line"><span class="lbl r">Big swing coming</span> 29.80 and settling after last night's storms. The forecast has it climbing about four-tenths of an inch between tonight and Wednesday evening as the cold air arrives.</div>
<div class="line"><span class="lbl t">The log</span> Days since the last one: Garret 7, Dad 7, Mom 4. October so far: one each.</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">Independents running for Congress</div><div class="big">~200</div></div>
<div class="txt">Nearly 200 independent candidates are running in more than 100 House races this fall, NPR counts, trying to prove there's room outside the two parties. Their odds of winning are very low.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Economics Nobel','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>Agents Search Rep. Ilhan Omar's Home</h3><p>Homeland Security agents searched the Minnesota Democrat's Washington home Monday; sources tell CBS the long-running probe concerns immigration paperwork her late father filled out when she was a child. Omar, a U.S. citizen, called it an attempt to target political enemies.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Deadly Roller Coaster Accident in Georgia</h3><p>One rider died and several were hurt Monday on a coaster at Six Flags Over Georgia. Riders were helped off a stuck train.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Houthis Warn the U.S.</h3><p>The Iran-backed group in Yemen is threatening a "painful" response if the U.S. joins Saudi Arabia's fight against it. President Trump is weighing strikes after deadly Houthi attacks on Saudi airports.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>Ship Sunk in Black Sea Drone Attack</h3><p>Eleven crew members are missing after a merchant ship sank overnight. Bulgaria's prime minister summoned Russia's ambassador.</p></div></div>
''')
R("four Republican and two Democratic senators told Trump Sunday to reverse his Russian diesel deal","early voting opens in 11 days, Oct 24, the same day registration closes")
R("<b>22 days</b> to Election Day","<b>21 days</b> to Election Day")
S('<h2 class="sec"><span class="o">&#9962;</span>The Home Wire<span class="o">&#9962;</span></h2>','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<h2 class="sec"><span class="o">&#9962;</span>The Home Wire<span class="o">&#9962;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Wegmans Closing Amore</h3><p>Wegmans will close its Amore restaurant on East Avenue by the end of the month. The company said no amount of marketing or investment would have brought in enough customers.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Pomfret &middot; Another Battery Storage Plan</h3><p>RWE Clean Energy wants to build a battery energy storage system near the electric substation in Laona. Company representatives introduced the proposal at a Pomfret Town Board meeting.</p></div></div>
''')
S('<h2 class="sec"><span class="o">&#9733;</span>The Marquee<span class="o">&#9733;</span></h2>','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron','''<h2 class="sec"><span class="o">&#9733;</span>The Marquee<span class="o">&#9733;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>RJ Mitte Dies at 34</h3><p>He played Walter White Jr. on <i>Breaking Bad</i>, the Emmy-winning drama. Mitte lived with cerebral palsy, as his character did.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3><i>High Potential</i> Gets the Super Bowl Slot</h3><p>The drama gets the coveted slot right after the Super Bowl, on ABC and Disney+. It was already the network's most-watched series.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3><i>It's a Wonderful Life</i> at 80</h3><p>An 80th-anniversary box set brings a 4K remaster and keepsakes for the 1946 film. An early start on the holiday shelf.</p></div></div>
''')
S('<div class="touch-head">Monday Morning Quarterback</div>','<h2 class="sec"><span class="o">&#9873;</span>The Chase','''<div class="touch-head">Bills 37, Rams 34 (OT)</div>
<div class="line"><b>How it went.</b> A shootout in Los Angeles. Josh Allen ran for one touchdown, threw for another to Keon Coleman and finished with 331 total yards; James Cook scored twice on the ground, the second a 5-yard run that put Buffalo up 34&ndash;27 with 1:44 left. The Rams tied it on a 1-yard Kyren Williams run with eight seconds to go. In overtime the Bills fumbled deep in Rams territory, but Greg Rousseau blocked a Rams field goal, and Tyler Bass hit from 45 with 1:55 left to win it.</div>
<div class="line"><b>Got right:</b> 234 rushing yards, and Bass made all three of his field goals. <b>To fix:</b> 13 penalties for 112 yards, and a defense that let Matthew Stafford complete 40 of 54 passes and the Rams hold the ball for nearly 38 minutes. Buffalo is 4&ndash;1. At Las Vegas Sunday, 4:25.</div>
<div class="line"><b>Jets</b> &middot; Riding Sunday's win into Foxborough. New England, 3&ndash;2, is coming off a 45&ndash;17 rout of Las Vegas. Sunday, 1:00.</div>
<div class="pnote"><b>The Sunday Tax &middot; Week 6.</b> Week 5 went to Ryan Holovics, who takes the $95 pot. Picks at <a href="https://tally.so/r/RGOakJ">tally.so/r/RGOakJ</a>; standings at <a href="https://benthambulletin.github.io/pool/">benthambulletin.github.io/pool</a>. $5 a week, straight-up winners, the pot to the best record. Anyone with the link can play. Sheets lock at each kickoff; first game Thu 8:15 p.m., Seahawks at Denver.</div>
<table class="tbl"><tr><th>AFC East</th><th class="n">W</th><th class="n">L</th><th class="n">PCT</th></tr>
<tr><td style="color:var(--red)">Buffalo</td><td class="n">4</td><td class="n">1</td><td class="n">.800</td></tr>
<tr><td>New England</td><td class="n">3</td><td class="n">2</td><td class="n">.600</td></tr>
<tr><td style="color:var(--red)">N.Y. Jets</td><td class="n">2</td><td class="n">3</td><td class="n">.400</td></tr>
<tr><td>Miami</td><td class="n">0</td><td class="n">5</td><td class="n">.000</td></tr></table>
''')
S('<div class="touch-head">Briscoe Takes Charlotte</div>','<h2 class="sec"><span class="o">&#9790;</span>On This Day','''<div class="touch-head">Four to Go</div>
<div class="line">Behind Larson, Hamlin, Bell and Briscoe, Ryan Blaney is fifth, 85 back, and Joey Logano sixth, 92 back. Tyler Reddick, with a season-best five wins, sits seventh, 114 back.</div>
''')
S('<div class="otd">','<h2 class="sec"><span class="o">&#10023;</span>Question of the Day','''<div class="otd"><b>October 13, 1792</b> &mdash; Workers laid the cornerstone of the White House, then called the President's House. John Adams became its first resident in 1800.</div>
''')
S('<div class="qotd">','<div class="dbl">','''<div class="qotd">I have plenty of paths but lead nowhere, and every fall families pay to get lost in me. What am I? <i>Answer below the fold.</i></div>
''')
R("<b>Question of the Day:</b> A clock. Daylight saving time ends Nov. 1.","<b>Question of the Day:</b> A corn maze.")
R('headlines via CBS, NPR, BBC, PBS, WIVB, Dunkirk Observer, Niagara Gazette, Variety, Deadline, Hollywood Reporter, Billboard','headlines via CBS, NPR, BBC, PBS, WIVB, Dunkirk Observer, Rochester First, Hollywood Reporter')
d['no']=111; d['date']='2026-10-13'; d['headline']='Bills win in OT · Summer\'s last warm day · Chilly weekend ahead · Week 6 Sunday Tax'
d['body_html']=b; d['plate_path']=None; d['plate_caption']=None
json.dump(d,open('edition-2026-10-13.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-13.json','w'),ensure_ascii=False,indent=1)
p=json.load(open('site/data/pressure.json')); p=[x for x in p if x['date']!='2026-10-13']
p.append({'date':'2026-10-13','in':29.80,'mb':1009.3,'station':'KIAG','time':'06:53 EDT'}); json.dump(p,open('site/data/pressure.json','w'),indent=1)
print('ok')
# --- review fixes ---
d=json.load(open('edition-2026-10-13.json')); b=d['body_html']
R("29.80 and settling after last night's storms.","29.80 and slipping, down about a tenth of an inch since yesterday morning, with a little more to go through this morning's storms.")
R("<b>New county numbers tomorrow.</b> The state foliage report comes out Wednesday afternoon; Monroe County was past 30 percent last week.","<b>New numbers Thursday.</b> The state's foliage report comes out Wednesday afternoon; our county numbers run Thursday. Last week Greece, in Monroe County, was past 30 percent color.")
R("Tyler Reddick, with a season-best five wins, sits seventh, 114 back.","Tyler Reddick, a five-time winner this year, sits seventh, 114 back. Larson leads Hamlin by 49 with four races left.")
R("Forecast &amp; barometer per NWS Buffalo","Forecast per NWS Buffalo &middot; barometer forecast via Open-Meteo")
R("scores and standings via Sportradar","Bills recap via AP &middot; scores, standings and NASCAR points via Sportradar")
R("look west-southwest after sunset for the crescent moon, setting at 7:45.","look low in the southwest right after sunset for the thin crescent moon, which sets at 7:45.")
R("One last warm, summery day before October remembers itself: showers this morning, sun this afternoon, then a raw weekend with Saturday stuck in the 40s.","One last warm, summery day: showers this morning, sun this afternoon, then a chilly, partly sunny Saturday that tops out at 49.")
R("Riders were helped off a stuck train.","Aerial footage showed the train stuck on the track as riders were helped off.")
R("the same day registration closes &middot; register by Oct 24","the same day registration closes")
R("New England, 3&ndash;2, is coming off a 45&ndash;17 rout of Las Vegas. Sunday, 1:00.","The Jets are 2&ndash;3; a second straight win would pull them to .500 against a 3&ndash;2 Patriots team. Sunday, 1:00.")
R("An early start on the holiday shelf.","The Christmas classic is now counted among the best movies ever made.")
d['body_html']=b
json.dump(d,open('edition-2026-10-13.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-13.json','w'),ensure_ascii=False,indent=1)
print('fixed')
