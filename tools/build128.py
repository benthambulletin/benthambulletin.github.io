import json, subprocess
src = json.load(open('/home/claude/site/data/edition-2026-10-29.json'))['body_html']

def R(a, c):
    global src
    assert src.count(a) == 1, ('R', a[:60], src.count(a))
    src = src.replace(a, c)

def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50])
    src = src[:i] + new + src[j:]

R('No. 127', 'No. 128')
R('Thursday &middot; October 29 &middot; 2026', 'Friday &middot; October 30 &middot; 2026')
S('<div class="tiles">', '<div class="plate-wrap">', '''<div class="tiles">
  <div class="tile"><div class="v">57&deg;</div><div class="k">Partly Sunny</div></div>
  <div class="tile"><div class="v">6:10</div><div class="k">Sunset &middot; 1&frac12; min earlier</div></div>
  <div class="tile urg"><div class="v">4</div><div class="k">Days to Election Day</div></div>
</div>
''')
R('alt="Three trees in full gold and orange leaf against a deep blue sky, fallen leaves on the grass below"',
  'alt="Two painted pumpkins dressed as storybook characters, one blue and bandaged, one purple with a green bow, beside a Little Miss Naughty book on fallen leaves"')
R('<div class="plate-sub">Gold and orange &middot; <span style="white-space:nowrap">Photo by Gregg</span></div>',
  '<div class="plate-sub">Mr. Bump and Little Miss Naughty, in pumpkin</div>')

S('<div class="fam">', '<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass',
'''<div class="fam"><b>Halloween is tomorrow</b>, and the pumpkins on the cover came dressed for it: Mr. Bump in his bandages and Little Miss Naughty, book and all.
<div class="line" style="margin-top:.4rem"><span class="lbl t">The log</span> Days since the last migraine: Garret 1, Dad 24, Mom 21. October so far: Garret four, Dad one, Mom one.</div>
<ul class="cal">
<li><span class="dt">Oct 31</span><span>Halloween</span></li>
<li><span class="dt">Nov 1</span><span>Raiders at Jets, 1:00 &middot; Ravens at Bills, 1:00</span></li>
<li><span class="dt">Nov 1</span><span>Clocks fall back &middot; early voting ends</span></li>
<li><span class="dt">Nov 3</span><span>Election Day</span></li>
</ul>
<div class="ask"><b>Send something to the paper:</b> a photo, a story, your Sunday answer or a date for the calendar, at <a href="https://tally.so/r/rjxDpl">tally.so/r/rjxDpl</a>. It runs the next morning under your name.<br><b>Had a migraine?</b> Log it at <a href="https://tally.so/r/obWNYP">tally.so/r/obWNYP</a>.</div></div>
<div class="pnote"><b>From the Group Chat &middot; Kaylani</b> &middot; <i>Tommy's 2 Cents, satire</i><br>
<b>BREAKING: Hamburg Voters to Decide Fate of Cheeseburger.</b> In a move that has left residents stunned, a proposition has made its way onto the Village of Hamburg ballot that would ban cheese on any hamburger sold within village limits. Supporters of "Proposition Plain Patty" say the town that gave the world the hamburger should honor its "original, unadulterated recipe," with fines of up to $50 per slice. "The hamburger was born here naked, and it should stay that way," said a spokesperson for the Committee for Burger Purity. One diner owner is already stockpiling American singles "in case things go underground." Polls open Tuesday. Cheese lovers are urged to make their voices heard, or forever hold their pickles.<br>
<b>Joanne:</b> This is an OUTRAGE. My family has been putting cheese on burgers in this village for three generations and I will NOT be told how to eat my lunch. See you at the polls!!! &#129472;&#127828;</div>
''')

