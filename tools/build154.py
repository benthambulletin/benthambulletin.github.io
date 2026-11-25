import json, sys, re
sys.path.insert(0,'/home/claude'); sys.path.insert(0,'/home/claude/site/tools')
from curve import curve
y = json.load(open('/home/claude/edition-2026-11-24.json'))['body_html']
f = json.load(open('/home/claude/site/data/forecast.json'))
def R(s, old, new):
    assert s.count(old) == 1, old[:60]
    return s.replace(old, new)
pre = y[:y.find('<div class="part">')]
pre = R(pre, 'No. 153', 'No. 154')
pre = R(pre, 'Tuesday &middot; November 24 &middot; 2026', 'Wednesday &middot; November 25 &middot; 2026')
pre = R(pre, '<div class="v">39&deg;</div><div class="k">Mostly Sunny</div>', '<div class="v">42&deg;</div><div class="k">Mostly Sunny</div>')
pre = R(pre, '<div class="v">4:45</div><div class="k">Sunset</div>', '<div class="v">4:44</div><div class="k">Sunset &middot; 1 min less</div>')
pre = R(pre, '<div class="v">2</div><div class="k">Days to Thanksgiving</div>', '<div class="v">1</div><div class="k">Day to Thanksgiving</div>')
pre = R(pre, 'alt="A doctored version of the 2024 Butler rally photo showing Nvidia CEO Jensen Huang raising a red bra beside an Nvidia flag"', 'alt="The front of the Buffalo Convention Center, white and blue panels with BUFFALO CONVENTION CENTER in blue letters"')
cap = 'The Buffalo Convention Center, the new start and finish of Thursday&rsquo;s Turkey Trot. File photo, 2023. Photo: Kenneth C. Zirkel, <a href="https://commons.wikimedia.org/wiki/File:Buffalo_Convention_Center_after_renovations.jpg">CC BY 4.0</a>.'
s0 = pre.find('<div class="plate-sub">'); s1 = pre.find('</div>', s0)
pre = pre[:s0] + '<div class="plate-sub">' + cap + pre[s1:]

BYLINE = '<div style="display:flex;gap:.8rem;align-items:center;margin:.5rem 0 .7rem"><img src="/assets/margo.jpg" alt="Margo Bentham, in ink" style="width:86px;height:86px;flex:none;border-radius:4px;border:1px solid var(--rule,#d3b88f)"><div><div style="font-family:\'Playfair Display\',Georgia,serif;font-weight:700;font-size:1.2rem;line-height:1.1">Margo Bentham</div><div style="font-family:Archivo,Arial,sans-serif;font-size:.6rem;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:var(--teal,#2f5e3e);margin-top:.2rem">Editor-in-chief &middot; lead meteorologist</div><div style="font-style:italic;font-size:.85rem;color:var(--soft,#664a2c);margin-top:.3rem">Has never once been seen at the office.</div><div style="font-family:Archivo,Arial,sans-serif;font-size:.62rem;font-weight:800;letter-spacing:.12em;text-transform:uppercase;margin-top:.35rem"><a href="https://tally.so/r/EqxJpo">Ask Margo &rarr;</a></div></div></div>'

box = open('/home/claude/site/spool/trot/box-template.html').read()
box = R(box, 'Dry for the race. Cold and windy. Rain after 1.', 'Dry for the race. Cold, and windier. Rain after 1.')
box = R(box, '<li><b>Race morning, 6 to noon:</b> cloudy and dry, mid-30s at the start, low 40s by late morning.</li>', '<li><b>Race morning, 6 to noon:</b> cloudy and dry. Wednesday night&rsquo;s low is 28 and Thursday&rsquo;s high is 42, so figure the mid-30s at the 9:00 start.</li>')
box = R(box, '<li><b>Wind:</b> east 8 to 15 mph, gusts up to 30. Feels colder than it reads.</li>', '<li><b>Wind:</b> northeast 9 to 20 mph, gusts as high as 37. Feels colder than it reads.</li>')
box = R(box, '<li><b>Rain:</b> after 1 p.m., 70% chance, a tenth to a quarter inch.</li>', '<li><b>Rain:</b> after 1 p.m., 90% chance, a quarter to half an inch by dark.</li>')
box = R(box, '<li><b>Thursday night:</b> a soaker, half to three-quarters of an inch. Easy on the drive home from Derek&#39;s.</li>' if '&#39;' in box else "<li><b>Thursday night:</b> a soaker, half to three-quarters of an inch. Easy on the drive home from Derek's.</li>", '<li><b>Thursday night:</b> rain, 1 to 2 inches, gusts to 36, low 35. Easy on the drive home from Derek&rsquo;s.</li>')
box = R(box, 'Since yesterday: no change to the timing.', 'Since yesterday: rain odds up to 90 from 70, gusts up to 37 from 30, and the wind swung around to the northeast. Timing hasn&rsquo;t budged.')
box = R(box, 'Thursday, 9 a.m., Franklin St.', 'Thursday, 9 a.m., Franklin St. &middot; North Tonawanda forecast')

