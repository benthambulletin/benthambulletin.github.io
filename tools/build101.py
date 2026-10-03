import json
d=json.load(open('edition-2026-10-02.json')); b=d['body_html']
baro=open('/tmp/claude-0/-home-claude/001a10af-13f9-5479-8fec-28bf86d9c496/scratchpad/baro101.html').read(); baro=baro[:baro.index('<!--')]
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
R('No. 100','No. 101')
R('Friday &middot; October 2 &middot; 2026','Saturday &middot; October 3 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">63&deg;</div><div class="k">Sunny all day</div></div>
  <div class="tile"><div class="v">30.31&#8243; &#9650;</div><div class="k">Big climb overnight</div></div>
  <div class="tile urg"><div class="v">31</div><div class="k">Days to Election Day</div></div>
</div>
''')
# no photo yet; drop plate and the hundredth head
S('<div class="plate-wrap">','<h2 class="sec"><span class="o">&#9825;</span>Family Today','''<div class="plate-wrap"><div class="frame"><span class="tick tl"></span><span class="tick tr"></span><span class="tick bl"></span><span class="tick br"></span>
<img src="__PLATE__" alt="Plate I"></div>
<div class="plate-cap">Plate I &middot; The Family Album</div>
<div class="plate-sub">Friday night lights under a sunset sky</div></div>
''')
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>Friday night lights have the cover</b>, the storm clouds breaking into a sunset over the field. <b>The good weekend is here:</b> sunny and 63 today, 68 tomorrow. Sunday is a full day on the couch if you want it: Bills and Patriots at 1:00, Jets at Chicago at 1:00, then Las Vegas at 5:30. Tomorrow's paper runs long.
''')
S('<div class="wx">','<div class="towns">','''<div class="wx"><div class="bigtemp">63<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">Blue sky, cool night</span>
Low <b>45&deg;</b> tonight &middot; light east wind<br>No rain for North Tonawanda until Wednesday night</div></div>
''')
S('<div class="towns">','<div class="strip5">','''<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">43<sup>&deg;</sup></div><div class="d">At dawn &middot; high 63&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">44<sup>&deg;</sup></div><div class="d">At dawn &middot; high 64&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">46<sup>&deg;</sup></div><div class="d">At dawn &middot; high 63&deg;</div></div>
</div>
''')
S('<div class="strip5">','<h2 class="sec"><span class="o">&#127810;</span>The Turning','''<div class="strip5">
  <div><div class="d">Sat</div><div class="i">&#9728;</div><div class="h">63</div><div class="w">sunny</div></div>
  <div><div class="d">Sun</div><div class="i">&#9728;</div><div class="h">68</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Mon</div><div class="i">&#9728;</div><div class="h">60</div><div class="w">sunny, breezy</div></div>
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">58</div><div class="w">sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#9728;</div><div class="h">66</div><div class="w">sunny</div></div>
</div>
<div class="line"><span class="lbl t">Chilly start</span> Scottsville drops to 38 tonight; North Tonawanda and Dunkirk to 45. <span class="lbl t">Breezy Monday</span> West wind picks up, gusting near 30 around Scottsville. <span class="lbl t">Outdoor window</span> All five days.</div>
''')
S('<div class="line"><b>Still waiting','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','''<div class="line"><b>The high country goes first.</b> Our trees usually reach peak color in the last week of October. The next state report comes Wednesday.</div>
''')
S('<div class="sky">','<div class="stars">','''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 0 50 96 Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>Last quarter</b> this morning, half lit and in Cancer, rising just after midnight.<br>
<span class="lbl t">Sun</span> 7:15a &ndash; 6:53p &middot; <b>11h 38m</b><br>
<span class="lbl t">Next new moon</span> Sat, Oct 10 &middot; <span class="lbl t">Next full moon</span> Mon, Oct 26</div></div>
<div class="line"><span class="lbl r">Tonight</span> Clear and dark until the moon comes up after midnight. Saturn sits opposite the Sun this weekend, so it is up all night and at its brightest of the year.</div>
''')
S('<div class="stars">','<div style="font-family:\'LOI\'','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>The moon in Cancer squares Saturn in your sign</b>, to within a degree. Home wants more of your time than the calendar says it has. Give it the afternoon. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>Last-quarter moon in your sign</b>, squaring the Sun. The halfway point. Finish one thing before you start the next. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Mars in Leo sextiles Uranus</b>. The plan you make up on the spot beats the careful one today. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>Your ruler Mercury is still squared by Mars and Pluto</b>. Double-check the weekend plans before everybody commits. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Venus in your sign gets a trine from the moon</b>. Warmth comes easy. Spend it on the people at your own table. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
S('<div class="baro-top">','<h2 class="sec"><span class="o">&#10038;</span>The Ledger',baro+'''<div class="line"><span class="lbl t">A big swing up</span> 30.31 this morning, up about 15 millibars since yesterday morning as high pressure moved in. The dial watches for big swings in either direction, so it reads high today even with sunshine outside.</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">Heating oil, per gallon, this winter</div><div class="big">$6.27</div></div>
<div class="txt">The state energy office expects heating oil to average $6.27 a gallon this winter, up from $3.72 &mdash; nearly 70% more.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Hochul','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>Hiring Slows to a Crawl</h3><p>The economy added 29,000 jobs in September, far fewer than in August, and unemployment rose to 4.2%.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>G7 Taps 100 Million Barrels</h3><p>The big industrial nations will release 100 million barrels of oil and fuel from their reserves, starting with diesel, to bring prices down.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Hawaii's Sea Arch Is Gone</h3><p>The 550-year-old H&#333;lei Sea Arch, a lava-rock landmark in Volcanoes National Park, collapsed into the Pacific some time last weekend.</p></div></div>
''')
R('<b>32 days</b> to Election Day','<b>31 days</b> to Election Day')
S('<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; County Parks','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; The Auto Show Ends After 118 Years</h3><p>Organizers have discontinued the Rochester Auto Show, which dates to 1908.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Hilton &middot; Apple Fest This Weekend</h3><p>Tens of thousands are expected for vendors and food run by local nonprofits; the 2024 festival drew more than 70,000.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Dunkirk &middot; Water Rates Hold Up the Budget</h3><p>Mayor Kate Wdowiasz says she can't offer her 2027 budget until the fight over proposed water rate increases is settled. Mayors usually present theirs in September.</p></div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Eddie Murphy','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron','''<div class="wire"><div class="num">1</div><div><h3>Flutie Flakes Are Back</h3><p>Nearly three decades after they first hit Buffalo shelves, Doug Flutie is bringing the cereal back to Western New York to support autism programs.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Pedro Pascal in <i>Behemoth!</i></h3><p>Tony Gilroy's first feature since 2012 casts Pascal as a classical cellist in a midlife crisis. Early reviews are split.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Stray Kids Join the Grammy Boycott</h3><p>The K-pop group is following BTS in not submitting music this year, over the Recording Academy's new Best Asian Pop category.</p></div></div>
''')
S('<div class="touch-head">Two Days to Sunday</div>','<table class="tbl">','''<div class="touch-head">Tomorrow at 1:00</div>
<div class="line"><b>Bills</b> &middot; Nobody ruled out. Christian Benford (toe) and Ray Davis (hamstring) are questionable; T.J. Sanders (illness) is doubtful. New England will be without Christian Gonzalez and Christian Barmore.</div>
<div class="line"><b>Jets</b> &middot; Minkah Fitzpatrick is back to full practice. Breece Hall, Mason Taylor, Adonai Mitchell, Dylan Parham and Kiko Mauigoa are out. Chicago is short too: Caleb Williams is out with a hamstring, and the Bears haven't named a starter.</div>
''')
S('<div class="touch-head">Two Days to Las Vegas</div>','<div class="cards">','''<div class="touch-head">Tomorrow at Las Vegas</div>
<div class="line">Race five of ten. Larson leads by 26 over Hamlin and 50 over Bell.</div>
''')
S('<div class="otd">','<h2 class="sec">','''<div class="otd"><b>October 3, 1951</b> &mdash; Bobby Thomson's ninth-inning home run beat the Dodgers and sent the Giants to the World Series: "the Shot Heard 'Round the World."</div>
''')
R('What has a neck but no head?','What has keys but can\'t open a single lock?')
R('<b>Question of the Day:</b> A bottle.','<b>Question of the Day:</b> A piano.')
R('headlines via NPR, CBS, WIVB, WKBW, WXXI, Rochester First, Variety, Deadline, Billboard &middot; injury reports via the Patriots and Jets',
  'headlines via CBS, BBC, WKBW, Rochester First, Dunkirk Observer, Deadline, Variety, Hollywood Reporter &middot; injury reports via the Patriots, Jets and Bears')
d.update(date='2026-10-03',no=101,body_html=b,plate_path='/home/claude/plate101.jpg',plate_caption='Friday night lights under a sunset sky',headline="Friday night lights · Sunny weekend · Hiring slows · Heating oil to $6.27 · Flutie Flakes are back")
json.dump(d,open('site/data/edition-2026-10-03.json','w'),indent=1); json.dump(d,open('edition-2026-10-03.json','w'),indent=1)
p=json.load(open('site/data/pressure.json'))
if p[-1]['date']!='2026-10-03': p.append({"date":"2026-10-03","in":30.31,"mb":1026.3,"station":"KIAG","time":"05:53 EDT"})
json.dump(p,open('site/data/pressure.json','w'),indent=1)
print('ok')
