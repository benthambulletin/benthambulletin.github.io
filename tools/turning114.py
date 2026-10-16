import json
d=json.load(open('site/data/edition-2026-10-16.json')); b=d['body_html']
o='<div class="line"><b>Still waiting on the county numbers.</b> Gusts near 40 today could strip a good share of leaves either way; North Tonawanda usually peaks in the last week of October.</div>'
assert o in b
b=b.replace(o,'<div class="line"><b>The new numbers are in.</b> The state\'s spotters have Niagara Falls at 50 percent color and Lewiston at 10; Chautauqua Institution, near Dunkirk, at 70; and Greece, in Monroe County, at 30. Springville, south of Buffalo, leads the region at 90. Gusts near 40 today could strip a good share of what has turned.</div>')
o2='&middot; race time via NASCAR.com'; assert o2 in b
b=b.replace(o2,'&middot; foliage per the I LOVE NY report (via thisiscny.com) &middot; race time via NASCAR.com')
d['body_html']=b
for p in ['edition-2026-10-16.json','site/data/edition-2026-10-16.json']: json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('ok')
# --- review fixes ---
d=json.load(open('site/data/edition-2026-10-16.json')); b=d['body_html']
i=b.index('<b>The new numbers are in.</b>'); j=b.index('</div>',i)
b=b[:i]+'<b>The new numbers are in.</b> The state\'s spotters have Niagara Falls at 50 percent color and Lewiston at 10; Chautauqua Institution, in Chautauqua County, at 70; and Greece, in Monroe County, at 30. Springville, south of Buffalo, leads the Niagara region at 90, and Little Valley, in Cattaraugus County, has reached full color. North Tonawanda usually peaks in the last week of October. Gusts near 40 today may bring some of it down early.'+b[j:]
d['body_html']=b
for p in ['edition-2026-10-16.json','site/data/edition-2026-10-16.json']: json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
