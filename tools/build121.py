import json, subprocess
d=json.load(open('edition-2026-10-22.json')); b=d['body_html']
ballot=subprocess.run(['python3','site/tools/ballot_box.py','2026-10-23'],capture_output=True,text=True,check=True).stdout.strip()+'\n'
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
R('No. 120','No. 121')
R('Thursday &middot; October 22 &middot; 2026','Friday &middot; October 23 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">58&deg;</div><div class="k">Mostly sunny</div></div>
  <div class="tile"><div class="v">6:20</div><div class="k">Sunset &middot; 1&frac12; min earlier</div></div>
  <div class="tile urg"><div class="v">11</div><div class="k">Days to Election Day</div></div>
</div>
''')
R('<div class="dbl-tight"><div class="a"></div><div class="b"></div></div>\n<h2 class="sec"><span class="o">&#9825;</span>Family Today<span class="o">&#9825;</span></h2>\n<div class="fam">','<div class="plate-wrap"><div class="frame"><span class="tick tl"></span><span class="tick tr"></span><span class="tick bl"></span><span class="tick br"></span>\n<img src="__PLATE__" alt="Four smiling family members on a couch, two grandmothers and two girls, with a black and white spaniel in front"></div>\n<div class="plate-cap">Plate I &middot; The Family Album</div>\n<div class="plate-sub">Happy birthday, Claire</div></div>\n<div class="dbl-tight"><div class="a"></div><div class="b"></div></div>\n<h2 class="sec"><span class="o">&#9825;</span>Family Today<span class="o">&#9825;</span></h2>\n<div class="alert">&#127881; <b>Happy birthday, Claire!</b></div>\n<div class="fam">')
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>The cover is for Claire</b>, whose birthday is today, the very day the sun moves into Scorpio. Garret and Ariel share theirs Sunday; safe travels to Garret on Long Island. Halloween is eight days out.
<div class="line" style="margin-top:.4rem"><span class="lbl t">The log</span> Days since the last migraine: Garret 17, Dad 17, Mom 14. October so far: one each.</div>
''')
R('<li><span class="dt">Oct 22</span><span>Patriots at Bears &mdash; 8:15, Prime Video</span></li>\n','')
S('<div class="wx">','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','''<div class="wx"><div class="bigtemp">58<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">A crisp birthday Friday, with fog in the low spots and sun by mid-morning</span>
Low <b>35&deg;</b> tonight &middot; light east wind<br>Dry through Tuesday, warming to 64 Sunday</div></div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">43<sup>&deg;</sup></div><div class="d">Clear &middot; high 58&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">37<sup>&deg;</sup></div><div class="d">Fog &middot; high 58&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">37<sup>&deg;</sup></div><div class="d">Clear &middot; high 57&deg;</div></div>
</div>
<div class="strip5">
  <div><div class="d">Fri</div><div class="i">&#9728;</div><div class="h">58</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Sat</div><div class="i">&#9728;</div><div class="h">61</div><div class="w">sunny</div></div>
  <div><div class="d">Sun</div><div class="i">&#9728;</div><div class="h">64</div><div class="w">sunny</div></div>
  <div><div class="d">Mon</div><div class="i">&#9728;</div><div class="h">63</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">54</div><div class="w">mostly sunny</div></div>
</div>
<div class="line"><span class="lbl r">Frost</span> Scottsville drops to 30 tonight with patchy fog; North Tonawanda 35. <span class="lbl t">Outdoor window</span> The whole weekend, best Sunday at 64.</div>
<div class="line"><span class="lbl t">Away</span> Garret on Long Island: sunny and 56 today, 41 tonight; sunny through Monday, highs 56 to 64.</div>
''')
S('<div class="sky">','<div class="stars">','''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 1 50 96 A39 46 0 0 1 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>A waxing gibbous</b>, 92 percent lit, in Pisces, rises at 4:55 p.m. and sets at 5:50 a.m.<br>
<span class="lbl t">Sun</span> 7:39a &ndash; 6:20p &middot; <b>10h 42m</b><br>
<span class="lbl t">Hunter's Moon</span> Mon, Oct 26 &middot; <span class="lbl t">New moon</span> Mon, Nov 9</div></div>
<div class="line"><span class="lbl r">Tonight</span> The sun crossed into Scorpio this morning. At 8 p.m. the nearly full moon is a third of the way up the east-southeast sky; the Hunter's Moon is Monday. Sunset is a minute and a half earlier than yesterday.</div>
''')
S('<div class="stars">','<div style="font-family','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>Neptune in your sign sextiles Pluto</b>. Old plans get a second look. Some of them were good. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>Venus squares Pluto</b>. Feelings run hot over something small. Sleep on it. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Mercury squares Jupiter in your sign</b>. You're right, but say it once. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>Uranus trines Pluto</b>. A change you've resisted turns out easy. Let it happen. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>The sun enters your sign and meets Venus</b>. Scorpio season opens on Claire's birthday. Happy birthday. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">Niagara Falls Main Street buildings the city took over</div><div class="big">38</div></div>
<div class="txt">The city bought them from absentee landlords to resell to developers; the latest plan turns a building empty for decades into Niagara University student housing, WKBW reports.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Two Hostages','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>No More Carriage Horses in New York</h3><p>The New York City Council voted Thursday to ban horse-drawn carriage rides by 2028, a law named for Romanch Mahajan, 18, who died in a carriage accident in Central Park in June. Mayor Zohran Mamdani's office says he will sign it.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>A Son Hears His Mother's Voice</h3><p>Aung San Suu Kyi, Myanmar's ousted leader, spoke by phone with her son, Kim Aris, on Thursday, their first conversation since the 2021 coup put her in detention, NPR reports. Her first question, he said, was about his health.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>A Flaw Under Most of the Web</h3><p>Researchers at Wiz, using OpenAI technology, found security flaws in a programming language that helps run about 70 percent of the world's websites, and hacking attempts have risen since, NPR reports. OpenAI called it "one of the most impactful vulnerabilities in recent memory."</p></div></div>
''')
S('<div class="ballot">','<h2 class="sec"><span class="o">&#9962;</span>The Home Wire',ballot)
S('<div class="wire"><div class="num">1</div><div><h3>Honeoye Falls','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<div class="wire"><div class="num">1</div><div><h3>Fredonia &middot; Second Thoughts on Flock Cameras</h3><p>Village trustees in Fredonia are weighing whether to shut down Flock license-plate cameras, objecting that they went up without a board vote, WKBW reports. The cameras record which vehicles pass a spot and when.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Wilson &middot; On to the Semifinals</h3><p>Hayden Fellows scored four goals as top-seeded Wilson beat Silver Creek/Forestville 6&ndash;0 in a Section VI Class C boys soccer quarterfinal Thursday, the <i>Observer</i> reports. The 15&ndash;1&ndash;1 Lakemen host Randolph Monday at 7.</p></div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Christina Aguilera','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron','''<div class="wire"><div class="num">1</div><div><h3>Ryan Gosling's Spooky Band Returns</h3><p>Dead Man's Bones, Ryan Gosling's duo with Zach Shields, will release new music Oct. 27, 17 years after its only album, the Hollywood Reporter says. The ghost-and-monster rock band is timing its comeback for Halloween.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Prince William, Superfan</h3><p>The Prince of Wales dropped in on <i>The Graham Norton Show</i> and said he's a "big fan" of Christopher Nolan's movies and the game show <i>The Traitors</i>, Variety reports. The episode airs tonight in Britain.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3><i>The Notebook</i> Goes to London</h3><p>The musical version of <i>The Notebook</i>, with songs by Ingrid Michaelson, will open in the West End, Variety reports. It will be the first show at the newly renamed Judi Dench Theatre, formerly the Shaftesbury.</p></div></div>
''')
S('<div class="touch-head">Thursday Night: Patriots at Bears</div>','<table class="tbl">','''<div class="touch-head">Bears 30, Patriots 24</div>
<div class="line"><b>Bills</b> &middot; Chicago did Buffalo a favor Thursday night: the loss drops New England to 4&ndash;3, a game and a half behind the Bills, who are off this week.</div>
<div class="line"><b>Jets</b> &middot; Miami, 0&ndash;5, comes to MetLife Sunday at 1:00. A win would pull the Jets within a game of New England.</div>
''')
R('<tr><td>New England</td><td class="n">4</td><td class="n">2</td><td class="n">.667</td></tr>','<tr><td>New England</td><td class="n">4</td><td class="n">3</td><td class="n">.571</td></tr>')
S('<div class="touch-head">Talladega Sunday</div>','<h2 class="sec"><span class="o">&#9790;</span>On This Day','''<div class="touch-head">Talladega Sunday</div>
<div class="line">Larson leads Bell by 5 with three races left.</div>
''')
S('<div class="otd">','<h2 class="sec"><span class="o">&#10023;</span>Question of the Day','''<div class="otd"><b>October 23, 2001</b> &mdash; Apple introduced the iPod, pitched as "1,000 songs in your pocket."</div>
''')
S('<div class="qotd">I wear a white sheet','<div class="dbl">','''<div class="qotd">I sweep the floor all year, but on one October night I fly. What am I? <i>Answer below the fold.</i></div>
''')
R("<b>Question of the Day:</b> A ghost.","<b>Question of the Day:</b> A witch's broomstick.")
S('<div class="s">Forecast per NWS','<div class="sig">','''<div class="s">Forecast per NWS Buffalo, with the NWS forecast for Long Island &middot; Niagara Falls, Dunkirk and Rochester stations &middot; sky computed for 14120 &middot; election summary from the paper's election tracker &middot; headlines via CBS, NPR, WKBW, Dunkirk Observer, Variety, Hollywood Reporter &middot; scores and NASCAR points via Sportradar</div>
''')
d['no']=121; d['date']='2026-10-23'
d['headline']="Happy birthday, Claire · Bears 30, Patriots 24 · NYC bans carriage horses · Sunny weekend"
d['body_html']=b; d['plate_path']='/home/claude/plate121.jpg'; d['plate_caption']='Happy birthday, Claire'
json.dump(d,open('edition-2026-10-23.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-23.json','w'),ensure_ascii=False,indent=1)
m=json.load(open('site/data/migraines.json')); m['updated']='2026-10-23'; json.dump(m,open('site/data/migraines.json','w'),indent=1)
print('built')
