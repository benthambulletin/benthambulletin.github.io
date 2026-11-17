import json
p='/home/claude/site/data/edition-2026-11-17.json'; e=json.load(open(p)); s=e['body_html']
def R(a,b,n=1):
    global s
    assert s.count(a)==n,(a[:50],s.count(a)); s=s.replace(a,b)
i=s.index("<p>Oprah Winfrey has put out her annual Favorite Things list"); j=s.index('</p>',i)+4
s=s[:i]+"<p>Oprah Winfrey has put out her Favorite Things list, the holiday gift guide she started on her talk show in 1996, the Hollywood Reporter says. It began by accident, the magazine recounts, when a producer gave her a pair of pajamas she liked so much that she gave a pair to everyone in her studio audience.</p>"+s[j:]
R('Not announced: the number of floors, the opening date,','Not announced: the number of floors, the exact opening date,')
R('Andy Masley, an independent researcher, told the Times that whether the emissions','Andy Masley, an independent researcher, says whether the emissions')
R('in 40 of 41 local ballot measures this month.</p>','in 40 of 41 local ballot measures this month, the Times reports.</p>')
R('by itself, half a percent of the country\'s emissions','by itself, about half a percent of the country\'s emissions')
R('Service was back to normal early Tuesday; Chase said','The tracker showed service back to normal early Tuesday; Chase said')
R('hand it to Benderson Development for a project that includes housing','hand it back to Benderson Development for a mixed-use project that includes housing')
R('It gets breezy, with gusts possible to 20 mph.','A southwest breeze builds to as much as 20 mph.')
R('highest in the south around 9.','highest in the south in mid-evening.')
# space between the Wayfair item's paragraphs
for a in ('<p>What will be inside:','<p>Amherst\'s store is about two-thirds','<p>Against IKEA:'):
    R(a,a.replace('<p>','<p style="margin-top:.7em">'))
e['body_html']=s
for q in [p,'/home/claude/edition-2026-11-17.json']: json.dump(e,open(q,'w'),ensure_ascii=False,indent=1)
