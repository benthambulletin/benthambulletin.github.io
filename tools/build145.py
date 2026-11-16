import json, sys
sys.path.insert(0, '/home/claude'); from curve import curve
src = json.load(open('/home/claude/site/data/edition-2026-11-15.json'))['body_html']
def R(a, c, n=1):
    global src
    assert src.count(a) == n, ('R', a[:60], src.count(a)); src = src.replace(a, c)
def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50]); src = src[:i] + new + src[j:]
f = json.load(open('/home/claude/site/data/forecast.json'))
assert f['generated_utc'].startswith('2026-11-16')
assert [f['towns'][n]['observation']['temp_f'] for n in ['North Tonawanda', 'Dunkirk', 'Scottsville']] == [39, 43, 39]
assert f['lakes']['readings'] == {'Lake Erie (Buffalo)': 55, 'Lake Ontario (Rochester)': 56} and 'Sun Nov 15 2026 The water temperature off Buffalo' in f['lakes']['text']
hourly = f['towns']['North Tonawanda']['hourly']; assert 'T05:00' in hourly[0]['start']
chart = curve(hourly, 7 * 60 + 9, 16 * 60 + 51)

cover = '''<svg viewBox="0 0 750 375" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A drawing of a small space probe with a dish antenna far out among the stars, a tiny pale dot of home behind it">
<rect width="750" height="375" fill="#1b2230"/>
<g fill="#f4e5b4"><circle cx="60" cy="50" r="1.6"/><circle cx="140" cy="210" r="1.2"/><circle cx="230" cy="90" r="1.8"><animate attributeName="opacity" values="1;.3;1" dur="4s" repeatCount="indefinite"/></circle><circle cx="330" cy="300" r="1.3"/><circle cx="410" cy="40" r="1.4"/><circle cx="520" cy="250" r="1.7"><animate attributeName="opacity" values=".4;1;.4" dur="5s" repeatCount="indefinite"/></circle><circle cx="610" cy="70" r="1.3"/><circle cx="690" cy="180" r="1.6"/><circle cx="700" cy="330" r="1.2"/><circle cx="90" cy="320" r="1.5"><animate attributeName="opacity" values="1;.4;1" dur="6s" repeatCount="indefinite"/></circle><circle cx="285" cy="185" r="1.1"/><circle cx="470" cy="150" r="1.2"/></g>
<circle cx="110" cy="285" r="5" fill="#9fc3d8"/><circle cx="110" cy="285" r="5" fill="none" stroke="#9fc3d8" stroke-width="1"><animate attributeName="r" values="5;26" dur="3s" repeatCount="indefinite"/><animate attributeName="opacity" values=".8;0" dur="3s" repeatCount="indefinite"/></circle>
<line x1="118" y1="280" x2="520" y2="150" stroke="#9fc3d8" stroke-width="1" stroke-dasharray="2 9" opacity=".6"/>
<g transform="translate(560 135) rotate(-18)"><animateTransform attributeName="transform" type="translate" values="556 137;564 133;556 137" dur="9s" repeatCount="indefinite" additive="replace"/>
<line x1="-70" y1="0" x2="70" y2="0" stroke="#d3b88f" stroke-width="3"/><line x1="10" y1="0" x2="55" y2="48" stroke="#d3b88f" stroke-width="3"/>
<rect x="-18" y="-12" width="36" height="24" rx="3" fill="#cf6f1a"/>
<path d="M-34 -14 Q0 -58 34 -14 Z" fill="#f8eedb" stroke="#d3b88f" stroke-width="2"/><line x1="0" y1="-14" x2="0" y2="-48" stroke="#d3b88f" stroke-width="2"/><circle cx="0" cy="-50" r="3.5" fill="#e8b100"/></g>
</svg>'''
i = src.find('<img src="__PLATE__"'); j = src.find('>', i) + 1; assert i > 0
src = src[:i] + cover + src[j:]
R('<div class="plate-sub">Liftoff from the couch</div>', '<div class="plate-sub">A light-day from home</div>')
R('No. 144', 'No. 145'); R('Sunday &middot; November 15 &middot; 2026', 'Monday &middot; November 16 &middot; 2026')
S('<div class="tiles">', '<div class="plate-wrap">', '''<div class="tiles">
  <div class="tile"><div class="v">49&deg;</div><div class="k">Partly Sunny</div></div>
  <div class="tile"><div class="v">4:51</div><div class="k">Sunset</div></div>
  <div class="tile urg"><div class="v">10</div><div class="k">Days to Thanksgiving</div></div>
</div>
''')
S('<div class="wire lead">', '<div class="part"><span>The Almanac</span></div>', '''<div class="wire lead"><div><span class="kick">The Lead</span><h3>Voyager 1 Is About to Be One Light-Day Away</h3>
<p>On Wednesday, NASA's Voyager 1 is set to reach a distance no spacecraft has reached: one light-day from Earth, NPR reports. A light-day is how far light travels in 24 hours, more than 16 billion miles. Nothing people have launched has gone farther.</p>
<p>Voyager 1 left Earth on Sept. 5, 1977, and has been flying for nearly 50 years. It passed Jupiter and Saturn on the way out, and in 1979 it discovered a faint ring system around Jupiter.</p>
<p>NASA wants company for the occasion. On Tuesday night it is asking people to blink the probe's call sign, V-G-R, at the sky in Morse code, with a flashlight, a phone light or anything else that flashes. V is three quick flashes and a long one. G is two long and one quick. R is quick, long, quick. NASA calls it a symbolic celebration.</p>
</div></div>
<div class="wire"><div><h3>The Poll: 6&nbsp;a.m. It Is</h3><p>Three votes for 6 a.m., one for 8 a.m., one for either. Starting today, the Bulletin arrives at 6.</p></div></div>
<h2 class="sec">The National Wire</h2>
<div class="wire"><div class="num">1</div><div><h3>A Third U.S. Carrier Reaches the Middle East</h3><p>The aircraft carrier USS Theodore Roosevelt has joined two other American carriers in the Middle East as the war with Iran goes on, a U.S. military official confirmed to CBS; the three-carrier presence is expected to be temporary as ships rotate through. Bahrain said it intercepted Iranian strikes, and Iran's Foreign Ministry on Sunday rejected Germany's demand that it stop enriching uranium, the process that makes nuclear fuel.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Five Million Fewer on Food Aid</h3><p>About five million people have lost federal food benefits over the past year, since a sweeping tax and spending law cut funding for SNAP, the program once known as food stamps, and tightened who qualifies, NPR reports. It is considered the fastest decline in decades; in San Diego, one county benefits office has started handing out groceries on Saturdays.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Mexico's "Boss of Bosses" Dies at 80</h3><p>Miguel &Aacute;ngel F&eacute;lix Gallardo, who ran the Guadalajara Cartel at the height of the 1980s cocaine boom, has died in a hospital at 80, the BBC reports. He is credited with building the alliance between Colombian traffickers and Mexican cartels that changed how the drug trade works.</p></div></div>
<h2 class="sec">The Home Wire</h2>
<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; $60 Million for the Old Kodak Park</h3><p>New York will put $60 million toward modernizing the power grid at Eastman Business Park, the 1,200-acre former Kodak Park, Gov. Kathy Hochul announced, WXXI reports. The whole project is estimated at more than $93 million and is meant to bring enough electricity to empty buildings and open lots to attract new manufacturers.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Update: Wilson Wins It All</h3><p>The Wilson girls soccer team won the program's first state championship Sunday in Dryden, finishing a perfect 21&ndash;0 season, the <i>Observer</i> reports. The Lakewomen outscored their opponents 12&ndash;1 across the state tournament.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Dunkirk &middot; High School Hoops on an NBA Floor</h3><p>The Dunkirk and Forestville boys basketball teams will play each other Dec. 13 in the Cleveland Cavaliers' home arena, Dunkirk athletic director Kyle Jarrell told the school board, the <i>Observer</i> reports. It is part of a series the Cavaliers run for high school teams; the junior varsity game tips off at 11 a.m.</p></div></div>
<h2 class="sec">The Marquee</h2>
<div class="wire"><div class="num">1</div><div><h3>An Oscar for Glenn Close, at Last</h3><p>Glenn Close received an honorary Oscar on Sunday night at the Governors Awards, the film academy's annual dinner for career honors, the Hollywood Reporter says. Animator Floyd Norman and director Ridley Scott, who was absent after a recent medical procedure, were honored too.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Grammy Nominations This Morning</h3><p>The nominees for the 2027 Grammy Awards are being announced on a livestream starting at 7:45 this morning, Billboard reports. Olivia Dean, last year's best new artist, is widely expected to land several of the top ones, and she is one of the presenters reading the names.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>A Fourth Baby Mahomes</h3><p>Brittany Mahomes, wife of Chiefs quarterback Patrick Mahomes, was at Sunday's game in Atlanta five days after announcing she is expecting the couple's fourth child, E! News reports. They have three children: Sterling, Bronze and Golden.</p></div></div>
<h2 class="sec">The Gridiron &middot; Monday Morning Quarterback</h2>
<div class="wire"><div><h3>Bills 31, Jets 12</h3><p>Buffalo led only 10&ndash;6 at halftime, then scored three touchdowns after it: a Josh Allen sneak, a 45-yard pass to D. Moore and a 74-yard run by James Cook. Allen's first touchdown was the 323rd of his career, passing Peyton Manning for the most by a quarterback in his first ten seasons, Buffalo Rumblings reports. <b>Got right:</b> the ground game, 201 yards, and a pass rush with four sacks. <b>To fix:</b> Allen completed 11 of 21 with an interception, and the Bills gave the ball away twice.</p></div></div>
<div class="wire"><div><h3>Jets: Yards, but No End Zone</h3><p>The Jets moved the ball, 376 yards to Buffalo's 389, and held it longer. <b>Got right:</b> kicker J. Sanders made all four of his field goals, the longest from 48. <b>To fix:</b> finishing drives; all of the points came on those kicks. Quarterback Geno Smith left with an ankle injury in the third quarter, and rookie Cade Klubnik could make his first start Sunday against the Chargers, the Associated Press reports in the <i>Observer</i>.</p></div></div>
<div class="wire"><div><h3>AFC East</h3><table class="standings"><tr><td>Bills</td><td>8&ndash;1</td></tr><tr><td>Patriots</td><td>5&ndash;5</td></tr><tr><td>Jets</td><td>2&ndash;8</td></tr><tr><td>Dolphins</td><td>1&ndash;8</td></tr></table><p><b>Around the league:</b> the Bengals beat the Steelers 38&ndash;18 on Sunday night, and the 49ers outlasted the Cowboys 46&ndash;40, ProFootballTalk reports. <b>The AI Editor's scorecard:</b> the September picks were Bills 11&ndash;6 and Jets 6&ndash;11. Buffalo needs three wins in its last eight games to match its number; the Jets need four in their last seven.</p></div></div>
''')
S('<p class="wlede">', '<div class="line"><span class="lbl t">Next 24 hours</span>', '''<p class="wlede">Clouds give way to some sun, and a dry, milder week starts here</p>
<div class="wxrow">
  <div class="wxc"><div class="k">Tonight</div><div class="v">38&deg;</div><div class="s">partly cloudy</div></div>
  <div class="wxc"><div class="k">Wind</div><div class="v">3&ndash;9</div><div class="s">mph, west</div></div>
  <div class="wxc"><div class="k">Rain</div><div class="v">2%</div><div class="s">dry</div></div>
  <div class="wxc"><div class="k">Normal</div><div class="v">48&deg;</div><div class="s">for the date</div></div>
</div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">39<sup>&deg;</sup></div><div class="d">Cloudy<br>high 49&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">43<sup>&deg;</sup></div><div class="d">Cloudy<br>high 49&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">39<sup>&deg;</sup></div><div class="d">Cloudy<br>high 48&deg;</div></div>
</div>
<div class="towns lakes">
  <div class="town"><div class="n">Lake Erie</div><div class="t">55<sup>&deg;</sup></div><div class="d">off Buffalo, Sunday</div></div>
  <div class="town"><div class="n">Lake Ontario</div><div class="t">56<sup>&deg;</sup></div><div class="d">off Rochester, Sunday</div></div>
</div>
<div class="strip5">
  <div><div class="d">Mon</div><div class="i">&#9925;</div><div class="h">49</div><div class="w">partly sunny</div></div>
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">54</div><div class="w">sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#9728;</div><div class="h">56</div><div class="w">sunny</div></div>
  <div><div class="d">Thu</div><div class="i">&#9925;</div><div class="h">58</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Fri</div><div class="i">&#9925;</div><div class="h">59</div><div class="w">mostly sunny</div></div>
</div>
''')
S('<div class="line"><span class="lbl t">Next 24 hours</span>', '<h2 class="sec">The Almanac Sky</h2>', '<div class="line"><span class="lbl t">Next 24 hours</span></div>' + chart + '''<div class="line"><span class="lbl t">Outdoor window</span> Early afternoon, 1 to 4, when it is 47 or 48 and dry. Tuesday through Friday are better still.</div>
<div class="line"><span class="lbl t">Frost watch</span> Scottsville drops to 34 tonight; North Tonawanda and Dunkirk stay near 40.</div>
''')
S('<h2 class="sec">The Almanac Sky</h2>', '<h2 class="sec">Coming Up</h2>', '''<h2 class="sec">The Almanac Sky</h2>
<div class="wxrow">
  <div class="wxc"><div class="k">Moon</div><svg class="moonmini" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#5a4d3b"/><path d="M50 4 A46 46 0 0 1 50 96 A6.8 46 0 0 0 50 4Z" fill="#f4e5b4"/></svg><div class="s">waxing crescent</div></div>
  <div class="wxc"><div class="k">Sunrise</div><div class="v">7:09</div><div class="s">a.m.</div></div>
  <div class="wxc"><div class="k">Daylight</div><div class="v">9h 42m</div><div class="s">2 min less</div></div>
</div>
<p class="skynote"><b>Tonight:</b> the moon, nearly half lit, is in Capricornus and stays up until 11:08. Saturn is the bright point highest in the south around 9; no other bright planet is up before midnight. The full moon is Nov. 24.</p>
<div class="touch-head">The Stars &middot; for fun</div>
<div class="stars slim">
<div class="star"><span class="sgn">Aries</span> <span class="who">Kaylani, Luka</span><br>A second friendly day in a row. Start the thing you have been circling.</div>
<div class="star"><span class="sgn">Cancer</span> <span class="who">Gregg</span><br>Still a quiet sky. A Monday with no surprises is its own gift.</div>
<div class="star"><span class="sgn">Leo</span> <span class="who">Leah, Tommy</span><br>Somebody sees it differently than you do. Hear them out before lunch.</div>
<div class="star"><span class="sgn">Virgo</span> <span class="who">Derek, Joanne</span><br>No pushes and no pulls. Pick the one errand and call it a day.</div>
<div class="star"><span class="sgn">Scorpio</span> <span class="who">Ariel, Claire, Garret</span><br>Small snags, nothing serious. Leave ten minutes early.</div>
</div>
''')
S('<h2 class="sec">Coming Up</h2>', '<div class="dbl"><div class="a">', '''<h2 class="sec">Coming Up</h2>
<div class="calbox"><div class="calrow"><div class="cd">Wed</div><div>Central Michigan at UB, 7:30</div></div>
<div class="calrow"><div class="cd">Sun</div><div>Dolphins at Bills, 1:00; Jets at Chargers</div></div>
<div class="calrow"><div class="cd">Nov 26</div><div>Thanksgiving; Chiefs at Bills, 8:20</div></div>
<div class="calnote">Migraine log: Garret, Saturday. Three logged this month.</div>
</div>
<h2 class="sec">The Ledger</h2>
<div class="ledger"><div class="num"><div class="cap">Shorebirds that fly to Alaska each year to breed</div><div class="big">12 million</div></div>
<div class="txt">Among them, NPR reports, is the pectoral sandpiper: the size of a robin, about three ounces, and good for more than 17,000 miles a year between Alaska and Argentina. It flaps the whole way.</div></div>
<h2 class="sec">On This Day</h2>
<div class="otd"><b>November 16, 1907</b> &mdash; Oklahoma became the 46th state.</div>
<h2 class="sec">Question of the Day</h2>
<div class="qotd">I have one eye, and it only opens when you click me. I am no use at noon and a great comfort at midnight. What am I? <i>Answer below the fold.</i></div>
''')
R('<b>Question of the Day:</b> A thermostat.', '<b>Question of the Day:</b> A flashlight.')
S('headlines via ', ' &middot; scores and stats via Sportradar', 'headlines via NPR, CBS, the BBC, WXXI, the Dunkirk <i>Observer</i>, the Hollywood Reporter, Billboard, E! News, Buffalo Rumblings, ProFootballTalk')
ed = {'date': '2026-11-16', 'no': 145, 'body_html': src, 'plate_path': None, 'plate_caption': 'A light-day from home',
      'headline': "Voyager 1 nears one light-day · Bills 31, Jets 12 · The paper moves to 6 a.m."}
for p in ['/home/claude/site/data/edition-2026-11-16.json', '/home/claude/edition-2026-11-16.json']:
    json.dump(ed, open(p, 'w'), ensure_ascii=False, indent=1)
print('ok', len(src), 'Sunday Spotlight' in src, 'Week Ahead' in src)
