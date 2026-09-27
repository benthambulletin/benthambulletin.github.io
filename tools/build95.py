import json
d=json.load(open('edition-2026-09-26.json')); b=d['body_html']
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
H=lambda o,t:f'<h2 class="sec"><span class="o">{o}</span>{t}<span class="o">{o}</span></h2>'

R('No. 94','No. 95')
R('Saturday &middot; September 26 &middot; 2026','Sunday &middot; September 27 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">67&deg;</div><div class="k">Clouds, showers tonight</div></div>
  <div class="tile"><div class="v">29.99&#8243; &#9660;</div><div class="k">Down a third day</div></div>
  <div class="tile urg"><div class="v">37</div><div class="k">Days to Election Day</div></div>
</div>
''')
R('Caught mid-cough, day two &mdash; still sick, and still not letting go of the diaper pack.','Toby, one bite from winning.')
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>Toby has the cover</b>, and the ball, very nearly. A dog on the front page on a Sunday is a tradition this paper just started. <b>Luka</b> has had a rough few days with the fever and the cough; the whole paper hopes this is the morning he turns the corner. Both teams kick off at one, the race is at three, and the rain holds off until evening.
''')
S('<ul class="cal">','</ul>','''<ul class="cal">
<li><span class="dt">Today</span><span>Chargers at Buffalo, Jets at Detroit &mdash; both 1:00</span></li>
<li><span class="dt">Today</span><span>Kansas, NASCAR playoffs &mdash; 3:00, USA</span></li>
<li><span class="dt">Oct 23</span><span>Claire's birthday</span></li>
<li><span class="dt">Oct 25</span><span>Garret and Ariel's birthday</span></li>
<li><span class="dt">Nov 3</span><span>Election Day</span></li>
''')
# Sunday Spotlight after Family Today
SPOT=H('&#9788;','The Sunday Spotlight')+'''
<div class="touch-head">The Seed Deadline Nobody Heard About</div>
<div class="line" style="color:var(--soft)">A change to federal law, tucked into a spending bill last November, is about to make it illegal to mail most cannabis seeds across state lines. Here is what happened and what it does, in plain terms.</div>
<div class="line"><b>What changed.</b> "Hemp" is the legal name for cannabis low enough in THC, the part that gets you high, to be treated as a farm crop. Since 2018, seeds counted as hemp because a seed itself has almost no THC in it, and that is how online seed shops have legally shipped to every state. The new definition judges a seed by the plant it would grow into instead. Seeds of ordinary high-THC varieties stop being hemp, and shipping them across a state line becomes, on paper, federal drug distribution.</div>
<div class="line"><b>When.</b> The law was set to take effect November 12. On September 2 a stopgap funding bill pushed most of the new hemp rules back to December 11, mainly to protect CBD and hemp-drink makers. Whether seeds moved with them is not clear from anything published yet, and the seed companies are not waiting to find out: they are treating November 12 as the last day to ship.</div>
<div class="line"><b>What it does not touch.</b> State law. In New York, growing a few plants at home for yourself is legal, and buying seeds from a licensed dispensary inside the state is unaffected. What goes away is the mail-order business from out of state, which is where most home growers have always bought.</div>
<div class="line"><b>Can it be fixed?</b> Several bills would treat seeds as an ordinary farm product again, and one would let states opt out. None has a vote scheduled. The likeliest vehicle is the next Farm Bill, and the House passed its version without the fix. People who follow it closely call partial relief plausible and a full repeal before the deadline unlikely.</div>
<div class="line" style="color:var(--soft)">Written by an A.I. from public reporting. Nothing here is legal advice.</div>
'''
R('<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass', SPOT+'<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass')
S('<div class="wx">','<div class="towns">','''<div class="wx"><div class="bigtemp">67<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">Clouds thicken, and the rain waits for dark</span>
Low <b>56&deg;</b> &middot; Northeast 8&ndash;15<br>Rain <b>Tonight</b> &mdash; a chance of showers, mostly before 11</div></div>
''')
S('<div class="towns">','<div class="strip5">','''<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">55<sup>&deg;</sup></div><div class="d">Fair &middot; high 67&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">43<sup>&deg;</sup></div><div class="d">Fog, then partly sunny &middot; high 66&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">56<sup>&deg;</sup></div><div class="d">Showers after 3 &middot; high 64&deg;</div></div>
</div>
''')
S('<div class="strip5">','<div class="line"><span class="lbl t">Yes, rain tomorrow','''<div class="strip5">
  <div><div class="d">Sun</div><div class="i">&#9729;</div><div class="h">67</div><div class="w">showers tonight</div></div>
  <div><div class="d">Mon</div><div class="i">&#9729;</div><div class="h">67</div><div class="w">mostly cloudy</div></div>
  <div><div class="d">Tue</div><div class="i">&#9925;</div><div class="h">72</div><div class="w">partly sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#9925;</div><div class="h">74</div><div class="w">partly sunny</div></div>
  <div><div class="d">Thu</div><div class="i">&#127782;</div><div class="h">74</div><div class="w">p.m. showers</div></div>
</div>
''')
S('<div class="line"><span class="lbl t">Yes, rain tomorrow','<div class="pnote">','''<div class="line"><span class="lbl t">Game day</span> Dry at Orchard Park for the one o'clock kickoff, clouds building and a northeast breeze. Showers are a chance tonight, mainly before 11. Scottsville gets the real rain, 80%, from mid-afternoon on. <span class="lbl t">Outdoor window</span> This morning; then Tuesday and Wednesday, 72 and 74.</div>
''')
S('<div class="pnote">','<h2 class="sec"><span class="o">&#127810;</span>The Turning','''<div class="pnote"><b>Long Island, the morning after the worst of it.</b> More than 13,000 PSEG customers lost power across the weekend, from nearly 800 separate outages. The Coast Guard measured a 57 mph gust at Eaton's Neck. Freeport, Island Park, Lindenhurst and Mastic Beach flooded at high tide, and waves of seven to ten feet chewed at the beaches from Fire Island to Montauk. The LIRR suspended parts of the Long Beach and Port Jefferson branches, Fire Island ferries are out through today, and the Long Island Fair was cancelled. A swimmer went missing at Robert Moses State Park. It winds down today and clears Monday afternoon. Outages: 1-800-490-0075.</div>
''')
S('<div class="line"><b>A pause in the cold.</b>','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','''<div class="line"><b>Still a waiting game.</b> The three counties show essentially no change. Wednesday's report is the next number, and a mild week keeps it slow.</div>
''')
S('<div class="sky">','<div class="stars">','''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 1 50 96 A42 46 0 0 1 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>Ninety-nine percent</b>, just past full, and rising at 7:14 tonight, eleven minutes after sunset. This is the second night of the Harvest Moon effect: it keeps coming up close to dusk rather than an hour later each evening.<br>
<span class="lbl t">Sun</span> 7:08a &ndash; 7:03p &middot; <b>11h 56m</b><br>
<span class="lbl t">Last quarter</span> Sat, Oct 3 &middot; <span class="lbl t">Next new moon</span> Sat, Oct 10</div></div>
<div class="line"><span class="lbl r">Tonight</span> <b>Saturn</b> follows the moon up at 7:24. <b>Jupiter</b> rises at 3:09 a.m. <b>Mars</b> crosses into Leo overnight, around 2 a.m.</div>
''')
S('<div class="stars">','<div style="font-family:','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>The moon is in Aries and trine Jupiter</b>, a warm, easy aspect between a fiery moon and the planet of good luck. After a week of full-moon pressure, this is the soft landing. Let someone look after you. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>Mars spends its last day in your sign</b>, at the final degree, opposite Pluto. The push ends tonight. Whatever you started this month, it will not be finished by force today; set it down cleanly. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Mars arrives in Leo overnight</b> and stays until mid-November. With Jupiter already here, the next seven weeks bring both the nerve and the luck. Start the thing Monday. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>Mercury, your ruler, squares Mars</b> today: sharp words come easily and land harder than meant. A good day to write the email and a bad day to send it. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Pluto, your old ruler, is trine the Sun</b> and sextile Neptune almost exactly, with Venus still resting in your sign. Deep, quiet and steady; the kind of Sunday that restores more than it costs. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
S('<div class="baro-top">','<h2 class="sec"><span class="o">&#10038;</span>The Ledger','''<div class="baro-top"><div class="dial">Moderate &middot; 42/100</div><div class="press">29.99&#8243;</div><div class="trend">&#8595; down a third day</div></div>
<div class="baro"><svg viewBox="0 0 820 180" xmlns="http://www.w3.org/2000/svg">
<g font-family="AR" font-size="13" fill="#6b5f44"><line x1="64" y1="18" x2="790" y2="18" stroke="#d6cbaf"/><text x="16" y="22">30.54</text>
<line x1="64" y1="60" x2="790" y2="60" stroke="#d6cbaf"/><text x="16" y="64">30.36</text><line x1="64" y1="102" x2="790" y2="102" stroke="#d6cbaf"/><text x="16" y="106">30.18</text>
<line x1="64" y1="144" x2="790" y2="144" stroke="#d6cbaf"/><text x="16" y="148">30.00</text></g>
<polyline points="120,56 280,27 440,13 600,55 760,147" fill="none" stroke="#0e8a8a" stroke-width="3"/>
<g fill="#0e8a8a"><circle cx="120" cy="56" r="6"/><circle cx="280" cy="27" r="6"/><circle cx="440" cy="13" r="6"/><circle cx="600" cy="55" r="6"/></g>
<circle cx="760" cy="147" r="7" fill="#c8302f"/><circle cx="760" cy="147" r="15" fill="none" stroke="#c8302f" stroke-width="2.5"/>
<g font-family="AR" font-size="14" fill="#6b5f44" text-anchor="middle"><text x="120" y="174">Wed 30.44</text><text x="280" y="174">Thu 30.50</text><text x="440" y="174">Fri 30.32</text><text x="600" y="174">Sat 30.15</text></g>
<text x="760" y="174" font-family="AR" font-size="14" font-weight="700" fill="#c8302f" text-anchor="middle">Today 29.99</text></svg></div>
<div class="line"><span class="lbl t">Half an inch in three days</span> 29.99 this morning, down from Thursday's record 30.50. Today's number is an ordinary one; it is the long, steady slide that migraine sufferers tend to feel. It levels off tonight as the showers pass, so the pressure should stop pulling by Monday.</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">Customers who lost power on Long Island</div><div class="big">13,000</div></div>
<div class="txt">From nearly 800 separate outages over the weekend, one downed line or tree at a time. Most were back by morning.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Walkout','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>U.S. and China Cut Tariffs, Open an A.I. Channel</h3><p>Xi Jinping's visit ended with tariff cuts on about $30 billion in goods and an agreed dialogue on artificial intelligence, according to Beijing.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Supreme Court Blocks Missouri's Map a Third Time</h3><p>The justices again refused to let Missouri use a new Republican-drawn congressional map for November, keeping a Kansas City Democratic seat intact.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Trump Rejects Iran's Hormuz Offer</h3><p>Tehran offered to reopen the Strait of Hormuz within a week if the U.S. lifts its naval blockade. The president turned it down.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>Hurricane Nolo Skirts Hawaii</h3><p>The storm weakened and stayed south of the Big Island, but brought heavy rain and gusty winds; warnings were cancelled Saturday.</p></div></div>
''')
# Full Ballot replaces daily bar
S('<div class="ballot">','<h2 class="sec"><span class="o">&#9962;</span>The Home Wire',H('&#9745;','The Ballot')+'''
<div class="touch-head">Hochul Pulls Away</div>
<div class="line">Thirty-seven days. Two polls released this week agree on the direction, if not the size. <b>Quinnipiac</b> has Governor Hochul at 58 and Bruce Blakeman at 39 among likely voters, a 19-point lead. <b>Siena</b> has it closer, 50 to 41, up a point or two for Hochul since August.</div>
<div class="line"><b>What voters say matters.</b> Cost of living first at 28 percent, then the economy at 21, then health care. Hochul leads among voters on both of the top two. The same Quinnipiac poll put Senator Schumer's approval at 36 percent and President Trump's at 29 in New York.</div>
<div class="line">The three House seats this family votes in, NY-26, NY-23 and NY-25, are not expected to be close.</div>
<div class="line" style="color:var(--soft)">Early voting Oct 24&ndash;Nov 1 &middot; register by Oct 24 &middot; Election Day Nov 3.</div>
''')
S('<h2 class="sec"><span class="o">&#9962;</span>The Home Wire','<h2 class="sec"><span class="o">&#9733;</span>The Marquee',H('&#9962;','The Home Wire')+'''
<div class="wire"><div class="num">1</div><div><h3>Dunkirk &middot; Water Base Rate Going Up $10</h3><p>The city's finance committee is backing a jump in the monthly base charge from $20 to $30, about 19 cents a day for a typical home, after the state Comptroller said water revenue was not covering costs. The Common Council votes next.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Rochester &middot; Free Afternoon at the Memorial Art Gallery</h3><p>Hispanic Heritage Celebration Day is today, noon to 4, with free admission, music and dance. The Philharmonic repeats its opening program at 2 at Kodak Hall.</p></div></div>
''')
S('<h2 class="sec"><span class="o">&#9733;</span>The Marquee','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron',H('&#9733;','The Marquee')+'''
<div class="wire"><div class="num">1</div><div><h3>A Month Since Dolly</h3><p>Fans marked Dolly Parton Day this weekend, one month after her death, with tributes in Nashville and across the country.</p></div></div>
''')
S('<div class="touch-head">Tomorrow at One</div>','<table class="tbl">','''<div class="touch-head">Kickoff at One</div>
<div class="line"><b>Bills</b> &middot; the Chargers at Highmark, CBS. Buffalo is 2&ndash;0; Los Angeles is 0&ndash;2 and lost to Las Vegas at home last week. Coleman, Moore and Oliver are all questionable. The oddsmakers make it roughly three-to-one Buffalo.</div>
<div class="line"><b>Jets</b> &middot; at Detroit, indoors, 1&ndash;1 against a Lions team coming off a Thursday-night loss in Orchard Park. A good road test for a team that has played better than its record.</div>
''')
S('<div class="touch-head">Qualifying Today at Kansas</div>','<div class="cards">','''<div class="touch-head">Rain Set the Grid</div>
<div class="line">Weather wiped out practice and qualifying at Kansas, so the lineup came from NASCAR's performance formula for the third time in four Chase races. <b>Joey Logano</b> starts on the pole with <b>Kyle Larson</b> beside him; Denny Hamlin, one point behind Larson, starts sixth.</div>
''')
R('<div class="cards"><div class="card"><div class="h">&#127937; Round 4</div><div class="m">Hollywood Casino 400, Kansas</div><div class="s">Sun, Sep 27 &middot; 3:00 &middot; USA</div></div></div>',
  '<div class="cards"><div class="card"><div class="h">&#127937; Round 4 &middot; today</div><div class="m">Hollywood Casino 400, Kansas</div><div class="s">3:00 &middot; USA</div></div></div>')
SUN=H('&#10038;','The Week Ahead')+'''
<div class="line"><b>Weather.</b> Grey and 67 Monday, then 72 and 74 Tuesday and Wednesday, the warmest days left in the forecast. Showers return Thursday afternoon.</div>
<div class="line"><b>Sky.</b> Mars enters Leo overnight tonight. Last-quarter moon Saturday.</div>
<div class="line"><b>Football.</b> Monday Morning Quarterback tomorrow, with both results.</div>
<div class="line"><b>The Turning.</b> New foliage report Wednesday afternoon.</div>
<div class="line"><b>Calendar.</b> Nothing on the family calendar this week. Send it in if there is.</div>
'''+H('&#9776;','The Week in the Glass')+'''
<table class="tbl"><tr><th>Day</th><th class="n">Barometer</th><th class="n">High</th><th class="n">Rain</th></tr>
<tr><td>Mon 21</td><td class="n">30.20</td><td class="n">60</td><td class="n">&mdash;</td></tr>
<tr><td>Tue 22</td><td class="n">30.30</td><td class="n">64</td><td class="n">&mdash;</td></tr>
<tr><td>Wed 23</td><td class="n">30.44</td><td class="n">67</td><td class="n">&mdash;</td></tr>
<tr><td>Thu 24</td><td class="n">30.50</td><td class="n">68</td><td class="n">&mdash;</td></tr>
<tr><td>Fri 25</td><td class="n">30.32</td><td class="n">66</td><td class="n">&mdash;</td></tr>
<tr><td>Sat 26</td><td class="n">30.15</td><td class="n">70</td><td class="n">&mdash;</td></tr>
<tr><td>Sun 27</td><td class="n">29.99</td><td class="n">67</td><td class="n">tonight</td></tr></table>
<div class="line">Four days up to the highest reading in the log, then three days straight down. A dry week start to finish. No migraines reported this week; the thirty-day read is set for around October 6.</div>
'''+H('&#10023;','The Sunday Question')+'''
<div class="qotd"><b>What is one thing you do every fall that you would miss if you skipped it?</b><br>Send it to the group chat this week. Answers run here next Sunday under your names.<br><span style="color:var(--soft)">Last week's question &mdash; the longest you have ever waited for something &mdash; is still open.</span></div>
'''
R('<h2 class="sec"><span class="o">&#9790;</span>On This Day', SUN+'<h2 class="sec"><span class="o">&#9790;</span>On This Day')
S('<div class="otd">','<h2 class="sec"><span class="o">&#10023;</span>Question','''<div class="otd"><b>September 27, 1825</b> &mdash; the Locomotion No. 1 pulled the first passenger train on a public steam railway, between Stockton and Darlington in England, at about eight miles an hour with a man on horseback riding ahead with a flag. The Erie Canal opened a month later. Within twenty years the railroads were beating it.</div>
''')
R('I have a neck but no head, and I wear a cap. What am I?','The more of me you take, the more you leave behind. What am I?')
R('<b>Question of the Day:</b> A bottle.','<b>Question of the Day:</b> Footsteps.')
R('storm reports via NWS, ABC7, CBS New York, FOX Weather','storm reports via News 12 Long Island &middot; polls via Quinnipiac and Siena &middot; Dunkirk via the <i>Observer</i>')
d.update(date='2026-09-27',no=95,body_html=b,plate_path='/home/claude/plate95.jpg',plate_caption='Toby, one bite from winning',
 headline="Toby on the cover · The seed deadline · Bills and Jets at one · Showers tonight")
json.dump(d,open('site/data/edition-2026-09-27.json','w'),indent=1); json.dump(d,open('edition-2026-09-27.json','w'),indent=1)
p=json.load(open('site/data/pressure.json'))
if p[-1]['date']!='2026-09-27': p.append({"date":"2026-09-27","in":29.99,"mb":1015.7,"station":"KIAG","time":"06:53 EDT"})
json.dump(p,open('site/data/pressure.json','w'),indent=1)
print('ok')
