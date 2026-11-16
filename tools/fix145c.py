import json
p='/home/claude/site/data/edition-2026-11-16.json'; e=json.load(open(p)); s=e['body_html']
def R(a,b):
    global s
    assert s.count(a)==1,a[:50]; s=s.replace(a,b)
R('Grammy Nominations This Morning','Raye Leads the Grammy Nominations')
i=s.index('<p>The nominees for the 2027 Grammy Awards are being announced'); j=s.index('</p>',i)+4
s=s[:i]+"<p>The nominees for the 2027 Grammy Awards were announced this morning, and the English singer Raye leads with 11, PBS reports. That ties Beyonc&eacute;'s record for the most nominations by a woman in one year, and it includes record, song and album of the year, her first time up for the big three.</p>"+s[j:]
R('Billboard, E! News','PBS, E! News')
e['body_html']=s
for q in [p,'/home/claude/edition-2026-11-16.json']: json.dump(e,open(q,'w'),ensure_ascii=False,indent=1)
