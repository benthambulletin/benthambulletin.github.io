import json
src = json.load(open('/home/claude/site/data/edition-2026-11-07.json'))['body_html']
def R(a, c, n=1):
    global src
    assert src.count(a) == n, ('R', a[:60], src.count(a)); src = src.replace(a, c)
def S(start, end, new):
    global src
    i = src.find(start); j = src.find(end, i + len(start))
    assert i >= 0 and j > i, ('S', start[:50], end[:50]); src = src[:i] + new + src[j:]

f = json.load(open('/home/claude/site/data/forecast.json'))
hr = [h['temp'] for h in f['towns']['North Tonawanda']['hourly']][:24]
W, H, P = 320, 62, 12
lo, hi = min(hr), max(hr)
xs = [P + i * (W - 2 * P) / (len(hr) - 1) for i in range(len(hr))]
ys = [H - P - (t - lo) * (H - 2 * P - 10) / max(1, hi - lo) for t in hr]
pts = ' '.join(f'{x:.1f},{y:.1f}' for x, y in zip(xs, ys))
ih, il = hr.index(hi), len(hr) - 1 - hr[::-1].index(lo)
lanc = 'start' if il < len(hr) / 2 else 'end'; lx = xs[il] + (5 if lanc == 'start' else -5)
spark = (f'<div class="line"><span class="lbl t">Next 24 hours</span></div>'
         f'<svg viewBox="0 0 {W} {H}" style="display:block;width:100%;max-width:420px;height:auto;margin:0 auto .4rem" role="img" aria-label="Hourly temperatures for North Tonawanda over the next 24 hours, from {hr[0]} now to a high of {hi} and a low of {lo}">'
         f'<polyline points="{pts}" fill="none" stroke="#9c3216" stroke-width="2" stroke-linejoin="round"/>'
         f'<circle cx="{xs[ih]:.1f}" cy="{ys[ih]:.1f}" r="3" fill="#9c3216"/><text x="{xs[ih]:.1f}" y="{ys[ih]-6:.1f}" text-anchor="middle" font-family="Archivo,Arial" font-size="10" fill="#24170c">{hi}&deg;</text>'
         f'<circle cx="{xs[il]:.1f}" cy="{ys[il]:.1f}" r="3" fill="#2f5e3e"/><text x="{lx:.1f}" y="{ys[il]-6:.1f}" text-anchor="{lanc}" font-family="Archivo,Arial" font-size="10" fill="#24170c">{lo}&deg;</text>'
         f'<text x="{P}" y="{H-1}" font-family="Archivo,Arial" font-size="9" fill="#6b5a48">now</text><text x="{W-P}" y="{H-1}" text-anchor="end" font-family="Archivo,Arial" font-size="9" fill="#6b5a48">this time tomorrow</text></svg>\n')

# cover: a checkered flag snapping in a gusty sky over an oval, leaves blowing
cells = ''.join(f'<rect x="{c*18}" y="{r*18}" width="18" height="18" fill="{"#24170c" if (r+c)%2 else "#fbf5e4"}"/>' for r in range(5) for c in range(7))
leaves = ''.join(f'<path class="lf l{i}" d="M0 0 q6 -8 12 0 q-6 8 -12 0z" fill="{col}" transform="translate({x} {y})"/>' for i, (x, y, col) in enumerate([(40, 120, '#cf6f1a'), (120, 60, '#9c3216'), (260, 150, '#b8862b'), (500, 90, '#cf6f1a'), (620, 170, '#9c3216')]))
svg = f'''<svg viewBox="0 0 750 375" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="A checkered flag snapping in a gusty autumn wind above an oval racetrack, with leaves blowing past" style="display:block;width:100%;height:auto">
<style>.fl{{animation:wave 1.6s ease-in-out infinite;transform-origin:0 50%}}@keyframes wave{{0%,100%{{transform:skewY(0deg) scaleX(1)}}50%{{transform:skewY(-6deg) scaleX(.94)}}}}
.lf{{animation:blow 7s linear infinite}}.l1{{animation-delay:-1.5s}}.l2{{animation-delay:-3s}}.l3{{animation-delay:-4.5s}}.l4{{animation-delay:-6s}}
@keyframes blow{{0%{{transform:translate(-60px,120px) rotate(0)}}100%{{transform:translate(800px,40px) rotate(720deg)}}}}
.cl{{animation:drift 30s linear infinite}}@keyframes drift{{from{{transform:translateX(-200px)}}to{{transform:translateX(800px)}}}}
@media (prefers-reduced-motion:reduce){{.fl,.lf,.cl{{animation:none}}}}</style>
<defs><linearGradient id="sk" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#9fb3bf"/><stop offset="1" stop-color="#e8dcc4"/></linearGradient></defs>
<rect width="750" height="375" fill="url(#sk)"/>
<g class="cl" opacity=".75"><ellipse cx="120" cy="70" rx="90" ry="22" fill="#f4ede0"/><ellipse cx="420" cy="50" rx="120" ry="26" fill="#f4ede0"/></g>
<ellipse cx="375" cy="320" rx="330" ry="70" fill="#5b4a3a"/><ellipse cx="375" cy="320" rx="270" ry="44" fill="#2f5e3e"/>
<path d="M60 320 a315 62 0 0 0 630 0" fill="none" stroke="#fbf5e4" stroke-width="2" stroke-dasharray="14 10" opacity=".7"/>
<rect x="196" y="70" width="6" height="240" fill="#3a2a1c"/><circle cx="199" cy="68" r="6" fill="#b8862b"/>
<g transform="translate(202 78)"><g class="fl">{cells}</g></g>
{leaves}
</svg>'''

