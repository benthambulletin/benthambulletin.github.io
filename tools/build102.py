import json
d=json.load(open('edition-2026-10-03.json')); b=d['body_html']
baro=open('/tmp/claude-0/-home-claude/001a10af-13f9-5479-8fec-28bf86d9c496/scratchpad/baro102.html').read(); baro=baro[:baro.index('<!--')]
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
H=lambda o,t:f'<h2 class="sec"><span class="o">{o}</span>{t}<span class="o">{o}</span></h2>\n'
CAP='Luka at the doctor, on antibiotics and ready for Sunday'
R('No. 101','No. 102')
R('Saturday &middot; October 3 &middot; 2026','Sunday &middot; October 4 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">68&deg;</div><div class="k">Mild, front tonight</div></div>
  <div class="tile"><div class="v">30.23&#8243; &#9660;</div><div class="k">Falling again</div></div>
  <div class="tile urg"><div class="v">30</div><div class="k">Days to Election Day</div></div>
</div>
''')
S('<div class="plate-sub">','</div></div>',f'<div class="plate-sub">{CAP}')
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>Luka has the cover</b>, checked over at the doctor's and now on antibiotics. Dad's report: he is ready for a Jets and Bills win. Game-day Sunday in October, the good kind: 68 and mostly sunny, Bills and Patriots at 1:00, Jets at Chicago at 1:00, Las Vegas at 5:30. Then frost is possible around Scottsville Monday night.
''')
# Sunday Spotlight after Family Today
spot=H('&#127809;','The Sunday Spotlight')+'''<div class="touch-head">The Month in Migraine</div>
<div class="line" style="color:var(--soft)">Once a month this space covers what changed in migraine research and treatment, in plain terms, and what the family's own log shows.</div>
<div class="line"><b>New national rules for prevention.</b> On Aug. 31 the American Academy of Neurology and the American Headache Society published their first new guideline on preventing migraine since 2012. Qulipta (atogepant) is on the top tier of drugs doctors should offer. It is a "CGRP blocker": it blocks a nerve chemical that helps set off attacks. Also on the top tier are the monthly shots built on the same idea, plus the older blood-pressure and seizure pills. Patients no longer have to fail an older drug first. A preventive that is working should be talked over at six months, not stopped automatically, and price is a fair tiebreaker.</div>
<div class="line"><b>Same pill, a new use.</b> On Sept. 10 AbbVie reported a 468-woman trial of atogepant for migraines tied to the menstrual cycle: 1.2 fewer migraine days around the period, against 0.4 on a dummy pill, with no new side-effect problems. The company will ask regulators to add that use to the label.</div>
<div class="line"><b>The diary beats the barometer.</b> A Sept. 23 study of 53,065 people using a migraine app built a model that called the next day's attack correctly 91 times in 100 when it said "attack," and caught 80 percent of attacks. A person's own last 30 days of headaches did most of the predicting; weather mattered less. It has not yet been shown to help anyone avoid an attack.</div>
<div class="line"><b>Cannabis, measured.</b> A Sept. 22 review of five controlled trials, 1,072 adults, found vaporized THC plus CBD gave more people relief at two hours than a placebo. CBD alone did not, and the trials were hard to blind.</div>
<div class="line"><b>Who to see.</b> A Sept. 4 count found 797 board-certified headache specialists in the whole country, and none in 91 percent of counties.</div>
<div class="line"><b>Our own month.</b> The family log is new and has no entries yet. That diary study is the case for it: log each one at <a href="https://tally.so/r/obWNYP">tally.so/r/obWNYP</a> and the Barograph will show what the pressure was doing first.</div>
<div class="line" style="color:var(--soft)">Written by an A.I. from public reporting. Not medical advice.</div>
'''
R(H('&#9788;','The Weather Glass'), spot+H('&#9788;','The Weather Glass'))
S('<div class="wx">','<div class="towns">','''<div class="wx"><div class="bigtemp">68<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">One last mild one before the frost</span>
Low <b>48&deg;</b> tonight &middot; south breeze ahead of a cold front<br>A stray shower possible tonight, 24%</div></div>
''')
S('<div class="towns">','<div class="strip5">','''<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">44<sup>&deg;</sup></div><div class="d">Overnight &middot; high 68&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">53<sup>&deg;</sup></div><div class="d">Overnight &middot; high 68&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">42<sup>&deg;</sup></div><div class="d">Overnight &middot; high 70&deg;</div></div>
</div>
''')
S('<div class="strip5">','<h2 class="sec"><span class="o">&#127810;</span>The Turning','''<div class="strip5">
  <div><div class="d">Sun</div><div class="i">&#9728;</div><div class="h">68</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Mon</div><div class="i">&#9728;</div><div class="h">60</div><div class="w">sunny</div></div>
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">61</div><div class="w">sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#127780;</div><div class="h">67</div><div class="w">stray shower</div></div>
  <div><div class="d">Thu</div><div class="i">&#127780;</div><div class="h">66</div><div class="w">sun, then a shower?</div></div>
</div>
<div class="line"><span class="lbl r">Frost chance</span> Scottsville drops to 37 Monday night with patchy frost by Tuesday morning. North Tonawanda bottoms out at 40, Dunkirk at 42. Bring in the tender plants. <span class="lbl t">Outdoor window</span> Today through Tuesday.</div>
''')
S('<div class="line"><b>The high country goes first.</b>','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','''<div class="line"><b>Color is coming down the map.</b> Peak arrives in the Adirondacks first and here last, usually the final week of October. A new state report lands Wednesday.</div>
''')
S('<div class="sky">','<div class="stars">','''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 0 50 96 A21 46 0 0 1 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>Thirty-eight percent</b> and waning, in Cancer, rising at 1:21 a.m.<br>
<span class="lbl t">Sun</span> 7:16a &ndash; 6:51p &middot; <b>11h 35m</b><br>
<span class="lbl t">Next new moon</span> Sat, Oct 10 &middot; <span class="lbl t">Hunter's Moon</span> Mon, Oct 26</div></div>
<div class="line"><span class="lbl r">Tonight</span> The Sun sets before 7 now and keeps sliding about two minutes earlier a night. Saturn is exactly opposite the Sun today, up from dusk to dawn and as bright as it gets all year.</div>
''')
S('<div class="stars">','<div style="font-family:\'LOI\'','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>The Sun is exactly opposite Saturn in your sign</b>. The yearly reckoning with rules and duties lands on you today. Say clearly what you owe and what you don't. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>The moon spends its last full day in your sign</b>. Home game. Stay in, make the chili, feed whoever shows up. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Mars in Leo trines Neptune</b>. Game-day instincts are sound. Trust the gut call. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>Your ruler Mercury closes in on Venus</b>. Say the kind thing out loud instead of thinking it. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Venus holds your sign while Mercury moves up beside her</b>. Charm and argument in the same hand. Lead with the charm. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
S('<div class="baro-top">','<h2 class="sec"><span class="o">&#10038;</span>The Ledger',baro+'''<div class="line"><span class="lbl t">Falling fast again</span> 30.23 at 3 this morning, down 2 millibars in three hours as the next front approaches, a day after the big climb. A drop that quick puts the dial at high even though the pressure is still on the high side overall. No migraines logged this week.</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">The hemp THC business</div><div class="big">$28B</div></div>
<div class="txt">That is the size of the market for hemp-based THC drinks and other products, now fighting for its life after Congress voted to close the loophole it grew up in.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Hiring','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>The Supreme Court Opens Monday</h3><p>The new term starts with cases on climate change, the president's immigration policies and the Second Amendment among the biggest.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Debris From a Missing Medical Jet</h3><p>Searchers found wreckage of a medical jet with six aboard that disappeared near Nantucket early Saturday, flying from Bermuda to Boston.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Trump Pushes Year-Round Daylight Time</h3><p>The president urged supporters to call Arkansas Sen. Tom Cotton to back a bill that would stop the twice-a-year clock change.</p></div></div>
''')
S('<div class="ballot">','<h2 class="sec"><span class="o">&#9962;</span>The Home Wire',H('&#9745;','The Ballot')+'''<div class="touch-head">A Quiet Week in the Polls</div>
<div class="line">Thirty days. No new statewide poll came out this week. The last two, both from mid-September, have Governor Hochul ahead of Bruce Blakeman by 9 points (Siena, 50 to 41) and by 19 (Quinnipiac, 58 to 39) among likely voters.</div>
<div class="line"><b>Coming this week.</b> President Trump is expected in Syracuse on Friday to campaign for Blakeman, according to Politico and local reports.</div>
<div class="line"><b>The national read.</b> Control of the Senate runs through a handful of states. Trump rallied outside Dayton on Saturday for Jon Husted in a tight Ohio race against Sherrod Brown.</div>
<div class="line">The three House seats this family votes in, NY-26, NY-23 and NY-25, are not expected to be close.</div>
<div class="line" style="color:var(--soft)">Early voting Oct 24&ndash;Nov 1 &middot; register by Oct 24 &middot; Election Day Nov 3.</div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; The Auto Show','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<div class="wire"><div class="num">1</div><div><h3>Buffalo &middot; Sabres Rally to Win the Home Opener</h3><p>Down two goals, they came back to beat Chicago 4&ndash;3 Saturday night on Jiri Kulich's goal with 6:40 left.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Rochester &middot; Pumpkins at the Beach Today</h3><p>Autumn at the Lake brings a pumpkin patch and a decorating contest to Ontario Beach Park, noon to 3.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Chautauqua &middot; A Grape-Country Mystery</h3><p>New research into three old local firms, Huntley Manufacturing, Fredonia Preserving and Bedford Products, is tracing a trail through Fredonia, Silver Creek, Brocton and Dunkirk.</p></div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Flutie','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron','''<div class="wire"><div class="num">1</div><div><h3>Taylor Swift Crashes <i>SNL</i></h3><p>She turned up in host Dakota Johnson's opening monologue, playing her breakup therapist.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Tom Cruise's <i>Digger</i> Stumbles</h3><p>The Warner Bros. satire is headed for an opening under $10 million, possibly Cruise's lowest in nearly two decades, while <i>Verity</i> leads the box office.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Elton John Says Goodbye</h3><p>He played the first of his final two shows Friday in Mexico City and thanked fans for "all the love."</p></div></div>
''')
S('<div class="touch-head">Tomorrow at 1:00</div>','<table class="tbl">','''<div class="touch-head">Today at 1:00</div>
<div class="line"><b>Bills</b> &middot; Unbeaten Buffalo hosts New England. Christian Benford and Ray Davis are game-time calls; New England is without Christian Gonzalez and Christian Barmore. Saturday, "Buffalo Joe" Andreessen signed a two-year extension to stay in his hometown.</div>
<div class="line"><b>Jets</b> &middot; At Chicago, with Minkah Fitzpatrick back and Breece Hall, Mason Taylor, Adonai Mitchell, Dylan Parham and Kiko Mauigoa out. The Bears are missing Caleb Williams. A good afternoon for the defense to set the tone.</div>
<div class="line" style="color:var(--soft)">Both games, and what decided them, in tomorrow's paper.</div>
''')
S('<div class="touch-head">Tomorrow at Las Vegas</div>','<div class="cards">','''<div class="touch-head">Tonight at Las Vegas</div>
<div class="line">The halfway point of the ten-race Chase. Larson starts the night 26 points clear of Hamlin and 50 ahead of Bell.</div>
''')
# Sunday back-of-book before On This Day
back=H('&#127810;','The Week Ahead')+'''<div class="line"><b>Weather.</b> Sunny and about 60 Monday and Tuesday, with frost possible around Scottsville Monday night. Back to the upper 60s Wednesday with a chance of showers.</div>
<div class="line"><b>The Barograph at thirty days.</b> A month of hourly readings, and what they do and don't show. Tuesday.</div>
<div class="line"><b>The Ballot.</b> The president in Syracuse Friday.</div>
<div class="line"><b>The Turning.</b> New foliage report Wednesday.</div>
<div class="line"><b>Next Sunday's Spotlight.</b> How lake-effect snow works, before the first band sets up.</div>
<div class="line"><b>Calendar.</b> Claire's birthday Oct 23; Halloween in 27 days.</div>
'''+H('&#9776;','The Week in the Glass')+'''<table class="tbl"><tr><th>Day</th><th class="n">Barometer</th><th class="n">Fcst high</th><th>Sky</th></tr>
<tr><td>Mon 28</td><td class="n">29.95</td><td class="n">68</td><td>cloudy</td></tr>
<tr><td>Tue 29</td><td class="n">30.02</td><td class="n">73</td><td>fog, then sun</td></tr>
<tr><td>Wed 30</td><td class="n">30.05</td><td class="n">74</td><td>mostly cloudy</td></tr>
<tr><td>Thu 1</td><td class="n">29.96</td><td class="n">76</td><td>showers, rain at night</td></tr>
<tr><td>Fri 2</td><td class="n">29.88</td><td class="n">65</td><td>rain, then clouds</td></tr>
<tr><td>Sat 3</td><td class="n">30.31</td><td class="n">63</td><td>sunny</td></tr>
<tr><td>Sun 4</td><td class="n">30.23</td><td class="n">68</td><td>mostly sunny</td></tr></table>
<div class="line">Steady early in the week, a slide into Friday's rain, then a 14-millibar jump by Saturday morning, the biggest swing of the week. The warmest forecast was Thursday's. No migraines logged.</div>
'''+H('&#10023;','The Sunday Question')+'''<div class="qotd"><b>What is the best Halloween costume you ever wore? Worst counts too.</b><br>Send it to the group chat this week. Answers run here next Sunday under your names.<br><span style="color:var(--soft)">Last week's question, the fall tradition you would miss most, is still open.</span></div>
'''
R(H('&#9790;','On This Day'), back+H('&#9790;','On This Day'))
S('<div class="otd">','<h2 class="sec">','''<div class="otd"><b>October 4, 1957</b> &mdash; The Soviet Union launched Sputnik, the first man-made satellite. Americans went out on fall nights hoping to spot it; the bright dot most saw was its rocket stage, and radio fans listened for its beep.</div>
''')
R('What has keys but can\'t open a single lock?','Carved in October, I grin all night on the porch with a candle for a brain. What am I?')
R('<b>Question of the Day:</b> A piano.','<b>Question of the Day:</b> A jack-o\'-lantern.')
R('headlines via CBS, BBC, WKBW, Rochester First, Dunkirk Observer, Deadline, Variety, Hollywood Reporter &middot; injury reports via the Patriots, Jets and Bears',
  'headlines via CBS, PBS, NPR, WKBW, WIVB, Rochester First, Dunkirk Observer, Variety, Billboard, Hollywood Reporter &middot; polls via Siena and Quinnipiac &middot; injury reports via the Patriots, Jets and Bears')
d.update(date='2026-10-04',no=102,body_html=b,plate_path='/home/claude/plate102.jpg',plate_caption=CAP,headline="Luka is ready · The month in migraine · Game day · Frost possible Monday night")
json.dump(d,open('site/data/edition-2026-10-04.json','w'),indent=1); json.dump(d,open('edition-2026-10-04.json','w'),indent=1)
p=json.load(open('site/data/pressure.json'))
if p[-1]['date']!='2026-10-04': p.append({"date":"2026-10-04","in":30.23,"mb":1023.6,"station":"KIAG","time":"02:53 EDT"})
json.dump(p,open('site/data/pressure.json','w'),indent=1)
print('ok')
