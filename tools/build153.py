import json, sys
sys.path.insert(0,'/home/claude'); sys.path.insert(0,'/home/claude/site/tools')
from curve import curve
from market_chart import market_chart
y = json.load(open('/home/claude/edition-2026-11-23.json'))['body_html']
f = json.load(open('/home/claude/site/data/forecast.json'))
m = json.load(open('/home/claude/site/data/market.json'))
def R(s, old, new):
    assert s.count(old) == 1, old[:60]
    return s.replace(old, new)
pre = y[:y.find('<div class="part">')]
pre = R(pre, 'No. 152', 'No. 153')
pre = R(pre, 'Monday &middot; November 23 &middot; 2026', 'Tuesday &middot; November 24 &middot; 2026')
pre = R(pre, '<div class="v">48&deg;</div><div class="k">Partly Sunny</div>', '<div class="v">39&deg;</div><div class="k">Mostly Sunny</div>')
pre = R(pre, '<div class="v">3</div><div class="k">Days to Thanksgiving</div>', '<div class="v">2</div><div class="k">Days to Thanksgiving</div>')
pre = R(pre, 'alt="A small boy pushing a hand truck loaded with a gray trash can down a store aisle"', 'alt="A doctored version of the 2024 Butler rally photo showing Nvidia CEO Jensen Huang raising a red bra beside an Nvidia flag"')
pre = R(pre, '<div class="plate-cap">Plate I &middot; The Family Album</div>', '<div class="plate-cap">The Cover</div>')
cap = open('/home/claude/site/spool/next/caption.txt').read().strip()
pre = R(pre, '<div class="plate-sub">Hand truck, trash can, aisle 28: one small man on a job.</div>', '<div class="plate-sub">'+cap.replace("'","&rsquo;")+'</div>')

BYLINE = '<div style="display:flex;gap:.8rem;align-items:center;margin:.5rem 0 .7rem"><img src="/assets/margo.jpg" alt="Margo Bentham, in ink" style="width:86px;height:86px;flex:none;border-radius:4px;border:1px solid var(--rule,#d3b88f)"><div><div style="font-family:\'Playfair Display\',Georgia,serif;font-weight:700;font-size:1.2rem;line-height:1.1">Margo Bentham</div><div style="font-family:Archivo,Arial,sans-serif;font-size:.6rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--teal,#2f5e3e);margin-top:.2rem">Editor-in-chief &middot; lead meteorologist</div><div style="font-style:italic;font-size:.85rem;color:var(--soft,#664a2c);margin-top:.3rem">Has never once been seen at the office.</div><div style="font-family:Archivo,Arial,sans-serif;font-size:.62rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;margin-top:.35rem"><a href="https://tally.so/r/EqxJpo">Ask Margo &rarr;</a></div></div></div>'

