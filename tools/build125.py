import json, subprocess
src = open('/home/claude/b124.html').read()

def R(a, c):
    global src
    assert src.count(a) == 1, ('R', a[:60], src.count(a))
    src = src.replace(a, c)

def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50])
    src = src[:i] + new + src[j:]

R('No. 124', 'No. 125')
R('Monday &middot; October 26 &middot; 2026', 'Tuesday &middot; October 27 &middot; 2026')
S('<div class="tiles">', '<div class="plate-wrap">', '''<div class="tiles">
  <div class="tile"><div class="v">54&deg;</div><div class="k">Mostly Sunny</div></div>
  <div class="tile"><div class="v">6:14</div><div class="k">Sunset &middot; 1&frac12; min earlier</div></div>
  <div class="tile urg"><div class="v">7</div><div class="k">Days to Election Day</div></div>
</div>
''')
S('<div class="plate-wrap">', '<div class="dbl-tight">', '')

S('<div class="fam">', '<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass',
'''<div class="fam"><b>Welcome home</b> to everyone back from Long Island. Four days to Halloween, and the porch pumpkins have one more week of work.
<div class="line" style="margin-top:.4rem"><span class="lbl t">The log</span> Days since the last migraine: Garret 4, Dad 21, Mom 18. October so far: Garret two, Dad one, Mom one.</div>
<ul class="cal">
<li><span class="dt">Oct 31</span><span>Halloween</span></li>
<li><span class="dt">Nov 1</span><span>Raiders at Jets, 1:00 &middot; Ravens at Bills, 1:00</span></li>
<li><span class="dt">Nov 1</span><span>Clocks fall back &middot; early voting ends</span></li>
<li><span class="dt">Nov 3</span><span>Election Day</span></li>
</ul>
<div class="ask"><b>Send something to the paper:</b> a photo, a story, your Sunday answer or a date for the calendar, at <a href="https://tally.so/r/rjxDpl">tally.so/r/rjxDpl</a>. It runs the next morning under your name.<br><b>Had a migraine?</b> Log it at <a href="https://tally.so/r/obWNYP">tally.so/r/obWNYP</a>.</div></div>
''')

S('<div class="wx">', '<h2 class="sec"><span class="o">&#127810;</span>The Turning',
'''<div class="wx"><div class="bigtemp">54<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">Sweater weather: a crisp, mostly sunny 54, the coolest day of the week</span>
Low <b>39&deg;</b> tonight &middot; light east wind<br>Warming to 69 Thursday; showers Thursday night, 48%</div></div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">39<sup>&deg;</sup></div><div class="d">Clear &middot; high 54&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">39<sup>&deg;</sup></div><div class="d">Clear &middot; high 55&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">43<sup>&deg;</sup></div><div class="d">Clear &middot; high 52&deg;</div></div>
</div>
<div class="strip5">
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">54</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#9729;</div><div class="h">65</div><div class="w">partly sunny</div></div>
  <div><div class="d">Thu</div><div class="i">&#9728;</div><div class="h">69</div><div class="w">sunny</div></div>
  <div><div class="d">Fri</div><div class="i">&#9728;</div><div class="h">62</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Sat</div><div class="i">&#9729;</div><div class="h">64</div><div class="w">partly sunny</div></div>
</div>
<div class="line"><span class="lbl r">Halloween</span> Saturday looks partly sunny and 64; trick-or-treat night turns mostly cloudy, with a 10 percent chance of rain and a low of 46.</div>
<div class="line"><span class="lbl r">Frost</span> Scottsville dips to 33 tonight; North Tonawanda 39. <span class="lbl t">Outdoor window</span> Wednesday and Thursday.</div>
''')

S('<div class="line">This is North', '<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky',
'''<div class="line"><b>Report day tomorrow.</b> The state's new foliage numbers land Wednesday afternoon, in North Tonawanda's usual peak week.</div>
''')

S('<div class="sky">', '<h2 class="sec"><span class="o">&#10038;</span>The Ledger',
'''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 0 50 96 A43 46 0 0 0 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>A waning gibbous</b>, 97 percent lit, in Aries; sets at 9:43 a.m., rises at 6:50 p.m.<br>
<span class="lbl t">Sun</span> 7:44a &ndash; 6:14p &middot; <b>10h 31m</b><br>
<span class="lbl t">Clocks fall back</span> Sun, Nov 1 &middot; <span class="lbl t">New moon</span> Mon, Nov 9</div></div>
<div class="line"><span class="lbl r">Tonight</span> The moon comes up in the east-northeast at 6:50, more than half an hour after sunset and later each night now. Saturn is already well up in the southeast by then.</div>
<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>The moon squares Jupiter</b>. You'll want seconds of everything. Have them, then take a walk. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>Uranus trines Pluto</b>. Rearrange one room. The house will thank you. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Mercury squares Mars in your sign</b>. Sharp words come quick today. Count to ten, then say half. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>Neptune sextiles Pluto</b>. A quiet hunch is worth following. Make the call. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Mercury, in your sign, squares Jupiter</b>. Big plans after a big trip. Sleep on them first. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
<div style="font-family:'LOI';font-style:italic;font-size:.8rem;color:var(--soft);margin-top:.4rem">Positions computed for noon today at 14120. The sky is real; the readings are for fun.</div>
''')

