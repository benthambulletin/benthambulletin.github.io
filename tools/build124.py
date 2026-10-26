import json, subprocess
src = open('/home/claude/b122.html').read()

def R(a, c):
    global src
    assert src.count(a) == 1, ('R', a[:60], src.count(a))
    src = src.replace(a, c)

def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50])
    src = src[:i] + new + src[j:]

R('No. 122', 'No. 124')
R('Saturday &middot; October 24 &middot; 2026', 'Monday &middot; October 26 &middot; 2026')
S('<div class="tiles">', '<div class="plate-wrap">', '''<div class="tiles">
  <div class="tile"><div class="v">64&deg;</div><div class="k">Partly Sunny</div></div>
  <div class="tile"><div class="v">6:15</div><div class="k">Sunset &middot; 1&frac12; min earlier</div></div>
  <div class="tile urg"><div class="v">8</div><div class="k">Days to Election Day</div></div>
</div>
''')
R('alt="A grinning little boy and a smiling man in glasses in a hot tub against a weathered wood wall"',
  'alt="A calm harbor with dock pilings, a flagpole and a far shoreline under an orange and blue sky"')
R('<div class="plate-sub">Hot tub buddies</div>', '<div class="plate-sub">Still water and an orange sky, the last morning on Long Island</div>')

S('<div class="fam">', '<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass',
'''<div class="fam"><b>Home day.</b> The family heads back from Long Island today, and that's the harbor on the cover, sent at 6 this morning. Safe travels, everyone. Halloween is Saturday, five days out.
<div class="line" style="margin-top:.4rem"><span class="lbl t">The log</span> Days since the last migraine: Garret 3, Dad 20, Mom 17. October so far: Garret two, Dad one, Mom one.</div>
<ul class="cal">
<li><span class="dt">Today</span><span>The family home from Long Island</span></li>
<li><span class="dt">Oct 31</span><span>Halloween</span></li>
<li><span class="dt">Nov 1</span><span>Raiders at Jets, 1:00 &middot; Ravens at Bills, 1:00</span></li>
<li><span class="dt">Nov 1</span><span>Clocks fall back &middot; early voting ends</span></li>
<li><span class="dt">Nov 3</span><span>Election Day</span></li>
</ul>
<div class="ask"><b>Send something to the paper:</b> a photo, a story, your Sunday answer or a date for the calendar, at <a href="https://tally.so/r/rjxDpl">tally.so/r/rjxDpl</a>. It runs the next morning under your name.<br><b>Had a migraine?</b> Log it at <a href="https://tally.so/r/obWNYP">tally.so/r/obWNYP</a>.</div></div>
''')

S('<div class="wx">', '<h2 class="sec"><span class="o">&#127810;</span>The Turning',
'''<div class="wx"><div class="bigtemp">64<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">Five days to Halloween: a partly sunny afternoon, then porch-light dusk at 6:15 and a cold night</span>
Low <b>37&deg;</b> tonight &middot; light north wind<br>Cooler Tuesday at 56; a chance of showers Thursday night</div></div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">48<sup>&deg;</sup></div><div class="d">Mostly clear &middot; high 64&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">52<sup>&deg;</sup></div><div class="d">Clear &middot; high 62&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">43<sup>&deg;</sup></div><div class="d">Fog early &middot; high 66&deg;</div></div>
</div>
<div class="strip5">
  <div><div class="d">Mon</div><div class="i">&#9729;</div><div class="h">64</div><div class="w">partly sunny</div></div>
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">56</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#9729;</div><div class="h">66</div><div class="w">partly sunny</div></div>
  <div><div class="d">Thu</div><div class="i">&#9728;</div><div class="h">68</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Fri</div><div class="i">&#127782;</div><div class="h">66</div><div class="w">showers early, 29%</div></div>
</div>
<div class="line"><span class="lbl r">Frost</span> Scottsville dips to 31 Tuesday night; North Tonawanda holds at 37. <span class="lbl t">Outdoor window</span> Today, Wednesday and Thursday.</div>
<div class="line"><span class="lbl t">Away</span> Long Island, last day: sunny and 65 for the drive home.</div>
''')

S('<div class="line"><b>This week', '<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky',
'''<div class="line">No new numbers until the state's foliage report Wednesday afternoon.</div>
''')

S('<div class="sky">', '<h2 class="sec"><span class="o">&#10038;</span>The Ledger',
'''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>Just past full</b>, 99 percent lit, in Aries; the Hunter's Moon peaked at 12:11 this morning. Sets at 8:22 a.m., rises at 6:11 p.m.<br>
<span class="lbl t">Sun</span> 7:42a &ndash; 6:15p &middot; <b>10h 34m</b><br>
<span class="lbl t">New moon</span> Mon, Nov 9 &middot; <span class="lbl t">Beaver Moon</span> Tue, Nov 24</div></div>
<div class="line"><span class="lbl r">Tonight</span> The moon still looks full when it comes up in the east at 6:11, a few minutes before sunset. Saturn rises at 5:25 and is a third of the way up the southeastern sky by 8:30.</div>
<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>Neptune, in your sign, sextiles Pluto</b>. A daydream turns into a plan. Write down the first step. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>Uranus sextiles Neptune</b>. Try the new thing at dinner. Worst case, it's a story. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Mercury squares Jupiter in your sign</b>. Big talk, small print. Read it twice. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>Venus squares Pluto</b>. A tug-of-war over the thermostat. Grab a sweater and call it a draw. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>The sun in your sign squares Pluto</b>. The suitcases can wait until tomorrow. Unpack the good part first. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
<div style="font-family:'LOI';font-style:italic;font-size:.8rem;color:var(--soft);margin-top:.4rem">Positions computed for noon today at 14120. The sky is real; the readings are for fun.</div>
''')

