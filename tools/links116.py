import json
d=json.load(open('site/data/edition-2026-10-18.json')); b=d['body_html']
o='Send it at tally.so/r/rjxDpl this week.'
assert o in b
b=b.replace(o,'Send it at <a href="https://tally.so/r/rjxDpl">tally.so/r/rjxDpl</a> this week.')
d['body_html']=b
for p in ['edition-2026-10-18.json','site/data/edition-2026-10-18.json']: json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('ok')
