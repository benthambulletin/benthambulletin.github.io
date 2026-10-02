import json
d=json.load(open('edition-2026-10-01.json')); b=d['body_html']
baro=open('/tmp/claude-0/-home-claude/001a10af-13f9-5479-8fec-28bf86d9c496/scratchpad/baro100.html').read(); baro=baro[:baro.index('<!--')]
baro=baro.replace('&#8212; steady overnight','&#8593; rising since 4 a.m.')
assert 'rising since' in baro
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
H=lambda o,t:f'<h2 class="sec"><span class="o">{o}</span>{t}<span class="o">{o}</span></h2>'
R('No. 99','No. 100')
R('Thursday &middot; October 1 &middot; 2026','Friday &middot; October 2 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">65&deg;</div><div class="k">Rain, then clouds</div></div>
  <div class="tile"><div class="v">29.88&#8243; &#9650;</div><div class="k">Rising as rain clears</div></div>
  <div class="tile urg"><div class="v">32</div><div class="k">Days to Election Day</div></div>
</div>
''')
# no photo yet: drop the plate block
S('<div class="plate-wrap">','<h2 class="sec"><span class="o">&#9825;</span>Family Today','')
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>Friday, and the rain is on its way out.</b> Showers end by late morning, then two dry days: sunny and 64 Saturday, 68 Sunday for the Bills and Patriots at 1:00. A good weekend to be outside.
''')
R('<div class="ask">Had a migraine? Say so in the group chat &mdash; the day and roughly when &mdash; and the paper will mark it on the Barograph. Enough entries and we will know what the glass does before one hits.</div>',
  '<div class="ask">Had a migraine? Log it at <a href="https://tally.so/r/obWNYP">tally.so/r/obWNYP</a> &mdash; who, the day, roughly when &mdash; and the paper will mark it on the Barograph. Enough entries and we will see what the pressure does before one hits.</div>')
