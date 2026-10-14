import json,hashlib
v=hashlib.md5(open('site/2026/10/14/kaylani.jpg','rb').read()).hexdigest()[:8]
d=json.load(open('site/data/edition-2026-10-14.json')); b=d['body_html']
o='please do not answer with your vehicle.</div>'
assert b.count(o)==1
b=b.replace(o,'please do not answer with your vehicle.<img src="/2026/10/14/kaylani.jpg?v='+v+'" alt="A gray SUV parked inside a grocery store entrance among shattered glass and a bent door frame" style="display:block;width:100%;height:auto;margin-top:.7rem;border:1px solid var(--rule)"><span style="display:block;font-family:\'LOI\';font-style:italic;font-size:.8rem;color:var(--soft);margin-top:.3rem">Photo sent by Kaylani</span></div>')
d['body_html']=b
for p in ['edition-2026-10-14.json','site/data/edition-2026-10-14.json']:
    json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('ok')
# --- review fixes ---
d=json.load(open('site/data/edition-2026-10-14.json')); b=d['body_html']
for o,n in [('>Photo sent by Kaylani<','>Rosenberg Police Department photo, sent by Kaylani<'),
            ("Kaylani sent in today's strangest news story; it's just below.","Kaylani sent in a strange one from Texas; it's just below."),
            ('alt="A gray SUV parked inside a grocery store entrance among','alt="A gray compact SUV inside a Kroger entrance among')]:
    assert b.count(o)==1,o; b=b.replace(o,n)
d['body_html']=b
for p in ['edition-2026-10-14.json','site/data/edition-2026-10-14.json']:
    json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
