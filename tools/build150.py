import json, sys
sys.path.insert(0, '/home/claude'); from curve import curve; from market_chart import market_chart
src = json.load(open('/home/claude/site/data/edition-2026-11-20.json'))['body_html']
def R(a, c, n=1):
    global src
    assert src.count(a) == n, ('R', a[:60], src.count(a)); src = src.replace(a, c)
def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50]); src = src[:i] + new + src[j:]
f = json.load(open('/home/claude/site/data/forecast.json'))
assert f['generated_utc'].startswith('2026-11-21')
assert [f['towns'][n]['observation']['temp_f'] for n in ['North Tonawanda', 'Dunkirk', 'Scottsville']] == [36, None, 36]
assert f['lakes']['readings'] == {'Lake Erie (Buffalo)': 53, 'Lake Ontario (Rochester)': 54} and 'Fri Nov 20 2026' in f['lakes']['text']
hourly = f['towns']['North Tonawanda']['hourly']; assert 'T05:00' in hourly[0]['start']
chart = curve(hourly, 7 * 60 + 15, 16 * 60 + 47)
m = json.load(open('/home/claude/site/data/market.json')); assert m['last'][0] == '2026-11-19'
mkt = market_chart(m, year=2026).replace("via the St. Louis Fed.</div>", "via the St. Louis Fed. Friday's fall is not yet in the data.</div>")
assert "Friday's fall" in mkt
COVER = {'path': '/home/claude/plate150.jpg', 'alt': 'A boy holding up a small picture book in front of his face', 'caption': 'Now reading: Mr. Busy'}
i = src.find('<img src="__PLATE__"'); j = src.find('>', i) + 1; assert i > 0
src = src[:i] + '<img src="__PLATE__" alt="%s">' % COVER['alt'] + src[j:]
i = src.find('<div class="plate-sub">'); j = src.find('</div>', i) + 6; src = src[:i] + '<div class="plate-sub">%s</div>' % COVER['caption'] + src[j:]
R('<div class="plate-cap">The Cover</div>', '<div class="plate-cap">Plate I &middot; The Family Album</div>')
R('No. 149', 'No. 150'); R('Friday &middot; November 20 &middot; 2026', 'Saturday &middot; November 21 &middot; 2026')
S('<div class="tiles">', '<div class="plate-wrap">', '''<div class="tiles">
  <div class="tile"><div class="v">64&deg;</div><div class="k">Fog, Then Sun</div></div>
  <div class="tile"><div class="v">4:47</div><div class="k">Sunset</div></div>
  <div class="tile urg"><div class="v">5</div><div class="k">Days to Thanksgiving</div></div>
</div>
''')
S('<div class="wire lead">', '<div class="part"><span>The Almanac</span></div>', '''<div class="wire lead"><div><span class="kick">The Lead</span><h3>Wall Street Slides Into a Correction</h3>
<p>The stock market fell hard again Friday. The S&amp;P 500, an index of 500 big American companies that most retirement funds follow, dropped 3.7 percent, its seventh losing day in a row and its longest such streak since February 2020, CBS reports. That left it more than 10 percent below its recent high, which is what Wall Street calls a correction.</p>
''' + mkt + '''
<p>The worry is artificial intelligence. A.I. companies drove much of this year's gains, and investors now doubt that the enormous spending on data centers will pay off; chip makers led Friday's losses. The Nasdaq, the index heaviest in technology, lost 1,261 points and gave back everything it had gained in 2026. Anthropic, the A.I. company that began trading Thursday, fell 9.3 percent to $88.14, still above the $83 its shares were first sold for. (A disclosure: this paper is put together with Anthropic's A.I.)</p>
<p>For a family, it means a 401(k) or an index fund is probably worth less than it was at its October peak. It does not say what comes next: an analyst at E*Trade told CBS that only a third of the corrections since 1983 went on to become bear markets, meaning falls of 20 percent or more.</p>
<div class="pull">"It's impossible to know when any selloff will run its course."<br>&mdash; Chris Larkin, E*Trade from Morgan Stanley</div>
</div></div>
<h2 class="sec">Family Today</h2>
<div class="pnote" style="border:1px solid var(--rule,#d3b88f);padding:.6rem .75rem"><b>From the Group Chat &middot; Gregg, Friday</b><br>"I got today's riddle &#128515;"</div>
<h2 class="sec">The National Wire</h2>
<div class="wire"><div class="num">1</div><div><h3>Guilty Verdict in the Palisades Fire</h3><p>A jury has found Jonathan Rinderknecht guilty of starting the blaze that grew into the Palisades Fire in Los Angeles in January 2025, CBS reports; an earlier trial ended with a deadlocked jury. The fire killed 12 people and destroyed more than 6,800 buildings, and he faces between five and 40 years in federal prison.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>A $7.25 Billion Settlement Over Roundup</h3><p>A Missouri judge on Friday approved a $7.25 billion settlement of lawsuits claiming the weedkiller Roundup causes cancer, the BBC reports. Bayer, the German company that makes it, will pay users who have non-Hodgkin lymphoma, a blood cancer, and those who fall ill later; payments run from $10,000 to $165,000.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Update: A Court Halts the Iowa Blast</h3><p>A federal appeals court on Friday put the Army's plan to blow up unstable explosives at an Iowa ammunition plant on hold indefinitely, CBS reports. Two environmental groups had sued, arguing that the emergency permit was not valid and that residents had too little warning.</p></div></div>
<h2 class="sec">The Home Wire</h2>
<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Comfort Care for the Zoo's Elephant</h3><p>Genny C., the African elephant who has lived at the Seneca Park Zoo since 1979, is receiving palliative care, meaning treatment aimed at keeping her comfortable as she ages, WXXI reports. The zoo says she has had digestive trouble for months and has struggled to keep her weight, and that the barn will be closed to visitors on days she is not feeling well.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Rochester &middot; No Border Patrol Station Downtown</h3><p>U.S. Customs and Border Protection has dropped its plan to turn space in the Keating Federal Building in downtown Rochester into a Border Patrol station, WXXI reports. Sens. Chuck Schumer and Kirsten Gillibrand and Rep. Joseph Morelle announced the reversal Friday; the agency says it will look at other options.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Portland &middot; A Winemaker Earns a Rare Diploma</h3><p>Brian Barmore, head winemaker at 21 Brix Winery in Portland, in Chautauqua County, has earned the top diploma of the Wine &amp; Spirit Education Trust along with its certificate of merit, the <i>Observer</i> reports. He first walked into the winery as a customer in 2018; his final paper was on orange wines.</p></div></div>
<h2 class="sec">The Marquee</h2>
<div class="wire"><div class="num">1</div><div><h3>Patrick Stewart's Cause of Death</h3><p>Patrick Stewart, the English actor who died Oct. 28 at 86, died of cardiopulmonary arrest, with Lewy body dementia listed as an underlying condition, Rolling Stone reports, citing a death certificate obtained by People. His family's statement at the time had spoken of "a brief and poignant journey" with Alzheimer's disease and Lewy body dementia.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Ina Garten Will Not Be Dancing</h3><p>Ina Garten, the Barefoot Contessa, said on her podcast that she was asked to do <i>Dancing With the Stars</i> and turned it down, E! News reports. "Nobody needs to see that," she said. "That's not happening."</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>How Cher Got Phil Collins's Line</h3><p>Phil Collins says Cher sang his line in the "We Are the World" finale at Live Aid in 1985 because he was too tired to stay for it, Billboard reports. The two had met that day on the Concorde he took to play both the London and Philadelphia shows; she asked if he could get her in, and he told her, "You're Cher. ... Just turn up."</p></div></div>
<h2 class="sec">The Gridiron</h2>
<div class="wire"><div><h3>Bills: Dolphins Tomorrow at 1</h3><p>The Bills are 8&ndash;1, the best record in the AFC, and over the last three games have allowed one touchdown and 28 points in all, the Associated Press reports in the Dunkirk <i>Observer</i>. Asked whether that is because they keep drawing backup quarterbacks, with another due Sunday, defensive tackle Ed Oliver said: "Who cares. ... You don't get to choose."</p></div></div>
<div class="wire"><div><h3>Jets: Smith Is Cleared</h3><p>Geno Smith practiced in full Friday and carries no injury label into Sunday's game with the Chargers, ProFootballTalk reports. "He looks solid," coach Aaron Glenn said. "It's very encouraging."</p></div></div>
<div class="wire"><div><h3>Around the Division: Maye Is Hurt</h3><p>Patriots quarterback Drake Maye broke his right fibula, a bone in the lower leg, in last week's loss to the Lions in Munich and is likely out for most or all of the regular season, ProFootballTalk says, citing ESPN.</p></div></div>
''')
S('<p class="wlede">', '<div class="line"><span class="lbl t">Next 24 hours</span>', '''<p class="wlede">Fog at first light, then sunshine and a May afternoon in late November</p>
<div class="wxrow">
  <div class="wxc"><div class="k">Tonight</div><div class="v">45&deg;</div><div class="s">partly cloudy</div></div>
  <div class="wxc"><div class="k">Wind</div><div class="v">2&ndash;6</div><div class="s">mph, south</div></div>
  <div class="wxc"><div class="k">Rain</div><div class="v">None</div><div class="s">until late Sunday night</div></div>
  <div class="wxc"><div class="k">Normal</div><div class="v">46&deg;</div><div class="s">for the date</div></div>
</div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">36<sup>&deg;</sup></div><div class="d">Fog<br>high 64&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">&mdash;</div><div class="d">Clear<br>high 64&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">36<sup>&deg;</sup></div><div class="d">Clear<br>high 66&deg;</div></div>
</div>
<div class="towns lakes">
  <div class="town"><div class="n">Lake Erie</div><div class="t">53<sup>&deg;</sup></div><div class="d">off Buffalo, Friday</div></div>
  <div class="town"><div class="n">Lake Ontario</div><div class="t">54<sup>&deg;</sup></div><div class="d">off Rochester, Friday</div></div>
</div>
<div class="strip5">
  <div><div class="d">Sat</div><div class="i">&#9728;</div><div class="h">64</div><div class="w">fog, then sunny</div></div>
  <div><div class="d">Sun</div><div class="i">&#9729;</div><div class="h">64</div><div class="w">mostly cloudy</div></div>
  <div><div class="d">Mon</div><div class="i">&#127782;</div><div class="h">48</div><div class="w">early showers</div></div>
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">39</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#9728;</div><div class="h">41</div><div class="w">mostly sunny</div></div>
</div>
''')
S('<div class="line"><span class="lbl t">Next 24 hours</span>', '<h2 class="sec">The Almanac Sky</h2>', '<div class="line"><span class="lbl t">Next 24 hours</span></div>' + chart + '''<div class="line"><span class="lbl t">Outdoor window</span> Late morning through sunset. Low 60s from noon on, easing back to the upper 50s by late afternoon.</div>
<div class="line"><span class="lbl t">Frost watch</span> None this weekend. Monday night falls to 31 and Tuesday night to 24.</div>
''')
S('<h2 class="sec">The Almanac Sky</h2>', '<h2 class="sec">Coming Up</h2>', '''<h2 class="sec">The Almanac Sky</h2>
<div class="wxrow">
  <div class="wxc"><div class="k">Moon</div><svg class="moonmini" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#5a4d3b"/><path d="M50 4 A46 46 0 0 1 50 96 A35.5 46 0 0 1 50 4Z" fill="#f4e5b4"/></svg><div class="s">waxing gibbous</div></div>
  <div class="wxc"><div class="k">Sunrise</div><div class="v">7:15</div><div class="s">a.m.</div></div>
  <div class="wxc"><div class="k">Daylight</div><div class="v">9h 32m</div><div class="s">2 min less</div></div>
</div>
<p class="skynote"><b>Tonight:</b> the moon, 89 percent lit, rises at 2:39 this afternoon and sets at 3:38 a.m. Saturn is again the only bright planet of the evening, highest in the south around 9. Mars and Jupiter come up after 11. Full moon Tuesday.</p>
<div class="touch-head">The Stars &middot; for fun</div>
<div class="stars slim">
<div class="star"><span class="sgn">Aries</span> <span class="who">Kaylani, Luka</span><br>The moon is still yours, and Venus is waving from across the sky. Somebody wants your attention; give it.</div>
<div class="star"><span class="sgn">Cancer</span> <span class="who">Gregg</span><br>A cross-angled moon for a second day. You beat the riddle anyway, so the sky can keep its opinion.</div>
<div class="star"><span class="sgn">Leo</span> <span class="who">Leah, Tommy</span><br>Easy light from a friendly moon. A good Saturday to be seen.</div>
<div class="star"><span class="sgn">Virgo</span> <span class="who">Derek, Joanne</span><br>Nothing aimed your way. Do the list, or lose the list.</div>
<div class="star"><span class="sgn">Scorpio</span> <span class="who">Ariel, Claire, Garret</span><br>The moon has no business with you today. Do not check the retirement account.</div>
</div>
''')
S('<h2 class="sec">Coming Up</h2>', '<div class="dbl"><div class="a">', '''<h2 class="sec">Coming Up</h2>
<div class="calbox"><div class="calrow"><div class="cd">Sun</div><div>Dolphins at Bills, 1:00; Jets at Chargers, 4:05</div></div>
<div class="calrow"><div class="cd">Thu</div><div>Thanksgiving; Chiefs at Bills, 8:20</div></div>
<div class="calrow"><div class="cd">Fri</div><div>UB at Akron, noon</div></div>
<div class="calnote">Migraine log: nothing new since Joanne's on Monday. Four this month.</div>
</div>
<h2 class="sec">The Ledger</h2>
<div class="ledger"><div class="num"><div class="cap">What a typical Erie County water bill goes up next year</div><div class="big">$1.77 a month</div></div>
<div class="txt">The water authority's 2027 budget raises rates and puts $78.6 million into the water system, WKBW reports.</div></div>
<h2 class="sec">On This Day</h2>
<div class="otd"><b>November 21, 1877</b> &mdash; Thomas Edison announced the phonograph, a machine that could record sound and play it back.</div>
<h2 class="sec">Question of the Day</h2>
<div class="qotd">Feed me all year and I only get heavier; to get anything back, you may have to break me. What am I? <i>Answer below the fold.</i></div>
''')
R('<b>Question of the Day:</b> A coat hanger.', '<b>Question of the Day:</b> A piggy bank.')
S('headlines via ', ' &middot; scores and stats via Sportradar', 'headlines via CBS, the BBC, WXXI, WKBW, the Dunkirk <i>Observer</i>, Rolling Stone, E! News, Billboard, ProFootballTalk; market data via FRED')
ed = {'date': '2026-11-21', 'no': 150, 'body_html': src, 'plate_path': COVER['path'], 'plate_caption': COVER['caption'],
      'headline': "Wall Street slides into a correction · Guilty verdict in the Palisades Fire · Patrick Stewart's cause of death"}
for p in ['/home/claude/site/data/edition-2026-11-21.json', '/home/claude/edition-2026-11-21.json']:
    json.dump(ed, open(p, 'w'), ensure_ascii=False, indent=1)
print('ok', len(src))
