import json
d=json.load(open('edition-2026-10-08.json')); b=d['body_html']
baro=open('/tmp/claude-0/-home-claude/001a10af-13f9-5479-8fec-28bf86d9c496/scratchpad/baro107.html').read(); baro=baro[:baro.index('<!--')].strip()+'\n'
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
R('No. 106','No. 107')
R('Thursday &middot; October 8 &middot; 2026','Friday &middot; October 9 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">66&deg;</div><div class="k">Sunny</div></div>
  <div class="tile"><div class="v">30.14&#8243; &#9650;</div><div class="k">Rising fast</div></div>
  <div class="tile urg"><div class="v">25</div><div class="k">Days to Election Day</div></div>
</div>
''')
S('<div class="plate-wrap">','<h2 class="sec"><span class="o">&#9825;</span>Family Today','')
S('<div class="alert">','<ul class="cal">','''<div class="fam"><b>A frosty-windshield kind of morning, minus the frost.</b> Clear and cold at dawn, then a bright Friday afternoon. Get the leaves raked Saturday; Sunday belongs to the rain and the Jets.
''')
R('<li><span class="dt">Today</span><span>Ariel and Tom&rsquo;s 3rd anniversary</span></li>\n','')
S('<div class="wx">','<div class="towns">','''<div class="wx"><div class="bigtemp">66<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">Crisp sun, a cold clear night</span>
Low <b>42&deg;</b> tonight &middot; west 6&ndash;15, then light north<br>Dry today and tonight</div></div>
''')
S('<div class="towns">','<div class="strip5">','''<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">43<sup>&deg;</sup></div><div class="d">Clear &middot; high 66&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">45<sup>&deg;</sup></div><div class="d">Clear &middot; high 64&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">45<sup>&deg;</sup></div><div class="d">Clear &middot; high 66&deg;</div></div>
</div>
''')
S('<div class="strip5">','<h2 class="sec"><span class="o">&#127810;</span>The Turning','''<div class="strip5">
  <div><div class="d">Fri</div><div class="i">&#9728;</div><div class="h">66</div><div class="w">sunny</div></div>
  <div><div class="d">Sat</div><div class="i">&#9728;</div><div class="h">72</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Sun</div><div class="i">&#127783;</div><div class="h">65</div><div class="w">rain, 90%</div></div>
  <div><div class="d">Mon</div><div class="i">&#9729;</div><div class="h">68</div><div class="w">mostly cloudy</div></div>
  <div><div class="d">Tue</div><div class="i">&#127782;</div><div class="h">66</div><div class="w">chance showers</div></div>
</div>
<div class="line"><span class="lbl r">Sunday</span> What's left of Hurricane Isaias brings rain from about 8 a.m. into the night, 90 percent, a quarter to half an inch. Scottsville dips to 39 tonight, the coldest of the three towns. <span class="lbl t">Outdoor window</span> Today and Saturday.</div>
''')
S('<div class="line"><b>Monroe County is turning fast.</b>','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','''<div class="line"><b>Color is coming on.</b> Wednesday's state report had Greece, the Monroe County reading nearest Scottsville, past 30 percent. Saturday's sun is the best light of the weekend to see it; the next report lands Wednesday.</div>
''')
R('<b>A thin sliver</b>, 5 percent lit, in Virgo, rose at 5:04 a.m.<br>','<b>Nearly new</b>, 1 percent lit, in Libra, rose at 6:14 a.m.<br>')
R('7:20a &ndash; 6:44p &middot; <b>11h 24m</b>','7:21a &ndash; 6:42p &middot; <b>11h 21m</b>')
R('<span class="lbl t">Next new moon</span> Sat, Oct 10','<span class="lbl t">New moon</span> Sat, Oct 10, 11:50 a.m.')
S('<div class="line"><span class="lbl r">Tonight</span> Clear skies and almost no moon.','<div class="stars">','''<div class="line"><span class="lbl r">Tonight</span> The darkest, clearest night of the week: no moon at all and a cold, dry sky. Saturn is up in the east after dark. Sunset now comes before 6:45.</div>
''')
S('<div class="stars">','<div style="font-family','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>The moon sits across the sky from you, opposite Neptune in your sign</b>. Things look foggier than they are. Sleep on the big decision. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>Uranus trines Pluto in the background</b>. A slow change at home finally settles into place. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>The moon sextiles Mars in your sign</b>. Energy for the weekend list. Start with the hardest job. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>The moon leaves your sign for Libra</b>. Attention turns to money. Look at the one bill you've been avoiding. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Venus in your sign squares Mars, nearly exact</b>. Pick the gentle word; it wins today. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
S('<div class="baro-top">','<h2 class="sec"><span class="o">&#10038;</span>The Ledger',baro+'''<div class="line"><span class="lbl r">Big swing, upward</span> 30.14 and still climbing, up about 10 millibars since yesterday morning as high pressure builds in behind the storm.</div>
<div class="line"><span class="lbl t">The log</span> Days since the last one: Garret 3, Dad 3, Mom none logged. October so far: Garret 1, Dad 1, Mom 0.</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">Days at sea</div><div class="big">321</div></div>
<div class="txt">The carrier USS Abraham Lincoln and its 4,500-plus sailors got home to San Diego Thursday after 321 days away, a record run supporting the Iran war. Families met them on the pier.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Margaret','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>Navi Pillay Wins the Nobel Peace Prize</h3><p>The South African human rights lawyer and former international judge was honored for advancing human rights and international law. She served on the International Criminal Court, which the Trump administration sanctioned last year.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Army Report on the D.C. Midair Crash</h3><p>The Army's review found failures in air traffic control, helicopter routes, training and safety practices, and called for fixes. It was finished in May and released Thursday after pressure from victims' families.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Teen Chatbot Safeguards Fall Short</h3><p>A Common Sense Media study found most of the safeguards in ChatGPT for Teens failed its tests. Among the gaps: the bot doesn't alert parents when a teen talks about self-harm.</p></div></div>
''')
R('<b>26 days</b> to Election Day &middot; new Marist poll: Hochul leads Blakeman by 11 among registered voters, Blakeman leads upstate &middot; register by Oct 24','<b>25 days</b> to Election Day &middot; mailing a ballot late? Get it postmarked at the post office counter so it isn\'t rejected &middot; register by Oct 24')
S('<h2 class="sec"><span class="o">&#9962;</span>The Home Wire<span class="o">&#9962;</span></h2>','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<h2 class="sec"><span class="o">&#9962;</span>The Home Wire<span class="o">&#9962;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; A NASA Telescope Built Here</h3><p>NASA picked L3Harris to design, build and test a telescope for LISA, a space mission to detect ripples in space-time, and the company says the work will be done in Rochester. The mission is led by the European Space Agency.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Fredonia &middot; New School Playgrounds Open</h3><p>Both Wheelock school playgrounds are finished: Chestnut Street opened in late September and Main Street on Oct. 7. Construction delays had pushed the work into the school year.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>North Tonawanda &middot; New Charge in Car Show Crash</h3><p>Charles Brancato, 73, of Tonawanda was arraigned Thursday on a charge of second-degree vehicular assault, North Tonawanda police said. Eight people were hurt when his car went into the crowd at a September car show.</p></div></div>
''')
S('<h2 class="sec"><span class="o">&#9733;</span>The Marquee<span class="o">&#9733;</span></h2>','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron','''<h2 class="sec"><span class="o">&#9733;</span>The Marquee<span class="o">&#9733;</span></h2>
<div class="wire"><div class="num">1</div><div><h3><i>Avatar: Seven Havens</i> Arrives</h3><p>The creators of <i>The Last Airbender</i> are back with a new Paramount+ series set after <i>The Legend of Korra</i>. <i>Variety</i> calls its postapocalyptic turn intriguing; <i>The Hollywood Reporter</i>, promising.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>The Coven Returns</h3><p>Jessica Lange, Sarah Paulson and the <i>Coven</i> cast are back for the 13th season of FX's <i>American Horror Story</i>. Ryan Murphy lured some of them back after years away, just in time for Halloween.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Gromit Speaks</h3><p>Martin Freeman will voice Gromit, Wallace's famously silent dog, in the audiobook of Gromit's autobiography. It's the first time the character has ever spoken.</p></div></div>
''')
R('<div class="touch-head">Four Days to Los Angeles</div>','<div class="touch-head">Three Days to Los Angeles</div>')
S('<div class="line"><b>Bills</b>','<div class="pnote">','''<div class="line"><b>Bills</b> &middot; The Rams come in 2&ndash;2, splitting their last two: a 30&ndash;26 loss at Denver, then a 24&ndash;20 win at Philadelphia. Buffalo is 3&ndash;1 and still first in the AFC East.</div>
<div class="line"><b>Jets</b> &middot; Cleveland's 3&ndash;1 has them tied with Baltimore atop the AFC North, so Sunday is a real test at home. A win gets the Jets back in the mix.</div>
<div class="line"><b>Thursday night</b> &middot; Tampa Bay 24, Dallas 16, an upset: Sportradar's model had given the Bucs a 20 percent chance.</div>
''')
S('<div class="pnote">','<table class="tbl">','')
R('<div class="touch-head">Three Days to Charlotte</div>','<div class="touch-head">Two Days to Charlotte</div>')
S('<div class="line">Hamlin has won','<div class="cards">','''<div class="line">Five drivers sit within 84 points of Larson going to Charlotte: Hamlin, Bell, Logano, Blaney and Chase Briscoe. Tyler Reddick has the most wins of the 16 this year, five, but sits seventh.</div>
''')
S('<div class="otd">','<h2 class="sec"><span class="o">&#10023;</span>Question','''<div class="otd"><b>October 9, 1888</b> &mdash; The Washington Monument opened to the public. Workers had set its capstone four years earlier, and at 555 feet it was then the tallest structure in the world.</div>
''')
S('<div class="qotd">','<div class="dbl">','''<div class="qotd">I turn without moving, fall without getting hurt, and get raked into a pile every October. What am I? <i>Answer below the fold.</i></div>
''')
R("<b>Question of the Day:</b> A jack-o'-lantern.","<b>Question of the Day:</b> A leaf.")
R('headlines via CBS, NPR, BBC, PBS, WKBW, Niagara Gazette, Rochester First, Variety, Hollywood Reporter, Billboard, Deadline','headlines via CBS, NPR, PBS, WIVB, Dunkirk Observer, Rochester First, Variety, Hollywood Reporter')
d['no']=107; d['date']='2026-10-09'; d['headline']='Crisp and clear · Isaias rain Sunday · Pressure up 10 mb · Pillay wins the Peace Prize'
d['body_html']=b; d['plate_path']=None; d['plate_caption']=None
json.dump(d,open('edition-2026-10-09.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-09.json','w'),ensure_ascii=False,indent=1)
p=json.load(open('site/data/pressure.json')); p=[x for x in p if x['date']!='2026-10-09']
p.append({'date':'2026-10-09','in':30.14,'mb':1020.5,'station':'KIAG','time':'06:53 EDT'}); json.dump(p,open('site/data/pressure.json','w'),indent=1)
print('ok')
# --- review fixes ---
d=json.load(open('edition-2026-10-09.json')); b=d['body_html']
R('<div class="cap">Days at sea</div>','<div class="cap">Days away</div>')
R('after 321 days away, a record run supporting the Iran war.','after 321 days away, a record stretch of unbroken time at sea supporting the Iran war.')
R(' as high pressure builds in behind the storm.',' as high pressure builds in.')
R("an upset: Sportradar's model had given the Bucs a 20 percent chance.","an upset: the Bucs went in with about a 1-in-5 chance.")
R('<div class="wire"><div class="num">1</div><div><h3>Navi Pillay','''<div class="wire"><div class="num">1</div><div><h3>Isaias Takes Aim at the Gulf Coast</h3><p>The first Atlantic hurricane of the year is forecast to strengthen to Category 3 before landfall somewhere between Mississippi and the Florida Panhandle. Forecasters expect heavy rain and possible flash flooding.</p></div></div>
<div class="wire"><div class="num">1</div><div><h3>Navi Pillay''')
b=b.replace('<div class="num">1</div><div><h3>Navi Pillay','<div class="num">2</div><div><h3>Navi Pillay',1)
R('<div class="num">2</div><div><h3>Army Report','<div class="num">3</div><div><h3>Army Report')
R('<div class="num">3</div><div><h3>Teen Chatbot','<div class="num">4</div><div><h3>Teen Chatbot')
R("What's left of Hurricane Isaias brings rain from about 8 a.m. into the night","Isaias's leftovers are expected to bring rain from about 8 a.m. into the night")
R("The Army's review found failures","The Army's review of the January 2025 collision of an Army helicopter and an American Airlines jet over the Potomac, which killed 67, found failures")
R('<b>A frosty-windshield kind of morning, minus the frost.</b> Clear and cold at dawn, then a bright Friday afternoon.','<b>Sweater weather at the bus stop.</b> Clear and chilly at dawn, low 40s, then a bright Friday afternoon.')
R('The darkest, clearest night of the week: no moon at all and a cold, dry sky. Saturn is up in the east after dark. Sunset now comes before 6:45.','A dark, clear night: no moon at all and a chilly, dry sky, down to the low 40s. Sunset now comes before 6:45.')
R('<b>Venus in your sign squares Mars, nearly exact</b>. Pick the gentle word; it wins today.','<b>The moon goes quiet in Libra, the sign just before yours</b>. Rest up this weekend; birthday season starts in two weeks.')
R('Tyler Reddick has the most wins of the 16 this year, five, but sits seventh.','Tyler Reddick has the most wins of the 16 this year, five, but sits seventh, 106 back. Sunday is the sixth of 10 races; most points at Homestead on Nov. 8 takes the title.')
d['body_html']=b
json.dump(d,open('edition-2026-10-09.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-09.json','w'),ensure_ascii=False,indent=1)
R('Crisp sun, a cold clear night','Crisp sun, a chilly clear night')
d['body_html']=b
json.dump(d,open('edition-2026-10-09.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-09.json','w'),ensure_ascii=False,indent=1)
print('fixed')
