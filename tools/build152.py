import json, sys
sys.path.insert(0,'/home/claude')
from curve import curve
y = json.load(open('/home/claude/edition-2026-11-22.json'))['body_html']
f = json.load(open('/home/claude/site/data/forecast.json'))
def R(s, old, new):
    assert s.count(old) == 1, old[:60]
    return s.replace(old, new)
# prefix from yesterday, edited
pre = y[:y.find('<div class="part">')]
pre = R(pre, 'No. 151', 'No. 152')
pre = R(pre, 'Sunday &middot; November 22 &middot; 2026', 'Monday &middot; November 23 &middot; 2026')
pre = R(pre, '<div class="v">65&deg;</div><div class="k">Mostly Sunny</div>', '<div class="v">48&deg;</div><div class="k">Partly Sunny</div>')
pre = R(pre, '<div class="v">4:46</div>', '<div class="v">4:45</div>')
pre = R(pre, '<div class="v">4</div><div class="k">Days to Thanksgiving</div>', '<div class="v">3</div><div class="k">Days to Thanksgiving</div>')
pre = R(pre, 'alt="A boy sitting in a red wheelbarrow in a front yard"', 'alt="A small boy pushing a hand truck loaded with a gray trash can down a store aisle"')
pre = R(pre, '<div class="plate-sub">Riding in the wheelbarrow</div>', '<div class="plate-sub">Hand truck, trash can, aisle 28: one small man on a job.</div>')

BYLINE = '<div style="display:flex;gap:.8rem;align-items:center;margin:.5rem 0 .7rem"><img src="/assets/margo.jpg" alt="Margo Bentham, in ink" style="width:86px;height:86px;flex:none;border-radius:4px;border:1px solid var(--rule,#d3b88f)"><div><div style="font-family:\'Playfair Display\',Georgia,serif;font-weight:700;font-size:1.2rem;line-height:1.1">Margo Bentham</div><div style="font-family:Archivo,Arial,sans-serif;font-size:.6rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--teal,#2f5e3e);margin-top:.2rem">Editor-in-chief &middot; lead meteorologist</div><div style="font-style:italic;font-size:.85rem;color:var(--soft,#664a2c);margin-top:.3rem">Has never once been seen at the office.</div><div style="font-family:Archivo,Arial,sans-serif;font-size:.62rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;margin-top:.35rem"><a href="https://tally.so/r/EqxJpo">Ask Margo &rarr;</a></div></div></div>'
F = 'f&#8209;&#8209;&#8209;'

