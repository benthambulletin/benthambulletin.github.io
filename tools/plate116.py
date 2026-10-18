import json
d=json.load(open('site/data/edition-2026-10-18.json')); b=d['body_html']
anchor='<div class="dbl-tight"><div class="a"></div><div class="b"></div></div>\n<h2 class="sec"><span class="o">&#9825;</span>Family Today<span class="o">&#9825;</span></h2>\n<div class="fam">'
assert b.count(anchor)==1
cap="A big hug from behind"
plate='<div class="plate-wrap"><div class="frame"><span class="tick tl"></span><span class="tick tr"></span><span class="tick bl"></span><span class="tick br"></span>\n<img src="__PLATE__" alt="A smiling girl in a flowered top hugs a small boy in a dark sweatshirt from behind, in a living room"></div>\n<div class="plate-cap">Plate I &middot; The Family Album</div>\n<div class="plate-sub">'+cap+'</div></div>\n'
b=b.replace(anchor,plate+anchor)
d['body_html']=b; d['plate_path']='/home/claude/plate116.jpg'; d['plate_caption']=cap
for p in ['edition-2026-10-18.json','site/data/edition-2026-10-18.json']: json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('ok')
# --- review fix: recrop (0,400,1932,1932) to keep the hug ---