S('<div class="ledger">', '<h2 class="sec"><span class="o">&#10038;</span>The National Wire',
'''<div class="ledger"><div class="num"><div class="cap">Measles cases in Pennsylvania this year</div><div class="big">1,338</div></div>
<div class="txt">The worst-hit state, across 44 counties, by the state health department's count; U.S. cases are running more than double last year's, NPR reports.</div></div>
''')

ballot = subprocess.run(['python3', '/home/claude/site/tools/ballot_box.py', '2026-10-26'], capture_output=True, text=True, cwd='/home/claude/site').stdout.strip()
assert ballot.startswith('<div class="ballot">')
S('<div class="wire"><div class="num">1</div><div><h3>A Truce', '<h2 class="sec"><span class="o">&#9962;</span>The Home Wire',
'''<div class="wire"><div class="num">1</div><div><h3>Update: Lula Wins a Fourth Term</h3><p>With every vote counted, Brazil's electoral court says President Luiz In&aacute;cio Lula da Silva beat Fl&aacute;vio Bolsonaro with 51.8 percent, a lead of nearly 4.4 million votes, CBS reports. Bolsonaro refused to concede and asked for the results to be thrown out after a judge's last-minute decision to keep polls open two extra hours.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Serbia's Strongman Concedes</h3><p>Serbia's longtime leader Aleksandar Vu&#269;i&#263; admitted defeat Sunday to a student-led protest movement in snap parliamentary elections, and crowds celebrated in Belgrade and other cities, the BBC reports. The movement formed less than two years ago after a railway station disaster blamed on corruption; an independent projection gives it 52.9 percent of the vote.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Machado Comes Home</h3><p>Venezuelan opposition leader Mar&iacute;a Corina Machado returned home Sunday after more than 10 months in exile, and huge crowds lined her route through Caracas, the BBC reports. She slipped out of the country last December to accept the Nobel Peace Prize; the U.S. seized President Nicol&aacute;s Maduro in January and backed his deputy, Delcy Rodr&iacute;guez, as interim president.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>A 93-Year-Old Turns the Tables</h3><p>A 93-year-old woman in western Japan got calls from a man posing as a police officer, who said her bank account had been raided and that an officer would come collect her ATM card, CBS reports. She suspected a scam, told her son and the real police, and officers were waiting at her house when the man showed up.</p></div></div>
''' + ballot + '\n')

S('<div class="wire"><div class="num">1</div><div><h3>Rochester', '<h2 class="sec"><span class="o">&#9733;</span>The Marquee',
'''<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; A $16 Million Facelift for the Hyatt</h3><p>A $16 million renovation to make the downtown Hyatt Regency a top-flight, full-service hotel will start "as soon as possible," WXXI reports. The Riverside closed in 2020 and the Wyndham this summer, and the deputy mayor says the city is about 1,000 hotel rooms short.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Silver Creek &middot; A Home Playoff Game</h3><p>Silver Creek/Forestville piled up 437 yards in a 31&ndash;13 win over Franklinville/Ellicottville to lock up the third seed in the Section VI Class D playoffs, the <i>Observer</i> reports. Manny Sanchez ran for 204 yards, and the Black Knights host sixth-seeded Cattaraugus-Little Valley in next weekend's quarterfinals.</p></div></div>
''')

S('<div class="wire"><div class="num">1</div><div><h3>A First Look', '<h2 class="sec"><span class="o">&#127944;</span>The Gridiron',
'''<div class="wire"><div class="num">1</div><div><h3>The Voice of Bugs Bunny Dies at 46</h3><p>Eric Bauza, the Emmy-winning actor who voiced Bugs Bunny and Daffy Duck, died Sunday at 46, his manager said, CBS reports. The Los Angeles County medical examiner lists hypertensive cardiovascular disease, heart damage from long-term high blood pressure; he had more than 400 credits, including Porky Pig and Marvin the Martian.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Olivia Rodrigo Back on Top</h3><p>Olivia Rodrigo's <i>you seem pretty sad for a girl so in love</i> is back atop the Billboard 200, its third week on top, Billboard reports. A new remix of "Expectations" with Chappell Roan did it; Zach Bryan's new album debuts in second place.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Miranda Lambert's Thanksgiving Halftime</h3><p>Miranda Lambert will headline halftime when the Cowboys host the Eagles on Thanksgiving, Billboard reports. The show kicks off the Salvation Army's Red Kettle campaign each year, and Lambert says this is its 30th anniversary.</p></div></div>
''')

