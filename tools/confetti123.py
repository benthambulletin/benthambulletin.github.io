import json, random
random.seed(1025)
cols=['#9c3216','#cf6f1a','#2f5e3e','#e8b100','#c8302f','#0e8a8a','#7a4fa0']
parts=[]
for i in range(60):
    x=random.uniform(10,590); dur=random.uniform(3.5,7.5); beg=-random.uniform(0,7.5)
    c=random.choice(cols); w=random.uniform(5,10); h=random.uniform(9,16); rot=random.choice([360,-360,720,-720])
    sway=random.uniform(-25,25)
    shape=(f'<rect x="{-w/2:.1f}" y="{-h/2:.1f}" width="{w:.1f}" height="{h:.1f}" rx="1.5" fill="{c}"/>' if i%3 else f'<circle r="{w/2+1:.1f}" fill="{c}"/>')
    parts.append(f'<g><animateTransform attributeName="transform" type="translate" values="{x:.0f},-20; {x+sway:.0f},150; {x:.0f},320" dur="{dur:.2f}s" begin="{beg:.2f}s" repeatCount="indefinite"/>'
                 f'<g>{shape}<animateTransform attributeName="transform" type="rotate" from="0" to="{rot}" dur="{dur/2:.2f}s" begin="{beg:.2f}s" repeatCount="indefinite"/></g></g>')
svg=('<svg viewBox="0 0 600 300" role="img" aria-label="Confetti falling around the words Happy Birthday, Garret and Ariel" xmlns="http://www.w3.org/2000/svg" style="display:block;width:100%;height:auto;background:#fbf5e4">'
     + ''.join(parts) +
     '<text x="300" y="138" text-anchor="middle" font-family="PFI, Georgia, serif" font-style="italic" font-size="30" fill="#9c3216">Happy Birthday</text>'
     '<text x="300" y="188" text-anchor="middle" font-family="PF, Georgia, serif" font-weight="800" font-size="46" fill="#24170c">Garret &amp; Ariel</text>'
     '</svg>')
d=json.load(open('edition-2026-10-25.json')); b=d['body_html']
i=b.index('<div class="plate-wrap">'); j=b.index('<div class="dbl-tight"><div class="a"></div><div class="b"></div></div>\n<h2 class="sec"><span class="o">&#9825;</span>Family Today',i)
block=('<div class="plate-wrap"><div class="frame"><span class="tick tl"></span><span class="tick tr"></span><span class="tick bl"></span><span class="tick br"></span>\n'
       + svg + '</div>\n<div class="plate-cap">Plate I &middot; The Family Album</div>\n<div class="plate-sub">Happy birthday, Garret and Ariel</div></div>\n')
b=b[:i]+block+b[j:]
b=b.replace("cover photo by Isabella Fischer on Unsplash &middot; ","")
assert 'Unsplash' not in b
d['body_html']=b; d['plate_path']=None; d['plate_caption']=None
for p in ['edition-2026-10-25.json','site/data/edition-2026-10-25.json']: json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('confetti in')
