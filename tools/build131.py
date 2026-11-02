import json, random
src = json.load(open('/home/claude/site/data/edition-2026-11-01.json'))['body_html']

def R(a, c, n=1):
    global src
    assert src.count(a) == n, ('R', a[:60], src.count(a))
    src = src.replace(a, c)

def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50])
    src = src[:i] + new + src[j:]

# ---- drawn cover: Election Eve ----
random.seed(1102)
W, H = 600, 320
p = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="An illustrated election eve: a brick schoolhouse polling place at dusk with a VOTE sign and bunting, glowing windows, bare trees, falling leaves and twinkling stars" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;height:auto">']
p.append('<defs><linearGradient id="esky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#1b2340"/><stop offset=".6" stop-color="#5a3b4a"/><stop offset="1" stop-color="#d98a3a"/></linearGradient>'
         '<radialGradient id="eglow"><stop offset="0" stop-color="#ffe39a" stop-opacity=".8"/><stop offset="1" stop-color="#ffd27a" stop-opacity="0"/></radialGradient></defs>')
p.append(f'<rect width="{W}" height="{H}" fill="url(#esky)"/>')
for _ in range(36):
    x, y = random.uniform(0, W), random.uniform(0, 140)
    r = random.uniform(.6, 1.5); d = random.uniform(1.8, 4.5); b = random.uniform(0, 4)
    p.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r:.1f}" fill="#fbf5e4"><animate attributeName="opacity" values="1;.25;1" dur="{d:.1f}s" begin="-{b:.1f}s" repeatCount="indefinite"/></circle>')
# ground
p.append(f'<path d="M0 262 Q150 248 300 258 T600 254 V{H} H0Z" fill="#24170c"/>')
# bare trees
for tx in (60, 540):
    p.append(f'<path d="M{tx} 260 L{tx+2} 175 M{tx+1} 205 L{tx+20} 186 M{tx+1} 192 L{tx-18} 176 M{tx+20} 186 L{tx+31} 179 M{tx-18} 176 L{tx-27} 168 M{tx+1} 220 L{tx-13} 208" stroke="#24170c" stroke-width="5" stroke-linecap="round" fill="none"/>')
# schoolhouse
p.append('<rect x="200" y="160" width="200" height="100" fill="#7a2e1a"/>')
p.append('<path d="M188 162 L300 108 L412 162Z" fill="#3a2716"/>')
p.append('<rect x="284" y="78" width="32" height="34" fill="#7a2e1a"/><path d="M278 80 L300 64 L322 80Z" fill="#3a2716"/>')
p.append('<path d="M300 64 V40" stroke="#3a2716" stroke-width="2"/>')
# flag on the cupola pole, waving
p.append('<g><path d="M300 41 h22 v13 h-22Z" fill="#c8302f"><animateTransform attributeName="transform" type="skewY" values="0;4;0;-3;0" dur="2.4s" repeatCount="indefinite"/></path>'
         '<path d="M300 45 h22 M300 50 h22" stroke="#fbf5e4" stroke-width="1.6"><animateTransform attributeName="transform" type="skewY" values="0;4;0;-3;0" dur="2.4s" repeatCount="indefinite"/></path>'
         '<rect x="300" y="41" width="9" height="7" fill="#1b2340"><animateTransform attributeName="transform" type="skewY" values="0;4;0;-3;0" dur="2.4s" repeatCount="indefinite"/></rect></g>')
# windows glowing
for wx in (218, 252, 334, 368):
    p.append(f'<circle cx="{wx+7}" cy="196" r="22" fill="url(#eglow)"><animate attributeName="opacity" values=".7;1;.8;.7" dur="3.1s" repeatCount="indefinite"/></circle>'
             f'<rect x="{wx}" y="182" width="14" height="28" fill="#ffd27a"/><path d="M{wx+7} 182 V210 M{wx} 196 H{wx+14}" stroke="#7a2e1a" stroke-width="1.5"/>')