NEW = '''<div class="tiles">
  <div class="tile"><div class="v">55&deg;</div><div class="k">Partly Sunny</div></div>
  <div class="tile"><div class="v">4:59</div><div class="k">Sunset</div></div>
  <div class="tile urg"><div class="v">1</div><div class="k">Day to Bills&ndash;Vikings</div></div>
</div>
<div class="calline"><b>Coming up</b> Today &middot; Jets at KC, 1:00; NASCAR finale, 3:00 &middot; Mon &middot; Bills at MIN, 8:15 &middot; Wed &middot; Veterans Day<br><b>Migraine log</b> Garret, 5 days ago (2 this month); no one else this week</div>
<div class="plate-wrap"><div class="frame"><span class="tick tl"></span><span class="tick tr"></span><span class="tick bl"></span><span class="tick br"></span>
''' + svg + '''</div>
<div class="plate-cap">Plate I &middot; The Family Album</div>
<div class="plate-sub">Finale Sunday, and a gusty one</div></div>
<div class="dbl-tight"><div class="a"></div><div class="b"></div></div>
<h2 class="sec"><span class="o">&#9873;</span>The Sunday Spotlight<span class="o">&#9873;</span></h2>
<div class="spot"><h3>How the NASCAR Chase Ends</h3>
<p><i>An AI wrote this section.</i></p>
<p><b>What changed.</b> NASCAR scrapped its old elimination playoffs, which ended with four drivers racing one final race where the best finisher took the title, before this season, and brought back "the Chase," Fox Sports reports. After the regular season the top 16 drivers had their points reset, with 100 points separating first from 16th, then ran 10 races in which every point counted and nobody was knocked out. Today's race at Homestead-Miami Speedway, a 1.5-mile oval near Miami, is the 10th and last.</p>
<p><b>The math.</b> Only three drivers can still win, NBC Sports says: Kyle Larson with 2,469 points, Christopher Bell 67 behind and Denny Hamlin 70 behind. A race win pays 55 points, each of the race's two "stages" (checkpoints at set laps) pays up to 10 to the top ten, and the fastest lap pays one, so 76 is the most anyone can earn today. Larson clinches with just 9: a top-three run at the end of Stage 1 on lap 80 would do it, and with no stage points at all, finishing 28th or better would. Bell and Hamlin both have to win the race, pile up stage points and need Larson's day to fall apart.</p>
<p><b>What it means.</b> For a casual fan, the new format rewards a whole fall of good racing rather than one lucky Sunday, and the trade-off shows today: Larson's cushion is big enough that the drama may be over early. If he holds on, it is his third Cup title, after 2021 and 2025, Fox says; neither Bell nor Hamlin has won one.</p>
<p><b>Coming down the road.</b> The green flag drops shortly after 3 p.m. on NBC, with pre-race coverage at 2, about when the Jets game in Kansas City is winding down. Monday's paper will have the champion, and The Chase goes quiet until next season's Daytona 500.</p></div>
<h2 class="sec"><span class="o">&#9788;</span>The Weather Glass<span class="o">&#9788;</span></h2>
<div class="wx"><div class="bigtemp">55<sup>&deg;</sup></div><div class="wxtext">
<span class="lede">A blustery Sunday: partly sunny and 55, with southwest gusts as high as 44 mph</span>
Low <b>44&deg;</b> tonight &middot; showers possible, 50%<br>Showers after 4 p.m., 20% &middot; fcst high 55, normal 51</div></div>
<div class="towns">
  <div class="town"><div class="n">North Tonawanda</div><div class="t">40<sup>&deg;</sup></div><div class="d">Partly cloudy<br>high 55&deg;</div></div>
  <div class="town"><div class="n">Dunkirk</div><div class="t">48<sup>&deg;</sup></div><div class="d">Mostly cloudy<br>high 54&deg;</div></div>
  <div class="town"><div class="n">Scottsville</div><div class="t">45<sup>&deg;</sup></div><div class="d">Cloudy<br>high 57&deg;</div></div>
</div>
<div class="strip5">
  <div><div class="d">Sun</div><div class="i">&#127788;</div><div class="h">55</div><div class="w">partly sunny, gusty</div></div>
  <div><div class="d">Mon</div><div class="i">&#9925;</div><div class="h">53</div><div class="w">morning showers</div></div>
  <div><div class="d">Tue</div><div class="i">&#9728;</div><div class="h">60</div><div class="w">mostly sunny</div></div>
  <div><div class="d">Wed</div><div class="i">&#9925;</div><div class="h">55</div><div class="w">partly sunny</div></div>
  <div><div class="d">Thu</div><div class="i">&#127783;</div><div class="h">47</div><div class="w">showers</div></div>
</div>
''' + spark + '''<div class="line"><span class="lbl t">First flakes?</span> Thursday night brings a chance of rain and snow showers in North Tonawanda, with a low around 31. <span class="lbl t">Outdoor window</span> Tuesday, mostly sunny and 60.</div>
<div class="line"><span class="lbl t">The lakes</span> Erie 59&deg; off Buffalo, Ontario 58&deg; off Rochester, Saturday's readings.</div>
<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky<span class="o">&#9790;</span></h2>
<div class="sky"><svg viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg"><circle cx="50" cy="50" r="46" fill="#211c14"/><path d="M50 4 A46 46 0 0 0 50 96 A45.5 46 0 0 1 50 4Z" fill="#f4e5b4"/><circle cx="50" cy="50" r="46" fill="none" stroke="#211c14" stroke-width="2"/></svg><div>
<b>A day from new</b>, 1 percent lit and lost in the sun's glare, in Virgo; rose at 6:27 a.m., sets at 4:14 p.m.<br>
<span class="lbl t">Sun</span> 6:58a &ndash; 4:59p &middot; <b>10h 0m</b> of daylight, 2.4 minutes less than Saturday<br>
<span class="lbl t">Planets</span> Look south around 10 tonight for Saturn, still the lone bright one.<br>
<span class="lbl t">New moon</span> Mon, Nov 9 &middot; <span class="lbl t">Beaver Moon</span> Tue, Nov 24</div></div>
<div class="stars">
<div class="star"><div class="sg">Aries</div><div><b>The moon and Mercury huddle in Scorpio, far from your sign.</b> Secrets come out today. Keep the good ones. <span class="who">Kaylani, Luka</span></div></div>
<div class="star"><div class="sg">Cancer</div><div><b>The moon in Scorpio trines your sign.</b> Easy and warm. Call someone you've been meaning to. <span class="who">Gregg</span></div></div>
<div class="star"><div class="sg">Leo</div><div><b>The moon in Scorpio squares your sign.</b> Pride versus the remote control. Let them have it. <span class="who">Leah, Tommy</span></div></div>
<div class="star"><div class="sg">Virgo</div><div><b>The moon in Scorpio sextiles your sign.</b> A tidy plan works today. Make the plan a nap. <span class="who">Derek, Joanne</span></div></div>
<div class="star"><div class="sg">Scorpio</div><div><b>The moon is in your sign, right beside Mercury.</b> Your words land hard today. Say the sharp thing kindly. <span class="who">Ariel, Claire, Garret</span></div></div>
</div>
<div style="font-family:'LOI';font-style:italic;font-size:.8rem;color:var(--soft);margin-top:.4rem">The sky is real; the readings are for fun.</div>
<h2 class="sec"><span class="o">&#10038;</span>The Ledger<span class="o">&#10038;</span></h2>
<div class="ledger"><div class="num"><div class="cap">Fewer people homeless in America last year</div><div class="big">49,000</div></div>
<div class="txt">The count fell more than 6 percent in 2025, NPR reports, the second year in a row it has gone down after years of record highs.</div></div>
<h2 class="sec"><span class="o">&#10038;</span>The National Wire<span class="o">&#10038;</span></h2>
<div class="wire lead"><div><span class="kick">The Lead</span><h3>Trump Offers Dana White the Podium</h3>
<p>President Trump said Saturday he has offered the job of White House press secretary, the president's chief spokesman who briefs reporters, to UFC boss Dana White, NPR reports. "Dana, please take the job!" he posted.</p>
<p>White, in London promoting a boxing match, said he was flying to Washington and would meet with Trump on Monday. Asked how he would fit it in with running the UFC, the mixed-martial-arts league, he said, "Yeah, I got a lot of jobs already." He also posted a photo of himself at the briefing-room podium, captioned "On to the next chapter."</p>
<p>The job has been open since Oct. 16, when Katie Zacharia was removed after five days, CBS says; Karoline Leavitt left it in August. At least one outlet suggested the offer might be tongue-in-cheek, and the White House did not comment.</p>
<div class="pull">"Dana will be a Press Secretary like none other," Trump wrote.</div>
</div></div>
<div class="wire"><div class="num">2</div><div><h3>Update: Who Leads the New Senate?</h3><p>Democrats will hold at least 54 Senate seats when Congress convenes in January, CBS reports, and several incoming senators want someone other than Chuck Schumer, who has led Senate Democrats since 2017, as majority leader, the senator who decides what comes up for a vote. "There should be no coronation," said Maryland Sen. Chris Van Hollen, whose aide says he will not run for the job himself.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Six Killed in Krakow</h3><p>A 25-year-old gunman with far-right views drove into the Main Square of Krakow, Poland's second-largest city, on Saturday and fired at random, killing six people and wounding 15 before police shot him within three minutes, AP and the BBC report. Police later found three of his family members dead at his home; Poland's defense minister called it "an act of terror."</p></div></div>
<h2 class="sec"><span class="o">&#9962;</span>The Home Wire</h2>
'''
NEW = NEW.replace('<h2 class="sec"><span class="o">&#9962;</span>The Home Wire</h2>\n', '<h2 class="sec"><span class="o">&#9962;</span>The Home Wire<span class="o">&#9962;</span></h2>\n') + '''<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; A Perfect 900</h3><p>Steve Meyer bowled three straight 300 games, twelve strikes in a row each time, at Domm's Bowling Center on Saturday for a perfect 900 series, Rochester First reports. He is only the third bowler in Upstate New York to do it.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>Bemus Point &middot; Veterans Charity Fights Fraud Charges</h3><p>The operators of Healing for Heroes, a retreat for disabled veterans, are fighting charges Attorney General Letitia James filed in August, the Dunkirk <i>Observer</i> reports. She says the couple who run it rented the 30-acre property on Airbnb at least 32 times in 2024 and 2025, kept the $33,312 for themselves, and spent nearly half of about $100,000 in donations on their property.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>Buffalo &amp; Grand Island &middot; The State Sues Over Seneca Land</h3><p>New York has filed lawsuits against the U.S. Interior Department over its decisions giving Seneca Nation land in Buffalo and on Grand Island "restricted-fee" status, WIVB reports. That federal protection takes the land out from under state oversight, the state argues, WGRZ says.</p></div></div>
<h2 class="sec"><span class="o">&#9733;</span>The Marquee<span class="o">&#9733;</span></h2>
<div class="wire"><div class="num">1</div><div><h3>Druski Hosts SNL, With Emma Stone</h3><p>Druski, the comedian famous for his phone videos, hosted <i>Saturday Night Live</i> for the first time last night, the first online content creator ever to host, the Hollywood Reporter says. His co-star in the coming romantic comedy <i>The Catch</i>, Emma Stone, joined him for the monologue, Deadline reports.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>More <i>Heated Rivalry</i></h3><p>The hit hockey romance is filming a third season alongside its second, and a holiday movie shoots in December for theaters next December, Deadline's sources say, Page Six reports. The show's Canadian network, Crave, says it has "no projects to confirm"; in the U.S. it streams on HBO.</p></div></div>
<div class="wire"><div class="num">3</div><div><h3>U2 Weighs In on Sheeran and Macklemore</h3><p>After Macklemore was dropped from Ed Sheeran's U.S. tour over things he said, U2's the Edge told the BBC, "We totally support Macklemore's right as an artist to say what he wanted to say," Billboard reports. He added, "I don't think Ed should be vilified."</p></div></div>
<h2 class="sec"><span class="o">&#127944;</span>The Gridiron<span class="o">&#127944;</span></h2>
<div class="line"><b>Bills</b> &middot; Left tackle Dion Dawkins is listed as questionable for Monday night at Minnesota with a rib injury, the first time this season he is at risk of missing a game, and receiver Joshua Palmer is out with a bad hamstring, ProFootballTalk reports. The NFL fined Baltimore's Roquan Smith $35,822 for two hits last week that drew no flag, one a facemask on Josh Allen, Buffalo Rumblings says. Monday is the league's top-scoring offense, 33.3 points a game, against its best defense.</div>
<div class="line"><b>Jets</b> &middot; Kickoff in Kansas City is shortly after 1:00 in sunny weather in the low 60s, Gang Green Nation reports, against a Chiefs team that has lost two straight after a 5&ndash;0 start. The Jets called up linebacker Troy Reeder and tackle Brant Banks from the practice squad for the game.</div>
<h2 class="sec"><span class="o">&#9873;</span>The Chase<span class="o">&#9873;</span></h2>
<div class="line">Finale day. The standings and the math are in the Sunday Spotlight up top.</div>
<h2 class="sec"><span class="o">&#127810;</span>The Week Ahead<span class="o">&#127810;</span></h2>
<div class="line"><b>Weather.</b> Last week: summer-warm through Wednesday, then a cooldown; the coldest dawn was 39 on Saturday. This week runs 53 to 60 through Wednesday, then 47 Thursday with the first chance of snow showers that night.</div>
<div class="line"><b>Games.</b> Bills at Minnesota Monday night at 8:15; Bills at the Jets next Sunday, Nov. 15, at 1:00.</div>
<div class="line"><b>Veterans Day.</b> Wednesday.</div>
<div class="line"><b>Next Sunday's Spotlight.</b> This winter's heating bill: National Grid and NYSEG rates, what has changed and the cheapest things that actually lower a bill.</div>
<h2 class="sec"><span class="o">&#10023;</span>The Sunday Question<span class="o">&#10023;</span></h2>
<div class="qotd"><b>Last week: what's the first election you remember?</b><br><b>Ariel:</b> "Clinton's first term!"<br><br><b>This week, with the first flakes in the forecast: what's the best snow day you remember?</b><br>Send it at <a href="https://tally.so/r/rjxDpl">tally.so/r/rjxDpl</a> this week. Answers run here next Sunday under your names.</div>
<h2 class="sec"><span class="o">&#9790;</span>On This Day<span class="o">&#9790;</span></h2>
<div class="otd"><b>November 8, 1895</b> &mdash; In his lab in W&uuml;rzburg, Germany, physicist Wilhelm R&ouml;ntgen noticed a glow from rays that passed straight through paper and wood. He called them X-rays, the X for unknown.</div>
<h2 class="sec"><span class="o">&#10023;</span>Question of the Day<span class="o">&#10023;</span></h2>
<div class="qotd">I'm born in a storm, I have coal for eyes and a carrot for a nose, and the first warm day is the end of me. What am I? <i>Answer below the fold.</i></div>
'''

