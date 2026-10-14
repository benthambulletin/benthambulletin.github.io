import json
d=json.load(open('edition-2026-10-13.json')); b=d['body_html']
baro=open('/tmp/claude-0/-home-claude/001a10af-13f9-5479-8fec-28bf86d9c496/scratchpad/baro112.html').read(); baro=baro[:baro.index('<!--')].strip()+'\n'
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
R('No. 111','No. 112')
R('Tuesday &middot; October 13 &middot; 2026','Wednesday &middot; October 14 &middot; 2026')
# tiles (also drops yesterday's plate block; no photo yet today)
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">64&deg;</div><div class="k">Mostly cloudy</div></div>
  <div class="tile"><div class="v">29.90&#8243; &#9660;</div><div class="k">Big drop Friday</div></div>
  <div class="tile urg"><div class="v">20</div><div class="k">Days to Election Day</div></div>
</div>
''')
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>Three days to the party.</b> The family birthday party is Saturday, and the forecast for it is mostly sunny, breezy and 49, so bring a layer. Kaylani sent in today's strangest news story; it's just below.
''')
# Group Chat box after Family Today
R('''tally.so/r/obWNYP</a>.</div></div>
<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass''','''tally.so/r/obWNYP</a>.</div></div>
<h2 class="sec"><span class="o">&#9998;</span>From the Group Chat<span class="o">&#9998;</span></h2>
<div class="qotd"><b>Kaylani writes:</b> Today's news you didn't ask for. In Rosenberg, Texas, a man reportedly drove his car through a locked Kroger pharmacy entrance after finding the store closed, because he needed to use the restroom. No injuries were reported. Some people knock. Some people find a gas station. This gentleman chose automotive demolition. Today's takeaway: when nature calls, please do not answer with your vehicle.</div>
<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass''')
# Weather Glass
S('<div class="wx">','<h2 class="sec"><span class="o">&#127810;</span>The Turning','''<div class="wx"><div class="bigtemp">64<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">Sweater weather, on a northwest wind</span>
Low <b>45&deg;</b> tonight &middot; northwest 8&ndash;12<br>A stray shower possible 8 to 9 a.m., 20 percent, then mostly cloudy</div></div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">59<sup>&deg;</sup></div><div class="d">Cloudy &middot; high 64&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">63<sup>&deg;</sup></div><div class="d">Cloudy &middot; high 63&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">63<sup>&deg;</sup></div><div class="d">Cloudy &middot; high 64&deg;</div></div>
</div>
<div class="strip5">
  <div><div class="d">Wed</div><div class="i">&#9729;</div><div class="h">64</div><div class="w">mostly cloudy</div></div>
  <div><div class="d">Thu</div><div class="i">&#9925;</div><div class="h">60</div><div class="w">partly sunny, rain at night</div></div>
  <div><div class="d">Fri</div><div class="i">&#9928;</div><div class="h">59</div><div class="w">showers, storms</div></div>
  <div><div class="d">Sat</div><div class="i">&#127780;</div><div class="h">49</div><div class="w">mostly sunny, breezy</div></div>
  <div><div class="d">Sun</div><div class="i">&#9728;</div><div class="h">60</div><div class="w">sunny</div></div>
</div>
<div class="line"><span class="lbl r">The turn</span> Rain arrives around 8 p.m. Thursday, then showers and thunderstorms Friday, with a half to three-quarters of an inch of rain. Friday night drops to 35 here and 32 in Scottsville. <span class="lbl t">Outdoor window</span> Thursday until dinner, and Sunday, sunny and 60.</div>
''')
S('<div class="line"><b>New numbers Thursday.</b>','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','''<div class="line"><b>Report day.</b> The state's volunteer spotters file this afternoon, and the county numbers run here tomorrow. North Tonawanda usually peaks in the last week of October.</div>
''')
# Sky
S('<div class="sky">','<div class="stars">','''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 0 50 96 A32 46 0 0 1 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>A waxing crescent</b>, 16 percent lit, in Sagittarius, sets at 8:25 p.m.<br>
<span class="lbl t">Sun</span> 7:28a &ndash; 6:34p &middot; <b>11h 6m</b><br>
<span class="lbl t">Hunter's Moon</span> Mon, Oct 26</div></div>
<div class="line"><span class="lbl r">Tonight</span> If the clouds part, the crescent hangs in the southwest after sunset and sets at 8:25, a little fuller than last night. Saturn is up in the east-southeast after dark. Today runs almost three minutes shorter than yesterday.</div>
''')
S('<div class="stars">','<div style="font-family','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>The moon in Sagittarius trines Saturn in your sign</b>. Fire signs in step. Plan the thing you keep putting off. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>Venus squares Pluto</b>. A strong feeling deserves a second look before it gets a reply. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>The moon trines Mars in your sign</b>. Energy and good humor show up together. Use both. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>Mercury, your ruler, sits deep in Scorpio</b>. Ask the question under the question. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Venus in your sign squares Mars</b>. Charm and impatience in the same room. Pick charm. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
# Barograph
S('<div class="baro-top">','<h2 class="sec"><span class="o">&#10038;</span>The Ledger',baro+'''<div class="line"><span class="lbl r">Big swing coming</span> 29.90 and rising, up about a tenth of an inch since yesterday morning. The forecast has it climbing another third of an inch by Thursday morning, then dropping about six-tenths of an inch between Thursday morning and Friday morning as the storm comes through.</div>
<div class="line"><span class="lbl t">The log</span> Days since the last one: Garret 8, Dad 8, Mom 5. October so far: one each.</div>
''')
# Ledger
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">Colleges with no application fee</div><div class="big">140</div></div>
<div class="txt">Governor Hochul says 140 New York colleges will waive application fees: all of SUNY, plus private colleges that just signed on. Applying to ten now costs the same as applying to one.</div></div>
''')
# National Wire
S('<div class="wire"><div class="num">1</div><div><h3>Agents Search','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>Pope Leo Has Lung Cancer</h3><p>Surgeons removed the lower lobe of the pope's right lung Tuesday in a roughly 90-minute operation, and tests confirmed lung cancer, the Vatican said. It called the surgery successful, with no complications, and said he had a peaceful night.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Judge Blocks White House Press Ban</h3><p>A federal judge ruled late Tuesday that the White House can't shut out CNN, MS NOW and Politico reporters over their coverage, at least until the case goes to trial. Judge Timothy Kelly said pulling their passes likely violated their First and Fifth Amendment rights.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Guilfoyle Out as Ambassador</h3><p>The White House asked Kimberly Guilfoyle to resign as ambassador to Greece on Tuesday, and she is stepping aside. Reports said she offered access to officials in exchange for help paying off her debt; she has denied the misconduct allegations.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>40 Years for Tupac's Killing</h3><p>Duane Davis, a former gang leader, was sentenced to 40 years for orchestrating the drive-by shooting that killed Tupac Shakur. A jury found him guilty last month; the rap star was shot in Las Vegas in 1996.</p></div></div>
''')
S('<div class="ballot">','<h2 class="sec"><span class="o">&#9962;</span>The Home Wire','''<div class="ballot">&#9745; The Ballot &middot; <b>20 days</b> to Election Day &middot; early voting opens in 10 days, Oct 24, the same day registration closes &middot; Hochul and Blakeman met last night in their only debate, sparring over immigration, the cost of living and Trump</div>
''')
# Home Wire
S('<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Wegmans','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Orangutans Coming Back to the Zoo</h3><p>Monroe County lawmakers voted 22&ndash;4 Tuesday night to advance the Seneca Park Zoo's expansion, which adds a new tropical exhibit. It brings orangutans and lemurs a step closer to returning.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>North Tonawanda &middot; A 4.25% Tax Increase Proposed</h3><p>The city's proposed 2027 budget carries a 4.25 percent property tax increase. That means higher tax bills again next year, the <i>Niagara Gazette</i> reports.</p></div></div>
''')
# Marquee
S('<div class="wire"><div class="num">1</div><div><h3>RJ Mitte','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron','''<div class="wire"><div class="num">1</div><div><h3><i>Girls</i> Is Coming Back</h3><p>Lena Dunham's HBO series returns for a limited run, ten years after its finale. HBO says the reunion takes on the milestone of turning forty.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Led Zeppelin Said Yes to <i>Narnia</i></h3><p>Robert Plant and Jimmy Page gave Greta Gerwig their blessing to use "Stairway to Heaven" in the first trailer for <i>Narnia: The Magician's Nephew</i>. Billboard has the story of how she asked.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>First Reactions to <i>Clayface</i></h3><p>Early reactions are in for DC Studios' body-horror film, co-written by Mike Flanagan and directed by James Watkins. It opens in theaters Oct. 23.</p></div></div>
''')
# Gridiron
S('<div class="touch-head">Bills 37, Rams 34 (OT)</div>','<table class="tbl">','''<div class="touch-head">Sunday: Vegas and Foxborough</div>
<div class="line"><b>Bills</b> &middot; At Las Vegas Sunday, 4:25. The Raiders are 3&ndash;2 and coming off a 45&ndash;17 loss in New England. Tackle Spencer Brown left Monday's overtime win with a back injury; the week's first practice report comes out today. After Vegas comes the bye.</div>
<div class="line"><b>Jets</b> &middot; At New England Sunday, 1:00. The defense that held Cleveland to 12 points last Sunday draws a 3&ndash;2 Patriots team that scored 45 the same afternoon.</div>
<div class="pnote"><b>The Sunday Tax &middot; Week 6.</b> Picks at <a href="https://tally.so/r/RGOakJ">tally.so/r/RGOakJ</a>; standings at <a href="https://benthambulletin.github.io/pool/">benthambulletin.github.io/pool</a>. $5 a week, straight-up winners, the pot to the best record. Anyone with the link can play. Sheets lock at each kickoff; first game Thu 8:15 p.m., Seahawks at Denver.</div>
''')
# Chase
S('<div class="touch-head">Four to Go</div>','<h2 class="sec"><span class="o">&#9790;</span>On This Day','''<div class="touch-head">Phoenix Next</div>
<div class="line">Sunday's race at Phoenix opens the last four. Kyle Larson leads, with Denny Hamlin 49 points back, Christopher Bell 51 and Chase Briscoe 65; the most points after Homestead on Nov. 8 takes the title. Daniel Su&aacute;rez, 14th in the standings, will stay in Spire Motorsports' #7 Chevrolet next year under a contract extension.</div>
''')
S('<div class="otd">','<h2 class="sec"><span class="o">&#10023;</span>Question of the Day','''<div class="otd"><b>October 14, 1947</b> &mdash; Chuck Yeager flew the Bell X-1 faster than the speed of sound over California's Mojave Desert, the first pilot to do it. He had named the plane <i>Glamorous Glennis</i>, after his wife.</div>
''')
S('<div class="qotd">I have plenty','<div class="dbl">','''<div class="qotd">I wear a carved grin, keep a candle for a heart, and only work one night a year. What am I? <i>Answer below the fold.</i></div>
''')
R('<b>Question of the Day:</b> A corn maze.','<b>Question of the Day:</b> A jack-o\'-lantern.')
S('<div class="s">Forecast per NWS','<div class="sig">','''<div class="s">Forecast per NWS Buffalo &middot; barometer forecast via Open-Meteo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; sky computed for 14120 &middot; headlines via NPR, CBS, BBC, PBS, AP via WIVB, Niagara Gazette, Rochester First, Billboard, Hollywood Reporter &middot; Bills injury news via Yahoo Sports &middot; Su&aacute;rez news via Speedway Media &middot; scores, standings and NASCAR points via Sportradar</div>
''')
d['no']=112; d['date']='2026-10-14'
d['headline']="Pope has lung cancer · Big pressure drop Friday · Kaylani in the Group Chat · Phoenix next"
d['body_html']=b; d['plate_path']=None; d['plate_caption']=None
json.dump(d,open('edition-2026-10-14.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-14.json','w'),ensure_ascii=False,indent=1)
p=json.load(open('site/data/pressure.json')); p=[x for x in p if x['date']!='2026-10-14']
p.append({'date':'2026-10-14','in':29.90,'mb':1012.6,'station':'KIAG','time':'06:53 EDT'}); json.dump(p,open('site/data/pressure.json','w'),indent=1)
s=json.load(open('site/data/inbox/seen.json'))
if 'Nqvy4zB' not in s['seen']: s['seen'].append('Nqvy4zB')
json.dump(s,open('site/data/inbox/seen.json','w'),indent=1)
json.dump([],open('site/data/inbox/photo-queue.json','w'))
print('built')
