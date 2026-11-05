import json
P=['/home/claude/edition-2026-11-05.json','/home/claude/site/data/edition-2026-11-05.json']
e=json.load(open(P[1]));b=e['body_html']
def R(a,c):
    global b
    assert b.count(a)==1,a[:60]; b=b.replace(a,c)
# Rochester item first, drop Fredonia
i=b.find('<div class="wire"><div class="num">3</div><div><h3>Fredonia'); j=b.find('<h2',i); assert i>0
b=b[:i]+b[j:]
R('<div class="wire"><div class="num">2</div><div><h3>Dunkirk','<div class="wire"><div class="num">3</div><div><h3>Dunkirk')
R('<div class="wire"><div class="num">1</div><div><h3>North Tonawanda','''<div class="wire"><div class="num">1</div><div><h3>Rochester &middot; RTS On Demand Is Ending</h3><p>The Regional Transit Service will end RTS On Demand, its rideshare-style service, in 2027 because of money trouble, Rochester First reports; "Expenses are rising much faster than our revenues," CEO Miguel Vel&aacute;zquez said. RTS plans to rework service in those areas instead, including expanding some fixed bus routes, WXXI reports.</p></div></div>
<div class="wire"><div class="num">2</div><div><h3>North Tonawanda''')
R('State Sen. Borrello and Assemblyman Molitor, both Republicans, were re-elected even as Democrats gained seats in Albany, the <i>Observer</i> reports. Rep. Nick Langworthy beat Aaron Gies of Olean 59 to 39 percent and carried every county in the district.',
  'State Sen. George Borrello won another term, 68 to 30 percent over Victoria Guite-Williams, and Assemblyman Andrew Molitor beat Thomas Carle 26,485 votes to 15,490, the <i>Observer</i> reports; both Republicans held on while Democrats flipped at least a dozen seats in Albany. Rep. Nick Langworthy\'s final margin over Aaron Gies of Olean was 59 to 39 percent, and he carried every county in the district.')
R('led Republican Sen. Cindy Hyde-Smith by just over 1,100 votes early Thursday with about 96 percent counted, CBS reports. A Democratic win in a state this Republican would be a stunning result; at one point Wednesday only a few dozen votes separated them.',
  'led Republican Sen. Cindy Hyde-Smith by just over 1,100 votes early Thursday, CBS reports. On Wednesday morning, with about 96 percent counted, only a few dozen votes separated them, a stunningly close race in a state as Republican as Mississippi, CBS says.')
R('The warm spell is over: a windy 64 today, and rain most of the way to Sunday.','The record warmth is behind us, but not the mild: a windy 64 today, then rain most of the way to Sunday and cooler air behind it.')
R('<h3>Meryl Streep Is the New Aslan</h3>','<h3>Neeson Hands Aslan to Streep</h3>')
R('Deadline reports. The film opens in theaters Feb. 12.','Deadline reports, though he told an interviewer the new film was "news to me," Variety adds. It opens in theaters Feb. 12.')
R('Sportradar gives the Jaguars an 80 percent chance.','Sportradar gives the Jaguars an 82 percent chance.')
R('<b>The moon, in Virgo, trines Uranus</b>.','<b>The moon trines Uranus</b>.')
R('headlines via CBS, BBC, NPR, WIVB, WKBW,','headlines via CBS, BBC, NPR, WIVB, WKBW, Rochester First, WXXI,')
e['body_html']=b
for p in P: json.dump(e,open(p,'w'),ensure_ascii=False,indent=1)
print('ok')
