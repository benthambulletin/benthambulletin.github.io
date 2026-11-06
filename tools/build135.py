import json, random
src = json.load(open('/home/claude/site/data/edition-2026-11-05.json'))['body_html']

def R(a, c, n=1):
    global src
    assert src.count(a) == n, ('R', a[:60], src.count(a))
    src = src.replace(a, c)

def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50])
    src = src[:i] + new + src[j:]

# ---- drawn cover: a rainy Friday, an umbrella on the porch steps ----
random.seed(1106)
W, H = 600, 320
p = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="An illustrated rainy Friday: rain streaking down past a porch light, an open red umbrella on the steps, ripples in a puddle and wet leaves on the walk" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;height:auto">']
p.append('<defs><linearGradient id="rsky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#5d6672"/><stop offset="1" stop-color="#9aa1a6"/></linearGradient>'
         '<radialGradient id="rglow"><stop offset="0" stop-color="#ffe39a" stop-opacity=".85"/><stop offset="1" stop-color="#ffd27a" stop-opacity="0"/></radialGradient></defs>')
p.append(f'<rect width="{W}" height="{H}" fill="url(#rsky)"/>')
# house wall and porch
p.append('<rect x="330" y="40" width="270" height="200" fill="#7a4a24"/>')
for y in range(52, 240, 14):
    p.append(f'<path d="M330 {y} H600" stroke="#5a3418" stroke-width="1.2"/>')
p.append('<rect x="420" y="110" width="58" height="130" fill="#3a2716"/><circle cx="470" cy="178" r="2.5" fill="#e8b100"/>')
p.append('<circle cx="510" cy="118" r="44" fill="url(#rglow)"><animate attributeName="opacity" values=".8;1;.85;.8" dur="4s" repeatCount="indefinite"/></circle><rect x="503" y="106" width="14" height="22" rx="3" fill="#ffe39a" stroke="#24170c" stroke-width="2"/>')
p.append('<rect x="320" y="240" width="280" height="14" fill="#5a3418"/><rect x="340" y="254" width="260" height="14" fill="#4a2c14"/><rect x="360" y="268" width="240" height="14" fill="#3a2716"/>')
# ground and walk
p.append(f'<rect x="0" y="282" width="{W}" height="38" fill="#2f5e3e"/><path d="M0 282 H600" stroke="#24170c" stroke-width="2"/>')
# puddle ripples
p.append('<ellipse cx="170" cy="300" rx="90" ry="10" fill="#7d8890" opacity=".7"/>')
for i, (cx, d) in enumerate(((130, 2.2), (200, 2.8), (165, 3.4))):
    p.append(f'<ellipse cx="{cx}" cy="300" rx="2" ry=".6" fill="none" stroke="#e8edf0" stroke-width="1.2"><animate attributeName="rx" values="2;26" dur="{d}s" begin="-{i*.8:.1f}s" repeatCount="indefinite"/><animate attributeName="ry" values=".6;5" dur="{d}s" begin="-{i*.8:.1f}s" repeatCount="indefinite"/><animate attributeName="opacity" values="1;0" dur="{d}s" begin="-{i*.8:.1f}s" repeatCount="indefinite"/></ellipse>')
# umbrella on the steps
p.append('<g transform="translate(400 232) rotate(-18)"><path d="M-46 0 Q-46 -40 0 -44 Q46 -40 46 0 Q34 -8 23 0 Q12 -8 0 0 Q-12 -8 -23 0 Q-34 -8 -46 0Z" fill="#c8302f" stroke="#7a1f1a" stroke-width="2"/>'
         '<path d="M0 -44 V0 M-23 0 Q-20 -30 0 -44 M23 0 Q20 -30 0 -44" stroke="#7a1f1a" stroke-width="1.4" fill="none"/><path d="M0 0 V22 Q0 30 -8 28" stroke="#24170c" stroke-width="3" fill="none"/></g>')
# wet leaves on the walk
for x, y, c, r in ((60, 292, '#cf6f1a', 20), (110, 310, '#9c3216', -35), (250, 296, '#e8b100', 50), (300, 312, '#cf6f1a', -10)):
    p.append(f'<path transform="translate({x} {y}) rotate({r})" d="M0 -6 C5 -3 5 3 0 6 C-5 3 -5 -3 0 -6Z" fill="{c}"/>')
