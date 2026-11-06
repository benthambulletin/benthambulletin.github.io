import json
P=['/home/claude/edition-2026-11-06.json','/home/claude/site/data/edition-2026-11-06.json']
e=json.load(open(P[1]));b=e['body_html']
def R(a,c):
    global b
    assert b.count(a)==1,a[:60]; b=b.replace(a,c)
R("<b>Umbrella Friday</b>: rain showers and 56 today, more rain Saturday, then a sunny, breezy Sunday for the Jets in Kansas City and NASCAR's last race.",
  "<b>Gray Friday</b>: rain today and more Saturday, then a mostly sunny, gusty Sunday at home for the Jets game in Kansas City and NASCAR's finale.")
R("<b>Bills</b> &middot; At Minnesota Monday night, 8:15.</div>","<b>Bills</b> &middot; At Minnesota Monday night, 8:15; the Vikings are 6&ndash;1, same as Buffalo.</div>")
R("<b>Jets</b> &middot; At Kansas City Sunday, 1:00.</div>","<b>Jets</b> &middot; At Kansas City Sunday, 1:00; the Chiefs are 5&ndash;2 and lost at Denver last week.</div>")
R("A federal judge in Washington blocked construction of President Trump's proposed 250-foot triumphal arch for 14 days, late Thursday, siding for now with a group of Vietnam veterans, the District of Columbia and Virginia, CBS reports. Judge Tanya Chutkan wrote that they are likely to show the government didn't follow required legal steps.",
  "A federal judge in Washington blocked construction of President Trump's proposed 250-foot triumphal arch for 14 days late Thursday, hours after the federal planning commission for the capital approved it 8&ndash;4, CBS reports. Judge Tanya Chutkan sided for now with the Vietnam veterans, the District of Columbia and Virginia who sued, writing that they are likely to show the government skipped required legal steps.")
R("Pomfret's zoning appeals board granted Steve St. George a special-use permit for a concrete and asphalt recycling yard at his property, with a list of conditions attached, the <i>Observer</i> reports. The approval came at the board's third hearing, Oct. 6.",
  "Pomfret's zoning appeals board granted Steve St. George a special-use permit for a concrete and asphalt recycling yard on Webster Road at its third hearing, Oct. 6, the <i>Observer</i> reports. The recycling equipment can run only on weekdays from 7:30 a.m. to 4 p.m., and no more than 50 days a year.")
R("It's one of the college's biggest volunteer days.","Homeowners who want help hang a flier on their door; 17 student clubs have signed up.")
R("Birthday month nearly done; one more good story to tell.","Two weeks of Scorpio season left; spend them on one good story.")
R("He said a proposed film about the character was turned down because, as he put it, \"he's dead.\"","He said Disney turned down <i>The Hunt for Ben Solo</i>, a film he spent two years developing with director Steven Soderbergh, with a short answer: \"No, he's dead.\"")
R("<b>Neptune, in your sign, sextiles Pluto</b>.","<b>Neptune sextiles Pluto</b>.")
R("scores via Sportradar","scores and NASCAR points via Sportradar")
R("Takashi Yamazaki's R-rated follow-up,","Takashi Yamazaki's R-rated new Godzilla film,")
e['body_html']=b
for p in P: json.dump(e,open(p,'w'),ensure_ascii=False,indent=1)
print('ok')
