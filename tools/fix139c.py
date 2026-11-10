"""No. 139 relayout, review fixes (Nov 10, second review)."""
import json,re
P='/home/claude/site/data/edition-2026-11-10.json'
e=json.load(open(P)); b=e['body_html']
def R(o,n):
    global b; assert b.count(o)==1,o; b=b.replace(o,n)
m=re.search(r'<div class="pull">[^<]*</div>\n?',b); assert m and 'Thanksgiving holidays' in m.group(0); b=b.replace(m.group(0),'')
R('<h3>Jets Deal at the Deadline</h3>','<h3>Jets Make a Deadline-Week Trade</h3>')
R(' Sunday they host the Bills at 1:00.</p>','</p>')
e['body_html']=b
json.dump(e,open(P,'w'),indent=1); json.dump(e,open('/home/claude/edition-2026-11-10.json','w'),indent=1)
