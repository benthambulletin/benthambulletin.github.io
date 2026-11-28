import json, sys, shutil, os
sys.path.insert(0,'/home/claude'); sys.path.insert(0,'/home/claude/site/tools')
from curve import curve
from erie_graphic import erie_block
S='/home/claude/site/'
if os.path.exists(S+'spool/next/plate.jpg'): shutil.copy(S+'spool/next/plate.jpg','/home/claude/plate157.jpg')
for fn in ('groupchat','otd'):
    if os.path.exists(S+f'spool/saturday/{fn}.html'): shutil.copy(S+f'spool/saturday/{fn}.html',f'/home/claude/{fn}157.html')
gc = open('/home/claude/groupchat157.html').read(); otd = open('/home/claude/otd157.html').read()
y = json.load(open('/home/claude/edition-2026-11-27.json'))['body_html']
f = json.load(open(S+'data/forecast.json'))
def R(s, old, new):
    assert s.count(old) == 1, old[:60]
    return s.replace(old, new)
pre = y[:y.find('<div class="part">')]
pre = R(pre, 'No. 156', 'No. 157')
pre = R(pre, 'Friday &middot; November 27 &middot; 2026', 'Saturday &middot; November 28 &middot; 2026')
pre = R(pre, '<div class="v">47&deg;</div><div class="k">Showers</div>', '<div class="v">46&deg;</div><div class="k">Showers, Windy</div>')
pre = R(pre, '<div class="v">4:43</div><div class="k">Sunset &middot; 1 min less</div>', '<div class="v">4:43</div><div class="k">Sunset</div>')
pre = R(pre, '<div class="tile urg"><div class="v">9</div><div class="k">Days to Bills&ndash;Patriots</div></div>', '<div class="tile urg"><div class="v">8</div><div class="k">Days to Bills&ndash;Patriots</div></div>')
pre = R(pre, 'alt="A young boy at the table with a slice of pumpkin pie and whipped cream on his chin"', 'alt="A young boy in pajamas coloring at a small table"')
s0 = pre.find('<div class="plate-sub">'); s1 = pre.find('</div>', s0)
pre = pre[:s0] + '<div class="plate-sub">Black Friday, indoor division.' + pre[s1:]
BYLINE = '<div style="display:flex;gap:.8rem;align-items:center;margin:.5rem 0 .7rem"><img src="/assets/margo.jpg" alt="Margo Bentham, in ink" style="width:86px;height:86px;flex:none;border-radius:4px;border:1px solid var(--rule,#d3b88f)"><div><div style="font-family:\'Playfair Display\',Georgia,serif;font-weight:700;font-size:1.2rem;line-height:1.1">Margo Bentham</div><div style="font-family:Archivo,Arial,sans-serif;font-size:.6rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--teal,#2f5e3e);margin-top:.2rem">Editor-in-chief &middot; lead meteorologist</div><div style="font-style:italic;font-size:.85rem;color:var(--soft,#664a2c);margin-top:.3rem">Reads the group chat. All of it.</div><div style="font-family:Archivo,Arial,sans-serif;font-size:.62rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;margin-top:.35rem"><a href="https://tally.so/r/EqxJpo">Ask Margo &rarr;</a></div></div></div>'
P='https://tally.so/r/gbGYaN?poll=2026-11-28&amp;pick='
btn='display:block;border:1px solid var(--rule,#d3b88f);border-radius:8px;padding:.5rem .8rem;margin:.35rem 0;text-decoration:none;color:inherit;background:rgba(255,255,255,.35)'
poll = f'''<h2 class="sec">Today&rsquo;s Poll</h2>
<p style="font-family:'Playfair Display',Georgia,serif;font-weight:700;font-size:1.15rem;margin:.2rem 0 .4rem">Best leftover?</p>
<a href="{P}A" style="{btn}"><b>A</b> &nbsp;Turkey sandwich</a>
<a href="{P}B" style="{btn}"><b>B</b> &nbsp;Stuffing</a>
<a href="{P}C" style="{btn}"><b>C</b> &nbsp;Pie for breakfast</a>
<a href="{P}D" style="{btn}"><b>D</b> &nbsp;Cold mashed potatoes</a>
<p style="font-size:.85rem;font-style:italic;margin-top:.4rem">Tap one, pick your name, done. Results and Margo&rsquo;s verdict tomorrow.</p>
'''
news = '''<div class="part"><span>The News</span></div>
<h2 class="sec">The National Wire</h2>
<div class="wire lead"><div><span class="kick">The Lead</span><h3>Andrea Stewart-Cousins, Senate Leader, Dies at 76</h3><p>Andrea Stewart-Cousins, the Yonkers Democrat who led the New York State Senate and was the first Black woman to lead a legislative conference in Albany, died unexpectedly on Friday, WXXI reports. She was 76, and the cause wasn&rsquo;t immediately clear.</p><p>She held one of the three most powerful posts in state government and had a hand in all the major legislation passed since Democrats took the Senate in 2018, WXXI reports. Senate Democrats had voted to give her another two-year term as majority leader less than two weeks ago.</p><p>Senate Democrats must now pick a new leader by majority vote before the 2027 session begins, Rochester First reports, and her Westchester seat will need a special election.</p></div></div>
<div class="wire"><div><span class="num">2</span><h3>Two Jets Clip Wings at Reagan National</h3><p>Two American Airlines Boeing 737s clipped wings while taxiing for departure at Reagan National Airport outside Washington on Friday evening; no one was hurt, and the Federal Aviation Administration will investigate, the BBC reports. It&rsquo;s the same airport where 67 people died when a jetliner and an Army helicopter collided in January 2025.</p></div></div>
<div class="wire"><div><span class="num">3</span><h3>Blast Near a School in Afghanistan</h3><p>At least seven students were killed and 99 hurt Saturday morning in an explosion near a school in Asadabad, the capital of Kunar province, a Taliban government spokesman said, the BBC reports. Initial findings blame &ldquo;negligence and carelessness&rdquo; at an explosives depot belonging to nearby mining companies.</p></div></div>
<h2 class="sec">Family Today</h2>
<p>Black Friday, by the look of today&rsquo;s cover, was spent at the coloring table. The coloring got done.</p>
''' + gc + '''
<h2 class="sec">The Home Wire</h2>
<div class="wire"><div><span class="num">4</span><h3>Lancaster and Hamburg &middot; The Lights Are On</h3><p>Legendary Lights, nearly 400 decorated homes in Stony Brook, a Lancaster neighborhood (not the Long Island one), lit up Thanksgiving night and runs every night until New Year&rsquo;s Day; drive or walk through, WIVB and WGRZ report. The Festival of Lights at the Hamburg Fairgrounds opened Friday with more than 70 drive-through displays and runs through Dec. 30.</p></div></div>
<div class="wire"><div><span class="num">4</span><h3>Lewiston &middot; A Credit Union Moves In</h3><p>Ontario Shores Federal Credit Union plans to open its fifth location at 451 Center St. in Lewiston, the <i>Niagara Gazette</i> reports. &ldquo;We think it&rsquo;s a great opportunity for the credit union and the people of Lewiston,&rdquo; CEO Jeff Bell said, calling it a not-for-profit, community-based option.</p></div></div>
<div class="wire"><div><span class="num">5</span><h3>Buffalo &middot; UB Is Going to the MAC Title Game</h3><p>The University at Buffalo beat Akron 17&ndash;9 on Friday to clinch a spot in the Mid-American Conference championship game, WGRZ reports. Messiah Burch ran for 130 yards and a touchdown on 24 carries.</p></div></div>
<div class="wire"><div><span class="num">6</span><h3>Rochester &middot; Cruel Summer Comes Home</h3><p>Cruel Summer, a Rochester-based Taylor Swift tribute band that has spent the year selling out venues across the Northeast, is coming home for its annual Swift birthday show, Rochester First reports. It plays Saturday, Dec. 12, at the Theater at Innovative Field.</p></div></div>
<h2 class="sec">The Marquee</h2>
<div class="wire"><div><span class="num">7</span><h3>WWE&rsquo;s Bronson Reed Dies at 38</h3><p>Jermaine Haley, the Australian wrestler known in WWE as Bronson Reed, died Friday of medical complications, WWE said, the Hollywood Reporter reports; he leaves a pregnant wife, Paige, and a daughter. Us Weekly reports he had suffered broken ribs and a lacerated kidney when he was thrown off the stage at WWE&rsquo;s Crown Jewel event in Saudi Arabia on Nov. 7.</p></div></div>
<div class="wire"><div><span class="num">8</span><h3>The Killers&rsquo; Guitarist Survived a Major Stroke</h3><p>Dave Keuning, 50, says he had a major stroke two weeks ago, went straight into surgery thanks to his wife acting fast, and that doctors gave him a 40% chance of survival, Billboard reports. &ldquo;By some miracle I am fine,&rdquo; he wrote, adding that the first hour after a stroke is critical.</p></div></div>
<div class="wire"><div><span class="num">9</span><h3>Bob Newhart Couldn&rsquo;t Afford to Quit</h3><p>Michael Seth Starr&rsquo;s biography of Bob Newhart says he once tried to quit &ldquo;The Bob Newhart Show&rdquo; and backed down when CBS threatened a $6 million lawsuit, Page Six reports. &ldquo;I don&rsquo;t have $6 million,&rdquo; he said later. &ldquo;And my wife wouldn&rsquo;t lend me any of her money.&rdquo;</p></div></div>
''' + poll + '''
<h2 class="sec">The Gridiron</h2>
<div class="wire"><div><h3>Bills: A New Road to the No. 1 Seed</h3><p>With Denver and Kansas City both losing this week, the Bills have a second path to the AFC&rsquo;s top seed, Buffalo Rumblings reports: win their three AFC East games, against the Patriots, Jets and Dolphins, and then either beat the Broncos on Christmas Day or beat both the Packers and the Bears in mid-December. Next up: at New England, Sunday, Dec. 6, at 4:25.</p></div></div>
<div class="wire"><div><h3>Jets: Payback in Miami?</h3><p>The Jets play at Miami Sunday at 1:00, looking for their first AFC East win under coach Aaron Glenn, Gang Green Nation reports. The Dolphins have won just once this season, 28&ndash;25 over the Jets in Week 7, and the Jets haven&rsquo;t won in Miami since 2014.</p></div></div>
'''
hourly = f['towns']['North Tonawanda']['hourly']
crv = curve(hourly, 7*60+23, 16*60+43)
erie = erie_block(json.load(open(S+'data/climate.json')), 51, 'Friday')
alm = '''<div class="part"><span>The Almanac</span></div>
<h2 class="sec">The Weather Glass</h2>
''' + BYLINE + '''
<p class="wlede">Showers till about noon, then a west wind with an attitude, gusting past 30. Gray, 46, and the lake is still sloshing. Tommy: best thing on Derek&rsquo;s table Thursday. One answer, no hedging, and the mushrooms are a cop-out. <a href="https://tally.so/r/rjxDpl">Answer here.</a></p>
<div class="touch-head" style="margin-top:1.1rem">Today</div>
<div class="wxrow">
  <div class="wxc"><div class="k">Tonight</div><div class="v">39&deg;</div><div class="s">a few showers</div></div>
  <div class="wxc"><div class="k">Wind</div><div class="v">13&ndash;20</div><div class="s">mph, west; gusts 33</div></div>
  <div class="wxc"><div class="k">Showers</div><div class="v">70%</div><div class="s">before noon</div></div>
  <div class="wxc"><div class="k">Normal</div><div class="v">43&deg;</div><div class="s">for the date</div></div>
</div>
<div class="line"><span class="lbl t">Next 24 hours</span></div>''' + crv + '''
<div class="line"><span class="lbl t">Records</span> Buffalo&rsquo;s for the date: 72 in 1990; 11 in 1955. A year ago: 33 and 28, with a trace of snow.</div>
<div class="touch-head" style="margin-top:1.1rem">This week</div>
<div class="strip5">
  <div><div class="d">Sat</div><div class="i">&#127782;</div><div class="h">46</div><div class="w">showers a.m.</div></div>
  <div><div class="d">Sun</div><div class="i">&#127781;</div><div class="h">50</div><div class="w">showers later</div></div>
  <div><div class="d">Mon</div><div class="i">&#127783;</div><div class="h">44</div><div class="w">rain showers</div></div>
  <div><div class="d">Tue</div><div class="i">&#127780;</div><div class="h">41</div><div class="w">partly sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#127780;</div><div class="h">49</div><div class="w">partly sunny</div></div>
</div>
<div class="line"><span class="lbl t">Frost watch</span> Back below freezing Monday night, 28.</div>
<div class="touch-head" style="margin-top:1.1rem">Around us &middot; at dawn</div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">39<sup>&deg;</sup></div><div class="d">Cloudy<br>high 46&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">43<sup>&deg;</sup></div><div class="d">Cloudy<br>high 48&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">40<sup>&deg;</sup></div><div class="d">Cloudy<br>high 46&deg;</div></div>
</div>
<div class="towns lakes">
  <div class="town"><div class="n">Lake Erie</div><div class="t">51<sup>&deg;</sup></div><div class="d">off Buffalo, Friday</div></div>
  <div class="town"><div class="n">Lake Ontario</div><div class="t">53<sup>&deg;</sup></div><div class="d">off Rochester, Friday</div></div>
</div>
''' + erie + '''
<div class="line">The lake has flipped. Thursday&rsquo;s northeast wind shoved the water toward Toledo; now a west-southwest wind is pushing it back, and Buffalo&rsquo;s end ran about 1.8 feet above Toledo&rsquo;s Friday afternoon and evening. This morning it&rsquo;s still about 13 inches higher. That back-and-forth is a seiche: the lake rocking like water in a tipped bathtub.</div>
<div class="line" style="margin-top:.4rem"><span class="lbl t">Snow so far</span> since July 1, through Friday. Still zero.</div>
<div class="towns snow"><div class="town"><div class="n">North Tonawanda</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 5.8"</div></div><div class="town"><div class="n">Orchard Park</div><div class="t">n/a</div><div class="d">normal 7.8"</div></div><div class="town"><div class="n">Dunkirk</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 7.8"</div></div><div class="town"><div class="n">Scottsville</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 7.3"</div></div></div>
<h2 class="sec">The Almanac Sky</h2>
<div class="wxrow">
  <div class="wxc"><div class="k">Moon</div><svg class="moonmini" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#3a2a1c" opacity=".25"/><path d="M50 4 A46 46 0 0 0 50 96 A25.2 46 0 0 0 50 4Z" fill="#f4e5b4"/></svg><div class="s">77% lit</div></div>
  <div class="wxc"><div class="k">Sunrise</div><div class="v">7:23</div><div class="s">a.m.</div></div>
  <div class="wxc"><div class="k">Daylight</div><div class="v">9h 20m</div><div class="s">2 min less</div></div>
</div>
<p class="skynote"><b>Tonight:</b> the waning moon rises at 9:15 p.m. in Cancer and sets at 12:03 Sunday afternoon. Saturn is the evening&rsquo;s bright planet, highest in the south around 8; Jupiter rises around 10:45, Mars just after 11. Next new moon, December 8; next full, December 23.</p>
<div class="touch-head">The Stars &middot; for fun</div>
<div class="stars slim">
<div class="star"><span class="sgn">Aries</span> <span class="who">Kaylani, Luka</span><br>A warm moon on your side. Pick the movie tonight; nobody will fight you.</div>
<div class="star"><span class="sgn">Cancer</span> <span class="who">Gregg</span><br>Nothing in your corner today. Report the weather in the group chat anyway; it&rsquo;s your calling.</div>
<div class="star"><span class="sgn">Leo</span> <span class="who">Leah, Tommy</span><br>The moon is in your sign by the zodiac, whatever the stars behind it say. Tommy, answer Margo&rsquo;s question; Leah, vote in the poll.</div>
<div class="star"><span class="sgn">Virgo</span> <span class="who">Derek, Joanne</span><br>A quiet sky. The leftovers are yours to ration.</div>
<div class="star"><span class="sgn">Scorpio</span> <span class="who">Ariel, Claire, Garret</span><br>The moon is leaning on you. Sleep in again; it worked yesterday.</div>
</div>
<h2 class="sec">Coming Up</h2>
<div class="calbox"><div class="calrow"><div class="cd">Today</div><div>Macy&rsquo;s 100th parade, 8:30 a.m., NBC</div></div>
<div class="calrow"><div class="cd">Sun</div><div>Jets at Dolphins, 1:00</div></div>
<div class="calrow"><div class="cd">Dec. 6</div><div>Bills at Patriots, 4:25</div></div>
<div class="calnote">Migraine log: Garret&rsquo;s last was Wednesday; Joanne&rsquo;s, last Sunday. Five this month.</div>
</div>
''' + otd + '''
<h2 class="sec">Question of the Day</h2>
<div class="qotd">I&rsquo;m full of air, I&rsquo;m held down by ropes, and I only fly when the wind says so. What am I? <i>Answer below the fold.</i></div>
<div class="dbl"><div class="a"></div><div class="b"></div></div>
<div class="colo"><div class="s" style="margin-bottom:8px"><b>Question of the Day:</b> A parade balloon.</div>
<div class="s">Forecast, lake temperatures and radar per NWS Buffalo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; Lake Erie levels and wind per NOAA &middot; normals from NOAA &middot; sky computed for 14120 &middot; headlines via WXXI, Rochester First, the <i>Niagara Gazette</i>, the BBC, WIVB, WGRZ, the Hollywood Reporter, Us Weekly, Billboard, Page Six, Buffalo Rumblings, Gang Green Nation &middot; game times via Sportradar &middot; On This Day per the Grand Ole Opry and History.com &middot; snow and records via ACIS</div>
<div class="ask"><a href="https://tally.so/r/rjxDpl">Send something to the paper</a> &middot; <a href="https://tally.so/r/obWNYP">Log a migraine</a> &middot; <a href="https://tally.so/r/EqxJpo">Ask Margo</a> &middot; <a href="https://tally.so/r/gbGYaN">Today&rsquo;s Poll</a></div>
<div class="sig">&mdash; Margo</div><div class="orn">&#127809; &#127810; &#127809;</div></div>'''
body = pre + news + alm
ed = {'date':'2026-11-28','no':157,'body_html':body,'plate_path':'/home/claude/plate157.jpg','plate_caption':'Black Friday, indoor division.','headline':'Senate leader Stewart-Cousins dies · Bills’ new road to No. 1 · first Poll'}
for p in ['/home/claude/edition-2026-11-28.json', S+'data/edition-2026-11-28.json']:
    json.dump(ed, open(p,'w'), ensure_ascii=False)
print('ok', len(body), bool(erie))