S('<div class="touch-head">Jets Tomorrow', '<h2 class="sec"><span class="o">&#9873;</span>The Chase',
'''<div class="touch-head">Monday Morning Quarterback</div>
<div class="line"><b>Dolphins 28, Jets 25.</b> Miami led 21&ndash;7 at halftime behind Malik Willis, who threw two touchdown passes to C. Douglas, the second a 63-yarder with 4:55 left, and ran for another. The Jets came back hard: Geno Smith found Mason Taylor for 12 yards and Taylor caught the two-point try to make it 28&ndash;25 with 3:24 to go, but they got no closer.</div>
<div class="line"><b>Got right:</b> Smith went 23 of 30 for 287 yards and three touchdowns, two of them to Taylor, and the offense outgained Miami 377 to 360. <b>To fix:</b> the first half, a missed field goal, and 156 Miami rushing yards. The Jets are 2&ndash;5; the Raiders visit Sunday at 1:00.</div>
<div class="line"><b>Bills</b> &middot; Off Sunday and still 5&ndash;1, a game and a half clear of New England. Baltimore visits Sunday at 1:00, coming off a 35&ndash;13 home loss to Cincinnati.</div>
<table class="tbl"><tr><th>AFC East</th><th class="n">W</th><th class="n">L</th><th class="n">PCT</th></tr>
<tr><td style="color:var(--red)">Buffalo</td><td class="n">5</td><td class="n">1</td><td class="n">.833</td></tr>
<tr><td>New England</td><td class="n">4</td><td class="n">3</td><td class="n">.571</td></tr>
<tr><td style="color:var(--red)">N.Y. Jets</td><td class="n">2</td><td class="n">5</td><td class="n">.286</td></tr>
<tr><td>Miami</td><td class="n">1</td><td class="n">5</td><td class="n">.167</td></tr></table>
<div class="line"><b>Around the league.</b> Seattle beat Kansas City 20&ndash;3, the Chiefs' first loss, and Minnesota beat Indianapolis to stay perfect at 6&ndash;0. Pittsburgh won the NFL's first regular-season game in France, 16&ndash;10 over New Orleans. Dallas plays at Philadelphia tonight.</div>
<div class="line"><b>The AI Editor, graded.</b> Bills 11&ndash;6: 5&ndash;1, ahead of pace. Jets 6&ndash;11: 2&ndash;5, a half game behind it. Ravens over Rams in the Super Bowl: split Sunday, Baltimore routed by Cincinnati to fall to 4&ndash;3 and the Rams winning 35&ndash;21 at Las Vegas to get to 3&ndash;4.</div>
''')

S('<div class="touch-head">Talladega Tomorrow</div>', '<h2 class="sec"><span class="o">&#9790;</span>On This Day',
'''<div class="touch-head">Larson Wins Talladega</div>
<div class="line">Kyle Larson fell to 11th on the last lap of overtime, then charged back through the tri-oval to win, his first victory at a drafting track in 59 tries, Hendrick Motorsports reports. William Byron was second and Ricky Stenhouse Jr. third. Larson now leads Denny Hamlin by 73 points, Christopher Bell by 74 and Chase Briscoe by 79. Two races left: Martinsville Sunday, then Homestead.</div>
''')

S('<div class="otd">', '<h2 class="sec"><span class="o">&#10023;</span>Question of the Day',
'''<div class="otd"><b>October 26, 1825</b> &mdash; The Erie Canal opened, 363 miles from Buffalo to Albany. Gov. DeWitt Clinton set out from Buffalo on the <i>Seneca Chief</i>, bound for New York City; the canal still runs through the Tonawandas.</div>
''')

R('''I'm striped yellow, orange and white, and I show up by the bagful every October. What am I?''',
  '''I'm built overnight without a hammer, I'm strung across the porch light, and my builder eats whatever drops in. What am I?''')
R('<b>Question of the Day:</b> Candy corn.', '<b>Question of the Day:</b> A spider web.')
S('<div class="s">Forecast per', '<div class="sig">',
'''<div class="s">Forecast per NWS Buffalo, with the NWS forecast for Long Island &middot; Niagara Falls, Dunkirk and Rochester stations &middot; sky computed for 14120 &middot; election summary from the paper's election tracker &middot; headlines via CBS, BBC, NPR, WXXI, Dunkirk Observer, Billboard &middot; scores via Sportradar &middot; NASCAR via Hendrick Motorsports</div>
''')

ed = {"date": "2026-10-26", "no": 124, "body_html": src, "plate_path": "/home/claude/plate124.jpg",
      "plate_caption": "Still water and an orange sky, the last morning on Long Island",
      "headline": "Lula wins again · Larson takes Talladega · Jets fall to Miami · Home from Long Island"}
for p in ['/home/claude/edition-2026-10-26.json', '/home/claude/site/data/edition-2026-10-26.json']:
    json.dump(ed, open(p, 'w'), ensure_ascii=False, indent=1)
print('ok')

# --- review fixes ---
