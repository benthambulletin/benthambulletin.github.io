import json, subprocess
src = json.load(open('/home/claude/site/data/edition-2026-10-30.json'))['body_html']

def R(a, c):
    global src
    assert src.count(a) == 1, ('R', a[:60], src.count(a))
    src = src.replace(a, c)

def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50])
    src = src[:i] + new + src[j:]

R('No. 128', 'No. 129')
R('Friday &middot; October 30 &middot; 2026', 'Saturday &middot; October 31 &middot; 2026')
S('<div class="tiles">', '<div class="dbl-tight">', '''<div class="tiles">
  <div class="tile"><div class="v">56&deg;</div><div class="k">Sunny</div></div>
  <div class="tile"><div class="v">6:09</div><div class="k">Sunset &middot; last on daylight time</div></div>
  <div class="tile urg"><div class="v">3</div><div class="k">Days to Election Day</div></div>
</div>
''')

S('<h2 class="sec"><span class="o">&#9825;</span>Family Today<span class="o">&#9825;</span></h2>', '<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass',
'''<h2 class="sec"><span class="o">&#9825;</span>Family Today<span class="o">&#9825;</span></h2>
<div class="alert">&#127875; <b>Happy Halloween!</b></div>
<div class="fam"><b>Trick-or-treat night</b> looks dry and partly cloudy, with a low of 38 by morning. Bring the porch light on early: sunset is 6:09, and tonight the clocks fall back an hour at 2 a.m.
<div class="line" style="margin-top:.4rem"><span class="lbl t">The log</span> Days since the last migraine: Garret 2, Dad 25, Mom 2. October: Garret four, Dad one, Mom two.</div>
<ul class="cal">
<li><span class="dt">Today</span><span>Halloween &middot; clocks fall back tonight</span></li>
<li><span class="dt">Nov 1</span><span>Raiders at Jets, 1:00 &middot; Ravens at Bills, 1:00</span></li>
<li><span class="dt">Nov 1</span><span>Early voting ends</span></li>
<li><span class="dt">Nov 3</span><span>Election Day</span></li>
</ul>
<div class="ask"><b>Send something to the paper:</b> a photo, a story, your Sunday answer or a date for the calendar, at <a href="https://tally.so/r/rjxDpl">tally.so/r/rjxDpl</a>. It runs the next morning under your name.<br><b>Had a migraine?</b> Log it at <a href="https://tally.so/r/obWNYP">tally.so/r/obWNYP</a>.</div></div>
''')

S('<div class="wx">', '<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky',
'''<div class="wx"><div class="bigtemp">56<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">A sunny Halloween with light wind, then a cool, dry night for the costumes</span>
Low <b>38&deg;</b> tonight &middot; partly cloudy, 2% rain<br>Warming to 69 by Election Day</div></div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">39<sup>&deg;</sup></div><div class="d">Mostly clear &middot; high 56&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">39<sup>&deg;</sup></div><div class="d">Cloudy &middot; high 53&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">45<sup>&deg;</sup></div><div class="d">Cloudy &middot; high 56&deg;</div></div>
</div>
<div class="strip5">
  <div><div class="d">Sat</div><div class="i">&#9728;</div><div class="h">56</div><div class="w">sunny</div></div>
  <div><div class="d">Sun</div><div class="i">&#9728;</div><div class="h">64</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Mon</div><div class="i">&#9728;</div><div class="h">65</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Tue</div><div class="i">&#127782;</div><div class="h">69</div><div class="w">slight chance showers</div></div>
  <div><div class="d">Wed</div><div class="i">&#127782;</div><div class="h">70</div><div class="w">chance showers</div></div>
</div>
<div class="line"><span class="lbl r">Frost</span> Scottsville dips to 33 tonight; North Tonawanda 38. <span class="lbl t">Outdoor window</span> Today through Monday.</div>
<div class="line"><span class="lbl t">The Turning</span> Peak color is making its final appearance across Greater Niagara this weekend, the state's weekly report says, with Niagara Falls and Lewiston among the places changing most.</div>
''')

