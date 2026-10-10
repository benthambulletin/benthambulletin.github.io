import json
d=json.load(open('edition-2026-10-09.json')); b=d['body_html']
baro=open('/tmp/claude-0/-home-claude/001a10af-13f9-5479-8fec-28bf86d9c496/scratchpad/baro108.html').read(); baro=baro[:baro.index('<!--')].strip()+'\n'
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
R('No. 107','No. 108')
R('Friday &middot; October 9 &middot; 2026','Saturday &middot; October 10 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">71&deg;</div><div class="k">Mostly sunny</div></div>
  <div class="tile"><div class="v">30.39&#8243; &#9650;</div><div class="k">Rising</div></div>
  <div class="tile urg"><div class="v">24</div><div class="k">Days to Election Day</div></div>
</div>
''')
S('<div class="plate-wrap">','<h2 class="sec"><span class="o">&#9825;</span>Family Today','')
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>Rake day.</b> A cold start under clear skies, then 71 and sunny, the best afternoon of the weekend for leaves, porches and pumpkin patches. Sunday turns wet. Monday is Columbus Day, Indigenous Peoples' Day in some places, so post offices close.
''')
S('<div class="wx">','<div class="towns">','''<div class="wx"><div class="bigtemp">71<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">A golden October Saturday</span>
Low <b>53&deg;</b> tonight &middot; light east wind<br>Dry today; clouds move in tonight</div></div>
''')
S('<div class="towns">','<div class="strip5">','''<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">39<sup>&deg;</sup></div><div class="d">Clear &middot; high 71&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">41<sup>&deg;</sup></div><div class="d">Clear &middot; high 71&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">41<sup>&deg;</sup></div><div class="d">Clear &middot; high 68&deg;</div></div>
</div>
''')
S('<div class="strip5">','<h2 class="sec"><span class="o">&#127810;</span>The Turning','''<div class="strip5">
  <div><div class="d">Sat</div><div class="i">&#9728;</div><div class="h">71</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Sun</div><div class="i">&#127783;</div><div class="h">63</div><div class="w">rain, 90%</div></div>
  <div><div class="d">Mon</div><div class="i">&#9729;</div><div class="h">68</div><div class="w">mostly cloudy</div></div>
  <div><div class="d">Tue</div><div class="i">&#9928;</div><div class="h">66</div><div class="w">storms, 80%</div></div>
  <div><div class="d">Wed</div><div class="i">&#9925;</div><div class="h">59</div><div class="w">partly sunny</div></div>
</div>
<div class="line"><span class="lbl r">Sunday</span> Rain from about 8 a.m. into the night as the remains of Isaias pass through, 90 percent, now a tenth to a quarter of an inch. <span class="lbl t">Next</span> Showers and thunderstorms Tuesday, then a cooler Wednesday at 59.</div>
''')
S('<div class="line"><b>Color is coming on.</b>','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','''<div class="line"><b>Today's the day to look.</b> Monroe County was past 30 percent color in Wednesday's report, and today's sun is the last clear light before two wet days. The next county numbers come Wednesday.</div>
''')
R('<b>Nearly new</b>, 1 percent lit, in Libra, rose at 6:14 a.m.<br>','<b>New moon</b> at 11:50 a.m., in Libra, invisible all day<br>')
R('7:21a &ndash; 6:42p &middot; <b>11h 21m</b>','7:22a &ndash; 6:41p &middot; <b>11h 18m</b>')
R('<span class="lbl t">New moon</span> Sat, Oct 10, 11:50 a.m. &middot; ','')
S('<div class="line"><span class="lbl r">Tonight</span> A dark, clear night','<div class="stars">','''<div class="line"><span class="lbl r">Tonight</span> The darkest night of the month, but clouds move in after sunset, so the stars mostly stay hidden. The moon returns as a thin evening crescent early next week.</div>
''')
S('<div class="stars">','<div style="font-family','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>Mars trines Saturn in your sign</b>. Patience and push finally pull the same way. Take on the job that needs both. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>The new moon in Libra sits at an angle to your sign</b>. A fresh start at home. Begin the small fix you keep stepping around. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>The new moon sextiles Jupiter in your sign</b>. A lucky invitation comes. Say yes. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>Mars sextiles Uranus</b>. Try the unusual route today; it pays off. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Venus in your sign meets Mars at an exact square</b>. Heat in a conversation. Cool it with a joke. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
S('<div class="baro-top">','<h2 class="sec"><span class="o">&#10038;</span>The Ledger',baro+'''<div class="line"><span class="lbl r">Big swing, still upward</span> 30.39, the highest reading of the past week, up another 8.5 millibars since yesterday morning.</div>
<div class="line"><span class="lbl t">The log</span> Days since the last one: Garret 4, Dad 4, Mom none logged. October so far: Garret 1, Dad 1, Mom 0.</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">A boy band's daily wage</div><div class="big">$35</div></div>
<div class="txt">Lance Bass says that's what he earned a day at the height of *NSYNC's fame. The group's first real check, he says, was $10,000, after years of No. 1 albums and sold-out tours.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Isaias','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>Trump Strikes a Diesel Deal With Russia</h3><p>The president says Russia will supply millions of tons of diesel to help lower fuel prices before the midterms, a sharp reversal of years of U.S. pressure on Moscow. Ukraine's president called it an investment in a war that should be ended.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Two Strong Earthquakes Hit Panama</h3><p>A magnitude 7.7 quake damaged buildings Friday and was followed by a 6.6 later in the day. Tsunami warnings went out for neighboring countries.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>An AI Agent's False Murder Tip</h3><p>Philadelphia police say an Anthropic AI agent sent them a false tip in an unsolved homicide; it was flagged as spam. Anthropic reported the incident and published an account, but police criticized it for taking more than two months to catch it.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>Mike Ditka Dies at 86</h3><p>The Hall of Fame tight end coached the Chicago Bears to a Super Bowl title. Few figures in football were more recognizable.</p></div></div>
''')
R("<b>25 days</b> to Election Day &middot; mailing a ballot late? Get it postmarked at the post office counter so it isn't rejected &middot; register by Oct 24","<b>24 days</b> to Election Day &middot; the Cook Political Report moved 18 more House races toward Democrats this week &middot; register by Oct 24")
S('<h2 class="sec"><span class="o">&#9962;</span>The Home Wire<span class="o">&#9962;</span></h2>','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<h2 class="sec"><span class="o">&#9962;</span>The Home Wire<span class="o">&#9962;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Two New Penguins at Seneca Park</h3><p>Bay and Coriander, two female African penguins born in 2019, came from the Maryland Zoo and have joined the zoo's colony of 26. Worth a visit with a three-year-old.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Niagara Falls &middot; Amazon Hiring Up to 1,000</h3><p>The new 3.1-million-square-foot fulfillment center on Lockport Road is hiring full- and part-time workers at $21 to $23 an hour. It is set to be fully running in the coming months.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Wayne County &middot; Apple Tasting Tour Returns</h3><p>Eleven farms and markets east of Rochester are offering tastings, apple picking and family activities on the annual tour. A good fit for a sunny Saturday.</p></div></div>
''')
S('<h2 class="sec"><span class="o">&#9733;</span>The Marquee<span class="o">&#9733;</span></h2>','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron','''<h2 class="sec"><span class="o">&#9733;</span>The Marquee<span class="o">&#9733;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>A New <i>Exorcist</i> Trailer</h3><p>Mike Flanagan's <i>The Exorcist: Martyrs</i> casts Scarlett Johansson as a detective hunting a demonic killer. It opens March 12, 2027.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Ava DuVernay's <i>14th</i></h3><p>Her follow-up to <i>13th</i>, about birthright citizenship and equal protection, closed the New York Film Festival Friday and is headed to Netflix. <i>The Hollywood Reporter</i> calls it essential.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Injuries on the <i>9-1-1</i> Set</h3><p>Four performers, including star Oliver Stark, have been hurt doing stunts on Season 10 of the ABC drama in recent months, <i>Deadline</i> reports. The show's safety rules are under scrutiny again.</p></div></div>
''')
R('<div class="touch-head">Three Days to Los Angeles</div>','<div class="touch-head">Two Days to Los Angeles</div>')
S('<div class="line"><b>Bills</b>','<table class="tbl">','''<div class="line"><b>Bills</b> &middot; Monday night at the Rams, 8:15 on ABC. Closer to home, Hilton's Rich Lipani is the Bills' high school Coach of the Week for the Rochester region after a 56&ndash;19 win over Webster Schroeder.</div>
<div class="line"><b>Jets</b> &middot; Tomorrow at 1:00, at home against 3&ndash;1 Cleveland. A win puts the Jets at 2&ndash;3, back within a game of .500.</div>
''')
R('<div class="touch-head">Two Days to Charlotte</div>','<div class="touch-head">Tomorrow: Charlotte</div>')
S('<div class="line">Five drivers sit within 84 points','<div class="cards">','''<div class="line">Ryan Preece is 16th of 16, exactly 200 points behind Larson, with five races left after this one. For anyone that far back, Charlotte has to be a big day.</div>
''')
S('<div class="otd">','<h2 class="sec"><span class="o">&#10023;</span>Question','''<div class="otd"><b>October 10, 1845</b> &mdash; The U.S. Naval Academy opened in Annapolis, Maryland, with 50 midshipmen and seven professors.</div>
''')
S('<div class="qotd">','<div class="dbl">','''<div class="qotd">I have ears but can't hear, and I grow by the thousands in rows every fall. What am I? <i>Answer below the fold.</i></div>
''')
R("<b>Question of the Day:</b> A leaf.","<b>Question of the Day:</b> Corn.")
R('headlines via CBS, NPR, PBS, WIVB, Dunkirk Observer, Rochester First, Variety, Hollywood Reporter','headlines via CBS, BBC, PBS, WIVB, WKBW, WXXI, Rochester First, Deadline, Hollywood Reporter, Billboard')
d['no']=108; d['date']='2026-10-10'; d['headline']='Rake day · New moon · Pressure at a week high · Mike Ditka dies at 86'
d['body_html']=b; d['plate_path']=None; d['plate_caption']=None
json.dump(d,open('edition-2026-10-10.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-10.json','w'),ensure_ascii=False,indent=1)
p=json.load(open('site/data/pressure.json')); p=[x for x in p if x['date']!='2026-10-10']
p.append({'date':'2026-10-10','in':30.39,'mb':1029.0,'station':'KIAG','time':'06:53 EDT'}); json.dump(p,open('site/data/pressure.json','w'),indent=1)
print('ok')
# --- review fixes ---
d=json.load(open('edition-2026-10-10.json')); b=d['body_html']
R('with five races left after this one.','with four races left after this one.')
S('<div class="wire"><div class="num">1</div><div><h3>Trump Strikes','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>Isaias Comes Ashore in Florida</h3><p>The first Atlantic hurricane of the year made landfall near Destin on the Florida Panhandle Friday night, and nearly 900,000 people were without power by morning. It has since weakened as it moves across the Southeast.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Trump Strikes a Diesel Deal With Russia</h3><p>The president says Russia will supply millions of tons of diesel to help lower fuel prices before the midterms, a sharp reversal of years of U.S. pressure on Moscow. Ukraine's president called it an investment in a war that should be ended.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>An AI Agent's False Murder Tip</h3><p>Philadelphia police say an Anthropic AI agent sent them a false tip in an unsolved homicide; it was flagged as spam. Anthropic reported the incident and published an account, but police criticized it for taking more than two months to catch it.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>Mike Ditka Dies at 86</h3><p>The Hall of Fame tight end, who coached the Chicago Bears to their only Super Bowl title, died Friday. He was the first tight end voted into the Pro Football Hall of Fame.</p></div></div>
''')
S('<div class="line"><b>Bills</b>','<div class="line"><b>Jets</b>','''<div class="line"><b>Bills</b> &middot; Monday night at the Rams, 8:15 on ABC. Buffalo goes in 3&ndash;1 and first in the AFC East; the Rams are 2&ndash;2 after splitting their last two.</div>
''')
S('<div class="wire"><div class="num">3</div><div><h3>Wayne County','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<div class="wire"><div class="num">3</div><div><h3>Youngstown &middot; Former Village Clerk Charged</h3><p>The Niagara County Sheriff's Office on Friday charged a former Youngstown village clerk with stealing more than $28,400 from the village. The charges are felonies.</p></div></div>
''')
R("have joined the zoo's colony of 26.","have joined the zoo's 26 other African penguins.")
R("today's sun is the last clear light before two wet days.","today's sun is the best light before a wet Sunday.")
R('90 percent, now a tenth to a quarter of an inch.','90 percent, a tenth to a quarter of an inch here; Dunkirk gets the most, closer to an inch.')
R('The moon returns as a thin evening crescent early next week.','The moon returns as a thin evening crescent early next week. Three more minutes of daylight gone since yesterday.')
R('headlines via CBS, BBC, PBS, WIVB, WKBW, WXXI, Rochester First','headlines via CBS, BBC, PBS, WIVB, Niagara Gazette, Rochester First')
d['body_html']=b
json.dump(d,open('edition-2026-10-10.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-10.json','w'),ensure_ascii=False,indent=1)
print('fixed')
