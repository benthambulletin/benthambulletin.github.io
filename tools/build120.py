import json, subprocess
d=json.load(open('edition-2026-10-21.json')); b=d['body_html']
ballot=subprocess.run(['python3','site/tools/ballot_box.py','2026-10-22'],capture_output=True,text=True,check=True).stdout.strip()+'\n'
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
R('No. 119','No. 120')
R('Wednesday &middot; October 21 &middot; 2026','Thursday &middot; October 22 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">62&deg;</div><div class="k">Mostly sunny</div></div>
  <div class="tile"><div class="v">6:22</div><div class="k">Sunset</div></div>
  <div class="tile urg"><div class="v">12</div><div class="k">Days to Election Day</div></div>
</div>
''')
R('<div class="dbl-tight"><div class="a"></div><div class="b"></div></div>\n<h2 class="sec"><span class="o">&#9825;</span>Family Today','<div class="plate-wrap"><div class="frame"><span class="tick tl"></span><span class="tick tr"></span><span class="tick bl"></span><span class="tick br"></span>\n<img src="__PLATE__" alt="A smiling little boy in a blue jacket sits on a gym bleacher beside a young woman in black and orange warmups"></div>\n<div class="plate-cap">Plate I &middot; The Family Album</div>\n<div class="plate-sub">Bleacher buddies</div></div>\n<div class="dbl-tight"><div class="a"></div><div class="b"></div></div>\n<h2 class="sec"><span class="o">&#9825;</span>Family Today')
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>Claire's birthday is tomorrow.</b> Garret and Ariel share theirs Sunday, safe travels to Garret on Long Island, and Halloween is nine days out.
<div class="line" style="margin-top:.4rem"><span class="lbl t">The log</span> Days since the last migraine: Garret 16, Dad 16, Mom 13. October so far: one each.</div>
''')
R('<li><span class="dt">Oct 23</span><span>Claire\'s birthday</span></li>','<li><span class="dt">Oct 22</span><span>Patriots at Bears &mdash; 8:15, Prime Video</span></li>\n<li><span class="dt">Oct 23</span><span>Claire\'s birthday</span></li>')
S('<div class="wx">','<h2 class="sec"><span class="o">&#127810;</span>The Turning','''<div class="wx"><div class="bigtemp">62<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">Frost on the windshield again, then a bright, sweater-weather afternoon</span>
Low <b>38&deg;</b> tonight &middot; light northwest wind<br>Dry through Sunday; Monday's rain chance is near zero</div></div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">34<sup>&deg;</sup></div><div class="d">Clear &middot; high 62&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">32<sup>&deg;</sup></div><div class="d">Clear &middot; high 59&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">32<sup>&deg;</sup></div><div class="d">Clear &middot; high 61&deg;</div></div>
</div>
<div class="strip5">
  <div><div class="d">Thu</div><div class="i">&#9728;</div><div class="h">62</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Fri</div><div class="i">&#9728;</div><div class="h">58</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Sat</div><div class="i">&#9728;</div><div class="h">63</div><div class="w">sunny</div></div>
  <div><div class="d">Sun</div><div class="i">&#9728;</div><div class="h">64</div><div class="w">sunny</div></div>
  <div><div class="d">Mon</div><div class="i">&#9728;</div><div class="h">65</div><div class="w">mostly sunny</div></div>
</div>
<div class="line"><span class="lbl r">Frost</span> Friday night, Claire's birthday, drops to 28 in Scottsville and 34 in North Tonawanda. <span class="lbl t">Outdoor window</span> Every day through Monday.</div>
<div class="line"><span class="lbl t">Away</span> Garret on Long Island: sunny and 63 today, 42 tonight; sunny every day through Monday, highs 54 to 63.</div>
''')
# no foliage numbers found this week yet: The Turning sits out today
S('<h2 class="sec"><span class="o">&#127810;</span>The Turning','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','')
S('<div class="sky">','<div class="stars">','''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 1 50 96 A33 46 0 0 1 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>A waxing gibbous</b>, 86 percent lit, in Aquarius, rises at 4:34 p.m. and sets at 4:39 a.m.<br>
<span class="lbl t">Sun</span> 7:37a &ndash; 6:22p &middot; <b>10h 44m</b><br>
<span class="lbl t">Hunter's Moon</span> Mon, Oct 26 &middot; <span class="lbl t">New moon</span> Mon, Nov 9</div></div>
<div class="line"><span class="lbl r">Tonight</span> At 8 p.m. the moon is a third of the way up the southeast sky, four nights from the Hunter's Moon, with Saturn lower and to its left. Sunset comes a minute and a half earlier than yesterday.</div>
''')
S('<div class="stars">','<div style="font-family','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>Uranus sextiles Neptune in your sign</b>. An odd idea turns out to be a good one. Try it. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>Uranus trines Pluto</b>. Something you've outgrown is easy to let go of today. Let it. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Mars in your sign trines Saturn</b>. Discipline pays off. Do the dull part first. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>The sun squares Pluto</b>. Someone pushes. You don't have to push back. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Venus in your sign meets the sun</b>. You look good and you know it. Birthday weekend, right on cue. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
# Barograph retired (Garret, Oct 21)
S('<h2 class="sec"><span class="o">&#9776;</span>The Barograph','<h2 class="sec"><span class="o">&#10038;</span>The Ledger','')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">North Tonawanda's tax levy increase</div><div class="big">4.25%</div></div>
<div class="txt">The Common Council voted to override the state's 2 percent cap, the fifth time in seven years. The final vote on the $52 million budget is Nov. 10.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Russia Frees','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>Two Hostages Freed After a Year</h3><p>Eva Gretzmacher, 76, an Austrian aid worker, and Claudia Abbt, 69, of Switzerland, kidnapped separately in Niger early last year, have been freed and handed to authorities in Benghazi, Libya, the BBC reports. Who held them and how they were released has not been disclosed.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>A Starter Home Takes Twice as Long</h3><p>Saving for a down payment and closing costs now takes twice as long as it did in 2019, a new Center for Responsible Lending analysis finds, NPR reports. Higher prices, mortgage rates above 7 percent and rising homeowners insurance are all part of it.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Deadly Attack on a Saudi Airport</h3><p>Two people were killed and eight hurt in an attack on King Fahd International Airport in Dammam, in eastern Saudi Arabia, Wednesday evening. Authorities didn't say what struck it; Yemen's Iran-backed Houthis have repeatedly targeted the kingdom's airports with drones and missiles.</p></div></div>
''')
S('<div class="ballot">','<h2 class="sec"><span class="o">&#9962;</span>The Home Wire',ballot)
S('<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; $20 Million','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<div class="wire"><div class="num">1</div><div><h3>Honeoye Falls &middot; An Urgent Care, With Pushback</h3><p>Construction is set to start within a month on a 10,000-square-foot family medicine and urgent care center at 20 North St., run by Canandaigua's F.F. Thompson Hospital, WXXI reports. The nearest urgent care now is about 20 minutes away in Henrietta; some residents object to the developer's request for $750,000 in tax breaks.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Arkwright &middot; A Tax Break for Veterans</h3><p>The town board approved a property tax exemption for military veterans, the <i>Observer</i> reports. Supervisor Brian McAvoy called it "the right thing to do," though he said it may be more ceremonial than a big savings.</p></div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Ozzy','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron','''<div class="wire"><div class="num">1</div><div><h3>Christina Aguilera Drops In</h3><p>Chappell Roan brought out Christina Aguilera at her Los Angeles show Wednesday night. Aguilera sang "Beautiful," then the two dueted on Roan's "Coffee"; Roan said Aguilera "honestly paved the way for me."</p></div></div>
<div class="wire"><div class="num">2</div><div><h3><i>Back to Black</i> at 20</h3><p>Mark Ronson led an all-star tribute to Amy Winehouse at London's Roundhouse Wednesday for the 20th anniversary of <i>Back to Black</i>, Billboard reports. It's the Camden venue where she made her final public appearance in 2011.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Spotify Hits 306 Million</h3><p>Spotify added 6 million paying subscribers last quarter to reach 306 million, Variety reports. Monthly users grew to 788 million, and revenue rose 16 percent.</p></div></div>
''')
S('<div class="touch-head">Four Days to Sunday</div>','<div class="pnote">','''<div class="touch-head">Thursday Night: Patriots at Bears</div>
<div class="line"><b>Bills</b> &middot; A second Bill was suspended for spitting: defensive back Sam Franklin Jr. got one game without pay for spitting on a Raiders player late in Sunday's win, the NFL said Wednesday, WIVB reports. Buffalo is off this week.</div>
<div class="line"><b>Jets</b> &middot; Home Sunday at 1:00 against winless Miami. Tonight's game is the one to watch for both teams: New England, second in the division at 4&ndash;2, plays at Chicago at 8:15 on Prime Video.</div>
''')
R('<div class="line"><b>Around the league.</b> The Eagles will not be disciplined over how they handled Jalen Hurts&rsquo;s blood clots, a source told the AP.</div>\n','')
S('<div class="touch-head">Talladega Sunday</div>','<h2 class="sec"><span class="o">&#9790;</span>On This Day','''<div class="touch-head">Talladega Sunday</div>
<div class="line">Seven drivers sit within 56 points with three races left: Larson 2,370, Bell 2,365, Briscoe 2,346, Hamlin 2,339, Blaney 2,330, Logano 2,326, Reddick 2,314.</div>
''')
S('<div class="otd">','<h2 class="sec"><span class="o">&#10023;</span>Question of the Day','''<div class="otd"><b>October 22, 1938</b> &mdash; Chester Carlson made the first xerographic copy in a makeshift lab in Astoria, Queens: "10.-22.-38 ASTORIA." It became the photocopier.</div>
''')
S('<div class="qotd">What has one eye','<div class="dbl">','''<div class="qotd">I wear a white sheet, I have no feet, and I only come out on one night in October. What am I? <i>Answer below the fold.</i></div>
''')
R("<b>Question of the Day:</b> A needle.","<b>Question of the Day:</b> A ghost.")
S('<div class="s">Forecast per NWS','<div class="sig">','''<div class="s">Forecast per NWS Buffalo, with the NWS forecast for Long Island &middot; Niagara Falls, Dunkirk and Rochester stations &middot; sky computed for 14120 &middot; election summary from the paper's election tracker &middot; headlines via BBC, NPR, WXXI, WIVB, Niagara Gazette, Dunkirk Observer, Variety, Billboard &middot; scores, standings and NASCAR points via Sportradar</div>
''')
d['no']=120; d['date']='2026-10-22'
d['headline']="Bleacher buddies · Claire's birthday tomorrow · NT overrides tax cap · Patriots at Bears tonight"
d['body_html']=b; d['plate_path']='/home/claude/plate120.jpg'; d['plate_caption']='Bleacher buddies'
json.dump(d,open('edition-2026-10-22.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-22.json','w'),ensure_ascii=False,indent=1)
m=json.load(open('site/data/migraines.json')); m['updated']='2026-10-22'; json.dump(m,open('site/data/migraines.json','w'),indent=1)
print('built')