S('<div class="wx">', '<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky',
'''<div class="wx"><div class="bigtemp">57<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">Behind the front: a breezy, partly sunny 57, and a cold night for carving</span>
Low <b>36&deg;</b> tonight &middot; northwest wind around 12 today<br>Dry right through Halloween and Sunday</div></div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">48<sup>&deg;</sup></div><div class="d">Cloudy &middot; high 57&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">52<sup>&deg;</sup></div><div class="d">Mostly cloudy &middot; high 55&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">50<sup>&deg;</sup></div><div class="d">Cloudy &middot; high 57&deg;</div></div>
</div>
<div class="strip5">
  <div><div class="d">Fri</div><div class="i">&#9729;</div><div class="h">57</div><div class="w">partly sunny</div></div>
  <div><div class="d">Sat</div><div class="i">&#9728;</div><div class="h">58</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Sun</div><div class="i">&#9729;</div><div class="h">64</div><div class="w">partly sunny</div></div>
  <div><div class="d">Mon</div><div class="i">&#9729;</div><div class="h">64</div><div class="w">partly sunny</div></div>
  <div><div class="d">Tue</div><div class="i">&#127782;</div><div class="h">68</div><div class="w">slight chance showers</div></div>
</div>
<div class="line"><span class="lbl r">Halloween</span> Mostly sunny and 58; trick-or-treat night partly cloudy and dry, falling toward 39. <span class="lbl r">Frost</span> Scottsville dips to 34 Saturday night.</div>
<div class="line"><span class="lbl t">Election Day</span> Tuesday 68, with a 20 percent chance of showers. <span class="lbl t">Outdoor window</span> Saturday and Sunday.</div>
''')

S('<div class="sky">', '<h2 class="sec"><span class="o">&#10038;</span>The Ledger',
'''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 0 50 96 A22 46 0 0 0 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>A waning gibbous</b>, 74 percent lit, in Gemini; sets at 1:12 p.m., rises at 9:54 p.m.<br>
<span class="lbl t">Sun</span> 7:47a &ndash; 6:10p &middot; <b>10h 23m</b><br>
<span class="lbl t">New moon</span> Mon, Nov 9 &middot; <span class="lbl t">Beaver Moon</span> Tue, Nov 24</div></div>
<div class="line"><span class="lbl r">Tonight</span> Partly cloudy after the front. Saturn is well up in the southeast by 9; the moon doesn't rise until 9:54.</div>
<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>The moon squares Saturn in your sign</b>. A rule gets in the way. Follow it today, fight it Monday. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>The sun trines the moon in your sign</b>. Easy day. Say what you mean and people hear it. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Venus sextiles Jupiter in your sign</b>. You'll be the best-dressed at the party. Commit to the costume. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>Neptune sextiles Pluto</b>. Let the plan be loose this weekend. It'll come together. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Uranus trines Pluto</b>. Your season, your holiday. Something new suits you. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
<div style="font-family:'LOI';font-style:italic;font-size:.8rem;color:var(--soft);margin-top:.4rem">Positions computed for noon today at 14120. The sky is real; the readings are for fun.</div>
''')

S('<div class="ledger">', '<h2 class="sec"><span class="o">&#10038;</span>The National Wire',
'''<div class="ledger"><div class="num"><div class="cap">Ballots already cast in the midterms</div><div class="big">43 million+</div></div>
<div class="txt">Early voting nationwide is surging with four days to go, the BBC reports.</div></div>
''')

ballot = subprocess.run(['python3', '/home/claude/site/tools/ballot_box.py', '2026-10-30'], capture_output=True, text=True, cwd='/home/claude/site').stdout.strip()
assert ballot.startswith('<div class="ballot">')
S('<div class="wire"><div class="num">1</div><div><h3>Brewers', '<h2 class="sec"><span class="o">&#9962;</span>The Home Wire',
'''<div class="wire"><div class="num">1</div><div><h3>Update: Oleshky Empties Out</h3><p>The evacuation of the Russian-occupied Ukrainian city of Oleshky is under way, Russian and Ukrainian authorities confirm, with 25 buses allowed to carry up to 750 people out during a four-hour window this morning, the BBC reports. The ceasefire has covered the whole Kherson front since Tuesday so the road out could be cleared of mines; several hundred residents chose to stay.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>A $6.3 Billion Crypto Hack</h3><p>A North Korean unit was likely behind a hack that hit more than $6 billion on Binance, the world's biggest cryptocurrency exchange, a U.S. blockchain intelligence firm says, CBS reports. Binance says it froze about $3 billion, suspended withdrawals for a day or two and will cover all losses.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Google's AI Eats Its Ads</h3><p>Google lost about $500 billion in stock market value after its own executive said its conversational "AI mode" is cutting into the money it makes from ads beside ordinary search results, the BBC reports. The BBC notes millions now ask chatbots such as ChatGPT and Claude instead of searching.</p></div></div>
''' + ballot + '\n')

