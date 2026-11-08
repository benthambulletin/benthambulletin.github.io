import json
p='/home/claude/edition-2026-11-08.json'; ed=json.load(open(p)); s=ed['body_html']
def R(a,b):
    global s; assert s.count(a)==1,(a[:60],s.count(a)); s=s.replace(a,b)
R('Last week: summer-warm through Wednesday, then a cooldown; the coldest dawn was 39 on Saturday. This week runs 53 to 60 through Wednesday, then 47 Thursday with the first chance of snow showers that night.',
  'Last week: warm through Wednesday (77 that day), then a cooldown; the coldest dawn was 36 last Sunday. This week runs 53 to 60 through Wednesday, then 47 Thursday, with a chance of rain and snow showers that night.')
R('This week, with the first flakes in the forecast:','This week, with snow showers in Thursday night&rsquo;s forecast:')
R('<span class="lbl t">First flakes?</span>','<span class="lbl t">Snow watch</span>')
R('For a casual fan, the new format rewards a whole fall of good racing rather than one lucky Sunday, and the trade-off shows today: Larson\'s cushion is big enough that the drama may be over early.',
  'For a casual fan, the change means a title earned over ten races rather than decided by one, and the math shows why today may not be close: Larson needs 9 points, Bell and Hamlin need a win and help.')
R(', about when the Jets game in Kansas City is winding down.',', while the Jets are still playing in Kansas City.')
R('in Virgo; rose at 6:27 a.m.','against the stars of Virgo; rose at 6:27 a.m.')
R('Buffalo &amp; Grand Island &middot; The State Sues','Grand Island &amp; Buffalo &middot; The State Sues')
R('The NFL fined Baltimore\'s Roquan Smith $35,822 for two hits last week that drew no flag, one a facemask on Josh Allen, Buffalo Rumblings says. Monday is the league\'s top-scoring offense, 33.3 points a game, against its best defense.',
  'The NFL fined Baltimore\'s Roquan Smith $35,822 for two unflagged hits last week, one a facemask on Josh Allen. Monday pits the Bills, the league\'s top-scoring offense at 33.3 points a game, against the Vikings, its best defense, Buffalo Rumblings says.')
R('headlines via NPR, CBS,','headlines via NPR, CBS, PBS NewsHour (AP),')
ed['body_html']=s
for q in [p,'/home/claude/site/data/edition-2026-11-08.json']: json.dump(ed,open(q,'w'),ensure_ascii=False,indent=1)
print('ok')