S('<div class="sky">', '<h2 class="sec"><span class="o">&#10038;</span>The Ledger',
'''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 0 50 96 A12 46 0 0 0 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>A waning gibbous</b>, 63 percent lit, in Gemini; sets at 1:58 p.m., rises at 11:11 p.m.<br>
<span class="lbl t">Sun</span> 7:49a &ndash; 6:09p &middot; <b>10h 20m</b><br>
<span class="lbl t">New moon</span> Mon, Nov 9 &middot; <span class="lbl t">Beaver Moon</span> Tue, Nov 24</div></div>
<div class="line"><span class="lbl r">Clocks</span> Standard time returns at 2 a.m. Sunday: set clocks back an hour. Tomorrow the sun rises at 6:50 and sets at 5:08.</div>
<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>Uranus sextiles Neptune in your sign</b>. A wild costume idea is the right one. Go with it. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>The moon squares Venus</b>. You'll want to keep the good candy. Share the second-best. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Mercury squares Mars in your sign</b>. A sharp comeback is on the tip of your tongue. Save it for the Bills game. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>Venus sextiles Jupiter</b>. Answer the door with a smile. It comes back to you. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Neptune sextiles Pluto</b>. The spookiest night falls in your season. You were made for this one. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
<div style="font-family:'LOI';font-style:italic;font-size:.8rem;color:var(--soft);margin-top:.4rem">Positions computed for noon today at 14120. The sky is real; the readings are for fun.</div>
''')

S('<div class="ledger">', '<h2 class="sec"><span class="o">&#10038;</span>The National Wire',
'''<div class="ledger"><div class="num"><div class="cap">Rise in U.S. energy prices over the past year</div><div class="big">20.4%</div></div>
<div class="txt">The September price index, WKBW reports. New York's heating-aid program, HEAP, opens for applications Monday, Nov. 2.</div></div>
''')

ballot = subprocess.run(['python3', '/home/claude/site/tools/ballot_box.py', '2026-10-31'], capture_output=True, text=True, cwd='/home/claude/site').stdout.strip()
assert ballot.startswith('<div class="ballot">')
S('<div class="wire"><div class="num">1</div><div><h3>Update: Oleshky', '<h2 class="sec"><span class="o">&#9962;</span>The Home Wire',
'''<div class="wire"><div class="num">1</div><div><h3>Patriot Missiles for Ukraine</h3><p>The State Department approved the sale of 500 Patriot interceptor missiles to Ukraine for $2.1 billion, paid for by Canada and European allies with no U.S. money, CBS reports. President Zelensky warned it could take "several years" for them all to arrive, the BBC reports.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Oil Profits Soar Again</h3><p>ExxonMobil earned $15.4 billion this quarter, more than double a year ago, and the three biggest oil companies made just over $36 billion together, NPR reports. The war in Iran has cut the oil moving out of the Middle East, and Brent crude trades around $113 a barrel.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>A Deal for Nature</h3><p>Nearly 200 countries meeting in Armenia agreed early Saturday on the key parts of a new action plan to protect nature, the BBC reports. It builds on the 2022 pledge to "halt and reverse" nature's decline, including protecting 30 percent of land and seas; money is still the sticking point.</p></div></div>
''' + ballot + '\n')

S('<div class="wire"><div class="num">1</div><div><h3>Monroe County', '<h2 class="sec"><span class="o">&#9733;</span>The Marquee',
'''<div class="wire"><div class="num">1</div><div><h3>North Tonawanda &middot; High School Threat Not Credible</h3><p>North Tonawanda police say a social media threat made by a North Tonawanda High School student is not credible, WIVB reports. The school district called police Friday about the "concerning" post.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Dunkirk &middot; Police Want Parents to Step In</h3><p>Dunkirk police answered seven incidents in the past month, from trespassing to robbery and assault, all involving kids 13 to 15, WKBW reports. Chief Douglas Swizer says parents need to be involved, and police are now charging some of them, WIVB reports.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Rochester &middot; A Flower on the Bridge</h3><p>Work began this week on "In Full Bloom," a nearly 25-foot metal sculpture of the city's five-petal mark on the downtown Sister Cities Bridge, WXXI reports. Its center will light up; the city says it will be finished in the coming weeks.</p></div></div>
''')

