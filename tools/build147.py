import json, sys, os
sys.path.insert(0, '/home/claude'); from curve import curve
src = json.load(open('/home/claude/site/data/edition-2026-11-17.json'))['body_html']
def R(a, c, n=1):
    global src
    assert src.count(a) == n, ('R', a[:60], src.count(a)); src = src.replace(a, c)
def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50]); src = src[:i] + new + src[j:]
f = json.load(open('/home/claude/site/data/forecast.json'))
assert f['generated_utc'].startswith('2026-11-18')
assert [f['towns'][n]['observation']['temp_f'] for n in ['North Tonawanda', 'Dunkirk', 'Scottsville']] == [39, 41, 37]
assert f['lakes']['readings'] == {'Lake Erie (Buffalo)': 54, 'Lake Ontario (Rochester)': 54} and 'Tue Nov 17 2026 The water temperature off Buffalo' in f['lakes']['text']
hourly = f['towns']['North Tonawanda']['hourly']; assert 'T05:00' in hourly[0]['start']
chart = curve(hourly, 7 * 60 + 11, 16 * 60 + 49)
COVER = json.load(open('/home/claude/cover147.json')) if os.path.exists('/home/claude/cover147.json') else None
i = src.find('<img src="__PLATE__"'); j = src.find('>', i) + 1; assert i > 0
if COVER:
    src = src[:i] + '<img src="__PLATE__" alt="%s">' % COVER['alt'] + src[j:]
    R('<div class="plate-sub">A test drive at the store</div>', '<div class="plate-sub">%s</div>' % COVER['caption'])
    R('<div class="plate-cap">Plate I &middot; The Family Album</div>', '<div class="plate-cap">The Cover</div>')
else:
    a = src.rfind('<div class="plate-wrap">', 0, i); b = src.find('<div class="part"><span>The News</span></div>'); assert 0 < a < b
    src = src[:a] + src[b:]
