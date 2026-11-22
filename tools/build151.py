import json, sys
sys.path.insert(0, '/home/claude'); from curve import curve; from market_chart import market_chart
src = json.load(open('/home/claude/site/data/edition-2026-11-21.json'))['body_html']
def R(a, c, n=1):
    global src
    assert src.count(a) == n, ('R', a[:60], src.count(a)); src = src.replace(a, c)
def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50]); src = src[:i] + new + src[j:]
f = json.load(open('/home/claude/site/data/forecast.json'))
assert f['generated_utc'].startswith('2026-11-22')
assert [f['towns'][n]['observation']['temp_f'] for n in ['North Tonawanda', 'Dunkirk', 'Scottsville']] == [37, 57, 36]
assert f['lakes']['readings'] == {'Lake Erie (Buffalo)': 53, 'Lake Ontario (Rochester)': 54} and 'Sat Nov 21 2026' in f['lakes']['text']
hourly = f['towns']['North Tonawanda']['hourly']; assert 'T05:00' in hourly[0]['start']
chart = curve(hourly, 7 * 60 + 16, 16 * 60 + 46)
m = json.load(open('/home/claude/site/data/market.json')); assert m['last'] == ['2026-11-20', 6910.39]
mkt = market_chart(m, year=2026)
snow = json.load(open('/home/claude/site/data/snow.json'))['places']
assert {k: (v['season_in'], v['normal_in'], v['last_date']) for k, v in snow.items()} == {'North Tonawanda': (0.0, 3.9, '2026-11-21'), 'Orchard Park': (0.0, 5.4, '2026-11-21'), 'Dunkirk': (0.0, 5.4, '2026-11-21'), 'Scottsville': (0.0, 4.8, '2026-11-21')}
cl = json.load(open('/home/claude/site/data/climate.json')); assert cl['date'] == '2026-11-22'
b = cl['stations']['BUF']; assert b['record_high'] == {'f': 69, 'years': ['1953']} and b['record_low'] == {'f': 9, 'years': ['2018']} and b['last_year']['high'] == 46.0 and b['last_year']['low'] == 33.0
assert json.load(open('/home/claude/site/data/alerts.json'))['alerts'] == {}
spot_chart = open('/home/claude/site/data/spotlight/thanksgiving-2026.html').read()
COVER = {'path': '/home/claude/plate151.jpg', 'alt': 'A boy sitting in a red wheelbarrow in a front yard', 'caption': 'Riding in the wheelbarrow'}
i = src.find('<img src="__PLATE__"'); j = src.find('>', i) + 1; assert i > 0
src = src[:i] + '<img src="__PLATE__" alt="%s">' % COVER['alt'] + src[j:]
i = src.find('<div class="plate-sub">'); j = src.find('</div>', i) + 6; src = src[:i] + '<div class="plate-sub">%s</div>' % COVER['caption'] + src[j:]
R('<div class="plate-cap">Plate I &middot; The Family Album</div>', '<div class="plate-cap">Plate I &middot; The Family Album</div>')
R('No. 150', 'No. 151'); R('Saturday &middot; November 21 &middot; 2026', 'Sunday &middot; November 22 &middot; 2026')
R('<div class="sig">&mdash; G.</div>', '<div class="sig">&mdash; Margo</div>')
S('<div class="tiles">', '<div class="plate-wrap">', '''<div class="tiles">
  <div class="tile"><div class="v">65&deg;</div><div class="k">Mostly Sunny</div></div>
  <div class="tile"><div class="v">4:46</div><div class="k">Sunset</div></div>
  <div class="tile urg"><div class="v">4</div><div class="k">Days to Thanksgiving</div></div>
</div>
''')
S('<div class="wire lead">', '<div class="part"><span>The Almanac</span></div>', '''<div class="wire lead"><div><span class="kick">The Lead</span><h3>Storms Line Up for Thanksgiving Week</h3>
<p>A new round of storms is expected to hit both coasts early this week, just as people head out for the holiday, NPR reports. San Francisco's mayor asked people there to skip travel unless it is essential, with extreme high tides and rain forecast from Monday afternoon through Wednesday.</p>
<p>It has already been a wet fall across much of the country. California saw mudslides, waterspouts and flooding this past week, and Florida had coastal flooding and streets under water. NPR traces part of it to a strong El Ni&ntilde;o, a warming of the Pacific that shifts weather around the world.</p>
<p>Closer to home, the trouble is timing rather than storms. The weather service has a chance of rain and snow showers here on Thanksgiving Day itself, after 7 a.m., with a high near 43. Anyone flying out of state this week should check their airline before leaving for the airport.</p>
</div></div>
<h2 class="sec">The Sunday Spotlight</h2>
<div class="spot"><h3>What Thanksgiving Dinner Costs This Year</h3>
<p><i>An AI wrote this section.</i></p>
<p><b>The number.</b> The classic Thanksgiving dinner for ten costs $58.63 this year, about $5.86 a plate, according to the American Farm Bureau Federation's yearly survey. That is up $3.45 from last year, a little over 6 percent, and the first increase since the record of $64.05 in 2022. Volunteer shoppers in all 50 states and Puerto Rico priced the same list of groceries in the first week of November.</p>
''' + spot_chart + '''
<p><b>The turkey did it.</b> A 16-pound bird costs $23.68, up about 10 percent, and it is roughly 40 cents of every dollar on the list. The Farm Bureau's economist, Faith Parum, points to strong demand, tight supplies of turkey and higher costs to raise them. Cranberries, milk, rolls and stuffing all went up too. Four things got slightly cheaper: the veggie tray, pie crusts, frozen peas and whipping cream, each by less than 4 percent.</p>
<p><b>Why the rest crept up.</b> The Farm Bureau names high diesel prices, which make everything cost more to haul, and a shortage of farm workers. Neither shows up as one big jump; they add a little to almost every item.</p>
<p><b>What it means for us.</b> The Northeast pays the most of any region, $61.57 for the same meal. A bigger menu with ham, potatoes and green beans comes to $81.72. Next to the 2022 record it is still a cheaper year; next to last year, a few dollars more.</p>
<p><b>Coming down the road.</b> Turkey prices usually ease after the holiday, when stores stop selling birds below cost to bring shoppers in. The survey runs again next November, and it is the number to compare against.</p>
</div>
<h2 class="sec">The National Wire</h2>
<div class="wire"><div class="num">1</div><div><h3>A Most-Wanted Cartel Boss Is Captured</h3><p>Mexican special forces arrested Fausto Isidro Meza Flores, known as "Chapo Isidro," a drug lord on the FBI's 10 most wanted list, after a shoot-out in Sinaloa on Friday, the BBC reports. Seven suspects and four Mexican soldiers were killed, and the United States is seeking his extradition on charges of flooding the country with fentanyl and other drugs.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Trump Backs a 10 Percent Cap on Credit Card Rates</h3><p>President Trump said Saturday he would work with the incoming Democratic Congress to cap credit card interest rates, the Associated Press reports in PBS NewsHour. The usual proposal is a 10 percent cap; most cards now charge far more, so it would cut what people pay on balances they carry.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>The FBI's Crime Database May Have Been Hacked</h3><p>The FBI is investigating an apparent breach of its National Crime Information Center, the database police across the country use for warrants and background checks, the BBC reports, citing U.S. media. The agency did not comment; asked about it Saturday, the president said he had "just heard" about it.</p></div></div>
<h2 class="sec">The Market</h2>
''' + mkt + '''
<p>The S&amp;P 500, the index of 500 big companies that most retirement funds follow, ended the week Friday at 6,910, 11.6 percent below its Oct. 6 high. That keeps it in a correction, Wall Street's word for a drop of 10 percent or more from a peak. Markets reopen Monday.</p>
<h2 class="sec">The Home Wire</h2>
<div class="wire"><div class="num">1</div><div><h3>Lockport &middot; Homelessness Help, Scattered</h3><p>People working on homelessness in Lockport say the effort is held back by limited federal money, a shortage of affordable housing and agencies that don't coordinate, the <i>Lockport Union-Sun &amp; Journal</i> reports. Niagara County Legislature chair Mike Hill told the paper the county doesn't get federal housing money directly; it flows through the Homeless Alliance of Western New York, which hands it out in competitive grants.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Niagara Falls &middot; Fewer Shootings</h3><p>Shootings with injuries fell 13 percent statewide in the first 10 months of 2026 in the communities in New York's gun-violence program, the <i>Lockport Union-Sun &amp; Journal</i> reports. Niagara Falls police are one of the 29 departments in it, and they reported fewer shootings than at this point last year.</p></div></div>
<h2 class="sec">The Marquee</h2>
<div class="wire"><div class="num">1</div><div><h3>Miley Cyrus Is Married</h3><p>Miley Cyrus married drummer Maxx Morando on Saturday at a private home in Palm Springs, Page Six reports, after five years together. Her parents, Billy Ray and Tish Cyrus, were there, and the Flaming Lips' Wayne Coyne, a longtime friend, officiated.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Britney Spears Says Sorry to Her Family</h3><p>Britney Spears apologized on Instagram on Saturday to the family she has feuded with publicly for years, Page Six reports. "I'm so very sorry for bringing up past issues," she wrote, saying she had done it to protect her heart.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>No New <i>American Psycho</i></h3><p>Director Luca Guadagnino says his new film of Bret Easton Ellis's novel <i>American Psycho</i> is off, the Hollywood Reporter says. "Unfortunately for me, as we speak, it's not happening," he said on a Deadline podcast, without saying why.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>E.J. Carroll, 66</h3><p>E.J. Carroll, a character actor seen on <i>Law &amp; Order</i> and <i>Boardwalk Empire</i>, died after collapsing on a New York City street Thursday on his way to a voiceover job, Us Weekly reports. He was 66, and a cause of death has not been determined.</p></div></div>
<h2 class="sec">The Gridiron</h2>
<div class="wire"><div><h3>Bills: Dolphins at 1, Shorthanded</h3><p>The Bills host Miami at 1 p.m. without cornerback Christian Benford and linebacker Dorian Williams, both ruled out Friday, ProFootballTalk reports; defensive tackle Ed Oliver was added late as questionable with a side injury, along with Damar Hamlin and T.J. Sanders. Josh Allen has 11 rushing touchdowns; one more would make him only the fifth player ever with four straight seasons of 12 or more, and the first who isn't a running back.</p></div></div>
<div class="wire"><div><h3>Jets: Smith Likely in Los Angeles</h3><p>Geno Smith is expected to start at quarterback against the Chargers at 4:05, Gang Green Nation reports.</p></div></div>
''')
S('<h2 class="sec">The Weather Glass</h2>', '<h2 class="sec">The Almanac Sky</h2>', '''<h2 class="sec">The Weather Glass</h2>
<div style="display:flex;gap:.8rem;align-items:center;margin:.5rem 0 .7rem"><img src="/assets/margo.svg" alt="Margo Bentham, in silhouette" style="width:86px;height:auto;flex:none"><div><div style="font-family:'Playfair Display',Georgia,serif;font-weight:700;font-size:1.2rem;line-height:1.1">Margo Bentham</div><div style="font-family:Archivo,Arial,sans-serif;font-size:.6rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--teal,#2f5e3e);margin-top:.2rem">Editor-in-chief &middot; lead meteorologist</div><div style="font-style:italic;font-size:.85rem;color:var(--soft,#664a2c);margin-top:.3rem">Has never once been seen at the office.</div></div></div>
<p class="wlede">Sixty-five and sunny in late November. Enjoy the hell out of it, because Tuesday night it's 25.</p>
<div class="touch-head" style="margin-top:1.1rem">Today</div>
<div class="wxrow">
  <div class="wxc"><div class="k">Tonight</div><div class="v">42&deg;</div><div class="s">showers late</div></div>
  <div class="wxc"><div class="k">Wind</div><div class="v">8</div><div class="s">mph, south</div></div>
  <div class="wxc"><div class="k">Rain</div><div class="v">28%</div><div class="s">after 1 a.m.</div></div>
  <div class="wxc"><div class="k">Normal</div><div class="v">45&deg;</div><div class="s">for the date</div></div>
</div>
<div class="line"><span class="lbl t">Next 24 hours</span></div>''' + chart + '''<div class="line"><span class="lbl t">Records</span> Buffalo's for the date: 69 in 1953; 9 in 2018. A year ago: 46 and 33.</div>
<div class="touch-head" style="margin-top:1.1rem">This week</div>
<div class="strip5">
  <div><div class="d">Sun</div><div class="i">&#9728;</div><div class="h">65</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Mon</div><div class="i">&#9925;</div><div class="h">48</div><div class="w">partly sunny</div></div>
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">39</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#9728;</div><div class="h">42</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Thu</div><div class="i">&#127784;</div><div class="h">43</div><div class="w">rain or snow</div></div>
</div>
<div class="line"><span class="lbl t">Outdoor window</span> All day today; low 60s from 11 a.m. to about 3, the last warm afternoon of the week.</div>
<div class="line"><span class="lbl t">Frost watch</span> Monday night 30, Tuesday night 25: a hard freeze. Bring in anything that minds.</div>
<div class="touch-head" style="margin-top:1.1rem">Around us &middot; at dawn</div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">37<sup>&deg;</sup></div><div class="d">Clear<br>high 65&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">57<sup>&deg;</sup></div><div class="d">Clear<br>high 64&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">36<sup>&deg;</sup></div><div class="d">Clear<br>high 67&deg;</div></div>
</div>
<div class="towns lakes">
  <div class="town"><div class="n">Lake Erie</div><div class="t">53<sup>&deg;</sup></div><div class="d">off Buffalo, Saturday</div></div>
  <div class="town"><div class="n">Lake Ontario</div><div class="t">54<sup>&deg;</sup></div><div class="d">off Rochester, Saturday</div></div>
</div>
<div class="line" style="margin-top:.4rem"><span class="lbl t">Snow so far</span> since July 1, through Saturday. Not a flake yet anywhere.</div>
<div class="towns snow"><div class="town"><div class="n">North Tonawanda</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 3.9"</div></div><div class="town"><div class="n">Orchard Park</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 5.4"</div></div><div class="town"><div class="n">Dunkirk</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 5.4"</div></div><div class="town"><div class="n">Scottsville</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 4.8"</div></div></div>
''')
S('<h2 class="sec">The Almanac Sky</h2>', '<h2 class="sec">Coming Up</h2>', '''<h2 class="sec">The Almanac Sky</h2>
<div class="wxrow">
  <div class="wxc"><div class="k">Moon</div><svg class="moonmini" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#5a4d3b"/><path d="M50 4 A46 46 0 0 1 50 96 A41.1 46 0 0 1 50 4Z" fill="#f4e5b4"/></svg><div class="s">waxing gibbous</div></div>
  <div class="wxc"><div class="k">Sunrise</div><div class="v">7:16</div><div class="s">a.m.</div></div>
  <div class="wxc"><div class="k">Daylight</div><div class="v">9h 30m</div><div class="s">2 min less</div></div>
</div>
<p class="skynote"><b>Tonight:</b> the moon, 95 percent lit and in Aries, comes up at 3:06 this afternoon and stays up until 4:54 a.m. Saturn is the only bright planet of the evening, highest in the south around 9. Mars and Jupiter rise after 11. The full moon, the Beaver Moon, is Tuesday.</p>
<div class="touch-head">The Stars &middot; for fun</div>
<div class="stars slim">
<div class="star"><span class="sgn">Aries</span> <span class="who">Kaylani, Luka</span><br>The moon has moved on to Taurus and left you alone. Nap accordingly.</div>
<div class="star"><span class="sgn">Cancer</span> <span class="who">Gregg</span><br>A friendly moon. Pick a favorite dish; the stars back you.</div>
<div class="star"><span class="sgn">Leo</span> <span class="who">Leah, Tommy</span><br>The moon is at a cross angle. Don't start the argument at kickoff.</div>
<div class="star"><span class="sgn">Virgo</span> <span class="who">Derek, Joanne</span><br>An easy, earthy moon. Good day to plan the menu.</div>
<div class="star"><span class="sgn">Scorpio</span> <span class="who">Ariel, Claire, Garret</span><br>The moon sits across from you. Let somebody else carve.</div>
</div>
''')
S('<h2 class="sec">Coming Up</h2>', '<div class="dbl"><div class="a">', '''<h2 class="sec">Coming Up</h2>
<div class="calbox"><div class="calrow"><div class="cd">Today</div><div>Dolphins at Bills, 1:00; Jets at Chargers, 4:05</div></div>
<div class="calrow"><div class="cd">Tue</div><div>Full moon</div></div>
<div class="calrow"><div class="cd">Thu</div><div>Thanksgiving; Turkey Trot downtown, 9:00; Chiefs at Bills, 8:20</div></div>
<div class="calrow"><div class="cd">Fri</div><div>UB at Akron, noon</div></div>
<div class="calnote">Migraine log: nothing new since Joanne's on Monday. Four this month.</div>
</div>
<h2 class="sec">The Week Ahead</h2>
<div class="line"><b>Weather.</b> Last week: mild all week, with highs climbing from 49 Monday to 64 Saturday; coldest dawn 36 Saturday. This week turns: 48 Monday, then highs around 40 Tuesday and Wednesday, a hard freeze Tuesday night, and a chance of rain and snow showers Thanksgiving Day.</div>
<div class="line"><b>Games.</b> Bills and Jets today; Chiefs at Bills on Thanksgiving night; UB at Akron Friday.</div>
<div class="line"><b>Thanksgiving.</b> Thursday. Garret runs the Turkey Trot downtown at 9.</div>
<div class="line"><b>Next Sunday's Spotlight.</b> The month in migraine.</div>
<h2 class="sec">The Sunday Question</h2>
<div class="qotd"><b>Last week we asked what one dish has to be on the Thanksgiving table.</b><br><b>Gregg:</b> "How in the heck can anyone pick just one 'most favorite' dish at Thanksgiving?? I'm finding it quite impossible &#129335;"</div>
<div class="qotd"><b>This week: what's the one Thanksgiving job you always end up with?</b><br>Send it at <a href="https://tally.so/r/rjxDpl">tally.so/r/rjxDpl</a>. Answers run here next Sunday under your names.</div>
<h2 class="sec">On This Day</h2>
<div class="otd"><b>November 22, 1963</b> &mdash; President John F. Kennedy was shot riding in an open car through downtown Dallas, a little after 12:30 in the afternoon. Within the hour Walter Cronkite read the bulletin on CBS that the president had died at 1 p.m. Central time. Vice President Lyndon Johnson took the oath of office aboard Air Force One before it left Dallas. For a generation, "where were you" meant this day.</div>
<h2 class="sec">Question of the Day</h2>
<div class="qotd">The longer I stand up for you, the shorter I get, and I weep the whole time. What am I? <i>Answer below the fold.</i></div>
''')
R('<b>Question of the Day:</b> A piggy bank.', '<b>Question of the Day:</b> A candle.')
S('headlines via ', ' &middot; scores and stats via Sportradar', 'headlines via NPR, the BBC, PBS NewsHour, the <i>Lockport Union-Sun &amp; Journal</i>, Page Six, the Hollywood Reporter, Us Weekly, ProFootballTalk, Gang Green Nation; Spotlight figures from the American Farm Bureau Federation; market data via Yahoo Finance; snow and records via ACIS')
ed = {'date': '2026-11-22', 'no': 151, 'body_html': src, 'plate_path': COVER['path'], 'plate_caption': COVER['caption'],
      'headline': "Storms line up for Thanksgiving week · What dinner costs this year · Miley Cyrus is married"}
for p in ['/home/claude/site/data/edition-2026-11-22.json', '/home/claude/edition-2026-11-22.json']:
    json.dump(ed, open(p, 'w'), ensure_ascii=False, indent=1)
print('ok', len(src))
