import json, sys, shutil
sys.path.insert(0,'/home/claude'); sys.path.insert(0,'/home/claude/site/tools')
from curve import curve
from erie_graphic import erie_block
S='/home/claude/site/'
shutil.copy(S+'spool/next/plate.jpg','/home/claude/plate156.jpg') if __import__('os').path.exists(S+'spool/next/plate.jpg') else None
y = json.load(open('/home/claude/edition-2026-11-26.json'))['body_html']
f = json.load(open(S+'data/forecast.json'))
def R(s, old, new):
    assert s.count(old) == 1, old[:60]
    return s.replace(old, new)
pre = y[:y.find('<div class="part">')]
pre = R(pre, 'No. 155', 'No. 156')
pre = R(pre, 'Thursday &middot; November 26 &middot; 2026', 'Friday &middot; November 27 &middot; 2026')
pre = R(pre, '<div class="v">42&deg;</div><div class="k">Rain Later</div>', '<div class="v">47&deg;</div><div class="k">Showers</div>')
pre = R(pre, '<div class="v">4:44</div><div class="k">Sunset</div>', '<div class="v">4:43</div><div class="k">Sunset &middot; 1 min less</div>')
pre = R(pre, '<div class="tile urg"><div class="v">Today</div><div class="k">Thanksgiving</div></div>', '<div class="tile urg"><div class="v">9</div><div class="k">Days to Bills&ndash;Patriots</div></div>')
pre = R(pre, 'alt="Family members together at the 2019 Turkey Trot, Briar second from right"', 'alt="A young boy at the table with a slice of pumpkin pie and whipped cream on his chin"')
s0 = pre.find('<div class="plate-sub">'); s1 = pre.find('</div>', s0)
pre = pre[:s0] + '<div class="plate-sub">Thanksgiving, by the slice.' + pre[s1:]

BYLINE = '<div style="display:flex;gap:.8rem;align-items:center;margin:.5rem 0 .7rem"><img src="/assets/margo.jpg" alt="Margo Bentham, in ink" style="width:86px;height:86px;flex:none;border-radius:4px;border:1px solid var(--rule,#d3b88f)"><div><div style="font-family:\'Playfair Display\',Georgia,serif;font-weight:700;font-size:1.2rem;line-height:1.1">Margo Bentham</div><div style="font-family:Archivo,Arial,sans-serif;font-size:.6rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--teal,#2f5e3e);margin-top:.2rem">Editor-in-chief &middot; lead meteorologist</div><div style="font-style:italic;font-size:.85rem;color:var(--soft,#664a2c);margin-top:.3rem">Has never once been seen at the office.</div><div style="font-family:Archivo,Arial,sans-serif;font-size:.62rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;margin-top:.35rem"><a href="https://tally.so/r/EqxJpo">Ask Margo &rarr;</a></div></div></div>'
otd = open('/home/claude/otd156.html').read()
open('/home/claude/otd156.html','w').write(otd)

