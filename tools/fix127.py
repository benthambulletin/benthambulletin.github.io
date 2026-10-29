import json
P=['/home/claude/edition-2026-10-29.json','/home/claude/site/data/edition-2026-10-29.json']
e=json.load(open(P[1]));b=e['body_html']
F=[("<h3>Update: Spain's Toll Rises to 68</h3><p>At least 68 people died and dozens were hurt when one high-speed train hit the back of another in central Spain Wednesday, CBS reports. The BBC has released audio of exchanges between the control center and the drivers before the crash; it is Spain's second major train crash this year.</p>",
 "<h3>Update: Spain's Toll Rises to 69</h3><p>At least 69 people died when a state-run high-speed train ran into the back of a stopped train near Urda, south of Madrid, Wednesday morning, the BBC reports. Audio published in Spanish media appears to show the moving train was cleared to go even though the other had stalled about 15 miles ahead; it is Spain's second deadly train crash this year, NPR notes.</p>"),
("<span class=\"lbl r\">Frost</span> Scottsville dips to 34 Friday and Saturday nights.","<span class=\"lbl r\">Record watch</span> Rochester's record for the date is 76, set in 1896, Rochester First says; Scottsville's forecast high is 75. <span class=\"lbl r\">Frost</span> Scottsville dips to 34 Friday and Saturday nights."),
("<span class=\"lbl t\">Outdoor window</span> This afternoon, before the wind and showers.</div>","<span class=\"lbl t\">Outdoor window</span> This afternoon, before the wind and showers.</div>\n<div class=\"line\"><span class=\"lbl t\">The Turning</span> Monroe County, around Scottsville, is expected to reach 80 percent color this week and peak in Greece, in bright yellow and red, the state's weekly report says.</div>"),
("Dunkirk has showers and thunderstorms tonight, 76 percent;","Dunkirk has showers and thunderstorms tonight, 80 percent;"),
('<div class="wire"><div class="num">1</div><div><h3>Lockport','<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; A Memorial for First Responders</h3><p>Monroe County dedicated a new First Responders Memorial on Civic Center Plaza Wednesday, WXXI reports. It stands next to the memorials for fallen sheriff\'s deputies and city police and firefighters.</p></div></div>\n<div class="wire"><div class="num">2</div><div><h3>Lockport'),
('<div class="wire"><div class="num">2</div><div><h3>Fredonia &middot; Volleyball Rolls On</h3><p>Fredonia\'s girls beat Salamanca Wednesday in the Section VI Class B2 volleyball quarterfinals at Fredonia High, the <i>Observer</i> reports. Coach Amanda Krakowiak called a timeout with the first set tied 20&ndash;20 to reset her team.</p>',
 '<div class="wire"><div class="num">3</div><div><h3>Fredonia &middot; Volleyball Rolls On</h3><p>Fredonia\'s girls swept Salamanca 25&ndash;21, 25&ndash;3, 25&ndash;15 Wednesday in the Section VI Class B2 volleyball quarterfinals at Fredonia High, the <i>Observer</i> reports. Tied 20&ndash;20 in the first set, the \'Billies scored five of the next six points to take it.</p>'),
("joining the biggest names in restaurant and grocery delivery, CBS reports.","uniting a major restaurant-delivery company with one of the nation's top grocery-delivery services, CBS reports."),
("U2 will play a small, invitation-only show for BBC Music in central London on Nov. 3, Billboard reports.","U2 will play an intimate show for a select group of fans for BBC Music in central London on Nov. 3, Billboard reports."),
("bring a jacket, since the Weather Service has gusts to 37 and a 30 percent chance of showers after 5.","bring a jacket, since showers may arrive by the end."),
("headlines via CBS, BBC, WKBW,","headlines via CBS, BBC, NPR, WKBW, WXXI, Rochester First,")]
for a,c in F:
  assert b.count(a)==1,a[:60]; b=b.replace(a,c)
e['body_html']=b
for p in P: json.dump(e,open(p,'w'),ensure_ascii=False,indent=1)
print('fixed')