S('<div class="wx">','<div class="towns">','''<div class="wx"><div class="bigtemp">65<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">Wet morning, dry weekend</span>
Low <b>46&deg;</b> tonight &middot; Northwest 7&ndash;12 today<br>Showers until about 11, then cloudy</div></div>
''')
S('<div class="towns">','<div class="strip5">','''<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">61<sup>&deg;</sup></div><div class="d">Rain &amp; mist &middot; high 65&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">63<sup>&deg;</sup></div><div class="d">Light rain &middot; high 64&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">64<sup>&deg;</sup></div><div class="d">Light rain &middot; high 65&deg;</div></div>
</div>
''')
S('<div class="strip5">','<h2 class="sec"><span class="o">&#127810;</span>The Turning','''<div class="strip5">
  <div><div class="d">Fri</div><div class="i">&#127782;</div><div class="h">65</div><div class="w">showers till 11</div></div>
  <div><div class="d">Sat</div><div class="i">&#9728;</div><div class="h">64</div><div class="w">sunny</div></div>
  <div><div class="d">Sun</div><div class="i">&#9728;</div><div class="h">68</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Mon</div><div class="i">&#9728;</div><div class="h">59</div><div class="w">sunny</div></div>
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">58</div><div class="w">sunny</div></div>
</div>
<div class="line"><span class="lbl t">Rain</span> Another half to three-quarters of an inch is possible before it ends late this morning. <span class="lbl t">Cooler</span> Lows in the mid-40s tonight and Saturday night; Scottsville dips to 38 Saturday night. <span class="lbl t">Outdoor window</span> Saturday through Tuesday.</div>
''')
S('<div class="line"><b>The state\'s weekly report','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','''<div class="line"><b>Still waiting on our turn.</b> This week's state report has the Adirondacks near peak and the Catskills halfway there. Around here the color usually tops out the last week of October.</div>
''')
S('<div class="sky">','<div class="stars">','''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 0 50 96 A9 46 0 0 0 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>Sixty percent</b> and waning, in Gemini, rising at 10:50 tonight.<br>
<span class="lbl t">Sun</span> 7:14a &ndash; 6:54p &middot; <b>11h 40m</b><br>
<span class="lbl t">Last quarter</span> Sat, Oct 3 &middot; <span class="lbl t">Next new moon</span> Sat, Oct 10</div></div>
<div class="line"><span class="lbl r">Tonight</span> Skies clear after dark. Saturn rises around sunset and is up all night; Jupiter and Mars are in the east before dawn.</div>
''')
S('<div class="stars">','<div style="font-family:\'LOI\'','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>Neptune in your sign sextiles Pluto almost exactly</b>, and Mars trines Neptune. Quiet changes stick today. Let something old go without making a speech about it. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>The moon crosses into your sign tonight</b>, at the tail end of Gemini all day. Save the big conversation for the weekend, when you have home field. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Mars in Leo is opposite Pluto</b>, within half a degree. Someone pushes back. Pick the one fight worth having and let the rest go by. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>The Sun in Libra trines Uranus</b>. A change of routine pays off. Take the other road home. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Mercury in your sign squares both Mars and Pluto</b> at once. Say less, mean all of it. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
S('<div class="baro-top">','<h2 class="sec"><span class="o">&#10038;</span>The Ledger',baro+'''<div class="line"><span class="lbl t">The low has passed</span> Pressure bottomed out around 4 this morning at 29.80 and is climbing again as the rain moves off &mdash; 29.88 by 6:30, up about 2.5 millibars in three hours. It is still lower than yesterday morning, but rising, so the dial drops back to low.</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">Buffalo-area pay growth</div><div class="big">6.5%</div></div>
<div class="txt">Gross pay in the Buffalo metro rose 6.5% over the past year, the fastest of the major metros ADP tracks and well above the national average.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Tennessee','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>Hochul Hands the Cornell Case to the AG</h3><p>The governor named Attorney General Letitia James special prosecutor on a former student's allegation she was gang-raped at a fraternity house in 2024, saying she had lost faith in the local DA.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>9,000 More Troops Head to the Middle East</h3><p>The new deployment comes as President Trump says the war with Iran will end "very quickly," and no later than right after the election.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Crew 13 Reaches the Space Station</h3><p>Four astronauts launched Thursday morning and docked Thursday night for a six-month stay. Four others head home after 235 days in orbit.</p></div></div>
''')
R('<b>33 days</b> to Election Day','<b>32 days</b> to Election Day')
S('<div class="wire"><div class="num">1</div><div><h3>Lewiston','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; County Parks Turn 100</h3><p>Monroe County set the first rules for its park system a century ago this week; Ellison Park opened a year later. "Parks 100" brings photo walks and other events.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Niagara Falls &middot; Goodyear Closing Its Chemical Plant</h3><p>About 85 jobs go as the company gets out of the chemical business, according to an SEC filing.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Chautauqua &middot; Measles Exposure at the ER</h3><p>The county health department says people later confirmed to have measles were in UPMC Chautauqua's emergency room in Jamestown in late September.</p></div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>A Record','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron','''<div class="wire"><div class="num">1</div><div><h3>Eddie Murphy's First TV Drama</h3><p>Peacock is developing <i>The Chairman</i> from <i>Mad Men</i> creator Matthew Weiner. If it goes ahead, it is Murphy's first live-action scripted series.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3><i>Big Brother</i> Is Coming Back Twice</h3><p>At the Season 28 finale, Julie Chen Moonves announced CBS has renewed the show for Seasons 29 and 30.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Metallica Opens at the Sphere</h3><p>Night one of the "Life Burns Faster" residency is in the books in Las Vegas, with dates scheduled through March 2027.</p></div></div>
''')
S('<div class="touch-head">Three Days to Sunday</div>','<table class="tbl">','''<div class="touch-head">Two Days to Sunday</div>
<div class="line"><b>Bills</b> &middot; Christian Benford (toe) missed a second straight practice Thursday. Keon Coleman, Joe Andreessen, Damar Hamlin (ribs) and DJ Moore (shoulder) were limited. Still no Josh Allen on the report.</div>
<div class="line"><b>Jets</b> &middot; Good news first: Minkah Fitzpatrick practiced fully Thursday. Breece Hall, Mason Taylor, Adonai Mitchell and guard Dylan Parham did not practice.</div>
''')
S('<div class="touch-head">Three Days to Las Vegas</div>','<div class="cards">','''<div class="touch-head">Two Days to Las Vegas</div>
<div class="line">Larson carries a 26-point lead over Hamlin into race five; Bell is 50 back.</div>
''')
R('<div class="otd"><b>October 1, 1971</b> &mdash; Walt Disney World opened in Florida, with the Magic Kingdom as its only park. Today it has four.</div>',
  '<div class="otd"><b>October 2, 1950</b> &mdash; <i>Peanuts</i> ran for the first time, in seven newspapers. Charlie Brown was in the very first strip.</div>')
R('What gets wetter the more it dries?','What has a neck but no head?')
R('<b>Question of the Day:</b> A towel.','<b>Question of the Day:</b> A bottle.')
R('headlines via NPR, CBS, BBC, WIVB, Niagara Gazette, Dunkirk Observer, Rochester First, Variety, Billboard &middot; injury reports via WGR and the Jets',
  'headlines via NPR, CBS, WIVB, WKBW, WXXI, Rochester First, Variety, Deadline, Billboard &middot; injury reports via the Patriots and Jets')
d.update(date='2026-10-02',no=100,body_html=b,plate_path=None,plate_caption=None,headline="Rain out by lunch, sunny weekend · Cornell case to the AG · Goodyear closing in Niagara Falls · Buffalo pay up 6.5%")
json.dump(d,open('site/data/edition-2026-10-02.json','w'),indent=1); json.dump(d,open('edition-2026-10-02.json','w'),indent=1)
p=json.load(open('site/data/pressure.json'))
if p[-1]['date']!='2026-10-02': p.append({"date":"2026-10-02","in":29.88,"mb":1011.9,"station":"KIAG","time":"06:23 EDT"})
json.dump(p,open('site/data/pressure.json','w'),indent=1)
print('ok')
