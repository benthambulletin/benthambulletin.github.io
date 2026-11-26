import json, sys
sys.path.insert(0,'/home/claude'); sys.path.insert(0,'/home/claude/site/tools')
from curve import curve
from erie_graphic import erie_block
S='/home/claude/site/'
y = json.load(open('/home/claude/edition-2026-11-25.json'))['body_html']
f = json.load(open(S+'data/forecast.json'))
def R(s, old, new):
    assert s.count(old) == 1, old[:60]
    return s.replace(old, new)
pre = y[:y.find('<div class="part">')]
pre = R(pre, 'No. 154', 'No. 155')
pre = R(pre, 'Wednesday &middot; November 25 &middot; 2026', 'Thursday &middot; November 26 &middot; 2026')
pre = R(pre, '<div class="v">42&deg;</div><div class="k">Mostly Sunny</div>', '<div class="v">42&deg;</div><div class="k">Rain Later</div>')
pre = R(pre, '<div class="v">4:44</div><div class="k">Sunset &middot; 1 min less</div>', '<div class="v">4:44</div><div class="k">Sunset</div>')
pre = R(pre, '<div class="tile urg"><div class="v">1</div><div class="k">Day to Thanksgiving</div></div>', '<div class="tile urg"><div class="v">Today</div><div class="k">Thanksgiving</div></div>')
pre = R(pre, 'alt="The front of the Buffalo Convention Center, white and blue panels with BUFFALO CONVENTION CENTER in blue letters"', 'alt="Family members together at the 2019 Turkey Trot, Briar second from right"')
pre = R(pre, '<div class="plate-cap">The Cover</div>', '<div class="plate-cap">Plate I &middot; The Family Album</div>')
s0 = pre.find('<div class="plate-sub">'); s1 = pre.find('</div>', s0)
pre = pre[:s0] + '<div class="plate-sub">Briar, second from right, with family at the 124th Turkey Trot, 2019. It&rsquo;s always for her.' + pre[s1:]

BYLINE = '<div style="display:flex;gap:.8rem;align-items:center;margin:.5rem 0 .7rem"><img src="/assets/margo-thanksgiving.jpg" alt="Margo Bentham, in ink, in a turkey hood" style="width:86px;height:86px;flex:none;border-radius:4px;border:1px solid var(--rule,#d3b88f)"><div><div style="font-family:\'Playfair Display\',Georgia,serif;font-weight:700;font-size:1.2rem;line-height:1.1">Margo Bentham</div><div style="font-family:Archivo,Arial,sans-serif;font-size:.6rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--teal,#2f5e3e);margin-top:.2rem">Editor-in-chief &middot; lead meteorologist</div><div style="font-style:italic;font-size:.85rem;color:var(--soft,#664a2c);margin-top:.3rem">Did not ask for the hat.</div><div style="font-family:Archivo,Arial,sans-serif;font-size:.62rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;margin-top:.35rem"><a href="https://tally.so/r/EqxJpo">Ask Margo &rarr;</a></div></div></div>'

box = open('/home/claude/box155.html').read()
box = R(box, 'Dry, gray, windy. Rain rain after 2pm.', 'Dry, gray, windy. Rain after 2.')
box = R(box, '<b>Rain:</b> rain after 2pm,', '<b>Rain:</b> after 2 p.m.,')
box = R(box, 'SINCE_YESTERDAY', 'Since yesterday: the rain slid back an hour, to 2, but the odds hit 100, gusts are up to 43 from 37, and the afternoon total is up to a half to three-quarters of an inch, from a quarter to a half. Sold out: 14,000 of you on the new course.')
fam = open('/home/claude/family.html').read()
otd = open('/home/claude/otd.html').read()

