import json
d=json.load(open('edition-2026-09-27.json')); b=d['body_html']
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
def S(start,end,new):
    global b
    i=b.index(start); j=b.index(end,i); b=b[:i]+new+b[j:]
H=lambda o,t:f'<h2 class="sec"><span class="o">{o}</span>{t}<span class="o">{o}</span></h2>'
R('No. 95','No. 96')
R('Sunday &middot; September 27 &middot; 2026','Monday &middot; September 28 &middot; 2026')
S('<div class="tiles">','<div class="dbl-tight">','''<div class="tiles">
  <div class="tile"><div class="v">68&deg;</div><div class="k">Cloudy, drier later</div></div>
  <div class="tile good"><div class="v">29.95&#8243; &#8212;</div><div class="k">Leveling off</div></div>
  <div class="tile urg"><div class="v">36</div><div class="k">Days to Election Day</div></div>
</div>
''')
S('<div class="plate-wrap">','<h2 class="sec"><span class="o">&#9825;</span>Family Today','')
S('<div class="fam">','<ul class="cal">','''<div class="fam"><b>Three and oh.</b> The Bills won ugly and stayed perfect; the Jets came back from fourteen down and lost in the last minute. Both games are below. <b>Luka</b>, the paper hopes the cough has finally loosened its grip. A grey Monday gives way to the best three days of the week, with 77 by Thursday.
''')
S('<ul class="cal">','</ul>','''<ul class="cal">
<li><span class="dt">Oct 4</span><span>Patriots at Buffalo, Jets at Chicago &mdash; both 1:00</span></li>
<li><span class="dt">Oct 4</span><span>Las Vegas, NASCAR playoffs &mdash; 5:30, USA</span></li>
<li><span class="dt">Oct 23</span><span>Claire's birthday</span></li>
<li><span class="dt">Oct 25</span><span>Garret and Ariel's birthday</span></li>
<li><span class="dt">Nov 3</span><span>Election Day</span></li>
''')
S('<h2 class="sec"><span class="o">&#9788;</span>The Sunday Spotlight','<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass','')
S('<div class="wx">','<div class="towns">','''<div class="wx"><div class="bigtemp">68<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">A grey start to a good week</span>
Low <b>57&deg;</b> &middot; Northeast, light<br>Rain <b>None today</b> &mdash; next chance Thursday night</div></div>
''')
S('<div class="towns">','<div class="strip5">','''<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">57<sup>&deg;</sup></div><div class="d">Overcast &middot; high 68&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">58<sup>&deg;</sup></div><div class="d">Drizzle, then cloudy &middot; high 65&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">58<sup>&deg;</sup></div><div class="d">Grey, drizzle ending</div></div>
</div>
''')
S('<div class="strip5">','<div class="line"><span class="lbl t">Game day','''<div class="strip5">
  <div><div class="d">Mon</div><div class="i">&#9729;</div><div class="h">68</div><div class="w">cloudy</div></div>
  <div><div class="d">Tue</div><div class="i">&#9925;</div><div class="h">72</div><div class="w">partly sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#9925;</div><div class="h">74</div><div class="w">partly sunny</div></div>
  <div><div class="d">Thu</div><div class="i">&#9925;</div><div class="h">77</div><div class="w">showers at night</div></div>
  <div><div class="d">Fri</div><div class="i">&#127782;</div><div class="h">69</div><div class="w">a.m. showers</div></div>
</div>
''')
S('<div class="line"><span class="lbl t">Game day','<div class="pnote">','''<div class="line"><span class="lbl t">Outdoor window</span> Tuesday through Thursday afternoon: 72, 74, then 77, the warmest day left on the board. Showers move in Thursday night. <span class="lbl t">Dunkirk</span> Mostly sunny Tuesday through Thursday, 78 on Thursday.</div>
''')
S('<div class="pnote">','<h2 class="sec"><span class="o">&#127810;</span>The Turning','')
S('<div class="line"><b>Still a waiting game.</b>','<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky','''<div class="line"><b>Wednesday is the next report.</b> A mild, bright midweek is good color weather: sunny days build the red in the maples.</div>
''')
S('<div class="sky">','<div class="stars">','''<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 1 50 96 A38 46 0 0 1 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>Ninety-five percent</b> and waning, in Taurus, rising at 7:40 tonight. Each night now it comes up about half an hour later.<br>
<span class="lbl t">Sun</span> 7:09a &ndash; 7:02p &middot; <b>11h 53m</b><br>
<span class="lbl t">Last quarter</span> Sat, Oct 3 &middot; <span class="lbl t">Next new moon</span> Sat, Oct 10</div></div>
<div class="line"><span class="lbl r">Tonight</span> <b>Saturn</b> is up at 7:20, just ahead of the moon. <b>Mars</b>, now in Leo, rises at 1:28 a.m., and <b>Jupiter</b> follows at 3:06; the two are in the same part of the sky before dawn.</div>
''')
S('<div class="stars">','<div style="font-family:','''<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>The moon has moved on to Taurus</b> and squares Mars, fresh into Leo. After a weekend in your sign it leaves a little friction behind. Pick one thing to push on and let the rest wait. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>Mars left your sign overnight</b> after two months. The pressure you have been carrying lifts today; what is left is the part that was actually yours to do. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>Mars entered Leo at 2 this morning</b> and stays until late November, joining Jupiter already there. Eight weeks of drive and good fortune in the same sign. Start something. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>Mercury, your ruler, is opposite the moon</b> and still square Mars. Thoughts are quick and the tone is sharp. Say the useful half. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>Pluto, your old ruler, is opposite Mars</b> and square the moon. A test of who decides. Venus sits quiet in your sign; lead with that, not the fight. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
''')
S('<div class="baro-top">','<h2 class="sec"><span class="o">&#10038;</span>The Ledger','''<div class="baro-top"><div class="dial">Low &middot; 28/100</div><div class="press">29.95&#8243;</div><div class="trend">&#8212; leveling off</div></div>
<div class="baro"><svg viewBox="0 0 820 180" xmlns="http://www.w3.org/2000/svg">
<g font-family="AR" font-size="13" fill="#6b5f44"><line x1="64" y1="18" x2="790" y2="18" stroke="#d6cbaf"/><text x="16" y="22">30.54</text>
<line x1="64" y1="60" x2="790" y2="60" stroke="#d6cbaf"/><text x="16" y="64">30.34</text><line x1="64" y1="102" x2="790" y2="102" stroke="#d6cbaf"/><text x="16" y="106">30.14</text>
<line x1="64" y1="144" x2="790" y2="144" stroke="#d6cbaf"/><text x="16" y="148">29.94</text></g>
<polyline points="120,26 280,64 440,100 600,134 760,142" fill="none" stroke="#0e8a8a" stroke-width="3"/>
<g fill="#0e8a8a"><circle cx="120" cy="26" r="6"/><circle cx="280" cy="64" r="6"/><circle cx="440" cy="100" r="6"/><circle cx="600" cy="134" r="6"/></g>
<circle cx="760" cy="142" r="7" fill="#c8302f"/><circle cx="760" cy="142" r="15" fill="none" stroke="#c8302f" stroke-width="2.5"/>
<g font-family="AR" font-size="14" fill="#6b5f44" text-anchor="middle"><text x="120" y="174">Thu 30.50</text><text x="280" y="174">Fri 30.32</text><text x="440" y="174">Sat 30.15</text><text x="600" y="174">Sun 29.99</text></g>
<text x="760" y="174" font-family="AR" font-size="14" font-weight="700" fill="#c8302f" text-anchor="middle">Today 29.95</text></svg></div>
<div class="line"><span class="lbl t">The slide has stopped</span> 29.95 this morning, just four hundredths below yesterday after three days of steady drops. Over the last twelve hours it has hardly moved. A flat, ordinary reading is the kind that rarely causes trouble.</div>
''')
S('<div class="ledger">','<h2 class="sec"><span class="o">&#10038;</span>The National Wire','''<div class="ledger"><div class="num"><div class="cap">Bills turnovers in a game they won</div><div class="big">5</div></div>
<div class="txt">Three fumbles and two interceptions, and Buffalo still beat the Chargers by eight. Teams that give the ball away five times almost never win.</div></div>
''')
S('<div class="wire"><div class="num">1</div><div><h3>U.S. and China','<h2 class="sec"><span class="o">&#9745;</span>The Ballot','''<div class="wire"><div class="num">1</div><div><h3>Trump Expects Iran Talks This Week</h3><p>A day after rejecting Tehran's offer to reopen the Strait of Hormuz, the president said negotiators should meet again this week, with Qatar carrying messages between the two sides.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Five Held in U.K. Over Plot Against U.S. Base</h3><p>British police arrested five people on terrorism charges over an alleged plan to damage a base housing American troops, the president confirmed; investigators suspect an Iranian link.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Ireland Refuses Handshakes With Israel's Team</h3><p>Irish players wore black armbands and declined the pre-match handshake before a Nations League game in Hungary, then won 3&ndash;0.</p></div></div>
''')
S('<h2 class="sec"><span class="o">&#9745;</span>The Ballot','<h2 class="sec"><span class="o">&#9962;</span>The Home Wire','<div class="ballot">&#9745; The Ballot &middot; <b>36 days</b> to Election Day &middot; early voting Oct 24&ndash;Nov 1 &middot; register by Oct 24</div>\n')
S('<h2 class="sec"><span class="o">&#9962;</span>The Home Wire','<h2 class="sec"><span class="o">&#9733;</span>The Marquee',H('&#9962;','The Home Wire')+'''
<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; Red Wings Fall One Game Short</h3><p>After winning the International League title, the Red Wings lost the Triple-A national championship to Oklahoma City, 5&ndash;3 in ten innings, in Las Vegas. The team is holding a season celebration at ESL Ballpark.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Erie County &middot; $1.08 Million From the Stadium Surcharge</h3><p>The 6 percent charge on tickets, parking, food and merchandise at the new Highmark Stadium brought in $1,080,915 in August alone. It goes to a fund for the stadium's upkeep.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Dunkirk &middot; Water Rate Vote Pushed Back</h3><p>The $10 base-rate increase missed the Common Council agenda; the city comptroller took responsibility and says it will be up at the next meeting.</p></div></div>
''')
S('<h2 class="sec"><span class="o">&#9733;</span>The Marquee','<h2 class="sec"><span class="o">&#127944;</span>The Gridiron',H('&#9733;','The Marquee')+'''
<div class="wire"><div class="num">1</div><div><h3>SNL Opens Season 52 With a Knick</h3><p>Jalen Brunson hosted Saturday's premiere with K-pop group Katseye. Chloe Fineman is gone after seven seasons, and new cast member Grace Reiter is the first born in the 2000s.</p></div></div>
''')
S('<h2 class="sec"><span class="o">&#127944;</span>The Gridiron','<h2 class="sec"><span class="o">&#9873;</span>The Chase',H('&#127944;','The Gridiron')+'''
<div class="touch-head">Monday Morning Quarterback</div>
<div class="line"><b>Bills 24, Chargers 16.</b> Buffalo turned it over five times and won anyway. Los Angeles led 10&ndash;0 after one; Josh Allen's one-yard sneak just before half tied it. The game turned early in the fourth when C.J. Gardner-Johnson picked off Justin Herbert at the one and ran it back 41 yards. Allen scored again, James Cook added the clincher, and Buffalo is 3&ndash;0.</div>
<div class="line"><b>Got right:</b> the ground game and the pass rush. Cook ran for 154 yards, Allen became the first quarterback of the Super Bowl era with multiple rushing touchdowns in three straight games, and Greg Rousseau's two sacks give him six, a team record through three games, past Bruce Smith. <b>To fix:</b> the ball. Three lost fumbles, two interceptions and ten penalties against a winless team.</div>
<div class="line"><b>Jets 24, Lions 31.</b> The Jets were down 24&ndash;10 going into the fourth and tied it anyway: Geno Smith hit Jeremy Ruckert, then Garrett Wilson for 23 yards, and Sterling Shepard caught the two-point try. Detroit answered with Jahmyr Gibbs, his third touchdown, with 2:30 left. A sack and fumble with 51 seconds to go ended it.</div>
<div class="line"><b>Got right:</b> Smith was 31 of 37 for 321 yards and three touchdowns, and rookie tight end Kenyon Sadiq caught seven for 105. <b>To fix:</b> the run game, 58 yards on 19 carries, and the five sacks. A good team on the road, and they had it tied late.</div>
<table class="tbl"><tr><th>AFC East</th><th class="n">W</th><th class="n">L</th><th class="n">PCT</th></tr>
<tr><td style="color:var(--red)">Buffalo</td><td class="n">3</td><td class="n">0</td><td class="n">1.000</td></tr>
<tr><td style="color:var(--red)">N.Y. Jets</td><td class="n">1</td><td class="n">2</td><td class="n">.333</td></tr>
<tr><td>New England</td><td class="n">1</td><td class="n">2</td><td class="n">.333</td></tr>
<tr><td>Miami</td><td class="n">0</td><td class="n">3</td><td class="n">.000</td></tr></table>
<div class="line"><b>Around the league.</b> Jacksonville routed New England 35&ndash;6, and Kansas City won in Miami 24&ndash;10. Baltimore beat Dallas 34&ndash;31. Denver edged the Rams 30&ndash;26 last night. Minnesota, San Francisco, Kansas City, Las Vegas and Buffalo are the unbeaten five. Eagles at Bears tonight.</div>
<div class="line"><b>The AI Editor, graded.</b> Bills 11&ndash;6: 3&ndash;0, ahead of pace. Jets 6&ndash;11: 1&ndash;2, about on it. Ravens over Rams in the Super Bowl: Baltimore 2&ndash;1, the Rams 1&ndash;2.</div>
<div class="line"><b>Sunday, both at one:</b> Patriots at Buffalo; Jets at Chicago.</div>
''')
S('<div class="touch-head">Rain Set the Grid</div>','<div class="cards">','''<div class="touch-head">Larson Takes Kansas</div>
<div class="line">Kyle Larson won both stages, led 235 laps and took the lead from Chase Briscoe with six laps to go, beating Austin Cindric by just over half a second. Denny Hamlin finished third. With a maximum-points day, Larson now leads Hamlin by 26. Christopher Bell is 50 back.</div>
''')
R('<div class="cards"><div class="card"><div class="h">&#127937; Round 4 &middot; today</div><div class="m">Hollywood Casino 400, Kansas</div><div class="s">3:00 &middot; USA</div></div></div>',
  '<div class="cards"><div class="card"><div class="h">&#127937; Round 5</div><div class="m">South Point 400, Las Vegas</div><div class="s">Sun, Oct 4 &middot; 5:30 &middot; USA</div></div></div>')