S('<div class="ledger">', '<h2 class="sec"><span class="o">&#10038;</span>The National Wire',
'''<div class="ledger"><div class="num"><div class="cap">Pounds of food scraps Buffalo's compost pickup has kept out of landfills since 2023</div><div class="big">1.7 million</div></div>
<div class="txt">From 2,000 households. The city now hopes to reach about 10,000 within five years, with 1,000 already on the waitlist, WKBW reports.</div></div>
''')

ballot = subprocess.run(['python3', '/home/claude/site/tools/ballot_box.py', '2026-10-27'], capture_output=True, text=True, cwd='/home/claude/site').stdout.strip()
assert ballot.startswith('<div class="ballot">')
S('<div class="wire"><div class="num">1</div><div><h3>Update: Lula', '<h2 class="sec"><span class="o">&#9962;</span>The Home Wire',
'''<div class="wire"><div class="num">1</div><div><h3>Israel Votes</h3><p>Israelis are voting today in their first national election since the Oct. 7, 2023, attack, and turnout is the highest since 1981, the BBC reports. Polls show Prime Minister Benjamin Netanyahu nearly even with former military chief Gadi Eisenkot, but neither side is projected to reach the 61 seats needed to govern, so weeks of coalition bargaining may follow.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Update: The Oleshky Truce Begins</h3><p>The ceasefire in Oleshky, the Russian-occupied Ukrainian city cut off from food, water and electricity, has started, and both Ukrainian officials and Russia's defense ministry say it is holding, the BBC reports. Aid deliveries and evacuations are set for Friday; residents told the BBC they have been cooking garden weeds to survive.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Dollar General Sued Over Prices</h3><p>The Federal Trade Commission and 20 states sued Dollar General Monday, accusing the chain of charging more at the register than its shelf prices said, for years, CBS reports. The FTC says the mislabeling took "millions of dollars in unlawful overcharges" from shoppers at its 21,000 stores.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>Comey Charged a Third Time</h3><p>Federal prosecutors moved to charge former FBI Director James Comey with leaking national defense information, the third time the Justice Department has tried to prosecute him, the BBC reports. His lawyers say the case involves an alleged 2016 disclosure to the <i>New York Times</i>; Comey calls it an "appalling abuse."</p></div></div>
''' + ballot + '\n')

S('<div class="wire"><div class="num">1</div><div><h3>Rochester', '<h2 class="sec"><span class="o">&#9733;</span>The Marquee',
'''<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; The School for the Deaf Turns 150</h3><p>The Rochester School for the Deaf on St. Paul Street is marking 150 years since it opened, and alumni came back this month to meet today's students, WXXI reports. "RSD is really my second home," said Patti Canne, class of 1981, now a social worker at the University of Rochester, speaking in American Sign Language through an interpreter.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Niagara Falls &middot; Water Rates Could Rise 3%</h3><p>The Niagara Falls Water Board is weighing a 3 percent rate increase for 2027, the <i>Niagara Gazette</i> reports. The proposed budget is just over $39.8 million, up from $39.28 million; the board's director says costs are under control but revenue is falling.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Dunkirk &middot; Perch and Walleye Are Biting</h3><p>Yellow perch fishing on Lake Erie is "kicking into high gear" in 50 to 55 feet of water between Cattaraugus Creek and Sturgeon Point, the <i>Observer</i>'s outdoors column says. Walleye are schooled up at 80 to 110 feet from Dunkirk west to Barcelona, and one three-man boat limited out off Dunkirk in two hours.</p></div></div>
''')

