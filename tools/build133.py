import json, random
src = json.load(open('/home/claude/site/data/edition-2026-11-03.json'))['body_html']

def R(a, c, n=1):
    global src
    assert src.count(a) == n, ('R', a[:60], src.count(a))
    src = src.replace(a, c)

def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50])
    src = src[:i] + new + src[j:]

# ---- drawn cover: the morning after, a warm sunrise over the lake ----
random.seed(1104)
W, H = 600, 320
p = [f'<svg viewBox="0 0 {W} {H}" role="img" aria-label="An illustrated sunrise over a calm lake: a big orange sun lifting above the water, gulls gliding, maples on the shore and the words The Morning After" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;height:auto">']
p.append('<defs><linearGradient id="msky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3b4a72"/><stop offset=".45" stop-color="#c8643a"/><stop offset=".75" stop-color="#f3b45a"/><stop offset="1" stop-color="#f8d98c"/></linearGradient>'
         '<linearGradient id="mlake" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e59a4a"/><stop offset="1" stop-color="#3b4a72"/></linearGradient></defs>')
p.append(f'<rect width="{W}" height="{H}" fill="url(#msky)"/>')
# rising sun
p.append('<g><animateTransform attributeName="transform" type="translate" values="0,30; 0,0; 0,30" dur="16s" repeatCount="indefinite"/>'
         '<circle cx="300" cy="212" r="58" fill="#ffd27a" opacity=".35"/><circle cx="300" cy="212" r="40" fill="#ffe39a"/></g>')
# lake
p.append('<rect x="0" y="214" width="600" height="106" fill="url(#mlake)"/>')
for i in range(7):
    y = 228 + i * 12; w = 120 - i * 12
    p.append(f'<rect x="{300-w/2:.0f}" y="{y}" width="{w}" height="2.5" rx="1" fill="#ffe39a" opacity="{.8-i*.09:.2f}"><animate attributeName="x" values="{300-w/2-6:.0f};{300-w/2+6:.0f};{300-w/2-6:.0f}" dur="{3+i*.5:.1f}s" repeatCount="indefinite"/></rect>')
# shores with maples
p.append('<path d="M0 214 L0 196 Q60 186 120 200 Q150 206 170 214Z" fill="#24170c"/><path d="M600 214 L600 192 Q540 184 480 198 Q450 206 430 214Z" fill="#24170c"/>')
for tx, ty, c in ((40, 182, '#9c3216'), (92, 186, '#cf6f1a'), (520, 178, '#cf6f1a'), (566, 182, '#9c3216')):
    p.append(f'<rect x="{tx-2}" y="{ty}" width="4" height="22" fill="#24170c"/><circle cx="{tx}" cy="{ty-6}" r="16" fill="{c}"/>')
# gulls
def gull(x, y, s, d, b, dx):
    return (f'<g><animateTransform attributeName="transform" type="translate" values="{x},{y}; {x+dx},{y-14}; {x+2*dx},{y}" dur="{d}s" begin="-{b}s" repeatCount="indefinite"/>'
            f'<path transform="scale({s})" d="M-12 0 Q-6 -7 0 0 Q6 -7 12 0" stroke="#24170c" stroke-width="2" fill="none"><animate attributeName="d" values="M-12 0 Q-6 -7 0 0 Q6 -7 12 0;M-12 -3 Q-6 2 0 0 Q6 2 12 -3;M-12 0 Q-6 -7 0 0 Q6 -7 12 0" dur="1.2s" repeatCount="indefinite"/></path></g>')
p.append(gull(120, 110, 1.1, 18, 3, 180)); p.append(gull(380, 90, .8, 22, 9, -160)); p.append(gull(240, 140, .7, 15, 6, 120))
p.append('<text x="300" y="58" text-anchor="middle" font-family="PF, Georgia, serif" font-style="italic" font-size="20" fill="#f8d98c">The</text>')
p.append('<text x="300" y="98" text-anchor="middle" font-family="PF, Georgia, serif" font-weight="800" font-size="40" fill="#fbf5e4">Morning After</text>')
p.append('</svg>')
svg = ''.join(p)

