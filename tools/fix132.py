import json
P=['/home/claude/edition-2026-11-03.json','/home/claude/site/data/edition-2026-11-03.json']
e=json.load(open(P[1]));b=e['body_html']
def R(a,c):
    global b
    assert b.count(a)==1,a[:60]; b=b.replace(a,c)
R('<div class="touch-head">Short Week for Baltimore</div>','<div class="touch-head">Two Road Trips</div>')
R('<b>Bills</b> &middot; Buffalo has a week to rest before Monday night at Minnesota, 8:15. The Ravens, beaten 36&ndash;10 in Orchard Park, host Jacksonville Thursday night, and Sportradar gives them only a 20 percent chance.',
  '<b>Bills</b> &middot; A long week before Monday night at Minnesota, 8:15. Thursday night opens the week with Jacksonville at Baltimore, the first game on this week\'s pool sheet.')
R('<b>Jets</b> &middot; At Kansas City Sunday at 1:00. Sportradar likes the Chiefs at 80 percent, but Kansas City is coming off a 28&ndash;24 loss in Denver.',
  '<b>Jets</b> &middot; At Kansas City Sunday at 1:00. Sportradar gives the Jets a 20 percent chance; the Chiefs are the clear favorite at home.')
R('The administration had filed the request earlier the same day.','The administration filed the request only hours earlier, on the eve of today\'s vote; the ruling lets California keep counting those ballots.')
R("to help people hit by September's flash flooding apply","to help people hit by September's record flash flooding in North Buffalo and the Northtowns apply")
R('<b>Venus sextiles Jupiter in your sign</b>. Warm day','<b>The moon passes through Leo</b>. Warm day')
R('The <i>Chicago Tribune</i> went to press with "DEWEY DEFEATS TRUMAN" before the count was done. Truman won, and the next day, in St. Louis, he held the paper up for photographers.',
  'The <i>Chicago Tribune</i> edition dated today ran "DEWEY DEFEATS TRUMAN," printed before the count was done. Truman won, and on Nov. 4, at St. Louis Union Station, he held a copy up for photographers.')
R('Not yet: the forecast bottoms out at 40, Saturday night, as the warm spell ends.','Not yet: the coldest night in the forecast is Saturday, 40 here and 38 in Scottsville.')
R('<b>10h 13m</b><br>','<b>10h 13m</b>, 2&frac12; minutes less than yesterday<br>')
R('<span class="lbl r">Vote early</span> Early voting is over','<span class="lbl r">Polls</span> Early voting is over')
e['body_html']=b
for p in P: json.dump(e,open(p,'w'),ensure_ascii=False,indent=1)
print('ok')