news = '''<div class="part"><span>The News</span></div>
''' + box + '''
<h2 class="sec">The National Wire</h2>
<div class="wire lead"><div><span class="kick">The Lead</span><h3>Macy&rsquo;s Parade Postponed, a First</h3><p>For the first time in its history, the Macy&rsquo;s Thanksgiving Day Parade has been postponed because of weather. The 100th parade will now step off Saturday at 8:30 a.m., Macy&rsquo;s said Wednesday, as a powerful coastal storm moves into New York.</p><p>The nor&rsquo;easter is expected to make it too windy for the balloons to fly safely, the BBC reports. The parade was suspended during World War Two, but it has never been put off for weather; in 1971 Macy&rsquo;s kept the balloons on the ground instead. Governor Kathy Hochul declared a state of emergency Wednesday night for Long Island, New York City and Westchester County.</p><p>Macy&rsquo;s had planned 100 balloons for the 100th parade, including 10 new ones: Bluey in a crown and a Minion riding a banana like a horse.</p><div class="pull">&ldquo;While we are heartbroken that our parade was postponed, the safety of our participants and spectators is and always will be our top priority.&rdquo; <span style="font-size:.8rem">&mdash; Will Coss, the parade&rsquo;s executive producer</span></div></div></div>
<div class="wire"><div><span class="num">2</span><h3>Steelers Cut Aaron Rodgers</h3><p>The Pittsburgh Steelers released Aaron Rodgers, the 42-year-old four-time MVP, on Wednesday, shortly after he tore into coach Mike McCarthy on ESPN&rsquo;s &ldquo;The Pat McAfee Show,&rdquo; NPR reports. It capped about 18 hours that began with the team benching him for backup Mason Rudolph ahead of Friday&rsquo;s game against Denver; McCarthy said Rodgers had given him an &ldquo;ultimatum&rdquo; on Tuesday.</p></div></div>
<div class="wire"><div><span class="num">3</span><h3>A Million SpaceX Satellites Approved</h3><p>The Federal Communications Commission has approved SpaceX&rsquo;s plan to launch a million satellites that would run on sunlight and process data for AI in orbit, the first approval of its kind, the BBC reports. Amazon called it a &ldquo;lofty ambition rather than a real plan,&rdquo; and U.S. astronomers said it would &ldquo;significantly undermine&rdquo; the public&rsquo;s ability to study the night sky.</p></div></div>
''' + fam + '''
<h2 class="sec">The Home Wire</h2>
<div class="wire"><div><span class="num">4</span><h3>North Tonawanda &middot; Oliver Street Rallies After Two Fires</h3><p>Two fires on Nov. 17 in the same Oliver Street building, one around 3 a.m. and another that evening, destroyed Academy Auction House and Carl&rsquo;s Tattooing, WKBW reports; the fire department called the first one accidental and electrical, and nobody was hurt in either. Neighbors have set up GoFundMe campaigns totaling more than $10,000 for owners Matt Hoffman and Carl Cederman, with others for families who lived upstairs.</p></div></div>
<div class="wire"><div><span class="num">5</span><h3>Chili &middot; Apartment Fire Displaces Families</h3><p>Several families are out of their homes after a fire broke out around 5 a.m. Wednesday at the Cedars of Chili Apartments on Purple Leaf Lane, Rochester First reports. One adult and three children were taken to Strong Memorial Hospital with minor injuries.</p></div></div>
<div class="wire"><div><span class="num">6</span><h3>Ellicottville &middot; Holiday Valley Waits a Week</h3><p>Holiday Valley has pushed its opening from Nov. 27 to Friday, Dec. 4, weather permitting, WIVB reports. Crews fired up nearly 120 snow guns after temperatures dropped overnight, WGRZ reports.</p></div></div>
<h2 class="sec">The Marquee</h2>
<div class="wire"><div><span class="num">7</span><h3>Andy Taylor of Duran Duran Dies at 65</h3><p>Andy Taylor, Duran Duran&rsquo;s original guitarist on &ldquo;Hungry Like the Wolf,&rdquo; &ldquo;Rio&rdquo; and &ldquo;The Reflex,&rdquo; hits tied up with the launch of MTV, has died at 65, his family and bandmates said, NPR reports. The band said he brought &ldquo;an indelible fire and swagger to our music.&rdquo;</p></div></div>
<div class="wire"><div><span class="num">8</span><h3>U2 Plays the First Thanksgiving Eve Game</h3><p>U2 headlined halftime of the NFL&rsquo;s first Thanksgiving Eve game, Packers at Rams, streamed on Netflix, opening with &ldquo;Sunday Bloody Sunday&rdquo; and paying tribute to Dolly Parton, Billboard reports. The tribute was &ldquo;Torn,&rdquo; her duet with Bono and the final vocal recording of Parton&rsquo;s career, Rolling Stone reports.</p></div></div>
<div class="wire"><div><span class="num">9</span><h3>&ldquo;South Park&rdquo; Ends Its Season on &ldquo;GTA VI&rdquo;</h3><p>The &ldquo;South Park&rdquo; season 29 finale used the long-awaited release of the video game &ldquo;Grand Theft Auto VI&rdquo; as its stand-in for the midterm elections, the Hollywood Reporter says. Power outages blamed on billionaires&rsquo; AI data centers keep the town from playing it.</p></div></div>
<h2 class="sec">The Gridiron</h2>
<div class="wire"><div><h3>Tonight: Chiefs at Bills, 8:20</h3><p>The Bills haven&rsquo;t ruled anyone out; five players are questionable, among them Dalton Kincaid, Christian Benford and Dorian Williams, WGRZ and Buffalo Rumblings report, while the Chiefs will be without two starters. Rumblings calls Kincaid a true game-time decision, with inactives due at 6:50. Bring a coat: rain and gusts into the 40s tonight.</p></div></div>
<div class="wire"><div><h3>Jets: at Miami, Sunday, 1:00</h3><p>No new team news.</p></div></div>
<div class="wire"><div><h3>The Sunday Tax &middot; Week 12</h3><p>The Rams beat the Packers 26&ndash;13 last night to open the week. Today&rsquo;s sheets lock at kickoff: Bears at Lions at 1:00, Eagles at Cowboys at 4:30, Chiefs at Bills at 8:20. Standings at <a href="https://benthambulletin.github.io/pool/">benthambulletin.github.io/pool</a>.</p></div></div>
'''
hourly = f['towns']['North Tonawanda']['hourly']
crv = curve(hourly, 7*60+21, 16*60+44)
erie = erie_block(json.load(open(S+'data/climate.json')), 52, 'Wednesday')
alm = '''<div class="part"><span>The Almanac</span></div>
<h2 class="sec">The Weather Glass</h2>
''' + BYLINE + '''
<p class="wlede">Run early, eat late. The rain holds off till about 2, then it pours through the night: an inch and a half to nearly three inches by Friday morning, gusts in the 40s. The turkey&rsquo;s the only one who should be getting basted.</p>
<div class="touch-head" style="margin-top:1.1rem">Today</div>
<div class="wxrow">
  <div class="wxc"><div class="k">Tonight</div><div class="v">35&deg;</div><div class="s">rain</div></div>
  <div class="wxc"><div class="k">Wind</div><div class="v">9&ndash;21</div><div class="s">mph, east; gusts 43</div></div>
  <div class="wxc"><div class="k">Rain</div><div class="v">After 2</div><div class="s">100%</div></div>
  <div class="wxc"><div class="k">Normal</div><div class="v">44&deg;</div><div class="s">for the date</div></div>
</div>
<div class="line"><span class="lbl t">Next 24 hours</span></div>''' + crv + '''
<div class="line"><span class="lbl t">Records</span> Buffalo&rsquo;s for the date: 66 in 1988; 15 in 1938, 1949 and 1974. A year ago: 55 and 32, with 0.2 inch of snow.</div>
<div class="touch-head" style="margin-top:1.1rem">This week</div>
<div class="strip5">
  <div><div class="d">Thu</div><div class="i">&#127783;</div><div class="h">42</div><div class="w">rain after 2</div></div>
  <div><div class="d">Fri</div><div class="i">&#127783;</div><div class="h">46</div><div class="w">rain, showers</div></div>
  <div><div class="d">Sat</div><div class="i">&#127782;</div><div class="h">48</div><div class="w">showers early</div></div>
  <div><div class="d">Sun</div><div class="i">&#127782;</div><div class="h">51</div><div class="w">chance showers</div></div>
  <div><div class="d">Mon</div><div class="i">&#9729;</div><div class="h">MONHI</div><div class="w">MONSKY</div></div>
</div>
<div class="line"><span class="lbl t">Rain total</span> A half to three-quarters of an inch this afternoon, 1 to 2 inches tonight, a quarter to half inch more Friday.</div>
<div class="touch-head" style="margin-top:1.1rem">Around us &middot; at dawn</div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">32<sup>&deg;</sup></div><div class="d">Clear<br>high 42&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">36<sup>&deg;</sup></div><div class="d">Clear<br>high 44&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">30<sup>&deg;</sup></div><div class="d">Clear<br>high 42&deg;</div></div>
</div>
<div class="towns lakes">
  <div class="town"><div class="n">Lake Erie</div><div class="t">52<sup>&deg;</sup></div><div class="d">off Buffalo, Wednesday</div></div>
  <div class="town"><div class="n">Lake Ontario</div><div class="t">53<sup>&deg;</sup></div><div class="d">off Rochester, Wednesday</div></div>
</div>
''' + erie + '''
<div class="line" style="margin-top:.4rem"><span class="lbl t">Snow so far</span> since July 1, through Wednesday. Still nothing, and nothing coming.</div>
<div class="towns snow"><div class="town"><div class="n">North Tonawanda</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 5.1"</div></div><div class="town"><div class="n">Orchard Park</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 6.9"</div></div><div class="town"><div class="n">Dunkirk</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 6.9"</div></div><div class="town"><div class="n">Scottsville</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 6.4"</div></div></div>
<h2 class="sec">The Almanac Sky</h2>
<div class="wxrow">
  <div class="wxc"><div class="k">Moon</div><svg class="moonmini" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#3a2a1c" opacity=".25"/><path d="M50 4 A46 46 0 0 0 50 96 A40.0 46 0 0 0 50 4Z" fill="#f4e5b4"/></svg><div class="s">93% lit</div></div>
  <div class="wxc"><div class="k">Sunrise</div><div class="v">7:21</div><div class="s">a.m.</div></div>
  <div class="wxc"><div class="k">Daylight</div><div class="v">9h 23m</div><div class="s">2 min less</div></div>
</div>
<p class="skynote"><b>Tonight:</b> the waning moon rises at 6:36 p.m. in Gemini, though tonight&rsquo;s rain will hide it, and sets at 10:52 Friday morning. Saturn is the evening&rsquo;s bright planet, highest in the south around 8; Jupiter rises around 11, Mars just after. Next new moon, December 8; next full, December 23.</p>
<div class="touch-head">The Stars &middot; for fun</div>
<div class="stars slim">
<div class="star"><span class="sgn">Aries</span> <span class="who">Kaylani, Luka</span><br>The moon is in a mood with you. Bring the rolls, hand them over, and let someone else take the credit.</div>
<div class="star"><span class="sgn">Cancer</span> <span class="who">Gregg</span><br>The moon is in your sign on Thanksgiving. Take the good chair and don&rsquo;t apologize.</div>
<div class="star"><span class="sgn">Leo</span> <span class="who">Leah, Tommy</span><br>Nothing overhead. Tommy runs, Leah brings the salad; the universe calls it even.</div>
<div class="star"><span class="sgn">Virgo</span> <span class="who">Derek, Joanne</span><br>A friendly moon for the people doing all the cooking. Delegate the dishes.</div>
<div class="star"><span class="sgn">Scorpio</span> <span class="who">Ariel, Claire, Garret</span><br>A good moon for runners. Five miles, then seconds.</div>
</div>
<h2 class="sec">Coming Up</h2>
<div class="calbox"><div class="calrow"><div class="cd">Today</div><div>Turkey Trot, 9:00; at Derek&rsquo;s, appetizers 1, dinner 3; Chiefs at Bills, 8:20</div></div>
<div class="calrow"><div class="cd">Sat</div><div>Macy&rsquo;s parade, rescheduled, 8:30 a.m.</div></div>
<div class="calrow"><div class="cd">Sun</div><div>Jets at Dolphins, 1:00</div></div>
<div class="calnote">Migraine log: Joanne&rsquo;s last was Sunday; Garret&rsquo;s, Nov. 14. Four this month.</div>
</div>
''' + otd + '''
<h2 class="sec">Question of the Day</h2>
<div class="qotd">I&rsquo;m a boat that never leaves the table, and everyone wants a turn with me. What am I? <i>Answer below the fold.</i></div>
<div class="dbl"><div class="a"></div><div class="b"></div></div>
<div class="colo"><div class="s" style="margin-bottom:8px"><b>Question of the Day:</b> The gravy boat.</div>
<div class="s">Forecast, lake temperatures and radar per NWS Buffalo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; Lake Erie levels and wind per NOAA &middot; normals from NOAA &middot; sky computed for 14120 &middot; headlines via CBS, the BBC, NPR, WKBW, WIVB, WGRZ, Rochester First, Billboard, Rolling Stone, the Hollywood Reporter, Buffalo Rumblings &middot; scores and game times via Sportradar &middot; On This Day per George Washington&rsquo;s Mount Vernon &middot; snow and records via ACIS</div>
<div class="ask"><a href="https://tally.so/r/rjxDpl">Send something to the paper</a> &middot; <a href="https://tally.so/r/obWNYP">Log a migraine</a> &middot; <a href="https://tally.so/r/EqxJpo">Ask Margo</a></div>
<div class="sig">&mdash; Margo</div><div class="orn">&#127809; &#127810; &#127809;</div></div>'''
P = f['towns']['North Tonawanda']['periods']
mon = next((p for p in P if p['name'] == 'Monday'), None)
if mon:
    alm = alm.replace('MONHI', str(mon['temp'])).replace('MONSKY', mon['short'].lower()[:18])
else:
    alm = alm.replace('\n  <div><div class="d">Mon</div><div class="i">&#9729;</div><div class="h">MONHI</div><div class="w">MONSKY</div></div>', '')
body = pre + news + alm
ed = {'date':'2026-11-26','no':155,'body_html':body,'plate_path':'/home/claude/plate155.jpg','plate_caption':'Briar, second from right, with family at the 124th Turkey Trot, 2019.','headline':'Happy Thanksgiving: Trot dry at 9, rain after 2 · Macy’s parade postponed · Chiefs at Bills'}
for p in ['/home/claude/edition-2026-11-26.json', S+'data/edition-2026-11-26.json']:
    json.dump(ed, open(p,'w'), ensure_ascii=False)
print('ok', len(body), bool(erie), mon and (mon['temp'], mon['short']))
