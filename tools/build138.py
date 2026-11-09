import json
src = json.load(open('/home/claude/site/data/edition-2026-11-08.json'))['body_html']
def R(a, c, n=1):
    global src
    assert src.count(a) == n, ('R', a[:60], src.count(a)); src = src.replace(a, c)
def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50]); src = src[:i] + new + src[j:]
f = json.load(open('/home/claude/site/data/forecast.json'))
hr = [h['temp'] for h in f['towns']['North Tonawanda']['hourly']][:24]
W, H, P = 320, 62, 12
lo, hi = min(hr), max(hr)
xs = [P + i * (W - 2 * P) / (len(hr) - 1) for i in range(len(hr))]
ys = [H - P - (t - lo) * (H - 2 * P - 10) / max(1, hi - lo) for t in hr]
pts = ' '.join(f'{x:.1f},{y:.1f}' for x, y in zip(xs, ys))
ih, il = hr.index(hi), hr.index(lo)
lanc = 'start' if il < len(hr) / 2 else 'end'; lx = xs[il] + (5 if lanc == 'start' else -5)
spark = (f'<div class="line"><span class="lbl t">Next 24 hours</span></div>'
         f'<svg viewBox="0 0 {W} {H}" style="display:block;width:100%;max-width:420px;height:auto;margin:0 auto .4rem" role="img" aria-label="Hourly temperatures for North Tonawanda over the next 24 hours, from {hr[0]} now to a high of {hi} and a low of {lo}">'
         f'<polyline points="{pts}" fill="none" stroke="#9c3216" stroke-width="2" stroke-linejoin="round"/>'
         f'<circle cx="{xs[ih]:.1f}" cy="{ys[ih]:.1f}" r="3" fill="#9c3216"/><text x="{xs[ih]:.1f}" y="{ys[ih]-6:.1f}" text-anchor="middle" font-family="Archivo,Arial" font-size="10" fill="#24170c">{hi}&deg;</text>'
         f'<circle cx="{xs[il]:.1f}" cy="{ys[il]:.1f}" r="3" fill="#2f5e3e"/><text x="{lx:.1f}" y="{ys[il]-6:.1f}" text-anchor="{lanc}" font-family="Archivo,Arial" font-size="10" fill="#24170c">{lo}&deg;</text>'
         f'<text x="{P}" y="{H-1}" font-family="Archivo,Arial" font-size="9" fill="#6b5a48">now</text><text x="{W-P}" y="{H-1}" text-anchor="end" font-family="Archivo,Arial" font-size="9" fill="#6b5a48">this time tomorrow</text></svg>\n')

# cover: Monday Night Football under the lights, a new moon, drizzle clearing
lights = ''.join(f'<g transform="translate({x} 60)"><rect x="-3" y="0" width="6" height="150" fill="#3a2a1c"/><rect x="-26" y="-14" width="52" height="18" rx="3" fill="#3a2a1c"/>' + ''.join(f'<circle cx="{-18+k*12}" cy="-5" r="4.5" fill="#fff6c8" class="bulb"/>' for k in range(4)) + f'<path d="M-26 4 L-160 260 L160 260 L26 4Z" fill="url(#beam)" opacity=".55"/></g>' for x in (120, 630))
drops = ''.join(f'<line class="dr d{i%4}" x1="{40+i*37}" y1="0" x2="{34+i*37}" y2="14" stroke="#c9d6e0" stroke-width="1.4" opacity=".6"/>' for i in range(19))
svg = f'''<svg viewBox="0 0 750 375" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A football field glowing under stadium lights on a dark, drizzly night, with a ball on the fifty-yard line" style="display:block;width:100%;height:auto">
<style>.bulb{{animation:gl 2.4s ease-in-out infinite}}@keyframes gl{{50%{{opacity:.75}}}}
.dr{{animation:fall 1.2s linear infinite}}.d1{{animation-delay:-.3s}}.d2{{animation-delay:-.6s}}.d3{{animation-delay:-.9s}}@keyframes fall{{from{{transform:translateY(-20px)}}to{{transform:translateY(240px)}}}}
@media (prefers-reduced-motion:reduce){{.bulb,.dr{{animation:none}}}}</style>
<defs><linearGradient id="nt" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#141a28"/><stop offset="1" stop-color="#2c3346"/></linearGradient>
<linearGradient id="beam" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff6c8" stop-opacity=".7"/><stop offset="1" stop-color="#fff6c8" stop-opacity="0"/></linearGradient></defs>
<rect width="750" height="375" fill="url(#nt)"/>
{drops}
<path d="M0 250 L750 250 L750 375 L0 375Z" fill="#2f5e3e"/>
<path d="M60 250 L690 250 L750 375 L0 375Z" fill="#3c7350"/>
{''.join(f'<line x1="{375+(k-5)*63}" y1="250" x2="{375+(k-5)*75}" y2="375" stroke="#e8f0e6" stroke-width="2" opacity=".7"/>' for k in range(11))}
{lights}
<ellipse cx="375" cy="318" rx="22" ry="12" fill="#6b3a1f"/><path d="M362 318 h26" stroke="#f4ede0" stroke-width="2"/><path d="M370 314 v8 M375 313 v10 M380 314 v8" stroke="#f4ede0" stroke-width="1.5"/>
</svg>'''

