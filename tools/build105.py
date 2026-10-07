import json
d=json.load(open('edition-2026-10-06.json')); b=d['body_html']
baro=open('/tmp/claude-0/-home-claude/001a10af-13f9-5479-8fec-28bf86d9c496/scratchpad/baro105.html').read(); baro=baro[:baro.index('<!--')]
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
R('No. 104','No. 105')
R('Tuesday &middot; October 6 &middot; 2026','Wednesday &middot; October 7 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">68&deg;</div><div class="k">Windy, storms late</div></div>
  <div class="tile"><div class="v">29.88&#8243; &#9660;</div><div class="k">Falling fast</div></div>
  <div class="tile urg"><div class="v">27</div><div class="k">Days to Election Day</div></div>
</div>
''')
S('<div class="plate-wrap">','<h2 class="sec"><span class="o">&#9825;</span>Family Today','')
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>Leaf-pile weather, minus the leaf piles.</b> A warm, blustery Wednesday, gusts to 35 this afternoon, then showers and a few thunderstorms late tonight. Thursday and Friday clear out, and Saturday warms to 72.
''')
S('<div class="wx">','<div class="towns">','''<div class="wx"><div class="bigtemp">68<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">A warm wind ahead of the storms</span>
Low <b>49&deg;</b> tonight &middot; southwest 12&ndash;20, gusts to 35<br>Storms likely 11 p.m. to 2 a.m., 55 percent</div></div>
''')
S('<div class="towns">','<div class="strip5">','''<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">52<sup>&deg;</sup></div><div class="d">Clear &middot; high 68&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">54<sup>&deg;</sup></div><div class="d">Clear &middot; high 68&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">48<sup>&deg;</sup></div><div class="d">Cloudy &middot; high 70&deg;</div></div>
</div>
''')
S('<div class="strip5">','<h2 class="sec"><span class="o">&#127810;</span>The Turning','''<div class="strip5">
  <div><div class="d">Wed</div><div class="i">&#9928;</div><div class="h">68</div><div class="w">windy, storms late</div></div>
  <div><div class="d">Thu</div><div class="i">&#9728;</div><div class="h">65</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Fri</div><div class="i">&#9728;</div><div class="h">64</div><div class="w">sunny</div></div>
  <div><div class="d">Sat</div><div class="i">&#9728;</div><div class="h">72</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Sun</div><div class="i">&#127782;</div><div class="h">72</div><div class="w">showers after 2</div></div>
</div>
<div class="line"><span class="lbl r">Tonight</span> Scattered showers after 7, then showers and thunderstorms likely from 11 to 2. Rain totals stay light. <span class="lbl t">Outdoor window</span> Thursday through Saturday; Sunday's showers arrive in the afternoon.</div>
''')
S('<div class="line"><b>A new state foliage report lands tomorrow afternoon.</b>','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','''<div class="line"><b>The state's new foliage report comes out this afternoon.</b> Our county numbers run tomorrow.</div>
''')
S('<div class="sky">','<div class="stars">','''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 0 50 96 A41 46 0 0 1 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>A sliver</b>, 10 percent lit, in Virgo, rising at 5:05 a.m.<br>
<span class="lbl t">Sun</span> 7:20a &ndash; 6:46p &middot; <b>11h 26m</b><br>
<span class="lbl t">Next new moon</span> Sat, Oct 10 &middot; <span class="lbl t">Hunter's Moon</span> Mon, Oct 26</div></div>
<div class="line"><span class="lbl r">Tonight</span> Clouds and storms take the sky. The moon is nearly gone ahead of Saturday's new moon; the dark nights after it are the best stargazing of the month.</div>
''')
S('<div class="stars">','<div style="font-family:\'LOI\'','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>The Sun's opposition to Saturn in your sign is loosening</b>. The tug between what you owe and what you want lets up a little. Take the evening for yourself. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>The moon in Virgo sextiles Venus</b>. Easy warmth with the people closest by. Say yes to the visit. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Mars in your sign sextiles Uranus, exactly</b>. Try the new way of doing the old chore. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>The moon arrives in your sign, smiling at Mercury and Venus</b>. The right words come easily. Use them on someone who needs them. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Mercury and Venus stand together in your sign, still squared by Mars</b>. Settle the tense thing before the storm rolls in. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
S('<div class="baro-top">','<h2 class="sec"><span class="o">&#10038;</span>The Ledger',baro+'''<div class="line"><span class="lbl r">Big-swing day</span> 29.88 and falling fast, down about 12 millibars since yesterday morning ahead of tonight's storms.</div>
<div class="line"><span class="lbl t">The log's first entries</span> Dad logged one Tuesday about 8 a.m., Garret about 10 a.m. (the red marks above). In the 12 hours before each, pressure was climbing slowly, up about 2 millibars &mdash; a high, steady morning, not a drop. October so far: Garret 1, Dad 1, Mom 0.</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">Surprise Social Security deposit</div><div class="big">$90</div></div>
<div class="txt">Roughly 20 million people on Medicare are getting a $90 deposit from Social Security this week, part of a White House push on health costs. Check the bank account before you call about it.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>A Physics Nobel','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>Tropical Storm Isaias Forms in the Gulf</h3><p>Forecasters expect it to become a hurricane by Thursday and approach the northern Gulf Coast on Friday.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>New York Declares a Measles Emergency</h3><p>Gov. Hochul declared a state disaster emergency over measles cases spreading across rural parts of the state and neighboring states. Health departments urge anyone unsure of their vaccination status to check.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Paramount Closes Its Warner Bros. Deal</h3><p>The $110 billion merger puts two big movie studios, CBS News and CNN, and networks like Comedy Central and TNT under one roof.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>The Chemistry Nobel</h3><p>Henri Kagan and Kenso Soai won for discoveries about how chemists can steer reactions to make one "handed" version of a molecule over its mirror image, which matters for making medicines.</p></div></div>
''')
R('<b>28 days</b> to Election Day','<b>27 days</b> to Election Day')
S('<div class="wire"><div class="num">1</div><div><h3>Rochester area','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Canal Trail by UR Reopens</h3><p>The Erie Canalway Trail along the University of Rochester is open again. It has new paving, fencing, better drainage and accessibility upgrades.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>NY-23 &middot; Langworthy and Gies Debate</h3><p>Republican Rep. Nick Langworthy and Democrat Aaron Gies met Tuesday night in Elmira. Affordability and tariffs led the night.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Niagara Falls &middot; Goodyear Whistleblower Sues</h3><p>A fired state DEC engineer who raised concerns about the Goodyear plant's emissions is suing the agency, alleging civil rights violations, and wants a new arbitration hearing.</p></div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Andrew Garfield','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron','''<div class="wire"><div class="num">1</div><div><h3>Eva Marie Saint Dies at 102</h3><p>She won an Oscar for her film debut, opposite Marlon Brando in <i>On the Waterfront</i>, and starred in Hitchcock's <i>North by Northwest</i>.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3><i>Ted Lasso</i> Wraps Season Four</h3><p>The finale, "Being Alive," closed a season that branched out into AFC Richmond's women's team.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3><i>Phantom</i> Coming to Theaters</h3><p>A live stage recording of Andrew Lloyd Webber's <i>The Phantom of the Opera</i>, directed for the screen by Brett Sullivan of <i>Hadestown</i>, will play in cinemas in 2027.</p></div></div>
''')
S('<div class="touch-head">Six Days to Los Angeles</div>','<div class="pnote">','''<div class="touch-head">Five Days to Los Angeles</div>
<div class="line"><b>Bills</b> &middot; D.J. Moore's shoulder injury isn't considered long-term, but whether he plays Monday night against the Rams is still open. Keon Coleman caught the long touchdown in his place Sunday.</div>
<div class="line"><b>Jets</b> &middot; Cleveland comes in at 3&ndash;1 and well rested: the Browns haven't played since beating Pittsburgh 27&ndash;24 last Thursday. Sunday, 1:00, at home.</div>
''')
S('<div class="pnote">','</div>','<div class="pnote"><b>The Sunday Tax &middot; Week 5.</b> Picks at <a href="https://tally.so/r/RGOakJ">tally.so/r/RGOakJ</a>; standings at <a href="https://benthambulletin.github.io/pool/">benthambulletin.github.io/pool</a>. Free to play for now, straight-up winners, bragging rights on the line; a $5 buy-in may come later. Anyone with the link can play. Sheets lock at each kickoff; first game Thu 8:15 p.m., Bucs at Dallas.')
S('<div class="touch-head">Five Days to Charlotte</div>','<div class="cards">','''<div class="touch-head">Four Days to Charlotte</div>
<div class="line">The Bank of America 400 on the 1.5-mile oval Sunday afternoon. Larson brings a 40-point lead over Hamlin into race six.</div>
''')
S('<div class="otd">','<h2 class="sec">','''<div class="otd"><b>October 7, 1913</b> &mdash; Ford started its first moving assembly line at Highland Park, Michigan, cutting the time to build a Model T from hours to minutes.</div>
''')
R('I have a head and a tail but no body, and I get flipped before every kickoff. What am I?','I have a cap but no head, a stem but no flowers, and I pop up on the forest floor every October. What am I?')
R('<b>Question of the Day:</b> A coin.','<b>Question of the Day:</b> A mushroom.')
S('headlines via','</div>','headlines via CBS, NPR, WIVB, WXXI, Niagara Gazette, Deadline, Variety &middot; Bills via CBS Sports &middot; wire from the national desks')
d.update(date='2026-10-07',no=105,body_html=b,plate_path=None,plate_caption=None,headline="Windy, storms tonight · Pressure down 12 mb · First migraine log entries · Isaias in the Gulf")
json.dump(d,open('site/data/edition-2026-10-07.json','w'),indent=1); json.dump(d,open('edition-2026-10-07.json','w'),indent=1)
p=json.load(open('site/data/pressure.json'))
p=[x for x in p if x['date']!='2026-10-07']; p.append({"date":"2026-10-07","in":29.88,"mb":1011.8,"station":"KIAG","time":"05:53 EDT"})
json.dump(p,open('site/data/pressure.json','w'),indent=1)
print('ok')
