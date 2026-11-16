import json
p='/home/claude/site/data/edition-2026-11-16.json'; e=json.load(open(p)); s=e['body_html']
def R(a,b):
    global s
    assert s.count(a)==1,a[:50]; s=s.replace(a,b)
R('a Josh Allen sneak, a 45-yard pass','a 1-yard Josh Allen run, a 45-yard pass')
R("Allen's first touchdown was the 323rd of his career, passing Peyton Manning for the most by a quarterback in his first ten seasons, Buffalo Rumblings reports.","Allen's first touchdown was the 323rd of his career, running and passing combined, moving him past Peyton Manning for the most by a quarterback through his first 10 seasons, Buffalo Rumblings reports.")
R('in San Diego, one county benefits office has started handing out groceries on Saturdays.',"in San Diego, workers at one county benefits office spent Saturday morning loading groceries into people's cars.")
R("Olivia Dean, last year's best new artist,",'Olivia Dean, the reigning best new artist,')
R('He is credited with building the alliance between Colombian traffickers and Mexican cartels that changed how the drug trade works.','He is credited with building an alliance between Colombian traffickers and his own cartel, a way of doing business the BBC says endures to this day.')
R('Leave ten minutes early.','Leave a little early.')
e['body_html']=s
for q in [p,'/home/claude/edition-2026-11-16.json']: json.dump(e,open(q,'w'),ensure_ascii=False,indent=1)
