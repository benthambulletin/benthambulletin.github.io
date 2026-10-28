import json, subprocess
src = json.load(open('/home/claude/site/data/edition-2026-10-27.json'))['body_html']

def R(a, c):
    global src
    assert src.count(a) == 1, ('R', a[:60], src.count(a))
    src = src.replace(a, c)

def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50])
    src = src[:i] + new + src[j:]

R('No. 125', 'No. 126')
R('Tuesday &middot; October 27 &middot; 2026', 'Wednesday &middot; October 28 &middot; 2026')
S('<div class="tiles">', '<div class="plate-wrap">', '''<div class="tiles">
  <div class="tile"><div class="v">67&deg;</div><div class="k">Mostly Sunny</div></div>
  <div class="tile"><div class="v">6:13</div><div class="k">Sunset &middot; 1&frac12; min earlier</div></div>
  <div class="tile urg"><div class="v">6</div><div class="k">Days to Election Day</div></div>
</div>
''')
R('alt="A smiling little boy and a man in glasses wearing woven baskets upside down as hats"',
  'alt="A bright moon behind thin clouds, framed by tall pines over a dark treeline and a lawn"')
R('<div class="plate-sub">Hats on</div>', '<div class="plate-sub">Moonrise on the Chautauqua Ridge</div>')

S('<div class="fam">', '<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass',
'''<div class="fam"><b>The moon over the Chautauqua Ridge</b>, on the cover, came in from Garret Tuesday night. Halloween is Saturday, three days out, and the forecast is kind to it.
<div class="line" style="margin-top:.4rem"><span class="lbl t">The log</span> Garret logged a migraine Tuesday at 6 a.m. Days since the last one: Garret 1, Dad 22, Mom 19. October so far: Garret three, Dad one, Mom one.</div>
<ul class="cal">
<li><span class="dt">Oct 31</span><span>Halloween</span></li>
<li><span class="dt">Nov 1</span><span>Raiders at Jets, 1:00 &middot; Ravens at Bills, 1:00</span></li>
<li><span class="dt">Nov 1</span><span>Clocks fall back &middot; early voting ends</span></li>
<li><span class="dt">Nov 3</span><span>Election Day</span></li>
</ul>
<div class="ask"><b>Send something to the paper:</b> a photo, a story, your Sunday answer or a date for the calendar, at <a href="https://tally.so/r/rjxDpl">tally.so/r/rjxDpl</a>. It runs the next morning under your name.<br><b>Had a migraine?</b> Log it at <a href="https://tally.so/r/obWNYP">tally.so/r/obWNYP</a>.</div></div>
''')

S('<div class="wx">', '<h2 class="sec"><span class="o">&#127810;</span>The Turning',
'''<div class="wx"><div class="bigtemp">67<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">A warm spell in late October: mostly sunny and 67 today, warmer and windy tomorrow</span>
Low <b>49&deg;</b> tonight &middot; light southeast wind<br>Thursday 72, gusts to 33; showers possible after 5 p.m.</div></div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">43<sup>&deg;</sup></div><div class="d">Mostly cloudy &middot; high 67&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">43<sup>&deg;</sup></div><div class="d">Clear &middot; high 66&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">39<sup>&deg;</sup></div><div class="d">Mostly clear &middot; high 69&deg;</div></div>
</div>
<div class="strip5">
  <div><div class="d">Wed</div><div class="i">&#9728;</div><div class="h">67</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Thu</div><div class="i">&#127782;</div><div class="h">72</div><div class="w">sunny, showers late</div></div>
  <div><div class="d">Fri</div><div class="i">&#9728;</div><div class="h">60</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Sat</div><div class="i">&#9728;</div><div class="h">60</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Sun</div><div class="i">&#9729;</div><div class="h">64</div><div class="w">partly sunny</div></div>
</div>
<div class="line"><span class="lbl r">Halloween</span> Mostly sunny and 60 Saturday; trick-or-treat night turns mostly cloudy and cool, low 40, with only a 2 percent chance of rain.</div>
<div class="line"><span class="lbl t">Thursday night</span> Showers before 2 a.m., 50 percent, with gusts to 30; the Bills rally in Niagara Square starts at 5:30. <span class="lbl t">Outdoor window</span> Today.</div>
''')

S('<div class="line"><b>Report day tomorrow.</b>', '<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky',
'''<div class="line">The state's new foliage report comes out this afternoon; the numbers run tomorrow.</div>
''')

