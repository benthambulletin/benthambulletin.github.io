import json
d=json.load(open('edition-2026-10-24.json')); b=d['body_html']
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
def INS(before,new):
    global b
    assert before in b, before[:70]; b=b.replace(before,new+before,1)
R('No. 122','No. 123')
R('Saturday &middot; October 24 &middot; 2026','Sunday &middot; October 25 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">65&deg;</div><div class="k">Sunny</div></div>
  <div class="tile"><div class="v">6:17</div><div class="k">Sunset &middot; 1&frac12; min earlier</div></div>
  <div class="tile urg"><div class="v">9</div><div class="k">Days to Election Day</div></div>
</div>
''')
R('<h2 class="sec"><span class="o">&#9825;</span>Family Today<span class="o">&#9825;</span></h2>\n<div class="fam">','<h2 class="sec"><span class="o">&#9825;</span>Family Today<span class="o">&#9825;</span></h2>\n<div class="alert">&#127881; <b>Happy birthday, Garret and Ariel!</b></div>\n<div class="fam">')
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>Garret and Ariel share a birthday today</b>, and the sky is putting on a show for it: tonight's moon is the Hunter's Moon, full just after midnight. Garret is still on Long Island and heads home tomorrow; Halloween is Saturday.
<div class="line" style="margin-top:.4rem"><span class="lbl t">The log</span> Days since the last migraine: Garret 2, Dad 19, Mom 16. October so far: Garret two, Dad one, Mom one.</div>
''')
R('<li><span class="dt">Oct 24</span><span>Early voting opens &mdash; through Nov 1</span></li>\n','<li><span class="dt">Oct 26</span><span>Hunter&rsquo;s Moon &middot; Garret home</span></li>\n')
R('<li><span class="dt">Oct 25</span><span>Garret and Ariel\'s birthday</span></li>\n','')
R('<li><span class="dt">Oct 25</span><span>Dolphins at Jets &mdash; 1:00 &middot; Bills off</span></li>\n','<li><span class="dt">Today</span><span>Dolphins at Jets &mdash; 1:00 &middot; Bills off</span></li>\n')
R('<li><span class="dt">Nov 1</span><span>Ravens at Bills</span></li>','<li><span class="dt">Nov 1</span><span>Ravens at Bills &middot; clocks fall back &middot; early voting ends</span></li>')
# Sunday Spotlight
INS('<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass','''<h2 class="sec"><span class="o">&#127809;</span>The Sunday Spotlight<span class="o">&#127809;</span></h2>
<div class="touch-head">Spotting an AI Scam</div>
<div class="line" style="color:var(--soft)">Short this week, for the birthday edition. Scammers now use AI to copy voices and write convincing messages; the defenses are old-fashioned and they work. An AI wrote this section.</div>
<div class="line"><b>1. The size of it.</b> Americans reported $893 million in losses to AI-related scams in 2025, across 22,364 complaints, according to the FBI's annual internet crime report, as covered by the security firm Malwarebytes. <b>What it means:</b> that counts only what people reported, so the real number is higher. The FBI says AI is mostly supercharging old tricks: romance scams, fake kidnapping calls, people pretending to be the government.</div>
<div class="line"><b>2. The voice on the phone.</b> The security company McAfee says about three seconds of someone's recorded voice is enough to clone it, and in its survey of 7,000 people, 70 percent weren't confident they could tell a real voice from a copy. <b>What it means for us:</b> a call that sounds exactly like one of the kids or grandkids, saying there's an emergency and money is needed fast, is the classic setup.</div>
<div class="line"><b>3. Three checks that catch it.</b> <b>Hang up and call back</b> on a number you already have, not one the caller gives you. <b>Agree on a family safe word</b> that anyone in real trouble can say. <b>Never pay because someone is rushing you</b>, and never by gift card, cryptocurrency or wire; the FBI flags those as the scammer's favorites.</div>
<div class="line"><b>Coming down the road.</b> The FBI also suggests posting less of your own voice and video publicly, since that's the raw material. If something does happen, call the bank right away and report it at <a href="https://www.ic3.gov">ic3.gov</a> or <a href="https://reportfraud.ftc.gov">reportfraud.ftc.gov</a>. A safe word costs nothing; pick one at the next family dinner.</div>
''')
S('<div class="wx">','<h2 class="sec"><span class="o">&#127810;</span>The Turning','''<div class="wx"><div class="bigtemp">65<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">A warm, golden birthday Sunday, the best day of the week, and a Hunter's Moon rising at dusk</span>
Low <b>47&deg;</b> tonight &middot; light southwest wind<br>Dry until a chance of showers Thursday</div></div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">37<sup>&deg;</sup></div><div class="d">Clear &middot; high 65&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">50<sup>&deg;</sup></div><div class="d">Clear &middot; high 64&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">37<sup>&deg;</sup></div><div class="d">Clear &middot; high 68&deg;</div></div>
</div>
<div class="strip5">
  <div><div class="d">Sun</div><div class="i">&#9728;</div><div class="h">65</div><div class="w">sunny</div></div>
  <div><div class="d">Mon</div><div class="i">&#9729;</div><div class="h">64</div><div class="w">partly sunny</div></div>
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">55</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#9729;</div><div class="h">65</div><div class="w">partly sunny</div></div>
  <div><div class="d">Thu</div><div class="i">&#127782;</div><div class="h">67</div><div class="w">showers late, 29%</div></div>
</div>
<div class="line"><span class="lbl r">Frost</span> Scottsville drops to 29 Tuesday night; North Tonawanda 34. <span class="lbl t">Outdoor window</span> Today, Monday and Wednesday.</div>
<div class="line"><span class="lbl t">Away</span> Garret on Long Island: sunny and 62 for the birthday, 42 tonight; sunny and 64 for the trip home Monday.</div>
''')
R("<b>This week's state foliage report</b> lists Lewiston, Buffalo, East Aurora, Chautauqua and Jamestown among the places with the most significant change. North Tonawanda usually peaks this last week of October.","<b>Peak week, by the calendar.</b> North Tonawanda usually tops out the last week of October; the state's latest report has Lewiston, Buffalo, East Aurora, Chautauqua and Jamestown among the fastest-changing spots. New numbers Wednesday.")
S('<div class="sky">','<div class="stars">','''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>The Hunter's Moon</b>, full at 12:11 a.m. Monday, in Pisces; rises at 5:41 p.m. and sets at 8:23 a.m.<br>
<span class="lbl t">Sun</span> 7:41a &ndash; 6:17p &middot; <b>10h 36m</b><br>
<span class="lbl t">New moon</span> Mon, Nov 9 &middot; <span class="lbl t">Clocks fall back</span> Sun, Nov 1</div></div>
<div class="line"><span class="lbl r">Tonight</span> The Hunter's Moon comes up in the east just before sunset; by 8 p.m. it's about a quarter of the way up, due east. It's the first full moon after September's Harvest Moon.</div>
''')
S('<div class="stars">','<div style="font-family','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>The full moon rises in your sign</b>. Everything's lit up. A good night to finish something. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>Uranus trines Pluto</b>. Clear out one old thing. You'll feel lighter. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>The moon trines Jupiter in your sign</b>. Generous mood. Call someone you owe a call. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>Mercury squares Jupiter</b>. Promises come easy today. Keep them small. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>The sun in your sign stays close to Venus</b>. A birthday sky for Garret and Ariel, and a late-birthday one for Claire. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">Erie County ballots, first day of early voting</div><div class="big">13,000+</div></div>
<div class="txt">Every one was accounted for despite technical trouble at some polling places, the county Board of Elections told WIVB.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>A Truce for One','<div class="ballot">','''<div class="wire"><div class="num">1</div><div><h3>Brazil Votes</h3><p>Brazilians choose a president today in a close runoff between Luiz In&aacute;cio Lula da Silva, 80, seeking a fourth term, and Senator Fl&aacute;vio Bolsonaro, 45, the BBC reports. Bolsonaro finished first in the Oct. 4 first round; his father, the former president, is serving a 27-year sentence for plotting a coup.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>France Protests Again</h3><p>More than 1,300 people were arrested Saturday as hundreds of thousands protested across France, with tear gas and water cannon in Paris and barricades burning in Marseille, the BBC reports. Officials say they avoided the rioting and looting of the weekend before.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Shooting at a Homecoming</h3><p>At least 12 people, six of them children, were shot near the football stadium in Tallahassee after Florida A&amp;M's homecoming game Saturday, CBS reports. Police say a fight broke out first; three are seriously hurt, and no one has been arrested.</p></div></div>
''')
S('<div class="ballot">','<h2 class="sec"><span class="o">&#9962;</span>The Home Wire','''<h2 class="sec"><span class="o">&#9745;</span>The Ballot<span class="o">&#9745;</span></h2>
<div class="touch-head">Nine Days Out, and Early Voting Is Open</div>
<div class="line"><b>Governor.</b> Kathy Hochul leads Bruce Blakeman by about 12 points. The newest major poll, Quinnipiac (Oct 15&ndash;19), has her ahead 55 to 41, down from 19 points in its September poll; Blakeman leads upstate, where all five of our towns are, 52 to 46. <b>What it means:</b> Hochul is still the clear favorite, but the race has tightened a little.</div>
<div class="line"><b>NY-26, North Tonawanda.</b> Democrat Tim Kennedy, the incumbent, against Republican Dennis Hannon. The Cook Political Report rates it solidly Democratic.</div>
<div class="line"><b>NY-23, Orchard Park, Dunkirk and Fredonia.</b> Republican Nick Langworthy, the incumbent, against Democrat Aaron Gies. No public poll.</div>
<div class="line"><b>NY-25, Scottsville.</b> Democrat Joe Morelle, the incumbent, against Republican McIntyre. No public poll.</div>
<div class="line"><b>Down the ballot in North Tonawanda.</b> State Senate: Ortt (R, inc.) against Arida (D). The city also votes yes or no on an $18 million community center at the Keller Building, paid for by a special property tax of about 84 cents per $1,000 of assessed value before grants. Every town's full list is on the tracker.</div>
<div class="line"><b>The national read.</b> Democrats are favored to take the House; Cook expects them to gain 12 to 22 seats. The Senate is close, tilting Democratic: they lead narrowly or are tied in all six Republican seats they're chasing, with Iowa and Kansas dead even, and must also hold Michigan and Minnesota. The president's approval is about 22 points underwater in the average.</div>
<div class="line" style="color:var(--soft)">Early voting through Nov 1 &middot; Election Day Nov 3, 6 a.m.&ndash;9 p.m. &middot; sites and every race: <a href="https://benthambulletin.github.io/election/">benthambulletin.github.io/election</a></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Fewer','<h2 class="sec"><span class="o">&#9733;</span>The Marquee','''<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; A Night for the Duffys</h3><p>The Boys and Girls Club of Rochester honored Barb and Bob Duffy at its annual gala downtown Saturday, Rochester First reports. The couple has worked on behalf of the community for more than four decades.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Fredonia &middot; A Dunkirk Diplomat Remembered</h3><p>The Fredonia Shakespeare Club opened its season with a talk on Edna "Betty" Boorady, a lawyer and diplomat born in Dunkirk, by Dunkirk Historical Museum curator Katherine Szewczuk, the <i>Observer</i> reports. Boorady graduated from St. Mary's Academy in 1938 and Cornell Law School in 1954.</p></div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>A First Look','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron','''<div class="wire"><div class="num">1</div><div><h3>Elvis's Owners Sue an AI Company</h3><p>The owners of Elvis Presley's music sued Anthropic, the AI company, on Friday, claiming it used 274 of his songs, including "Can't Help Falling in Love," to train its models without permission, Billboard and the Hollywood Reporter report. The suit seeks $150,000 per song, according to Rolling Stone.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Netflix's Ten Years in Korea</h3><p>Stars of <i>Squid Game</i> and <i>KPop Demon Hunters</i> took the stage in Seoul Saturday as Netflix marked a decade in Korea, Variety reports. Co-CEO Ted Sarandos previewed a second season of <i>All of Us Are Dead</i>.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Jay-Z Wraps Up "Jay-Z 30"</h3><p>Jay-Z closed his yearlong 30th-anniversary concert series in Los Angeles with Dr. Dre, Snoop Dogg and Too Short, Variety reports. It followed Friday's show with Blue Ivy and John Legend.</p></div></div>
''')
S('<div class="touch-head">Jets Tomorrow at 1:00</div>','<table class="tbl">','''<div class="touch-head">Jets at 1:00 Today</div>
<div class="line"><b>Jets</b> &middot; Winless Miami at MetLife this afternoon. The early game is in Paris at 9:30 a.m., Steelers against the Saints, the NFL's first regular-season game in France.</div>
<div class="line"><b>Bills</b> &middot; Off today, resting at 5&ndash;1 and a game and a half clear in the division. Baltimore visits next Sunday.</div>
''')
S('<div class="touch-head">Talladega Tomorrow</div>','<h2 class="sec"><span class="o">&#9790;</span>On This Day','''<div class="touch-head">Talladega Today</div>
<div class="line">Larson leads Bell by 5 going in, with Martinsville and Homestead still to come.</div>
''')
INS('<h2 class="sec"><span class="o">&#9790;</span>On This Day','''<h2 class="sec"><span class="o">&#127810;</span>The Week Ahead<span class="o">&#127810;</span></h2>
<div class="line"><b>Weather.</b> Sun and the 60s most days; a frosty Wednesday morning in Scottsville; a chance of showers Thursday.</div>
<div class="line"><b>Family.</b> Garret home from Long Island Monday. Halloween Saturday.</div>
<div class="line"><b>The Ballot.</b> Early voting runs through next Sunday, Nov 1; Election Day is Tuesday, Nov 3.</div>
<div class="line"><b>Games.</b> Next Sunday, Nov 1, the Bills host Baltimore.</div>
<div class="line"><b>The sky.</b> The Hunter's Moon tonight. Clocks fall back an hour next Sunday at 2 a.m.</div>
<div class="line"><b>Next Sunday's Spotlight.</b> Why we change the clocks.</div>
<h2 class="sec"><span class="o">&#9776;</span>The Week in the Glass<span class="o">&#9776;</span></h2>
<table class="tbl"><tr><th>Day</th><th class="n">Dawn</th><th class="n">Fcst high</th><th>Sky</th></tr>
<tr><td>Mon 19</td><td class="n">43</td><td class="n">64</td><td>sunny</td></tr>
<tr><td>Tue 20</td><td class="n">39</td><td class="n">63</td><td>mostly sunny</td></tr>
<tr><td>Wed 21</td><td class="n">34</td><td class="n">60</td><td>sunny</td></tr>
<tr><td>Thu 22</td><td class="n">34</td><td class="n">62</td><td>mostly sunny</td></tr>
<tr><td>Fri 23</td><td class="n">43</td><td class="n">58</td><td>mostly sunny</td></tr>
<tr><td>Sat 24</td><td class="n">36</td><td class="n">62</td><td>sunny</td></tr>
<tr><td>Sun 25</td><td class="n">37</td><td class="n">65</td><td>sunny</td></tr></table>
<div class="line">Seven dry days in a row in North Tonawanda, the coldest dawns Wednesday and Thursday at 34. One migraine logged this week: Garret, Friday.</div>
<h2 class="sec"><span class="o">&#10023;</span>The Sunday Question<span class="o">&#10023;</span></h2>
<div class="qotd"><b>Last week: what's the best birthday present you ever got?</b><br>No answers came in; it's still a good question for the birthday table today.<br><br><b>This week, for Halloween: what's the best costume you ever wore?</b><br>Send it at <a href="https://tally.so/r/rjxDpl">tally.so/r/rjxDpl</a> this week. Answers run here next Sunday under your names.</div>
''')
S('<div class="otd">','<h2 class="sec"><span class="o">&#10023;</span>Question of the Day','''<div class="otd"><b>October 25, 1881</b> &mdash; Pablo Picasso was born in M&aacute;laga, Spain. He shares a birthday with Garret and Ariel.</div>
''')
S('<div class="qotd">I\'m striped yellow','<div class="dbl">','''<div class="qotd">What can you catch but never throw, and goes around every October? <i>Answer below the fold.</i></div>
''')
R("<b>Question of the Day:</b> Candy corn.","<b>Question of the Day:</b> A cold.")
S('<div class="s">Forecast per NWS','<div class="sig">','''<div class="s">Forecast per NWS Buffalo, with the NWS forecast for Long Island &middot; Niagara Falls, Dunkirk and Rochester stations &middot; sky computed for 14120 &middot; foliage from the I LOVE NY report &middot; election summary from the paper's election tracker &middot; Spotlight from the FBI internet crime report via Malwarebytes and McAfee survey figures via Heimdal &middot; headlines via BBC, CBS, WIVB, Rochester First, Dunkirk Observer, Billboard, Hollywood Reporter, Variety &middot; NASCAR points via Sportradar</div>
''')
d['no']=123; d['date']='2026-10-25'
d['headline']="Happy birthday, Garret and Ariel · Hunter's Moon tonight · Spotting an AI scam · Jets host Miami"
d['body_html']=b; d['plate_path']=None; d['plate_caption']=None
json.dump(d,open('edition-2026-10-25.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-25.json','w'),ensure_ascii=False,indent=1)
print('built')
