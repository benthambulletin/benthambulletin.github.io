import json,re
P=['/home/claude/edition-2026-10-31.json','/home/claude/site/data/edition-2026-10-31.json']
e=json.load(open(P[1]));b=e['body_html']
F=[('<div class="ledger"><div class="num"><div class="cap">Rise in U.S. energy prices over the past year</div><div class="big">20.4%</div></div>\n<div class="txt">The September price index, WKBW reports. New York\'s heating-aid program, HEAP, opens for applications Monday, Nov. 2.</div></div>',
 '<div class="ledger"><div class="num"><div class="cap">What National Fuel expects a typical home to spend on heat this winter</div><div class="big">$742</div></div>\n<div class="txt">Nearly 5 percent less than last winter, WKBW reports. New York\'s heating-aid program, HEAP, opens for applications Monday, Nov. 2.</div></div>'),
("Once a year, strangers in disguise ring your bell, and you pay them to go away. What night is it?","What room does a ghost never go into?"),
("<b>Question of the Day:</b> Halloween. Happy trick-or-treating.","<b>Question of the Day:</b> The living room. Happy Halloween."),
("<b>Bills</b> &middot; Buffalo's own Goo Goo Dolls will play the Bills' Thanksgiving halftime show, WIVB reports. First comes Baltimore, Sunday at 1:00 on standard time.","<b>Bills</b> &middot; At 5&ndash;1 and atop the AFC East, Buffalo hosts Baltimore Sunday at 1:00, on standard time. Buffalo's own Goo Goo Dolls will play the Bills' Thanksgiving halftime show, WIVB reports."),
("Chief Douglas Swizer says parents need to be involved, and police are now charging some of them, WIVB reports.","Chief Douglas Swizer says parents need to be involved, and police have charged several parents with endangering the welfare of a child for failing to control them."),
("Bring the porch light on early","Turn the porch light on early"),
("<span>Halloween &middot; clocks fall back tonight</span>","<span>Halloween</span>")]
for a,c in F:
  assert b.count(a)==1,a[:60]; b=b.replace(a,c)
# reorder home wire: Rochester, Dunkirk, North Tonawanda
i=b.find('<h2 class="sec"><span class="o">&#9962;</span>The Home Wire');i=b.find('<div class="wire">',i);j=b.find('<h2 class="sec"><span class="o">&#9733;</span>The Marquee')
items=re.findall(r'<div class="wire">.*?</p></div></div>\n',b[i:j],re.S); assert len(items)==3
nt,dk,roc=items
fix=lambda s,n: re.sub(r'<div class="num">\d</div>',f'<div class="num">{n}</div>',s)
b=b[:i]+fix(roc,1)+fix(dk,2)+fix(nt,3)+b[j:]
e['body_html']=b
for p in P: json.dump(e,open(p,'w'),ensure_ascii=False,indent=1)
print('fixed')
