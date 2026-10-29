import json, subprocess
src = json.load(open('/home/claude/site/data/edition-2026-10-28.json'))['body_html']

def R(a, c):
    global src
    assert src.count(a) == 1, ('R', a[:60], src.count(a))
    src = src.replace(a, c)

def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50])
    src = src[:i] + new + src[j:]

R('No. 126', 'No. 127')
R('Wednesday &middot; October 28 &middot; 2026', 'Thursday &middot; October 29 &middot; 2026')
S('<div class="tiles">', '<div class="plate-wrap">', '''<div class="tiles">
  <div class="tile"><div class="v">70&deg;</div><div class="k">Mostly Sunny</div></div>
  <div class="tile"><div class="v">6:12</div><div class="k">Sunset &middot; 1&frac12; min earlier</div></div>
  <div class="tile urg"><div class="v">5</div><div class="k">Days to Election Day</div></div>
</div>
''')
R('alt="A bright moon behind thin clouds, framed by tall pines over a dark treeline and a lawn"',
  'alt="Three trees in full gold and orange leaf against a deep blue sky, fallen leaves on the grass below"')
R('<div class="plate-sub">Moonrise on the Chautauqua Ridge &middot; <span style="white-space:nowrap">Photo by Gregg</span></div>',
  '<div class="plate-sub">Gold and orange &middot; <span style="white-space:nowrap">Photo by Gregg</span></div>')

S('<div class="fam">', '<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass',
'''<div class="fam"><b>Gregg sent the cover again</b>, this time three trees in full color. Halloween is Saturday, two days out.
<div class="line" style="margin-top:.4rem"><span class="lbl t">The log</span> Garret logged a migraine at 3 a.m. today. Days since the last one: Garret 0, Dad 23, Mom 20. October so far: Garret four, Dad one, Mom one.</div>
<ul class="cal">
<li><span class="dt">Oct 31</span><span>Halloween</span></li>
<li><span class="dt">Nov 1</span><span>Raiders at Jets, 1:00 &middot; Ravens at Bills, 1:00</span></li>
<li><span class="dt">Nov 1</span><span>Clocks fall back &middot; early voting ends</span></li>
<li><span class="dt">Nov 3</span><span>Election Day</span></li>
</ul>
<div class="ask"><b>Send something to the paper:</b> a photo, a story, your Sunday answer or a date for the calendar, at <a href="https://tally.so/r/rjxDpl">tally.so/r/rjxDpl</a>. It runs the next morning under your name.<br><b>Had a migraine?</b> Log it at <a href="https://tally.so/r/obWNYP">tally.so/r/obWNYP</a>.</div></div>
''')

S('<div class="wx">', '<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky',
'''<div class="wx"><div class="bigtemp">70<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">A gusty, 70-degree Thursday, then the cold front: showers tonight and a sweater Friday</span>
Gusts to 37 &middot; showers possible after 5 p.m., 30%<br>Low <b>45&deg;</b> tonight; showers before 11, 50%</div></div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">54<sup>&deg;</sup></div><div class="d">Clear &middot; high 70&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">57<sup>&deg;</sup></div><div class="d">Clear &middot; high 71&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">54<sup>&deg;</sup></div><div class="d">Clear &middot; high 75&deg;</div></div>
</div>
<div class="strip5">
  <div><div class="d">Thu</div><div class="i">&#127782;</div><div class="h">70</div><div class="w">sunny, showers late</div></div>
  <div><div class="d">Fri</div><div class="i">&#9729;</div><div class="h">58</div><div class="w">partly sunny</div></div>
  <div><div class="d">Sat</div><div class="i">&#9728;</div><div class="h">58</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Sun</div><div class="i">&#9729;</div><div class="h">64</div><div class="w">partly sunny</div></div>
  <div><div class="d">Mon</div><div class="i">&#9729;</div><div class="h">64</div><div class="w">partly sunny</div></div>
</div>
<div class="line"><span class="lbl r">Storms</span> Dunkirk has showers and thunderstorms tonight, 76 percent; Scottsville, likely. <span class="lbl r">Halloween</span> Mostly sunny and 58; trick-or-treat night mostly cloudy, low 39, a 1 percent chance of rain.</div>
<div class="line"><span class="lbl r">Frost</span> Scottsville dips to 34 Friday and Saturday nights. <span class="lbl t">Outdoor window</span> This afternoon, before the wind and showers.</div>
''')

