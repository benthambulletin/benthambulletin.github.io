import json
src = json.load(open('/home/claude/site/data/edition-2026-11-13.json'))['body_html']
def R(a, c, n=1):
    global src
    assert src.count(a) == n, ('R', a[:60], src.count(a)); src = src.replace(a, c)
def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50]); src = src[:i] + new + src[j:]
f = json.load(open('/home/claude/site/data/forecast.json'))
assert f['generated_utc'].startswith('2026-11-14')
assert [f['towns'][n]['observation']['temp_f'] for n in ['North Tonawanda', 'Dunkirk', 'Scottsville']] == [37, 39, 36]
assert f['lakes']['readings'] == {'Lake Erie (Buffalo)': 56, 'Lake Ontario (Rochester)': 56} and 'Fri Nov 13 2026 The water temperature off Buffalo' in f['lakes']['text']
h0 = f['towns']['North Tonawanda']['hourly'][0]['start']; assert 'T06:00' in h0
hr = [h['temp'] for h in f['towns']['North Tonawanda']['hourly']][:24]
W, H, P = 320, 62, 12
lo, hi = min(hr), max(hr); assert (hi, lo) == (42, 32)
xs = [P + i * (W - 2 * P) / (len(hr) - 1) for i in range(len(hr))]
ys = [H - P - (t - lo) * (H - 2 * P - 10) / max(1, hi - lo) for t in hr]
pts = ' '.join(f'{x:.1f},{y:.1f}' for x, y in zip(xs, ys))
ih, il = hr.index(hi), len(hr) - 1 - hr[::-1].index(lo)
def lab(i, t, col):
    anc = 'start' if i < 3 else ('end' if i > len(hr) - 4 else 'middle')
    return (f'<circle cx="{xs[i]:.1f}" cy="{ys[i]:.1f}" r="3" fill="{col}"/><text x="{xs[i]:.1f}" y="{ys[i]-6:.1f}" text-anchor="{anc}" font-family="Archivo,Arial" font-size="10" fill="#24170c">{t}&deg;</text>')
spark = (f'<div class="line"><span class="lbl t">Next 24 hours</span></div>'
         f'<svg viewBox="0 0 {W} {H}" style="display:block;width:100%;max-width:420px;height:auto;margin:0 auto .4rem" data-start="6" role="img" aria-label="Hourly temperatures for North Tonawanda over the next 24 hours, from {hr[0]} at 6 a.m. to a high of {hi} and a low of {lo}">'
         f'<polyline points="{pts}" fill="none" stroke="#9c3216" stroke-width="2" stroke-linejoin="round"/>'
         + lab(ih, hi, '#9c3216') + lab(il, lo, '#2f5e3e') +
         f'<text x="{P}" y="{H-1}" font-family="Archivo,Arial" font-size="9" fill="#6b5a48">now</text><text x="{W-P}" y="{H-1}" text-anchor="end" font-family="Archivo,Arial" font-size="9" fill="#6b5a48">this time tomorrow</text></svg>\n')

