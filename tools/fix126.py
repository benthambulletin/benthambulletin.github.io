import json
P=['/home/claude/edition-2026-10-28.json','/home/claude/site/data/edition-2026-10-28.json']
e=json.load(open(P[1]));b=e['body_html']
i=b.find('<h2 class="sec"><span class="o">&#127810;</span>The Turning');j=b.find('<h2 class="sec"><span class="o">&#9790;</span>The Almanac Sky')
assert 0<i<j and j-i<400; b=b[:i]+b[j:]
F=[("Showers before 2 a.m., 50 percent, with gusts to 30; the Bills rally in Niagara Square starts at 5:30.","Showers before 2 a.m., 50 percent, with gusts to 30; less than a tenth of an inch."),
("With 70 percent counted, Netanyahu's Likud has 20.6 percent and Eisenkot's Yashar 15.9, and the bargaining to build a government has begun.","With 70 percent counted, Netanyahu's Likud has 20.6 percent and Eisenkot's Yashar 15.9; whoever governs needs a majority of the Knesset's 120 seats."),
("Saturn has the early evening to itself; by the time the moon clears the northeastern trees around 7:40, the ringed planet is high in the southeast.","Saturn has the early evening to itself, low in the southeast at dusk. The moon rises in the northeast at 7:40, and by 9:30 Saturn stands about halfway up the southeastern sky."),
("<b>Bills</b> &middot; Baltimore was outscored 35&ndash;0 after halftime in Sunday's loss to Cincinnati and has been outscored by 70 points in second halves this season, the AP reports; Lamar Jackson has missed three straight games with an ankle injury. The Bills (5&ndash;1) host them Sunday at 1:00.","<b>Bills</b> &middot; Rookies spent their day off Tuesday giving middle schoolers from Franklin and Hoover a tour of the new Highmark Stadium, WKBW reports. The Bills (5&ndash;1) host Baltimore Sunday at 1:00; the Ravens were outscored 35&ndash;0 after halftime last week, the AP reports, and Lamar Jackson has missed three straight games."),
("Tuesday they reached back to their early songs.","Tuesday they reached back to \"This Is a Call,\" from their first album in 1995.")]
for a,c in F:
  assert b.count(a)==1,a; b=b.replace(a,c)
e['body_html']=b
for p in P: json.dump(e,open(p,'w'),ensure_ascii=False,indent=1)
print('fixed')