mkt = market_chart(m, year=2026)
news = '''<div class="part"><span>The News</span></div>
<h2 class="sec">The National Wire</h2>
<div class="wire lead"><div><span class="kick">The Lead</span><h3>Nvidia Takes Its Boss Back, and Trump Posts a Meme</h3><p>Nvidia reinstated Jensen Huang as chief executive on Monday, less than two weeks after he was forced to resign over revelations of extramarital affairs, one of them with a suspected Chinese spy, the BBC reports. The chipmaker's board had at first turned down his offer to return; President Trump says he "made the deal" to get Huang his job back, and both the president and the company are facing criticism from lawmakers.</p><p>Hours later, Trump posted the image on today's cover to Truth Social with no caption: a doctored version of the Associated Press photo of him after the 2024 shooting at his rally in Butler, Pennsylvania, with Huang in his place, holding up a red bra, GV Wire reports. In a CNBC interview Trump suggested the scandal could help Huang, saying, "Sex sells, fellas," and in a separate post called him "a Great Patriot and National Treasure."</p><p>Investors cheered the return. Nvidia's shares jumped 31 percent on Monday, adding almost $1 trillion to its value, the BBC reports.</p></div></div>
<div class="wire"><div><span class="num">1</span><h3>Update: The Iowa Blast Is Back On for Wednesday</h3><p>A federal appeals court on Monday declined to block the Army from detonating five tons of unstable explosives at a munitions plant in Iowa, and the Army says it will go ahead Wednesday morning, CBS reports. Environmental groups had warned the blast could send a plume of toxic lead into the surrounding area; the government says the material has become unstable and could explode on its own.</p></div></div>
<h2 class="sec">The Market</h2>
''' + mkt + '''
<p>Stocks came roaring back Monday: the S&amp;P 500 rose 4.7 percent and the Nasdaq gained 6.5 percent, CBS reports. Friday's sell-off had pushed the S&amp;P into a correction, a drop of 10 percent or more from its high; Monday's close leaves it about 7 percent below its October 6 peak, out of correction territory for now.</p>
<h2 class="sec">The Home Wire</h2>
<div class="wire"><div><span class="num">2</span><h3>Niagara Falls &middot; Budget Night at City Hall</h3><p>The Niagara Falls City Council meets today to consider amendments to Mayor Robert Restaino's proposed 2027 budget, the <i>Niagara Gazette</i> reports. The plan totals $107.6 million, $4.1 million more than this year's, with a separate $34.5 million capital budget.</p></div></div>
<div class="wire"><div><span class="num">3</span><h3>Buffalo &middot; Tops Lawsuit Against Social Media Dismissed</h3><p>New York's highest court, the Court of Appeals, rejected a lawsuit filed on behalf of victims and families of the 2022 Tops supermarket shooting that argued social media companies helped radicalize the gunman, WIVB reports. The ruling found the platforms are not liable, WGRZ reports.</p></div></div>
<div class="wire"><div><span class="num">4</span><h3>Webster &middot; The Town vs. the Reindeer</h3><p>The town of Webster has ordered Dennis McCormick to move the 20-foot inflatable reindeer outside his home on Holt Road, Rochester First reports. He says it's never been an issue, and he's weighing his options.</p></div></div>
<h2 class="sec">The Marquee</h2>
<div class="wire"><div><span class="num">5</span><h3>Adam Driver Joins the X-Men, as the Villain</h3><p>Adam Driver, Kylo Ren in the last "Star Wars" trilogy, told Seth Meyers about playing Mister Sinister, a shape-shifting, mind-reading scientist, the main villain in Marvel's upcoming "X-Men" film, Variety reports.</p></div></div>
<div class="wire"><div><span class="num">6</span><h3>Hila Klein Leaves the "H3 Podcast"</h3><p>Hila Klein is leaving the "H3 Podcast," a month after it came out that her husband and co-host, Ethan Klein, had a six-month affair, Variety reports. "I'm devastated that things have come to this," she said in a post on the show's Instagram.</p></div></div>
<div class="wire"><div><span class="num">7</span><h3>Tonight on TV</h3><p>"Dancing With the Stars" hands out the Mirrorball trophy in its finale tonight, and a new Miss Universe is crowned, TVLine reports.</p></div></div>
<h2 class="sec">The Gridiron</h2>
<div class="wire"><div><h3>Bills: The One Seed Is in Reach</h3><p>With the Jaguars and Bengals both losing this week, the Bills can lock up the AFC's top seed, which has eluded them throughout Josh Allen's career, by winning the rest of their conference games, Buffalo Rumblings reports. The Bengals fell 22&ndash;20 to the Commanders on a last-second field goal Monday night, ProFootballTalk reports. Before Thursday's game, the team will honor restaurateur Russell Salvatore, a longtime supporter, WGRZ reports.</p></div></div>
<div class="wire"><div><h3>Jets: A Win, and an Argument</h3><p>Sunday's win in Los Angeles was the Jets' first in five weeks, and Gang Green Nation reports the fan base is split between enjoying it and worrying about draft position. Next: at Miami on Sunday.</p></div></div>
<div class="wire"><div><h3>The Sunday Tax &middot; Week 12</h3><p>Josh won Week 11 with 11 right and takes the $85 pot. Week 12 is open: picks at <a href="https://tally.so/r/RGOakJ">tally.so/r/RGOakJ</a>, standings at <a href="https://benthambulletin.github.io/pool/">benthambulletin.github.io/pool</a>. $5 a week, straight-up winners, the pot to the best record, and anyone with the link can play. Sheets lock at each kickoff; first game Wednesday at 8, Packers at Rams.</p></div></div>
'''
hourly = f['towns']['North Tonawanda']['hourly']
crv = curve(hourly, 7*60+18, 16*60+45)
alm = '''<div class="part"><span>The Almanac</span></div>
<h2 class="sec">The Weather Glass</h2>
''' + BYLINE + '''
<p class="wlede">Sun's out, warmth isn't. Upper 30s, barely a breeze, and 24 tonight. Bring the hoses in or buy new ones in April.</p>
<div class="touch-head" style="margin-top:1.1rem">Turkey Trot Watch &middot; Thursday 6 a.m. to noon</div>
<p>Day two, and the forecast is holding. For North Tonawanda, the weather service still has the rain waiting until after 1 p.m. Thursday, now with a 70 percent chance once it comes, under cloudy skies with a high near 43. Wednesday night bottoms out around 29, and the east wind picks up Thursday, 7 to 15 mph with gusts as high as 30. Translation for the six of you: it's dry for the race and cold at the start, so dress for the 30s and the wind, not the high. And Thursday night is a soaker, so whoever's driving home from Derek's, take it easy.</p>
<div class="touch-head" style="margin-top:1.1rem">Today</div>
<div class="wxrow">
  <div class="wxc"><div class="k">Tonight</div><div class="v">24&deg;</div><div class="s">partly cloudy</div></div>
  <div class="wxc"><div class="k">Wind</div><div class="v">3&ndash;7</div><div class="s">mph, northwest</div></div>
  <div class="wxc"><div class="k">Rain</div><div class="v">None</div><div class="s">till Thursday p.m.</div></div>
  <div class="wxc"><div class="k">Normal</div><div class="v">44&deg;</div><div class="s">for the date</div></div>
</div>
<div class="line"><span class="lbl t">Next 24 hours</span></div>''' + crv + '''
<div class="line"><span class="lbl t">Records</span> Buffalo's for the date: 65 in 2001 and 2014; 8 in 1938. A year ago: 47 and 30.</div>
<div class="touch-head" style="margin-top:1.1rem">This week</div>
<div class="strip5">
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">39</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#9728;</div><div class="h">43</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Thu</div><div class="i">&#127783;</div><div class="h">43</div><div class="w">rain after 1</div></div>
  <div><div class="d">Fri</div><div class="i">&#127783;</div><div class="h">45</div><div class="w">rain showers</div></div>
  <div><div class="d">Sat</div><div class="i">&#127782;</div><div class="h">47</div><div class="w">chance showers</div></div>
</div>
<div class="line"><span class="lbl t">Outdoor window</span> Today and Wednesday, both mostly sunny and dry. Get the leaves and the lights done before Thursday afternoon.</div>
<div class="line"><span class="lbl t">Frost watch</span> 24 tonight in North Tonawanda, cold enough for a hard freeze. Wednesday night, 29.</div>
<div class="touch-head" style="margin-top:1.1rem">Around us &middot; at dawn</div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">34<sup>&deg;</sup></div><div class="d">Partly cloudy<br>high 39&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">36<sup>&deg;</sup></div><div class="d">Mostly cloudy<br>high 39&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">34<sup>&deg;</sup></div><div class="d">Mostly clear<br>high 39&deg;</div></div>
</div>
<div class="towns lakes">
  <div class="town"><div class="n">Lake Erie</div><div class="t">53<sup>&deg;</sup></div><div class="d">off Buffalo</div></div>
  <div class="town"><div class="n">Lake Ontario</div><div class="t">54<sup>&deg;</sup></div><div class="d">off Rochester</div></div>
</div>
<div class="line" style="margin-top:.4rem"><span class="lbl t">Snow so far</span> since July 1, through Monday. Still nothing measured anywhere.</div>
<div class="towns snow"><div class="town"><div class="n">North Tonawanda</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 4.5"</div></div><div class="town"><div class="n">Orchard Park</div><div class="t">n/a</div><div class="d">normal 6.1"</div></div><div class="town"><div class="n">Dunkirk</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 6.1"</div></div><div class="town"><div class="n">Scottsville</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 5.6"</div></div></div>
<h2 class="sec">The Almanac Sky</h2>
<div class="wxrow">
  <div class="wxc"><div class="k">Moon</div><svg class="moonmini" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#f4e5b4"/></svg><div class="s">full</div></div>
  <div class="wxc"><div class="k">Sunrise</div><div class="v">7:18</div><div class="s">a.m.</div></div>
  <div class="wxc"><div class="k">Daylight</div><div class="v">9h 26m</div><div class="s">2 min less</div></div>
</div>
<p class="skynote"><b>Tonight:</b> the full moon of November, the Beaver Moon, rises at 4:26 this afternoon in Taurus and stays up until 8:52 Wednesday morning. Saturn is the evening's only bright planet, highest in the south around 9; Jupiter rises at 11 and Mars just after. The next new moon is December 8.</p>
<div class="touch-head">The Stars &middot; for fun</div>
<div class="stars slim">
<div class="star"><span class="sgn">Aries</span> <span class="who">Kaylani, Luka</span><br>A chatty Gemini moon is on your side. Talk your way into the last roll.</div>
<div class="star"><span class="sgn">Cancer</span> <span class="who">Gregg</span><br>The moon has nothing for you today. Rest up for the in-laws.</div>
<div class="star"><span class="sgn">Leo</span> <span class="who">Leah, Tommy</span><br>A friendly moon. Good day to buy the salad stuff without a lecture.</div>
<div class="star"><span class="sgn">Virgo</span> <span class="who">Derek, Joanne</span><br>A tense angle for the hosts. Make one list, not four.</div>
<div class="star"><span class="sgn">Scorpio</span> <span class="who">Ariel, Claire, Garret</span><br>Nothing in the sky aimed at you. Taper. Thursday's coming.</div>
</div>
<h2 class="sec">Coming Up</h2>
<div class="calbox"><div class="calrow"><div class="cd">Tonight</div><div>Full moon, the Beaver Moon</div></div>
<div class="calrow"><div class="cd">Thu</div><div>Thanksgiving. Turkey Trot downtown, 9:00; at Derek's, appetizers 1, dinner 3; Chiefs at Bills, 8:20</div></div>
<div class="calrow"><div class="cd">Sun</div><div>Jets at Dolphins, 1:00</div></div>
<div class="calnote">Migraine log: nothing new since Joanne's on Sunday. Four this month.</div>
</div>
<h2 class="sec">On This Day</h2>
<div class="otd">OTDTEXT</div>
<h2 class="sec">Question of the Day</h2>
<div class="qotd">QOTDQ <i>Answer below the fold.</i></div>
<div class="dbl"><div class="a"></div><div class="b"></div></div>
<div class="colo"><div class="s" style="margin-bottom:8px"><b>Question of the Day:</b> QOTDA</div>
<div class="s">Forecast, lake temperatures and radar per NWS Buffalo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; normals from NOAA &middot; sky computed for 14120 &middot; headlines via the BBC, CBS, GV Wire, WIVB, WGRZ, Rochester First, the <i>Niagara Gazette</i>, Variety, TVLine, ProFootballTalk, Buffalo Rumblings, Gang Green Nation &middot; S&amp;P 500 closes via Yahoo Finance &middot; On This Day per OTDSRC &middot; snow and records via ACIS &middot; scores via Sportradar</div>
<div class="ask"><a href="https://tally.so/r/rjxDpl">Send something to the paper</a> &middot; <a href="https://tally.so/r/obWNYP">Log a migraine</a> &middot; <a href="https://tally.so/r/EqxJpo">Ask Margo</a></div>
<div class="sig">&mdash; Margo</div><div class="orn">&#127809; &#127810; &#127809;</div></div>
'''
import otd153
for k,v in otd153.T.items(): alm = alm.replace(k, v)
body = pre + news + alm
ed = {'date':'2026-11-24','no':153,'body_html':body,'plate_path':'/home/claude/plate153.jpg','plate_caption':cap,'headline':'Nvidia takes Huang back and Trump posts a meme · Stocks rally · Turkey Trot rain holds off'}
for p in ('/home/claude/edition-2026-11-24.json','/home/claude/site/data/edition-2026-11-24.json'):
    json.dump(ed, open(p,'w'), ensure_ascii=False)
print('ok', len(body))
