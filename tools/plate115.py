import json
d=json.load(open('site/data/edition-2026-10-17.json')); b=d['body_html']
anchor='<div class="dbl-tight"><div class="a"></div><div class="b"></div></div>\n<h2 class="sec"><span class="o">&#9825;</span>Family Today<span class="o">&#9825;</span></h2>\n<div class="fam">'
assert b.count(anchor)==1
cap="Pines against a low October sun"
plate='<div class="plate-wrap"><div class="frame"><span class="tick tl"></span><span class="tick tr"></span><span class="tick bl"></span><span class="tick br"></span>\n<img src="__PLATE__" alt="Tall pines silhouetted against a low sun and heavy clouds over a wide lawn"></div>\n<div class="plate-cap">Plate I &middot; The Family Album</div>\n<div class="plate-sub">'+cap+'</div></div>\n'
b=b.replace(anchor,plate+anchor)
d['body_html']=b; d['plate_path']='/home/claude/plate115.jpg'; d['plate_caption']=cap
for p in ['edition-2026-10-17.json','site/data/edition-2026-10-17.json']:
    json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('ok')
# --- review fixes: gamma 0.56 overall; caption 'The pines under a heavy October sky'; alt without sun claim ---
# --- Garret 7:23: 'Its sunrise' → caption 'An October sunrise behind the pines', alt updated ---