# rain
for _ in range(70):
    x = random.uniform(-40, 600); d = random.uniform(.6, 1.1); b = random.uniform(0, 1.2); l = random.uniform(10, 18)
    p.append(f'<path d="M{x:.0f} -20 l-4 {l:.0f}" stroke="#e8edf0" stroke-width="1.3" opacity=".7"><animateTransform attributeName="transform" type="translate" values="0,0; -36,340" dur="{d:.2f}s" begin="-{b:.2f}s" repeatCount="indefinite"/></path>')
p.append('<text x="150" y="96" text-anchor="middle" font-family="PF, Georgia, serif" font-style="italic" font-size="20" fill="#fbf5e4">a rainy</text>')
p.append('<text x="150" y="140" text-anchor="middle" font-family="PF, Georgia, serif" font-weight="800" font-size="44" fill="#fbf5e4">Friday</text>')
p.append('</svg>')
svg = ''.join(p)

R('No. 134', 'No. 135')
R('Thursday &middot; November 5 &middot; 2026', 'Friday &middot; November 6 &middot; 2026')
S('<div class="tiles">', '<div class="plate-wrap">', '''<div class="tiles">
  <div class="tile"><div class="v">56&deg;</div><div class="k">Rain Showers</div></div>
  <div class="tile"><div class="v">5:01</div><div class="k">Sunset</div></div>
  <div class="tile urg"><div class="v">$4.06</div><div class="k">Gas, a gallon</div></div>
</div>
''')
S('<div class="plate-wrap">', '<div class="dbl-tight">', '''<div class="plate-wrap"><div class="frame"><span class="tick tl"></span><span class="tick tr"></span><span class="tick bl"></span><span class="tick br"></span>
''' + svg + '''</div>
<div class="plate-cap">Plate I &middot; The Family Album</div>
<div class="plate-sub">A rainy Friday</div></div>
''')

