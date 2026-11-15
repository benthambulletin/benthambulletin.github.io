import json, sys
sys.path.insert(0, '/home/claude'); from curve import curve
src = json.load(open('/home/claude/site/data/edition-2026-11-14.json'))['body_html']
def R(a, c, n=1):
    global src
    assert src.count(a) == n, ('R', a[:60], src.count(a)); src = src.replace(a, c)
def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50]); src = src[:i] + new + src[j:]
f = json.load(open('/home/claude/site/data/forecast.json'))
assert f['generated_utc'].startswith('2026-11-15')
assert [f['towns'][n]['observation']['temp_f'] for n in ['North Tonawanda', 'Dunkirk', 'Scottsville']] == [39, 40, 38]
assert f['lakes']['readings'] == {'Lake Erie (Buffalo)': 55, 'Lake Ontario (Rochester)': 54} and 'Sat Nov 14 2026 The water temperature off Buffalo' in f['lakes']['text']
hourly = f['towns']['North Tonawanda']['hourly']; assert 'T06:00' in hourly[0]['start']
chart = curve(hourly, 7 * 60 + 7, 16 * 60 + 51)

cover = '''<svg viewBox="0 0 750 375" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A drawing of a football on a kicking tee in front of goalposts under drifting gray clouds">
<rect width="750" height="375" fill="#cfd3d1"/>
<g fill="#eef0ee" opacity=".9"><g><ellipse cx="140" cy="70" rx="90" ry="22"/><ellipse cx="200" cy="56" rx="60" ry="20"/><animateTransform attributeName="transform" type="translate" values="-40 0;60 0;-40 0" dur="38s" repeatCount="indefinite"/></g>
<g><ellipse cx="520" cy="96" rx="110" ry="24"/><ellipse cx="590" cy="80" rx="70" ry="20"/><animateTransform attributeName="transform" type="translate" values="40 0;-70 0;40 0" dur="46s" repeatCount="indefinite"/></g></g>
<rect y="285" width="750" height="90" fill="#2f5e3e"/>
<g stroke="#f8eedb" stroke-width="3" opacity=".8"><line x1="0" y1="312" x2="750" y2="312"/><line x1="0" y1="350" x2="750" y2="350"/></g>
<g stroke="#e8b100" stroke-width="9" stroke-linecap="round" fill="none"><line x1="375" y1="285" x2="375" y2="205"/><line x1="285" y1="205" x2="465" y2="205"/><line x1="285" y1="205" x2="285" y2="80"/><line x1="465" y1="205" x2="465" y2="80"/></g>
<g><animateTransform attributeName="transform" type="translate" values="0 0;0 -5;0 0" dur="3.2s" repeatCount="indefinite"/>
<ellipse cx="375" cy="318" rx="46" ry="27" fill="#9c3216" transform="rotate(-18 375 318)"/>
<g stroke="#f8eedb" stroke-width="3" stroke-linecap="round" transform="rotate(-18 375 318)"><line x1="352" y1="318" x2="398" y2="318"/><line x1="362" y1="311" x2="362" y2="325"/><line x1="375" y1="311" x2="375" y2="325"/><line x1="388" y1="311" x2="388" y2="325"/></g></g>
<rect x="362" y="345" width="26" height="9" rx="3" fill="#cf6f1a"/>
</svg>'''
R('<img src="__PLATE__" alt="A boy tending a backyard fire pit at dusk">', cover)
R('<div class="plate-sub">Tending the fire</div>', '<div class="plate-sub">Game day under a gray sky</div>')
R('No. 143', 'No. 144'); R('Saturday &middot; November 14 &middot; 2026', 'Sunday &middot; November 15 &middot; 2026')
S('<div class="tiles">', '<div class="plate-wrap">', '''<div class="tiles">
  <div class="tile"><div class="v">45&deg;</div><div class="k">Cloudy</div></div>
  <div class="tile"><div class="v">4:51</div><div class="k">Sunset</div></div>
  <div class="tile urg"><div class="v">11</div><div class="k">Days to Thanksgiving</div></div>
</div>
''')
S('<div class="wire lead">', '<div class="part"><span>The Almanac</span></div>', '''<div class="wire lead"><div><span class="kick">The Lead &middot; Update</span><h3>Starship Comes Home, and the Tower Catches It</h3>
<p>SpaceX caught its Starship spacecraft out of the sky Saturday. After about 22 hours in orbit, the top half of the world's biggest rocket came back through the heat of reentry, flipped upright over its Texas launch site, and settled into two giant mechanical arms on the launch tower, CBS reports. The BBC notes the arms are nicknamed "chopsticks."</p>
<p>It was the first time a Starship has been recovered from orbit; earlier test flights ended with planned splashdowns in the ocean. The other half of the plan did not work: the attempt to catch the booster, the bottom part of the rocket, was called off minutes after Friday's launch.</p>
<div class="pull">"One of the most incredible and historic engineering feats of all time has just happened right in front of our eyes."<br>&mdash; Jessie Anderson, SpaceX commentator</div>
<p>Why it matters: a rocket that can be caught and flown again is far cheaper than one thrown away after each trip. SpaceX has to recover both halves reliably before that pays off, the BBC says, and founder Elon Musk says the goal is cheaper launches to orbit, the moon and, eventually, Mars.</p>
</div></div>
<div class="wire"><div><h3>Last Call: Should the Paper Come at 6&nbsp;a.m. or 8&nbsp;a.m.?</h3><p>Four votes are in on what time of the morning the Bulletin is sent, and it is close. The choice is the way it is now, a text at about 8 a.m., or published and texted on its own at 6 a.m. so it is waiting when you wake up. The poll closes tonight: vote at <a href="https://tally.so/r/5XjVlv">tally.so/r/5XjVlv</a>, ten seconds, and the count runs here Monday.</p></div></div>
<h2 class="sec">The Sunday Spotlight</h2>
<div class="spot"><h3>This Winter's Heating Bill</h3>
<p><i>An AI wrote this section.</i></p>
<p><b>What the forecast says.</b> National Grid, the company that delivers power to much of upstate New York, put out its winter forecast last month, covering Nov. 1 through March 31. A typical home heating with natural gas (713 therms, the unit gas is billed in) should pay about $9 less than last winter. The electric bill goes the other way: up 3 to 5 percent, or $22 to $39 over the five months, depending on where you live, CNY Central reports. Both numbers assume an ordinary winter.</p>
<p><b>Why gas barely moves.</b> A bill has two parts. Supply is the gas or electricity itself, passed along at cost. Delivery is the pipes, wires and crews. The price of gas itself is down, but delivery charges are up under a three-year rate plan the state approved in August 2025, which pays for new equipment and for replacing about 112 miles of leak-prone gas pipe, FingerLakes1 reports. One eats most of the other.</p>
<p><b>The fuel that did jump.</b> Heating oil. The state's energy agency listed it at $6.21 a gallon in early October, up 67 percent from $3.72 a year earlier. Propane was up about 13 percent. Anyone with a tank in the yard is facing a very different winter than anyone on a gas line.</p>
<p><b>What it means here.</b> For a gas-heated house, this winter should cost about what last winter did, and the weather will matter more than the rates. A cold January moves a bill far more than $9. NYSEG and RG&amp;E, which serve parts of Western New York and the Rochester area, have not put out a comparable winter number that we could find; last February they said the electricity they buy for customers cost 36 to 44 percent more than a year before, so their customers have reason to watch the supply line on the bill.</p>
<p><b>The cheap fixes, by National Grid's own figures.</b> Each degree you turn the thermostat down may save 1 to 3 percent a year on heating. Sealing drafts may save about 15 percent on heating and cooling. Change the furnace filter monthly in heating season. These are the utility's estimates, and they are modest: none of them makes a big bill small.</p>
<p><b>Help paying.</b> HEAP, the state's Home Energy Assistance Program, which gives grants toward heating bills, opened for the season Nov. 2. The income limit is $3,563 a month for one person, $4,659 for two and $6,852 for a family of four; apply through the county social services office. National Grid also has a budget plan that spreads the year's cost over 12 even payments.</p>
<p><b>Coming down the road.</b> The rate plan runs three years, so delivery charges are set to keep rising after this winter. And the forecast was made with prices from the end of September; a hard cold snap can still change the supply side.</p></div>
<h2 class="sec">The National Wire</h2>
<div class="wire"><div class="num">1</div><div><h3>Update: A Wiring Job Stopped the Flights</h3><p>Friday's nationwide ground stop traced back to work replacing old copper wire with fiber-optic cable in the air traffic control system, Transportation Secretary Sean Duffy said, according to the BBC; he said the government is trying to learn whether the contractor, L3Harris, or faulty equipment was to blame. Cancellations carried into Saturday as airlines cleared the backlog.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Measles Is No Longer "Eliminated" Here</h3><p>The United States has lost its status as a country where measles is eliminated, a label it had held for a quarter century, because outbreaks are no longer ending within a year, NPR reports, citing researchers who told KFF Health News of the Pan American Health Organization's decision. More than 8,000 people have been sickened and more than 830 hospitalized in the past two years; two doses of the measles vaccine prevent about 97 percent of infections.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Zelenskyy: U.S. Asked About Land for NATO</h3><p>Ukrainian President Volodymyr Zelenskyy said American negotiators asked him for the first time whether Ukraine would pull out of Donbas, its contested eastern region, in exchange for membership in NATO, the Western military alliance, CBS reports. He said that if a full package of security guarantees, troops, weapons and money were offered, he would put the question to Ukrainians.</p></div></div>
<h2 class="sec">The Home Wire</h2>
<div class="wire"><div class="num">1</div><div><h3>Wilson &middot; On to the State Final</h3><p>Wilson High School beat St. Lawrence in a state semifinal Saturday in Moravia and will play for a state championship, the <i>Lockport Journal</i> reports. Abigail Labarre scored the goal that let coach Jeff Hart start emptying his bench.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Dunkirk &middot; Holiday Blood Drives Start Monday</h3><p>The Red Cross begins its holiday-season blood drives in Dunkirk on Monday and is asking especially for type O donors, the <i>Observer</i> reports. Anyone who gives between Nov. 23 and Dec. 6 gets a <i>Wheel of Fortune</i> mug and a chance at a trip to a taping of the show.</p></div></div>
<h2 class="sec">The Marquee</h2>
<div class="wire"><div class="num">1</div><div><h3>Phil Collins Gets His Ovation</h3><p>Phil Collins, who walks with two canes and could not perform, cried at a long ovation as he entered the Rock &amp; Roll Hall of Fame on Saturday night in Los Angeles, Page Six reports. Oprah Winfrey inducted the late Luther Vandross, Oasis, Sade and Queen Latifah went in too, and U2 opened the show with a surprise two-song set, according to Billboard.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>The Kids Have Spoken: BTS</h3><p>The Korean pop group BTS won three Kids' Choice Awards on Saturday, including favorite group for a fifth time, a record, Billboard reports. The show aired on CBS for the first time.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>The Voice at the Bottom of "Elvira"</h3><p>Richard Sterban, the bass singer who sang the "oom poppa, mow mow" in the Oak Ridge Boys' hit "Elvira," died Saturday at 83, Billboard reports. He started out singing backup for Elvis Presley and retired from touring last year.</p></div></div>
<h2 class="sec">The Gridiron</h2>
<div class="wire"><div><h3>Bills at Jets, 1:00</h3><p>The Bills (7&ndash;1) activated Jordan Hancock from injured reserve for today's game; he has been out since Week 2 with a hamstring injury, and his return leaves them deep at safety, Buffalo Rumblings reports. To make room, they released Te'Cory Couch.</p></div></div>
<div class="wire"><div><h3>Jets: A Rookie Joins In</h3><p>The Jets (2&ndash;7) activated rookie safety VJ Payne, a seventh-round pick who missed the preseason with a bone bruise, and waived lineman Kohl Levao, Gang Green Nation reports. The site's forecast for East Rutherford: chilly and partly cloudy, with wind of 10 to 15 mph and gusts to 25.</p></div></div>
''')
S('<p class="wlede">', '<div class="line"><span class="lbl t">Next 24 hours</span>', '''<p class="wlede">Gray from start to finish: a stray sprinkle early, then only clouds</p>
<div class="wxrow">
  <div class="wxc"><div class="k">Tonight</div><div class="v">35&deg;</div><div class="s">cloudy</div></div>
  <div class="wxc"><div class="k">Wind</div><div class="v">6&ndash;9</div><div class="s">mph, northwest</div></div>
  <div class="wxc"><div class="k">Rain</div><div class="v">15%</div><div class="s">early</div></div>
  <div class="wxc"><div class="k">Normal</div><div class="v">48&deg;</div><div class="s">for the date</div></div>
</div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">39<sup>&deg;</sup></div><div class="d">Cloudy<br>high 45&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">40<sup>&deg;</sup></div><div class="d">Cloudy<br>high 46&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">38<sup>&deg;</sup></div><div class="d">Light rain<br>high 44&deg;</div></div>
</div>
<div class="towns lakes">
  <div class="town"><div class="n">Lake Erie</div><div class="t">55<sup>&deg;</sup></div><div class="d">off Buffalo, Saturday</div></div>
  <div class="town"><div class="n">Lake Ontario</div><div class="t">54<sup>&deg;</sup></div><div class="d">off Rochester, Saturday</div></div>
</div>
<div class="strip5">
  <div><div class="d">Sun</div><div class="i">&#9729;</div><div class="h">45</div><div class="w">cloudy</div></div>
  <div><div class="d">Mon</div><div class="i">&#9729;</div><div class="h">49</div><div class="w">mostly cloudy</div></div>
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">54</div><div class="w">sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#9728;</div><div class="h">56</div><div class="w">sunny</div></div>
  <div><div class="d">Thu</div><div class="i">&#9925;</div><div class="h">57</div><div class="w">mostly sunny</div></div>
</div>
''')
S('<div class="line"><span class="lbl t">Next 24 hours</span>', '<h2 class="sec">The Almanac Sky</h2>', '<div class="line"><span class="lbl t">Next 24 hours</span></div>' + chart + '''<div class="line"><span class="lbl t">Outdoor window</span> Dry after the early sprinkle and stuck at 43 from late morning through dusk. Any hour works; none of them is sunny.</div>
<div class="line"><span class="lbl t">Frost watch</span> None tonight under the clouds. Scottsville is the one to watch Monday night, with a low of 32.</div>
''')
S('<h2 class="sec">The Almanac Sky</h2>', '<h2 class="sec">Coming Up</h2>', '''<h2 class="sec">The Almanac Sky</h2>
<div class="wxrow">
  <div class="wxc"><div class="k">Moon</div><svg class="moonmini" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#5a4d3b"/><path d="M50 4 A46 46 0 0 1 50 96 A15.3 46 0 0 0 50 4Z" fill="#f4e5b4"/></svg><div class="s">waxing crescent</div></div>
  <div class="wxc"><div class="k">Sunrise</div><div class="v">7:07</div><div class="s">a.m.</div></div>
  <div class="wxc"><div class="k">Daylight</div><div class="v">9h 44m</div><div class="s">2 min less</div></div>
</div>
<p class="skynote"><b>Tonight:</b> the moon, a third lit, is in Capricornus and sets at 10:03; the clouds will likely hide it. Saturn is the one bright planet up, highest in the south around 9. The next full moon is Nov. 24.</p>
<div class="touch-head">The Stars &middot; for fun</div>
<div class="stars slim">
<div class="star"><span class="sgn">Aries</span> <span class="who">Kaylani, Luka</span><br>The moon is on your side today. Say yes to the invitation.</div>
<div class="star"><span class="sgn">Cancer</span> <span class="who">Gregg</span><br>Nothing in the sky is asking anything of you. Enjoy the game.</div>
<div class="star"><span class="sgn">Leo</span> <span class="who">Leah, Tommy</span><br>The moon sits across from you. Someone else may want the last word; let them have it.</div>
<div class="star"><span class="sgn">Virgo</span> <span class="who">Derek, Joanne</span><br>A blank page of a day. Fill it with something that is not a chore.</div>
<div class="star"><span class="sgn">Scorpio</span> <span class="who">Ariel, Claire, Garret</span><br>A little static today. Read the message twice before answering it.</div>
</div>
''')
S('<h2 class="sec">Coming Up</h2>', '<div class="dbl"><div class="a">', '''<h2 class="sec">Coming Up</h2>
<div class="calbox"><div class="calrow"><div class="cd">Today</div><div>Bills at Jets, 1:00</div></div>
<div class="calrow"><div class="cd">Wed</div><div>Central Michigan at UB, 7:30</div></div>
<div class="calrow"><div class="cd">Nov 22</div><div>Dolphins at Bills, 1:00; Jets at Chargers, 4:05</div></div>
<div class="calrow"><div class="cd">Nov 26</div><div>Thanksgiving; Chiefs at Bills, 8:20</div></div>
<div class="calnote">Migraine log: Garret, Saturday. Three logged this month.</div>
</div>
<h2 class="sec">The Week Ahead</h2>
<div class="line"><b>Weather.</b> Last week: a slide from 60 on Tuesday to 41 on Friday, with the coldest dawn 32 on Wednesday. This week climbs back: 49 Monday, then sunny and 54 to 57 Tuesday through Thursday.</div>
<div class="line"><b>Games.</b> Bills at the Jets today at 1:00; Central Michigan at UB Wednesday night; Dolphins at Bills next Sunday.</div>
<div class="line"><b>Thanksgiving.</b> A week from Thursday.</div>
<div class="line"><b>Next Sunday's Spotlight.</b> What Thanksgiving dinner costs this year, and why.</div>
<h2 class="sec">The Sunday Question</h2>
<div class="qotd"><b>This week, with Thanksgiving a week from Thursday: what one dish has to be on the table, and who makes it best?</b><br>Send it at <a href="https://tally.so/r/rjxDpl">tally.so/r/rjxDpl</a> this week. Answers run here next Sunday under your names.</div>
<h2 class="sec">The Ledger</h2>
<div class="ledger"><div class="num"><div class="cap">Days to Christmas</div><div class="big">40</div></div>
<div class="txt">Counting from this morning. That is six Sundays, including this one.</div></div>
<h2 class="sec">On This Day</h2>
<div class="otd"><b>November 15, 1926</b> &mdash; NBC went on the air as a radio network, 100 years ago today, with a gala broadcast from the Waldorf-Astoria hotel in New York.</div>
<h2 class="sec">Question of the Day</h2>
<div class="qotd">I never leave the wall, yet the whole house argues over me. Nudge me up and the furnace wakes. What am I? <i>Answer below the fold.</i></div>
''')
R('<b>Question of the Day:</b> A zipper.', '<b>Question of the Day:</b> A thermostat.')
S('headlines via ', ' &middot; scores and stats via Sportradar', 'headlines via CBS, the BBC, NPR, CNY Central, FingerLakes1, the <i>Lockport Journal</i>, the Dunkirk <i>Observer</i>, NYSEG, Page Six, Billboard, Buffalo Rumblings, Gang Green Nation')
ed = {'date': '2026-11-15', 'no': 144, 'body_html': src, 'plate_path': None, 'plate_caption': 'Game day under a gray sky',
      'headline': "Starship caught · This winter's heating bill · Bills at Jets, 1:00"}
for p in ['/home/claude/site/data/edition-2026-11-15.json', '/home/claude/edition-2026-11-15.json']:
    json.dump(ed, open(p, 'w'), ensure_ascii=False, indent=1)
print('ok', len(src))
