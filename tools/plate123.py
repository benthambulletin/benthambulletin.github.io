import json
d=json.load(open('edition-2026-10-25.json')); b=d['body_html']
def R(a,c):
    global b
    assert a in b, a[:70]; b=b.replace(a,c)
R('<div class="dbl-tight"><div class="a"></div><div class="b"></div></div>\n<h2 class="sec"><span class="o">&#9825;</span>Family Today','<div class="plate-wrap"><div class="frame"><span class="tick tl"></span><span class="tick tr"></span><span class="tick bl"></span><span class="tick br"></span>\n<img src="__PLATE__" alt="A hand holds out a cupcake with purple frosting, sprinkles and one striped birthday candle"></div>\n<div class="plate-cap">Plate I &middot; The Family Album</div>\n<div class="plate-sub">Happy birthday, Garret and Ariel &middot; photo by Isabella Fischer on Unsplash</div></div>\n<div class="dbl-tight"><div class="a"></div><div class="b"></div></div>\n<h2 class="sec"><span class="o">&#9825;</span>Family Today')
R("Safe travels to Garret, still on Long Island and heading home tomorrow;","Safe travels to Garret and the whole family, heading home from Long Island tomorrow;")
R('<span class="dt">Oct 26</span><span>Hunter&rsquo;s Moon &middot; Garret home</span>','<span class="dt">Oct 26</span><span>Hunter&rsquo;s Moon &middot; the family home from Long Island</span>')
R("<span class=\"lbl t\">Away</span> Garret on Long Island:","<span class=\"lbl t\">Away</span> The family on Long Island:")
R("<b>Family.</b> Garret home from Long Island Monday.","<b>Family.</b> Everyone home from Long Island Monday.")
R("headlines via BBC,","cover photo by Isabella Fischer on Unsplash &middot; headlines via BBC,")
d['body_html']=b; d['plate_path']='/home/claude/plate123.jpg'; d['plate_caption']='Happy birthday, Garret and Ariel'
json.dump(d,open('edition-2026-10-25.json','w'),ensure_ascii=False,indent=1)
json.dump(d,open('site/data/edition-2026-10-25.json','w'),ensure_ascii=False,indent=1)
print('plated')