R('No. 132', 'No. 133')
R('Tuesday &middot; November 3 &middot; 2026', 'Wednesday &middot; November 4 &middot; 2026')
S('<div class="tiles">', '<div class="plate-wrap">', '''<div class="tiles">
  <div class="tile"><div class="v">77&deg;</div><div class="k">Partly Sunny</div></div>
  <div class="tile"><div class="v">5:03</div><div class="k">Sunset</div></div>
  <div class="tile urg"><div class="v">7</div><div class="k">Senate seats flipped</div></div>
</div>
''')
S('<div class="plate-wrap">', '<div class="dbl-tight">', '''<div class="plate-wrap"><div class="frame"><span class="tick tl"></span><span class="tick tr"></span><span class="tick bl"></span><span class="tick br"></span>
''' + svg + '''</div>
<div class="plate-cap">Plate I &middot; The Family Album</div>
<div class="plate-sub">The morning after</div></div>
''')

BODY = '''<h2 class="sec"><span class="o">&#9825;</span>Family Today<span class="o">&#9825;</span></h2>
<div class="fam"><b>The morning after</b>: Democrats won both houses of Congress overnight, and Kathy Hochul won a second full term. The results are in the Ballot just below. Outside, it's near-record warm, 77, before the rain tonight.
<div class="line" style="margin-top:.4rem"><span class="lbl t">The log</span> Days since the last migraine: Garret 1, Dad 29, Mom 6. November so far: Garret one, Monday into Tuesday.</div>
<ul class="cal">
<li><span class="dt">Nov 8</span><span>Jets at Kansas City, 1:00 &middot; NASCAR's finale at Homestead</span></li>
<li><span class="dt">Nov 9</span><span>Bills at Minnesota, Monday night, 8:15</span></li>
</ul>
<div class="ask"><b>Send something to the paper:</b> a photo, a story, your Sunday answer or a date for the calendar, at <a href="https://tally.so/r/rjxDpl">tally.so/r/rjxDpl</a>. It runs the next morning under your name.<br><b>Had a migraine?</b> Log it at <a href="https://tally.so/r/obWNYP">tally.so/r/obWNYP</a>.</div></div>
<h2 class="sec"><span class="o">&#9745;</span>The Ballot &middot; Results<span class="o">&#9745;</span></h2>
<div class="touch-head">Democrats Take Congress</div>
<div class="line"><b>The Senate.</b> Democrats have won it. They took seven Republican-held seats: Troy Jackson beat Susan Collins in Maine (Collins conceded), Sherrod Brown beat Jon Husted in Ohio, James Talarico beat Ken Paxton in Texas, Josh Turek won Iowa, Adam Hamilton beat Roger Marshall in Kansas, Roy Cooper won North Carolina and Annie Andrews won South Carolina. They kept every seat they had to defend, including Michigan, where Abdul El-Sayed beat Mike Rogers. The AP count at 12:30 a.m. was 52 to 41, before Maine and Michigan were called; Alaska and Nebraska are still counting.</div>
<div class="line"><b>The House.</b> Democrats are winning it. They flipped three Pennsylvania seats, with Bob Brooks, Paige Cognetti and Janelle Stelson beating Republican incumbents, and in New York's Hudson Valley, Mike Lawler (R) conceded NY-17 to Cait Conley (D). News outlets say Democrats have the majority; the AP had them at 197 seats to 117 at 12:30 a.m., with 121 seats still uncalled.</div>
<div class="line"><b>New York.</b> Hochul (D) beat Bruce Blakeman (R) for a second full term; the AP called it at 9:18 p.m.</div>
<div class="line"><b>Our House seats.</b> <b>NY-26</b> (North Tonawanda): Kennedy (D) leads Hannon (R) 65 to 34 percent with about 82 percent counted. <b>NY-23</b> (Orchard Park, Dunkirk, Fredonia): Langworthy (R) won, the AP called. <b>NY-25</b> (Scottsville): Morelle (D) leads McIntyre (R) 63 to 37 percent with about 75 percent counted.</div>
<div class="line"><b>Albany.</b> In North Tonawanda's open Assembly seat, Wydysh (R) leads McMurray (D) with 54 percent, unofficially. For Scottsville, Helming (R) leads Mills (D) for State Senate, and Hawley (R) was reported reelected to the Assembly. Ortt's and Borrello's Senate seats, the other Assembly races, North Tonawanda's community-center vote and the county races aren't in the tracker yet.</div>
<div class="line"><b>What it means.</b> From January, a Democratic Congress and a Republican president: new laws will need both, and Democrats will chair the committees. <b>What's next:</b> Westchester's delayed ballots are counted today to settle NY-17; Alaska's final tally is Nov. 18, when New York counties also begin the official canvass.</div>
<div class="line" style="color:var(--soft)">Every race, updated as counts come in: <a href="https://benthambulletin.github.io/election/">benthambulletin.github.io/election</a></div>
<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass<span class="o">&#9788;</span></h2>
<div class="wx"><div class="bigtemp">77<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">Summer's last word: partly sunny and 77, near the record, then rain moves in tonight</span>
Low <b>58&deg;</b> tonight &middot; rain after 7 p.m., 80%<br>Gusts to 32 Thursday; colder by the weekend</div></div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">61<sup>&deg;</sup></div><div class="d">Clear &middot; high 77&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">66<sup>&deg;</sup></div><div class="d">Clear &middot; high 78&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">55<sup>&deg;</sup></div><div class="d">Clear &middot; high 78&deg;</div></div>
</div>
<div class="strip5">
  <div><div class="d">Wed</div><div class="i">&#9925;</div><div class="h">77</div><div class="w">rain tonight</div></div>
  <div><div class="d">Thu</div><div class="i">&#9925;</div><div class="h">65</div><div class="w">windy, clearing</div></div>
  <div><div class="d">Fri</div><div class="i">&#127783;</div><div class="h">61</div><div class="w">chance of showers</div></div>
  <div><div class="d">Sat</div><div class="i">&#127783;</div><div class="h">53</div><div class="w">showers likely</div></div>
  <div><div class="d">Sun</div><div class="i">&#9925;</div><div class="h">54</div><div class="w">partly sunny</div></div>
</div>
<div class="line"><span class="lbl t">Outdoor window</span> Today, until about 7 p.m. Rochester's forecasters call it near-record warmth, Rochester First reports.</div>
<div class="line"><span class="lbl t">Frost watch</span> Not yet, but closer: 36 Sunday night in North Tonawanda, 35 in Scottsville.</div>
<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky<span class="o">&#9790;</span></h2>
<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 0 50 96 A26.9 46 0 0 1 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>Waning crescent</b>, 21 percent lit, in Leo; rose at 1:54 a.m., sets at 2:46 p.m.<br>
<span class="lbl t">Sun</span> 6:53a &ndash; 5:03p &middot; <b>10h 10m</b>, 2&frac12; minutes less than yesterday<br>
<span class="lbl t">Mercury</span> Lines up almost exactly with the sun today, lost in its glare.<br>
<span class="lbl t">New moon</span> Mon, Nov 9 &middot; <span class="lbl t">Beaver Moon</span> Tue, Nov 24</div></div>
<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>Neptune, in your sign, sextiles Pluto</b>. Big news, slow change. Plan for the long run. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>Uranus sextiles Neptune</b>. Everyone has a take this morning. Yours can wait till dinner. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Venus sextiles Jupiter in your sign</b>, exact today. Celebrate gracefully, or console gracefully. Both count. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>Uranus trines Pluto</b>. Read past the headline before you forward it. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Mercury meets the sun in your sign</b>, nearly to the degree. Clear head, clear words. Say the kind thing first. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
<div style="font-family:'LOI';font-style:italic;font-size:.8rem;color:var(--soft);margin-top:.4rem">Positions computed for noon today at 14120. The sky is real; the readings are for fun.</div>
<h2 class="sec"><span class="o">&#10038;</span>The Ledger<span class="o">&#10038;</span></h2>
<div class="ledger"><div class="num"><div class="cap">Royalties collected for songwriters and composers worldwide in 2025, a record</div><div class="big">$15.9B</div></div>
<div class="txt">Up 11.9 percent from 2024, the global royalty federation CISAC says, Billboard reports; more than half the jump comes from counting a U.S. collector for the first time. CISAC calls AI its "largest test."</div></div>
<h2 class="sec"><span class="o">&#10038;</span>The National Wire<span class="o">&#10038;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>Guilty Plea in an Ethiopia Spy Case</h3><p>Abraham Teklu Lemma, a former U.S. contractor born in Ethiopia, pleaded guilty to passing dozens of classified documents and photos to senior Ethiopian officials over more than two years, the Justice Department said, the BBC reports. He hoped some of it would help target fighters from Ethiopia's Tigray region during the 2020&ndash;22 civil war; under the plea deal he faces up to 22 years in prison.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>A Cruise Ship Sails On, Empty</h3><p>The MV <i>Odyssey</i>, a Florida company's ship on a planned three-year trip around the world, left Cambodia late Tuesday with only crew aboard, CBS reports. The company suspended the voyage last week over soaring fuel costs and gave its 203 passengers a few hours' notice to get off at the port of Sihanoukville.</p></div></div>
<h2 class="sec"><span class="o">&#9962;</span>The Home Wire<span class="o">&#9962;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Campus Hacking Charges</h3><p>Two Canadian men are accused of a computer-hacking scheme aimed at schools and colleges, including some in Western New York, the U.S. Attorney's office says, Rochester First reports. Investigators say they ran the scheme through private servers in several countries, registered under false names.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Fredonia &middot; Honoring Student Veterans</h3><p>SUNY Fredonia holds its annual Veterans Day ceremony Friday at 3:30 p.m. in the Williams Center Multipurpose Room, open to the public, the <i>Observer</i> reports. Veterans and students will speak, and more than $3,700 in scholarships will go to students connected to the veteran community.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Pomfret &middot; Recycling Yard Still Waiting</h3><p>After three meetings, Pomfret's zoning appeals board still hasn't granted Steve St. George a permit for a concrete and asphalt recycling yard on Webster Road, on land that used to grow grapes, the <i>Observer</i> reports. He needs a special-use permit, a sign-off for a business the zoning doesn't allow on its own.</p></div></div>
<h2 class="sec"><span class="o">&#9733;</span>The Marquee<span class="o">&#9733;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>Tokyo's Top Prize to a Manhole Cover</h3><p>Milcho Manchevski's <i>Sister Brother Manhole Cover</i>, a comic fable about two siblings who strip scrap metal from the streets of Skopje, North Macedonia, won the Grand Prix at the Tokyo International Film Festival, Variety reports. The prize comes with about $19,000, Deadline adds.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Australia Starts a National Songbook</h3><p>Midnight Oil's "Beds Are Burning" and the Easybeats' "Friday on My Mind" are among the first 10 songs named to Australia's new National Songbook, announced Wednesday in Canberra, Billboard reports. The yearly honor recognizes songs "whose creative vision has given voice to Australian stories."</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Van Damme Picks Up a Sword</h3><p>Jean-Claude Van Damme will star in <i>Katana</i>, a yakuza action film set in Japan, Deadline reports. It's from French producer Jeremy Zag, the creator of the cartoon hit <i>Miraculous</i>.</p></div></div>
<h2 class="sec"><span class="o">&#127944;</span>The Gridiron<span class="o">&#127944;</span></h2>
<div class="touch-head">Gardner-Johnson Released</div>
<div class="line"><b>Bills</b> &middot; Buffalo released safety C.J. Gardner-Johnson Tuesday, a day after he finished a one-game NFL suspension for spitting toward Las Vegas players, the <i>Observer</i> reports. The team gave no reason, though the suspension and his uneven play were seen as factors, the <i>Observer</i>'s report says. Next: Monday night at Minnesota, 8:15.</div>
<div class="line"><b>Jets</b> &middot; At Kansas City Sunday at 1:00.</div>
<div class="pnote"><b>The Sunday Tax &middot; Week 9.</b> Picks at <a href="https://tally.so/r/RGOakJ">tally.so/r/RGOakJ</a>; standings at <a href="https://benthambulletin.github.io/pool/">benthambulletin.github.io/pool</a>. $5 a week, straight-up winners, the pot to the best record. Anyone with the link can play. Sheets lock at each kickoff; first game tomorrow, Thu 8:15 p.m., Jaguars at Ravens.</div>
<table class="tbl"><tr><th>AFC East</th><th class="n">W</th><th class="n">L</th><th class="n">PCT</th></tr>
<tr><td style="color:var(--red)">Buffalo</td><td class="n">6</td><td class="n">1</td><td class="n">.857</td></tr>
<tr><td>New England</td><td class="n">5</td><td class="n">3</td><td class="n">.625</td></tr>
<tr><td style="color:var(--red)">N.Y. Jets</td><td class="n">2</td><td class="n">6</td><td class="n">.250</td></tr>
<tr><td>Miami</td><td class="n">1</td><td class="n">6</td><td class="n">.143</td></tr></table>
<h2 class="sec"><span class="o">&#9873;</span>The Chase<span class="o">&#9873;</span></h2>
<div class="line">No change: Larson leads Bell by 67 with Homestead left.</div>
<h2 class="sec"><span class="o">&#9790;</span>On This Day<span class="o">&#9790;</span></h2>
<div class="otd"><b>November 4, 1922</b> &mdash; In Egypt's Valley of the Kings, Howard Carter's crew uncovered the first step down to the tomb of Tutankhamun.</div>
<h2 class="sec"><span class="o">&#10023;</span>Question of the Day<span class="o">&#10023;</span></h2>
<div class="qotd">I'm a race with no runners and no finish line you can see, and I'm often called before I'm over. What am I? <i>Answer below the fold.</i></div>
'''
S('<h2 class="sec"><span class="o">&#9825;</span>Family Today', '<div class="dbl"><div class="a"></div><div class="b"></div></div>\n<div class="colo">', BODY)
R("<b>Question of the Day:</b> A polling place.", "<b>Question of the Day:</b> An election. Ours are on the tracker.")
S('<div class="s">Forecast per', '<div class="sig">',
'''<div class="s">Forecast per NWS Buffalo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; sky computed for 14120 &middot; family counts from the paper's migraine log &middot; results from the paper's election tracker (AP calls) &middot; Sunday Tax from the pool's standings &middot; headlines via BBC, CBS, Rochester First, the Dunkirk <i>Observer</i>, Billboard, Variety, Deadline &middot; scores and NASCAR points via Sportradar</div>
''')

ed = {"date": "2026-11-04", "no": 133, "body_html": src, "plate_path": None,
      "plate_caption": "The morning after",
      "headline": "Democrats take Congress · Hochul wins again · Near-record 77"}
for f in ['/home/claude/edition-2026-11-04.json', '/home/claude/site/data/edition-2026-11-04.json']:
    json.dump(ed, open(f, 'w'), ensure_ascii=False, indent=1)
print('ok', len(svg))
