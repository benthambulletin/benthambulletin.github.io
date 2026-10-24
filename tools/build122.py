import json, subprocess
d=json.load(open('edition-2026-10-23.json')); b=d['body_html']
ballot=subprocess.run(['python3','site/tools/ballot_box.py','2026-10-24'],capture_output=True,text=True,check=True).stdout.strip()+'\n'
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
R('No. 121','No. 122')
R('Friday &middot; October 23 &middot; 2026','Saturday &middot; October 24 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">62&deg;</div><div class="k">Sunny</div></div>
  <div class="tile"><div class="v">6:19</div><div class="k">Sunset &middot; 1&frac12; min earlier</div></div>
  <div class="tile urg"><div class="v">10</div><div class="k">Days to Election Day</div></div>
</div>
''')
# no photo today
S('<div class="plate-wrap">','<div class="dbl-tight"><div class="a"></div><div class="b"></div></div>\n<h2 class="sec"><span class="o">&#9825;</span>Family Today','') if '<div class="plate-wrap">' in b else None
R('<div class="alert">&#127881; <b>Happy birthday, Claire!</b></div>\n','')
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>Early voting opens today.</b> Tomorrow is Garret and Ariel's shared birthday; safe travels to Garret, still on Long Island. Halloween is a week from today.
<div class="line" style="margin-top:.4rem"><span class="lbl t">The log</span> Garret logged one Friday at 12:25 p.m. Days since the last one: Dad 18, Mom 15. October so far: Garret two, Dad one, Mom one.</div>
''')
R('<li><span class="dt">Oct 23</span><span>Claire\'s birthday</span></li>\n','')
R('<li><span class="dt">Oct 24</span><span>Early voting opens</span></li>','<li><span class="dt">Oct 24</span><span>Early voting opens &mdash; through Nov 1</span></li>')
S('<div class="wx">','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','''<div class="wx"><div class="bigtemp">62<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">A gold-leaf Saturday: sun all day, then a near-full moon rising at dusk</span>
Low <b>40&deg;</b> tonight &middot; light south wind<br>Dry through Tuesday; warmest Sunday at 65</div></div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">36<sup>&deg;</sup></div><div class="d">Clear &middot; high 62&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">50<sup>&deg;</sup></div><div class="d">Clear &middot; high 61&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">32<sup>&deg;</sup></div><div class="d">Clear &middot; high 62&deg;</div></div>
</div>
<div class="strip5">
  <div><div class="d">Sat</div><div class="i">&#9728;</div><div class="h">62</div><div class="w">sunny</div></div>
  <div><div class="d">Sun</div><div class="i">&#9728;</div><div class="h">65</div><div class="w">sunny</div></div>
  <div><div class="d">Mon</div><div class="i">&#9728;</div><div class="h">63</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">52</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#9729;</div><div class="h">62</div><div class="w">partly sunny</div></div>
</div>
<div class="line"><span class="lbl r">Frost</span> Scottsville drops to 28 Tuesday night, North Tonawanda to 33. <span class="lbl t">Outdoor window</span> Today through Monday.</div>
<div class="line"><span class="lbl t">Away</span> Garret on Long Island: patchy frost, then partly sunny and 59 today; 41 tonight; sunny Sunday and Monday, 62 and 65.</div>
<h2 class="sec"><span class="o">&#127810;</span>The Turning<span class="o">&#127810;</span></h2>
<div class="line"><b>Western New York is turning fast.</b> This week's state foliage report lists Lewiston, Buffalo, East Aurora, Chautauqua and Jamestown among the places with the most significant change. North Tonawanda usually peaks this last week of October.</div>
''')
S('<div class="sky">','<div class="stars">','''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 1 50 96 A43 46 0 0 1 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>A waxing gibbous</b>, 97 percent lit, in Pisces, rises at 5:16 p.m. and sets at 7:05 a.m.<br>
<span class="lbl t">Sun</span> 7:40a &ndash; 6:19p &middot; <b>10h 39m</b><br>
<span class="lbl t">Hunter's Moon</span> Mon, Oct 26 &middot; <span class="lbl t">New moon</span> Mon, Nov 9</div></div>
<div class="line"><span class="lbl r">Tonight</span> The almost-full moon rises at 5:16 with Saturn close beside it; by 8 p.m. the pair sits low in the east.</div>
''')
S('<div class="stars">','<div style="font-family','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>The moon meets Saturn in your sign</b>. A serious mood, a solid plan. Write it down. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>Uranus sextiles Neptune</b>. A small change in routine feels like a vacation. Take the long way. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>The moon trines Mars in your sign</b>. Energy to burn. Rake the leaves before someone asks. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>The sun squares Pluto</b>. Someone wants control of the plan. Let them have the small stuff. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>The sun and Venus travel together in your sign</b>. Birthday eve for Garret and Ariel, and you're all in good light. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">Buffalo plows working last February</div><div class="big">14 of 36</div></div>
<div class="txt">Buffalo's new snow plan still runs into the same problem: not enough mechanics to fix the aging fleet, WKBW reports.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>No More Carriage','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>A Truce for One Ukrainian City</h3><p>The White House says First Lady Melania Trump brokered a ceasefire for Oleshky, a Russian-occupied city short of food, medicine and clean water, so aid can come in and residents can leave. Russia and Ukraine confirmed the deal, the BBC reports, and both say their forces will stop firing Monday night.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Fire at the Eagle's Nest</h3><p>Hitler's mountaintop retreat above Berchtesgaden, Germany, was engulfed in flames Friday night, and police detained a suspect. About 200 emergency workers fought the fire through difficult terrain; no one was hurt.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Births Hit a Record Low</h3><p>The U.S. birth rate fell to a record low, the latest federal data show, as fewer women in their 20s have children, NPR reports. The birth rate for women 30 to 45 is rising.</p></div></div>
''')
S('<div class="ballot">','<h2 class="sec"><span class="o">&#9962;</span>The Home Wire',ballot)
S('<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Flu','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Fewer Emergency Vets</h3><p>Emergency veterinary care is getting harder to find in the Rochester region, and Lollypop Farm says the problem is spreading nationwide, Rochester First reports. Lollypop is back to a full staff, but many clinics and shelters are not.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Niagara &amp; Erie &middot; Radiation Search Narrows</h3><p>Teams have screened 1,094 properties in Niagara and Erie counties since July, and more than 907 owners have been told no further testing is needed, WKBW reports. Forty properties were referred to the EPA, and cleanup could begin at some within weeks.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Silver Creek &middot; Senior Housing Opens Soon</h3><p>Silver Creek Senior Housing, built on the long-empty site of the old Silver Creek School on Main Street, opens in the coming weeks, the <i>Observer</i> reports. Mayor Kathy Tampio toured it and praised the project.</p></div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Ryan Gosling','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron','''<div class="wire"><div class="num">1</div><div><h3>A First Look at <i>Cliff Booth</i></h3><p>Quentin Tarantino surprised an AFI Fest crowd Friday night by showing the first 17 minutes of <i>The Further Mis-Adventures of Cliff Booth</i>, his sequel to <i>Once Upon a Time in Hollywood</i>, Deadline reports. It's the first public look at the film.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Drake Turns 40</h3><p>Drake celebrated with more than 400 guests in New York Friday night, and the Backstreet Boys showed up to sing "I Want It That Way" with him, Billboard reports. He turns 40 today.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Jay-Z Brings Out Blue Ivy</h3><p>Jay-Z brought out his daughter Blue Ivy Carter, DJ Khaled and John Legend at the first of two nights at SoFi Stadium in Los Angeles, Variety reports. He brought Brooklyn to L.A. with "Empire State of Mind."</p></div></div>
''')
S('<div class="touch-head">Bears 30, Patriots 24</div>','<table class="tbl">','''<div class="touch-head">Jets Tomorrow at 1:00</div>
<div class="line"><b>Bills</b> &middot; Defensive coordinator Jim Leonhard is using the bye to work on a defense that ranks among the NFL's worst in yards and points allowed, the AP reports. Buffalo is 5&ndash;1; Baltimore visits Nov. 1.</div>
<div class="line"><b>Jets</b> &middot; Winless Miami comes to MetLife Sunday at 1:00. A win would pull the Jets to 3&ndash;4, one game behind New England.</div>
''')
S('<div class="touch-head">Talladega Sunday</div>','<h2 class="sec"><span class="o">&#9790;</span>On This Day','''<div class="touch-head">Talladega Tomorrow</div>
<div class="line">Seven drivers sit within 56 points with three races to go; Larson leads Bell by 5.</div>
''')
S('<div class="otd">','<h2 class="sec"><span class="o">&#10023;</span>Question of the Day','''<div class="otd"><b>October 24, 1901</b> &mdash; On her 63rd birthday, schoolteacher Annie Edson Taylor became the first person to go over Niagara Falls in a barrel, and lived.</div>
''')
S('<div class="qotd">I sweep the floor','<div class="dbl">','''<div class="qotd">I'm striped yellow, orange and white, and I show up by the bagful every October. What am I? <i>Answer below the fold.</i></div>
''')
R("<b>Question of the Day:</b> A witch's broomstick.","<b>Question of the Day:</b> Candy corn.")
S('<div class="s">Forecast per NWS','<div class="sig">','''<div class="s">Forecast per NWS Buffalo, with the NWS forecast for Long Island &middot; Niagara Falls, Dunkirk and Rochester stations &middot; sky computed for 14120 &middot; foliage from the I LOVE NY report &middot; election summary from the paper's election tracker &middot; headlines via BBC, CBS, NPR, WKBW, Rochester First, Dunkirk Observer, AP, Deadline, Billboard, Variety &middot; NASCAR points via Sportradar</div>
''')
d['no']=122; d['date']='2026-10-24'
d['headline']="Early voting opens · Birthday eve · Oleshky truce · Jets host Miami tomorrow"
d['body_html']=b; d['plate_path']=None; d['plate_caption']=None
json.dump(d,open('edition-2026-10-24.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-24.json','w'),ensure_ascii=False,indent=1)
print('built')
# --- review fixes ---
d=json.load(open('edition-2026-10-24.json')); b=d['body_html']
R("<b>Jets</b> &middot; Winless Miami comes to MetLife Sunday at 1:00. A win would pull the Jets to 3&ndash;4, one game behind New England.","<b>Jets</b> &middot; Kickoff against Miami is 1:00 tomorrow at MetLife. The Jets are 2&ndash;4; the Dolphins are still looking for their first win.")
R("Garret logged one Friday at 12:25 p.m. Days since the last one: Dad 18, Mom 15.","Garret logged a migraine Friday at 12:25 p.m. Days since the last one: Garret 1, Dad 18, Mom 15.")
R("and both say their forces will stop firing Monday night.","and both say their forces will stop firing Monday night; the White House puts the start of the truce at Thursday, Oct. 29.")
R("his sequel to <i>Once Upon a Time in Hollywood</i>","the sequel to his <i>Once Upon a Time in Hollywood</i>")
R("Mayor Kathy Tampio toured it and praised the project.","Its 54 apartments are for people 62 and older; 113 people applied, so a lottery will pick the tenants.")
R("The birth rate for women 30 to 45 is rising.","The CDC says the fertility rate fell 1 percent in 2025, with a 6 percent drop among women 20 to 24, while the rate for women 30 to 45 is rising.")
R("no one was hurt.","no injuries were reported.")
R("with Saturn close beside it; by 8 p.m. the pair sits low in the east.","with Saturn about a fist's width away; by 8 p.m. the pair is a third of the way up the eastern sky.")
R("then a near-full moon rising at dusk","then a near-full moon already up by dusk")
R("Dry through Tuesday; warmest Sunday at 65","Dry all week; warmest Sunday at 65")
R("<b>The sun and Venus travel together in your sign</b>. Birthday eve for Garret and Ariel, and you're all in good light.","<b>The sun in your sign squares Pluto</b>. Birthday eve for Garret and Ariel: let someone else plan the party.")
R("<b>The sun squares Pluto</b>. Someone wants control of the plan. Let them have the small stuff.","<b>Venus squares Pluto</b>. Someone wants control of the plan. Let them have the small stuff.")
R("Seven drivers sit within 56 points with three races to go; Larson leads Bell by 5.","Larson 2,370, Bell 2,365; seven within 56 points.")
R("<b>Western New York is turning fast.</b> This week's state foliage report lists","<b>This week's state foliage report</b> lists")
d['body_html']=b
json.dump(d,open('edition-2026-10-24.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-24.json','w'),ensure_ascii=False,indent=1)
print('fixed')