NEW = '''<div class="tiles">
  <div class="tile"><div class="v">52&deg;</div><div class="k">Cloudy, Breezy</div></div>
  <div class="tile"><div class="v">4:57</div><div class="k">Sunset</div></div>
  <div class="tile urg"><div class="v">17</div><div class="k">Days to Thanksgiving</div></div>
</div>
<div class="calline"><b>Coming up</b> Tonight &middot; Bills at MIN, 8:15 &middot; Wed &middot; Veterans Day &middot; Sun &middot; Bills at Jets, 1:00<br><b>Migraine log</b> Garret, 6 days ago (2 this month); no one else this week</div>
<div class="plate-wrap"><div class="frame"><span class="tick tl"></span><span class="tick tr"></span><span class="tick bl"></span><span class="tick br"></span>
''' + svg + '''</div>
<div class="plate-cap">Plate I &middot; The Family Album</div>
<div class="plate-sub">Monday night, under the lights</div></div>
<div class="dbl-tight"><div class="a"></div><div class="b"></div></div>
<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass<span class="o">&#9788;</span></h2>
<div class="wx"><div class="bigtemp">52<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">A gray, damp start and a cloudy, breezy day at 52, with northwest gusts to 28</span>
Low <b>40&deg;</b> tonight &middot; mostly cloudy<br>Showers end by 10 a.m. &middot; fcst high 52, normal 50</div></div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">46<sup>&deg;</sup></div><div class="d">Light rain<br>high 52&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">48<sup>&deg;</sup></div><div class="d">Cloudy<br>high 52&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">46<sup>&deg;</sup></div><div class="d">Light rain<br>high 51&deg;</div></div>
</div>
<div class="strip5">
  <div><div class="d">Mon</div><div class="i">&#9729;</div><div class="h">52</div><div class="w">cloudy, breezy</div></div>
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">59</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#9925;</div><div class="h">56</div><div class="w">partly sunny</div></div>
  <div><div class="d">Thu</div><div class="i">&#127783;</div><div class="h">49</div><div class="w">rain</div></div>
  <div><div class="d">Fri</div><div class="i">&#127783;</div><div class="h">44</div><div class="w">chance of rain</div></div>
</div>
''' + spark + '''<div class="line"><span class="lbl t">Outdoor window</span> Tuesday, mostly sunny and 59. <span class="lbl t">Snow watch</span> Friday night, a chance of rain and snow, low around 31.</div>
<div class="line"><span class="lbl t">The lakes</span> Erie 58&deg; off Buffalo, Ontario 58&deg; off Rochester, Sunday's readings.</div>
<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky<span class="o">&#9790;</span></h2>
<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><circle cx="50" cy="50" r="46" fill="none" stroke="#6b5a48" stroke-width="2"/></svg><div>
<b>New moon today</b>, traveling with the sun against the stars of Libra; it rose at 7:35 a.m. and sets at 4:44 p.m., unseen.<br>
<span class="lbl t">Sun</span> 7:00a &ndash; 4:57p &middot; <b>9h 58m</b> of daylight<br>
<span class="lbl t">Planets</span> Saturn, about halfway up the southern sky around 10 tonight.<br>
<span class="lbl t">Beaver Moon</span> Tue, Nov 24 &middot; <span class="lbl t">Next new moon</span> Tue, Dec 8</div></div>
<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>A new moon in Scorpio, a long way from your sign.</b> Fresh starts happen elsewhere today. Help someone else's along. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>The new moon in Scorpio trines your sign.</b> Plant an idea today. It grows. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>The moon squares your sign and the Mars and Jupiter sitting in it.</b> Big energy, short fuse. Count to ten before kickoff. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>The new moon sextiles your sign.</b> A good day to start the list. Just start it. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>The new moon is in your sign, beside the sun.</b> Your own small new year. Make one quiet promise. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
<div style="font-family:'LOI';font-style:italic;font-size:.8rem;color:var(--soft);margin-top:.4rem">The sky is real; the readings are for fun.</div>
<h2 class="sec"><span class="o">&#10038;</span>The Ledger<span class="o">&#10038;</span></h2>
<div class="ledger"><div class="num"><div class="cap">Feet Lake Powell rose after Southwest floods</div><div class="big">20</div></div>
<div class="txt">Rare relief for the giant Colorado River reservoir and the Southwest it waters, PBS NewsHour reports.</div></div>
<h2 class="sec"><span class="o">&#10038;</span>The National Wire<span class="o">&#10038;</span></h2>
<div class="wire lead"><div><span class="kick">The Lead</span><h3>Nvidia Investigates Its Own Boss</h3>
<p>Nvidia, the company whose chips power the artificial-intelligence boom, has opened an independent investigation of its co-founder and CEO, Jensen Huang, CBS reports. It follows <i>New York Times</i> reports that he had a close relationship with Alice Huang, a Chinese businesswoman U.S. intelligence agencies believe worked for China's Ministry of State Security, its main spy agency. The two are not related.</p>
<p>In a message to employees Sunday, Huang admitted being "unfaithful" to his wife and apologized to her and their children, without naming the woman. "There is no excuse for what I did. I am deeply sorry," he wrote.</p>
<p>Nvidia's board says it has "no reason to believe" national security or company secrets were compromised, NPR reports, but that its inquiry "will examine all available information." Huang has led the company for 30 years, the BBC notes.</p>
<div class="pull">"There is no excuse for what I did."</div>
</div></div>
<div class="wire"><div class="num">2</div><div><h3>Update: Only Kidding, Dana</h3><p>President Trump said Sunday he "was only kidding" when he offered UFC boss Dana White the job of White House press secretary, the BBC reports. "Dana loves the idea," he said, adding that White would visit him Monday "for other reasons."</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Nine Hours Treading Water</h3><p>Two fishermen found a cruise ship pianist treading water about 20 miles off the California coast near Catalina Island on Friday, after he fell overboard from Royal Caribbean's <i>Ovation of the Seas</i>, the BBC and CBS report; officials think he was in the Pacific for nine hours. "The only thing he said to me was, 'Thank you. I thought I was gonna die,'" fisherman Sean Norton said.</p></div></div>
<h2 class="sec"><span class="o">&#9962;</span>The Home Wire<span class="o">&#9962;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; A Local Man Gets the Mariners</h3><p>Jason Kanzler, a Rochester-area native and former University at Buffalo baseball player, is the new manager of the Seattle Mariners, the club announced, WGRZ reports.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Dunkirk &middot; A New Fire Contract</h3><p>The Common Council unanimously approved a fire department contract that runs through Jan. 1, 2029, with no raises in 2025 and 2026, then 4 percent in 2027 and 2 percent in 2028, the <i>Observer</i> reports. It adds an emergency medical training officer and drops the assistant chief's position.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Westfield &middot; School Work 57 Percent Done</h3><p>Westfield Academy and Central School's building project is about 57 percent complete, with new locker rooms due this month, the <i>Observer</i> reports. The board approved a new playground, though one member said the district was being "overcharged" at more than half a million dollars.</p></div></div>
<h2 class="sec"><span class="o">&#9733;</span>The Marquee<span class="o">&#9733;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>Taylor and Karlie, Reunited</h3><p>Taylor Swift and her longtime friend Karlie Kloss sat together in the VIP section at Arrowhead on Sunday to watch Travis Kelce's Chiefs play the Jets, Billboard and Page Six report. Fans who had followed rumors of a falling-out called it "war is over."</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Ariana, De Niro and Stiller Sing</h3><p>Ariana Grande and her <i>Focker-in-Law</i> co-stars Robert De Niro and Ben Stiller sang "O Christmas Tree" on Sunday's <i>Tonight Show</i>, Billboard reports, as Jimmy Fallon marked the arrival of the Rockefeller Center Christmas tree. Grande took the high notes; Stiller gave "a valiant effort."</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Justin Timberlake's Family Runway</h3><p>Justin Timberlake walked the runway with his sons, Silas, 11, and Phineas, 6, and his niece Zaya at the Global Down Syndrome Foundation's fashion show in Denver on Saturday, Us Weekly reports. The fundraiser brought in more than $2.7 million for research.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>Gronk Enters the Patriots Hall</h3><p>Rob Gronkowski, the Amherst native and Williamsville North star who became one of the great tight ends, was inducted into the Patriots Hall of Fame this weekend, WGRZ reports.</p></div></div>
<h2 class="sec"><span class="o">&#127944;</span>The Gridiron<span class="o">&#127944;</span></h2>
<div class="touch-head">Monday Morning Quarterback</div>
<div class="line"><b>Jets 12, Chiefs 35</b> &middot; The Jets led 6&ndash;0 and trailed only 14&ndash;12 at halftime on four field goals, the longest from 54 yards. The Chiefs then scored 21 unanswered points in the second half, and the Jets were sacked five times. <b>Got right:</b> the first half, when they outgained Kansas City, won the turnover battle and scored on four of five drives, Gang Green Nation says. <b>To fix:</b> finishing drives; all 12 points came on field goals. They are 2&ndash;7.</div>
<div class="line"><b>Bills tonight</b> &middot; Buffalo plays at Minnesota at 8:15, both teams 6&ndash;1. It is the league's top-scoring offense, 33.3 points a game, against its stingiest defense, 13.3 allowed, Buffalo Rumblings says, and Carson Wentz starts at quarterback for the Vikings with Kyler Murray out. The full recap runs tomorrow.</div>
<div class="line"><b>AFC East</b> &middot; Bills 6&ndash;1 &middot; Patriots 5&ndash;4 &middot; Jets 2&ndash;7 &middot; Dolphins 1&ndash;7</div>
<div class="line"><b>Around the league</b> &middot; The 49ers beat the Raiders 38&ndash;17 to go 7&ndash;1; Cincinnati won 34&ndash;17 over Atlanta in Madrid; the Bears survived five turnovers to beat Tampa Bay 27&ndash;24 Sunday night.</div>
<div class="line"><b>The AI Editor's card</b> &middot; Picked the Bills at 11&ndash;6 (6&ndash;1 now) and the Jets at 6&ndash;11 (2&ndash;7 now, so four more wins needed to get there).</div>
<h2 class="sec"><span class="o">&#9873;</span>The Chase<span class="o">&#9873;</span></h2>
<div class="line"><b>Larson, again.</b> Kyle Larson clinched his third Cup Series title in six years early in Sunday's finale at Homestead, the first driver to win back-to-back since Jimmie Johnson in 2010, AP reports; Ryan Blaney won the race. "This was statistically probably one of our worst years," Larson said. Final points: Larson 2,501, Bell 2,452, Hamlin 2,445. The Chase rests until next season.</div>
<h2 class="sec"><span class="o">&#9790;</span>On This Day<span class="o">&#9790;</span></h2>
<div class="otd"><b>November 9, 1965</b> &mdash; At 5:16 p.m., a faulty relay at the Sir Adam Beck power station near Niagara Falls, Ontario, set off the Northeast Blackout. About 30 million people in the Northeast and Ontario lost power, some for up to 13 hours.</div>
<h2 class="sec"><span class="o">&#10023;</span>Question of the Day<span class="o">&#10023;</span></h2>
<div class="qotd">I lean in the garage all summer and nobody looks at me, but after the first big storm I'm the most popular thing in the house. What am I? <i>Answer below the fold.</i></div>
'''
R('No. 137', 'No. 138')
R('Sunday &middot; November 8 &middot; 2026', 'Monday &middot; November 9 &middot; 2026')
S('<div class="tiles">', '<div class="dbl"><div class="a"></div><div class="b"></div></div>\n<div class="colo">', NEW)
R("<b>Question of the Day:</b> A snowman.", "<b>Question of the Day:</b> A snow shovel.")
S('<div class="s">Forecast, lake temperatures', '<div class="ask">',
'''<div class="s">Forecast, lake temperatures and radar per NWS Buffalo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; normals from NOAA &middot; sky computed for 14120 &middot; headlines via CBS, NPR, the BBC, PBS NewsHour, WGRZ, the Dunkirk <i>Observer</i>, Billboard, Page Six, Us Weekly, Gang Green Nation, Buffalo Rumblings, AP &middot; scores, standings and NASCAR points via Sportradar</div>
''')
ed = {"date": "2026-11-09", "no": 138, "body_html": src, "plate_path": None, "plate_caption": "Monday night, under the lights",
      "headline": "Nvidia investigates its own boss · Larson, again · Bills under the lights"}
for p in ['/home/claude/edition-2026-11-09.json', '/home/claude/site/data/edition-2026-11-09.json']:
    json.dump(ed, open(p, 'w'), ensure_ascii=False, indent=1)
print('ok', lo, hi)
