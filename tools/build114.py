import json
d=json.load(open('edition-2026-10-15.json')); b=d['body_html']
baro=open('/tmp/claude-0/-home-claude/001a10af-13f9-5479-8fec-28bf86d9c496/scratchpad/baro114.html').read(); baro=baro[:baro.index('<!--')].strip()+'\n'
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
R('No. 113','No. 114')
R('Thursday &middot; October 15 &middot; 2026','Friday &middot; October 16 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">68&deg;</div><div class="k">Rain, wind</div></div>
  <div class="tile"><div class="v">29.61&#8243; &#9650;</div><div class="k">Big climb tonight</div></div>
  <div class="tile urg"><div class="v">18</div><div class="k">Days to Election Day</div></div>
</div>
''')
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>The party is tomorrow.</b> Mostly sunny and 48 with a northwest breeze, and it drops to freezing after dark, so pack coats for the ride home. Claire's birthday is a week from today.
''')
S('<div class="wx">','<h2 class="sec"><span class="o">&#127810;</span>The Turning','''<div class="wx"><div class="bigtemp">68<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">Rain and wind today, the first frost tomorrow night</span>
Falling to the upper 50s this afternoon &middot; west 16&ndash;24, gusts to 39<br>Rain on and off, 90 percent, a quarter to half an inch; low 37 tonight</div></div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">70<sup>&deg;</sup></div><div class="d">Cloudy &middot; high 68&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">72<sup>&deg;</sup></div><div class="d">Cloudy &middot; high 69&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">64<sup>&deg;</sup></div><div class="d">Light rain &middot; high 70&deg;</div></div>
</div>
<div class="strip5">
  <div><div class="d">Fri</div><div class="i">&#127783;</div><div class="h">68</div><div class="w">rain, windy, falling temps</div></div>
  <div><div class="d">Sat</div><div class="i">&#127780;</div><div class="h">48</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Sun</div><div class="i">&#9728;</div><div class="h">60</div><div class="w">sunny</div></div>
  <div><div class="d">Mon</div><div class="i">&#9728;</div><div class="h">65</div><div class="w">sunny</div></div>
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">66</div><div class="w">sunny</div></div>
</div>
<div class="line"><span class="lbl r">Frost watch</span> Saturday night drops to 32 in North Tonawanda and 28 in Scottsville under clear skies; Dunkirk holds at 36. Scottsville could see a few wet snowflakes mixed with rain showers Saturday. <span class="lbl t">Outdoor window</span> Saturday afternoon, then Sunday through Tuesday, sunny and in the 60s.</div>
''')
S('<h2 class="sec"><span class="o">&#127810;</span>The Turning','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','''<h2 class="sec"><span class="o">&#127810;</span>The Turning<span class="o">&#127810;</span></h2>
<div class="line"><b>Still waiting on the county numbers.</b> Today's wind will pull down plenty of leaves either way; North Tonawanda usually peaks in the last week of October.</div>
''')
S('<div class="sky">','<div class="stars">','''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 0 50 96 A17 46 0 0 1 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>A waxing crescent</b>, 32 percent lit, in Capricorn, sets at 10:06 p.m.<br>
<span class="lbl t">Sun</span> 7:30a &ndash; 6:31p &middot; <b>11h 1m</b><br>
<span class="lbl t">First quarter</span> Sun, Oct 18 &middot; <span class="lbl t">Hunter's Moon</span> Mon, Oct 26</div></div>
<div class="line"><span class="lbl r">Tonight</span> Clouds hang on after the rain, so the moon is a long shot. Daylight slips under 11 hours tomorrow.</div>
''')
S('<div class="stars">','<div style="font-family','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>The moon squares Neptune in your sign</b>. A foggy day for decisions. Sleep on the big one. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>The moon enters Capricorn, opposite your sign</b>. Someone else's needs come first today. It evens out. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Mars in your sign trines Saturn, exact</b>. Drive with discipline behind it. Finish what you start. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>The Sun sextiles Jupiter</b>. A helpful word from an unexpected corner. Take it. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>The moon sextiles Venus in your sign</b>. Easy company and a kind word. Good night for a party. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
S('<div class="baro-top">','<h2 class="sec"><span class="o">&#10038;</span>The Ledger',baro+'''<div class="line"><span class="lbl r">Big swing coming</span> 29.61 and at the week's low, down about two-thirds of an inch since yesterday morning. The storm moves out and it climbs about three-quarters of an inch between this morning and Saturday morning, the steepest stretch this evening.</div>
<div class="line"><span class="lbl t">The log</span> Days since the last one: Garret 10, Dad 10, Mom 7. October so far: one each.</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">Dollar General to Foodlink</div><div class="big">$1.9M</div></div>
<div class="txt">Dollar General will give nearly $1.9 million in food and personal care goods to Rochester's Foodlink after a state investigation found it charged New York shoppers more than its posted prices.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Inflation','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>Shooting at an Oregon Elementary School</h3><p>Three children, ages 5, 8 and 11, and a teacher were killed Thursday at Silver Rail Elementary in Bend, Oregon; two others were critically wounded. Police say the 16-year-old suspect was shot and killed by a bystander.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Suspicious Letters to Officials</h3><p>The FBI and Postal Inspection Service are investigating letters sent to senators' offices and election offices in several states, some with an unidentified white powder. Oklahoma, Ohio and Louisiana confirmed they were targeted.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Brewers Sweep Into the World Series</h3><p>Milwaukee finished a four-game sweep of the two-time defending champion Dodgers on Thursday. It is the Brewers' first World Series since 1982.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>Barn Owls on the Upper West Side</h3><p>A family of barn owls has nested in a water tower atop a building near Central Park. Manhattan has taken them in like celebrities.</p></div></div>
''')
S('<div class="ballot">','<h2 class="sec"><span class="o">&#9962;</span>The Home Wire','''<div class="ballot">&#9745; The Ballot &middot; <b>18 days</b> to Election Day &middot; early voting opens in 8 days, Oct 24, the same day registration closes &middot; every race: <a href="https://benthambulletin.github.io/election/">benthambulletin.github.io/election</a></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Airport','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Banana Ball Is Coming</h3><p>The Banana Ball Championship League will play at ESL Ballpark in July 2027, the Loco Beach Coconuts against the Texas Tailgaters. Buffalo gets its own visit in June.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Dunkirk &middot; Democrats Look for Candidates</h3><p>The Dunkirk Democratic Committee is taking letters of interest for city offices in 2027, including mayor and the Common Council. It is the first step toward next year's local ballot.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Fredonia &middot; Volleyball Sweep</h3><p>Londyn Wilmot had 18 kills and six blocks as Fredonia swept Olean 25&ndash;10, 25&ndash;15, 25&ndash;13 on Thursday. Alyse Bugaj added 26 assists.</p></div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3><i>The Lowdown</i>','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron','''<div class="wire"><div class="num">1</div><div><h3>Apatow on Norm Macdonald</h3><p>Judd Apatow's Netflix documentary <i>Norm: The Tale of Norm Macdonald</i> is out, built from archive footage instead of talking heads. It covers his <i>SNL</i> firing and how he kept his cancer diagnosis private.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3><i>Street Fighter</i> Opens</h3><p>The video-game movie took in about $4 million from Thursday previews. Box office trackers expect an opening weekend above $30 million.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Kylie Joins <i>Bad Fairies</i></h3><p>Kylie Minogue, Jonathan Groff and Catherine Tate have joined the voice cast of <i>Bad Fairies</i>. Cynthia Erivo leads the animated film.</p></div></div>
''')
S('<div class="touch-head">Rousseau Gets His Due</div>','<table class="tbl">','''<div class="touch-head">A Sunday Doubleheader</div>
<div class="line"><b>Bills</b> &middot; At Las Vegas Sunday, 4:25. This week Jim Kelly paid a surprise visit to former News 8 sports anchor John Kucko, who is fighting brain cancer, two old Rochester faces with cancer fights in common.</div>
<div class="line"><b>Jets</b> &middot; At New England Sunday, 1:00, so the family's two games run back to back. Thursday night, Denver beat Seattle 17&ndash;14.</div>
''')
S('<div class="touch-head">Blaney\'s Track</div>','<h2 class="sec"><span class="o">&#9790;</span>On This Day','''<div class="touch-head">Phoenix Sunday</div>
<div class="line">The first of the last four races goes off Sunday at 3 p.m. on USA. Kyle Larson leads Denny Hamlin by 49 points, Christopher Bell by 51 and Chase Briscoe by 65; the title goes to whoever has the most points after Homestead on Nov. 8.</div>
''')
S('<div class="otd">','<h2 class="sec"><span class="o">&#10023;</span>Question of the Day','''<div class="otd"><b>October 16, 1923</b> &mdash; Walt and Roy Disney signed their first contract to make animated films, the date the company counts as its founding.</div>
''')
S('<div class="qotd">The more of me you rake','<div class="dbl">','''<div class="qotd">I have plenty of ears but can't hear a thing, and every October people pay to get lost in me. What am I? <i>Answer below the fold.</i></div>
''')
R("<b>Question of the Day:</b> Fallen leaves.","<b>Question of the Day:</b> A cornfield, cut into a corn maze.")
S('<div class="s">Forecast per NWS','<div class="sig">','''<div class="s">Forecast per NWS Buffalo &middot; barometer forecast via Open-Meteo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; sky computed for 14120 &middot; headlines via CBS, NPR, BBC, PBS, Rochester First, WKBW, Dunkirk Observer, Hollywood Reporter, Variety, Deadline &middot; scores, standings and NASCAR points via Sportradar</div>
''')
d['no']=114; d['date']='2026-10-16'
d['headline']="Oregon school shooting · Brewers to the World Series · Frost Saturday night · Party tomorrow"
d['body_html']=b; d['plate_path']=None; d['plate_caption']=None
json.dump(d,open('edition-2026-10-16.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-16.json','w'),ensure_ascii=False,indent=1)
p=json.load(open('site/data/pressure.json')); p=[x for x in p if x['date']!='2026-10-16']
p.append({'date':'2026-10-16','in':29.61,'mb':1002.7,'station':'KIAG','time':'06:53 EDT'}); json.dump(p,open('site/data/pressure.json','w'),indent=1)
m=json.load(open('site/data/migraines.json')); m['updated']='2026-10-16'; json.dump(m,open('site/data/migraines.json','w'),indent=1)
print('built')