R('No. 142', 'No. 143'); R('Friday &middot; November 13 &middot; 2026', 'Saturday &middot; November 14 &middot; 2026')
R('alt="A little boy with brown hair and a gray sweatshirt grinning up at the camera in a living room"', 'alt="A boy tending a backyard fire pit at dusk"')
R('<div class="plate-sub">A grin for the camera</div>', '<div class="plate-sub">Tending the fire</div>')
S('<div class="tiles">', '<div class="plate-wrap">', '''<div class="tiles">
  <div class="tile"><div class="v">42&deg;</div><div class="k">Rain Showers</div></div>
  <div class="tile"><div class="v">4:52</div><div class="k">Sunset</div></div>
  <div class="tile urg"><div class="v">1</div><div class="k">Day to Bills&ndash;Jets</div></div>
</div>
''')
S('<div class="wire lead">', '<div class="part"><span>The Almanac</span></div>', '''<div class="wire lead"><div><span class="kick">The Lead</span><h3>Every Departure in the Country Was Held for Hours</h3>
<p>The Federal Aviation Administration ordered a nationwide ground stop Friday afternoon, an order that holds planes at the gate instead of letting them take off, on every departing flight in the United States, citing "extraordinary circumstances and for reasons of safety," CBS reports. The BBC puts the announcement at 3:54 p.m. Eastern and calls it the longest nationwide ground stop since Sept. 11, 2001.</p>
<p>The FAA blamed a telecommunications outage. Transportation Secretary Sean Duffy blamed "an incredibly old air traffic control system" whose routers "got overloaded with data," and Homeland Security Secretary Markwayne Mullin said there was no sign of a cyberattack. Sources told CBS that an update to the private network controllers use set off a reboot and a crash.</p>
<div class="pull">"At 8:15 tonight, Eastern time, we've opened up the airspace. &hellip; It's going to be slow."<br>&mdash; Sean Duffy</div>
<p>FlightAware counted more than 8,500 delayed flights and nearly 8,000 cancellations Friday, according to the BBC. More than 3,500 planes were in the air when the order came; some were diverted and others flew on to where they were going. "It's going to take us some time to unwind what's happened this afternoon," Duffy said.</p>
<p>In Rochester, most Friday evening departures and arrivals were cancelled, and Saturday's flights were listed on time as of late Friday, WXXI reports; Buffalo's airport was disrupted too, per WGRZ. Anyone flying this weekend should check with the airline before leaving for the airport. Airlines owe passengers on a cancelled flight a free rebooking or a refund, WXXI notes.</p>
</div></div>
<div class="wire"><div><h3>Reader Poll: When Should the Paper Arrive, 6&nbsp;a.m. or 8&nbsp;a.m.?</h3><p>The poll is still open, and one vote is in so far. The question is what time of the morning the Bulletin is sent to your phone: the link goes out by text at about 8 a.m. now, and it could instead be published and texted automatically at 6 a.m., so it is there when you get up. Pick one at <a href="https://tally.so/r/5XjVlv">tally.so/r/5XjVlv</a>; it takes ten seconds.</p></div></div>
<div class="wire"><div><h3>Wanted: Your Photos for the Cover</h3><p>Most covers are drawings because the album is short on pictures, so send two or three of yours (kids, pets, dinner, the view out the window) at <a href="https://tally.so/r/rjxDpl">tally.so/r/rjxDpl</a>. Each one runs at the top of the paper with your name under it.</p></div></div>
<h2 class="sec">The National Wire</h2>
<div class="wire"><div class="num">1</div><div><h3>Tanker Hits a Docked Riverboat in New Orleans</h3><p>A tanker, the Atlantic Asphalt, struck the docked paddlewheel cruise boat American Heritage about 12:30 p.m. Friday near the Port of New Orleans, leaving the riverboat on its side and largely underwater, CBS reports. Everyone was accounted for and no one died; Mayor Helena Moreno said 32 passengers were hospitalized, none in critical condition, and the Coast Guard's Capt. Melanie Burnham said, "There seems to be some type of a loss of steering."</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Trump, Putin and Xi to Sit Down Together</h3><p>President Trump, Russia's Vladimir Putin and China's Xi Jinping will hold the first three-way meeting among them Thursday in China, on the sidelines of an Asia-Pacific economic summit, the White House said Friday, according to CBS. Trump wants to talk about cutting nuclear arsenals and plans to raise the war in Iran, but Russia's war in Ukraine is not expected to come up, officials said.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Starship Reaches Orbit; Its Booster Does Not Come Home</h3><p>SpaceX's Starship, the world's biggest rocket, reached orbit Friday on its 15th test flight, but the booster that was supposed to fly back and be caught at the Texas launch pad aborted automatically and ended up in the Gulf of Mexico, PBS reports. The spacecraft itself is due to steer back toward the pad today for a first attempt at catching it.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>Update: Microsoft Is Back</h3><p>Microsoft said early Saturday that Outlook, Teams and Copilot are fully restored after the outage that led Friday's paper, the BBC reports. The outage reached more than 70 countries, and the company apologized.</p></div></div>
<h2 class="sec">The Home Wire</h2>
<div class="wire"><div class="num">1</div><div><h3>Chautauqua County &middot; Runners at the State Meet Today</h3><p>Chautauqua County runners race this morning at the state cross country championships at Queensbury High School, the <i>Observer</i> reports. The Clymer/Sherman/Panama boys, at the meet as a varsity team for the first time, are seeded first in Class D, the small-school division, in some pre-meet projections, coach Ray Shrout said.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Niagara-Wheatfield &middot; Coach "Ace" Cacciatore, 91</h3><p>Armand "Ace" Cacciatore, the Niagara-Wheatfield High School football and wrestling coach whose career ran four decades, died Wednesday at 91, the <i>Niagara Gazette</i> reports. The paper calls him one of the most successful and respected high school coaches in Western New York history, known to generations of athletes simply as "Coach."</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Niagara Falls &middot; The Falls by Helicopter, After Dark</h3><p>Rainbow Air Helicopter Tours began night flights over Niagara Falls on Friday, the first in its 32 years, the <i>Niagara Gazette</i> reports. They run Friday and Saturday evenings from 5 to 8:30 through March 13.</p></div></div>
<h2 class="sec">The Marquee</h2>
<div class="wire"><div class="num">1</div><div><h3>Journey's Drummer Steps Away</h3><p>Deen Castronovo, Journey's longtime drummer, is leaving the band's farewell tour "to focus on personal health matters," the group announced Friday, Billboard reports. Steve Murphy, a New York drummer who has played with Trans-Siberian Orchestra, fills in for the rest of November.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>The <i>Hunger Games</i> Author Speaks Up</h3><p>Suzanne Collins, who wrote <i>The Hunger Games</i> and stays out of the spotlight, posted a rare message to fans Friday praising the coming movie of her prequel, <i>Sunrise on the Reaping</i>, E! News reports. She called director Francis Lawrence's film "a vibrant and devastating adaptation of the novel."</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Tonight on TV: Mulaney Hosts <i>SNL</i></h3><p>John Mulaney hosts <i>Saturday Night Live</i> tonight, TVLine reports. Also on tonight: the singer Alex Warren hosts Nickelodeon's Kids' Choice Awards, and Hallmark has a new movie, <i>The Nights Before Christmas</i>.</p></div></div>
<h2 class="sec">The Gridiron</h2>
<div class="wire"><div><h3>Bills: The Line Gets Healthier</h3><p>Offensive linemen Dion Dawkins and Alec Anderson, who both missed Monday's game in Minnesota, practiced in full Friday and are set to play Sunday, and so is Connor McGovern, who has been dealing with a neck injury, Buffalo Rumblings reports. "This is a division game on the road, it's going to be as hard as it gets, right?" first-year coach Joe Brady said, according to the <i>Observer</i>.</p></div></div>
<div class="wire"><div><h3>Jets: Wilson Expected Back</h3><p>Coach Aaron Glenn said receiver Garrett Wilson has one step left in the concussion protocol, the league's checklist before a player can return from a head injury, and that he is confident Wilson will clear it and play against Buffalo, ProFootballTalk reports. Wilson missed last week's game; he has 43 catches for 527 yards and three touchdowns this season.</p></div></div>
''')
S('<p class="wlede">', '<div class="line"><span class="lbl t">Next 24 hours</span>', '''<p class="wlede">Cloudy and 37 at dawn, with flakes mixing in near Rochester; showers fill in from late morning</p>
<div class="wxrow">
  <div class="wxc"><div class="k">Tonight</div><div class="v">32&deg;</div><div class="s">showers likely</div></div>
  <div class="wxc"><div class="k">Wind</div><div class="v">7&ndash;12</div><div class="s">mph, northwest</div></div>
  <div class="wxc"><div class="k">Showers</div><div class="v">70%</div><div class="s">rain</div></div>
  <div class="wxc"><div class="k">Normal</div><div class="v">48&deg;</div><div class="s">for the date</div></div>
</div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">37<sup>&deg;</sup></div><div class="d">Cloudy<br>high 42&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">39<sup>&deg;</sup></div><div class="d">Cloudy<br>high 44&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">36<sup>&deg;</sup></div><div class="d">Rain, snow<br>high 41&deg;</div></div>
</div>
<div class="towns lakes">
  <div class="town"><div class="n">Lake Erie</div><div class="t">56<sup>&deg;</sup></div><div class="d">off Buffalo, Friday</div></div>
  <div class="town"><div class="n">Lake Ontario</div><div class="t">56<sup>&deg;</sup></div><div class="d">off Rochester, Friday</div></div>
</div>
<div class="strip5">
  <div><div class="d">Sat</div><div class="i">&#127783;</div><div class="h">42</div><div class="w">rain showers</div></div>
  <div><div class="d">Sun</div><div class="i">&#9729;</div><div class="h">45</div><div class="w">slight chance showers</div></div>
  <div><div class="d">Mon</div><div class="i">&#9925;</div><div class="h">49</div><div class="w">partly sunny</div></div>
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">53</div><div class="w">sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#9728;</div><div class="h">55</div><div class="w">sunny</div></div>
</div>
''')
S('<div class="line"><span class="lbl t">Next 24 hours</span>', '<h2 class="sec">The Almanac Sky</h2>', spark + '''<div class="line"><span class="lbl t">Outdoor window</span> Noon to 4 is the mildest stretch, at 42, but that is also when showers are likeliest. Tuesday and Wednesday turn sunny, in the 50s.</div>
<div class="line"><span class="lbl t">Frost watch</span> Back down to 32 here by early Sunday, with showers likely this evening.</div>
''')
S('<h2 class="sec">The Almanac Sky</h2>', '<h2 class="sec">Coming Up</h2>', '''<h2 class="sec">The Almanac Sky</h2>
<div class="wxrow">
  <div class="wxc"><div class="k">Moon</div><svg class="moonmini" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#5a4d3b"/><path d="M50 4 A46 46 0 0 1 50 96 A23.2 46 0 0 0 50 4Z" fill="#f4e5b4"/></svg><div class="s">waxing crescent</div></div>
  <div class="wxc"><div class="k">Sunrise</div><div class="v">7:06</div><div class="s">a.m.</div></div>
  <div class="wxc"><div class="k">Daylight</div><div class="v">9h 46m</div><div class="s">2 min less</div></div>
</div>
<p class="skynote"><b>Tonight:</b> the crescent, now a quarter lit, sits in Sagittarius and sets at 8:58, clouds permitting. Saturn is highest in the south around 9; Mars and Jupiter rise about 11:30. The full Beaver Moon is Nov. 24.</p>
<div class="touch-head">The Stars &middot; for fun</div>
<div class="stars slim">
<div class="star"><span class="sgn">Aries</span> <span class="who">Kaylani, Luka</span><br>Still a little friction in the air. Pick the chore that needs no one's opinion.</div>
<div class="star"><span class="sgn">Cancer</span> <span class="who">Gregg</span><br>The moon sits across from you again. Let the other person choose the channel.</div>
<div class="star"><span class="sgn">Leo</span> <span class="who">Leah, Tommy</span><br>A quiet sky for you. A rainy Saturday on the couch is fully approved.</div>
<div class="star"><span class="sgn">Virgo</span> <span class="who">Derek, Joanne</span><br>Things line up easily today. Make the list, then actually cross it off.</div>
<div class="star"><span class="sgn">Scorpio</span> <span class="who">Ariel, Claire, Garret</span><br>A friendly moon. Call the person you keep meaning to call.</div>
</div>
''')
S('<h2 class="sec">Coming Up</h2>', '<div class="dbl"><div class="a">', '''<h2 class="sec">Coming Up</h2>
<div class="calbox"><div class="calrow"><div class="cd">Tomorrow</div><div>Bills at Jets, 1:00</div></div>
<div class="calrow"><div class="cd">Wed</div><div>Central Michigan at UB, 7:30</div></div>
<div class="calrow"><div class="cd">Nov 22</div><div>Dolphins at Bills, 1:00; Jets at Chargers, 4:05</div></div>
<div class="calrow"><div class="cd">Nov 26</div><div>Thanksgiving; Chiefs at Bills, 8:20</div></div>
</div>
<h2 class="sec">The Ledger</h2>
<div class="ledger"><div class="num"><div class="cap">Days to the shortest day</div><div class="big">37</div></div>
<div class="txt">The winter solstice is Dec. 21. By then the day here will be 9 hours 1 minute long, 45 minutes shorter than today's. After that, it turns around.</div></div>
<h2 class="sec">On This Day</h2>
<div class="otd"><b>November 14, 1889</b> &mdash; The reporter Nellie Bly sailed from Hoboken, New Jersey, to try to beat the fictional trip in <i>Around the World in Eighty Days</i>. She was home in 72.</div>
<h2 class="sec">Question of the Day</h2>
<div class="qotd">I eat sticks for supper and grow taller with every bite, but one bucket of water puts me to bed. What am I? <i>Answer below the fold.</i></div>
''')
R('<b>Question of the Day:</b> A mailbox.', '<b>Question of the Day:</b> A campfire.')
S('headlines via ', ' &middot; scores and stats via Sportradar', 'headlines via CBS, the BBC, PBS, WXXI, WGRZ, the Dunkirk <i>Observer</i>, the <i>Niagara Gazette</i>, Billboard, E! News, TVLine, Buffalo Rumblings, ProFootballTalk')
ed = {'date': '2026-11-14', 'no': 143, 'body_html': src, 'plate_path': '/home/claude/plate143.jpg', 'plate_caption': 'Tending the fire',
      'headline': 'FAA ground stop · New Orleans riverboat collision · Bills at Jets tomorrow'}
for p in ['/home/claude/site/data/edition-2026-11-14.json', '/home/claude/edition-2026-11-14.json']:
    json.dump(ed, open(p, 'w'), ensure_ascii=False, indent=1)
print('ok', len(src))
