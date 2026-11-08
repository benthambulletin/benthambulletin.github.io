import json
p='/home/claude/edition-2026-11-08.json'; ed=json.load(open(p)); s=ed['body_html']
i=s.index('<div class="plate-wrap">'); j=s.index('<div class="dbl-tight">', i)
cap='Sunday hat, Sunday grin'
s=s[:i]+'''<div class="plate-wrap"><div class="frame"><span class="tick tl"></span><span class="tick tr"></span><span class="tick bl"></span><span class="tick br"></span>
<img src="__PLATE__" alt="A smiling little boy in a black ball cap and a navy sweatshirt"></div>
<div class="plate-cap">Plate I &middot; The Family Album</div>
<div class="plate-sub">'''+cap+'''</div></div>
'''+s[j:]
ed.update(body_html=s, plate_path='/home/claude/plate137.jpg', plate_caption=cap)
for q in [p,'/home/claude/site/data/edition-2026-11-08.json']: json.dump(ed,open(q,'w'),ensure_ascii=False,indent=1)
print('ok')