BODY = '''<h2 class="sec"><span class="o">&#9825;</span>Family Today<span class="o">&#9825;</span></h2>
<div class="fam"><b>Umbrella Friday</b>: rain showers and 56 today, more rain Saturday, then a sunny, breezy Sunday for the Jets in Kansas City and NASCAR's last race.
<div class="line" style="margin-top:.4rem"><span class="lbl t">The log</span> Days since the last migraine: Garret 3, Dad 31, Mom 8. November so far: Garret one.</div>
<ul class="cal">
<li><span class="dt">Nov 8</span><span>Jets at Kansas City, 1:00 &middot; NASCAR's finale at Homestead</span></li>
<li><span class="dt">Nov 9</span><span>Bills at Minnesota, Monday night, 8:15</span></li>
</ul>
<div class="ask"><b>Send something to the paper:</b> a photo, a story, your Sunday answer or a date for the calendar, at <a href="https://tally.so/r/rjxDpl">tally.so/r/rjxDpl</a>. It runs the next morning under your name.<br><b>Had a migraine?</b> Log it at <a href="https://tally.so/r/obWNYP">tally.so/r/obWNYP</a>.</div></div>
<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass<span class="o">&#9788;</span></h2>
<div class="wx"><div class="bigtemp">56<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">A wet, gray Friday: rain showers and 56, and a damp start to the weekend</span>
Low <b>38&deg;</b> tonight &middot; showers likely, 60%<br>Rain today, 80%; light west wind</div></div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">54<sup>&deg;</sup></div><div class="d">Light rain, fog &middot; high 56&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">55<sup>&deg;</sup></div><div class="d">Light rain &middot; high 55&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">50<sup>&deg;</sup></div><div class="d">Clear &middot; high 61&deg;</div></div>
</div>
<div class="strip5">
  <div><div class="d">Fri</div><div class="i">&#127783;</div><div class="h">56</div><div class="w">rain showers</div></div>
  <div><div class="d">Sat</div><div class="i">&#127783;</div><div class="h">53</div><div class="w">showers likely</div></div>
  <div><div class="d">Sun</div><div class="i">&#9728;</div><div class="h">56</div><div class="w">sunny, gusty</div></div>
  <div><div class="d">Mon</div><div class="i">&#9925;</div><div class="h">56</div><div class="w">partly sunny</div></div>
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">60</div><div class="w">mostly sunny</div></div>
</div>
<div class="line"><span class="lbl t">Outdoor window</span> Sunday morning, before a slight chance of showers after 1 and gusts to 33; Tuesday looks best.</div>
<div class="line"><span class="lbl t">Frost watch</span> Not this week: 36 tonight in Dunkirk and Tuesday night in Scottsville, 37 in North Tonawanda Tuesday night.</div>
<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky<span class="o">&#9790;</span></h2>
<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 0 50 96 A39.6 46 0 0 1 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>A sliver of a moon</b>, 7 percent lit, in Virgo; rose at 4:12 a.m., sets at 3:26 p.m.<br>
<span class="lbl t">Sun</span> 6:56a &ndash; 5:01p &middot; <b>10h 5m</b><br>
<span class="lbl t">Sunset</span> 5:00 on the dot tomorrow; from Sunday it comes before 5 p.m. until Jan. 10.<br>
<span class="lbl t">New moon</span> Mon, Nov 9 &middot; <span class="lbl t">Beaver Moon</span> Tue, Nov 24</div></div>
<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>Neptune, in your sign, sextiles Pluto</b>. A quiet plan beats a loud one. Draft it this weekend. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>Venus sextiles Jupiter</b>. Rainy-day comfort food is the correct call. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Venus sextiles Mars in your sign</b>. Flirt with a new project. No commitments till Monday. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>Uranus trines Pluto</b>. Rearrange one room. You'll wonder why you waited. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Uranus sextiles Neptune</b>. Birthday month nearly done; one more good story to tell. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
<div style="font-family:'LOI';font-style:italic;font-size:.8rem;color:var(--soft);margin-top:.4rem">Positions computed for noon today at 14120. The sky is real; the readings are for fun.</div>
<h2 class="sec"><span class="o">&#10038;</span>The Ledger<span class="o">&#10038;</span></h2>
<div class="ledger"><div class="num"><div class="cap">The national average for a gallon of gas, per GasBuddy</div><div class="big">$4.06</div></div>
<div class="txt">GasBuddy's Patrick De Haan expects it to dip under $4 by next week for the first time since July, CBS reports, and diesel under $6 by Thanksgiving.</div></div>
<h2 class="sec"><span class="o">&#10038;</span>The National Wire<span class="o">&#10038;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>Tech Stocks Tumble</h3><p>The tech-heavy Nasdaq index fell 5.5 percent Thursday and the slide spread to Asia and Europe on Friday, the BBC reports, wiping trillions of dollars off big tech companies. Investors fear a Democratic Congress and the states will rein in artificial intelligence and the huge data centers it runs on; NPR puts the U.S. loss at $2 trillion.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Judge Pauses Trump's Arch</h3><p>A federal judge in Washington blocked construction of President Trump's proposed 250-foot triumphal arch for 14 days, late Thursday, siding for now with a group of Vietnam veterans, the District of Columbia and Virginia, CBS reports. Judge Tanya Chutkan wrote that they are likely to show the government didn't follow required legal steps.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>California Empties Death Row</h3><p>Gov. Gavin Newsom says he will commute all 548 death sentences in California to life without parole, CBS reports. The death penalty itself stays on the books, so prosecutors could still seek it in new cases.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>Los Angeles Changes Mayors</h3><p>City Councilmember Nithya Raman beat Mayor Karen Bass in Los Angeles, CBS News projects. Raman, whom the BBC calls a democratic socialist, pledged to restore Angelenos' "faith in City Hall."</p></div></div>
<h2 class="sec"><span class="o">&#9962;</span>The Home Wire<span class="o">&#9962;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Four New Hall of Fame Toys</h3><p>The slide, the Pok&eacute;mon Trading Card Game, the Care Bears and Bingo were inducted into the National Toy Hall of Fame at Rochester's Strong National Museum of Play on Thursday, Rochester First reports. They were chosen from 12 finalists, WXXI reports.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Pomfret &middot; Recycling Yard Approved</h3><p>Pomfret's zoning appeals board granted Steve St. George a special-use permit for a concrete and asphalt recycling yard at his property, with a list of conditions attached, the <i>Observer</i> reports. The approval came at the board's third hearing, Oct. 6.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Fredonia &middot; Students Rake the Village</h3><p>Hundreds of SUNY Fredonia students fan out across the village Saturday from about noon for the annual Fall Sweep, helping residents with yard cleanup and leaves, the <i>Observer</i> reports. It's one of the college's biggest volunteer days.</p></div></div>
<h2 class="sec"><span class="o">&#9733;</span>The Marquee</h2>
'''
BODY = BODY.replace('The Marquee</h2>', 'The Marquee<span class="o">&#9733;</span></h2>') + '''<div class="wire"><div class="num">1</div><div><h3>Godzilla Stomps In</h3><p><i>Godzilla Minus Zero</i>, Takashi Yamazaki's R-rated follow-up, took in about $6 million in previews before its opening day, Deadline reports. That's ahead of what <i>Predator: Badlands</i> did in previews.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3><i>Back to Black</i> Is Back</h3><p>Amy Winehouse's <i>Back to Black</i> returned to the top 10 of four Billboard charts after its 20th-anniversary reissue, including album sales and vinyl, Billboard reports. It also re-entered the all-genre Billboard 200 in 42nd place.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Adam Driver Is Done With <i>Star Wars</i></h3><p>"The ship has sailed," Adam Driver said of playing Kylo Ren again, the <i>Hollywood Reporter</i> reports: "No more <i>Star Wars</i>." He said a proposed film about the character was turned down because, as he put it, "he's dead."</p></div></div>
<h2 class="sec"><span class="o">&#127944;</span>The Gridiron<span class="o">&#127944;</span></h2>
<div class="touch-head">Jaguars Roll in Baltimore</div>
<div class="line"><b>Thursday night.</b> Jacksonville 33, Baltimore 10. Trevor Lawrence threw a 50-yard touchdown pass, Cam Little kicked four field goals, and the Ravens' passers threw two interceptions; Baltimore fell to 4&ndash;5.</div>
<div class="line"><b>Bills</b> &middot; At Minnesota Monday night, 8:15.</div>
<div class="line"><b>Jets</b> &middot; At Kansas City Sunday, 1:00.</div>
<table class="tbl"><tr><th>AFC East</th><th class="n">W</th><th class="n">L</th><th class="n">PCT</th></tr>
<tr><td style="color:var(--red)">Buffalo</td><td class="n">6</td><td class="n">1</td><td class="n">.857</td></tr>
<tr><td>New England</td><td class="n">5</td><td class="n">3</td><td class="n">.625</td></tr>
<tr><td style="color:var(--red)">N.Y. Jets</td><td class="n">2</td><td class="n">6</td><td class="n">.250</td></tr>
<tr><td>Miami</td><td class="n">1</td><td class="n">6</td><td class="n">.143</td></tr></table>
<h2 class="sec"><span class="o">&#9873;</span>The Chase<span class="o">&#9873;</span></h2>
<div class="line">Sunday at Homestead decides it. Larson leads Bell by 67 and Hamlin by 70.</div>
<h2 class="sec"><span class="o">&#9790;</span>On This Day<span class="o">&#9790;</span></h2>
<div class="otd"><b>November 6, 1860</b> &mdash; Abraham Lincoln was elected the 16th president, winning without carrying a single Southern state.</div>
<h2 class="sec"><span class="o">&#10023;</span>Question of the Day<span class="o">&#10023;</span></h2>
<div class="qotd">I open when it pours and close when it clears, and every lost-and-found has a few of me. What am I? <i>Answer below the fold.</i></div>
'''
S('<h2 class="sec"><span class="o">&#9825;</span>Family Today', '<div class="dbl"><div class="a"></div><div class="b"></div></div>\n<div class="colo">', BODY)
R("<b>Question of the Day:</b> A skeleton. See Plate I.", "<b>Question of the Day:</b> An umbrella.")
S('<div class="s">Forecast per', '<div class="sig">',
'''<div class="s">Forecast per NWS Buffalo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; sky computed for 14120 &middot; family counts from the paper's migraine log &middot; headlines via BBC, CBS, NPR, Rochester First, WXXI, the Dunkirk <i>Observer</i>, Deadline, Billboard, the <i>Hollywood Reporter</i> &middot; scores via Sportradar</div>
''')

ed = {"date": "2026-11-06", "no": 135, "body_html": src, "plate_path": None,
      "plate_caption": "A rainy Friday",
      "headline": "Tech stocks tumble · Judge pauses the arch · Four new Hall of Fame toys"}
for f in ['/home/claude/edition-2026-11-06.json', '/home/claude/site/data/edition-2026-11-06.json']:
    json.dump(ed, open(f, 'w'), ensure_ascii=False, indent=1)
print('ok', len(svg))