S('<h2 class="sec"><span class="o">&#10038;</span>The Week Ahead','<h2 class="sec"><span class="o">&#9790;</span>On This Day','')
S('<div class="otd">','<h2 class="sec"><span class="o">&#10023;</span>Question','''<div class="otd"><b>September 28, 1928</b> &mdash; Alexander Fleming came back from vacation to his London lab and found mold growing on a dish of bacteria he had left out, with a clear ring around it where the bacteria had died. He called what the mold made penicillin. It took another fifteen years before it could be made in quantity.</div>
''')
R('The more of me you take, the more you leave behind. What am I?','I have keys but open no locks, space but no room, and you can enter but not go in. What am I?')
R('<b>Question of the Day:</b> Footsteps.','<b>Question of the Day:</b> A keyboard.')
R('storm reports via News 12 Long Island &middot; polls via Quinnipiac and Siena &middot; Dunkirk via the <i>Observer</i> &middot; North Tonawanda via WKBW and WGRZ','scores via the league &middot; Dunkirk via the <i>Observer</i> &middot; Rochester via WXXI &middot; Erie County via WKBW')
d.update(date='2026-09-28',no=96,body_html=b,plate_path=None,plate_caption='',headline="Bills 3-0 despite five turnovers · Jets fall late in Detroit · Larson wins Kansas · 77 by Thursday")
json.dump(d,open('site/data/edition-2026-09-28.json','w'),indent=1); json.dump(d,open('edition-2026-09-28.json','w'),indent=1)
p=json.load(open('site/data/pressure.json'))
if p[-1]['date']!='2026-09-28': p.append({"date":"2026-09-28","in":29.95,"mb":1014.2,"station":"KIAG","time":"05:53 EDT"})
json.dump(p,open('site/data/pressure.json','w'),indent=1)
print('ok')