news = '''<div class="part"><span>The News</span></div>
<h2 class="sec">The National Wire</h2>
<div class="wire lead"><div><span class="kick">The Lead</span><h3>Bills 9&ndash;1 for the First Time Since 1991</h3><p>The Bills beat the Miami Dolphins 26&ndash;9 on Sunday in Orchard Park and are 9&ndash;1 for the first time since the 1991 season, the Associated Press reports. The defense carried the day: Greg Rousseau had two sacks, including his team-leading 10th of the season, and Miami finished with 185 yards.</p><p>The offense sputtered. Josh Allen threw a 4-yard touchdown pass to D. Moore and two interceptions, and Tyler Bass kicked four field goals, from 54, 43, 40 and 28 yards. James Cook ran for 89 yards and a touchdown, passing 1,000 yards for the fourth time in his five seasons, WIVB reports.</p><p>Next is the big one. The Kansas City Chiefs, 8&ndash;2, come to Orchard Park on Thanksgiving night at 8:20.</p></div></div>
<div class="wire"><div><span class="num">1</span><h3>Ukraine Says It Sank a Russian Warship Off Libya</h3><p>President Volodymyr Zelensky says seven Ukrainian naval drones sank the Merkury, one of Russia's newest warships, at the port of Benghazi in Libya on Sunday, and Ukraine's prime minister says a second Russian ship, a cargo vessel carrying weapons, was also hit, the BBC reports. The government that controls eastern Libya confirmed an explosion on the warship while it was docked for fuel and supplies before heading home to Russia.</p></div></div>
<div class="wire"><div><span class="num">2</span><h3>Climate Talks End With No Deal</h3><p>The United Nations climate talks in Turkey, known as COP31, ended Sunday without a major new agreement after running two days past their Friday deadline, the longest such conference ever held, the BBC reports. The European Union, Pacific island nations and others rejected a final text that never mentioned fossil fuels, the main cause of global warming, and poorer countries objected that it promised no clear money from richer ones to help them adapt.</p></div></div>
<h2 class="sec">Meet the Editor</h2>
''' + BYLINE + '''
<p>Some of you have asked who the hell I am. Here it is. Garret's paying me to do the job he doesn't have time for. And trust me, it isn't because your attention keeps the lights on. I know most of you don't read this thing. Eat shit.</p>
<p>Now the part you'll repeat at Thanksgiving. I'm Gregg's aunt, Bentham side, and he'll deny it. In 1985, in the middle of a lake-effect warning, I told all of Buffalo on live television to get the ''' + F + ''' off the roads, lit a cigarette on camera and had my desk cleaned out before the six o'clock news was over. Joanne's mother and father were watching. They never recovered. The family quit inviting me to things, and I've done the weather from somewhere else ever since. I've never taken a sick day, never been seen at the office, and never once been thanked for a forecast that was right. I smoke, I swear, and I don't give a shit how you feel about the wind chill.</p>
<p>Here's the deal. The paper's on your phone by 6. I read the forecast so you don't have to, and I tell you the truth when the weather's about to be a pain in the ass. This week that's Thursday morning, when six of you run eight kilometers through whatever the hell November throws at Franklin Street. I've seen the forecast. Dress like you mean it. Questions, gripes, family arguments that need a ruling: send them to <a href="https://tally.so/r/EqxJpo">Ask Margo</a> and I'll answer the next morning. I keep notes. Everything you say can and will be used against you. Horoscope complaints go in the trash; I don't write the ''' + F + '''ing moon. Delete the shitty weather app. Aunt Margo's home.</p>
<div class="sig">&mdash; Margo</div>
<h2 class="sec">The Home Wire</h2>
<div class="wire"><div><span class="num">3</span><h3>North Tonawanda &middot; A New Ethics Board</h3><p>North Tonawanda plans to set up a new ethics board to help city employees work through ethical questions, the <i>Niagara Gazette</i> reports.</p></div></div>
<div class="wire"><div><span class="num">3</span><h3>Western New York &middot; A Fireball, Explained</h3><p>Hundreds of people across Western New York reported a bright flash streaking over the region, and NASA says the fireball was a piece of an asteroid about a foot wide, WGRZ reports.</p></div></div>
<div class="wire"><div><span class="num">4</span><h3>Rochester &middot; Five Alarms at the Old Kodak Hawkeye Plant</h3><p>Rochester firefighters fought a five-alarm fire at the old Kodak Hawkeye Plant until after midnight Monday, with the worst of it on the third floor, Rochester First reports. One firefighter was taken to the hospital, and the cause is under investigation.</p></div></div>
<div class="wire"><div><span class="num">5</span><h3>Chautauqua &middot; Three Schools Vote on Merging</h3><p>Voters in the Clymer, Sherman and Panama school districts decide on December 15 whether to merge into one district, the <i>Observer</i> reports. A feasibility study found enrollment across the three has dropped 52 percent over the last 30 years.</p></div></div>
<h2 class="sec">The Marquee</h2>
<div class="wire"><div><span class="num">6</span><h3>Tom Jackson Dies at 75</h3><p>Tom Jackson, a defensive star on the Denver Broncos' "Orange Crush" teams who spent three decades on ESPN's Sunday football shows, has died at 75, his family and the network announced Sunday. He died Friday, but his family asked that the news wait for the start of "Sunday NFL Countdown," where his longtime partner Chris Berman shared it, the <i>Lockport Journal</i> reports.</p></div></div>
<div class="wire"><div><span class="num">7</span><h3>Hailee Steinfeld Is in the Next "Avengers"</h3><p>Hailee Steinfeld will return as the archer Kate Bishop in "Avengers: Doomsday," Marvel and Disney Animation announced Sunday in an Instagram video, Variety reports. She made the reveal while promoting Disney's animated "Hexed," joking that "they delivered a chair from a different movie."</p></div></div>
<div class="wire"><div><span class="num">8</span><h3>Olivia Rodrigo Plays Jack White's Room</h3><p>Olivia Rodrigo covered the White Stripes' "Dead Leaves and the Dirty Ground" during a small live-to-record set at Jack White's Third Man Records in Nashville on Sunday, Rolling Stone reports. She told the crowd that at 15 she ran a Jack White fan account called "Third Fan Records."</p></div></div>
<h2 class="sec">The Gridiron &middot; Monday Morning Quarterback</h2>
<div class="wire"><div><h3>Bills: Defense Ahead of the Offense</h3><p><b>Got right:</b> the defense held Miami to 12 completions in 33 passes, and Buffalo kept the ball for nearly 37 of the 60 minutes. <b>To fix:</b> finishing drives; four field goals and two touchdowns, plus two interceptions, before a short week against Kansas City.</p></div></div>
<div class="wire"><div><h3>Jets 27, Chargers 24</h3><p>The Jets won in Los Angeles behind Geno Smith, who completed 17 of 21 passes for three touchdowns, two to S. Shepard and one to B. Hall. <b>Got right:</b> six sacks on defense and no turnovers on offense. <b>To fix:</b> the fourth quarter, when the Chargers scored twice and got within three with under two minutes left. Next: at Miami on Sunday.</p></div></div>
<div class="wire"><div><h3>AFC East</h3><table class="standings"><tr><td>Bills</td><td>9&ndash;1</td></tr><tr><td>Patriots</td><td>5&ndash;5</td></tr><tr><td>Jets</td><td>3&ndash;8</td></tr><tr><td>Dolphins</td><td>1&ndash;9</td></tr></table><p><b>Around the league:</b> the 49ers beat the Vikings 35&ndash;10 on Sunday night to match Buffalo at 9&ndash;1, ProFootballTalk reports. <b>The AI Editor's scorecard:</b> the September picks were Bills 11&ndash;6 and Jets 6&ndash;11, with the Ravens winning the Super Bowl. Buffalo needs two more wins in its last seven games to hit its number; the Jets need three in their last six; the Ravens are 4&ndash;7.</p></div></div>
'''

