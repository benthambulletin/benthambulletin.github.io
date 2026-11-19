import json, sys, os
sys.path.insert(0, '/home/claude'); from curve import curve
src = json.load(open('/home/claude/site/data/edition-2026-11-18.json'))['body_html']
def R(a, c, n=1):
    global src
    assert src.count(a) == n, ('R', a[:60], src.count(a)); src = src.replace(a, c)
def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50]); src = src[:i] + new + src[j:]
f = json.load(open('/home/claude/site/data/forecast.json'))
assert f['generated_utc'].startswith('2026-11-19')
assert [f['towns'][n]['observation']['temp_f'] for n in ['North Tonawanda', 'Dunkirk', 'Scottsville']] == [37, 50, 37]
assert f['lakes']['readings'] == {'Lake Erie (Buffalo)': 54, 'Lake Ontario (Rochester)': 54} and 'Wed Nov 18 2026 The water temperature off Buffalo' in f['lakes']['text']
hourly = f['towns']['North Tonawanda']['hourly']; assert 'T05:00' in hourly[0]['start']
chart = curve(hourly, 7 * 60 + 12, 16 * 60 + 48)
COVER = json.load(open('/home/claude/cover148.json'))
i = src.find('<img src="__PLATE__"'); j = src.find('>', i) + 1; assert i > 0
src = src[:i] + '<img src="__PLATE__" alt="%s">' % COVER['alt'] + src[j:]
i = src.find('<div class="plate-sub">'); j = src.find('</div>', i) + 6; src = src[:i] + '<div class="plate-sub">%s</div>' % COVER['caption'] + src[j:]
R('<div class="plate-cap">The Cover</div>', '<div class="plate-cap">Plate I &middot; The Family Album</div>')
R('No. 147', 'No. 148'); R('Wednesday &middot; November 18 &middot; 2026', 'Thursday &middot; November 19 &middot; 2026')
S('<div class="tiles">', '<div class="plate-wrap">', '''<div class="tiles">
  <div class="tile"><div class="v">58&deg;</div><div class="k">Fog, Then Sun</div></div>
  <div class="tile"><div class="v">4:48</div><div class="k">Sunset</div></div>
  <div class="tile urg"><div class="v">7</div><div class="k">Days to Thanksgiving</div></div>
</div>
''')
S('<div class="wire lead">', '<div class="part"><span>The Almanac</span></div>', '''<div class="wire lead"><div><span class="kick">The Lead</span><h3>Trump, Xi and Putin in One Room</h3>
<p>President Trump, China's Xi Jinping and Russia's Vladimir Putin sat down together Thursday in Shenzhen, China, a rare meeting of the leaders of three of the world's most powerful countries, CBS reports. Each made a short opening statement, and then they talked behind closed doors for about an hour and a half.</p>
<p>What they said in there is not known. None of the three spoke to reporters afterward, there was no joint statement, and Trump left straight for the airport to fly home.</p>
<p>Before the three-way session, Trump met each of the others alone. With Putin, Russia's state news agency TASS said, the main subject was the war in Ukraine. With Xi, the meeting ran about an hour, and Xi opened by calling relations between China and the United States stable.</p>
<div class="pull">"I think a lot of wonderful things can come out of this, or at least start."<br>&mdash; President Trump, standing beside Putin</div>
</div></div>
<h2 class="sec">The National Wire</h2>
<div class="wire"><div class="num">1</div><div><h3>The Biggest Stock Debut Ever Belongs to an A.I. Company</h3><p>Anthropic, a five-year-old artificial intelligence company, raised more than $81.3 billion by selling shares to the public for the first time, at $83 apiece, NPR reports; that tops the $75 billion SpaceX raised earlier this year. The shares begin trading today on the Nasdaq exchange under the symbol ANT. (A disclosure: this paper is put together with Anthropic's A.I.)</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Waymo Takes Its Robotaxis Off the Freeway</h3><p>Waymo has paused driverless rides on freeways across the United States after California banned them there over safety concerns, the BBC reports. The state's motor vehicle department cited a series of incidents, including robotaxis driving into active construction zones.</p></div></div>
<h2 class="sec">The Home Wire</h2>
<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Hochul Lays Out a Nuclear Plan</h3><p>Gov. Kathy Hochul was in Rochester on Wednesday to unveil a plan for adding nuclear power plants upstate, WXXI reports; the state calls it the Advanced Nuclear Master Plan. She called nuclear power "the most sustainable, the most reliable, and ... the most affordable way we can power our state."</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Erie County &middot; Road Salt Has Doubled in Price</h3><p>The salt Erie County buys for its roads has gone from about $43 a ton in 2022 to more than $93 a ton this year, WKBW reports. Highway departments are stocking up anyway after an unusually mild start to November.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Chautauqua County &middot; An Aerospace Plant Grows</h3><p>The county's Industrial Development Agency approved financial help for a $5.22 million expansion by Rand Aerospace &amp; Defense Group, which is buying the former Serta mattress factory in the town of Ellicott, the <i>Observer</i> reports. The second site is expected to keep Rand's 115 jobs and add 31 over three years.</p></div></div>
<h2 class="sec">The Marquee</h2>
<div class="wire"><div class="num">1</div><div><h3>Ella Langley's Night at the CMAs</h3><p>Ella Langley won entertainer of the year, the top prize, at the 60th Country Music Association Awards in Nashville on Wednesday, and won every category she was nominated in, Page Six reports. "This isn't real life," she said from the stage.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>A Van Gogh Sells for $190.4 Million</h3><p>Sotheby's sold Vincent van Gogh's <i>Chestnut Trees in Blossom</i> in New York on Wednesday for $190.4 million, a record for the artist, the BBC reports; his old record was $117.2 million. The sale went ahead after a last-minute agreement settled a claim that the painting had been sold under duress during the rise of the Nazis.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Tonight on TV: Two Fall Finales</h3><p><i>9-1-1</i> and <i>Grey's Anatomy</i> air their last new episodes of the fall tonight, TVLine reports. Also tonight, <i>The Traitors: New Blood</i> wraps up.</p></div></div>
<h2 class="sec">The Gridiron</h2>
<div class="wire"><div><h3>Bills: The Secondary Is Banged Up</h3><p>Cornerbacks Christian Benford and Dee Alford and tight end Dalton Kincaid all sat out Wednesday's practice, the first of the week before Sunday's game with the Dolphins, ProFootballTalk and Buffalo Rumblings report. The good news is up front: none of the starting offensive linemen missed practice with an injury.</p></div></div>
<div class="wire"><div><h3>Jets: Underdogs in Los Angeles</h3><p>The Chargers, fresh off their first win, are favored over the Jets on Sunday, ProFootballTalk reports.</p></div></div>
<div class="wire"><div><h3>UB 40, Central Michigan 21</h3><p>The Bulls won their sixth straight Wednesday night at home. Next is a trip to Akron on Friday, Nov. 27.</p></div></div>
<div class="wire"><div><h3>The Sunday Tax &middot; Week 11</h3><p>Last call for tonight's game: Colts at Texans kicks off at 8:15 p.m., and that pick locks when it does. Picks at <a href="https://tally.so/r/RGOakJ">tally.so/r/RGOakJ</a>, standings at <a href="https://benthambulletin.github.io/pool/">benthambulletin.github.io/pool</a>; $5 a week, straight-up winners, the pot to the best record, and anyone with the link can play.</p></div></div>
''')
S('<p class="wlede">', '<div class="line"><span class="lbl t">Next 24 hours</span>', '''<p class="wlede">Patchy fog until mid-morning, then sunny and the mildest day of the week so far</p>
<div class="wxrow">
  <div class="wxc"><div class="k">Tonight</div><div class="v">47&deg;</div><div class="s">partly cloudy</div></div>
  <div class="wxc"><div class="k">Wind</div><div class="v">8&ndash;14</div><div class="s">mph, southwest</div></div>
  <div class="wxc"><div class="k">Fog</div><div class="v">to 10</div><div class="s">a.m., patchy</div></div>
  <div class="wxc"><div class="k">Normal</div><div class="v">46&deg;</div><div class="s">for the date</div></div>
</div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">37<sup>&deg;</sup></div><div class="d">Clear<br>high 58&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">50<sup>&deg;</sup></div><div class="d">Clear<br>high 60&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">37<sup>&deg;</sup></div><div class="d">Clear<br>high 63&deg;</div></div>
</div>
<div class="towns lakes">
  <div class="town"><div class="n">Lake Erie</div><div class="t">54<sup>&deg;</sup></div><div class="d">off Buffalo, Wednesday</div></div>
  <div class="town"><div class="n">Lake Ontario</div><div class="t">54<sup>&deg;</sup></div><div class="d">off Rochester, Wednesday</div></div>
</div>
<div class="strip5">
  <div><div class="d">Thu</div><div class="i">&#9728;</div><div class="h">58</div><div class="w">fog, then sunny</div></div>
  <div><div class="d">Fri</div><div class="i">&#9728;</div><div class="h">58</div><div class="w">sunny</div></div>
  <div><div class="d">Sat</div><div class="i">&#9728;</div><div class="h">62</div><div class="w">sunny</div></div>
  <div><div class="d">Sun</div><div class="i">&#9925;</div><div class="h">63</div><div class="w">partly sunny</div></div>
  <div><div class="d">Mon</div><div class="i">&#127783;</div><div class="h">47</div><div class="w">chance showers</div></div>
</div>
''')
S('<div class="line"><span class="lbl t">Next 24 hours</span>', '<h2 class="sec">The Almanac Sky</h2>', '<div class="line"><span class="lbl t">Next 24 hours</span></div>' + chart + '''<div class="line"><span class="lbl t">Outdoor window</span> Late morning through sunset, in the mid to upper 50s once the fog lifts.</div>
<div class="line"><span class="lbl t">Frost watch</span> None tonight; it stays in the upper 40s. Scottsville dips to 36 Friday night.</div>
''')
S('<h2 class="sec">The Almanac Sky</h2>', '<h2 class="sec">Coming Up</h2>', '''<h2 class="sec">The Almanac Sky</h2>
<div class="wxrow">
  <div class="wxc"><div class="k">Moon</div><svg class="moonmini" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#5a4d3b"/><path d="M50 4 A46 46 0 0 1 50 96 A19.9 46 0 0 1 50 4Z" fill="#f4e5b4"/></svg><div class="s">waxing gibbous</div></div>
  <div class="wxc"><div class="k">Sunrise</div><div class="v">7:12</div><div class="s">a.m.</div></div>
  <div class="wxc"><div class="k">Daylight</div><div class="v">9h 36m</div><div class="s">2 min less</div></div>
</div>
<p class="skynote"><b>Tonight:</b> the moon, nearly three-quarters lit, is in Pisces and stays up until 1:19 a.m. Saturn is close by in the southern sky through the evening. Mars and Jupiter do not rise until after 11. The full moon is Tuesday.</p>
<div class="touch-head">The Stars &middot; for fun</div>
<div class="stars slim">
<div class="star"><span class="sgn">Aries</span> <span class="who">Kaylani, Luka</span><br>Another free pass from the moon. Spend it outside.</div>
<div class="star"><span class="sgn">Cancer</span> <span class="who">Gregg</span><br>Still a kind sky for you. Tell the story again; they like it.</div>
<div class="star"><span class="sgn">Leo</span> <span class="who">Leah, Tommy</span><br>Nothing is pulling at you. Make the plan for Saturday now.</div>
<div class="star"><span class="sgn">Virgo</span> <span class="who">Derek, Joanne</span><br>The moon is still across the way. Let somebody else drive.</div>
<div class="star"><span class="sgn">Scorpio</span> <span class="who">Ariel, Claire, Garret</span><br>The sun and moon are getting along, and so will you. Say the nice thing out loud.</div>
</div>
''')
S('<h2 class="sec">Coming Up</h2>', '<div class="dbl"><div class="a">', '''<h2 class="sec">Coming Up</h2>
<div class="calbox"><div class="calrow"><div class="cd">Sun</div><div>Dolphins at Bills, 1:00; Jets at Chargers</div></div>
<div class="calrow"><div class="cd">Nov 26</div><div>Thanksgiving; Chiefs at Bills, 8:20</div></div>
<div class="calrow"><div class="cd">Nov 27</div><div>UB at Akron, noon</div></div>
<div class="calnote">Migraine log: the latest entries are Joanne's on Monday and Garret's on Saturday. Four this month.</div>
</div>
<h2 class="sec">The Ledger</h2>
<div class="ledger"><div class="num"><div class="cap">What Elon Musk spent on the midterms</div><div class="big">$446 million</div></div>
<div class="txt">A record, the BBC reports. He now calls the spending "pretty foolish."</div></div>
<h2 class="sec">On This Day</h2>
<div class="otd"><b>November 19, 1863</b> &mdash; Abraham Lincoln gave the Gettysburg Address. It took about two minutes.</div>
<h2 class="sec">Question of the Day</h2>
<div class="qotd">I arrive without a sound, hide the far end of the street, and leave when the sun gets serious. What am I? <i>Answer below the fold.</i></div>
''')
R('<b>Question of the Day:</b> A rake.', '<b>Question of the Day:</b> Fog.')
S('headlines via ', ' &middot; scores and stats via Sportradar', 'headlines via CBS, NPR, the BBC, WXXI, WKBW, the Dunkirk <i>Observer</i>, Page Six, TVLine, ProFootballTalk, Buffalo Rumblings')
ed = {'date': '2026-11-19', 'no': 148, 'body_html': src, 'plate_path': COVER['path'], 'plate_caption': COVER['caption'],
      'headline': "Trump, Xi and Putin in one room · A record stock debut · Road salt doubles in price"}
for p in ['/home/claude/site/data/edition-2026-11-19.json', '/home/claude/edition-2026-11-19.json']:
    json.dump(ed, open(p, 'w'), ensure_ascii=False, indent=1)
print('ok', len(src))
