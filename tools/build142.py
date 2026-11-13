import json, re, glob, datetime
src = json.load(open('/home/claude/site/data/edition-2026-11-12.json'))['body_html']
def R(a, c, n=1):
    global src
    assert src.count(a) == n, ('R', a[:60], src.count(a)); src = src.replace(a, c)
def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50]); src = src[:i] + new + src[j:]
f = json.load(open('/home/claude/site/data/forecast.json'))
assert f['generated_utc'].startswith('2026-11-13')
assert [f['towns'][n]['observation']['temp_f'] for n in ['North Tonawanda', 'Dunkirk', 'Scottsville']] == [36, 37, 37]
hr = [h['temp'] for h in f['towns']['North Tonawanda']['hourly']][:24]
W, H, P = 320, 62, 12
lo, hi = min(hr), max(hr)
xs = [P + i * (W - 2 * P) / (len(hr) - 1) for i in range(len(hr))]
ys = [H - P - (t - lo) * (H - 2 * P - 10) / max(1, hi - lo) for t in hr]
pts = ' '.join(f'{x:.1f},{y:.1f}' for x, y in zip(xs, ys))
ih, il = hr.index(hi), len(hr) - 1 - hr[::-1].index(lo)
def lab(i, t, col):
    anc = 'start' if i < 3 else ('end' if i > len(hr) - 4 else 'middle')
    return (f'<circle cx="{xs[i]:.1f}" cy="{ys[i]:.1f}" r="3" fill="{col}"/><text x="{xs[i]:.1f}" y="{ys[i]-6:.1f}" text-anchor="{anc}" font-family="Archivo,Arial" font-size="10" fill="#24170c">{t}&deg;</text>')
spark = (f'<div class="line"><span class="lbl t">Next 24 hours</span></div>'
         f'<svg viewBox="0 0 {W} {H}" style="display:block;width:100%;max-width:420px;height:auto;margin:0 auto .4rem" role="img" aria-label="Hourly temperatures for North Tonawanda over the next 24 hours, from {hr[0]} now to a high of {hi} and a low of {lo}">'
         f'<polyline points="{pts}" fill="none" stroke="#9c3216" stroke-width="2" stroke-linejoin="round"/>'
         + lab(ih, hi, '#9c3216') + lab(il, lo, '#2f5e3e') +
         f'<text x="{P}" y="{H-1}" font-family="Archivo,Arial" font-size="9" fill="#6b5a48">now</text><text x="{W-P}" y="{H-1}" text-anchor="end" font-family="Archivo,Arial" font-size="9" fill="#6b5a48">this time tomorrow</text></svg>\n')
# next Friday the 13th after today
d = datetime.date(2026, 12, 13)
while d.weekday() != 4:
    m = d.month % 12 + 1; d = datetime.date(d.year + (1 if m == 1 else 0), m, 13)
nxt = d.strftime('%B %Y'); print('next Fri 13:', nxt)
assert [m for m in range(1, 13) if datetime.date(2026, m, 13).weekday() == 4] == [2, 3, 11]