R('No. 146', 'No. 147'); R('Tuesday &middot; November 17 &middot; 2026', 'Wednesday &middot; November 18 &middot; 2026')
S('<div class="tiles">', '<div class="plate-wrap">' if COVER else '<div class="part"><span>The News</span></div>', '''<div class="tiles">
  <div class="tile"><div class="v">54&deg;</div><div class="k">Sunny</div></div>
  <div class="tile"><div class="v">4:49</div><div class="k">Sunset</div></div>
  <div class="tile urg"><div class="v">8</div><div class="k">Days to Thanksgiving</div></div>
</div>
''')
S('<div class="wire lead">', '<div class="part"><span>The Almanac</span></div>', '''<div class="wire lead"><div><span class="kick">The Lead</span><h3>North Tonawanda's New Two Miles of Bike Path Are Open</h3>
<p>North Tonawanda opened a new two-mile stretch of bike path on Tuesday, a $2.7 million extension nearly a decade in the making, the <i>Niagara Gazette</i> reports. It runs along the Erie Canal between the North Tonawanda Botanical Gardens and Mayor's Park.</p>
<p>The new piece closes a gap. There is now a continuous run of trail from the Botanical Gardens all the way to Niagara Falls, the paper says, and a better connection to the state's trail system.</p>
</div></div>
<h2 class="sec">The National Wire</h2>
<div class="wire"><div class="num">1</div><div><h3>Trump Lands in China for the Three-Way Summit</h3><p>President Trump arrived Wednesday in Shenzhen, a center of China's tech industry, where Chinese leader Xi Jinping met him on a red carpet ahead of a summit with Xi and Russia's Vladimir Putin, CBS reports. The Kremlin's spokesman said Putin would meet Trump at a reception before the three sit down together, and Trump may also meet North Korea's Kim Jong Un.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Alaska's Senate Seat Flips</h3><p>Former Rep. Mary Peltola, a Democrat, defeated Republican Sen. Dan Sullivan in Alaska, CBS News projects, two weeks after Election Day; that gives Democrats 56 Senate seats to the Republicans' 44. Peltola, 53, is set to become the first Alaska Native elected to the Senate.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Update: "Zero Evidence" the Outages Are Linked</h3><p>Secretary of State Marco Rubio said there is "zero evidence" that the recent failures in air travel, banking and other systems are connected, CBS reports. He said he understood people are uneasy and wanted to be clear that the United States is not under systemic attack.</p></div></div>
<h2 class="sec">The Home Wire</h2>
<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Shovels in at High Falls State Park</h3><p>A ceremonial groundbreaking is set for this morning for High Falls State Park, 40 acres mostly in the Genesee River gorge in downtown Rochester, WXXI reports. "This park is transformational for downtown Rochester," said Lisa Baron of the nonprofit Greentopia, which expects to help with programming and job training. "But we want it transformational for everybody."</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Jamestown &middot; Natalie Merchant Rides in the Macy's Parade</h3><p>Jamestown native Natalie Merchant will perform on a float in this year's Macy's Thanksgiving Day Parade in New York City, the <i>Observer</i> reports. Others on the floats include the Indigo Girls, Blues Traveler, Queen Latifah and Jimmy Fallon with The Roots.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Sherman &middot; A Petition to Dissolve the Village</h3><p>Sherman's village board has received a petition to dissolve the village, and Mayor Colleen Meeder is pushing back on what she calls "false narratives" around it, the <i>Observer</i> reports. The claims she disputes are that the village does not support its fire department and that it is going bankrupt.</p></div></div>
<h2 class="sec">The Marquee</h2>
<div class="wire"><div class="num">1</div><div><h3>Glastonbury Names Its Headliners</h3><p>Harry Styles, Billie Eilish and Sam Fender will headline England's Glastonbury Festival next June, organizers announced Wednesday, Billboard reports. It will be the famous festival's first edition since 2025.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3><i>Dancing With the Stars</i> Has Its Finalists</h3><p>Harry Shum Jr. and partner Jenna Johnson were eliminated Tuesday, one week short of the finale, Us Weekly reports. That leaves Ezra Frech, Maura Higgins, Connor Wood, Tatyana Ali and Amber Glenn for the finale, live on ABC next Tuesday at 8.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Tonight on TV: Taylor Swift at the CMAs</h3><p>Taylor Swift returns to the stage at the CMA Awards, country music's annual awards show, tonight, TVLine reports. Also new today: Nicolas Cage plays the football coach and broadcaster John Madden in <i>Madden</i> on Prime Video.</p></div></div>
<h2 class="sec">The Gridiron</h2>
<div class="wire"><div><h3>Bills: A Rookie Guard to Injured Reserve</h3><p>The Bills put guard Ar'maj Reed-Adams, a sixth-round pick this year, on injured reserve; he had been on the injury report with back and elbow trouble, ProFootballTalk reports. Defensive back Te'Cory Couch, released before the Jets game, is back on the practice squad after clearing waivers, per Buffalo Rumblings.</p></div></div>
<div class="wire"><div><h3>Jets: The Long View</h3><p>The Jets are in line for three first-round picks in the 2027 draft, and two of them would land in the top six as the standings sit now, Gang Green Nation reports, using the draft-order site Tankathon. The site's point: that is enough to add several impact players, perhaps a quarterback among them.</p></div></div>
<div class="wire"><div><h3>The Sunday Tax &middot; Week 11</h3><p>One day left before the first sheet locks: Colts at Texans, Thursday at 8:15. Picks at <a href="https://tally.so/r/RGOakJ">tally.so/r/RGOakJ</a>, standings at <a href="https://benthambulletin.github.io/pool/">benthambulletin.github.io/pool</a>; $5 a week, straight-up winners, the pot to the best record, and anyone with the link can play.</p></div></div>
''')
S('<p class="wlede">', '<div class="line"><span class="lbl t">Next 24 hours</span>', '''<p class="wlede">Morning mist burns off to full sun and a light southwest breeze</p>
<div class="wxrow">
  <div class="wxc"><div class="k">Tonight</div><div class="v">41&deg;</div><div class="s">partly cloudy</div></div>
  <div class="wxc"><div class="k">Wind</div><div class="v">6&ndash;12</div><div class="s">mph, southwest</div></div>
  <div class="wxc"><div class="k">Rain</div><div class="v">0%</div><div class="s">dry</div></div>
  <div class="wxc"><div class="k">Normal</div><div class="v">47&deg;</div><div class="s">for the date</div></div>
</div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">39<sup>&deg;</sup></div><div class="d">Mist<br>high 54&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">41<sup>&deg;</sup></div><div class="d">Clear<br>high 55&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">37<sup>&deg;</sup></div><div class="d">Mostly clear<br>high 58&deg;</div></div>
</div>
<div class="towns lakes">
  <div class="town"><div class="n">Lake Erie</div><div class="t">54<sup>&deg;</sup></div><div class="d">off Buffalo, Tuesday</div></div>
  <div class="town"><div class="n">Lake Ontario</div><div class="t">54<sup>&deg;</sup></div><div class="d">off Rochester, Tuesday</div></div>
</div>
<div class="strip5">
  <div><div class="d">Wed</div><div class="i">&#9728;</div><div class="h">54</div><div class="w">sunny</div></div>
  <div><div class="d">Thu</div><div class="i">&#9925;</div><div class="h">58</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Fri</div><div class="i">&#9728;</div><div class="h">58</div><div class="w">sunny</div></div>
  <div><div class="d">Sat</div><div class="i">&#9728;</div><div class="h">64</div><div class="w">sunny</div></div>
  <div><div class="d">Sun</div><div class="i">&#9925;</div><div class="h">62</div><div class="w">sun, slight chance showers</div></div>
</div>
''')
S('<div class="line"><span class="lbl t">Next 24 hours</span>', '<h2 class="sec">The Almanac Sky</h2>', '<div class="line"><span class="lbl t">Next 24 hours</span></div>' + chart + '''<div class="line"><span class="lbl t">Outdoor window</span> From 10 to 4 it is above 50 and sunny, warmest about 1. A good day to try a new trail.</div>
<div class="line"><span class="lbl t">Frost watch</span> None here tonight. Scottsville is the cold spot at 36.</div>
''')
S('<h2 class="sec">The Almanac Sky</h2>', '<h2 class="sec">Coming Up</h2>', '''<h2 class="sec">The Almanac Sky</h2>
<div class="wxrow">
  <div class="wxc"><div class="k">Moon</div><svg class="moonmini" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#5a4d3b"/><path d="M50 4 A46 46 0 0 1 50 96 A11.1 46 0 0 1 50 4Z" fill="#f4e5b4"/></svg><div class="s">waxing gibbous</div></div>
  <div class="wxc"><div class="k">Sunrise</div><div class="v">7:11</div><div class="s">a.m.</div></div>
  <div class="wxc"><div class="k">Daylight</div><div class="v">9h 38m</div><div class="s">2 min less</div></div>
</div>
<p class="skynote"><b>Tonight:</b> the moon, now more than half lit and growing (that is what "waxing gibbous" means), is in Aquarius and sets at 12:13 a.m. Saturn sits highest in the south in mid-evening and is the only bright planet up before 11. The full moon is Tuesday.</p>
<div class="touch-head">The Stars &middot; for fun</div>
<div class="stars slim">
<div class="star"><span class="sgn">Aries</span> <span class="who">Kaylani, Luka</span><br>The moon has moved on and left you alone. Coast.</div>
<div class="star"><span class="sgn">Cancer</span> <span class="who">Gregg</span><br>The moon is in a friendly spot for you. Good day to fix the thing that has been squeaking.</div>
<div class="star"><span class="sgn">Leo</span> <span class="who">Leah, Tommy</span><br>The pressure is off. Do one thing slowly, on purpose.</div>
<div class="star"><span class="sgn">Virgo</span> <span class="who">Derek, Joanne</span><br>The moon is directly across from you. Someone will need a favor; it will not take long.</div>
<div class="star"><span class="sgn">Scorpio</span> <span class="who">Ariel, Claire, Garret</span><br>The friction is over and the words come easily today. Send the message you have been drafting.</div>
</div>
''')
S('<h2 class="sec">Coming Up</h2>', '<div class="dbl"><div class="a">', '''<h2 class="sec">Coming Up</h2>
<div class="calbox"><div class="calrow"><div class="cd">Tonight</div><div>Central Michigan at UB, 7:30</div></div>
<div class="calrow"><div class="cd">Sun</div><div>Dolphins at Bills, 1:00; Jets at Chargers</div></div>
<div class="calrow"><div class="cd">Nov 26</div><div>Thanksgiving; Chiefs at Bills, 8:20</div></div>
<div class="calnote">Migraine log: Joanne, Monday; Garret, Saturday. Four logged this month.</div>
</div>
<h2 class="sec">The Ledger</h2>
<div class="ledger"><div class="num"><div class="cap">People who watched 49ers&ndash;Cowboys</div><div class="big">27.13 million</div></div>
<div class="txt">That was the television audience for Sunday's game, ProFootballTalk reports. The final was 46&ndash;40, so nobody left early.</div></div>
<h2 class="sec">On This Day</h2>
<div class="otd"><b>November 18, 1883</b> &mdash; America's railroads switched to standard time zones, ending the days when every town set its own clocks by the sun.</div>
<h2 class="sec">Question of the Day</h2>
<div class="qotd">Two wheels, one chain, no engine. I only stay upright while I am going somewhere. What am I? <i>Answer below the fold.</i></div>
''')
R('<b>Question of the Day:</b> A shopping cart.', '<b>Question of the Day:</b> A bicycle.')
S('headlines via ', ' &middot; scores and stats via Sportradar', 'headlines via the <i>Niagara Gazette</i>, CBS, WXXI, the Dunkirk <i>Observer</i>, Billboard, Us Weekly, TVLine, ProFootballTalk, Buffalo Rumblings, Gang Green Nation')
ed = {'date': '2026-11-18', 'no': 147, 'body_html': src, 'plate_path': COVER['path'] if COVER else None, 'plate_caption': COVER['caption'] if COVER else '',
      'headline': "North Tonawanda's new bike path opens · Trump lands in China · Alaska's Senate seat flips"}
for p in ['/home/claude/site/data/edition-2026-11-18.json', '/home/claude/edition-2026-11-18.json']:
    json.dump(ed, open(p, 'w'), ensure_ascii=False, indent=1)
print('ok', len(src), bool(COVER))