S('<div class="wire"><div class="num">1</div><div><h3>The Voice', '<h2 class="sec"><span class="o">&#127944;</span>The Gridiron',
'''<div class="wire"><div class="num">1</div><div><h3>Jay-Z Gets the Super Bowl</h3><p>Jay-Z will headline the Super Bowl halftime show at SoFi Stadium in Los Angeles on Valentine's Day, announced during Monday Night Football, the <i>Hollywood Reporter</i> reports. He follows Bad Bunny, whose show at this year's Super Bowl won an Emmy.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Taylor Swift Joins the Songwriters</h3><p>Taylor Swift was inducted into the Nashville Songwriters Hall of Fame Monday night, with Brad Paisley doing the honors, Billboard reports. The 14-time Grammy winner told the room the writers of Music Row "raised me."</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Noah Wyle, Sexiest Man Alive</h3><p><i>People</i> named Noah Wyle its Sexiest Man Alive for 2026, his first time, Variety reports. He has been a TV doctor since 1994, when he started as John Carter on <i>ER</i>.</p></div></div>
''')

S('<div class="touch-head">Monday Morning Quarterback</div>', '<h2 class="sec"><span class="o">&#9873;</span>The Chase',
'''<div class="touch-head">Ravens Week</div>
<div class="line"><b>Bills</b> &middot; Buffalo throws a Bills rally in Niagara Square Thursday, 5:30 to 7:30 p.m., with food trucks, Billy Buffalo and a light show on the Statler, WKBW reports; the rain date is Friday. The Bills (5&ndash;1) host Baltimore (4&ndash;3) Sunday at 1:00.</div>
<div class="line"><b>Jets</b> &middot; Back at MetLife Sunday at 1:00 against the Raiders, who are 3&ndash;4. The Jets (2&ndash;5) lost to Miami by three this week, with Geno Smith's three touchdown passes nearly enough.</div>
<div class="pnote"><b>The Sunday Tax &middot; Week 8.</b> Picks at <a href="https://tally.so/r/RGOakJ">tally.so/r/RGOakJ</a>; standings at <a href="https://benthambulletin.github.io/pool/">benthambulletin.github.io/pool</a>. Week 7 went to Ryan, $95, his second straight. $5 a week, straight-up winners, the pot to the best record. Anyone with the link can play. Sheets lock at each kickoff; first game Thu 8:15 p.m., Panthers at Green Bay.</div>
<table class="tbl"><tr><th>AFC East</th><th class="n">W</th><th class="n">L</th><th class="n">PCT</th></tr>
<tr><td style="color:var(--red)">Buffalo</td><td class="n">5</td><td class="n">1</td><td class="n">.833</td></tr>
<tr><td>New England</td><td class="n">4</td><td class="n">3</td><td class="n">.571</td></tr>
<tr><td style="color:var(--red)">N.Y. Jets</td><td class="n">2</td><td class="n">5</td><td class="n">.286</td></tr>
<tr><td>Miami</td><td class="n">1</td><td class="n">5</td><td class="n">.167</td></tr></table>
<div class="line"><b>Monday night.</b> Dallas won 38&ndash;21 at Philadelphia; Dak Prescott threw three touchdown passes, two to CeeDee Lamb.</div>
''')

S('<div class="touch-head">Larson Wins Talladega</div>', '<h2 class="sec"><span class="o">&#9790;</span>On This Day',
'''<div class="touch-head">Martinsville Sunday</div>
<div class="line">Larson 2,441, Hamlin 73 back, Bell 74; two races left.</div>
''')

S('<div class="otd">', '<h2 class="sec"><span class="o">&#10023;</span>Question of the Day',
'''<div class="otd"><b>October 27, 1904</b> &mdash; New York City's first subway opened, running from City Hall to 145th Street for a nickel a ride.</div>
''')

R('''I'm built overnight without a hammer, I'm strung across the porch light, and my builder eats whatever drops in. What am I?''',
  '''I'm tall and pointed and black as the night, and I ride on a head while its owner takes flight. What am I?''')
R('<b>Question of the Day:</b> A spider web.', "<b>Question of the Day:</b> A witch's hat.")
S('<div class="s">Forecast per', '<div class="sig">',
'''<div class="s">Forecast per NWS Buffalo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; sky computed for 14120 &middot; election summary from the paper's election tracker &middot; Sunday Tax from the pool's standings &middot; headlines via BBC, CBS, WKBW, WXXI, Niagara Gazette, Dunkirk Observer, Hollywood Reporter, Billboard, Variety &middot; scores and NASCAR points via Sportradar and Hendrick Motorsports</div>
''')

ed = {"date": "2026-10-27", "no": 125, "body_html": src, "plate_path": None,
      "plate_caption": "Four days to Halloween",
      "headline": "Israel votes · Oleshky truce begins · Dollar General sued · Ravens week"}
for p in ['/home/claude/edition-2026-10-27.json', '/home/claude/site/data/edition-2026-10-27.json']:
    json.dump(ed, open(p, 'w'), ensure_ascii=False, indent=1)
print('ok')

# --- review fixes ---
