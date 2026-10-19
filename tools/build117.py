import json
d=json.load(open('edition-2026-10-18.json')); b=d['body_html']
baro=open('/tmp/claude-0/-home-claude/001a10af-13f9-5479-8fec-28bf86d9c496/scratchpad/baro117.html').read(); baro=baro[:baro.index('<!--')].strip()+'\n'
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
R('No. 116','No. 117')
R('Sunday &middot; October 18 &middot; 2026','Monday &middot; October 19 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">64&deg;</div><div class="k">Sunny, calm</div></div>
  <div class="tile"><div class="v">30.47&#8243; &#9660;</div><div class="k">Dips this afternoon</div></div>
  <div class="tile urg"><div class="v">15</div><div class="k">Days to Election Day</div></div>
</div>
''')
R('<div class="dbl-tight"><div class="a"></div><div class="b"></div></div>\n<h2 class="sec"><span class="o">&#9825;</span>Family Today','<div class="plate-wrap"><div class="frame"><span class="tick tl"></span><span class="tick tr"></span><span class="tick bl"></span><span class="tick br"></span>\n<img src="__PLATE__" alt="A woman trims the wet hair of a boy wearing a purple cape, seated on a folding chair"></div>\n<div class="plate-cap">Plate I &middot; The Family Album</div>\n<div class="plate-sub">Haircut day</div></div>\n<div class="dbl-tight"><div class="a"></div><div class="b"></div></div>\n<h2 class="sec"><span class="o">&#9825;</span>Family Today')
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>Bills 5&ndash;1 and off next week.</b> Claire's birthday is Friday, and Garret and Ariel share theirs on Sunday. Halloween is twelve days out, and the whole week runs dry and sunny.
''')
R('<li><span class="dt">Oct 18</span><span>Jets at Patriots &mdash; 1:00</span></li>\n<li><span class="dt">Oct 18</span><span>Bills at Raiders &mdash; 4:25</span></li>\n','')
# drop Sunday Spotlight
S('<h2 class="sec"><span class="o">&#127809;</span>The Sunday Spotlight','<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass','')
S('<div class="wx">','<h2 class="sec"><span class="o">&#127810;</span>The Turning','''<div class="wx"><div class="bigtemp">64<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">Blue-sky October, and a cold, clear night for porch lights</span>
Low <b>43&deg;</b> tonight &middot; southwest 5&ndash;8 today<br>Sunny all day; no rain in the forecast through Friday</div></div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">43<sup>&deg;</sup></div><div class="d">Clear &middot; high 64&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">45<sup>&deg;</sup></div><div class="d">Clear &middot; high 62&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">41<sup>&deg;</sup></div><div class="d">Frost, then sun &middot; high 66&deg;</div></div>
</div>
<div class="strip5">
  <div><div class="d">Mon</div><div class="i">&#9728;</div><div class="h">64</div><div class="w">sunny</div></div>
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">62</div><div class="w">sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#9728;</div><div class="h">60</div><div class="w">sunny</div></div>
  <div><div class="d">Thu</div><div class="i">&#9728;</div><div class="h">62</div><div class="w">sunny</div></div>
  <div><div class="d">Fri</div><div class="i">&#9728;</div><div class="h">58</div><div class="w">sunny</div></div>
</div>
<div class="line"><span class="lbl r">Frost</span> Scottsville drops to 34 Tuesday and Wednesday nights and 32 Friday night, Claire's birthday. <span class="lbl t">Outdoor window</span> Every day this week.</div>
''')
S('<div class="line"><b>New numbers Wednesday.</b>','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','''<div class="line"><b>Report day is Wednesday.</b> The state's spotters file Wednesday afternoon; their numbers run here Thursday, the last full week of October, when North Tonawanda usually peaks.</div>
''')
S('<div class="sky">','<div class="stars">','''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 0 50 96 A10 46 0 0 0 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>A waxing gibbous</b>, 60 percent lit, in Aquarius, sets at 1:17 a.m.<br>
<span class="lbl t">Sun</span> 7:34a &ndash; 6:26p &middot; <b>10h 53m</b><br>
<span class="lbl t">Hunter's Moon</span> Mon, Oct 26 &middot; <span class="lbl t">New moon</span> Mon, Nov 9</div></div>
<div class="line"><span class="lbl r">Tonight</span> Clear and cold: the moon is due south in the early evening, with Saturn up in the east-southeast. Sunset is at 6:26, a minute and a half earlier every day now.</div>
''')
S('<div class="stars">','<div style="font-family','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>The moon in Aquarius sextiles Saturn in your sign</b>. A friend's steady advice is worth taking. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>Neptune sextiles Pluto</b>. A quiet shift in the background. You'll notice it later. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Mars in your sign trines Saturn</b>. Patience pays on the hard thing. Keep at it. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>The moon trines Uranus</b>. A small surprise brightens a plain Monday. Say yes to it. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>The moon squares Venus in your sign</b>. A tender spot gets poked. Don't take it personally. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
S('<div class="baro-top">','<h2 class="sec"><span class="o">&#10038;</span>The Ledger',baro+'''<div class="line"><span class="lbl r">Big swing coming</span> 30.47, down a touch from yesterday's week high. It dips about a seventh of an inch this afternoon, most of it between noon and 3, then holds steady through Wednesday.</div>
<div class="line"><span class="lbl t">The log</span> Days since the last one: Garret 13, Dad 13, Mom 10. October so far: one each.</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">Josh Allen's TD passes, now tied</div><div class="big">Record</div></div>
<div class="txt">Allen's two touchdown passes in Las Vegas tied the Bills' career record, the AP reported. The next one breaks it.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Truck Hits','<h2 class="sec"><span class="o">&#9745;</span>The Ballot','''<div class="wire"><div class="num">1</div><div><h3>Update: Four Dead at Canadian Base</h3><p>Four Canadian service members were killed in the incident that set off a major fire at a military base in Alberta, CBS reports. Prime Minister Mark Carney called it one of the worst peacetime tragedies for the country's military.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Earhart Search Comes Up Empty</h3><p>Researchers who traveled to a remote Pacific island say the object they hoped was Amelia Earhart's plane is likely a collection of large trees that washed away. The mystery stands.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Pope Leo Back at Work</h3><p>Days after his lung cancer surgery, Pope Leo led the Sunday prayer at the Vatican and said he will resume his activities.</p></div></div>
<div class="wire"><div class="num">4</div><div><h3>Alberta Votes on Separation</h3><p>Albertans go to the polls on whether to hold a vote on leaving Canada. Polling suggests most want to stay, but the debate alone has divided the province.</p></div></div>
''')
S('<h2 class="sec"><span class="o">&#9745;</span>The Ballot','<h2 class="sec"><span class="o">&#9962;</span>The Home Wire','''<div class="ballot">&#9745; The Ballot &middot; <b>15 days</b> to Election Day &middot; early voting opens Saturday, Oct 24, and runs through Nov 1 &middot; Democrats favored for the House; the Senate close, tilting Democratic &middot; every race: <a href="https://benthambulletin.github.io/election/">benthambulletin.github.io/election</a></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Bills on the Bricks','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<div class="wire"><div class="num">1</div><div><h3>Dunkirk &middot; Marauders Win Again</h3><p>Xzavier Boland threw three touchdown passes as Dunkirk beat East Aurora/Holland 34&ndash;14 Friday at Karl Hoeppner Field. Jordan Thomas Smith caught two of them.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Orchard Park &middot; A Mural for Marv Levy</h3><p>A mural of the Hall of Fame Bills coach was unveiled Sunday at The Bryd House, painted by local artist Tara Bystrand. It carries his famous line, "Where else would you rather be than right here, right now?"</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Rochester &middot; Downtown Housing Pitches</h3><p>The mayor is backing a series of new proposals for housing downtown, WXXI reports.</p></div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Tarantino','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron','''<div class="wire"><div class="num">1</div><div><h3>Apu Speaks Again</h3><p>Voice actor Sunil Malhotra debuted as Apu on <i>The Simpsons</i> Sunday night, the character's first lines in nearly ten years. Hank Azaria gave up the role after the 2017 documentary <i>The Problem With Apu</i>.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>More <i>Ted Lasso</i>?</h3><p>Jason Sudeikis says he "would like to" make seasons 5 and 6. He once thought the show would end after season 3.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Julia Louis-Dreyfus on Broadway</h3><p>The revival of <i>Other Desert Cities</i> opened with Louis-Dreyfus in her Broadway debut, alongside Ed Harris and Allison Janney. Deadline called her "seriously funny"; The Hollywood Reporter said the play no longer feels timely.</p></div></div>
''')
S('<div class="touch-head">Today: 1:00 and 4:25</div>','<h2 class="sec"><span class="o">&#9873;</span>The Chase','''<div class="touch-head">Monday Morning Quarterback</div>
<div class="line"><b>Bills 33, Raiders 30.</b> Josh Allen threw touchdown passes to Khalil Shakir and Keon Coleman, and Tyler Bass made all four of his field goals. Las Vegas rallied to tie it at 23 early in the fourth quarter before James Cook's 3-yard run put Buffalo back ahead with 4:49 left. Bass added a 38-yarder, and the Raiders' late touchdown and onside kick came up short.</div>
<div class="line"><b>Got right:</b> no turnovers, 23 of 33 passing for Allen, and an interception on defense. <b>To fix:</b> eight penalties for 77 yards, and a fourth quarter that let Kirk Cousins throw for two touchdowns to Tre Tucker. Safety C.J. Gardner-Johnson was ejected for spitting. Buffalo is 5&ndash;1 and off next week; Baltimore visits Nov. 1.</div>
<div class="line"><b>Patriots 26, Jets 19.</b> New England led 17&ndash;3 at halftime on two Drake Maye touchdown passes. The Jets came back: Geno Smith hit Omar Cooper for a 48-yard touchdown, and Jason Sanders kicked four field goals to keep it within reach until the final minute.</div>
<div class="line"><b>Got right:</b> the defense forced three fumbles and recovered two, and Sanders went 4 for 4. <b>To fix:</b> the first half, and three sacks allowed. The Jets are 2&ndash;4; Miami, still winless, visits Sunday at 1:00.</div>
<table class="tbl"><tr><th>AFC East</th><th class="n">W</th><th class="n">L</th><th class="n">PCT</th></tr>
<tr><td style="color:var(--red)">Buffalo</td><td class="n">5</td><td class="n">1</td><td class="n">.833</td></tr>
<tr><td>New England</td><td class="n">4</td><td class="n">2</td><td class="n">.667</td></tr>
<tr><td style="color:var(--red)">N.Y. Jets</td><td class="n">2</td><td class="n">4</td><td class="n">.333</td></tr>
<tr><td>Miami</td><td class="n">0</td><td class="n">5</td><td class="n">.000</td></tr></table>
<div class="line"><b>Around the league.</b> Cleveland beat Baltimore 13&ndash;10, and Arizona won 18&ndash;16 in Los Angeles against the Rams. Kansas City beat the winless Chargers 22&ndash;6 to stay perfect, and Green Bay beat Dallas 23&ndash;13 Sunday night. San Francisco hosts Washington tonight.</div>
<div class="line"><b>The AI Editor, graded.</b> Bills 11&ndash;6: 5&ndash;1, well ahead of pace. Jets 6&ndash;11: 2&ndash;4, right on it. Ravens over Rams in the Super Bowl: a rough Sunday for both, Baltimore losing in Cleveland to fall to 4&ndash;2 and the Rams losing at home to Arizona to fall to 2&ndash;4.</div>
''')
S('<div class="touch-head">Today at Phoenix, 3:00</div>','<h2 class="sec"><span class="o">&#9790;</span>On This Day','''<div class="touch-head">Reddick Wins Phoenix</div>
<div class="line">Tyler Reddick held off Ryan Blaney by eight-tenths of a second for his sixth win of the year. Kyle Larson's day ended in the garage, and his lead is down to 5 points over Christopher Bell, who finished fourth. Chase Briscoe is 24 back, Denny Hamlin 31, Blaney 40. Three races left: Talladega Sunday, then Martinsville and Homestead.</div>
''')
S('<div class="otd">','<h2 class="sec"><span class="o">&#10023;</span>Question of the Day','''<div class="otd"><b>October 19, 1781</b> &mdash; British General Charles Cornwallis surrendered to George Washington at Yorktown, Virginia, effectively ending the fighting of the American Revolution.</div>
''')
S('<div class="qotd">I stand in the field','<div class="dbl">','''<div class="qotd">I have a neck but no head, two arms but no hands, and I come out of the closet every October when it gets cold. What am I? <i>Answer below the fold.</i></div>
''')
R("<b>Question of the Day:</b> A scarecrow.","<b>Question of the Day:</b> A sweater.")
S('<div class="s">Forecast per NWS','<div class="sig">','''<div class="s">Forecast per NWS Buffalo &middot; barometer forecast via Open-Meteo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; sky computed for 14120 &middot; election summary from the paper's election tracker &middot; headlines via CBS, BBC, Dunkirk Observer, WIVB, WXXI, Rochester First (AP), Deadline, Hollywood Reporter &middot; Phoenix results via Heavy &middot; scores, standings and NASCAR points via Sportradar</div>
''')
d['no']=117; d['date']='2026-10-19'
d['headline']="Bills 33, Raiders 30 · Patriots 26, Jets 19 · Reddick wins Phoenix · Sunny week"
d['body_html']=b; d['plate_path']='/home/claude/plate117.jpg'; d['plate_caption']='Haircut day'
json.dump(d,open('edition-2026-10-19.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-19.json','w'),ensure_ascii=False,indent=1)
p=json.load(open('site/data/pressure.json')); p=[x for x in p if x['date']!='2026-10-19']
p.append({'date':'2026-10-19','in':30.47,'mb':1031.9,'station':'KIAG','time':'06:53 EDT'}); json.dump(p,open('site/data/pressure.json','w'),indent=1)
m=json.load(open('site/data/migraines.json')); m['updated']='2026-10-19'; json.dump(m,open('site/data/migraines.json','w'),indent=1)
print('built')
