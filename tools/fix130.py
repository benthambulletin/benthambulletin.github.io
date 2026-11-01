import json
P=['/home/claude/edition-2026-11-01.json','/home/claude/site/data/edition-2026-11-01.json']
e=json.load(open(P[1]));b=e['body_html']
F=[(" It took first place at Mickey Rats in Jamestown.",""),
("<b>What it means:</b> Garret's four came in two clusters, which fits what his own log has shown before: attacks tend to bunch together.","<b>What it means:</b> three of Garret's four came within a week (Oct. 23 to 29), which fits what his own log has shown before: attacks tend to bunch together."),
("Democrats lead narrowly in Maine, Ohio and Texas and comfortably in North Carolina, Iowa and Alaska are dead heats, and Kansas has tipped to the Democrat.","Democrats lead narrowly in Maine, Ohio and Texas and comfortably in North Carolina; Iowa and Alaska are dead heats; and Kansas has tipped to the Democrat."),
("Orchard Park: Assembly, Burke (D, inc.) vs Dickson (R); Gallivan (R) unopposed for State Senate.","Orchard Park: Assembly, Burke (D, inc.) vs Dickson (R), and DiPietro (R, inc.) unopposed; Gallivan (R, inc.) unopposed for State Senate."),
('<div class="line"><b>Where to vote early, today only, 9 to 5.</b>','<div class="line"><b>County and town.</b> North Tonawanda\'s county legislature seats: Gooch (R, inc.) vs Mooradian (D), Andres (R, inc.) vs Kennedy (D), Bradt (R, inc.) vs Osborn (D). Dunkirk: Legislature District 1, Buchanan (D, inc.) vs Garza (R); Family Court, Sullivan (R, inc.) vs Moss (D); Sheriff Quattrone (R) unopposed. Fredonia: Scudder (R, inc.) vs Lee (D). Scottsville: DA Green (D) and Supervisor Kirch (R) unopposed.</div>\n<div class="line"><b>Where to vote early, today only, 9 to 5.</b>'),
('<div class="line"><span class="lbl r">Standard time</span> Sunrise jumps back an hour to 6:50, and darkness now arrives before supper.</div>\n',''),
("<i>SNL</i> also aired a clip of Patrick Stewart's 1994 episode in tribute.","<i>SNL</i> closed with a clip from Patrick Stewart's 1994 episode, in tribute to Stewart, who died this week at 86."),
("The rest may take longer, Binance told the BBC;","The rest may take longer, Binance says, the BBC reports;"),
("the ceasefire runs through this evening.","the ceasefire is expected to last through this evening."),
("A federal judge in Miami threw out President Trump's","A federal judge in Miami threw out, for the second time, President Trump's"),
("after two straight days of clean tests, the county health department says, WIVB reports.","after two straight days of clean tests, the Chautauqua County Health Department told WIVB.")]
for a,c in F:
  assert b.count(a)==1,a[:60]; b=b.replace(a,c)
e['body_html']=b
for p in P: json.dump(e,open(p,'w'),ensure_ascii=False,indent=1)
print('fixed')
