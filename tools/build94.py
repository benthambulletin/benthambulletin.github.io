import json,re
d=json.load(open('site/data/edition-2026-09-25.json'))
b=d['body_html']
def R(a,c):
    global b
    assert a in b, a[:70]
    b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i)
    b=b[:i]+new+b[j:]

R('No. 93','No. 94')
R('Friday &middot; September 25 &middot; 2026','Saturday &middot; September 26 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile good"><div class="v">70&deg;</div><div class="k">Mostly sunny, 53 at dawn</div></div>
  <div class="tile"><div class="v">30.15&#8243; &#9660;</div><div class="k">Falling a second day</div></div>
  <div class="tile urg"><div class="v">38</div><div class="k">Days to Election Day</div></div>
</div>
''')
R('Under the weather, holding court from the couch. Get well, Luka.','Caught mid-cough, day two &mdash; still sick, and still not letting go of the diaper pack.')
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>Luka is still sick.</b> The fever made headlines yesterday; today it is the cough, caught here mid-hack. Day two on the couch, more cartoons, more fluids, and the whole paper is rooting for a quieter night. <b>The Harvest Moon is full today</b> at 12:48 in the afternoon, and it comes up at 6:52 this evening, thirteen minutes before sunset. Look east around seven for the big orange one. Tomorrow is a football Sunday with both teams at one o'clock, and the first rain in over a week holds off until after five.
''')
S('<ul class="cal">','</ul>','''<ul class="cal">
<li><span class="dt">Today</span><span>Harvest Moon, full at 12:48 p.m., rises 6:52 p.m.</span></li>
<li><span class="dt">Sep 27</span><span>Chargers at Buffalo, Jets at Detroit &mdash; both 1:00</span></li>
<li><span class="dt">Sep 27</span><span>Kansas, NASCAR playoffs &mdash; 3:00, USA</span></li>
<li><span class="dt">Nov 3</span><span>Election Day</span></li>
''')
# weather glass
S('<div class="wx">','<div class="towns">','''<div class="wx"><div class="bigtemp">70<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">The pick of the weekend is today</span>
Low <b>55&deg;</b> &middot; North 8&ndash;13, partly cloudy tonight<br>Rain <b>Sunday evening</b> &mdash; 30% after 5 p.m., the first in the forecast since last week</div></div>
''')
S('<div class="towns">','<div class="strip5">','''<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">53<sup>&deg;</sup></div><div class="d">Fair &middot; high 70&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">45<sup>&deg;</sup></div><div class="d">Mostly sunny &middot; high 68&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">55<sup>&deg;</sup></div><div class="d">Mostly sunny &middot; high 68&deg;</div></div>
</div>
''')
S('<div class="strip5">','<div class="line"><span class="lbl t">Outdoor window','''<div class="strip5">
  <div><div class="d">Sat</div><div class="i">&#9728;</div><div class="h">70</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Sun</div><div class="i">&#127782;</div><div class="h">67</div><div class="w">showers late</div></div>
  <div><div class="d">Mon</div><div class="i">&#9729;</div><div class="h">67</div><div class="w">mostly cloudy</div></div>
  <div><div class="d">Tue</div><div class="i">&#9925;</div><div class="h">72</div><div class="w">partly sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#9925;</div><div class="h">73</div><div class="w">partly sunny</div></div>
</div>
''')
S('<div class="line"><span class="lbl t">Outdoor window','<div class="pnote">','''<div class="line"><span class="lbl t">Yes, rain tomorrow &mdash; late</span> The Weather Service added it this morning: a 30% chance of showers Sunday <b>after 5 p.m.</b>, mostly over by 8. Clouds build through the day, so kickoff at one should be dry and the fourth quarter probably too. Scottsville gets it worse, <b>60%</b>, "showers likely". Dunkirk matches us at 30. Monday stays gray, then Thursday and Friday carry another 30% chance each. <span class="lbl t">Outdoor window</span> Today, all day.</div>
''')
S('<div class="pnote">','<h2 class="sec"><span class="o">&#127810;</span>The Turning','''<div class="pnote"><b>The nor'easter is having its worst day on Long Island today.</b> Governor Hochul declared a <b>state of emergency</b> Friday evening for Nassau, Suffolk, the city and Westchester, and Blakeman and Romaine signed their own county declarations on top of it. Coastal flood warnings cover the whole island.<br><br><b>Overnight:</b> gusts hit <b>57 mph at Oakland Gardens in Queens</b> and <b>55 at Stony Brook</b>, and about 5,000 New York customers lost power by late Friday, mostly on the island and in coastal Queens. <b>Today:</b> the heaviest rounds of rain, 2 to 4 inches on Long Island, gusts 50 to 60 on the east end. The south shore bays &mdash; Lindenhurst, Freeport, Inwood &mdash; face major flooding at high tide, two to three feet of water in spots, made worse by today's full moon.<br><br><b>When it ends:</b> easing late Sunday, clearing Monday afternoon. Cross Sound ferries are cancelled through Sunday and Suffolk has closed beach driving until Tuesday morning. PSEG Long Island outages: 1-800-490-0075, or text OUT to 773454.</div>
''')
# turning
S('<h2 class="sec"><span class="o">&#127810;</span>The Turning','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','''<h2 class="sec"><span class="o">&#127810;</span>The Turning<span class="o">&#127810;</span></h2>
<div class="line"><b>A pause in the cold.</b> After two mornings in the forties, the next five nights all run 54 to 59. Maples color fastest on cold nights and bright days, so a mild week slows things slightly. Wednesday's statewide report is the next one to watch; the three counties still show essentially no change.</div>
''')
# sky
S('<div class="sky">','<div class="stars">','''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>Full today at 12:48 p.m.</b> &mdash; the Harvest Moon, in Aries, directly opposite the sun. It rises at 6:52 this evening, thirteen minutes before sunset, which is the whole trick: over the next few nights it keeps coming up close to dusk instead of the usual fifty minutes later.<br>
<span class="lbl t">Sun</span> 7:06a &ndash; 7:05p<br>
<span class="lbl t">Next new moon</span> Sat, Oct 10 &middot; <span class="lbl t">Next full</span> Mon, Oct 26</div></div>
<div class="line"><span class="lbl r">Tonight</span> <b>Saturn</b> rises at 7:28, about a fist's width from the moon and following it up the eastern sky. <b>Jupiter</b> is up at 3:12 a.m. <b>Mars</b> leaves Cancer for Leo early Monday.</div>
''')
S('<div class="stars">','<div style="font-family:','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>The full moon is in your sign today</b>, at three degrees of Aries, sitting on Neptune almost to the minute. Full moons in your own sign bring something to a head, and Neptune asks for sleep and softness while it does. Rest is the assignment. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>Mars is in the last degree of Cancer</b>, twenty-nine and change, and crosses out early Monday. The last degree of a sign is where the push is strongest and least patient. Use it on one thing, not five. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Mars reaches your sign on Monday</b> and joins Jupiter, which has been in Leo all year. Energy is about to meet luck. The weekend is the run-up; decide what you want the push for. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>The Sun in Libra is trine Pluto today</b>, within half a degree, and your ruler Mercury is clear of every aspect. Good conditions for fixing something slowly and permanently rather than quickly. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Pluto is sextile the full moon to the exact degree</b> and trine the Sun. Venus sits quiet in your sign at eight degrees. Today's full moon works for you rather than against you; let one thing finish. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
# barograph
S('<div class="baro-top">','<h2 class="sec"><span class="o">&#10038;</span>The Ledger','''<div class="baro-top"><div class="dial">Moderate &middot; 44/100</div><div class="press">30.15&#8243;</div><div class="trend">&#8595; down again, faster</div></div>
<div class="baro"><svg viewBox="0 0 820 180" xmlns="http://www.w3.org/2000/svg">
<g font-family="AR" font-size="13" fill="#6b5f44"><line x1="64" y1="18" x2="790" y2="18" stroke="#d6cbaf"/><text x="16" y="22">30.54</text>
<line x1="64" y1="60" x2="790" y2="60" stroke="#d6cbaf"/><text x="16" y="64">30.40</text><line x1="64" y1="102" x2="790" y2="102" stroke="#d6cbaf"/><text x="16" y="106">30.26</text>
<line x1="64" y1="144" x2="790" y2="144" stroke="#d6cbaf"/><text x="16" y="148">30.12</text></g>
<polyline points="120,90 280,48 440,30 600,84 760,135" fill="none" stroke="#0e8a8a" stroke-width="3"/>
<g fill="#0e8a8a"><circle cx="120" cy="90" r="6"/><circle cx="280" cy="48" r="6"/><circle cx="440" cy="30" r="6"/><circle cx="600" cy="84" r="6"/></g>
<circle cx="760" cy="135" r="7" fill="#c8302f"/><circle cx="760" cy="135" r="15" fill="none" stroke="#c8302f" stroke-width="2.5"/>
<g font-family="AR" font-size="14" fill="#6b5f44" text-anchor="middle"><text x="120" y="174">Tue 30.30</text><text x="280" y="174">Wed 30.44</text><text x="440" y="174">Thu 30.50</text><text x="600" y="174">Fri 30.32</text></g>
<text x="760" y="174" font-family="AR" font-size="14" font-weight="700" fill="#c8302f" text-anchor="middle">Today 30.15</text></svg></div>
<div class="line"><span class="lbl t">Two days, thirty-five hundredths</span> From Thursday's record 30.50 to 30.15 this morning. The first day's drop was the high sliding off; today's is steeper, 0.17, as the high gives way on its southern side to the storm off the coast. The number itself is still perfectly ordinary. It is the speed of the fall that migraine sufferers tend to feel, which is why the dial has moved up to moderate.</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">Hours and minutes of daylight today</div><div class="big">11:59</div></div>
<div class="txt">The first day under twelve hours since mid-March. Sunrise 7:06, sunset 7:05, three hours and twenty-four minutes less light than June 21. From here it drops about three minutes a day until December.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Judge Blocks','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>Walkout at the U.N. During Netanyahu's Speech</h3><p>Dozens of delegates left the General Assembly hall as the Israeli prime minister spoke, and more than a hundred protesters were arrested outside demanding his arrest.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Senate Rejects Iran War Powers Limit, 49&ndash;50</h3><p>One vote short. The resolution would have required congressional approval for further military action against Iran.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Trump's Suit Against Iowa Pollster Thrown Out</h3><p>A judge dismissed the case against the pollster and the Des Moines Register over a pre-election poll, citing the First Amendment.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>Musk Floated for the Paramount&ndash;Warner Deal</h3><p>David Ellison is weighing Elon Musk as an investor in the proposed megamerger of Paramount and Warner Bros.</p></div></div>
''')
R('<b>39 days</b>','<b>38 days</b>')
S('<h2 class="sec"><span class="o">&#9962;</span>The Home Wire','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<h2 class="sec"><span class="o">&#9962;</span>The Home Wire<span class="o">&#9962;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; The Philharmonic Opens Its Season Tonight</h3><p>Opening night at Kodak Hall, Eastman Theatre: Dvo&#345;&aacute;k's "New World" Symphony at 7:30, with a repeat tomorrow at 2:00.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Rochester &middot; Free Day at the Memorial Art Gallery</h3><p>Hispanic Heritage Celebration Day tomorrow, noon to 4, on the theme "Together, we are more": free admission, live music and dance, community tables.</p></div></div>
''')
S('<h2 class="sec"><span class="o">&#9733;</span>The Marquee','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron','''<h2 class="sec"><span class="o">&#9733;</span>The Marquee<span class="o">&#9733;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>The Storm Cancels Sheeran at Gillette</h3><p>Both Foxborough shows, Friday and tonight, called off by the promoter over 40-to-55 mph gusts. After the Macklemore removal and the openers walking out, the stands will simply be empty. Ticketmaster refunds are automatic; next stop is Atlanta, October 3.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Global Citizen Festival Called Off</h3><p>Tonight's show on the Great Lawn in Central Park is cancelled for the same storm.</p></div></div>
''')
S('<div class="touch-head">Two Days to Sunday</div>','<table class="tbl">','''<div class="touch-head">Tomorrow at One</div>
<div class="line"><b>Bills</b> &middot; final injury report is in. <b>Out:</b> Jordan Hancock and T.J. Sanders. <b>Questionable:</b> Keon Coleman, D.J. Moore, Ed Oliver and Ar'Maj Reed-Adams. Terrel Bernard and Bradley Chubb are cleared. Clouds building at Orchard Park, 67, north wind 9 to 13, and the showers are not due until after five.</div>
<div class="line"><b>Jets</b> &middot; indoors at Ford Field, no weather to worry about. Aaron Glenn says Adonai Mitchell should be good to go despite the finger. Mason Taylor is out. Detroit is missing a guard and a safety.</div>
''')
S('<div class="touch-head">Qualifying Tomorrow at Kansas</div>','<div class="cards">','''<div class="touch-head">Qualifying Today at Kansas</div>
<div class="line">The grid gets set this afternoon for Sunday's Hollywood Casino 400. Larson carries a one-point lead over Hamlin into it, and at a mile-and-a-half track the starting spot matters more than it does most weeks.</div>
''')
S('<div class="otd">','<h2 class="sec"><span class="o">&#10023;</span>Question','''<div class="otd"><b>September 26, 1960</b> &mdash; Kennedy and Nixon met in a Chicago television studio for the first televised presidential debate. About seventy million people watched. Nixon, recovering from a hospital stay, refused makeup; Kennedy looked rested. Radio listeners scored it closer than viewers did. Thirty-eight days out from this year's election, it is still the night people point to.</div>
''')
R('I come up as the sun goes down, several nights in a row, and I once bought farmers an extra hour of work. What am I?','I have a neck but no head, and I wear a cap. What am I?')
R('<b>Question of the Day:</b> The Harvest Moon &mdash; full tomorrow at 12:48 p.m.','<b>Question of the Day:</b> A bottle.')
R('wire from the national desks','storm reports via NWS, ABC7, CBS New York, FOX Weather &middot; wire from the national desks')
d.update(date='2026-09-26',no=94,body_html=b,plate_path='/home/claude/plate94.jpg',
 plate_caption='Caught mid-cough, day two',headline="Still sick, Luka · The Harvest Moon rises tonight · The nor'easter's worst day on Long Island · Showers here late Sunday")
json.dump(d,open('site/data/edition-2026-09-26.json','w'),indent=1)
json.dump(d,open('edition-2026-09-26.json','w'),indent=1)
p=json.load(open('site/data/pressure.json'))
if p[-1]['date']!='2026-09-26': p.append({"date":"2026-09-26","in":30.15,"mb":1021.5,"station":"KIAG","time":"06:53 EDT"})
json.dump(p,open('site/data/pressure.json','w'),indent=1)
print('ok')
