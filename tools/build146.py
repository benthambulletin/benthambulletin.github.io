import json, sys
sys.path.insert(0, '/home/claude'); from curve import curve
src = json.load(open('/home/claude/site/data/edition-2026-11-16.json'))['body_html']
def R(a, c, n=1):
    global src
    assert src.count(a) == n, ('R', a[:60], src.count(a)); src = src.replace(a, c)
def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50]); src = src[:i] + new + src[j:]
f = json.load(open('/home/claude/site/data/forecast.json'))
assert f['generated_utc'].startswith('2026-11-17')
assert [f['towns'][n]['observation']['temp_f'] for n in ['North Tonawanda', 'Dunkirk', 'Scottsville']] == [37, 43, 36]
assert f['lakes']['readings'] == {'Lake Erie (Buffalo)': 54, 'Lake Ontario (Rochester)': 55} and 'Mon Nov 16 2026 The water temperature off Buffalo' in f['lakes']['text']
hourly = f['towns']['North Tonawanda']['hourly']; assert 'T05:00' in hourly[0]['start']
chart = curve(hourly, 7 * 60 + 10, 16 * 60 + 50)
i = src.find('<img src="__PLATE__"'); j = src.find('>', i) + 1; assert i > 0
src = src[:i] + '<img src="__PLATE__" alt="A small boy steering a ride-on toy car down a warehouse store aisle">' + src[j:]
R('<div class="plate-sub">Voyager, in a NASA rendering. Image: NASA/JPL-Caltech</div>', '<div class="plate-sub">A test drive at the store</div>')
R('<div class="plate-cap">The Cover</div>', '<div class="plate-cap">Plate I &middot; The Family Album</div>')
R('No. 145', 'No. 146'); R('Monday &middot; November 16 &middot; 2026', 'Tuesday &middot; November 17 &middot; 2026')
S('<div class="tiles">', '<div class="plate-wrap">', '''<div class="tiles">
  <div class="tile"><div class="v">54&deg;</div><div class="k">Mostly Sunny</div></div>
  <div class="tile"><div class="v">4:50</div><div class="k">Sunset</div></div>
  <div class="tile urg"><div class="v">9</div><div class="k">Days to Thanksgiving</div></div>
</div>
''')
S('<div class="wire lead">', '<div class="part"><span>The Almanac</span></div>', '''<div class="wire lead"><div><span class="kick">The Lead</span><h3>What the Data Centers Put in the Air</h3>
<p>The 403 biggest data centers in the United States, the warehouse-size buildings full of computers that run the internet and A.I., give off an estimated 25.7 million metric tons of carbon dioxide a year, almost as much as Bolivia or Denmark. That is the finding of a study published Monday in the journal <i>Nature Sustainability</i> by a team led by Harvard researchers, The New York Times reports. It is the first peer-reviewed estimate since the A.I. boom began.</p>
<p>The centers used almost 2 percent of the country's electricity, more than New York City and Los Angeles combined, and produced about half a percent of its carbon dioxide. Fifty-four percent of their power came from burning fossil fuels, mostly natural gas and coal. Virginia, Iowa and Ohio account for about half the total, and Virginia alone for more than a quarter.</p>
<p>No public list of data centers exists, so the researchers pieced one together from a commercial dataset, building outlines and satellite images. The lead author, Gianluca Guidi, wants the federal government to require large data centers to report their electricity use and emissions. The figure is probably low: it leaves out hundreds of sites the team could not verify, and at least 250 more have opened since the study period ended.</p>
<p>There is pushback. Andy Masley, an independent researcher, told the Times that whether the emissions are an acceptable cost depends on how useful A.I. proves, and that part of the reason for them is how many people use it. Voters, for their part, limited or blocked data-center development in 40 of 41 local ballot measures this month.</p>
<p><b>The AI Editor's read</b> (an AI wrote this paragraph, and it runs in data centers like these, so weigh it accordingly): The counter-argument is half right. A growing share of emissions is not a verdict by itself, half a percent of the country's emissions for something a great many people use is not obviously out of line, and "is it worth it" is the right question for any industry. But it answers a different question. The study's main complaint is secrecy, and nobody can weigh a cost against a benefit when the cost had to be pieced together from satellite photos. Heavy use does not explain the fuel mix, either: the fossil share comes from where the centers were built and what powers them, and the study found Oregon's emit less carbon per unit of electricity because more of their power is fossil-free. And the costs and benefits land on different people. Users everywhere get the benefit; the towns near the plants and the people sharing that grid carry the cost, which is the backdrop to those ballot results. Waiting to see whether A.I. proves useful is reasonable as far as it goes. It is a weak reason to hold off on disclosure or cleaner power in the meantime.</p>
</div></div>
<h2 class="sec">The National Wire</h2>
<div class="wire"><div class="num">1</div><div><h3>Bank Apps Go Down, Then Come Back</h3><p>Customers of JPMorgan Chase, Bank of America, U.S. Bank, Capital One, Truist and Wells Fargo reported trouble getting into their accounts Monday, and so did users of the payment app Zelle, according to the outage tracker Downdetector, CBS reports. Service was back to normal early Tuesday; Chase said its problem was a technical bug, not a cyberattack.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Ukraine Knocks Out the Crimea Bridge</h3><p>The bridge linking Russia to occupied Crimea is closed after a Ukrainian strike sent a section of it into the water, the BBC reports; Russian officials confirmed drones had damaged it. Kyiv's mayor said two important bridges over the Dnipro River in the capital were closed after Russian attacks.</p></div></div>
<h2 class="sec">The Home Wire</h2>
<div class="wire"><div class="num">1</div><div><h3>Amherst &middot; A Wayfair Store for the Old Boulevard Mall</h3>
<p>Wayfair, the online furniture seller, plans a store of about 96,000 square feet at 1261 Niagara Falls Boulevard, on the site of the former Boulevard Mall, <a href="https://www.aboutwayfair.com/category/company-news/wayfair-to-open-a-store-in-buffalo-new-york">the company announced</a>. It is expected to open in 2028 and would be Wayfair's 12th. It will go into the space that last held Gabe's and, in the mall's heyday, Sears, <a href="https://www.yahoo.com/news/articles/wayfair-store-occupy-former-gabe-221923977.html">WIVB reports</a>; Supervisor Shawn Lavin said the rest of the mall will come down, and the town, which is in court to take the property by eminent domain, hopes to have it by early December and hand it to Benderson Development for a project that includes housing. Benderson's Eric Recoon called the store the "exciting first step."</p>
<p>What will be inside: Wayfair promises a curated selection, design experts on site, many items to take home the same day and bigger purchases delivered. The best guide is its existing stores, though a guide is not a promise. The first, in Wilmette, Illinois, shows furniture in room settings grouped by style, with a walled-off mattress shop, a home-project area with appliances, cabinets, tile and working showers and faucets, a free design studio, housewares, rugs, lighting, outdoor, kids and pets, and a cafe by the door, according to <a href="https://www.therecordnorthshore.org/2024/05/16/seeing-is-believing-a-tour-of-wayfair-in-wilmette-ahead-of-its-grand-opening/">The Record North Shore</a>. Shelf tags carry codes to scan, and screens open the full online catalog. In Atlanta, roughly whatever fits in the car goes home with you; sofas are not stocked and ship from a warehouse, <a href="https://www.axios.com/local/atlanta/2026/03/31/wayfair-opens-new-store-atlanta">Axios reports</a>.</p>
<p>Amherst's store is about two-thirds the size of those two, so expect a trimmed-down version. Not announced: the number of floors, the opening date, the number of jobs, and whether Amherst gets the cafe.</p>
<p>Against IKEA: both are big home stores with food. Wayfair sells many brands and styles and adds home improvement, shoppers wander between departments instead of following one path, and there is no warehouse hall of flat boxes. IKEA gets here first: it <a href="https://www.ikea.com/us/en/newsroom/corporate-news/ikea-u-s-announces-new-store-opening-in-buffalo-new-york-in-early-2027-pub0defe2e0/">has said</a> it will open a store of about 65,000 square feet at Walden Galleria in early 2027.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Rochester &middot; Cheerleading Is Back, as One Squad</h3><p>Competitive cheerleading returns to Rochester city schools this winter as a single district-wide squad, not separate school teams, WXXI reports. The district had cut the funding this year and faced a public backlash; Superintendent Eric Jay Rosser announced the new format at a school board meeting last week.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Chautauqua County &middot; More Patrols on the Rail Trails</h3><p>The Chautauqua County Sheriff's Office is stepping up patrols on the Chautauqua Rails-to-Trails system after reports of motorized vehicles damaging the paths, Sheriff James Quattrone said, according to WKBW. The system runs nearly 26 miles along old railroad beds from Sherman north to Brocton.</p></div></div>
<h2 class="sec">The Marquee</h2>
<div class="wire"><div class="num">1</div><div><h3>The Name Is Pattinson</h3><p>Robert Pattinson is the next James Bond, the franchise announced Monday, ending the long guessing game over who would follow Daniel Craig, CBS reports. He will be the seventh actor in the role since <i>Dr. No</i> in 1962, and called it "the honour of a lifetime."</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Thirteen Years of Waiting for a Video Game</h3><p>Fans of <i>Grand Theft Auto 6</i>, the first new entry in the series in 13 years, are booking time off work, buying consoles and even pretending to be in New Zealand to get in early, the BBC reports. One research firm, Sensor Tower, estimates 12 million advance orders worth $1.18 billion, a figure the game's maker has not confirmed.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Oprah's List Turns 30</h3><p>Oprah Winfrey has put out her annual Favorite Things list, the holiday gift guide she has made every year since 1996, the Hollywood Reporter says. It began by accident, the magazine recounts, when a producer on her talk show gave her a pair of pajamas she liked enough to tell the audience about.</p></div></div>
<h2 class="sec">The Gridiron</h2>
<div class="wire"><div><h3>Bills: Two-Touchdown Favorites, and Then Some</h3><p>The Bills are favored by 16.5 points over the Dolphins on Sunday, tied with Chiefs-Cardinals for the biggest point spread of the NFL season, ProFootballTalk reports. And one more for the record book from the Jets game: Josh Allen's two rushing touchdowns gave him 90 for his career, tying Hall of Fame running backs Eric Dickerson and Curtis Martin for 14th on the all-time list, per Buffalo Rumblings.</p></div></div>
<div class="wire"><div><h3>Jets: Next Stop, a Team That Just Won</h3><p>The Chargers, who host the Jets on Sunday, won for the first time this season Monday night, holding off the Ravens 23&ndash;20, ProFootballTalk reports. Los Angeles is 1&ndash;8.</p></div></div>
<div class="wire"><div><h3>The Sunday Tax &middot; Week 11</h3><p>Josh won Week 10 with a perfect 14&ndash;0 sheet and took the $95 pot. Week 11 is open: picks at <a href="https://tally.so/r/RGOakJ">tally.so/r/RGOakJ</a>, standings at <a href="https://benthambulletin.github.io/pool/">benthambulletin.github.io/pool</a>. $5 a week, straight-up winners, the pot to the best record, and anyone with the link can play. Sheets lock at each kickoff; first game Thursday at 8:15, Colts at Texans.</p></div></div>
''')
S('<p class="wlede">', '<div class="line"><span class="lbl t">Next 24 hours</span>', '''<p class="wlede">Clear and cold to start, then sun and a southwest breeze</p>
<div class="wxrow">
  <div class="wxc"><div class="k">Tonight</div><div class="v">40&deg;</div><div class="s">partly cloudy</div></div>
  <div class="wxc"><div class="k">Wind</div><div class="v">7&ndash;20</div><div class="s">mph, southwest</div></div>
  <div class="wxc"><div class="k">Rain</div><div class="v">0%</div><div class="s">dry</div></div>
  <div class="wxc"><div class="k">Normal</div><div class="v">47&deg;</div><div class="s">for the date</div></div>
</div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">37<sup>&deg;</sup></div><div class="d">Clear<br>high 54&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">43<sup>&deg;</sup></div><div class="d">Cloudy<br>high 52&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">36<sup>&deg;</sup></div><div class="d">Clear<br>high 56&deg;</div></div>
</div>
<div class="towns lakes">
  <div class="town"><div class="n">Lake Erie</div><div class="t">54<sup>&deg;</sup></div><div class="d">off Buffalo, Monday</div></div>
  <div class="town"><div class="n">Lake Ontario</div><div class="t">55<sup>&deg;</sup></div><div class="d">off Rochester, Monday</div></div>
</div>
<div class="strip5">
  <div><div class="d">Tue</div><div class="i">&#9925;</div><div class="h">54</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#9925;</div><div class="h">55</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Thu</div><div class="i">&#9925;</div><div class="h">58</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Fri</div><div class="i">&#9728;</div><div class="h">58</div><div class="w">sunny</div></div>
  <div><div class="d">Sat</div><div class="i">&#9925;</div><div class="h">63</div><div class="w">mostly sunny</div></div>
</div>
''')
S('<div class="line"><span class="lbl t">Next 24 hours</span>', '<h2 class="sec">The Almanac Sky</h2>', '<div class="line"><span class="lbl t">Next 24 hours</span></div>' + chart + '''<div class="line"><span class="lbl t">Outdoor window</span> Noon to 3, in the low 50s with sun. It gets breezy, with gusts possible to 20 mph.</div>
<div class="line"><span class="lbl t">Frost watch</span> None tonight. Scottsville dips to 35 Wednesday night.</div>
''')
S('<h2 class="sec">The Almanac Sky</h2>', '<h2 class="sec">Coming Up</h2>', '''<h2 class="sec">The Almanac Sky</h2>
<div class="wxrow">
  <div class="wxc"><div class="k">Moon</div><svg class="moonmini" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#5a4d3b"/><path d="M50 4 A46 46 0 0 1 50 96 A2.1 46 0 0 1 50 4Z" fill="#f4e5b4"/></svg><div class="s">half lit</div></div>
  <div class="wxc"><div class="k">Sunrise</div><div class="v">7:10</div><div class="s">a.m.</div></div>
  <div class="wxc"><div class="k">Daylight</div><div class="v">9h 40m</div><div class="s">2 min less</div></div>
</div>
<p class="skynote"><b>Tonight:</b> a half moon, just past first quarter, rides in Capricornus and does not set until 12:13 a.m. Saturn is the bright point highest in the south around 9. Mars and Jupiter come up together about 11:25. The full moon is a week from tonight.</p>
<div class="touch-head">The Stars &middot; for fun</div>
<div class="stars slim">
<div class="star"><span class="sgn">Aries</span> <span class="who">Kaylani, Luka</span><br>The moon is still in your corner. Ask for the favor today, not tomorrow.</div>
<div class="star"><span class="sgn">Cancer</span> <span class="who">Gregg</span><br>Nothing overhead has your name on it. Take the long way home.</div>
<div class="star"><span class="sgn">Leo</span> <span class="who">Leah, Tommy</span><br>The moon is leaning on you a little. Big plans can wait a day; lunch cannot.</div>
<div class="star"><span class="sgn">Virgo</span> <span class="who">Derek, Joanne</span><br>A gentle, easy sky. Rest counts as getting something done.</div>
<div class="star"><span class="sgn">Scorpio</span> <span class="who">Ariel, Claire, Garret</span><br>One more day of mild friction. Let the small stuff go by.</div>
</div>
''')
S('<h2 class="sec">Coming Up</h2>', '<div class="dbl"><div class="a">', '''<h2 class="sec">Coming Up</h2>
<div class="calbox"><div class="calrow"><div class="cd">Tonight</div><div>NASA's flashlight salute to Voyager 1</div></div>
<div class="calrow"><div class="cd">Wed</div><div>Central Michigan at UB, 7:30</div></div>
<div class="calrow"><div class="cd">Sun</div><div>Dolphins at Bills, 1:00; Jets at Chargers</div></div>
<div class="calrow"><div class="cd">Nov 26</div><div>Thanksgiving; Chiefs at Bills, 8:20</div></div>
<div class="calnote">Migraine log: Joanne, Monday; Garret, Saturday. Four logged this month.</div>
</div>
<h2 class="sec">The Ledger</h2>
<div class="ledger"><div class="num"><div class="cap">Rise in Niagara Falls water rates for 2027</div><div class="big">3%</div></div>
<div class="txt">The Falls Water Board has adopted next year's budget with the increase in it, the <i>Niagara Gazette</i> reports. The falls themselves remain free to look at.</div></div>
<h2 class="sec">On This Day</h2>
<div class="otd"><b>November 17, 1869</b> &mdash; The Suez Canal opened, joining the Mediterranean and the Red Sea and cutting weeks off the voyage between Europe and Asia.</div>
<h2 class="sec">Question of the Day</h2>
<div class="qotd">I have four wheels and no engine, a seat only a toddler fits in, and one wheel that always wants to go its own way. What am I? <i>Answer below the fold.</i></div>
''')
R('<b>Question of the Day:</b> A flashlight.', '<b>Question of the Day:</b> A shopping cart.')
S('headlines via ', ' &middot; scores and stats via Sportradar', 'headlines via The New York Times, CBS, the BBC, Wayfair, WIVB, The Record North Shore, Axios, IKEA, WXXI, WKBW, the Hollywood Reporter, the <i>Niagara Gazette</i>, Buffalo Rumblings, ProFootballTalk')
ed = {'date': '2026-11-17', 'no': 146, 'body_html': src, 'plate_path': '/home/claude/plate146.jpg', 'plate_caption': 'A test drive at the store',
      'headline': "What the data centers put in the air · A Wayfair store for the old Boulevard Mall · Pattinson is Bond"}
for p in ['/home/claude/site/data/edition-2026-11-17.json', '/home/claude/edition-2026-11-17.json']:
    json.dump(ed, open(p, 'w'), ensure_ascii=False, indent=1)
print('ok', len(src))