S('<div class="wire"><div class="num">1</div><div><h3>Rochester', '<h2 class="sec"><span class="o">&#9733;</span>The Marquee',
'''<div class="wire"><div class="num">1</div><div><h3>Monroe County &middot; Fewer Kids With Lead</h3><p>The number of Monroe County children found with elevated lead in their blood fell 27 percent in 2025, from 299 to 217, even as more were tested, county data released Thursday show, WXXI reports. Of 14,556 children tested, 217 topped the county's threshold; health experts say no level of lead is safe.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Niagara Falls &middot; Goodyear Plant Closing</h3><p>The Goodyear plant on 56th Street will close Dec. 30 and lay off 51 of its workers, a state WARN notice confirms, the <i>Niagara Gazette</i> reports. Five employees will stay on.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Fredonia &middot; On to the Funke Bowl</h3><p>Fredonia's football team beat Eden/North Collins 39&ndash;21 Thursday to reach the Chuck Funke Bowl final in Class C, the <i>Observer</i> reports. It's the second Hillbillies playoff win this week, after volleyball's quarterfinal sweep.</p></div></div>
''')

S('<div class="wire"><div class="num">1</div><div><h3>Paddington', '<h2 class="sec"><span class="o">&#127944;</span>The Gridiron',
'''<div class="wire"><div class="num">1</div><div><h3>Patrick Stewart Dies at 86</h3><p>Patrick Stewart, Captain Picard on <i>Star Trek: The Next Generation</i> and Professor X in the <i>X-Men</i> films, has died at 86, CBS reports. His friend and co-star Ian McKellen called him "a man to rely on, admire and in my case, love," the <i>Hollywood Reporter</i> reports.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>The Monster Is Back</h3><p>Early reactions to <i>Godzilla Minus Zero</i> from press screenings this week call it another hit, the <i>Hollywood Reporter</i> reports. It opens in North American theaters Nov. 6.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Noah Kahan at Highmark</h3><p>Noah Kahan is bringing his "The Last of the Bugs" world tour to the new Highmark Stadium, WKBW reports. It's part of a 2027 stadium tour, Rochester First says.</p></div></div>
''')

S('<div class="touch-head">Rally Night</div>', '<div class="pnote">',
'''<div class="touch-head">Allen and Jackson</div>
<div class="line"><b>Bills</b> &middot; Josh Allen won't take sides in the old debate over whether he or Lamar Jackson is the better quarterback, the AP reports: "He's been one of the best if not the best," Allen said. Fans filled Niagara Square for Thursday night's rally; Baltimore visits Sunday at 1:00.</div>
<div class="line"><b>Jets</b> &middot; Two straight close losses, by seven at New England and three to Miami; the Raiders (3&ndash;4) come to MetLife Sunday at 1:00 with the Jets looking to snap it.</div>
''')
S('<div class="pnote"><b>The Sunday Tax', '<table class="tbl">', '')

S('<div class="touch-head">Martinsville Sunday</div>', '<h2 class="sec"><span class="o">&#9790;</span>On This Day',
'''<div class="touch-head">Martinsville Sunday</div>
<div class="line">Larson by 73 over Hamlin, 74 over Bell, with two races left.</div>
''')

S('<div class="otd">', '<h2 class="sec"><span class="o">&#10023;</span>Question of the Day',
'''<div class="otd"><b>October 30, 1938</b> &mdash; Orson Welles's radio play of <i>The War of the Worlds</i>, staged as live news bulletins about a Martian landing in New Jersey, aired on CBS the night before Halloween.</div>
''')

S('<div class="qotd">', '<div class="dbl">',
'''<div class="qotd">I sleep upside down all day, fly out at dusk, and hang on half the porches in town this weekend. What am I? <i>Answer below the fold.</i></div>
''')
R("<b>Question of the Day:</b> A candy bar.", "<b>Question of the Day:</b> A bat.")
S('<div class="s">Forecast per', '<div class="sig">',
'''<div class="s">Forecast per NWS Buffalo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; sky computed for 14120 &middot; election summary from the paper's election tracker &middot; headlines via BBC, CBS, WXXI, Niagara Gazette, Dunkirk Observer, AP, WKBW, WIVB, Rochester First, Hollywood Reporter &middot; scores and NASCAR points via Sportradar and Hendrick Motorsports</div>
''')

ed = {"date": "2026-10-30", "no": 128, "body_html": src, "plate_path": "/home/claude/plate128.jpg",
      "plate_caption": "Mr. Bump and Little Miss Naughty, in pumpkin",
      "headline": "Halloween eve · Oleshky empties out · Patrick Stewart dies · Allen and Jackson"}
for p in ['/home/claude/edition-2026-10-30.json', '/home/claude/site/data/edition-2026-10-30.json']:
    json.dump(ed, open(p, 'w'), ensure_ascii=False, indent=1)
print('ok')