S('<div class="sky">', '<h2 class="sec"><span class="o">&#10038;</span>The Ledger',
'''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 0 50 96 A38 46 0 0 0 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>A waning gibbous</b>, 91 percent lit, in Taurus; sets at 11:02 a.m., rises at 7:40 p.m.<br>
<span class="lbl t">Sun</span> 7:45a &ndash; 6:13p &middot; <b>10h 28m</b><br>
<span class="lbl t">New moon</span> Mon, Nov 9 &middot; <span class="lbl t">Beaver Moon</span> Tue, Nov 24</div></div>
<div class="line"><span class="lbl r">Tonight</span> Saturn has the early evening to itself; by the time the moon clears the northeastern trees around 7:40, the ringed planet is high in the southeast.</div>
<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>The moon sextiles Saturn in your sign</b>. A steady day. Finish the boring thing first. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>Uranus sextiles Neptune</b>. An odd idea turns out to be a good one. Say it out loud. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Uranus trines Pluto</b>. Out with the old costume, in with the new. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>Mercury squares Mars</b>. The group chat gets heated. Send the GIF, not the paragraph. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>The sun in your sign squares Pluto</b>. Someone pushes. Push back once, kindly. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
<div style="font-family:'LOI';font-style:italic;font-size:.8rem;color:var(--soft);margin-top:.4rem">Positions computed for noon today at 14120. The sky is real; the readings are for fun.</div>
''')

S('<div class="ledger">', '<h2 class="sec"><span class="o">&#10038;</span>The National Wire',
'''<div class="ledger"><div class="num"><div class="cap">What the Iran war has cost the U.S. military so far</div><div class="big">$47.1 billion</div></div>
<div class="txt">Through mid-October, by Central Command's estimate obtained by CBS, most of it replacing spent munitions. Three months ago the Pentagon put it at about $37.5 billion.</div></div>
''')

ballot = subprocess.run(['python3', '/home/claude/site/tools/ballot_box.py', '2026-10-28'], capture_output=True, text=True, cwd='/home/claude/site').stdout.strip()
assert ballot.startswith('<div class="ballot">')
S('<div class="wire"><div class="num">1</div><div><h3>Israel Votes', '<h2 class="sec"><span class="o">&#9962;</span>The Home Wire',
'''<div class="wire"><div class="num">1</div><div><h3>Deadly Train Crash in Spain</h3><p>A high-speed train slammed into the back of another that had stopped in Toledo province, in central Spain, this morning, derailing two cars and killing at least 30 people, regional officials told AFP, CBS reports. Both trains were running from Madrid toward Seville; the cause isn't known yet.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Update: Israel's Vote Ends in a Stalemate</h3><p>Neither Prime Minister Benjamin Netanyahu's coalition nor Gadi Eisenkot's opposition bloc won a majority, exit polls show, CBS reports. With 70 percent counted, Netanyahu's Likud has 20.6 percent and Eisenkot's Yashar 15.9, and the bargaining to build a government has begun.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Methane Limits Rolled Back</h3><p>President Trump said Tuesday he is "terminating" a Biden-era rule limiting methane, a planet-warming gas, from oil and gas drilling, NPR reports. He said the change would unlock 210 million barrels of oil, which NPR notes is about 10 days of U.S. use.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>The Rays Stay Alive</h3><p>Tampa Bay beat Milwaukee 4&ndash;3 Tuesday night to win Game 4 of the World Series. The Brewers still lead three games to one, and Game 5 is tonight at 8 in Tampa Bay.</p></div></div>
''' + ballot + '\n')

S('<div class="wire"><div class="num">1</div><div><h3>Rochester', '<h2 class="sec"><span class="o">&#9733;</span>The Marquee',
'''<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Orangutans Are Coming Back</h3><p>Seneca Park Zoo broke ground Tuesday on its $135 million Tropics exhibit, WXXI and Rochester First report. Orangutans and lemurs, gone from the zoo since 2018, will live there when it opens in late 2029.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Town of Niagara &middot; Neighbors Ask to Move for Good</h3><p>Families near Gill Creek in the Town of Niagara, where state and federal testing found dangerous radiation levels, are asking to be relocated permanently, not just housed temporarily, WKBW reports. The EPA moved some families whose results came back high, but a few dozen neighbors around them were never moved.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Fredonia &middot; Boil Your Water</h3><p>Fredonia is under a boil-water order for "high turbidity levels and treatment deficiencies," meaning cloudy water the plant couldn't fully treat, the <i>Observer</i> reports. The village bought 966,000 gallons from Dunkirk over the weekend; boil water for at least a minute before drinking, cooking or brushing teeth.</p></div></div>
''')

