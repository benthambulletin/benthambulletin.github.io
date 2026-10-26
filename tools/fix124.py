import json
P=['/home/claude/edition-2026-10-26.json','/home/claude/site/data/edition-2026-10-26.json']
e=json.load(open(P[0]));b=e['body_html']
F=[("No new numbers until the state's foliage report Wednesday afternoon.","This is North Tonawanda's usual peak week. The latest state report still has Lewiston, Buffalo, East Aurora, Chautauqua and Jamestown changing fastest; fresh numbers Wednesday afternoon."),
("<b>Bills</b> &middot; Off Sunday and still 5&ndash;1, a game and a half clear of New England. Baltimore visits Sunday at 1:00, coming off a 35&ndash;13 home loss to Cincinnati.","<b>Bills</b> &middot; Off Sunday and still 5&ndash;1, a game and a half clear of New England with the bye behind them. Baltimore visits Sunday at 1:00, 4&ndash;3 after a 35&ndash;13 home loss to Cincinnati, and it's the same Ravens team the AI Editor picked to win the Super Bowl."),
("Five days to Halloween: a partly sunny afternoon","A partly sunny afternoon"),
("and that's the harbor on the cover, sent at 6 this morning.","and that's the water on the cover, from 6 this morning."),
("with Chappell Roan did it;","with Chappell Roan drove most of the jump;"),
("<h3>Serbia's Strongman Concedes</h3>","<h3>Serbia's Vu&#269;i&#263; Concedes</h3>"),
("movement in snap parliamentary elections","movement in early (snap) parliamentary elections"),
("Dunkirk Observer, Billboard &middot; scores","Dunkirk Observer, Billboard, AP via the Dunkirk Observer &middot; scores"),
("Fog early &middot; high 66&deg;","Fog early (fcst) &middot; high 66&deg;"),
("officers were waiting at her house when the man showed up.","officers were waiting at her house and arrested him when he showed up."),
("<span class=\"lbl t\">Away</span> Long Island, last day:","<span class=\"lbl t\">Away</span> The family on Long Island, last day:")]
for a,c in F:
  assert b.count(a)==1,a; b=b.replace(a,c)
e['body_html']=b
for p in P: json.dump(e,open(p,'w'),ensure_ascii=False,indent=1)
print('fixed')