S('<div class="wire"><div class="num">1</div><div><h3>Patrick Stewart', '<h2 class="sec"><span class="o">&#127944;</span>The Gridiron',
'''<div class="wire"><div class="num">1</div><div><h3><i>General Hospital</i> Wins Again</h3><p><i>General Hospital</i> won best daytime drama at Friday night's Daytime Emmys, and its Genie Francis received the lifetime achievement award, the <i>Hollywood Reporter</i> reports. <i>Beyond the Gates</i> won four, including best actress for Tamara Tunie.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Harryween</h3><p>Harry Styles opened Friday's Madison Square Garden show dressed as Elvis, then changed into the outfit from his 2010 <i>X Factor</i> audition to sing "Isn't She Lovely," Billboard reports. It was night 29 of his 30-show residency.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>One Last Role for Eric Bauza</h3><p>Eric Bauza, the voice of Bugs Bunny who died Oct. 25, will make a posthumous debut on <i>The Simpsons</i>, playing two characters, Deadline reports. He had more than 400 credits.</p></div></div>
''')

S('<div class="touch-head">Allen and Jackson</div>', '<table class="tbl">',
'''<div class="touch-head">Game Day Eve</div>
<div class="line"><b>Bills</b> &middot; Buffalo's own Goo Goo Dolls will play the Bills' Thanksgiving halftime show, WIVB reports. First comes Baltimore, Sunday at 1:00 on standard time.</div>
<div class="line"><b>Jets</b> &middot; The Raiders started 3&ndash;0 and have lost four straight since. Sportradar makes the Jets a slight favorite at home Sunday, 53 percent.</div>
''')

S('<div class="touch-head">Martinsville Sunday</div>', '<h2 class="sec"><span class="o">&#9790;</span>On This Day',
'''<div class="touch-head">Martinsville Tomorrow</div>
<div class="line">Larson leads by 73 with two to go.</div>
''')

S('<div class="otd">', '<h2 class="sec"><span class="o">&#10023;</span>Question of the Day',
'''<div class="otd"><b>October 31, 1926</b> &mdash; Harry Houdini, the escape artist no handcuffs could hold, died in Detroit on Halloween, 100 years ago today.</div>
''')

S('<div class="qotd">', '<div class="dbl">',
'''<div class="qotd">Once a year, strangers in disguise ring your bell, and you pay them to go away. What night is it? <i>Answer below the fold.</i></div>
''')
R("<b>Question of the Day:</b> A bat.", "<b>Question of the Day:</b> Halloween. Happy trick-or-treating.")
S('<div class="s">Forecast per', '<div class="sig">',
'''<div class="s">Forecast per NWS Buffalo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; sky computed for 14120 &middot; foliage from the I LOVE NY report via the Dunkirk Observer &middot; election summary from the paper's election tracker &middot; headlines via CBS, BBC, NPR, WKBW, WIVB, WXXI, Hollywood Reporter, Billboard, Deadline &middot; scores and NASCAR points via Sportradar and Hendrick Motorsports</div>
''')

ed = {"date": "2026-10-31", "no": 129, "body_html": src, "plate_path": None,
      "plate_caption": "Happy Halloween",
      "headline": "Happy Halloween · Clocks fall back · Patriots for Ukraine · Game day eve"}
for p in ['/home/claude/edition-2026-10-31.json', '/home/claude/site/data/edition-2026-10-31.json']:
    json.dump(ed, open(p, 'w'), ensure_ascii=False, indent=1)
print('ok')