S('<div class="wire"><div class="num">1</div><div><h3>Jay-Z', '<h2 class="sec"><span class="o">&#127944;</span>The Gridiron',
'''<div class="wire"><div class="num">1</div><div><h3>Horror Night on <i>Dancing With the Stars</i></h3><p><i>Dancing With the Stars</i> went horror for Halloween week, with routines to music from <i>Sinners</i>, <i>Black Swan</i> and <i>Joker</i>, the <i>Hollywood Reporter</i> reports. The night brought the season's first perfect score and a double elimination; Jackson Olson and Tyler Cameron went home.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Demi Lovato Says She's Fine</h3><p>Demi Lovato says she's "fine" after a reported brief hospital visit for an allergic reaction Tuesday, Billboard reports, citing <i>People</i>. In a since-deleted post, she guessed she's newly allergic to passionfruit or sushi.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Foo Fighters Take Over Kimmel</h3><p>Foo Fighters are playing four nights on <i>Jimmy Kimmel Live!</i> for the show's Halloween week, Billboard reports. Monday they played "Window" from their 12th album, <i>Your Favorite Toy</i>; Tuesday they reached back to their early songs.</p></div></div>
''')

S('<div class="touch-head">Ravens and Raiders</div>', '<table class="tbl">',
'''<div class="touch-head">Four Days to Kickoff</div>
<div class="line"><b>Bills</b> &middot; Baltimore was outscored 35&ndash;0 after halftime in Sunday's loss to Cincinnati and has been outscored by 70 points in second halves this season, the AP reports; Lamar Jackson has missed three straight games with an ankle injury. The Bills (5&ndash;1) host them Sunday at 1:00.</div>
<div class="line"><b>Jets</b> &middot; Sportradar's model calls Sunday's game against the Raiders close to a coin flip, 53 percent for the Jets. After that the schedule stiffens: at Kansas City Nov. 8, then the Bills at MetLife Nov. 15.</div>
<div class="pnote"><b>The Sunday Tax &middot; Week 8.</b> Picks at <a href="https://tally.so/r/RGOakJ">tally.so/r/RGOakJ</a>; standings at <a href="https://benthambulletin.github.io/pool/">benthambulletin.github.io/pool</a>. $5 a week, straight-up winners, the pot to the best record. Anyone with the link can play. Sheets lock at each kickoff; first game Thu 8:15 p.m., Panthers at Packers.</div>
''')
S('<div class="line"><b>Monday night.</b>', '<h2 class="sec"><span class="o">&#9873;</span>The Chase', '')

S('<div class="touch-head">Martinsville Sunday</div>', '<h2 class="sec"><span class="o">&#9790;</span>On This Day',
'''<div class="touch-head">Two to Go</div>
<div class="line">Larson leads Hamlin by 73 and Bell by 74, with Martinsville Sunday and Homestead Nov. 8.</div>
''')

S('<div class="otd">', '<h2 class="sec"><span class="o">&#10023;</span>Question of the Day',
'''<div class="otd"><b>October 28, 1886</b> &mdash; President Grover Cleveland, a former mayor of Buffalo, dedicated the Statue of Liberty in New York Harbor.</div>
''')

S('<div class="qotd">', '<div class="dbl">',
'''<div class="qotd"><b>Gregg asks:</b> How much fog can one pail of water make? <i>Answer below the fold.</i></div>
''')
R("<b>Question of the Day:</b> A witch's hat.", "<b>Question of the Day:</b> Enough to cover one square mile to a depth of 50 feet, Gregg says.")
S('<div class="s">Forecast per', '<div class="sig">',
'''<div class="s">Forecast per NWS Buffalo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; sky computed for 14120 &middot; election summary from the paper's election tracker &middot; Sunday Tax from the pool's standings &middot; headlines via CBS, NPR, WXXI, Rochester First, WKBW, Dunkirk Observer, AP, Hollywood Reporter, Billboard &middot; scores, odds and NASCAR points via Sportradar and Hendrick Motorsports</div>
''')

ed = {"date": "2026-10-28", "no": 126, "body_html": src, "plate_path": "/home/claude/plate126.jpg",
      "plate_caption": "Moonrise on the Chautauqua Ridge",
      "headline": "Spain train crash · Israel stalemate · Fredonia boil order · Gregg's fog question"}
for p in ['/home/claude/edition-2026-10-28.json', '/home/claude/site/data/edition-2026-10-28.json']:
    json.dump(ed, open(p, 'w'), ensure_ascii=False, indent=1)
print('ok')
