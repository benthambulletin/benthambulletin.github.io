import json, sys
sys.path.insert(0, '/home/claude'); from curve import curve
src = json.load(open('/home/claude/site/data/edition-2026-11-19.json'))['body_html']
def R(a, c, n=1):
    global src
    assert src.count(a) == n, ('R', a[:60], src.count(a)); src = src.replace(a, c)
def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50]); src = src[:i] + new + src[j:]
f = json.load(open('/home/claude/site/data/forecast.json'))
assert f['generated_utc'].startswith('2026-11-20')
assert [f['towns'][n]['observation']['temp_f'] for n in ['North Tonawanda', 'Dunkirk', 'Scottsville']] == [48, 55, 43]
assert f['lakes']['readings'] == {'Lake Erie (Buffalo)': 54, 'Lake Ontario (Rochester)': 55} and 'Thu Nov 19 2026 The water temperature off Buffalo' in f['lakes']['text']
hourly = f['towns']['North Tonawanda']['hourly']; assert 'T05:00' in hourly[0]['start']
chart = curve(hourly, 7 * 60 + 14, 16 * 60 + 47)
COVER = json.load(open('/home/claude/cover149.json'))
i = src.find('<img src="__PLATE__"'); j = src.find('>', i) + 1; assert i > 0
src = src[:i] + '<img src="__PLATE__" alt="%s">' % COVER['alt'] + src[j:]
i = src.find('<div class="plate-sub">'); j = src.find('</div>', i) + 6; src = src[:i] + '<div class="plate-sub">%s</div>' % COVER['caption'] + src[j:]
R('<div class="plate-cap">Plate I &middot; The Family Album</div>', '<div class="plate-cap">The Cover</div>')
R('No. 148', 'No. 149'); R('Thursday &middot; November 19 &middot; 2026', 'Friday &middot; November 20 &middot; 2026')
S('<div class="tiles">', '<div class="plate-wrap">', '''<div class="tiles">
  <div class="tile"><div class="v">59&deg;</div><div class="k">Sunny</div></div>
  <div class="tile"><div class="v">4:47</div><div class="k">Sunset</div></div>
  <div class="tile urg"><div class="v">6</div><div class="k">Days to Thanksgiving</div></div>
</div>
''')
S('<div class="wire lead">', '<div class="part"><span>The Almanac</span></div>', '''<div class="wire lead"><div><span class="kick">The Lead</span><h3>No Bill Will Wear 83 Again</h3>
<p>The Buffalo Bills will retire Andre Reed's number, 83, during the 2027 season, the team announced Thursday, the Associated Press reports in the Dunkirk <i>Observer</i>. Retiring a number means no Bills player will be issued it again.</p>
<p>The team shared a video of owner Terry Pegula breaking the news to Reed in person. "I can still see you going over the middle, getting knocked around, hanging onto the ball," Pegula told him. Jim Kelly and Thurman Thomas, his old teammates and fellow Hall of Famers, walked in wearing copies of his jersey.</p>
<p>Reed, a wide receiver, played 15 of his 16 seasons in Buffalo and was a mainstay of the teams that went to four straight Super Bowls in the 1990s. He finished with 951 catches for 13,198 yards and went into the Pro Football Hall of Fame in 2014. The team has not yet said which game next season will hold the ceremony, Buffalo Rumblings reports.</p>
<div class="pull">"Long time coming, man."<br>&mdash; Thurman Thomas, to Andre Reed</div>
</div></div>
<h2 class="sec">Family Today</h2>
<div class="pnote" style="border:1px solid var(--rule,#d3b88f);padding:.6rem .75rem"><b>From the Group Chat &middot; Gregg</b><br>"Yesterday's question was really good. I didn't get it."</div>
<h2 class="sec">The National Wire</h2>
<div class="wire"><div class="num">1</div><div><h3>Fiona the Hippo Has Died</h3><p>Fiona, the Cincinnati Zoo hippopotamus who became famous after her premature birth in 2017, died Thursday, days after swallowing a knit hat that landed in her enclosure, CBS reports. The zoo said a visitor had tossed the hat in the air and a ceiling fan flung it in; she would have turned 10 in January.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>A Pardon for Pete Rose</h3><p>President Trump on Thursday pardoned Pete Rose, baseball's career hits leader, who died in 2024 at 83, the BBC reports. Rose pleaded guilty in 1990 to filing false tax returns and was banned from baseball for betting on games; the league lifted that ban last year, which made him eligible for the Hall of Fame.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>The Army Puts Off a Risky Blast in Iowa</h3><p>The Army has delayed until Monday its plan to blow up unstable explosives at an ammunition plant in Middletown, Iowa, CBS reports; it had been set for noon today. Elected officials and environmental groups had warned that the blast could send a cloud of dust carrying toxic lead across parts of Iowa and Illinois.</p></div></div>
<h2 class="sec">The Home Wire</h2>
<div class="wire"><div class="num">1</div><div><h3>Finger Lakes &middot; A Measles Warning in Geneva</h3><p>Anyone who visited Geneva General Hospital between 11:30 a.m. Monday and 4:45 p.m. Tuesday may have been exposed to measles, WXXI reports, after a patient there tested positive. Ontario County health officials say those visitors should check their vaccination records and watch for symptoms through Dec. 8.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Fredonia &middot; SUNY Grows, but Not Here</h3><p>Enrollment across the state university system rose for the fourth year in a row, to 392,401 students, but SUNY Fredonia and Buffalo State are still shrinking, WKBW reports. "I continue to worry about Buffalo State and Fredonia," Chancellor John King told the station.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Niagara Falls &middot; Tips by Text, No Name Needed</h3><p>Niagara Falls police have set up an anonymous tip line, WKBW reports: anyone can text 716-804-4000 without giving a name. Police say it is meant for people who know something that could help a case but are afraid to come forward.</p></div></div>
<h2 class="sec">The Marquee</h2>
<div class="wire"><div class="num">1</div><div><h3>Grand Theft Auto 6 Arrives, and Breaks Records</h3><p>The video game <i>Grand Theft Auto 6</i> came out Thursday after a 13-year wait and is estimated to be the biggest entertainment launch in history, the BBC reports. Advance orders and first-day sales came to more than 24.5 million copies, about $2.36 billion, by the count of the research firm Sensor Tower.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>A New <i>Hunger Games</i> Opens Today</h3><p><i>The Hunger Games: Sunrise on the Reaping</i>, a prequel taken from Suzanne Collins's novel of last year, opens in 3,900 North American theaters today, the Hollywood Reporter says. The studio projects more than $80 million for the weekend, and the trade paper's sources expect it to pass $100 million.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Martin Short and the Wedding Cake</h3><p>On <i>Jimmy Kimmel Live</i>, Martin Short admitted he took a fork to a cake at Selena Gomez's wedding, thinking each group of guests had its own; it was the wedding cake, Rolling Stone reports. "I love the teeth marks of the fork where he tried to save it," Gomez said.</p></div></div>
<h2 class="sec">The Gridiron</h2>
<div class="wire"><div><h3>Bills: Four Sit Out Thursday</h3><p>Cornerback Christian Benford, tight end Dalton Kincaid, linebacker Dorian Williams and safety Damar Hamlin did not practice Thursday, Buffalo Rumblings reports, three days before the Dolphins come to Orchard Park. Cornerback Dee Alford, coming back from a concussion, moved up to limited work, and guard O'Cyrus Torrence returned.</p></div></div>
<div class="wire"><div><h3>Jets: Smith Plans to Start</h3><p>Quarterback Geno Smith said the plan is for him to start Sunday against the Chargers in Los Angeles, Gang Green Nation reports, though ESPN's Rich Cimini noted he was walking with a limp on Wednesday.</p></div></div>
<div class="wire"><div><h3>Thursday Night: Texans 26, Colts 3</h3><p>C.J. Stroud threw three touchdown passes and Houston outgained Indianapolis 355 yards to 167, ProFootballTalk reports.</p></div></div>
''')
S('<p class="wlede">', '<div class="line"><span class="lbl t">Next 24 hours</span>', '''<p class="wlede">Sunshine from start to finish, and a light west wind</p>
<div class="wxrow">
  <div class="wxc"><div class="k">Tonight</div><div class="v">37&deg;</div><div class="s">mostly clear</div></div>
  <div class="wxc"><div class="k">Wind</div><div class="v">5&ndash;9</div><div class="s">mph, west</div></div>
  <div class="wxc"><div class="k">Rain</div><div class="v">None</div><div class="s">until Sunday night</div></div>
  <div class="wxc"><div class="k">Normal</div><div class="v">46&deg;</div><div class="s">for the date</div></div>
</div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">48<sup>&deg;</sup></div><div class="d">Clear<br>high 59&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">55<sup>&deg;</sup></div><div class="d">Partly cloudy<br>high 57&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">43<sup>&deg;</sup></div><div class="d">Mostly clear<br>high 61&deg;</div></div>
</div>
<div class="towns lakes">
  <div class="town"><div class="n">Lake Erie</div><div class="t">54<sup>&deg;</sup></div><div class="d">off Buffalo, Thursday</div></div>
  <div class="town"><div class="n">Lake Ontario</div><div class="t">55<sup>&deg;</sup></div><div class="d">off Rochester, Thursday</div></div>
</div>
<div class="strip5">
  <div><div class="d">Fri</div><div class="i">&#9728;</div><div class="h">59</div><div class="w">sunny</div></div>
  <div><div class="d">Sat</div><div class="i">&#9728;</div><div class="h">63</div><div class="w">sunny</div></div>
  <div><div class="d">Sun</div><div class="i">&#9728;</div><div class="h">63</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Mon</div><div class="i">&#127783;</div><div class="h">47</div><div class="w">early rain chance</div></div>
  <div><div class="d">Tue</div><div class="i">&#9925;</div><div class="h">37</div><div class="w">partly sunny</div></div>
</div>
''')
S('<div class="line"><span class="lbl t">Next 24 hours</span>', '<h2 class="sec">The Almanac Sky</h2>', '<div class="line"><span class="lbl t">Next 24 hours</span></div>' + chart + '''<div class="line"><span class="lbl t">Outdoor window</span> All day. Mid-50s by late morning, upper 50s through the afternoon.</div>
<div class="line"><span class="lbl t">Frost watch</span> Close tonight: 37 in North Tonawanda, 35 in Scottsville. Monday night drops to 30.</div>
''')
S('<h2 class="sec">The Almanac Sky</h2>', '<h2 class="sec">Coming Up</h2>', '''<h2 class="sec">The Almanac Sky</h2>
<div class="wxrow">
  <div class="wxc"><div class="k">Moon</div><svg class="moonmini" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#5a4d3b"/><path d="M50 4 A46 46 0 0 1 50 96 A28.2 46 0 0 1 50 4Z" fill="#f4e5b4"/></svg><div class="s">waxing gibbous</div></div>
  <div class="wxc"><div class="k">Sunrise</div><div class="v">7:14</div><div class="s">a.m.</div></div>
  <div class="wxc"><div class="k">Daylight</div><div class="v">9h 34m</div><div class="s">2 min less</div></div>
</div>
<p class="skynote"><b>Tonight:</b> the moon, 81 percent lit, rises at 2:16 this afternoon and is up until 2:27 a.m., still in Pisces. Saturn is the one bright planet of the evening, highest in the south around 9. Mars and Jupiter rise after 11. Full moon Tuesday.</p>
<div class="touch-head">The Stars &middot; for fun</div>
<div class="stars slim">
<div class="star"><span class="sgn">Aries</span> <span class="who">Kaylani, Luka</span><br>The moon moves into your sign and brings stern old Saturn along. Big energy, with a bedtime.</div>
<div class="star"><span class="sgn">Cancer</span> <span class="who">Gregg</span><br>The moon is at a cross angle to you. If the riddle wins again, blame the sky.</div>
<div class="star"><span class="sgn">Leo</span> <span class="who">Leah, Tommy</span><br>A fellow fire sign has the moon, and it suits you. Start the thing.</div>
<div class="star"><span class="sgn">Virgo</span> <span class="who">Derek, Joanne</span><br>The moon has moved on from across the way. You may have the wheel back.</div>
<div class="star"><span class="sgn">Scorpio</span> <span class="who">Ariel, Claire, Garret</span><br>Nothing aimed at you today. A quiet Friday is not a trick.</div>
</div>
''')
S('<h2 class="sec">Coming Up</h2>', '<div class="dbl"><div class="a">', '''<h2 class="sec">Coming Up</h2>
<div class="calbox"><div class="calrow"><div class="cd">Sun</div><div>Dolphins at Bills, 1:00; Jets at Chargers, 4:05</div></div>
<div class="calrow"><div class="cd">Nov 26</div><div>Thanksgiving; Chiefs at Bills, 8:20</div></div>
<div class="calrow"><div class="cd">Nov 27</div><div>UB at Akron, noon</div></div>
<div class="calnote">Migraine log: nothing new since Joanne's on Monday. Four this month.</div>
</div>
<h2 class="sec">The Ledger</h2>
<div class="ledger"><div class="num"><div class="cap">FeedMore WNY's new warehouse in Hamburg</div><div class="big">200,000 square feet</div></div>
<div class="txt">It opened Thursday, WKBW reports, and replaces two Buffalo buildings the food bank had outgrown.</div></div>
<h2 class="sec">On This Day</h2>
<div class="otd"><b>November 20, 1985</b> &mdash; Microsoft released Windows 1.0. Most people kept typing commands for a few more years.</div>
<h2 class="sec">Question of the Day</h2>
<div class="qotd">I hang around the closet all day and hold your shape while you are out of it. What am I? <i>Answer below the fold.</i></div>
''')
R('<b>Question of the Day:</b> Fog.', '<b>Question of the Day:</b> A coat hanger.')
S('headlines via ', ' &middot; scores and stats via Sportradar', 'headlines via CBS, the BBC, the Dunkirk <i>Observer</i>, WXXI, WKBW, the Hollywood Reporter, Rolling Stone, ProFootballTalk, Buffalo Rumblings, Gang Green Nation')
ed = {'date': '2026-11-20', 'no': 149, 'body_html': src, 'plate_path': COVER['path'], 'plate_caption': COVER['caption'],
      'headline': "The Bills will retire Andre Reed's 83 · Fiona the hippo dies · Grand Theft Auto 6 breaks records"}
for p in ['/home/claude/site/data/edition-2026-11-20.json', '/home/claude/edition-2026-11-20.json']:
    json.dump(ed, open(p, 'w'), ensure_ascii=False, indent=1)
print('ok', len(src))
