import json
d=json.load(open('site/data/edition-2026-10-16.json')); b=d['body_html']
anchor='<div class="dbl-tight"><div class="a"></div><div class="b"></div></div>\n<h2 class="sec"><span class="o">&#9825;</span>Family Today<span class="o">&#9825;</span></h2>\n<div class="fam">'
assert b.count(anchor)==1
cap="Dressed for today's weather, Maid of the Mist style"
plate='<div class="plate-wrap"><div class="frame"><span class="tick tl"></span><span class="tick tr"></span><span class="tick bl"></span><span class="tick br"></span>\n<img src="__PLATE__" alt="A group selfie of the family in blue Maid of the Mist rain ponchos and sunglasses"></div>\n<div class="plate-cap">Plate I &middot; The Family Album</div>\n<div class="plate-sub">'+cap+'</div></div>\n'
b=b.replace(anchor,plate+anchor+'<b>Rain today, so the cover breaks out the ponchos.</b> ')
d['body_html']=b; d['plate_path']='/home/claude/plate114.jpg'; d['plate_caption']=cap
for p in ['edition-2026-10-16.json','site/data/edition-2026-10-16.json']:
    json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('ok')
# --- review fixes: recrop (0,40,1189,1040); caption "Rain gear, Maid of the Mist style" ---
