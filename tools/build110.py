import json
d=json.load(open('edition-2026-10-11.json')); b=d['body_html']
baro=open('/tmp/claude-0/-home-claude/001a10af-13f9-5479-8fec-28bf86d9c496/scratchpad/baro110.html').read(); baro=baro[:baro.index('<!--')].strip()+'\n'
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
R('No. 109','No. 110')
R('Sunday &middot; October 11 &middot; 2026','Monday &middot; October 12 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">69&deg;</div><div class="k">Cloudy, mild</div></div>
  <div class="tile"><div class="v">29.92&#8243; &#9650;</div><div class="k">Rising</div></div>
  <div class="tile urg"><div class="v">22</div><div class="k">Days to Election Day</div></div>
</div>
''')
S('<div class="plate-wrap">','<h2 class="sec"><span class="o">&#9825;</span>Family Today','')
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>A mild, gray Columbus Day,</b> the kind that smells like wet leaves, with post offices and banks closed. The Jets won yesterday, and the Bills play the Rams tonight. Halloween is 19 days out.
''')
S('<ul class="cal">','</ul>','''<ul class="cal">
<li><span class="dt">Tonight</span><span>Bills at Rams &mdash; 8:15, ABC</span></li>
<li><span class="dt">Oct 17</span><span>Family birthday party (from Ariel)</span></li>
<li><span class="dt">Oct 18</span><span>Jets at Patriots &mdash; 1:00</span></li>
<li><span class="dt">Oct 18</span><span>Bills at Raiders &mdash; 4:25</span></li>
<li><span class="dt">Oct 23</span><span>Claire's birthday</span></li>
<li><span class="dt">Oct 25</span><span>Garret and Ariel's birthday</span></li>
<li><span class="dt">Oct 31</span><span>Halloween</span></li>
<li><span class="dt">Nov 3</span><span>Election Day</span></li>
''')
S('<h2 class="sec"><span class="o">&#127809;</span>The Sunday Spotlight','<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass','')
S('<div class="wx">','<div class="towns">','''<div class="wx"><div class="bigtemp">69<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">Fog lifting off the wet leaves</span>
Low <b>61&deg;</b> tonight &middot; southwest 2&ndash;13<br>Dry today; storms possible before dawn</div></div>
''')
S('<div class="towns">','<div class="strip5">','''<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">57<sup>&deg;</sup></div><div class="d">Fog &middot; high 69&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">61<sup>&deg;</sup></div><div class="d">Cloudy &middot; high 70&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">55<sup>&deg;</sup></div><div class="d">Drizzle &middot; high 71&deg;</div></div>
</div>
''')
S('<div class="strip5">','<h2 class="sec"><span class="o">&#127810;</span>The Turning','''<div class="strip5">
  <div><div class="d">Mon</div><div class="i">&#9729;</div><div class="h">69</div><div class="w">cloudy</div></div>
  <div><div class="d">Tue</div><div class="i">&#9928;</div><div class="h">75</div><div class="w">storms possible, windy</div></div>
  <div><div class="d">Wed</div><div class="i">&#9729;</div><div class="h">66</div><div class="w">mostly cloudy</div></div>
  <div><div class="d">Thu</div><div class="i">&#9925;</div><div class="h">62</div><div class="w">partly sunny</div></div>
  <div><div class="d">Fri</div><div class="i">&#127783;</div><div class="h">61</div><div class="w">rain, 80%</div></div>
</div>
<div class="line"><span class="lbl r">Tuesday</span> A warm, windy 75 with gusts to 32 and a chance of thunderstorms. <span class="lbl t">First flakes?</span> The first mention of snow this season: a slight chance of rain and snow showers late Friday night, with a low of 36.</div>
''')
S('<div class="line"><b>Holding at','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','''<div class="line"><b>Two days to new numbers.</b> The state's next county report is Wednesday; Monroe County was past 30 percent color last week, and the weekend rain thinned some trees.</div>
''')
R('<b>A new crescent</b>, 1 percent lit, sets at 6:46 p.m.<br>','<b>A thin crescent</b>, 4 percent lit, in Scorpio, sets at 7:13 p.m.<br>')
R('7:24a &ndash; 6:39p &middot; <b>11h 15m</b>','7:25a &ndash; 6:37p &middot; <b>11h 12m</b>')
S('<div class="line"><span class="lbl r">Tonight</span> Clouds and rain hide','<div class="stars">','''<div class="line"><span class="lbl r">Tonight</span> If the clouds break after sunset, look low in the west-southwest for the young crescent before it sets at 7:13.</div>
''')
S('<div class="stars">','<div style="font-family','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>Uranus sextiles Neptune in your sign</b>. A new way of seeing an old problem. Try it on Tuesday's to-do list. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>The moon in Scorpio, a fellow water sign, meets Mercury</b>. Say what you mean; it lands well. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Mars in your sign sextiles Uranus</b>. A sudden change of plans works in your favor. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>Your ruler Mercury meets the moon</b>. A conversation goes deeper than planned. Let it. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Venus in your sign squares Pluto</b>. Hold something lightly today; gripping makes it worse. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
S('<div class="baro-top">','<h2 class="sec"><span class="o">&#10038;</span>The Ledger',baro+'''<div class="line"><span class="lbl r">Big swing coming</span> 29.92 and steady after yesterday's drop. The forecast has it dipping about a quarter inch into Tuesday afternoon's storms, then climbing back a quarter inch overnight into Wednesday.</div>
<div class="line"><span class="lbl t">The log</span> Days since the last one: Garret 6, Dad 6, Mom 3. October so far: one each.</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">Weeks at No. 1</div><div class="big">100</div></div>
<div class="txt">Taylor Swift's <i>The Life of a Showgirl</i> spent a 14th week atop the Billboard 200, bringing her career total to 100 weeks at No. 1. The Beatles are the only other act to get there.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Isaias Update','<h2 class="sec"><span class="o">&#9745;</span>The Ballot','''<div class="wire"><div class="num">1</div><div><h3>Economics Nobel to Two Americans</h3><p>Robert E. Hall and Michael Woodford won for their work on how to smooth out boom-and-bust cycles to limit unemployment and inflation. Their models help guide central banks like the Federal Reserve.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Trump Announces an "Energy Ceasefire"</h3><p>The president said Russia and Ukraine agreed to stop hitting each other's power plants but gave no details. Zelensky said he would back it if Moscow does, while saying Russian strikes on power plants continue.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>139 Dead as Migrant Boat Capsizes</h3><p>The boat, carrying 305 people from Djibouti to Yemen, overturned near the port town of Obock; 15 children are among the dead, the U.N. says. Dozens are still missing.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>Tropical Storm Rachel Soaks California</h3><p>The storm flooded parts of the Long Beach waterfront before weakening and moving inland. Forecasters call it a preview of a stormy season for the state.</p></div></div>
''')
S('<h2 class="sec"><span class="o">&#9745;</span>The Ballot','<h2 class="sec"><span class="o">&#9962;</span>The Home Wire','''<div class="ballot">&#9745; The Ballot &middot; <b>22 days</b> to Election Day &middot; Trump's Friday rally for Blakeman in Syracuse drew about 5,000 &middot; register by Oct 24</div>
''')
S('<h2 class="sec"><span class="o">&#9962;</span>The Home Wire<span class="o">&#9962;</span></h2>','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<h2 class="sec"><span class="o">&#9962;</span>The Home Wire<span class="o">&#9962;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>Gates &middot; Family Seeks Answers</h3><p>The adoptive brothers of Haley Rodriguez, the 27-year-old woman killed by Gates police, say they are still trying to understand her death and how it happened, WXXI reports.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Buffalo &middot; Honor Flight Comes Home</h3><p>Veterans from Buffalo Niagara Honor Flight Mission 24 landed back in Western New York Sunday night to a crowd waiting to welcome them.</p></div></div>
''')
S('<h2 class="sec"><span class="o">&#9733;</span>The Marquee<span class="o">&#9733;</span></h2>','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron','''<h2 class="sec"><span class="o">&#9733;</span>The Marquee<span class="o">&#9733;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>A Quiet <i>30 Rock</i> Reunion</h3><p>Liz, Jack, Tracy and the rest of the cast reunited Sunday night, paying tribute to Grizz along the way. <i>The Hollywood Reporter</i> called it weirdly stealth.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Princess Diana, in Her Own Words</h3><p>Prime Video has landed a documentary series built on unheard audio of Princess Diana. It was one of the most sought-after shows heading into this week's TV market in Cannes.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>The Other Jackson Brothers</h3><p>Jackie, Jermaine, Tito and Marlon, the founding members of the Jackson 5 not named Michael, are telling their story in a new documentary.</p></div></div>
''')
S('<div class="touch-head">Today at 1:00</div>','<h2 class="sec"><span class="o">&#9873;</span>The Chase','''<div class="touch-head">Monday Morning Quarterback</div>
<div class="line"><b>Jets 17, Browns 12.</b> Geno Smith hit Garrett Wilson for a 32-yard touchdown in the first quarter, and Cleveland didn't get into the end zone until Deshaun Watson's 29-yard touchdown pass put the Browns up 12&ndash;10 with 6:21 left; they missed the extra point. The Jets answered with a 22-yard touchdown run by Braelon Allen with 3:07 to go, then held on.</div>
<div class="line"><b>Got right:</b> the defense sacked Watson eight times, forced five three-and-outs and made two fourth-down stops, and the run game put up 134 yards. <b>To fix:</b> ten penalties for 102 yards and two lost fumbles. At New England next Sunday.</div>
<div class="line"><b>Bills at Rams, tonight 8:15 on ABC.</b> Buffalo goes in 3&ndash;1 without defensive tackle Ed Oliver and receiver Joshua Palmer. The Rams are 2&ndash;2. The full Bills recap leads tomorrow's paper.</div>
<table class="tbl"><tr><th>AFC East</th><th class="n">W</th><th class="n">L</th><th class="n">T</th></tr>
<tr><td style="color:var(--red)">Buffalo</td><td class="n">3</td><td class="n">1</td><td class="n">0</td></tr>
<tr><td>New England</td><td class="n">3</td><td class="n">2</td><td class="n">0</td></tr>
<tr><td style="color:var(--red)">N.Y. Jets</td><td class="n">2</td><td class="n">3</td><td class="n">0</td></tr>
<tr><td>Miami</td><td class="n">0</td><td class="n">5</td><td class="n">0</td></tr></table>
<div class="line"><b>Around the league.</b> New England routed Las Vegas 45&ndash;17. San Francisco won 32&ndash;29 at Seattle and Minnesota 23&ndash;13 at New Orleans; both are still unbeaten. The Giants and Commanders tied, 27&ndash;27. Green Bay beat Chicago 31&ndash;7.</div>
<div class="line"><b>The AI Editor, graded.</b> Bills 11&ndash;6: 3&ndash;1 before tonight, still ahead of pace. Jets 6&ndash;11: now 2&ndash;3, a little ahead of that pace. Ravens over Rams in the Super Bowl: Baltimore won 30&ndash;23 in Atlanta last night to go 4&ndash;1; the Rams, 2&ndash;2, host Buffalo tonight.</div>
''')
S('<div class="touch-head">Today at Charlotte, 3:00</div>','<h2 class="sec"><span class="o">&#127810;</span>The Week Ahead','''<div class="touch-head">Briscoe Takes Charlotte</div>
<div class="line">Chase Briscoe won at Charlotte, his third win of the year, and jumped to fourth. Larson still leads, now by 49 over Hamlin, 51 over Bell and 65 over Briscoe. Four races left, Homestead the last.</div>
''')
S('<h2 class="sec"><span class="o">&#127810;</span>The Week Ahead','<h2 class="sec"><span class="o">&#9790;</span>On This Day','')
S('<div class="otd">','<h2 class="sec"><span class="o">&#10023;</span>Question of the Day','''<div class="otd"><b>October 12, 1492</b> &mdash; Christopher Columbus's expedition reached an island in the Bahamas he named San Salvador. Its Lucayan people called it Guanahani.</div>
''')
S('<div class="qotd">','<div class="dbl">','''<div class="qotd">I have a face and two hands but no arms or legs, and in three weeks I'll give everybody an extra hour. What am I? <i>Answer below the fold.</i></div>
''')
R("<b>Question of the Day:</b> A pumpkin.","<b>Question of the Day:</b> A clock. Daylight saving time ends Nov. 1.")
R('headlines via CBS, NPR, BBC, WIVB, WKBW, Dunkirk Observer, Rochester First, Deadline, Hollywood Reporter, Billboard &middot; ballot via Ken-Ton Bee, Chautauqua Today, Niagara Gazette &middot; Spotlight draws on The New York Times, NOAA, the University of Windsor, the University at Buffalo and Cleveland Magazine','headlines via CBS, NPR, BBC, PBS, WIVB, WXXI, Niagara Gazette, Variety, Deadline, Hollywood Reporter, Billboard')
d['no']=110; d['date']='2026-10-12'; d['headline']='Jets beat Browns · Bills at Rams tonight · Briscoe wins Charlotte · First snow mention'
d['body_html']=b; d['plate_path']=None; d['plate_caption']=None
json.dump(d,open('edition-2026-10-12.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-12.json','w'),ensure_ascii=False,indent=1)
p=json.load(open('site/data/pressure.json')); p=[x for x in p if x['date']!='2026-10-12']
p.append({'date':'2026-10-12','in':29.92,'mb':1013.1,'station':'KIAG','time':'06:53 EDT'}); json.dump(p,open('site/data/pressure.json','w'),indent=1)
print('ok')
# --- review fixes ---
d=json.load(open('edition-2026-10-12.json')); b=d['body_html']
R("Trump's Friday rally for Blakeman in Syracuse drew about 5,000","four Republican and two Democratic senators told Trump Sunday to reverse his Russian diesel deal")
R('&#8595; falling overnight','&#8593; rising this morning')
R("29.92 and steady after yesterday's drop.","29.92 and edging up this morning after a drop of about a quarter inch yesterday.")
S('<div class="wire"><div class="num">1</div><div><h3>Gates','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<div class="wire"><div class="num">1</div><div><h3>Fredonia &middot; Fire Department Open House</h3><p>The Fredonia Fire Department and local police held an open house for residents Saturday. The department thanked everyone who came for the activities, demonstrations and "old fashioned fun."</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Buffalo &middot; Honor Flight Comes Home</h3><p>Veterans from Buffalo Niagara Honor Flight Mission 24 landed back in Western New York Sunday night to a crowd of family, friends and neighbors. The trip honored their service; the nonprofit is marking ten years.</p></div></div>
''')
R("Prime Video has landed a documentary series built on unheard audio of Princess Diana. It was one of the most sought-after shows heading into this week's TV market in Cannes.","Prime Video has landed the UK and Ireland rights to a documentary series built on unheard audio of Princess Diana. The three-part series will launch there as <i>Diana: Her Secret Confessions</i>; no U.S. home has been announced.")
R("are telling their story in a new documentary.</p>","are getting a documentary of their own for the first time. The feature-length film is being shopped at this week's TV market in Cannes, <i>Variety</i> reports.</p>")
R("15 children are among the dead, the U.N. says.","children are among the dead, the U.N. says.")
R("Monroe County was past 30 percent color last week, and the weekend rain thinned some trees.","Monroe County was past 30 percent color in last Wednesday's report; new county numbers come Wednesday.")
R("<b>Two days to new numbers.</b> The state's next county report is Wednesday; ","<b>Two days to new numbers.</b> ")
R("The first mention of snow this season: a slight chance","Snow shows up in the forecast: a slight chance")
R("Low <b>61&deg;</b> tonight &middot; southwest 2&ndash;13","Low <b>61&deg;</b> tonight &middot; southwest 7&ndash;12")
R("Their models help guide central banks like the Federal Reserve.","Their models help governments and central banks respond to economic shocks.")
R("Geno Smith hit Garrett Wilson for a 32-yard touchdown in the first quarter, and Cleveland didn't get into the end zone","Geno Smith hit Garrett Wilson for a 32-yard touchdown in the first quarter, and after two Cleveland field goals and a 54-yarder from the Jets it was 10&ndash;6 early in the fourth. Cleveland didn't get into the end zone")
R('<span class="lede">Fog lifting off the wet leaves</span>','<span class="lede">Fog lifting off the river</span>')
R("the Rams, 2&ndash;2, host Buffalo tonight.","the Rams play Buffalo tonight.")
d['body_html']=b
json.dump(d,open('edition-2026-10-12.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-12.json','w'),ensure_ascii=False,indent=1)
R('PBS, WIVB, WXXI, Niagara Gazette','PBS, WIVB, Dunkirk Observer, Niagara Gazette')
d['body_html']=b
json.dump(d,open('edition-2026-10-12.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-12.json','w'),ensure_ascii=False,indent=1)
print('fixed')
