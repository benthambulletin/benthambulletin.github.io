import json
d=json.load(open('site/data/edition-2026-10-13.json'))
b=d['body_html']
anchor='<div class="dbl-tight"><div class="a"></div><div class="b"></div></div>\n<h2 class="sec"><span class="o">&#9825;</span>Family Today<span class="o">&#9825;</span></h2>\n<div class="fam">'
assert b.count(anchor)==1
cap="Luka, one arm stacked with rolls of masking tape"
plate='<div class="plate-wrap"><div class="frame"><span class="tick tl"></span><span class="tick tr"></span><span class="tick bl"></span><span class="tick br"></span>\n<img src="__PLATE__" alt="Luka in dinosaur pajamas, rolls of masking tape stacked up his arm"></div>\n<div class="plate-cap">Plate I &middot; The Family Album</div>\n<div class="plate-sub">'+cap+'</div></div>\n'
new=plate+anchor+'<b>Luka has the cover</b>, his arm stacked with rolls of masking tape. '
b=b.replace(anchor,new)
d['body_html']=b; d['plate_path']='/home/claude/plate111.jpg'; d['plate_caption']=cap
for p in ['edition-2026-10-13.json','site/data/edition-2026-10-13.json']:
    json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('ok')
# --- review fixes ---
d=json.load(open('site/data/edition-2026-10-13.json')); b=d['body_html']
def R(o,n):
    global b; assert b.count(o)==1,o; b=b.replace(o,n)
R('alt="Luka in dinosaur pajamas, rolls','alt="Luka in a dinosaur shirt, rolls')
R('<b>Luka has the cover</b>, his arm stacked with rolls of masking tape. ','<b>Luka has the cover</b>, armed with masking tape. ')
R('<div class="plate-sub">Luka, one arm stacked with rolls of masking tape</div>','<div class="plate-sub">Luka, armed with masking tape</div>')
d['body_html']=b; d['plate_caption']='Luka, armed with masking tape'
for p in ['edition-2026-10-13.json','site/data/edition-2026-10-13.json']:
    json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('fixed')
d=json.load(open('site/data/edition-2026-10-13.json')); b=d['body_html']
R('<b>Luka has the cover</b>, armed with masking tape. ','<b>Luka has the cover.</b> ')
d['body_html']=b
for p in ['edition-2026-10-13.json','site/data/edition-2026-10-13.json']:
    json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
