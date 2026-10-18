import json
d=json.load(open('edition-2026-10-17.json')); b=d['body_html']
baro=open('/tmp/claude-0/-home-claude/001a10af-13f9-5479-8fec-28bf86d9c496/scratchpad/baro116.html').read(); baro=baro[:baro.index('<!--')].strip()+'\n'
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
R('No. 115','No. 116')
R('Saturday &middot; October 17 &middot; 2026','Sunday &middot; October 18 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">60&deg;</div><div class="k">Frost, then sun</div></div>
  <div class="tile"><div class="v">30.52&#8243; &#9650;</div><div class="k">Week's high</div></div>
  <div class="tile urg"><div class="v">16</div><div class="k">Days to Election Day</div></div>
</div>
''')
S('<div class="fam">','<div class="ask">','''<div class="fam"><b>Football Sunday, and birthday week.</b> The Jets kick off at 1:00 and the Bills at 4:25. Claire's birthday is Friday, and Garret and Ariel share theirs next Sunday.
<ul class="cal">
<li><span class="dt">Oct 18</span><span>Jets at Patriots &mdash; 1:00</span></li>
<li><span class="dt">Oct 18</span><span>Bills at Raiders &mdash; 4:25</span></li>
<li><span class="dt">Oct 23</span><span>Claire's birthday</span></li>
<li><span class="dt">Oct 24</span><span>Early voting opens; last day to register</span></li>
<li><span class="dt">Oct 25</span><span>Garret and Ariel's birthday</span></li>
<li><span class="dt">Oct 25</span><span>Dolphins at Jets &mdash; 1:00 &middot; Bills off</span></li>
<li><span class="dt">Oct 31</span><span>Halloween</span></li>
<li><span class="dt">Nov 3</span><span>Election Day</span></li>
</ul>
''')
# Sunday Spotlight after Family Today
R('''tally.so/r/obWNYP</a>.</div></div>
<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass''','''tally.so/r/obWNYP</a>.</div></div>
<h2 class="sec"><span class="o">&#127809;</span>The Sunday Spotlight<span class="o">&#127809;</span></h2>
<div class="touch-head">Your Ballot, Besides the Governor</div>
<div class="line" style="color:var(--soft)">Early voting opens Saturday. The governor's race gets the headlines; here is everything else our three towns will see, from the statewide offices down to the town. Congress and the governor are in The Ballot, further down. No endorsements. An AI wrote this section.</div>
<div class="line"><b>1. On every ballot in the state.</b> Attorney General: Democrat Letitia James, the incumbent, against Republican Saritha Komatireddy. Comptroller: Democrat Thomas DiNapoli, the incumbent, against Republican Joseph Hernandez. <b>What the jobs are:</b> the attorney general is the state's lawyer, who sues companies, defends state laws in court and handles consumer complaints; the comptroller is the state's auditor, who checks how money is spent and manages the state workers' pension fund. <b>What to know:</b> both incumbents are running again, so a vote here is mostly a vote on how they have done the job.</div>
<div class="line"><b>2. The judges (North Tonawanda and Dunkirk).</b> State Supreme Court, 8th District, which covers Erie, Niagara and Chautauqua counties: you vote for four of seven candidates. In New York, "Supreme Court" is the main trial court for big civil cases and serious crimes, not the state's highest court. Two candidates, Amodeo and Richardson, are endorsed by both parties, so the real contest is for the other two seats: Democrats Bucki and Joynt against Republicans Tripi and Hickey, with Vario on the Conservative line. <b>What it means for you:</b> judges rarely campaign hard, so this is the part of the ballot most people skip. The justices serve 14-year terms. Scottsville is in a different judicial district.</div>
<div class="line"><b>3. North Tonawanda.</b> State Senate, 62nd District: Republican Rob Ortt, the incumbent and the Senate's Republican leader, against Democrat Thomas Arida. State Assembly: the city is split. Part is in the 140th, where Democrat William Conrad, the incumbent, faces Republican challenger Faisal; part is in the open 145th, Republican Becky Wydysh against Democrat Nate McMurray, who has been pressing Wydysh to debate. County Legislature: in Districts 7, 8 and 9, Republicans Gooch, Andres and Bradt face Democrats Mooradian, Kennedy and Osborn. <b>The yes-or-no question:</b> whether the city should borrow up to $18 million for a community center at the Keller Building to replace the old youth and senior centers. It would be paid with a special property tax of about 84 cents per $1,000 of assessed value before any grants; on a house assessed at $150,000, that is about $126 a year, and grants would bring it down.</div>
<div class="line"><b>4. Dunkirk.</b> State Senate, 57th District: Republican George Borrello, the incumbent, against Democrat Victoria Guite-Williams. Assembly, 150th District: Republican Andy Molitor, the incumbent, against Democrat Carle. County: Legislature District 1, Democrat Buchanan, the incumbent, against Republican Garza; District 2, Democrat Bankoski unopposed. Family Court judge: Republican Sullivan, the incumbent, against Democrat Moss. Sheriff Quattrone, a Republican, is unopposed. No ballot questions.</div>
<div class="line"><b>5. Scottsville.</b> State Senate, 54th District: Republican Pam Helming, the incumbent, against Democrat Mills. Assembly, 139th District: Republican Steve Hawley, the incumbent, against Democrat Wolcott. District Attorney Green, a Democrat, and Wheatland Supervisor Kirch, a Republican, are unopposed. No ballot questions.</div>
<div class="line"><b>Coming down the road.</b> Saturday, Oct 24, is both the first day of early voting and the last day to register; early voting runs through Nov 1, and polls are open 6 a.m. to 9 p.m. on Election Day, Nov 3. Every county board of elections posts a sample ballot online; look yours up before you go so nothing on the back side surprises you. The race-by-race tracker is at <a href="https://benthambulletin.github.io/election/">benthambulletin.github.io/election</a>.</div>
<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass''')
S('<div class="wx">','<h2 class="sec"><span class="o">&#127810;</span>The Turning','''<div class="wx"><div class="bigtemp">60<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">Frost on the pumpkins, then a blue-sky afternoon</span>
Low <b>41&deg;</b> tonight &middot; southwest 5&ndash;15<br>Areas of frost before 9 a.m., then sunny; no rain in sight</div></div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">39<sup>&deg;</sup></div><div class="d">Clear &middot; high 60&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">43<sup>&deg;</sup></div><div class="d">Clear &middot; high 60&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">36<sup>&deg;</sup></div><div class="d">Widespread frost &middot; high 62&deg;</div></div>
</div>
<div class="strip5">
  <div><div class="d">Sun</div><div class="i">&#9728;</div><div class="h">60</div><div class="w">frost, then sunny</div></div>
  <div><div class="d">Mon</div><div class="i">&#9728;</div><div class="h">64</div><div class="w">sunny</div></div>
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">62</div><div class="w">sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#9728;</div><div class="h">62</div><div class="w">sunny</div></div>
  <div><div class="d">Thu</div><div class="i">&#127780;</div><div class="h">63</div><div class="w">mostly sunny</div></div>
</div>
<div class="line"><span class="lbl r">Frost</span> Scottsville has more frost tonight and Monday morning, at 33, and dips to 34 Tuesday night. <span class="lbl t">Outdoor window</span> All week: five dry, sunny days in the low 60s.</div>
''')
S('<div class="line"><b>Wednesday\'s report, still the latest.</b>','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','''<div class="line"><b>New numbers Wednesday.</b> A dry, sunny week should hold the color on the trees after Friday's wind. Last week's report had Niagara Falls at 50 percent and Chautauqua Institution at 70.</div>
''')
S('<div class="sky">','<div class="stars">','''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 0 50 96 Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>First quarter</b>, half lit at 12:12 p.m., in Capricorn, sets at 12:11 a.m.<br>
<span class="lbl t">Sun</span> 7:32a &ndash; 6:28p &middot; <b>10h 56m</b><br>
<span class="lbl t">Hunter's Moon</span> Mon, Oct 26</div></div>
<div class="line"><span class="lbl r">Tonight</span> A clear night: the half moon rides high in the south after dark, and Saturn is up in the east-southeast. Sunset is now before 6:30.</div>
''')
S('<div class="stars">','<div style="font-family','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>The moon reaches first quarter</b>. Halfway is a good place to check the plan. Adjust, don't abandon. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>Uranus trines Pluto</b>. Something that has been stuck starts to move. Help it along. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Mercury squares Jupiter in your sign</b>. The pep talk outruns the plan. Promise less, deliver more. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>The Sun sextiles Jupiter</b>. Good news travels a roundabout way. Listen for it. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Venus in your sign squares Pluto, within a degree</b>. Big feelings, birthday week. Let them be big. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
S('<div class="baro-top">','<h2 class="sec"><span class="o">&#10038;</span>The Ledger',baro+'''<div class="line"><span class="lbl r">Top of the week</span> 30.52, the highest reading of the week, up about a fifth of an inch since yesterday morning. It eases off slowly from here, down about a seventh of an inch by Tuesday morning.</div>
<div class="line"><span class="lbl t">The log</span> Days since the last one: Garret 12, Dad 12, Mom 9. October so far: one each.</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">Volunteer firefighter tax credit</div><div class="big">$800</div></div>
<div class="txt">Governor Hochul signed a law raising the state tax credit for volunteer firefighters and ambulance workers to $800 a year, from $200; married couples who both serve get $1,600.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Update: Pope','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>Truck Hits a Kids' Soccer Game</h3><p>A pickup drove onto a field during a children's soccer game at Wichita's Stryker Soccer Complex Saturday, killing a 6-year-old boy and a 35-year-old man. Police are investigating.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Deadly Fire at a Canadian Base</h3><p>People were killed and hurt Saturday in an incident that set off a major fire at Canadian Forces Base Wainwright in Alberta, Canada's defense minister said. Officials have not given a cause or a death toll.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Riots in Paris</h3><p>More than 1,800 people were arrested across France as protests turned violent, with looting and burned buildings. Police used tear gas on masked crowds throwing fireworks in the Place de la R&eacute;publique.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>Trump Lifts Russia Sanctions</h3><p>The president temporarily ended many of the restrictions on Russia that Congress recently passed, citing national security. Ukraine's President Zelensky said the decision "seems wrong."</p></div></div>
''')
S('<div class="ballot">','<h2 class="sec"><span class="o">&#9962;</span>The Home Wire','''<h2 class="sec"><span class="o">&#9745;</span>The Ballot<span class="o">&#9745;</span></h2>
<div class="touch-head">Sixteen Days Out</div>
<div class="line"><b>Governor.</b> Kathy Hochul leads Bruce Blakeman by 11 to 12 points in the two most recent major polls, Marist (53 to 42, Oct 1&ndash;4) and Emerson (52 to 40, Oct 3&ndash;5); Siena had it at 9 in September. Blakeman leads upstate, where all three of our towns are. One small text-message poll last week had it at 3, against every major poll. Their only debate, Tuesday, turned on utility bills, data centers and immigration enforcement. <b>What it means:</b> Hochul is still the clear favorite; no new statewide poll came out this week.</div>
<div class="line"><b>NY-26, North Tonawanda.</b> Democrat Tim Kennedy, the incumbent, against Republican Dennis Hannon. The Cook Political Report rates it solidly Democratic; Kennedy won 65 percent in 2024.</div>
<div class="line"><b>NY-23, Dunkirk.</b> Republican Nick Langworthy, the incumbent, against Democrat Aaron Gies. No public poll; the district leans Republican.</div>
<div class="line"><b>NY-25, Scottsville.</b> Democrat Joe Morelle, the incumbent, against Republican McIntyre. No public poll; Cook rates it solidly Democratic.</div>
<div class="line"><b>The state's one close House race</b> is in the Hudson Valley: Republican Mike Lawler against Democrat Cait Conley in NY-17, 48 to 46 for Conley in the one independent poll, which Cook calls a toss-up.</div>
<div class="line"><b>The national read.</b> Democrats lead the generic ballot, the question of which party you'd vote for in your House race, by about 8 to 9 points in the averages, and Cook moved 11 more House races toward them on Friday. The Senate is close to a coin flip: Democrats need a net gain of four seats, holding Michigan and Minnesota and winning four of six Republican-held races that are within the polls' margin of error. Betting markets give them a little better than 6 in 10. The president's approval is about 21 points underwater.</div>
<div class="line" style="color:var(--soft)">Early voting Oct 24&ndash;Nov 1 &middot; register by Oct 24 &middot; Election Day Nov 3, 6 a.m.&ndash;9 p.m. &middot; every race: <a href="https://benthambulletin.github.io/election/">benthambulletin.github.io/election</a></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Bill Nye','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Bills on the Bricks</h3><p>Football on the Bricks, the city's longest-running free concert series, hosts a Bills watch party at the Rochester Public Market today. Doors open at 1 p.m., with the band BBDANG at 1:30 before the 4:25 kickoff.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Dunkirk &middot; A Gold Medal Graduate</h3><p>Riley Grey Smith Mallon, a 2025 Dunkirk High School graduate, has earned the Congressional Award Gold Medal. He is now a sophomore at the Rochester Institute of Technology.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Fredonia &middot; Ability Awareness Awards</h3><p>The Resource Center holds its 37th Ability Awareness Awards on Tuesday, Nov. 3, at the White Inn in Fredonia. The luncheon honors the achievements of people with disabilities and those who support them.</p></div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Miley','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron','''<div class="wire"><div class="num">1</div><div><h3>Tarantino's Last Film Is Written</h3><p>Quentin Tarantino confirmed he has finished the script for his tenth and, he has long said, final film. He won't start on it yet; he says he wants to "live a little" first.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Iron Maiden's Last Leg</h3><p>The metal band announced a 2027 North American tour, the third and final leg of its 50th-anniversary run, starting in April.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Stars at the Academy Museum Gala</h3><p>Taylor Swift, Sabrina Carpenter and Jennifer Hudson were among the stars on the carpet at the Academy Museum's annual gala in Los Angeles. Colman Domingo, Rami Malek and Jamie Lee Curtis were there too.</p></div></div>
''')
S('<div class="touch-head">Tomorrow: 1:00 and 4:25</div>','<table class="tbl">','''<div class="touch-head">Today: 1:00 and 4:25</div>
<div class="line"><b>Jets</b> &middot; At New England, 1:00. A win over the 3&ndash;2 Patriots would put the 2&ndash;3 Jets level with them in the division. Next week, Miami at home.</div>
<div class="line"><b>Bills</b> &middot; At Las Vegas, 4:25, 4&ndash;1 against the 3&ndash;2 Raiders. A win heads into next week's bye; Baltimore visits Nov. 1.</div>
''')
S('<div class="touch-head">Tomorrow at Phoenix</div>','<h2 class="sec"><span class="o">&#9790;</span>On This Day','''<div class="touch-head">Today at Phoenix, 3:00</div>
<div class="line">The first of the last four races, on USA. Kyle Larson starts the day 49 points ahead of Denny Hamlin; Christopher Bell is 51 back and Chase Briscoe 65.</div>
<h2 class="sec"><span class="o">&#127810;</span>The Week Ahead<span class="o">&#127810;</span></h2>
<div class="line"><b>Weather.</b> Five sunny, dry days in the low 60s; frosty mornings in Scottsville.</div>
<div class="line"><b>Birthdays.</b> Claire on Friday. Garret and Ariel next Sunday, with a joint edition that morning.</div>
<div class="line"><b>The Ballot.</b> Saturday: early voting opens and registration closes.</div>
<div class="line"><b>Games.</b> Next Sunday the Jets host Miami at 1:00; the Bills are off.</div>
<div class="line"><b>The Turning.</b> New foliage report Wednesday.</div>
<div class="line"><b>Next Sunday's Spotlight.</b> How to spot an AI scam, kept short for the birthday edition.</div>
<h2 class="sec"><span class="o">&#9776;</span>The Week in the Glass<span class="o">&#9776;</span></h2>
<table class="tbl"><tr><th>Day</th><th class="n">Barometer</th><th class="n">Fcst high</th><th>Sky</th></tr>
<tr><td>Mon 12</td><td class="n">29.92</td><td class="n">69</td><td>fog, then sun</td></tr>
<tr><td>Tue 13</td><td class="n">29.80</td><td class="n">75</td><td>storms, then sun</td></tr>
<tr><td>Wed 14</td><td class="n">29.90</td><td class="n">64</td><td>mostly cloudy</td></tr>
<tr><td>Thu 15</td><td class="n">30.27</td><td class="n">61</td><td>cloudy, rain late</td></tr>
<tr><td>Fri 16</td><td class="n">29.61</td><td class="n">70</td><td>rain, wind</td></tr>
<tr><td>Sat 17</td><td class="n">30.30</td><td class="n">48</td><td>mostly sunny</td></tr>
<tr><td>Sun 18</td><td class="n">30.52</td><td class="n">60</td><td>frost, then sun</td></tr></table>
<div class="line">The wildest swing of the month: from 30.27 Thursday morning down to 29.61 Friday in the storm, about two-thirds of an inch, then back up to 30.52 this morning, the week's high. No migraines logged this week.</div>
<h2 class="sec"><span class="o">&#10023;</span>The Sunday Question<span class="o">&#10023;</span></h2>
<div class="qotd"><b>Last week: what's the fall food you only eat this time of year?</b><br><b>Ariel:</b> "Anything pumpkin flavored!!"<br><br><b>This week, for birthday week: what's the best birthday present you ever got?</b><br>Send it at tally.so/r/rjxDpl this week. Answers run here next Sunday under your names.</div>
''')
S('<div class="otd">','<h2 class="sec"><span class="o">&#10023;</span>Question of the Day','''<div class="otd"><b>October 18, 1867</b> &mdash; The United States formally took possession of Alaska from Russia in a flag ceremony at Sitka. Alaskans still mark the day as Alaska Day.</div>
''')
S('<div class="qotd">I have a trunk','<div class="dbl">','''<div class="qotd">I stand in the field all season stuffed with straw, and the crows still don't take me seriously. What am I? <i>Answer below the fold.</i></div>
''')
R("<b>Question of the Day:</b> A tree.","<b>Question of the Day:</b> A scarecrow.")
S('<div class="s">Forecast per NWS','<div class="sig">','''<div class="s">Forecast per NWS Buffalo &middot; barometer forecast via Open-Meteo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; sky computed for 14120 &middot; ballot via county boards and theballotbrief.com; polls via Marist, Emerson, Siena; ratings via Cook; national averages via Silver Bulletin and RealClearPolling; markets via Polymarket and Kalshi &middot; headlines via CBS, BBC, Rochester First, Dunkirk Observer, Variety, Billboard, Hollywood Reporter &middot; scores, schedules and NASCAR points via Sportradar</div>
''')
d['no']=116; d['date']='2026-10-18'
d['headline']="Your ballot, besides the governor · Football Sunday · Frost, then sun · Birthday week"
d['body_html']=b; d['plate_path']=None; d['plate_caption']=None
json.dump(d,open('edition-2026-10-18.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-18.json','w'),ensure_ascii=False,indent=1)
p=json.load(open('site/data/pressure.json')); p=[x for x in p if x['date']!='2026-10-18']
p.append({'date':'2026-10-18','in':30.52,'mb':1033.6,'station':'KIAG','time':'06:53 EDT'}); json.dump(p,open('site/data/pressure.json','w'),indent=1)
m=json.load(open('site/data/migraines.json')); m['updated']='2026-10-18'; json.dump(m,open('site/data/migraines.json','w'),indent=1)
print('built')
# --- review fixes ---
d=json.load(open('edition-2026-10-18.json')); b=d['body_html']
fx=[
("Their only debate, Tuesday, turned on utility bills, data centers and immigration enforcement.","In their only debate last Tuesday night they sparred over energy costs, immigration and public safety."),
("People were killed and hurt Saturday in an incident that set off a major fire at Canadian Forces Base Wainwright in Alberta, Canada's defense minister said. Officials have not given a cause or a death toll.","Several people were killed or hurt in a major fire at Canadian Forces Base Wainwright in Alberta. Officials have not given a cause or a death toll, calling the situation \"very active and delicate.\""),
("the half moon rides high in the south after dark","the half moon hangs low in the south after dark"),
("Democrat Nate McMurray, who has been pressing Wydysh to debate.","Democrat Nate McMurray, who ran for Congress in 2018 and 2020."),
("8th District, which covers Erie, Niagara and Chautauqua counties","8th District, which includes Erie, Niagara and Chautauqua counties"),
("the main trial court for big civil cases and serious crimes, not the state's highest court.","the main trial court for big civil cases, such as major lawsuits and divorces, not the state's highest court."),
("on a house assessed at $150,000, that is about $126 a year, and grants would bring it down.</div>","on a house assessed at $150,000, that is about $126 a year, and grants would bring it down. <b>Early voting:</b> Wheatfield Community Center, 2790 Church Rd, or Wendelville Fire Co., 7340 Campbell Blvd, Oct 24&ndash;Nov 1.</div>"),
("Sheriff Quattrone, a Republican, is unopposed. No ballot questions.</div>","Sheriff Quattrone, a Republican, is unopposed. No ballot questions. <b>Early voting:</b> the County Fairgrounds 4-H Building, 1089 Central Ave, Oct 24&ndash;Nov 1.</div>"),
("Wheatland Supervisor Kirch, a Republican, are unopposed. No ballot questions.</div>","Wheatland Supervisor Kirch, a Republican, are unopposed. No ballot questions. <b>Early voting:</b> the nearest sites are Henrietta Library, 625 Calkins Rd, and Gates Presbyterian, 1049 Wegman Rd; any of the county's 15 sites works, Oct 24&ndash;Nov 1.</div>"),
("A dry, sunny week should hold the color on the trees after Friday's wind. Last week's report had Niagara Falls at 50 percent and Chautauqua Institution at 70.","Last week's report, still the latest, had Niagara Falls at 50 percent color, Chautauqua Institution at 70 and Greece, in Monroe County, at 30."),
("Scottsville has more frost tonight and Monday morning, at 33, and dips to 34 Tuesday night.","Scottsville gets areas of frost again after 1 a.m. tonight and into Monday morning, with a low of 33; Tuesday night is nearly as cold, at 34."),
("30.52, the highest reading of the week, up about a fifth of an inch since yesterday morning. It eases off slowly from here, down about a seventh of an inch by Tuesday morning.","30.52, up about a fifth of an inch since yesterday morning. It drops back about a seventh of an inch between Monday morning and early Tuesday, mostly Monday afternoon."),
("The metal band announced a 2027 North American tour, the third and final leg of its 50th-anniversary run, starting in April.","The metal band announced its 2027 Run for Your Lives North American tour, starting in April. It is the third and final leg of the band's 50th-anniversary run."),
("A win over the 3&ndash;2 Patriots would put the 2&ndash;3 Jets level with them in the division. Next week, Miami at home.","They come in 2&ndash;3, two games behind Buffalo; Miami visits next Sunday at 1:00."),
("<span class=\"lbl t\">Hunter's Moon</span> Mon, Oct 26</div></div>","<span class=\"lbl t\">Hunter's Moon</span> Mon, Oct 26 &middot; <span class=\"lbl t\">New moon</span> Mon, Nov 9</div></div>"),
("No public poll; Cook rates it solidly Democratic.","No public poll; the district leans Democratic."),
]
for o,n in fx: R(o,n)
d['body_html']=b
json.dump(d,open('edition-2026-10-18.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-18.json','w'),ensure_ascii=False,indent=1)
print('fixed')