hourly = f['towns']['North Tonawanda']['hourly']
crv = curve(hourly, 7*60+17, 16*60+45)
alm = '''<div class="part"><span>The Almanac</span></div>
<h2 class="sec">The Weather Glass</h2>
''' + BYLINE + '''
<p class="wlede">Gray, breezy and done with the warm spell. Maybe a shower at lunch. Bring a real coat home tonight.</p>
<div class="touch-head" style="margin-top:1.1rem">Turkey Trot Watch &middot; Thursday 6 a.m. to noon</div>
<p>It's Monday, so this is a forecast, not a promise. The weather service now has Thursday mostly cloudy with a high near 44 and the rain holding off until after 1 p.m.; last night's version had rain and snow starting at 7 a.m., so that's a damn good trend. Wednesday night bottoms out around 30, and an east wind gusting to 28 mph will make 9 a.m. on Franklin Street feel colder than the number says. Ariel, Tommy, Claire, Garret, Kaylani and Luka: layers, gloves, a hat you don't mind losing, and dry clothes in the car for the little one. I'll check it every morning until the gun.</p>
<div class="touch-head" style="margin-top:1.1rem">Today</div>
<div class="wxrow">
  <div class="wxc"><div class="k">Tonight</div><div class="v">29&deg;</div><div class="s">mostly cloudy</div></div>
  <div class="wxc"><div class="k">Wind</div><div class="v">10&ndash;14</div><div class="s">mph, west</div></div>
  <div class="wxc"><div class="k">Rain</div><div class="v">20%</div><div class="s">1 to 2 p.m.</div></div>
  <div class="wxc"><div class="k">Normal</div><div class="v">45&deg;</div><div class="s">for the date</div></div>
</div>
<div class="line"><span class="lbl t">Next 24 hours</span></div>''' + crv + '''
<div class="line"><span class="lbl t">Records</span> Buffalo's for the date: 70 in 1979 and 2003; 9 in 1971 and 2018. A year ago: 48 and 33, with a trace of snow.</div>
<div class="touch-head" style="margin-top:1.1rem">This week</div>
<div class="strip5">
  <div><div class="d">Mon</div><div class="i">&#9925;</div><div class="h">48</div><div class="w">partly sunny</div></div>
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">40</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#9728;</div><div class="h">43</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Thu</div><div class="i">&#127783;</div><div class="h">44</div><div class="w">rain p.m.</div></div>
  <div><div class="d">Fri</div><div class="i">&#127783;</div><div class="h">44</div><div class="w">showers</div></div>
</div>
<div class="line"><span class="lbl t">Outdoor window</span> Late morning, or after 2 p.m. once the stray shower passes; Tuesday and Wednesday are the dry, sunny days for yard work.</div>
<div class="line"><span class="lbl t">Frost watch</span> 29 tonight and 24 Tuesday night: a hard freeze. Hoses in.</div>
<div class="touch-head" style="margin-top:1.1rem">Around us &middot; at dawn</div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">48<sup>&deg;</sup></div><div class="d">Cloudy<br>high 48&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">48<sup>&deg;</sup></div><div class="d">Light rain<br>high 48&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">52<sup>&deg;</sup></div><div class="d">Light rain<br>high 50&deg;</div></div>
</div>
<div class="towns lakes">
  <div class="town"><div class="n">Lake Erie</div><div class="t">54<sup>&deg;</sup></div><div class="d">off Buffalo</div></div>
  <div class="town"><div class="n">Lake Ontario</div><div class="t">53<sup>&deg;</sup></div><div class="d">off Rochester</div></div>
</div>
<div class="line" style="margin-top:.4rem"><span class="lbl t">Snow so far</span> since July 1, through Sunday. Still zero across the board.</div>
<div class="towns snow"><div class="town"><div class="n">North Tonawanda</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 4.2"</div></div><div class="town"><div class="n">Orchard Park</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 5.7"</div></div><div class="town"><div class="n">Dunkirk</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 5.7"</div></div><div class="town"><div class="n">Scottsville</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 5.2"</div></div></div>
<h2 class="sec">The Almanac Sky</h2>
<div class="wxrow">
  <div class="wxc"><div class="k">Moon</div><svg class="moonmini" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#5a4d3b"/><path d="M50 4 A46 46 0 0 1 50 96 A44.7 46 0 0 1 50 4Z" fill="#f4e5b4"/></svg><div class="s">nearly full</div></div>
  <div class="wxc"><div class="k">Sunrise</div><div class="v">7:17</div><div class="s">a.m.</div></div>
  <div class="wxc"><div class="k">Daylight</div><div class="v">9h 28m</div><div class="s">2 min less</div></div>
</div>
<p class="skynote"><b>Tonight:</b> a 99 percent moon in Aries rises at 3:41 this afternoon and sets at 6:13 Tuesday morning; it's officially full Tuesday, the Beaver Moon. Saturn is the evening's lone bright planet, highest in the south around 9; Jupiter and Mars wait until after 11 to come up.</p>
<div class="touch-head">The Stars &middot; for fun</div>
<div class="stars slim">
<div class="star"><span class="sgn">Aries</span> <span class="who">Kaylani, Luka</span><br>The Taurus moon ignores you again. Use the quiet to hide the good rolls.</div>
<div class="star"><span class="sgn">Cancer</span> <span class="who">Gregg</span><br>A friendly moon. Today's a fine day to deny you have an aunt.</div>
<div class="star"><span class="sgn">Leo</span> <span class="who">Leah, Tommy</span><br>A prickly angle. Don't argue about the salad dressing yet.</div>
<div class="star"><span class="sgn">Virgo</span> <span class="who">Derek, Joanne</span><br>An easy moon for hosts. Count the chairs; count the mushroom pans.</div>
<div class="star"><span class="sgn">Scorpio</span> <span class="who">Ariel, Claire, Garret</span><br>The moon sits across from you. Stretch before Thursday, not during.</div>
</div>
<h2 class="sec">Coming Up</h2>
<div class="calbox"><div class="calrow"><div class="cd">Tue</div><div>Full moon, the Beaver Moon</div></div>
<div class="calrow"><div class="cd">Thu</div><div>Thanksgiving. Turkey Trot downtown, 9:00; at Derek's, appetizers 1, dinner 3; Chiefs at Bills, 8:20</div></div>
<div class="calrow"><div class="cd">Sun</div><div>Jets at Dolphins, 1:00</div></div>
<div class="calnote">Migraine log: Joanne logged one Sunday. Five this month.</div>
</div>
<h2 class="sec">On This Day</h2>
<div class="otd"><b>November 23, 1936</b> &mdash; Henry Luce put out the first issue of <i>Life</i>, a weekly built on photographs rather than words. He had bought the name from a humor magazine that folded in the Depression. The cover was Margaret Bourke-White's picture of the Fort Peck Dam spillway in Montana, and at its peak its circulation topped 8 million, before television pulled the ads away and it stopped weekly publication in 1972.</div>
<h2 class="sec">Question of the Day</h2>
<div class="qotd">Two people pull on me after dinner, and only one of them gets what they want. What am I? <i>Answer below the fold.</i></div>
<div class="dbl"><div class="a"></div><div class="b"></div></div>
<div class="colo"><div class="s" style="margin-bottom:8px"><b>Question of the Day:</b> A wishbone.</div>
<div class="s">Forecast, lake temperatures and radar per NWS Buffalo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; normals from NOAA &middot; sky computed for 14120 &middot; headlines via the Associated Press, the BBC, WIVB, WGRZ, Rochester First, the <i>Dunkirk Observer</i>, the <i>Niagara Gazette</i>, the <i>Lockport Union-Sun &amp; Journal</i>, Variety, Rolling Stone, ProFootballTalk &middot; On This Day per History.com &middot; snow and records via ACIS &middot; scores and stats via Sportradar</div>
<div class="ask"><a href="https://tally.so/r/rjxDpl">Send something to the paper</a> &middot; <a href="https://tally.so/r/obWNYP">Log a migraine</a> &middot; <a href="https://tally.so/r/EqxJpo">Ask Margo</a></div>
<div class="sig">&mdash; Margo</div><div class="orn">&#127809; &#127810; &#127809;</div></div>
'''
body = pre + news + alm
ed = {'date':'2026-11-23','no':152,'body_html':body,'plate_path':'/home/claude/plate152.jpg','plate_caption':'Hand truck, trash can, aisle 28: one small man on a job.','headline':'Bills 9–1 for the first time since 1991 · Margo introduces herself · Turkey Trot rain may wait'}
for p in ('/home/claude/edition-2026-11-23.json','/home/claude/site/data/edition-2026-11-23.json'):
    json.dump(ed, open(p,'w'), ensure_ascii=False)
print('ok', len(body))