S('<div class="sky">', '<h2 class="sec"><span class="o">&#10038;</span>The Ledger',
'''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 0 50 96 A31 46 0 0 0 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>A waning gibbous</b>, 84 percent lit, in Taurus; sets at 12:13 p.m., rises at 8:42 p.m.<br>
<span class="lbl t">Sun</span> 7:46a &ndash; 6:12p &middot; <b>10h 26m</b><br>
<span class="lbl t">New moon</span> Mon, Nov 9 &middot; <span class="lbl t">Beaver Moon</span> Tue, Nov 24</div></div>
<div class="line"><span class="lbl r">Tonight</span> Clouds and showers likely hide it, but the moon rises in the northeast at 8:42, more than two and a half hours after sunset. Sunday the clocks fall back and sunset jumps to just after 5.</div>
<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>Venus sextiles Jupiter</b>. Generous mood all around. Say yes to the small favor. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>The moon trines Venus</b>. Comfort food tastes better tonight. Make the big pot. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>The moon sextiles Jupiter in your sign</b>. Lucky streak. Buy the scratch-off, but just one. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>Uranus trines Pluto</b>. A change you've been putting off goes easier than expected. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Mercury, in your sign, squares Mars</b>. Short fuse in a strong wind. Hold onto your hat and your temper. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
<div style="font-family:'LOI';font-style:italic;font-size:.8rem;color:var(--soft);margin-top:.4rem">Positions computed for noon today at 14120. The sky is real; the readings are for fun.</div>
''')

S('<div class="ledger">', '<h2 class="sec"><span class="o">&#10038;</span>The National Wire',
'''<div class="ledger"><div class="num"><div class="cap">Flu cases reported in New York in one October week</div><div class="big">3,500+</div></div>
<div class="txt">Plus more than 230 hospitalizations for the week ending Oct. 17. The state has declared flu prevalent, earlier than usual, WKBW reports.</div></div>
''')

ballot = subprocess.run(['python3', '/home/claude/site/tools/ballot_box.py', '2026-10-29'], capture_output=True, text=True, cwd='/home/claude/site').stdout.strip()
assert ballot.startswith('<div class="ballot">')
S('<div class="wire"><div class="num">1</div><div><h3>Deadly Train Crash', '<h2 class="sec"><span class="o">&#9962;</span>The Home Wire',
'''<div class="wire"><div class="num">1</div><div><h3>Brewers Win It All</h3><p>Milwaukee beat Tampa Bay 4&ndash;1 in Game 5 Wednesday night to win the World Series, the first championship in the franchise's history, CBS reports. The Brewers took the series four games to one.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Update: Spain's Toll Rises to 68</h3><p>At least 68 people died and dozens were hurt when one high-speed train hit the back of another in central Spain Wednesday, CBS reports. The BBC has released audio of exchanges between the control center and the drivers before the crash; it is Spain's second major train crash this year.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>DoorDash Buys Instacart</h3><p>DoorDash said this morning it will buy Instacart for $17 billion, or $65 a share, joining the biggest names in restaurant and grocery delivery, CBS reports. DoorDash says more supermarkets will be able to use Instacart's tools to run their own websites.</p></div></div>
''' + ballot + '\n')

S('<div class="wire"><div class="num">1</div><div><h3>Rochester', '<h2 class="sec"><span class="o">&#9733;</span>The Marquee',
'''<div class="wire"><div class="num">1</div><div><h3>Lockport &middot; Atomic-Era Mill Cleanup Gets Its Contractor</h3><p>The Army Corps of Engineers awarded a $249 million contract to Sevenson Environmental to clean up the old Guterl Specialty Steel site off Ohio Street, the <i>Niagara Gazette</i> reports. Nine buildings in the former Simonds Saw &amp; Steel complex handled uranium for the atomic program after World War II; work is expected to start next year.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Fredonia &middot; Volleyball Rolls On</h3><p>Fredonia's girls beat Salamanca Wednesday in the Section VI Class B2 volleyball quarterfinals at Fredonia High, the <i>Observer</i> reports. Coach Amanda Krakowiak called a timeout with the first set tied 20&ndash;20 to reset her team.</p></div></div>
''')

