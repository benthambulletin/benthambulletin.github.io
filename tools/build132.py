import json, random
src = json.load(open('/home/claude/site/data/edition-2026-11-02.json'))['body_html']

def R(a, c, n=1):
    global src
    assert src.count(a) == n, ('R', a[:60], src.count(a))
    src = src.replace(a, c)

def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50])
    src = src[:i] + new + src[j:]

# ---- drawn cover: Election Day, ballots into the box on a warm morning ----
random.seed(1103)
W, H = 600, 320
p = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="An illustrated Election Day morning: paper ballots drifting down into a wooden ballot box under a warm sun, with autumn leaves falling" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;height:auto">']
p.append('<defs><linearGradient id="dsky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9cc3cf"/><stop offset=".7" stop-color="#f3dcae"/><stop offset="1" stop-color="#f0c98a"/></linearGradient>'
         '<radialGradient id="dsun"><stop offset="0" stop-color="#fff2c4"/><stop offset=".45" stop-color="#ffd27a" stop-opacity=".9"/><stop offset="1" stop-color="#ffd27a" stop-opacity="0"/></radialGradient></defs>')
p.append(f'<rect width="{W}" height="{H}" fill="url(#dsky)"/>')
p.append('<circle cx="500" cy="70" r="70" fill="url(#dsun)"><animate attributeName="r" values="66;74;66" dur="5s" repeatCount="indefinite"/></circle><circle cx="500" cy="70" r="24" fill="#ffe39a"/>')
# soft clouds drifting
for cx, cy, d, b in ((120, 60, 40, 0), (330, 40, 55, 20)):
    p.append(f'<g opacity=".85"><animateTransform attributeName="transform" type="translate" values="-40,0; 60,0; -40,0" dur="{d}s" begin="-{b}s" repeatCount="indefinite"/>'
             f'<ellipse cx="{cx}" cy="{cy}" rx="38" ry="12" fill="#fbf5e4"/><ellipse cx="{cx+18}" cy="{cy-8}" rx="22" ry="12" fill="#fbf5e4"/></g>')
# rolling ground and maples
p.append(f'<path d="M0 250 Q160 232 320 246 T600 240 V{H} H0Z" fill="#2f5e3e"/>')
for tx, c in ((70, '#cf6f1a'), (540, '#9c3216')):
    p.append(f'<rect x="{tx-4}" y="200" width="8" height="48" fill="#3a2716"/><circle cx="{tx}" cy="190" r="30" fill="{c}"/><circle cx="{tx-18}" cy="204" r="18" fill="{c}"/><circle cx="{tx+18}" cy="204" r="18" fill="{c}"/>')
# ballot box
p.append('<rect x="235" y="170" width="130" height="92" rx="3" fill="#7a4a24" stroke="#3a2716" stroke-width="3"/>')
p.append('<rect x="225" y="160" width="150" height="16" rx="2" fill="#5a3418" stroke="#3a2716" stroke-width="3"/>')
p.append('<rect x="272" y="165" width="56" height="5" rx="2" fill="#24170c"/>')
p.append('<rect x="262" y="198" width="76" height="34" rx="2" fill="#fbf5e4" stroke="#c8302f" stroke-width="2"/>')
p.append('<text x="300" y="221" text-anchor="middle" font-family="Archivo, Arial, sans-serif" font-weight="700" font-size="15" fill="#c8302f" letter-spacing="2">VOTE</text>')
# ballots drifting into the slot
for i in range(5):
    d = 4.5 + i * .4; b = i * 1.0; x0 = 300 + random.uniform(-90, 90)
    p.append(f'<g><animateTransform attributeName="transform" type="translate" values="{x0:.0f},-20; {(x0+300)/2:.0f},70; 300,158" keyTimes="0;.55;1" dur="{d:.1f}s" begin="-{b:.1f}s" repeatCount="indefinite"/>'
             f'<g><rect x="-11" y="-14" width="22" height="28" fill="#fbf5e4" stroke="#24170c" stroke-width="1"/><path d="M-6 -7 h12 M-6 -1 h12 M-6 5 h8" stroke="#24170c" stroke-width="1"/><path d="M-8 -8 l2 2 l3 -4" stroke="#c8302f" stroke-width="1.6" fill="none"/>'
             f'<animateTransform attributeName="transform" type="rotate" values="-25;15;0" dur="{d:.1f}s" begin="-{b:.1f}s" repeatCount="indefinite"/></g>'
             f'<animate attributeName="opacity" values="1;1;0" keyTimes="0;.92;1" dur="{d:.1f}s" begin="-{b:.1f}s" repeatCount="indefinite"/></g>')