R('No. 136', 'No. 137')
R('Saturday &middot; November 7 &middot; 2026', 'Sunday &middot; November 8 &middot; 2026')
S('<div class="tiles">', '<div class="dbl"><div class="a"></div><div class="b"></div></div>\n<div class="colo">', NEW)
R("<b>Question of the Day:</b> A winter boot.", "<b>Question of the Day:</b> A snowman.")
S('<div class="s">Forecast, lake temperatures', '<div class="ask">',
'''<div class="s">Forecast, lake temperatures and radar per NWS Buffalo &middot; Niagara Falls, Dunkirk and Rochester stations &middot; normals from NOAA &middot; sky computed for 14120 &middot; headlines via NPR, CBS, the BBC, Rochester First, the Dunkirk <i>Observer</i>, WIVB, WGRZ, the Hollywood Reporter, Deadline, Page Six, Billboard, ProFootballTalk, Buffalo Rumblings, Gang Green Nation &middot; Spotlight from Fox Sports and NBC Sports &middot; schedule and NASCAR points via Sportradar</div>
''')
ed = {"date": "2026-11-08", "no": 137, "body_html": src, "plate_path": None, "plate_caption": "Finale Sunday, and a gusty one",
      "headline": "Trump offers Dana White the podium · How the Chase ends · Druski hosts SNL"}
for p in ['/home/claude/edition-2026-11-08.json', '/home/claude/site/data/edition-2026-11-08.json']:
    json.dump(ed, open(p, 'w'), ensure_ascii=False, indent=1)
print('ok', hr[0], lo, hi)
