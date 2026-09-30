import json
d=json.load(open('edition-2026-09-29.json')); b=d['body_html']
baro=open('/tmp/claude-0/-home-claude/001a10af-13f9-5479-8fec-28bf86d9c496/scratchpad/baro98.html').read(); baro=baro[:baro.index('<!--')]
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
H=lambda o,t:f'<h2 class="sec"><span class="o">{o}</span>{t}<span class="o">{o}</span></h2>'
R('No. 97','No. 98')
R('Tuesday &middot; September 29 &middot; 2026','Wednesday &middot; September 30 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">74&deg;</div><div class="k">Mostly cloudy, mild</div></div>
  <div class="tile good"><div class="v">30.05&#8243; &#8212;</div><div class="k">Holding steady</div></div>
  <div class="tile urg"><div class="v">34</div><div class="k">Days to Election Day</div></div>
</div>
''')
R('Last light over Port Bay, Saturday evening.','Luka, in the space-print sleep sack, winding down Tuesday night.')
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>Luka has the cover</b>, zipped into the planets and rockets and almost ready for bed. One more mild day, then the rain arrives: a few showers late tonight, the real soaking Thursday night and Friday, and a sunny, cooler weekend behind it. Last day of September.
''')
S('<div class="wx">','<div class="towns">','''<div class="wx"><div class="bigtemp">74<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">One more warm one before the rain</span>
Low <b>63&deg;</b> &middot; Southwest 3&ndash;10<br>Rain <b>50%</b> after midnight, light</div></div>
''')
S('<div class="towns">','<div class="strip5">','''<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">50<sup>&deg;</sup></div><div class="d">Fog &middot; high 74&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">61<sup>&deg;</sup></div><div class="d">Clear &middot; high 73&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">54<sup>&deg;</sup></div><div class="d">Mostly cloudy &middot; high 76&deg;</div></div>
</div>
''')
S('<div class="strip5">','<div class="line"><span class="lbl t">The rain</span>','''<div class="strip5">
  <div><div class="d">Wed</div><div class="i">&#9729;</div><div class="h">74</div><div class="w">mostly cloudy</div></div>
  <div><div class="d">Thu</div><div class="i">&#127782;</div><div class="h">74</div><div class="w">rain at night</div></div>
  <div><div class="d">Fri</div><div class="i">&#127783;</div><div class="h">68</div><div class="w">rain</div></div>
  <div><div class="d">Sat</div><div class="i">&#9728;</div><div class="h">65</div><div class="w">sunny</div></div>
  <div><div class="d">Sun</div><div class="i">&#9728;</div><div class="h">67</div><div class="w">mostly sunny</div></div>
</div>
''')
S('<div class="line"><span class="lbl t">The rain</span>','<h2 class="sec"><span class="o">&#127810;</span>The Turning','''<div class="line"><span class="lbl t">The week turns</span> The forecast got wetter overnight: showers Thursday morning, then 90% Thursday night and all of Friday. Friday night drops to 45, Saturday night 43, the coldest nights yet this fall. Sunny for the Bills game Sunday. <span class="lbl t">Outdoor window</span> Today.</div>
''')
S('<div class="line"><b>Tomorrow afternoon is the next foliage report.</b>','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','''<div class="line"><b>The foliage report comes out this afternoon.</b> Tomorrow's paper carries the three counties' numbers.</div>
''')
S('<div class="sky">','<div class="stars">','''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 1 50 96 A26 46 0 0 1 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>Eighty-one percent</b> and waning, rising at 8:53 tonight on its last hours in Taurus.<br>
<span class="lbl t">Sun</span> 7:11a &ndash; 6:58p &middot; <b>11h 47m</b><br>
<span class="lbl t">Last quarter</span> Sat, Oct 3 &middot; <span class="lbl t">Next new moon</span> Sat, Oct 10</div></div>
<div class="line"><span class="lbl r">Tonight</span> The sun sets before seven for the first time since spring. <b>Saturn</b> is up at 7:12, <b>Mars</b> at 1:26 a.m., <b>Jupiter</b> at 3:01.</div>
''')
S('<div class="stars">','<div style="font-family:','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>The moon sextiles Mars today</b>, an easy link between feeling and doing. Whatever you have been putting off moves more easily than it did on Monday. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>The moon is at the last degree of Taurus</b>, steady ground before it turns restless in Gemini tonight. Get the practical thing done while the day is still calm. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Mercury, just into Scorpio, squares Mars in your sign</b>. Someone will say exactly what they think. Hear the useful part and let the tone go. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>Your ruler, Mercury, crossed into Scorpio this morning</b> and squares Pluto. Conversations go deeper than planned. Ask the second question. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Mercury is in your sign now, beside Venus.</b> For the next three weeks words come easier and land better. Say the thing you have been rehearsing. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
S('<div class="baro-top">','<div class="line"><span class="lbl t">Climbing back</span>',baro)
S('<div class="line"><span class="lbl t">Climbing back</span>','<h2 class="sec"><span class="o">&#10038;</span>The Ledger','''<div class="line"><span class="lbl t">Calm before the rain</span> 30.05 and flat overnight, about as gentle as the chart gets. The rain Thursday night comes with falling pressure, so tomorrow's paper will watch the drop.</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">Inches of rain due Thursday night and Friday</div><div class="big">&frac34;</div></div>
<div class="txt">A half to three-quarters of an inch, by the Weather Service's count. Enough to soak the leaves and settle the dust.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>OpenAI Pulls','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>U.S. Forces Leave Iraq</h3><p>The Pentagon says American troops and equipment are out, 23 years after the invasion, and has declared the anti-ISIS mission over.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>A.I. Companies Sign a Voluntary Accord</h3><p>The president said leaders of the major A.I. firms agreed to "self-police," with internal and outside reviews of new systems. It is not a law.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>FBI Hit by a Data Breach</h3><p>Hackers got into the bureau's job-applicant portal. The FBI calls the breach massive and says it is going after those responsible.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>Polo Floods the Southwest</h3><p>The hurricane's remains flooded roads, and small New Mexico towns evacuated over fears a dam could fail.</p></div></div>
''')
R('<b>35 days</b>','<b>34 days</b>')
S('<h2 class="sec"><span class="o">&#9962;</span>The Home Wire','<h2 class="sec"><span class="o">&#9733;</span>The Marquee',H('&#9962;','The Home Wire')+'''
<div class="wire"><div class="num">1</div><div><h3>North Tonawanda &middot; LumberJack's Lease Bought Out</h3><p>The city bought out LumberJack's Patio Grill's lease on its River Road spot and is looking for a new restaurant to open there by next summer.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Buffalo &middot; A Two-Year Pause on Data Centers?</h3><p>City lawmakers moved a step toward a two-year ban on new data centers, double the state's one-year pause already in effect. Not final yet.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Henrietta &middot; Federal Money for Four Firefighters</h3><p>A grant of nearly $1 million will add four firefighters as volunteer ranks thin; eleven Rochester-area departments share $2.5 million.</p></div></div>
''')
S('<h2 class="sec"><span class="o">&#9733;</span>The Marquee','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron',H('&#9733;','The Marquee')+'''
<div class="wire"><div class="num">1</div><div><h3>Backpack Wins Fat Bear Week</h3><p>Bear 89, "Backpack," beat 910 in the final vote at Alaska's Katmai National Park, the internet's favorite contest for the chunkiest bear before winter.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Hanson Hits the End on <i>DWTS</i></h3><p>Taylor Hanson was voted off <i>Dancing With the Stars</i> after the show's yacht rock night.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Tom Cruise's Big Gamble</h3><p><i>Digger</i>, his film with Oscar winner Alejandro G. I&ntilde;&aacute;rritu, screened at the Academy Museum, where Cruise called it his riskiest role yet.</p></div></div>
''')
S('<div class="touch-head">Five Days to Sunday</div>','<table class="tbl">','''<div class="touch-head">Four Days to Sunday</div>
<div class="line"><b>Bills</b> &middot; Christian Benford left the Chargers game with a toe injury and was in a walking boot afterward; watch Wednesday's practice report. The Patriots come in short-handed, with A.J. Brown on injured reserve and three other starters hurt.</div>
<div class="line"><b>Jets</b> &middot; Bears quarterback Caleb Williams is out three to four weeks with a hamstring injury, so Case Keenum starts Sunday. He just beat the Eagles, which is why the line has come down from Chicago by 8&frac12; to 3&frac12;.</div>
''')
S('<div class="touch-head">Larson Up 26</div>','<div class="cards">','''<div class="touch-head">Four Days to Las Vegas</div>
<div class="line">Sunday evening's South Point 400 is race six of ten. Larson carries 26 points over Hamlin into it.</div>
''')
S('<div class="otd">','<h2 class="sec"><span class="o">&#10023;</span>Question','''<div class="otd"><b>September 30, 1927</b> &mdash; Babe Ruth hit his 60th home run of the season at Yankee Stadium, a record that stood for 34 years. Baseball's postseason opened this week; the Braves took the first wild-card game last night on a three-run homer in the eighth.</div>
''')
R('What can you catch but not throw?','What has hands but cannot clap?')
R('<b>Question of the Day:</b> A cold.','<b>Question of the Day:</b> A clock.')
d.update(date='2026-09-30',no=98,body_html=b,plate_path='/home/claude/plate98.jpg',plate_caption='Luka, in the space-print sleep sack, winding down Tuesday night',headline="Luka at bedtime · Rain Thursday night · U.S. leaves Iraq · Backpack wins Fat Bear Week")
json.dump(d,open('site/data/edition-2026-09-30.json','w'),indent=1); json.dump(d,open('edition-2026-09-30.json','w'),indent=1)
p=json.load(open('site/data/pressure.json'))
if p[-1]['date']!='2026-09-30': p.append({"date":"2026-09-30","in":30.05,"mb":1017.6,"station":"KIAG","time":"06:31 EDT"})
json.dump(p,open('site/data/pressure.json','w'),indent=1)
print('ok')
