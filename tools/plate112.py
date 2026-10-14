import json
d=json.load(open('site/data/edition-2026-10-14.json'))
b=d['body_html']
anchor='<div class="dbl-tight"><div class="a"></div><div class="b"></div></div>\n<h2 class="sec"><span class="o">&#9825;</span>Family Today<span class="o">&#9825;</span></h2>\n<div class="fam">'
assert b.count(anchor)==1
cap="Luka at the plate"
plate='<div class="plate-wrap"><div class="frame"><span class="tick tl"></span><span class="tick tr"></span><span class="tick bl"></span><span class="tick br"></span>\n<img src="__PLATE__" alt="Luka, barefoot on the patio, swings an orange plastic bat at a tee in the backyard"></div>\n<div class="plate-cap">Plate I &middot; The Family Album</div>\n<div class="plate-sub">'+cap+'</div></div>\n'
b=b.replace(anchor,plate+anchor+'<b>Luka has the cover.</b> ')
d['body_html']=b; d['plate_path']='/home/claude/plate112.jpg'; d['plate_caption']=cap
for p in ['edition-2026-10-14.json','site/data/edition-2026-10-14.json']:
    json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('ok')
# --- review polish ---
d=json.load(open('site/data/edition-2026-10-14.json')); b=d['body_html']
for o,n in [('alt="Luka, barefoot on the patio, swings an orange plastic bat at a tee in the backyard"','alt="Luka, barefoot on the patio in striped pajama pants, swings an orange plastic bat beside a red batting tee topped with a green frog ball"'),
            ('<b>Luka has the cover.</b> <b>Three days to the party.</b>','<b>Luka has the cover</b>, barefoot at the tee. <b>Three days to the party.</b>')]:
    assert b.count(o)==1,o; b=b.replace(o,n)
d['body_html']=b; d['headline']="Pope has lung cancer · Big pressure drop Thu night · Kaylani in the Group Chat · Phoenix next"
for p in ['edition-2026-10-14.json','site/data/edition-2026-10-14.json']:
    json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
