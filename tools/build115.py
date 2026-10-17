import json
d=json.load(open('edition-2026-10-16.json')); b=d['body_html']
baro=open('/tmp/claude-0/-home-claude/001a10af-13f9-5479-8fec-28bf86d9c496/scratchpad/baro115.html').read(); baro=baro[:baro.index('<!--')].strip()+'\n'
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
R('No. 114','No. 115')
R('Friday &middot; October 16 &middot; 2026','Saturday &middot; October 17 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">48&deg;</div><div class="k">Mostly sunny</div></div>
  <div class="tile"><div class="v">30.30&#8243; &#9650;</div><div class="k">Leveling off</div></div>
  <div class="tile urg"><div class="v">17</div><div class="k">Days to Election Day</div></div>
</div>
''')
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>Party day.</b> The family birthday party is today, under mostly sunny skies and a high of 48. Clear and cold tonight, with patchy frost before dawn, so bring the warm coat. Tomorrow is a football doubleheader, Jets at 1:00 and Bills at 4:25.
''')
S('<div class="wx">','<h2 class="sec"><span class="o">&#127810;</span>The Turning','''<div class="wx"><div class="bigtemp">48<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">Sweater weather, and frost on the windshield by morning</span>
Low <b>35&deg;</b> tonight, patchy frost around 4 to 5 a.m. &middot; northwest 6&ndash;13<br>A stray shower before 8 a.m., 20 percent, then mostly sunny</div></div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">37<sup>&deg;</sup></div><div class="d">Mostly clear &middot; high 48&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">43<sup>&deg;</sup></div><div class="d">Cloudy &middot; high 49&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">39<sup>&deg;</sup></div><div class="d">Mostly clear &middot; high 47&deg;</div></div>
</div>
<div class="strip5">
  <div><div class="d">Sat</div><div class="i">&#127780;</div><div class="h">48</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Sun</div><div class="i">&#9728;</div><div class="h">60</div><div class="w">sunny, breezy</div></div>
  <div><div class="d">Mon</div><div class="i">&#9728;</div><div class="h">64</div><div class="w">sunny</div></div>
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">65</div><div class="w">sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#9728;</div><div class="h">64</div><div class="w">sunny</div></div>
</div>
<div class="line"><span class="lbl r">Frost</span> Scottsville drops to 29 tonight with areas of frost into Sunday morning; North Tonawanda gets patchy frost at 35; Dunkirk stays at 38. <span class="lbl t">Outdoor window</span> Every afternoon through Wednesday, sunny, with highs in the 60s from Sunday on.</div>
''')
S('<div class="line"><b>The new numbers are in.</b>','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','''<div class="line"><b>Wednesday's report, still the latest.</b> Niagara Falls 50 percent color, Lewiston 10, Chautauqua Institution 70, Greece 30. Next week's numbers come Wednesday afternoon, the week North Tonawanda usually peaks.</div>
''')
S('<div class="sky">','<div class="stars">','''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 0 50 96 A8 46 0 0 1 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>Nearly half full</b>, 41 percent lit, in Capricorn, sets at 11:07 p.m.<br>
<span class="lbl t">Sun</span> 7:31a &ndash; 6:30p &middot; <b>10h 58m</b><br>
<span class="lbl t">First quarter</span> Sun, Oct 18 &middot; <span class="lbl t">Hunter's Moon</span> Mon, Oct 26</div></div>
<div class="line"><span class="lbl r">Tonight</span> Clear skies for the drive home from the party: the moon hangs in the south after dark, and Saturn is up in the east. Daylight drops under 11 hours today, for the first time this fall.</div>
''')
S('<div class="stars">','<div style="font-family','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>The moon squares Saturn in your sign</b>. The to-do list looks long. Take it one line at a time. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>Uranus sextiles Neptune</b>. An old daydream gets a practical nudge. Write it down. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Mars in your sign trines Saturn</b>. Steady effort wins the day. Show up and keep going. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>The moon moves through Capricorn, a fellow earth sign</b>. A calm, sensible day. Enjoy the party. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Mercury in your sign squares Jupiter</b>. Big talk, thin details. Ask for the specifics. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
S('<div class="baro-top">','<h2 class="sec"><span class="o">&#10038;</span>The Ledger',baro+'''<div class="line"><span class="lbl r">The big climb</span> 30.30, up about seven-tenths of an inch since yesterday morning as the storm cleared out. Most of the rise is done; it adds about a fifth of an inch more by Monday morning, then holds steady.</div>
<div class="line"><span class="lbl t">The log</span> Days since the last one: Garret 11, Dad 11, Mom 8. October so far: one each.</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">National Grid electric bills this winter</div><div class="big">+3&ndash;5%</div></div>
<div class="txt">National Grid expects typical residential electric customers to pay 3 to 5 percent more this winter. Gas customers could see a slight decrease.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Shooting','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>Update: Pope Leo Going Home</h3><p>The Vatican says Pope Leo XIV will be discharged from the hospital today, four days after surgeons removed part of his right lung. Photos released Thursday showed him celebrating Mass in the hospital.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Press Secretary Out After Five Days</h3><p>Katie Zacharia is out as White House press secretary after five days on the job. She had confirmed earlier this week that she never passed the bar exam.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Wind-Driven Fires in California</h3><p>Santa Ana winds pushed the Norte Fire into coastal homes in Southern California, forcing thousands to evacuate. It is one of 13 fires burning across the state.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>Musk Shows a Flying Tesla</h3><p>Elon Musk unveiled a Tesla prototype with thrusters that can do aerial acrobatics, in front of a cheering crowd in Texas. It is not approved for sale or for the road.</p></div></div>
''')
S('<div class="ballot">','<h2 class="sec"><span class="o">&#9962;</span>The Home Wire','''<div class="ballot">&#9745; The Ballot &middot; <b>17 days</b> to Election Day &middot; early voting opens a week from today, Oct 24, the same day registration closes &middot; every race: <a href="https://benthambulletin.github.io/election/">benthambulletin.github.io/election</a></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Banana Ball','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Bill Nye at RIT</h3><p>Bill Nye the Science Guy is back in Rochester as the guest speaker for RIT's homecoming, Brick City Weekend. He is best known for his Emmy-winning TV series.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Chautauqua County &middot; Most Seats Contested</h3><p>Thirteen of the county's 19 legislative districts have contested races in November. Eight of those seats are held by Republicans and six by Democrats, by the <i>Observer</i>'s count.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Niagara Falls &middot; A Gondola Over the Falls?</h3><p>A Niagara Falls student at the University at Buffalo is presenting a proposal for a gondola to view the falls from above. The city already has plenty of viewpoints; this would add one in the air.</p></div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Apatow','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron','''<div class="wire"><div class="num">1</div><div><h3>Miley Sings "Jolene"</h3><p>Miley Cyrus played her first "Bass Persuades" show at the Hollywood Bowl and gave a tearful "Jolene" in tribute to Dolly Parton. "Me and Dolly, we are eternal," she told the crowd.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Harry Styles Remembers Liam Payne</h3><p>Styles premiered an unreleased song, "What Is Enough," on the second anniversary of his former One Direction bandmate's death.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Elizabeth Holmes Doc Draws a Crowd</h3><p><i>You Can See Everything</i>, a documentary about the Theranos founder, is headed for about $12 million in its opening weekend, the second-best start ever for a documentary. <i>Street Fighter</i> leads the weekend at about $30 million.</p></div></div>
''')
S('<div class="touch-head">A Sunday Doubleheader</div>','<table class="tbl">','''<div class="touch-head">Tomorrow: 1:00 and 4:25</div>
<div class="line"><b>Jets</b> &middot; At New England, 1:00. The Jets are 2&ndash;3 and coming off their win over Cleveland; the Patriots are 3&ndash;2.</div>
<div class="line"><b>Bills</b> &middot; At Las Vegas, 4:25. Buffalo is 4&ndash;1 after the overtime win in Los Angeles; the Raiders are 3&ndash;2.</div>
''')
S('<div class="touch-head">Phoenix Sunday</div>','<h2 class="sec"><span class="o">&#9790;</span>On This Day','''<div class="touch-head">Tomorrow at Phoenix</div>
<div class="line">Ryan Blaney has won the last two Cup races at Phoenix and sits fifth, 85 points back. Larson leads, Hamlin, Bell and Briscoe chase, and the green flag drops at 3 p.m. on USA.</div>
''')
S('<div class="otd">','<h2 class="sec"><span class="o">&#10023;</span>Question of the Day','''<div class="otd"><b>October 17, 1989</b> &mdash; A magnitude 6.9 earthquake hit the San Francisco Bay Area minutes before Game 3 of the World Series between the Giants and A's at Candlestick Park. The game was postponed for ten days.</div>
''')
S('<div class="qotd">I\'m picked','<div class="dbl">','''<div class="qotd">I have a trunk, branches and leaves but I'm no elephant, and every October I drop everything. What am I? <i>Answer below the fold.</i></div>
''')
R("<b>Question of the Day:</b> An apple.","<b>Question of the Day:</b> A tree.")
S('<div class="s">Forecast per NWS','<div class="sig">','''<div class="s">Forecast per NWS Buffalo &middot; barometer forecast via Open-Meteo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; sky computed for 14120 &middot; foliage per the I LOVE NY report &middot; headlines via CBS, NPR, BBC, Niagara Gazette, Rochester First, Dunkirk Observer, Hollywood Reporter, Billboard, Deadline, Variety &middot; Phoenix notes via NASCAR.com &middot; scores, standings and NASCAR points via Sportradar</div>
''')
d['no']=115; d['date']='2026-10-17'
d['headline']="Party day · Frost tonight · Pope going home · Doubleheader tomorrow"
d['body_html']=b; d['plate_path']=None; d['plate_caption']=None
json.dump(d,open('edition-2026-10-17.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-17.json','w'),ensure_ascii=False,indent=1)
p=json.load(open('site/data/pressure.json')); p=[x for x in p if x['date']!='2026-10-17']
p.append({'date':'2026-10-17','in':30.30,'mb':1026.2,'station':'KIAG','time':'06:53 EDT'}); json.dump(p,open('site/data/pressure.json','w'),indent=1)
m=json.load(open('site/data/migraines.json')); m['updated']='2026-10-17'; json.dump(m,open('site/data/migraines.json','w'),indent=1)
print('built')