lc = ['#cf6f1a', '#9c3216', '#e8b100']
for i in range(9):
    x = random.uniform(10, 590); d = random.uniform(8, 14); b = random.uniform(0, 14); c = random.choice(lc)
    sway = random.uniform(15, 40) * random.choice([-1, 1])
    p.append(f'<g><animateTransform attributeName="transform" type="translate" values="{x:.0f},-10; {x+sway:.0f},150; {x:.0f},330" dur="{d:.1f}s" begin="-{b:.1f}s" repeatCount="indefinite"/>'
             f'<g><path d="M0 -6 C5 -3 5 3 0 6 C-5 3 -5 -3 0 -6Z" fill="{c}"/><animateTransform attributeName="transform" type="rotate" from="0" to="{random.choice([360,-360])}" dur="{d/2:.1f}s" repeatCount="indefinite"/></g></g>')
p.append('<text x="130" y="112" text-anchor="middle" font-family="PF, Georgia, serif" font-weight="800" font-size="34" fill="#24170c">Election Day</text>')
p.append('<text x="130" y="140" text-anchor="middle" font-family="PF, Georgia, serif" font-style="italic" font-size="18" fill="#9c3216">polls open 6 to 9</text>')
p.append('</svg>')
svg = ''.join(p)

R('No. 131', 'No. 132')
R('Monday &middot; November 2 &middot; 2026', 'Tuesday &middot; November 3 &middot; 2026')
S('<div class="tiles">', '<div class="plate-wrap">', '''<div class="tiles">
  <div class="tile"><div class="v">72&deg;</div><div class="k">Partly Sunny</div></div>
  <div class="tile"><div class="v">5:05</div><div class="k">Sunset</div></div>
  <div class="tile urg"><div class="v">Today</div><div class="k">Election Day</div></div>
</div>
''')
S('<div class="plate-wrap">', '<div class="dbl-tight">', '''<div class="plate-wrap"><div class="frame"><span class="tick tl"></span><span class="tick tr"></span><span class="tick bl"></span><span class="tick br"></span>
''' + svg + '''</div>
<div class="plate-cap">Plate I &middot; The Family Album</div>
<div class="plate-sub">Election Day</div></div>
''')

ballot = open('/home/claude/ballot132.html').read().replace('<b>0 days</b> to Election Day', '<b>Today</b> is Election Day')