S('<svg viewBox="0 0 750 375"', '</div>\n<div class="plate-cap">', '<img src="__PLATE__" alt="A little boy with brown hair and a gray sweatshirt grinning up at the camera in a living room">')
R('<div class="plate-sub">A raw, rainy Thursday</div>', '<div class="plate-sub">A grin for the camera</div>')
R('No. 141', 'No. 142'); R('Thursday &middot; November 12 &middot; 2026', 'Friday &middot; November 13 &middot; 2026')
S('<div class="tiles">', '<div class="plate-wrap">', '''<div class="tiles">
  <div class="tile"><div class="v">41&deg;</div><div class="k">Mixed Showers</div></div>
  <div class="tile"><div class="v">4:53</div><div class="k">Sunset</div></div>
  <div class="tile urg"><div class="v">13</div><div class="k">Days to Thanksgiving</div></div>
</div>
''')
S('<div class="wire lead">', '<div class="part"><span>The Almanac</span></div>', '''<div class="wire lead"><div><span class="kick">The Lead</span><h3>Microsoft Outage Knocks Out Outlook and Teams</h3>
<p>A Microsoft outage that has dragged on for hours has left Outlook email, the Teams meeting app and the Copilot assistant down or spotty for users from Asia to the United States, hitting companies and some government offices, CBS reports.</p>
<p>Microsoft says the trouble is in the systems behind Exchange Online, the service that runs its email, and that it has no sign the outage was caused by an attack.</p>
<p>Early Friday the company said service was coming back gradually, starting in Asia, with mailbox access improving, but warned that "some users may continue to experience intermittent issues." If work email is slow this morning, that is why.</p>
</div></div>
<div class="wire"><div><h3>Reader Poll: The Paper at 6 a.m. or 8 a.m.?</h3><p>This is about what time the Bulletin is sent to you. Right now the link is texted at about 8 a.m.; it could be published and texted automatically at 6 a.m. instead, waiting when you wake up. Which do you want? Vote at <a href="https://tally.so/r/5XjVlv">tally.so/r/5XjVlv</a>; it takes ten seconds.</p></div></div>
<h2 class="sec">The National Wire</h2>
<div class="wire"><div class="num">1</div><div><h3>Update: Brooklyn Toll Rises to Eight</h3><p>Eight people died and 18 were injured in Wednesday's building collapse in Brooklyn, the BBC reports; two of the dead were children, according to PBS. The search ended Thursday, about 24 hours after the collapse, when fire officials determined there were no more victims.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>A Challenge to Schumer</h3><p>Sen. Chris Van Hollen of Maryland said Thursday he will run against Sen. Chuck Schumer for Senate majority leader, the top job in the chamber Democrats won in last week's midterms, CBS reports. "We need new leadership," Van Hollen wrote, and Sen. Bernie Sanders of Vermont quickly backed him.</p></div></div>
<h2 class="sec">The Home Wire</h2>
<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; A Founder Steps Down After 45 Years</h3><p>Nydia Padilla-Rodriguez, who founded Borinquen Dance Theatre, retires in December after 45 years as its artistic director, WXXI reports. She built an award-winning youth program that teaches self-confidence and discipline through dance while celebrating Puerto Rican culture; her successor grew up in Rochester.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Fredonia &middot; Borrowing for the Water Hookup</h3><p>Fredonia is weighing a bond anticipation note, a short-term loan taken out ahead of a longer bond, to help pay for connecting to the North County Water District, Trustee Tim Mulholland said this week, the <i>Observer</i> reports. One priority is repaying the village water fund about $500,000 already spent on engineering and related costs.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Buffalo &middot; Masks Return to Hospital Floors</h3><p>Starting Monday, Catholic Health will require doctors, nurses and other staff who care for patients to wear masks, and will strongly encourage visitors to, as flu cases climb across the state, WKBW reports. "This is very different than, for example, masking in public the way we did with COVID," said Dr. Thomas Cumbo, an infectious disease physician at Kenmore Mercy.</p></div></div>
<h2 class="sec">The Marquee</h2>
<div class="wire"><div class="num">1</div><div><h3>Dolly's Last Song</h3><p>U2's new album, <i>Carnaval de Luz</i>, out today, closes with "Torn," a duet between Bono and Dolly Parton that is her final recording, Rolling Stone reports. Parton, who died in August at 80, recorded her part in June; "she got out of her bed to sing this song," Bono said.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Rosal&iacute;a Makes It Three</h3><p>Rosal&iacute;a won Album of the Year for <i>Lux</i> at Thursday's Latin Grammys, her third time taking the night's top prize and the first time a woman has won it that often as a lead artist, Rolling Stone reports. She was in tears as she accepted it from the Colombian rocker Juanes, who helped her early in her career.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Vader's Lightsaber: $4.875 Million</h3><p>The lightsaber Darth Vader used in <i>The Empire Strikes Back</i> and <i>Return of the Jedi</i>, including the duel where he tells Luke Skywalker "I am your father," sold Thursday for $4.875 million, CBS reports. Heritage Auctions calls it a record for any <i>Star Wars</i> collectible.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>Danes and McGregor, Jan. 13</h3><p><i>The Spot</i>, a psychological thriller starring Claire Danes and Ewan McGregor about a successful surgeon and her schoolteacher husband, premieres on Hulu on Jan. 13, Deadline reports. Hulu released the first photos along with the date.</p></div></div>
<h2 class="sec">The Gridiron</h2>
<div class="wire"><div><h3>Bills: Brown Sits Out</h3><p>Right tackle Spencer Brown did not practice Thursday because of the ankle injury he suffered Monday night in Minnesota, Buffalo Rumblings reports. Sam Franklin was added to the injury report with a shoulder injury.</p></div></div>
<div class="wire"><div><h3>Jets Want Geno Back</h3><p>The Jets are "expected to seriously consider" bringing quarterback Geno Smith back in 2027, The Athletic's Zack Rosenblatt wrote, according to Gang Green Nation. Smith, who can become a free agent after the season, has played well and is respected in the locker room, the site says.</p></div></div>
<div class="wire"><div><h3>UB Bulls: Five Straight, and Bowl Eligible</h3><p>The University at Buffalo beat Ball State 28&ndash;7 on Wednesday night for its fifth win in a row. It was the Bulls' sixth win, which makes them bowl eligible, meaning they have the six wins a team needs to be invited to a postseason bowl game, WGRZ reports.</p><p>They did it on the ground: 302 rushing yards on 52 carries and three rushing touchdowns, one a 67-yard run in the fourth quarter. Ball State's only points came on a blocked punt, and it missed three field goals.</p></div></div>
''')
S('<p class="wlede">', '<div class="line"><span class="lbl t">Next 24 hours</span>', '''<p class="wlede">Light snow at the Rochester airport at dawn; raw, with rain and snow showers on and off</p>
<div class="wxrow">
  <div class="wxc"><div class="k">Tonight</div><div class="v">32&deg;</div><div class="s">showers</div></div>
  <div class="wxc"><div class="k">Wind</div><div class="v">9 mph</div><div class="s">north</div></div>
  <div class="wxc"><div class="k">Showers</div><div class="v">40%</div><div class="s">rain or snow</div></div>
  <div class="wxc"><div class="k">Normal</div><div class="v">49&deg;</div><div class="s">for the date</div></div>
</div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">36<sup>&deg;</sup></div><div class="d">Cloudy<br>high 41&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">37<sup>&deg;</sup></div><div class="d">Cloudy<br>high 42&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">37<sup>&deg;</sup></div><div class="d">Light snow<br>high 41&deg;</div></div>
</div>
<div class="towns lakes">
  <div class="town"><div class="n">Lake Erie</div><div class="t">57<sup>&deg;</sup></div><div class="d">off Buffalo, Thursday</div></div>
  <div class="town"><div class="n">Lake Ontario</div><div class="t">57<sup>&deg;</sup></div><div class="d">off Rochester, Thursday</div></div>
</div>
<div class="strip5">
  <div><div class="d">Fri</div><div class="i">&#127784;</div><div class="h">41</div><div class="w">rain, snow showers</div></div>
  <div><div class="d">Sat</div><div class="i">&#127783;</div><div class="h">44</div><div class="w">rain showers</div></div>
  <div><div class="d">Sun</div><div class="i">&#9729;</div><div class="h">45</div><div class="w">mostly cloudy</div></div>
  <div><div class="d">Mon</div><div class="i">&#9925;</div><div class="h">48</div><div class="w">partly sunny</div></div>
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">52</div><div class="w">sunny</div></div>
</div>
''')
S('<div class="line"><span class="lbl t">Next 24 hours</span>', '<h2 class="sec">The Almanac Sky</h2>', spark + '''<div class="line"><span class="lbl t">Outdoor window</span> Late morning through mid-afternoon is the mildest stretch, near 41, with a shower possible at any point.</div>
<div class="line"><span class="lbl t">Snow watch</span> Snow showers may mix with the rain this morning and again tonight; lows of 32 here and 30 in Scottsville.</div>
''')
S('<h2 class="sec">The Almanac Sky</h2>', '<h2 class="sec">Coming Up</h2>', '''<h2 class="sec">The Almanac Sky</h2>
<div class="wxrow">
  <div class="wxc"><div class="k">Moon</div><svg class="moonmini" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#5a4d3b"/><path d="M50 4 A46 46 0 0 1 50 96 A30.2 46 0 0 0 50 4Z" fill="#f4e5b4"/></svg><div class="s">waxing crescent</div></div>
  <div class="wxc"><div class="k">Sunrise</div><div class="v">7:05</div><div class="s">a.m.</div></div>
  <div class="wxc"><div class="k">Daylight</div><div class="v">9h 49m</div><div class="s">2 min less</div></div>
</div>
<p class="skynote"><b>Tonight:</b> a 17 percent crescent in Sagittarius sets at 7:56, if the clouds part. Saturn is highest in the south around 9. Eleven days to the full Beaver Moon.</p>
<div class="touch-head">The Stars &middot; for fun</div>
<div class="stars slim">
<div class="star"><span class="sgn">Aries</span> <span class="who">Kaylani, Luka</span><br>The day pushes back a little. Friday the 13th has nothing to do with it; go slow anyway.</div>
<div class="star"><span class="sgn">Cancer</span> <span class="who">Gregg</span><br>Somebody sees it the opposite way. Hear them out before dinner.</div>
<div class="star"><span class="sgn">Leo</span> <span class="who">Leah, Tommy</span><br>Nothing is aimed at you today. Walk under the ladder if you like.</div>
<div class="star"><span class="sgn">Virgo</span> <span class="who">Derek, Joanne</span><br>The moon is working with you. Clear the one job you've been dodging.</div>
<div class="star"><span class="sgn">Scorpio</span> <span class="who">Ariel, Claire, Garret</span><br>A good day for words. Send the message you've been writing in your head.</div>
</div>
''')
S('<h2 class="sec">Coming Up</h2>', '<div class="dbl"><div class="a">', f'''<h2 class="sec">Coming Up</h2>
<div class="calbox"><div class="calrow"><div class="cd">Sun</div><div>Bills at Jets, 1:00</div></div>
<div class="calrow"><div class="cd">Wed</div><div>Central Michigan at UB, 7:30</div></div>
<div class="calrow"><div class="cd">Nov 22</div><div>Dolphins at Bills, 1:00; Jets at Chargers, 4:05</div></div>
<div class="calrow"><div class="cd">Nov 26</div><div>Thanksgiving; Chiefs at Bills, 8:20</div></div>
</div>
<h2 class="sec">The Ledger</h2>
<div class="ledger"><div class="num"><div class="cap">Friday the 13ths in 2026</div><div class="big">3</div></div>
<div class="txt">February, March and today. Three is the most one year can hold, and the next one is not until {nxt}.</div></div>
<h2 class="sec">On This Day</h2>
<div class="otd"><b>November 13, 1982</b> &mdash; The Vietnam Veterans Memorial was dedicated in Washington, its black granite wall carved with the names of more than 57,000 Americans.</div>
<h2 class="sec">Question of the Day</h2>
<div class="qotd">Hotels skip me between the twelfth floor and the fourteenth, bakers toss me in to round out a dozen, and today I have landed on a Friday. What number am I? <i>Answer below the fold.</i></div>
''')
R('<b>Question of the Day:</b> A puddle.', '<b>Question of the Day:</b> Thirteen.')
S('headlines via ', ' &middot; scores and stats via Sportradar', 'headlines via CBS, the BBC, PBS, WXXI, the Dunkirk <i>Observer</i>, WKBW, WGRZ, Rolling Stone, Deadline, Buffalo Rumblings, Gang Green Nation')
for dd in ['2026-11-10', '2026-11-11', '2026-11-12']:
    o = json.load(open(f'/home/claude/site/data/edition-{dd}.json'))['body_html']
    for w in ['Microsoft', 'Van Hollen', 'Schumer', 'Borinquen', 'Fredonia', 'Catholic Health', 'Dolly', 'Rosal', 'Vader', 'The Spot', 'Spencer Brown', 'Geno', 'Ball State', 'Flatbush', 'Brooklyn']:
        if w in o: print('PRIOR', dd, w)
assert 'No. 141' not in src and 'November 12 &middot;' not in src and 'Thursday &middot;' not in src
ed = {"date": "2026-11-13", "no": 142, "body_html": src, "plate_path": "/home/claude/plate142.jpg", "plate_caption": "A grin for the camera",
      "headline": "Microsoft outage · Reader poll: 6 a.m. or 8 a.m.? · UB is bowl eligible"}
for p in ['/home/claude/site/data/edition-2026-11-13.json', '/home/claude/edition-2026-11-13.json']:
    json.dump(ed, open(p, 'w'), indent=1)
print('built', len(src))