# door
p.append('<rect x="287" y="212" width="26" height="48" fill="#3a2716"/><circle cx="307" cy="238" r="1.6" fill="#e8b100"/>')
# bunting
p.append('<path d="M204 166 Q252 186 300 166 Q348 186 396 166" stroke="#fbf5e4" stroke-width="1" fill="none"/>')
cols = ['#c8302f', '#fbf5e4', '#1b5e8a']
for i in range(10):
    t = (i + .5) / 10
    bx = 204 + 192 * t
    loc = t * 2 % 1
    by = 166 + 20 * 4 * loc * (1 - loc) * .5 + 2
    p.append(f'<path d="M{bx-5:.0f} {by:.0f} h10 l-5 9Z" fill="{cols[i % 3]}"/>')
# VOTE sign on a stake
p.append('<rect x="438" y="226" width="4" height="34" fill="#3a2716"/><rect x="416" y="206" width="48" height="22" rx="2" fill="#fbf5e4" stroke="#c8302f" stroke-width="2"/>'
         '<text x="440" y="222" text-anchor="middle" font-family="Archivo, Arial, sans-serif" font-weight="700" font-size="13" fill="#c8302f" letter-spacing="1.5">VOTE</text>')
# falling leaves
lc = ['#cf6f1a', '#9c3216', '#e8b100']
for i in range(10):
    x = random.uniform(10, 590); d = random.uniform(8, 14); b = random.uniform(0, 14); c = random.choice(lc)
    sway = random.uniform(15, 40) * random.choice([-1, 1])
    p.append(f'<g><animateTransform attributeName="transform" type="translate" values="{x:.0f},-10; {x+sway:.0f},150; {x:.0f},330" dur="{d:.1f}s" begin="-{b:.1f}s" repeatCount="indefinite"/>'
             f'<g><path d="M0 -6 C5 -3 5 3 0 6 C-5 3 -5 -3 0 -6Z" fill="{c}"/><animateTransform attributeName="transform" type="rotate" from="0" to="{random.choice([360,-360])}" dur="{d/2:.1f}s" repeatCount="indefinite"/></g></g>')
p.append('<text x="120" y="70" text-anchor="middle" font-family="PF, Georgia, serif" font-style="italic" font-size="20" fill="#e8b100">Tomorrow,</text>')
p.append('<text x="120" y="108" text-anchor="middle" font-family="PF, Georgia, serif" font-weight="800" font-size="34" fill="#fbf5e4">you decide</text>')
p.append('</svg>')
svg = ''.join(p)

R('No. 130', 'No. 131')
R('Sunday &middot; November 1 &middot; 2026', 'Monday &middot; November 2 &middot; 2026')
S('<div class="tiles">', '<div class="plate-wrap">', '''<div class="tiles">
  <div class="tile"><div class="v">68&deg;</div><div class="k">Partly Sunny</div></div>
  <div class="tile"><div class="v">5:06</div><div class="k">Sunset</div></div>
  <div class="tile urg"><div class="v">1</div><div class="k">Day to Election Day</div></div>
</div>
''')
S('<div class="plate-wrap">', '<div class="dbl-tight">', '''<div class="plate-wrap"><div class="frame"><span class="tick tl"></span><span class="tick tr"></span><span class="tick bl"></span><span class="tick br"></span>
''' + svg + '''</div>
<div class="plate-cap">Plate I &middot; The Family Album</div>
<div class="plate-sub">Election Eve</div></div>
''')

ballot = open('/home/claude/ballot131.html').read().replace('<b>1 days</b>', '<b>1 day</b>')

