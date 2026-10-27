import json
P=['/home/claude/edition-2026-10-27.json','/home/claude/site/data/edition-2026-10-27.json']
e=json.load(open(P[0]));b=e['body_html']
F=[("Four days to Halloween, and the porch pumpkins have one more week of work.","Four days to Halloween, and the forecast for trick-or-treat night is in the Weather Glass below."),
("The moon comes up in the east-northeast at 6:50, more than half an hour after sunset and later each night now. Saturn is already well up in the southeast by then.","The moon comes up in the northeast at 6:50, more than half an hour after sunset and later each night now. Saturn is already up, low in the east, and is a third of the way up the southeastern sky by 8:30."),
("He has been a TV doctor since 1994, when he started as John Carter on <i>ER</i>.","He first played a TV doctor in 1994, as medical student and later Dr. John Carter on NBC's <i>ER</i>, alongside George Clooney."),
("<b>Jets</b> &middot; Back at MetLife Sunday at 1:00 against the Raiders, who are 3&ndash;4. The Jets (2&ndash;5) lost to Miami by three this week, with Geno Smith's three touchdown passes nearly enough.","<b>Jets</b> &middot; The Raiders (3&ndash;4) come to MetLife Sunday at 1:00, a week after their 35&ndash;21 home loss to the Rams. The Jets are 2&ndash;5 and get a team only a game better than them."),
('<div class="touch-head">Ravens Week</div>','<div class="touch-head">Ravens and Raiders</div>'),
('<span class="lbl t">Clocks fall back</span> Sun, Nov 1 &middot; <span class="lbl t">New moon</span> Mon, Nov 9','<span class="lbl t">New moon</span> Mon, Nov 9 &middot; <span class="lbl t">Beaver Moon</span> Tue, Nov 24'),
("The proposed budget is just over $39.8 million, up from $39.28 million; the board's director says costs are under control but revenue is falling.","The proposed budget, unveiled by executive director Sean Costello, is just over $39.8 million, up from $39.28 million; the <i>Gazette</i> says costs are under control but revenue is falling."),
("From 2,000 households. The city now hopes to reach about 10,000 within five years, with 1,000 already on the waitlist, WKBW reports.","From 2,000 households. Farmer Pirates, which runs the pickup, hopes to reach about 10,000 residents within five years, with 1,000 already on the waitlist, WKBW reports."),
("The state's new foliage numbers land Wednesday afternoon, in North Tonawanda's usual peak week.","The state's new foliage numbers land Wednesday afternoon."),
("Warming to 69 Thursday; showers Thursday night, 48%","Warming to 69 Thursday, gusts to 28; showers after 8 p.m. Thursday night, 48%"),
("at SoFi Stadium in Los Angeles on","at SoFi Stadium in Inglewood, near Los Angeles, on"),
("Panthers at Green Bay.","Panthers at Packers.")]
for a,c in F:
  assert b.count(a)==1,a; b=b.replace(a,c)
e['body_html']=b
for p in P: json.dump(e,open(p,'w'),ensure_ascii=False,indent=1)
print('fixed')