BODY = '''<h2 class="sec"><span class="o">&#9825;</span>Family Today<span class="o">&#9825;</span></h2>
<div class="fam"><b>Election Day</b>: polls are open 6 a.m. to 9 p.m., and it's a warm one to stand in line, 72 by afternoon. Results run in tomorrow's paper.
<div class="line" style="margin-top:.4rem"><span class="lbl t">The log</span> Days since the last migraine: Garret 5, Dad 28, Mom 5. None logged yet in November.</div>
<ul class="cal">
<li><span class="dt">Nov 8</span><span>Jets at Kansas City, 1:00 &middot; NASCAR's finale at Homestead</span></li>
<li><span class="dt">Nov 9</span><span>Bills at Minnesota, Monday night, 8:15</span></li>
</ul>
<div class="ask"><b>Send something to the paper:</b> a photo, a story, your Sunday answer or a date for the calendar, at <a href="https://tally.so/r/rjxDpl">tally.so/r/rjxDpl</a>. It runs the next morning under your name.<br><b>Had a migraine?</b> Log it at <a href="https://tally.so/r/obWNYP">tally.so/r/obWNYP</a>.</div></div>
<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass<span class="o">&#9788;</span></h2>
<div class="wx"><div class="bigtemp">72<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">Shirtsleeves on Election Day: a stray early shower, then partly sunny and 72</span>
Low <b>57&deg;</b> tonight &middot; south wind<br>Gusts to 24 today; rain Wednesday night into Thursday</div></div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">59<sup>&deg;</sup></div><div class="d">Cloudy &middot; high 72&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">59<sup>&deg;</sup></div><div class="d">Light rain, mist &middot; high 73&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">57<sup>&deg;</sup></div><div class="d">Cloudy &middot; high 73&deg;</div></div>
</div>
<div class="strip5">
  <div><div class="d">Tue</div><div class="i">&#9925;</div><div class="h">72</div><div class="w">partly sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#9728;</div><div class="h">76</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Thu</div><div class="i">&#127783;</div><div class="h">66</div><div class="w">morning rain</div></div>
  <div><div class="d">Fri</div><div class="i">&#9729;</div><div class="h">63</div><div class="w">chance of showers</div></div>
  <div><div class="d">Sat</div><div class="i">&#9729;</div><div class="h">56</div><div class="w">chance of showers</div></div>
</div>
<div class="line"><span class="lbl t">Polls</span> A slight chance of a shower before 9 a.m., then partly sunny; 20 percent chance of rain. <span class="lbl t">Outdoor window</span> Today and Wednesday, before the rain arrives after 7 p.m.</div>
<div class="line"><span class="lbl t">Frost watch</span> Not yet: the forecast bottoms out at 40, Saturday night, as the warm spell ends.</div>
<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky<span class="o">&#9790;</span></h2>
<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 0 50 96 A18.4 46 0 0 1 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>Waning crescent</b>, 30 percent lit, in Leo; sets at 2:25 p.m., rises again at 1:54 a.m. Wednesday.<br>
<span class="lbl t">Sun</span> 6:52a &ndash; 5:05p &middot; <b>10h 13m</b><br>
<span class="lbl t">Late tonight</span> Mars and Jupiter climb the eastern sky after midnight; the crescent follows at 1:54.<br>
<span class="lbl t">New moon</span> Mon, Nov 9 &middot; <span class="lbl t">Beaver Moon</span> Tue, Nov 24</div></div>
<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>Uranus sextiles Neptune in your sign</b>. Do the thing you've meant to do since spring. Today counts. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>Uranus trines Pluto</b>. Old habits, new line. Vote early in the day and enjoy the afternoon. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Venus sextiles Jupiter in your sign</b>. Warm day, warm crowd. Say hello to the poll workers. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>The moon squares Uranus</b>. A surprise in the schedule. Leave a little slack. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>The sun meets Mercury in your sign</b>. Say what you mean, once. Then let the count be the count. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
<div style="font-family:'LOI';font-style:italic;font-size:.8rem;color:var(--soft);margin-top:.4rem">Positions computed for noon today at 14120. The sky is real; the readings are for fun.</div>
<h2 class="sec"><span class="o">&#10038;</span>The Ledger<span class="o">&#10038;</span></h2>
<div class="ledger"><div class="num"><div class="cap">Raised in two months by the 6 percent surcharge at the Bills' new stadium</div><div class="big">$2.88M</div></div>
<div class="txt">September alone brought in $1.8 million, WKBW reports. The money goes to Erie County for future stadium upgrades and repairs.</div></div>
<h2 class="sec"><span class="o">&#10038;</span>The National Wire<span class="o">&#10038;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>U.S. Strikes an Iranian Island</h3><p>The U.S. struck Iran's Qeshm Island in the Strait of Hormuz, the narrow channel out of the Persian Gulf, after Iran's Revolutionary Guard fired on a U.S. aircraft, U.S. officials told CBS; they called the strikes limited and defensive. Iran's Guard said it shot down three U.S. drones, the BBC reports, as mediators work to keep the war that began in February from flaring again after today's vote.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Ukraine: 29 Dead at an Aid Site</h3><p>A Russian attack on a site where people had gathered for humanitarian aid in Ukraine's southern Zaporizhzhia region killed 29, with 48 still missing, NPR reports. Officials say at least nine 3,000-kilogram bombs hit the village, the BBC reports, and overnight strikes also hit power plants and hospitals across the country.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Court Won't Stop California's Count</h3><p>The Supreme Court on Monday turned down the Trump administration's request to order California election officials to set aside mail ballots from 20,000 people it alleges are not citizens, CBS reports. The administration had filed the request earlier the same day.</p></div></div>
<h2 class="sec"><span class="o">&#9962;</span>The Home Wire<span class="o">&#9962;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Veterans Day Parade Saturday</h3><p>Monroe County's fifth annual Veterans Day Parade steps off at 10:30 a.m. Saturday from South Goodman Street and Highland Avenue and ends with a ceremony at the Vietnam veterans memorial in Gary Beikirch Park, WXXI reports. Marching bands, veterans' groups and active-duty service members will march; State Senate Minority Leader Robert Ortt, a North Tonawanda Republican and Army National Guard veteran, is grand marshal.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Dunkirk &middot; $21 Million for the Schools</h3><p>The Dunkirk City School District awarded 24 bids worth more than $21 million for what the superintendent calls "the biggest phase" of its building project, the <i>Observer</i> reports. It covers a renovated cafeteria and kitchen at the middle and high school, a refurbished football field, track and tennis courts with new scoreboards, and air conditioning in classrooms.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Tonawanda &middot; Flood Loans Open</h3><p>The U.S. Small Business Administration has opened an office at the Ellwood Volunteer Firehouse in the Town of Tonawanda to help people hit by September's flash flooding apply for low-interest disaster loans, WKBW reports. Homeowners, renters, nonprofits and small businesses can apply, with rates starting at 3 percent.</p></div></div>
''' + ballot + '''<h2 class="sec"><span class="o">&#9733;</span>The Marquee<span class="o">&#9733;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>More Cuts Coming at Disney</h3><p>Disney is preparing another round of layoffs that would reach thousands of workers across its TV networks, film studio and other divisions, Deadline reports, citing sources. Some divisions are looking for up to 20 percent in cost savings.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3><i>Elsinore</i> Leads the British Indies</h3><p>Simon Stone's <i>Elsinore</i>, starring Andrew Scott, leads the British Independent Film Award nominations with 12, the <i>Hollywood Reporter</i> reports. Clio Barnard's <i>I See Buildings Fall Like Lightning</i> has eight, and <i>Animol</i>, the first feature directed by <i>Adolescence</i> actor Ashley Walters, has seven.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>The Chicks Push Back a Show</h3><p>The Chicks postponed Monday's concert at Hollywood's Dolby Theatre hours before doors opened, citing illness, and moved it to Wednesday, Billboard reports. The show is part of their tour marking 20 years of <i>Taking the Long Way</i>.</p></div></div>
<h2 class="sec"><span class="o">&#127944;</span>The Gridiron<span class="o">&#127944;</span></h2>
<div class="touch-head">Short Week for Baltimore</div>
<div class="line"><b>Bills</b> &middot; Buffalo has a week to rest before Monday night at Minnesota, 8:15. The Ravens, beaten 36&ndash;10 in Orchard Park, host Jacksonville Thursday night, and Sportradar gives them only a 20 percent chance.</div>
<div class="line"><b>Jets</b> &middot; At Kansas City Sunday at 1:00. Sportradar likes the Chiefs at 80 percent, but Kansas City is coming off a 28&ndash;24 loss in Denver.</div>
<div class="pnote"><b>The Sunday Tax &middot; Week 9.</b> Picks at <a href="https://tally.so/r/RGOakJ">tally.so/r/RGOakJ</a>; standings at <a href="https://benthambulletin.github.io/pool/">benthambulletin.github.io/pool</a>. Week 8 went to Tom, $100, on the tiebreaker. $5 a week, straight-up winners, the pot to the best record. Anyone with the link can play. Sheets lock at each kickoff; first game Thu 8:15 p.m., Jaguars at Ravens.</div>
<table class="tbl"><tr><th>AFC East</th><th class="n">W</th><th class="n">L</th><th class="n">PCT</th></tr>
<tr><td style="color:var(--red)">Buffalo</td><td class="n">6</td><td class="n">1</td><td class="n">.857</td></tr>
<tr><td>New England</td><td class="n">5</td><td class="n">3</td><td class="n">.625</td></tr>
<tr><td style="color:var(--red)">N.Y. Jets</td><td class="n">2</td><td class="n">6</td><td class="n">.250</td></tr>
<tr><td>Miami</td><td class="n">1</td><td class="n">6</td><td class="n">.143</td></tr></table>
<div class="line"><b>Monday night.</b> Chicago won 34&ndash;17 at Seattle.</div>
<h2 class="sec"><span class="o">&#9873;</span>The Chase</h2>
'''
BODY = BODY.replace('<h2 class="sec"><span class="o">&#9873;</span>The Chase</h2>', '<h2 class="sec"><span class="o">&#9873;</span>The Chase<span class="o">&#9873;</span></h2>') + '''<div class="line">Larson 2,469; Bell 67 back, Hamlin 70, Briscoe 84, Logano 103. Homestead Sunday decides it.</div>
<h2 class="sec"><span class="o">&#9790;</span>On This Day<span class="o">&#9790;</span></h2>
<div class="otd"><b>November 3, 1948</b> &mdash; The <i>Chicago Tribune</i> went to press with "DEWEY DEFEATS TRUMAN" before the count was done. Truman won, and the next day, in St. Louis, he held the paper up for photographers.</div>
<h2 class="sec"><span class="o">&#10023;</span>Question of the Day<span class="o">&#10023;</span></h2>
<div class="qotd">I have a booth but sell nothing, a curtain but no stage, and every November I'm busiest on a Tuesday. What am I? <i>Answer below the fold.</i></div>
'''
S('<h2 class="sec"><span class="o">&#9825;</span>Family Today', '<div class="dbl"><div class="a"></div><div class="b"></div></div>\n<div class="colo">', BODY)
R("<b>Question of the Day:</b> A ballot.", "<b>Question of the Day:</b> A polling place.")
S('<div class="s">Forecast per', '<div class="sig">',
'''<div class="s">Forecast per NWS Buffalo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; sky computed for 14120 &middot; family counts from the paper's migraine log &middot; election box from the paper's election tracker &middot; Sunday Tax from the pool's standings &middot; headlines via CBS, BBC, NPR, WKBW, WXXI, the Dunkirk <i>Observer</i>, Deadline, the <i>Hollywood Reporter</i>, Billboard &middot; scores, odds and NASCAR points via Sportradar</div>
''')

ed = {"date": "2026-11-03", "no": 132, "body_html": src, "plate_path": None,
      "plate_caption": "Election Day",
      "headline": "Election Day · U.S. strikes Iranian island · 72 and partly sunny"}
for f in ['/home/claude/edition-2026-11-03.json', '/home/claude/site/data/edition-2026-11-03.json']:
    json.dump(ed, open(f, 'w'), ensure_ascii=False, indent=1)
print('ok', len(svg))