am = open('/home/claude/site/spool/trot/askmargo-kaylani.md').read()
kq = am.split('**Kaylani asks:**')[1].split('**Margo:**')[0].strip()
ka = am.split('**Margo:**')[1].strip()
ka = R(ka, 'an east wind gusting to 30', 'a northeast wind gusting to 37')
ka = R(ka, 'A 131-year-old race', 'A 130-year-old race')
ka = ka.replace("'", '&rsquo;')
paras = ''.join('<p>'+p.strip()+'</p>' for p in ka.split('\n\n') if p.strip())
askm = '<h2 class="sec">Ask Margo</h2>\n<p><b>Kaylani asks:</b> <i>' + kq.replace("'", '&rsquo;') + '</i></p>\n' + paras + '\n'

guide = open('/home/claude/site/spool/trot/guide.html').read()

news = '''<div class="part"><span>The News</span></div>
''' + box + '''
<h2 class="sec">The National Wire</h2>
<div class="wire lead"><div><span class="kick">The Lead</span><h3>Kilmar &Aacute;brego Garc&iacute;a Leaves for Spain</h3><p>Kilmar &Aacute;brego Garc&iacute;a, the Maryland man whose wrongful deportation to El Salvador last year became a flashpoint in the fight over President Trump&rsquo;s immigration agenda, has left the United States for Spain, the BBC reports. He came to the U.S. illegally from El Salvador as a teenager and is married to a U.S. citizen.</p><p>The government admitted it had sent him to El Salvador by mistake and brought him back, but only to face human trafficking charges, which were later dropped, the BBC reports. The administration then kept trying to send him to other countries, including Uganda and Ghana.</p><p>Senator Chris Van Hollen, the Maryland Democrat who visited him in El Salvador&rsquo;s Cecot prison in 2025, said in a statement Tuesday:</p><div class="pull">&ldquo;Today, Kilmar is travelling to a country of his choice, a free man &ndash; unharmed and with dignity.&rdquo;</div></div></div>
<div class="wire"><div><span class="num">2</span><h3>Huawei Guilty of Stealing Trade Secrets</h3><p>A federal jury in Brooklyn found the Chinese telecom giant Huawei guilty on 10 of 12 counts, including conspiracy to steal trade secrets, bank fraud and conspiracy to violate U.S. sanctions, after a two-month trial, the BBC reports. Jurors acquitted it of the most serious charge, racketeering conspiracy, which would have required finding the company acted like a criminal enterprise; Huawei said it would take all necessary legal action to defend itself.</p></div></div>
<div class="wire"><div><span class="num">3</span><h3>Six Dead in Plane Crash off Mississippi</h3><p>Six people, four adults and two boys aged 8 and 10, were found dead Tuesday after a small plane went down in the Gulf of Mexico between Pascagoula, Mississippi, and Horn Island, the Coast Guard says. The Cessna 210 was flying from New Orleans to Fort Myers, Florida, when air traffic control lost contact with it at about 3:45 p.m., CBS and the BBC report.</p></div></div>
<h2 class="sec">Family Today</h2>
<p>Tommy and Leah: the paper hasn&rsquo;t heard from you in a while. Send a photo, a date or a gripe through the form at <a href="https://tally.so/r/rjxDpl">tally.so/r/rjxDpl</a>.</p>
<h2 class="sec">The Home Wire</h2>
<div class="wire"><div><span class="num">4</span><h3>Niagara Falls &middot; Dispatcher Disciplined Over 911 Call</h3><p>A Niagara Falls police dispatcher was disciplined in August over the handling of an emergency call reportedly placed about a half hour before a woman was fatally shot on Highland Avenue over the Fourth of July weekend, the <i>Niagara Gazette</i> reports. In a letter to the resident who complained, the department&rsquo;s office of professional standards said the allegations, about &ldquo;courtesy and communication responsibilities,&rdquo; were sustained.</p></div></div>
<div class="wire"><div><span class="num">5</span><h3>Fredonia &middot; Back to Dunkirk for Water?</h3><p>Two Fredonia village trustees, Tim Mulholland and LeeAnn Lazarony, want to halt the plan to get water from the North County Water District through Pomfret and instead revisit connecting directly to the city of Dunkirk, the Dunkirk <i>Observer</i> reports. The board approved a direct Dunkirk link in December 2023, but residents sued and stopped it; the Pomfret plan has since stalled over funding.</p></div></div>
<div class="wire"><div><span class="num">6</span><h3>Chautauqua County &middot; Ten Measles Cases</h3><p>Chautauqua County has had 10 reported measles cases, the county&rsquo;s Board of Health heard, and the state&rsquo;s count hadn&rsquo;t risen as of Tuesday morning, the <i>Observer</i> reports. The county&rsquo;s public health director, Lacey Wilson, asks anyone who suspects measles to call a doctor first rather than go straight to the emergency room, to avoid exposing others.</p></div></div>
<h2 class="sec">The Marquee</h2>
<div class="wire"><div><span class="num">7</span><h3>&ldquo;The Buffalo Miracle&rdquo; Is on HBO</h3><p>&ldquo;The Buffalo Miracle,&rdquo; a documentary about the people who helped one another through the deadly Christmas 2022 blizzard, debuted Tuesday night on HBO, WKBW reports. It&rsquo;s from two-time Oscar-winning director Ben Proudfoot, with Josh Allen as an executive producer through his new production company; a suburban McDonald&rsquo;s is the centerpiece.</p></div></div>
<div class="wire"><div><span class="num">8</span><h3>A Jamestown Girl on the Big Screen</h3><p>&ldquo;Hershey,&rdquo; the new movie about chocolate maker Milton Hershey, opens this week, and Catherine Hershey, his wife, was a Jamestown native, the <i>Observer</i> reports. Milton met her on a chance visit to a Jamestown candy shop; Alexandra Daddario spoke to students at the Nov. 15 premiere at the Milton Hershey School.</p></div></div>
<div class="wire"><div><span class="num">9</span><h3>2 Chainz Breaks Ribs in Cybertruck Crash</h3><p>Rapper 2 Chainz says he&rsquo;s resting with broken ribs after a head-on crash that totaled his orange Tesla Cybertruck, Billboard reports. He said the other driver swerved across the double-yellow line to dodge an opossum, and that he hadn&rsquo;t been drinking or using autopilot.</p></div></div>
<div class="wire"><div><span class="num">10</span><h3>Amanda Seyfried&rsquo;s Secret Script</h3><p>Amanda Seyfried appears in &ldquo;You Can See Everything,&rdquo; Nathan Fielder and Lance Oppenheim&rsquo;s documentary about Theranos founder Elizabeth Holmes, playing Holmes and herself, Variety reports. The script was so secret it took a &ldquo;five-factor authentication app&rdquo; to open it.</p></div></div>
''' + askm + guide + '''
<h2 class="sec">The Gridiron</h2>
<div class="wire"><div><h3>Bills: A Short Week, a Walk-Through</h3><p>The Bills haven&rsquo;t had a full practice this week: no practice Monday and a walk-through Tuesday, so the injury reports are estimates, Buffalo Rumblings reports. Spencer Brown, Damar Hamlin and Greg Rousseau look headed toward playing, and Christian Benford and Dorian Williams look questionable. Chiefs at Bills, Thanksgiving night at 8:20, in the team&rsquo;s Thanksgiving uniforms, WGRZ reports.</p></div></div>
<div class="wire"><div><h3>Jets: Geno&rsquo;s Day</h3><p>Geno Smith completed 17 of 21 passes for 176 yards and three touchdowns in Sunday&rsquo;s win over the Chargers, with scores on the Jets&rsquo; first five possessions, Gang Green Nation reports. Next: at Miami on Sunday.</p></div></div>
<div class="wire"><div><h3>The Sunday Tax &middot; Week 12</h3><p>Picks at <a href="https://tally.so/r/RGOakJ">tally.so/r/RGOakJ</a>, standings at <a href="https://benthambulletin.github.io/pool/">benthambulletin.github.io/pool</a>. $5 a week, straight-up winners, the pot to the best record, and anyone with the link can play. Sheets lock at each kickoff; the first is tonight at 8, Packers at Rams, then three more on Thanksgiving.</p></div></div>
'''
hourly = f['towns']['North Tonawanda']['hourly']
crv = curve(hourly, 7*60+20, 16*60+44)
P = f['towns']['North Tonawanda']['periods']
alm = '''<div class="part"><span>The Almanac</span></div>
<h2 class="sec">The Weather Glass</h2>
''' + BYLINE + '''
<p class="wlede">Last good day of the week. Sunny, 42, no wind to speak of. Rake, string the lights, fill the gas tank. Tomorrow afternoon the sky opens up and stays open through Friday.</p>
<div class="touch-head" style="margin-top:1.1rem">Today</div>
<div class="wxrow">
  <div class="wxc"><div class="k">Tonight</div><div class="v">28&deg;</div><div class="s">mostly cloudy</div></div>
  <div class="wxc"><div class="k">Wind</div><div class="v">3&ndash;9</div><div class="s">mph, east</div></div>
  <div class="wxc"><div class="k">Rain</div><div class="v">None</div><div class="s">till Thursday 1 p.m.</div></div>
  <div class="wxc"><div class="k">Normal</div><div class="v">44&deg;</div><div class="s">for the date</div></div>
</div>
<div class="line"><span class="lbl t">Next 24 hours</span></div>''' + crv + '''
<div class="line"><span class="lbl t">Records</span> Buffalo&rsquo;s for the date: 65 in 2001; 8 in 1938. A year ago: 54 and 41, with a quarter inch of rain.</div>
<div class="touch-head" style="margin-top:1.1rem">This week</div>
<div class="strip5">
  <div><div class="d">Wed</div><div class="i">&#9728;</div><div class="h">42</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Thu</div><div class="i">&#127783;</div><div class="h">42</div><div class="w">rain after 1</div></div>
  <div><div class="d">Fri</div><div class="i">&#127783;</div><div class="h">45</div><div class="w">rain, showers</div></div>
  <div><div class="d">Sat</div><div class="i">&#127782;</div><div class="h">47</div><div class="w">chance showers</div></div>
  <div><div class="d">Sun</div><div class="i">&#127782;</div><div class="h">51</div><div class="w">chance showers</div></div>
</div>
<div class="line"><span class="lbl t">Rain total</span> A quarter to half an inch Thursday afternoon, 1 to 2 inches Thursday night, and another quarter to half inch Friday.</div>
<div class="line"><span class="lbl t">Frost watch</span> 28 tonight, the last freeze in the forecast. After that the nights stay in the mid-30s through the weekend.</div>
<div class="touch-head" style="margin-top:1.1rem">Around us &middot; at dawn</div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">23<sup>&deg;</sup></div><div class="d">Clear<br>high 42&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">25<sup>&deg;</sup></div><div class="d">Clear<br>high 44&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">23<sup>&deg;</sup></div><div class="d">Mostly cloudy<br>high 42&deg;</div></div>
</div>
<div class="towns lakes">
  <div class="town"><div class="n">Lake Erie</div><div class="t">52<sup>&deg;</sup></div><div class="d">off Buffalo</div></div>
  <div class="town"><div class="n">Lake Ontario</div><div class="t">53<sup>&deg;</sup></div><div class="d">off Rochester</div></div>
</div>
<div class="line" style="margin-top:.4rem"><span class="lbl t">Snow so far</span> since July 1, through Tuesday. Still zero everywhere, and this week&rsquo;s storm is all rain.</div>
<div class="towns snow"><div class="town"><div class="n">North Tonawanda</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 4.8"</div></div><div class="town"><div class="n">Orchard Park</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 6.5"</div></div><div class="town"><div class="n">Dunkirk</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 6.5"</div></div><div class="town"><div class="n">Scottsville</div><div class="t">0.0<sup>"</sup></div><div class="d">normal 6.0"</div></div></div>
<h2 class="sec">The Almanac Sky</h2>
<div class="wxrow">
  <div class="wxc"><div class="k">Moon</div><svg class="moonmini" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#3a2a1c" opacity=".25"/><path d="M50 4 A46 46 0 0 0 50 96 A44.2 46 0 0 0 50 4Z" fill="#f4e5b4"/></svg><div class="s">98% lit</div></div>
  <div class="wxc"><div class="k">Sunrise</div><div class="v">7:20</div><div class="s">a.m.</div></div>
  <div class="wxc"><div class="k">Daylight</div><div class="v">9h 25m</div><div class="s">2 min less</div></div>
</div>
<p class="skynote"><b>Tonight:</b> a day past full and starting to wane, the moon rises at 5:24 p.m. in Taurus and sets at 9:59 Thursday morning, so it&rsquo;ll still be up over the start line. Saturn is the evening&rsquo;s bright planet, in the south after dark; Jupiter rises around 11, Mars just after. Next new moon, December 8; next full, the Cold Moon, December 23.</p>
<div class="touch-head">The Stars &middot; for fun</div>
<div class="stars slim">
<div class="star"><span class="sgn">Aries</span> <span class="who">Kaylani, Luka</span><br>The moon still likes you. Ask for the good stroller blanket now, not at 8:55 tomorrow.</div>
<div class="star"><span class="sgn">Cancer</span> <span class="who">Gregg</span><br>Another quiet sky. Eat lunch light; you know why.</div>
<div class="star"><span class="sgn">Leo</span> <span class="who">Leah, Tommy</span><br>Friendly moon, second day running. Buy the lettuce today; the store tomorrow is a war.</div>
<div class="star"><span class="sgn">Virgo</span> <span class="who">Derek, Joanne</span><br>The moon is leaning on you again. Thaw check at noon, mushroom count at four, then sit down.</div>
<div class="star"><span class="sgn">Scorpio</span> <span class="who">Ariel, Claire, Garret</span><br>Nothing overhead. Lay out the race clothes tonight, gloves on top.</div>
</div>
<h2 class="sec">Coming Up</h2>
<div class="calbox"><div class="calrow"><div class="cd">Tonight</div><div>Packers at Rams, 8:00, the Sunday Tax&rsquo;s first lock</div></div>
<div class="calrow"><div class="cd">Thu</div><div>Thanksgiving. Turkey Trot downtown, 9:00; at Derek&rsquo;s, appetizers 1, dinner 3; Chiefs at Bills, 8:20</div></div>
<div class="calrow"><div class="cd">Sun</div><div>Jets at Dolphins, 1:00</div></div>
<div class="calnote">Migraine log: Joanne&rsquo;s last was Sunday; Garret&rsquo;s, Nov. 14. Four this month.</div>
</div>
<h2 class="sec">On This Day</h2>
<div class="otd"><b>November 25, 1950</b> &mdash; Thanksgiving weekend, a storm took shape over the Carolinas and became what the weather service calls the Great Appalachian Storm. It dropped 30.5 inches of snow on Pittsburgh and as much as 62 at Coburn Creek, West Virginia; Louisville, Lexington and Bowling Green set November record lows that day, and gusts hit 94 mph in New York City and 140 at Bear Mountain. By the time it spun out over Lake Erie and into Canada, 160 people were dead. Buffalo, on the warm side of it, got no snow at all and sat in the 40s while Pittsburgh shivered in the single digits.</div>
<h2 class="sec">Question of the Day</h2>
<div class="qotd">Thousands will run on me Thursday morning, and I won&rsquo;t move an inch. What am I? <i>Answer below the fold.</i></div>
<div class="dbl"><div class="a"></div><div class="b"></div></div>
<div class="colo"><div class="s" style="margin-bottom:8px"><b>Question of the Day:</b> The street.</div>
<div class="s">Forecast, lake temperatures and radar per NWS Buffalo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; normals from NOAA &middot; sky computed for 14120 &middot; headlines via the BBC, CBS, the <i>Niagara Gazette</i>, the Dunkirk <i>Observer</i>, WKBW, Billboard, Variety, Buffalo Rumblings, Gang Green Nation, WGRZ &middot; Turkey Trot details per the YMCA Buffalo Niagara and its 2026 route map &middot; On This Day per NWS Jackson, Ky. &middot; snow and records via ACIS &middot; cover via Wikimedia Commons</div>
<div class="ask"><a href="https://tally.so/r/rjxDpl">Send something to the paper</a> &middot; <a href="https://tally.so/r/obWNYP">Log a migraine</a> &middot; <a href="https://tally.so/r/EqxJpo">Ask Margo</a></div>
<div class="sig">&mdash; Margo</div><div class="orn">&#127809; &#127810; &#127809;</div></div>'''
body = pre + news + alm
ed = {'date':'2026-11-25','no':154,'body_html':body,'plate_path':'/home/claude/plate154.jpg','plate_caption':'The Buffalo Convention Center, the new start and finish of the Turkey Trot.','headline':'Turkey Trot: dry at 9, windy, rain after 1 · Ábrego García leaves for Spain · Huawei verdict'}
for p in ['/home/claude/edition-2026-11-25.json','/home/claude/site/data/edition-2026-11-25.json']:
    json.dump(ed, open(p,'w'), ensure_ascii=False)
print('ok', len(body))