S('<div class="wire"><div class="num">1</div><div><h3>Horror Night', '<h2 class="sec"><span class="o">&#127944;</span>The Gridiron',
'''<div class="wire"><div class="num">1</div><div><h3>Paddington Stays in London</h3><p><i>Paddington the Musical</i> has extended its West End run through June 2028, Variety reports. It tied the record with seven Olivier Awards this year and nears its first anniversary at the Savoy Theatre.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>U2, Up Close</h3><p>U2 will play a small, invitation-only show for BBC Music in central London on Nov. 3, Billboard reports. The set mixes classics with songs from the coming album <i>Carnaval de Luz</i> and airs on BBC Two later in November.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Prada Goes Hand-Drawn</h3><p>Prada's new holiday campaign starring Sadie Sink and Maya Hawke was drawn by hand by veteran Disney animator John Pomeroy, Variety reports. It has drawn wide praise online since its debut Wednesday night, at a time when AI is everywhere in advertising.</p></div></div>
''')

S('<div class="touch-head">Four Days to Kickoff</div>', '<table class="tbl">',
'''<div class="touch-head">Rally Night</div>
<div class="line"><b>Bills</b> &middot; Tonight's Bills rally in Niagara Square runs 5:30 to 7:30, ending with a light show on the Statler; bring a jacket, since the Weather Service has gusts to 37 and a 30 percent chance of showers after 5. Baltimore visits Sunday at 1:00.</div>
<div class="line"><b>Jets</b> &middot; The Jets are 1&ndash;2 at MetLife this season, their home win a 17&ndash;12 decision over Cleveland on Oct. 11. They get the Raiders there Sunday at 1:00.</div>
<div class="pnote"><b>The Sunday Tax &middot; Week 8.</b> Picks at <a href="https://tally.so/r/RGOakJ">tally.so/r/RGOakJ</a>; standings at <a href="https://benthambulletin.github.io/pool/">benthambulletin.github.io/pool</a>. $5 a week, straight-up winners, the pot to the best record. Anyone with the link can play. Sheets lock at each kickoff; first game tonight at 8:15, Panthers at Packers.</div>
''')

S('<div class="touch-head">Two to Go</div>', '<h2 class="sec"><span class="o">&#9790;</span>On This Day',
'''<div class="touch-head">Martinsville Sunday</div>
<div class="line">Larson 2,441, with Hamlin 73 behind and Bell 74.</div>
''')

S('<div class="otd">', '<h2 class="sec"><span class="o">&#10023;</span>Question of the Day',
'''<div class="otd"><b>October 29, 1929</b> &mdash; Black Tuesday: the stock market crashed on Wall Street, the start of the Great Depression.</div>
''')

S('<div class="qotd">', '<div class="dbl">',
'''<div class="qotd">Kids knock on doors for me, dentists frown at me, and the best houses on the block hand me out full-size. What am I? <i>Answer below the fold.</i></div>
''')
R("<b>Question of the Day:</b> Enough to cover one square mile to a depth of 50 feet, Gregg says.", "<b>Question of the Day:</b> A candy bar.")
S('<div class="s">Forecast per', '<div class="sig">',
'''<div class="s">Forecast per NWS Buffalo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; sky computed for 14120 &middot; election summary from the paper's election tracker &middot; Sunday Tax from the pool's standings &middot; headlines via CBS, BBC, WKBW, Niagara Gazette, Dunkirk Observer, Variety, Billboard &middot; scores and NASCAR points via Sportradar and Hendrick Motorsports</div>
''')

ed = {"date": "2026-10-29", "no": 127, "body_html": src, "plate_path": "/home/claude/plate127.jpg",
      "plate_caption": "Gold and orange · Photo by Gregg",
      "headline": "Brewers win it all · Spain toll rises · DoorDash buys Instacart · Rally night"}
for p in ['/home/claude/edition-2026-10-29.json', '/home/claude/site/data/edition-2026-10-29.json']:
    json.dump(ed, open(p, 'w'), ensure_ascii=False, indent=1)
print('ok')