BODY = '''<h2 class="sec"><span class="o">&#9825;</span>Family Today<span class="o">&#9825;</span></h2>
<div class="fam"><b>Election Eve, and a Monday that feels like September</b>: 68 and partly sunny, with the Bills at 6&ndash;1 after Sunday's rout of Baltimore. Polls open at 6 tomorrow morning.
<div class="line" style="margin-top:.4rem"><span class="lbl t">The log</span> Days since the last migraine: Garret 4, Dad 27, Mom 4. None logged yet in November.</div>
<ul class="cal">
<li><span class="dt">Nov 3</span><span>Election Day, polls 6 a.m.&ndash;9 p.m.</span></li>
<li><span class="dt">Nov 8</span><span>Jets at Kansas City, 1:00 &middot; NASCAR's finale at Homestead</span></li>
<li><span class="dt">Nov 9</span><span>Bills at Minnesota, Monday night, 8:15</span></li>
</ul>
<div class="ask"><b>Send something to the paper:</b> a photo, a story, your Sunday answer or a date for the calendar, at <a href="https://tally.so/r/rjxDpl">tally.so/r/rjxDpl</a>. It runs the next morning under your name.<br><b>Had a migraine?</b> Log it at <a href="https://tally.so/r/obWNYP">tally.so/r/obWNYP</a>.</div></div>
<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass<span class="o">&#9788;</span></h2>
<div class="wx"><div class="bigtemp">68<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">Borrowed warmth: partly sunny and 68 today, 75 by Wednesday, then the rain comes</span>
Low <b>52&deg;</b> tonight &middot; light southwest wind<br>Rain showers Wednesday night and Thursday</div></div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">48<sup>&deg;</sup></div><div class="d">Clear &middot; high 68&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">57<sup>&deg;</sup></div><div class="d">Clear &middot; high 67&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">52<sup>&deg;</sup></div><div class="d">Clear &middot; high 71&deg;</div></div>
</div>
<div class="strip5">
  <div><div class="d">Mon</div><div class="i">&#9925;</div><div class="h">68</div><div class="w">partly sunny</div></div>
  <div><div class="d">Tue</div><div class="i">&#9925;</div><div class="h">71</div><div class="w">stray shower</div></div>
  <div><div class="d">Wed</div><div class="i">&#9728;</div><div class="h">75</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Thu</div><div class="i">&#127783;</div><div class="h">68</div><div class="w">rain showers</div></div>
  <div><div class="d">Fri</div><div class="i">&#127783;</div><div class="h">62</div><div class="w">chance of showers</div></div>
</div>
<div class="line"><span class="lbl t">Election Day</span> A slight chance of a shower, then partly sunny and 71 in North Tonawanda; 24 percent chance of rain. <span class="lbl t">Outdoor window</span> Today through Wednesday.</div>
<div class="line"><span class="lbl t">Frost watch</span> None this week: the coldest night in the forecast is 45, Friday night.</div>
<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky<span class="o">&#9790;</span></h2>
<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 0 50 96 A8.6 46 0 0 1 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>Waning crescent</b>, 41 percent lit, in Leo; rises at 12:43 a.m., sets at 2:01 p.m.<br>
<span class="lbl t">Sun</span> 6:51a &ndash; 5:06p &middot; <b>10h 15m</b>, 3 minutes less than yesterday<br>
<span class="lbl t">Tonight</span> Saturn in the southeast after dark; Mars and Jupiter rise near midnight, with the moon right beside them by 1 a.m.<br>
<span class="lbl t">New moon</span> Mon, Nov 9 &middot; <span class="lbl t">Beaver Moon</span> Tue, Nov 24</div></div>
<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>Neptune, in your sign, sextiles Pluto</b>. Small dreams, quietly planned. Write one down before bed. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>The moon meets Jupiter</b>. Generous mood. Pick up the tab, or at least the coffee. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>The moon meets Mars in your sign</b>. Energy to burn. Spend it on the yard while it's 68. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>Uranus sextiles Neptune</b>. An odd idea turns out to be the right one. Let it. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Venus sextiles Jupiter</b>, within a degree. Good company, good food, good Monday. Accept the invitation. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
<div style="font-family:'LOI';font-style:italic;font-size:.8rem;color:var(--soft);margin-top:.4rem">Positions computed for noon today at 14120. The sky is real; the readings are for fun.</div>
<h2 class="sec"><span class="o">&#10038;</span>The Ledger<span class="o">&#10038;</span></h2>
<div class="ledger"><div class="num"><div class="cap">Monroe County residents who voted early this year, a county record</div><div class="big">95,929</div></div>
<div class="txt">About 31,174 had by this point last year, Rochester First reports. Everyone else gets one more day: tomorrow.</div></div>
<h2 class="sec"><span class="o">&#10038;</span>The National Wire<span class="o">&#10038;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>Jet Crash in Palm Beach County</h3><p>A Learjet 60 flying from Austin, Texas, to the Bahamas nose-dived and crashed near homes in Palm Beach County, Florida, Sunday afternoon, killing all nine people aboard, CBS reports. No one on the ground was hurt, Gov. Ron DeSantis said; about 600 people were evacuated from around the site near a mobile home park, and the cause isn't known yet.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Sen. Chris Murphy Has a Stroke</h3><p>Connecticut Democrat Chris Murphy felt numbness in his arm at his son's hockey game Saturday and was found at a local hospital to have had a stroke, his chief of staff said Sunday, CBS reports. He was moved to Johns Hopkins for monitoring; he is awake, alert and responding well, and his office expects a full recovery.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>A Democrat Crosses Over in Michigan</h3><p>Democratic Rep. Haley Stevens, who narrowly lost August's Senate primary, endorsed Republican Mike Rogers for Michigan's open Senate seat on Sunday, CBS reports. She said the Democratic nominee, Abdul El-Sayed, had told her she was no longer welcome in his campaign; it's one of the races that could decide who controls the Senate.</p></div></div>
<h2 class="sec"><span class="o">&#9962;</span>The Home Wire<span class="o">&#9962;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>Greece &middot; Band Brings Home a State Title</h3><p>The Greece Blue Knights Marching Band came back from the state championships in Syracuse as champions, Rochester First reports. The band draws from all of Greece's secondary schools and last won a state title, in a lower class, in 2023.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Jamestown &middot; Jayhawks to Nationals</h3><p>Jamestown Community College's women's soccer team beat fifth-ranked Mohawk Valley 2&ndash;1 in Batavia Saturday to win the Region 3 title, the <i>Observer</i> reports. The win sends the Jayhawks to the national junior-college tournament.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Lockport &middot; Fatal House Fire</h3><p>One person died and another was hurt in a fire at a home on Park Avenue early Sunday, the <i>Niagara Gazette</i> reports. Firefighters were called at 3:37 a.m. for flames coming from the kitchen and a resident trapped inside; the cause is under investigation.</p></div></div>
''' + ballot + '''<h2 class="sec"><span class="o">&#9733;</span>The Marquee<span class="o">&#9733;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>The Black Parade Finally Tops the Chart</h3><p>My Chemical Romance has its first chart-topping album: <i>The Black Parade</i> jumped from 139th place to the top of the Billboard 200 after its 20th-anniversary deluxe reissue, Billboard reports. The 2006 album peaked at second place the first time around.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Wu-Tang at Halftime in Detroit</h3><p>Wu-Tang Clan will headline the halftime show when the Lions host the Bears on Thanksgiving, Nov. 26, on CBS, Billboard reports. Eminem and his manager, Paul Rosenberg, picked the act for the second straight year.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>A Sketch Becomes a Sitcom</h3><p>"The Smile Clinic," a digital short from <i>SNL Korea</i> that skewers Korea's cosmetic skin-care business, is being turned into a 10-episode half-hour sitcom, Deadline reports. It's the first spin-off ever from one of <i>Saturday Night Live</i>'s international versions.</p></div></div>
<h2 class="sec"><span class="o">&#127944;</span>The Gridiron<span class="o">&#127944;</span></h2>
<div class="touch-head">Monday Morning Quarterback</div>
<div class="line"><b>Bills 36, Ravens 10.</b> Lamar Jackson hurt his thumb on Baltimore's first offensive snap; he needs surgery and could miss the rest of the season, the Ravens' coach said. Buffalo led 16&ndash;7 at halftime and pulled away: Josh Allen ran for one touchdown and threw two, to D.J. Moore and Dalton Kincaid, and Tyler Bass kicked field goals of 56, 22 and 51 yards.</div>
<div class="line"><b>Got right:</b> the defense held Baltimore to 144 yards, with three takeaways and four sacks, and Allen's 11-yard touchdown to Moore was his 259th, playoffs included, a Bills record, WIVB reports. <b>To fix:</b> 10 penalties for 87 yards and two turnovers. The Bills are 6&ndash;1; they play at Minnesota on Monday night, Nov. 9.</div>
<div class="line"><b>Raiders 38, Jets 33.</b> A shootout the Jets led 30&ndash;28 after three quarters. Las Vegas won the fourth quarter 10&ndash;3; Kirk Cousins threw three touchdown passes on the day, two to Brock Bowers, and ran for another, and a 53-yard field goal with 31 seconds left sealed it.</div>
<div class="line"><b>Got right:</b> 439 yards of offense; Geno Smith threw for 290 yards and touchdowns to I. Williams and A. Mitchell, B. Allen ran 21 yards for another, and Sanders made all four field goals. <b>To fix:</b> a 95-yard kickoff return for a touchdown came right after one of the Jets' scores, and Smith threw an interception. The Jets are 2&ndash;6; they visit Kansas City Sunday at 1:00.</div>
<table class="tbl"><tr><th>AFC East</th><th class="n">W</th><th class="n">L</th><th class="n">PCT</th></tr>
<tr><td style="color:var(--red)">Buffalo</td><td class="n">6</td><td class="n">1</td><td class="n">.857</td></tr>
<tr><td>New England</td><td class="n">5</td><td class="n">3</td><td class="n">.625</td></tr>
<tr><td style="color:var(--red)">N.Y. Jets</td><td class="n">2</td><td class="n">6</td><td class="n">.250</td></tr>
<tr><td>Miami</td><td class="n">1</td><td class="n">6</td><td class="n">.143</td></tr></table>
<div class="line"><b>Around the league.</b> Detroit beat Minnesota 19&ndash;15, so no team is unbeaten. Denver beat Kansas City 28&ndash;24, Arizona beat Dallas 33&ndash;30, and Tampa Bay beat Atlanta 16&ndash;0 without completing a pass, the BBC notes. New England won 24&ndash;19 at Miami. Chicago plays at Seattle tonight.</div>
<div class="line"><b>The AI Editor, graded.</b> Bills 11&ndash;6: 6&ndash;1, ahead of pace. Jets 6&ndash;11: 2&ndash;6, behind it. Ravens over Rams in the Super Bowl: both are 4&ndash;4 after the Rams beat the Chargers 24&ndash;9, and Baltimore may be without Jackson for the season. That pick is in trouble.</div>
<h2 class="sec"><span class="o">&#9873;</span>The Chase<span class="o">&#9873;</span></h2>
<div class="touch-head">One Race Left</div>
<div class="line">William Byron won at Martinsville. Kyle Larson takes a 67-point lead over Christopher Bell, and 70 over Denny Hamlin, to the finale at Homestead on Sunday.</div>
<h2 class="sec"><span class="o">&#9790;</span>On This Day<span class="o">&#9790;</span></h2>
<div class="otd"><b>November 2, 1920</b> &mdash; Pittsburgh's KDKA read the Harding&ndash;Cox presidential election returns over the air, the first broadcast by a licensed commercial radio station.</div>
<h2 class="sec"><span class="o">&#10023;</span>Question of the Day<span class="o">&#10023;</span></h2>
<div class="qotd">I'm cast but never thrown, counted but never spent, and secret until the day I'm tallied. What am I? <i>Answer below the fold.</i></div>
'''
S('<h2 class="sec"><span class="o">&#9825;</span>Family Today', '<div class="dbl"><div class="a"></div><div class="b"></div></div>\n<div class="colo">', BODY)
R("<b>Question of the Day:</b> The Thanksgiving turkey.", "<b>Question of the Day:</b> A ballot.")
S('<div class="s">Forecast per', '<div class="sig">',
'''<div class="s">Forecast per NWS Buffalo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; sky computed for 14120 &middot; family counts from the paper's migraine log &middot; election box from the paper's election tracker &middot; headlines via CBS, BBC, WIVB, Rochester First, Niagara Gazette, the Dunkirk Observer, Billboard, Deadline &middot; scores via Sportradar &middot; NASCAR points via Yahoo Sports</div>
''')

ed = {"date": "2026-11-02", "no": 131, "body_html": src, "plate_path": None,
      "plate_caption": "Election Eve",
      "headline": "Bills rout Baltimore · Election Eve · Jet crash in Palm Beach · One race left"}
for f in ['/home/claude/edition-2026-11-02.json', '/home/claude/site/data/edition-2026-11-02.json']:
    json.dump(ed, open(f, 'w'), ensure_ascii=False, indent=1)
print('ok', len(svg))