news = '''<div class="part"><span>The News</span></div>
<h2 class="sec">The National Wire</h2>
<div class="wire"><div><span class="num">1</span><h3>Thanksgiving Storm Knocks Out Power to 800,000</h3><p>More than 800,000 customers were without power Thursday night across the Midwest and Northeast, more than 170,000 each in Pennsylvania and New Jersey, as a Thanksgiving storm brought torrential rain, high winds and flooding, CBS reports. More than 2,500 flights were delayed and more than 460 canceled, according to FlightAware; New Jersey was under a state of emergency.</p></div></div>
<div class="wire"><div><span class="num">2</span><h3>Strobe Talbott Dies at 80</h3><p>Strobe Talbott, the Time magazine reporter who became deputy secretary of state under President Bill Clinton and later ran the Brookings Institution, a Washington research group, died Thursday at 80 after a long illness, his son, Devin, confirmed, NPR reports. He and Clinton had roomed together at Oxford, where Time asked Talbott to help translate the leaked memoirs of Soviet leader Nikita Khrushchev.</p></div></div>
<h2 class="sec">Family Today</h2>
<p>Today&rsquo;s cover came in Thursday night from Garret: pie, handled. Keep them coming at <a href="https://tally.so/r/rjxDpl">tally.so/r/rjxDpl</a>.</p>
<h2 class="sec">The Home Wire</h2>

<div class="wire"><div><span class="num">3</span><h3>Rochester &middot; Genesee&rsquo;s Keg Tree Becomes a Food Drive</h3><p>The first 200 people who bring three non-perishable food items to the Genesee Brewery&rsquo;s Keg Tree lighting on Dec. 4 get a free keg-shaped mug etched with the tree, and the food drive runs through the holidays at the Genesee Brew House, WXXI reports. It&rsquo;s the brewery&rsquo;s first partnership with Foodlink, which says food-pantry visits in August and September were the highest it has ever seen.</p></div></div>
<div class="wire"><div><span class="num">4</span><h3>Sherman &middot; Village Will Vote on Dissolving</h3><p>Sherman residents will vote Tuesday, Feb. 9, from 6 a.m. to 9 p.m. at the fire hall on whether to dissolve the village, the Dunkirk <i>Observer</i> reports. Trustees set the date after confirming a citizen petition: 145 of its 151 signatures were from village residents.</p></div></div>
<div class="wire"><div><span class="num">5</span><h3>Silver Creek &middot; Community Bank Branch to Close</h3><p>Community Bank&rsquo;s Silver Creek branch, at Main Street and Central Avenue, is set to close in early 2027, Hanover Town Supervisor Lou Pelletter said, the <i>Observer</i> reports. It follows the bank&rsquo;s plan to close its Central Avenue branch in Dunkirk and move those customers to its Vineyard Drive office on March 19.</p></div></div>
<h2 class="sec">The Marquee</h2>
<div class="wire"><div><span class="num">6</span><h3>NBC Cuts the Goo Goo Dolls Short</h3><p>Buffalo&rsquo;s own Goo Goo Dolls played halftime at Highmark Stadium Thursday night, but NBC viewers saw only about 1 minute and 43 seconds of the set, WGRZ reports.</p></div></div>
<div class="wire"><div><span class="num">7</span><h3>Taylor Swift Skips the Game in Buffalo</h3><p>Taylor Swift appeared to skip husband Travis Kelce&rsquo;s game in Buffalo Thursday, Us Weekly reports, in keeping with her habit of passing on road games. She has attended every Chiefs home game this season.</p></div></div>
<div class="wire"><div><span class="num">8</span><h3>Wu-Tang Clan Plays Detroit&rsquo;s Halftime</h3><p>Wu-Tang Clan, joined by Red Hot Chili Peppers drummer Chad Smith, played a nearly seven-minute medley at halftime of the Lions&rsquo; Thanksgiving game, announced as the wrap-up of the group&rsquo;s farewell tour, Billboard reports. The Bears won, 39&ndash;35, on a touchdown with three seconds left.</p></div></div>
<h2 class="sec">The Gridiron</h2>
<div class="wire lead"><div><span class="kick">The Lead</span><h3>Bills 13, Chiefs 10: Bass From 57 at the Gun</h3><p>Tyler Bass hit a 57-yard field goal as time expired, and the Bills beat the Chiefs 13&ndash;10 on a rainy, windy Thanksgiving night in Orchard Park to go 10&ndash;1, the best record in the AFC, the AP reports. Bass had tied it at 10 with a 54-yarder early in the fourth; in between, Kansas City&rsquo;s Harrison Butker missed from 46.</p><p>James Cook ran for 117 yards and scored on a 5-yard run, and it was his 10th straight game with at least 75 yards and a touchdown, tying an NFL record Terry Allen set in 1995 and 1996, Buffalo Rumblings reports. Greg Rousseau&rsquo;s third-quarter sack of Patrick Mahomes was his 43rd, tying Mario Williams for seventh on the Bills&rsquo; all-time list.</p><p>The passing game didn&rsquo;t show up: 10 completions in 21 attempts for 81 yards and two interceptions, by Sportradar&rsquo;s count. The defense held the Chiefs to one touchdown, and replay took away a Rashee Rice catch on third down inside the final two minutes.</p><div class="pull">&ldquo;Not one that I agreed with.&rdquo; <span style="font-size:.8rem">&mdash; Chiefs coach Andy Reid on the overturned catch</span></div></div></div>
<div class="wire"><div><h3>Jets: 4&ndash;4 on Thanksgiving</h3><p>The Jets have played eight Thanksgiving games and split them, 4&ndash;4, starting as the New York Titans with a 41&ndash;35 win over the Dallas Texans in 1960, Gang Green Nation notes. This year they get Sunday at Miami, 1:00.</p></div></div>
'''
hourly = f['towns']['North Tonawanda']['hourly']
crv = curve(hourly, 7*60+22, 16*60+43)
erie = erie_block(json.load(open(S+'data/climate.json')), 51, 'Thursday')
alm = '''<div class="part"><span>The Almanac</span></div>
<h2 class="sec">The Weather Glass</h2>
''' + BYLINE + '''
<p class="wlede">The storm came through, the Bills won anyway, and today&rsquo;s just the leftover showers. Black Friday: wet parking lots, no snow, no excuse.</p>
<div class="touch-head" style="margin-top:1.1rem">Today</div>
<div class="wxrow">
  <div class="wxc"><div class="k">Tonight</div><div class="v">38&deg;</div><div class="s">chance showers</div></div>
  <div class="wxc"><div class="k">Wind</div><div class="v">6&ndash;13</div><div class="s">mph, southeast</div></div>
  <div class="wxc"><div class="k">Showers</div><div class="v">100%</div><div class="s">quarter to half inch</div></div>
  <div class="wxc"><div class="k">Normal</div><div class="v">43&deg;</div><div class="s">for the date</div></div>
</div>
<div class="line"><span class="lbl t">Next 24 hours</span></div>''' + crv + '''
<div class="line"><span class="lbl t">Records</span> Buffalo&rsquo;s for the date: 72 in 1990; 15 in 1951 and 1974. A year ago: 36 and 31, with 2.1 inches of snow.</div>
<div class="touch-head" style="margin-top:1.1rem">The Weekend &middot; Margo</div>
<p>Saturday&rsquo;s the one, and it&rsquo;s not much of a one. Showers quit by about 10 in North Tonawanda and Dunkirk, highs get to 47 and 48, and a west wind gusts near 30 to remind you it&rsquo;s still November. Sunday warms to 50, 52 in Scottsville, but the showers creep back, all day in North Tonawanda and after lunch everywhere else, and Sunday night it rains for real, 100 percent everywhere. So: lights up Saturday, leftovers Sunday, and if you&rsquo;re driving home from somewhere, leave before dinner. Not one f&#8209;&#8209;&#8209;ing snowflake in the forecast. &mdash; Margo</p>
<div class="touch-head" style="margin-top:1.1rem">This week</div>
<div class="strip5">
  <div><div class="d">Fri</div><div class="i">&#127783;</div><div class="h">47</div><div class="w">showers</div></div>
  <div><div class="d">Sat</div><div class="i">&#127781;</div><div class="h">47</div><div class="w">showers early</div></div>
  <div><div class="d">Sun</div><div class="i">&#127782;</div><div class="h">50</div><div class="w">showers likely</div></div>
  <div><div class="d">Mon</div><div class="i">&#127783;</div><div class="h">45</div><div class="w">showers, windy</div></div>
  <div><div class="d">Tue</div><div class="i">&#127780;</div><div class="h">TUEHI</div><div class="w">TUESKY</div></div>
</div>
<div class="touch-head" style="margin-top:1.1rem">Around us &middot; at dawn</div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">40<sup>&deg;</sup></div><div class="d">Mist<br>high 47&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">37<sup>&deg;</sup></div><div class="d">Light rain<br>high 47&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">41<sup>&deg;</sup></div><div class="d">Drizzle<br>high 49&deg;</div></div>
</div>
<div class="towns lakes">
  <div class="town"><div class="n">Lake Erie</div><div class="t">51<sup>&deg;</sup></div><div class="d">off Buffalo, Thursday</div></div>
  <div class="town"><div class="n">Lake Ontario</div><div class="t">52<sup>&deg;</sup></div><div class="d">off Rochester, Thursday</div></div>
</div>
''' + erie + '''
<div class="line">Thursday evening the northeast wind shoved Lake Erie toward Toledo: around 7 p.m. Buffalo&rsquo;s gauge sat more than 8 feet below Toledo&rsquo;s, and by 5 a.m. it had sloshed back to within 3 inches.</div>
<div class="line" style="margin-top:.4rem"><span class="lbl t">Snow so far</span> since July 1, through Thursday. Zero, four days from December.</div>
<div class="towns snow"><div class="town"><div class="n">North Tonawanda</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 5.4"</div></div><div class="town"><div class="n">Orchard Park</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 7.3"</div></div><div class="town"><div class="n">Dunkirk</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 7.3"</div></div><div class="town"><div class="n">Scottsville</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 6.8"</div></div></div>
<h2 class="sec">The Almanac Sky</h2>
<div class="wxrow">
  <div class="wxc"><div class="k">Moon</div><svg class="moonmini" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#3a2a1c" opacity=".25"/><path d="M50 4 A46 46 0 0 0 50 96 A33.5 46 0 0 0 50 4Z" fill="#f4e5b4"/></svg><div class="s">86% lit</div></div>
  <div class="wxc"><div class="k">Sunrise</div><div class="v">7:22</div><div class="s">a.m.</div></div>
  <div class="wxc"><div class="k">Daylight</div><div class="v">9h 21m</div><div class="s">2 min less</div></div>
</div>
<p class="skynote"><b>Tonight:</b> the waning moon rises at 7:55 p.m. in Gemini and sets at 11:32 Saturday morning, if the clouds part. Saturn is the evening&rsquo;s bright planet, highest in the south around 8; Jupiter rises around 10:50, Mars just after 11. Next new moon, December 8; next full, December 23.</p>
<div class="touch-head">The Stars &middot; for fun</div>
<div class="stars slim">
<div class="star"><span class="sgn">Aries</span> <span class="who">Kaylani, Luka</span><br>Still a prickly moon. Skip the 5 a.m. doorbuster; nothing in that store is worth it.</div>
<div class="star"><span class="sgn">Cancer</span> <span class="who">Gregg</span><br>The moon stays in your sign. Second plate of leftovers, no questions taken.</div>
<div class="star"><span class="sgn">Leo</span> <span class="who">Leah, Tommy</span><br>A quiet sky. Sleep in; the sales will still be there at noon.</div>
<div class="star"><span class="sgn">Virgo</span> <span class="who">Derek, Joanne</span><br>A kind moon after a long day of cooking. Let somebody else do the dishes.</div>
<div class="star"><span class="sgn">Scorpio</span> <span class="who">Ariel, Claire, Garret</span><br>The moon backs you, and Mercury&rsquo;s in on it. Good day to say the thing you&rsquo;ve been sitting on.</div>
</div>
<h2 class="sec">Coming Up</h2>
<div class="calbox"><div class="calrow"><div class="cd">Sat</div><div>Macy&rsquo;s 100th parade, rescheduled, 8:30 a.m.</div></div>
<div class="calrow"><div class="cd">Sun</div><div>Jets at Dolphins, 1:00</div></div>
<div class="calrow"><div class="cd">Dec. 6</div><div>Bills at Patriots, 4:25</div></div>
<div class="calnote">Migraine log: Garret&rsquo;s last was Wednesday; Joanne&rsquo;s, Sunday. Five this month.</div>
</div>
''' + otd + '''
<h2 class="sec">Question of the Day</h2>
<div class="qotd">I show up the day after, nobody planned me, and I&rsquo;m better cold. What am I? <i>Answer below the fold.</i></div>
<div class="dbl"><div class="a"></div><div class="b"></div></div>
<div class="colo"><div class="s" style="margin-bottom:8px"><b>Question of the Day:</b> Leftovers.</div>
<div class="s">Forecast, lake temperatures and radar per NWS Buffalo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; Lake Erie levels and wind per NOAA &middot; normals from NOAA &middot; sky computed for 14120 &middot; headlines via CBS, NPR, WGRZ, WXXI, the Dunkirk <i>Observer</i>, Us Weekly, Billboard, the AP via WIVB, Buffalo Rumblings, ProFootballTalk, Gang Green Nation &middot; scores and stats via Sportradar &middot; On This Day per History.com &middot; snow and records via ACIS</div>
<div class="ask"><a href="https://tally.so/r/rjxDpl">Send something to the paper</a> &middot; <a href="https://tally.so/r/obWNYP">Log a migraine</a> &middot; <a href="https://tally.so/r/EqxJpo">Ask Margo</a></div>
<div class="sig">&mdash; Margo</div><div class="orn">&#127809; &#127810; &#127809;</div></div>'''
P = f['towns']['North Tonawanda']['periods']
tue = next((p for p in P if p['name'] == 'Tuesday'), None)
if tue: alm = alm.replace('TUEHI', str(tue['temp'])).replace('TUESKY', tue['short'].lower()[:18])
else: alm = alm.replace('\n  <div><div class="d">Tue</div><div class="i">&#127780;</div><div class="h">TUEHI</div><div class="w">TUESKY</div></div>', '')
body = pre + news + alm
ed = {'date':'2026-11-27','no':156,'body_html':body,'plate_path':'/home/claude/plate156.jpg','plate_caption':'Thanksgiving, by the slice.','headline':'Bills 13, Chiefs 10 on Bass’s 57-yarder · storm leaves 800,000 dark · weekend outlook'}
for p in ['/home/claude/edition-2026-11-27.json', S+'data/edition-2026-11-27.json']:
    json.dump(ed, open(p,'w'), ensure_ascii=False)
print('ok', len(body), bool(erie), tue and (tue['temp'], tue['short']))
