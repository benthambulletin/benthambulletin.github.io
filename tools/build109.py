import json
d=json.load(open('edition-2026-10-10.json')); b=d['body_html']
baro=open('/tmp/claude-0/-home-claude/001a10af-13f9-5479-8fec-28bf86d9c496/scratchpad/baro109.html').read(); baro=baro[:baro.index('<!--')].strip()+'\n'
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
CAP="Luka takes a break under the lawnmower handle"
R('No. 108','No. 109')
R('Saturday &middot; October 10 &middot; 2026','Sunday &middot; October 11 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">63&deg;</div><div class="k">Rain likely</div></div>
  <div class="tile"><div class="v">30.19&#8243; &#9660;</div><div class="k">Falling fast</div></div>
  <div class="tile urg"><div class="v">23</div><div class="k">Days to Election Day</div></div>
</div>
''')
S('<div class="plate-sub">','</div></div>','<div class="plate-sub">'+CAP)
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>Luka has the cover</b>, supervising yard work from the best seat in the yard. Today belongs to the rain, the Jets at 1:00 and a long Sunday paper. A new date from Ariel is on the calendar: the family birthday party, Saturday.
''')
S('<ul class="cal">','</ul>','''<ul class="cal">
<li><span class="dt">Today</span><span>Browns at Jets &mdash; 1:00</span></li>
<li><span class="dt">Today</span><span>Charlotte, race 6 of the Chase &mdash; 3:00</span></li>
<li><span class="dt">Oct 12</span><span>Bills at Rams &mdash; Monday night, 8:15, ABC</span></li>
<li><span class="dt">Oct 17</span><span>Family birthday party (from Ariel)</span></li>
<li><span class="dt">Oct 18</span><span>Jets at Patriots &mdash; 1:00</span></li>
<li><span class="dt">Oct 23</span><span>Claire's birthday</span></li>
<li><span class="dt">Oct 25</span><span>Garret and Ariel's birthday</span></li>
<li><span class="dt">Oct 31</span><span>Halloween</span></li>
<li><span class="dt">Nov 3</span><span>Election Day</span></li>
''')
SPOT='''<h2 class="sec"><span class="o">&#127809;</span>The Sunday Spotlight<span class="o">&#127809;</span></h2>
<div class="touch-head">How Lake-Effect Snow Works</div>
<div class="line" style="color:var(--soft)">Twenty years ago tomorrow, the October Surprise dropped about 20 inches of heavy, wet snow on Buffalo with the leaves still on the trees. It was lake-effect snow, the same machine that will start up again in a few weeks. How it works, why it hits some of us and skips others, how forecasters call it, and what the new AI weather models can and can't do about it. An AI wrote this section.</div>
<div class="line"><b>1. The machine.</b> Lake-effect snow starts when very cold air blows across a lake that is still warm. The lake heats and moistens the bottom of that air, the warm, wet air rises, and it dumps its water as snow once it reaches land. The bigger the gap between the lake and the air above it, the harder it snows. That is why the season peaks from mid-November into January: the air has turned cold and the lakes haven't yet. <b>What it means for us:</b> Lake Erie is shallow, so it often freezes over by midwinter, and once it does, its lake-effect snow mostly shuts off. Lake Ontario is deep and rarely freezes, so it keeps going all winter.</div>
<div class="line"><b>2. The band.</b> The snow doesn't fall evenly. It comes in long, narrow bands, often 5 to 20 miles wide, that can sit over the same spot for hours. One side of a town can get two feet while the other side sees flurries and sun. <b>Where it lands is all about the wind.</b> A wind from the southwest drives Erie's band toward Buffalo and the Southtowns. A west wind aims it south of Buffalo and into ski country. A northwest wind sends it along the Chautauqua shore, toward Dunkirk. North Tonawanda usually sits north of Erie's bands, which is why it so often gets a dusting while Orchard Park digs out. Lake Ontario's bands mostly run east, toward Oswego and the Tug Hill; Rochester gets them only when the wind comes from the north or northwest, which is why Scottsville tends to come out lighter than Buffalo.</div>
<div class="line"><b>3. How forecasters call it.</b> The National Weather Service office in Buffalo watches three things: how cold the air is a mile up compared with the lake, which way the wind is blowing, and how long it will keep blowing that way. A small turn in the wind can move a band several miles, which is the difference between a snow day and a normal one. When a band looks likely, the office issues a lake-effect snow watch, then a warning, county by county. <b>What it means for us:</b> a warning for "Erie County" doesn't mean all of Erie County. Read the town list and the timing.</div>
<div class="line"><b>4. What AI changes.</b> This week's hurricane put the new AI forecasting models to a public test, The New York Times reported. Early on, the traditional models, which calculate the weather from the laws of physics, pointed Isaias west toward Alabama and Mississippi; the AI models, trained on decades of past weather, pushed it east toward Pensacola. Through the week the physics models moved toward the AI ones, and the storm came ashore near Destin, about 40 miles east of Pensacola. The Hurricane Center's deputy director told the Times his forecasters don't pick a "winning horse"; they blend the models with human judgment, which beats any single one. The AI models have now earned trust on where a storm goes, he said, but still trail the physics models on how strong it gets, and both kinds missed Hurricane Otis in 2023, which exploded where there were few weather sensors to feed them.</div>
<div class="line"><b>Why it matters for lake effect.</b> Honestly, it's an open question. Most AI weather models look at the world on a grid of squares roughly 15 miles across, which is about the width of a single lake band, too coarse to say which town gets buried. For the band itself, the Buffalo office still leans on fine-grained physics models and its own forecasters, who know these lakes. Where AI may help is the bigger picture: when the arctic air arrives and how long the wind holds steady. That is half the call. <b>What's next:</b> watch whether the Buffalo office's forecast discussions start citing the AI models this winter; that is the sign they are earning a seat at the table.</div>
<div class="line"><b>Coming down the road.</b> The lakes are still warm from summer, so the first cold blast of the season is the one to watch; that setup is what made the October Surprise. The Weather Glass will flag the first lake-effect watch for any of our three towns, and once the snow starts, the paper adds a season-to-date snow tracker for North Tonawanda.</div>
'''
R('<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass',SPOT+'<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass')
S('<div class="wx">','<div class="towns">','''<div class="wx"><div class="bigtemp">63<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">A gray, soaking Sunday</span>
Low <b>53&deg;</b> tonight &middot; light east, then northeast<br>Rain likely after 8 a.m., 70 percent, ending by about 10 tonight</div></div>
''')
S('<div class="towns">','<div class="strip5">','''<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">55<sup>&deg;</sup></div><div class="d">Mostly clear &middot; high 63&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">61<sup>&deg;</sup></div><div class="d">Mostly cloudy &middot; high 65&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">57<sup>&deg;</sup></div><div class="d">Cloudy &middot; high 62&deg;</div></div>
</div>
''')
S('<div class="strip5">','<h2 class="sec"><span class="o">&#127810;</span>The Turning','''<div class="strip5">
  <div><div class="d">Sun</div><div class="i">&#127783;</div><div class="h">63</div><div class="w">rain likely</div></div>
  <div><div class="d">Mon</div><div class="i">&#9729;</div><div class="h">68</div><div class="w">mostly cloudy</div></div>
  <div><div class="d">Tue</div><div class="i">&#9928;</div><div class="h">74</div><div class="w">storms likely</div></div>
  <div><div class="d">Wed</div><div class="i">&#9925;</div><div class="h">64</div><div class="w">partly sunny</div></div>
  <div><div class="d">Thu</div><div class="i">&#9728;</div><div class="h">62</div><div class="w">mostly sunny</div></div>
</div>
<div class="line"><span class="lbl r">Rain</span> The remains of Isaias: a quarter to half an inch in North Tonawanda by tonight, a quarter to half in Scottsville today alone, and the most in Dunkirk, half to three-quarters of an inch today. <span class="lbl t">Outdoor window</span> Monday, dry and mild for the holiday.</div>
''')
S('<div class="line"><b>Today','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','''<div class="line"><b>Holding at Wednesday's numbers.</b> Monroe County was past 30 percent color in the last state report; the rain will bring some leaves down early. New county numbers Wednesday.</div>
''')
R('<b>New moon</b> at 11:50 a.m., in Libra, invisible all day<br>','<b>A new crescent</b>, 1 percent lit, sets at 6:46 p.m.<br>')
R('7:22a &ndash; 6:41p &middot; <b>11h 18m</b>','7:24a &ndash; 6:39p &middot; <b>11h 15m</b>')
S('<div class="line"><span class="lbl r">Tonight</span> The darkest night','<div class="stars">','''<div class="line"><span class="lbl r">Tonight</span> Clouds and rain hide the first sliver of the new moon. Sunset is down to 6:39, about 2 hours earlier than in June.</div>
''')
S('<div class="stars">','<div style="font-family','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>Neptune in your sign sextiles Pluto</b>. A quiet idea gets traction. Write it down before the week starts. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>The Sun sextiles Jupiter</b>. A good day to ask for help. People will say yes. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Mars in your sign trines Saturn</b>. Steady effort beats loud effort. The week rewards whoever shows up. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>The new crescent squares Pluto</b>. Clear out one thing you've outgrown. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>The young moon enters your sign to join Mercury and Venus</b>. Three lights in Scorpio: you have the room. Use it kindly. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
S('<div class="baro-top">','<h2 class="sec"><span class="o">&#10038;</span>The Ledger',baro+'''<div class="line"><span class="lbl r">Big swing coming</span> 30.19 and falling. The forecast has it dropping about four-tenths of an inch between last night and tonight as Isaias's leftovers pass.</div>
<div class="line"><span class="lbl t">The log</span> Mom logged one Friday about 4 a.m.; it woke her. In the 12 hours before, pressure was climbing. Days since the last one: Garret 5, Dad 5, Mom 2. October so far: one each.</div>
<div class="pnote"><b>What the barometer told us.</b> The family's numbers are in: Garret's 40 logged migraines since April 2025, against hourly readings from the Niagara Falls station. The barometer did not predict them. Attacks fell on rising and falling days in the same share as any random day, and the size of the change didn't matter either. We'll keep printing the pressure because you like knowing it, and more entries from more of us could still change the answer, but it is weather, not a warning. What did show: attacks cluster. Nearly half came within three days of the one before, so "days since the last one" is the number that means something. Thank you for logging. <a href="https://tally.so/r/obWNYP">tally.so/r/obWNYP</a> &middot; <a href="https://tally.so/r/Zj4dpo">tally.so/r/Zj4dpo</a> &mdash; The Bulletin</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">Out of work, out of benefits</div><div class="big">4 in 10</div></div>
<div class="txt">Nearly that many people who lose a job now run through their unemployment benefits before they find new work, NPR reports. The search is taking longer than it used to.</div></div>
''')
S('<div class="pnote"><b>Hurricane update','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>Isaias Update: At Least Four Dead</h3><p>The storm has killed at least four people in Florida and Alabama, and hundreds of thousands are still without power. It has weakened to a tropical storm and is heading toward the Tennessee Valley.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Eight Killed in Erie Shooting</h3><p>A gunman killed eight people, including two children and a pregnant woman, at a house in Erie, Pa., Friday night, then died himself. Police say all but one of the dead, including the gunman, were related.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Pope Leo to Have Lung Surgery</h3><p>The 71-year-old pope will have surgery after a nodule was found on his lung. He said it was caught "at a very early stage."</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>Deadly Strike on Riyadh's Airport</h3><p>At least 12 people, including one American, were killed and 309 hurt in a strike Saturday on Riyadh's main airport. President Trump is weighing whether to join the fight against the Houthis, Iran's allies in Yemen.</p></div></div>
''')
BALLOT='''<h2 class="sec"><span class="o">&#9745;</span>The Ballot<span class="o">&#9745;</span></h2>
<div class="touch-head">Twenty-Three Days Out</div>
<div class="line"><b>Governor.</b> A new Marist poll has Kathy Hochul ahead of Bruce Blakeman by 11 points among registered voters statewide, but Blakeman ahead upstate, which is where all three of our towns are. President Trump rallied for Blakeman in Syracuse Friday and went after Hochul. <b>What it means:</b> Hochul is still the clear favorite, with the margin coming from downstate. Also on the statewide ballot: Attorney General Letitia James against Saritha Komatireddy, and Comptroller Thomas DiNapoli against Joseph Hernandez.</div>
<div class="line"><b>NY-26, North Tonawanda.</b> Democrat Tim Kennedy against Republican Dennis Hannon. No public poll; the Cook Political Report still rates it solidly Democratic, meaning it isn't considered in play.</div>
<div class="line"><b>NY-23, Dunkirk.</b> Republican Nick Langworthy against Democrat Aaron Gies. They debated Tuesday in Elmira, where affordability and tariffs led the night. The only polls are the campaigns' own; the district leans Republican.</div>
<div class="line"><b>NY-25, Scottsville.</b> Democrat Joe Morelle, in Congress since 2018, is favored again; no public poll, and Cook rates it solidly Democratic.</div>
<div class="line"><b>The state legislature, North Tonawanda.</b> State Senate, 62nd District: Republican Rob Ortt, the Senate's Republican leader, against Democrat Thomas Arida. Assembly, 145th District, which takes in part of North Tonawanda: an open seat, with Angelo Morinello not running; Republican Becky Wydysh against Democrat Nathan McMurray, who ran for Congress in 2018 and 2020. <b>Also on the North Tonawanda ballot:</b> a yes-or-no question on borrowing up to $18 million to build a community center.</div>
<div class="line"><b>The state legislature, Dunkirk.</b> State Senate, 57th District: Republican George Borrello against Democrat Victoria Guite, a SUNY Fredonia graduate who opposes huge data centers and wants big corporations to pay a little more to the communities where they operate. Scottsville's legislative races come with next Sunday's full ballot guide.</div>
<div class="line"><b>The national read.</b> The Cook Political Report moved 18 more House races toward Democrats this week. Trump campaigned in Tennessee Saturday.</div>
<div class="line"><b>What to do now.</b> Register by Oct 24. Next Sunday: everything else on your ballot, town by town.</div>
<div class="line" style="color:var(--soft)">Early voting Oct 24&ndash;Nov 1 &middot; register by Oct 24 &middot; Election Day Nov 3.</div>
'''
S('<div class="ballot">','<h2 class="sec"><span class="o">&#9962;</span>The Home Wire',BALLOT)
S('<h2 class="sec"><span class="o">&#9962;</span>The Home Wire<span class="o">&#9962;</span></h2>','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<h2 class="sec"><span class="o">&#9962;</span>The Home Wire<span class="o">&#9962;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Free Pet Adoptions Today</h3><p>Rochester Animal Services and The Rescue Effort are waiving adoption fees today to get more shelter animals into homes.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Silver Creek &middot; Seventy-Five Years</h3><p>Harry and Joan Suski of Silver Creek celebrate their 75th wedding anniversary Oct. 20. They were married in 1951 at Our Lady of Mount Carmel.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Tonawanda &middot; Car Hits Paula's Donuts</h3><p>A car crashed into Paula's Donuts on Sheridan Drive Saturday after a crash involving several vehicles in the Town of Tonawanda.</p></div></div>
''')
S('<h2 class="sec"><span class="o">&#9733;</span>The Marquee<span class="o">&#9733;</span></h2>','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron','''<h2 class="sec"><span class="o">&#9733;</span>The Marquee<span class="o">&#9733;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>A New <i>Blade Runner</i></h3><p>The first full trailer for <i>Blade Runner 2099</i> pairs Hunter Schafer with Michelle Yeoh in a limited series set when replicants have taken over. It's the first new <i>Blade Runner</i> since 2017.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Shane Gillis Hosts <i>SNL</i> Again</h3><p>His third time as host included an on-air slip in a Dr. Seuss sketch, for which he apologized. Rosal&iacute;a was the musical guest.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Barry Manilow Cancels Vegas Shows</h3><p>The 83-year-old walked off stage after two songs with bronchitis, days into his return to the Westgate residency. The next shows are canceled.</p></div></div>
''')
R('<div class="touch-head">Two Days to Los Angeles</div>','<div class="touch-head">Today at 1:00</div>')
S('<div class="line"><b>Bills</b>','<table class="tbl">','''<div class="line"><b>Jets</b> &middot; Home against Cleveland at 1:00. The Browns come in 3&ndash;1; the Jets are 1&ndash;3 and slight favorites at home. A win gets them back within a game of .500.</div>
<div class="line"><b>Bills</b> &middot; Tomorrow night at the Rams, 8:15 on ABC, without two starters: coach Joe Brady ruled out defensive tackle Ed Oliver and receiver Joshua Palmer on Saturday.</div>
<div class="line" style="color:var(--soft)">The Jets game in tomorrow's paper; both, in full, Tuesday after the Bills play.</div>
''')
R('<div class="touch-head">Tomorrow: Charlotte</div>','<div class="touch-head">Today at Charlotte, 3:00</div>')
S('<div class="line">Ryan Preece is 16th','<div class="cards">','''<div class="line">Race six of ten. Nine drivers start the day within 128 points of Larson; after today, four races are left before Homestead.</div>
''')
EXTRA='''<h2 class="sec"><span class="o">&#127810;</span>The Week Ahead<span class="o">&#127810;</span></h2>
<div class="line"><b>Weather.</b> Dry and mild for Columbus Day, 68. Showers and thunderstorms Tuesday with a warm 74, then cooler Wednesday and Thursday in the low 60s.</div>
<div class="line"><b>Games.</b> Bills at the Rams Monday, 8:15 on ABC. Jets at New England Sunday, Oct 18, 1:00.</div>
<div class="line"><b>The Ballot.</b> Registration closes Oct 24, the same day early voting opens.</div>
<div class="line"><b>The Turning.</b> New foliage report Wednesday.</div>
<div class="line"><b>Next Sunday's Spotlight.</b> What's on your ballot besides the governor, town by town.</div>
<div class="line"><b>Calendar.</b> The family birthday party Saturday, from Ariel. Claire's birthday Oct 23; Halloween in 20 days.</div>
<h2 class="sec"><span class="o">&#9776;</span>The Week in the Glass<span class="o">&#9776;</span></h2>
<table class="tbl"><tr><th>Day</th><th class="n">Barometer</th><th class="n">Fcst high</th><th>Sky</th></tr>
<tr><td>Mon 5</td><td class="n">30.04</td><td class="n">60</td><td>sunny, breezy</td></tr>
<tr><td>Tue 6</td><td class="n">30.24</td><td class="n">59</td><td>sunny, calm</td></tr>
<tr><td>Wed 7</td><td class="n">29.87</td><td class="n">68</td><td>windy, storms late</td></tr>
<tr><td>Thu 8</td><td class="n">29.83</td><td class="n">65</td><td>sunny, cool</td></tr>
<tr><td>Fri 9</td><td class="n">30.14</td><td class="n">66</td><td>sunny</td></tr>
<tr><td>Sat 10</td><td class="n">30.39</td><td class="n">71</td><td>mostly sunny</td></tr>
<tr><td>Sun 11</td><td class="n">30.19</td><td class="n">63</td><td>rain likely</td></tr></table>
<div class="line">A drop of about four-tenths of an inch into Wednesday's storms, then a climb of more than half an inch to Saturday's 30.39, the high of the week. Migraines logged: Dad and Garret Tuesday morning, on a high, steady day; Mom early Friday, while it was climbing.</div>
<h2 class="sec"><span class="o">&#10023;</span>The Sunday Question<span class="o">&#10023;</span></h2>
<div class="qotd"><b>What's the fall food you only eat this time of year?</b><br>Send it at tally.so/r/rjxDpl or to the group chat this week. Answers run here next Sunday under your names.<br><span style="color:var(--soft)">Last week's question, your best or worst Halloween costume, is still open.</span></div>
'''
R('<h2 class="sec"><span class="o">&#9790;</span>On This Day',EXTRA+'<h2 class="sec"><span class="o">&#9790;</span>On This Day')
S('<div class="otd">','<h2 class="sec"><span class="o">&#10023;</span>Question of the Day','''<div class="otd"><b>October 11, 1984</b> &mdash; Kathryn Sullivan became the first American woman to walk in space, stepping outside the shuttle Challenger for about three and a half hours.</div>
''')
S('<div class="qotd">I have ears','<div class="dbl">','''<div class="qotd">I'm round and orange, I grow on a vine, and every October somebody gives me a face. What am I? <i>Answer below the fold.</i></div>
''')
R("<b>Question of the Day:</b> Corn.","<b>Question of the Day:</b> A pumpkin.")
R('headlines via CBS, BBC, PBS, WIVB, Niagara Gazette, Rochester First, Deadline, Hollywood Reporter, Billboard','headlines via CBS, NPR, BBC, WIVB, WKBW, Dunkirk Observer, Rochester First, Deadline, Hollywood Reporter, Billboard &middot; ballot via Ken-Ton Bee, Chautauqua Today, Niagara Gazette &middot; Spotlight draws on The New York Times')
d['no']=109; d['date']='2026-10-11'; d['headline']='How lake-effect snow works · Isaias rain · The Ballot in full · Luka and the mower'
d['body_html']=b; d['plate_path']='/home/claude/plate109.jpg'; d['plate_caption']=CAP
json.dump(d,open('edition-2026-10-11.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-11.json','w'),ensure_ascii=False,indent=1)
p=json.load(open('site/data/pressure.json')); p=[x for x in p if x['date']!='2026-10-11']
p.append({'date':'2026-10-11','in':30.19,'mb':1022.4,'station':'KIAG','time':'06:53 EDT'}); json.dump(p,open('site/data/pressure.json','w'),indent=1)
print('ok')
# --- review fixes ---
d=json.load(open('edition-2026-10-11.json')); b=d['body_html']
R("on Sheridan Drive Saturday after a crash involving several vehicles in the Town of Tonawanda.</p>","on Sheridan Drive Friday evening after a crash involving several vehicles in the Town of Tonawanda.</p>")
R("after today, four races are left before Homestead.","after today, four races are left, Homestead the last of them.")
R("The first full trailer for <i>Blade Runner 2099</i> pairs Hunter Schafer with Michelle Yeoh in a limited series set when replicants have taken over. It's the first new <i>Blade Runner</i> since 2017.","A new trailer for <i>Blade Runner 2099</i>, shown at New York Comic Con, pairs Hunter Schafer with Michelle Yeoh in a limited series set when replicants have taken over. The team describes it as a detective story.")
R("The only polls are the campaigns' own; the district leans Republican.","The only polls are the campaigns' own, released two weeks ago: Langworthy's had him up 54 to 33, while Gies's found only 44 percent say Langworthy deserves another term. Campaign polls flatter their side; the district leans Republican.")
R("<b>The national read.</b> The Cook Political Report moved 18 more House races toward Democrats this week. Trump campaigned in Tennessee Saturday.","<b>The national read.</b> President Trump campaigned for Republicans in Tennessee Saturday, with midterm voting less than three weeks away.")
R("on a high, steady day; Mom early Friday, while it was climbing.","as it was still climbing after a big rise; Mom early Friday, also while it was climbing.")
R("dropped about 20 inches of heavy, wet snow on Buffalo","dropped nearly two feet of heavy, wet snow on Buffalo, 22.6 inches at the airport,")
R("Rochester gets them only when the wind comes from the north or northwest, which is why Scottsville tends to come out lighter than Buffalo.","Rochester's lakeshore gets them mainly when the wind comes from the north or northwest, and Scottsville, well inland, usually catches the edge of those bands rather than the heart of them.")
R("It has weakened to a tropical storm and is heading toward the Tennessee Valley.","It has weakened to a post-tropical storm, and its leftovers are today's rain here.")
R("which beats any single one.","which often beats any single one.")
R("coach Joe Brady ruled out defensive tackle Ed Oliver and receiver Joshua Palmer on Saturday.</div>","coach Joe Brady ruled out defensive tackle Ed Oliver and receiver Joshua Palmer on Saturday. Palmer hurt his shoulder in practice Friday, Brady said. Buffalo goes in 3&ndash;1 and first in the AFC East.</div>")
R("are waiving adoption fees today to get more shelter animals into homes.</p>","are waiving adoption fees today to get more shelter animals into homes. The waiver is for today only.</p>")
R("Republican George Borrello against Democrat Victoria Guite, a SUNY Fredonia graduate who opposes huge data centers and wants big corporations to pay a little more to the communities where they operate.","Republican incumbent George Borrello against Democrat Victoria Guite, a SUNY Fredonia graduate who opposes huge data centers and wants corporations to pay a little more.")
R("at a house in Erie, Pa., Friday night, then died himself.","at a house in Erie, Pa., Friday evening. The gunman is also dead.")
R('<div class="d">Cloudy &middot; high 62&deg;</div>','<div class="d">Rain coming &middot; high 62&deg;</div>')
R("about 2 hours earlier than in June.","about two and a half hours earlier than in June.")
R('<span class="lede">A gray, soaking Sunday</span>','<span class="lede">A gray, soaking October Sunday, porch lights on by supper</span>')
R("<b>Luka has the cover</b>, supervising yard work from the best seat in the yard.","<b>Luka has the cover</b>, stretched out on a mat under the lawnmower handle.")
R('<a href="https://tally.so/r/obWNYP">tally.so/r/obWNYP</a> &middot; <a href="https://tally.so/r/Zj4dpo">tally.so/r/Zj4dpo</a>','Log a migraine: <a href="https://tally.so/r/obWNYP">tally.so/r/obWNYP</a> &middot; Evening check-in: <a href="https://tally.so/r/Zj4dpo">tally.so/r/Zj4dpo</a>')
d['body_html']=b
json.dump(d,open('edition-2026-10-11.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-11.json','w'),ensure_ascii=False,indent=1)
print('fixed')
