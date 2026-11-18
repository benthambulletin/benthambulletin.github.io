import json
p='/home/claude/site/data/edition-2026-11-18.json'; e=json.load(open(p)); s=e['body_html']
def R(a,b):
    global s
    assert s.count(a)==1,a[:50]; s=s.replace(a,b)
R("The site's point: that is enough","Gang Green Nation's point: that is enough")
R('Two wheels, one chain, no engine. I only stay upright while I am going somewhere. What am I?','I have teeth but never chew, and every fall I gather a crowd that will not stay put. What am I?')
R('<b>Question of the Day:</b> A bicycle.','<b>Question of the Day:</b> A rake.')
R('One day left before the first sheet locks: Colts at Texans, Thursday at 8:15. Picks at','Week 11 is open. Sheets lock at each kickoff; the first is Colts at Texans, Thursday at 8:15 p.m. Picks at')
R('Jamestown &middot; Natalie Merchant Rides in the Macy\'s Parade','Chautauqua County &middot; Natalie Merchant Rides in the Macy\'s Parade')
R('From 10 to 4 it is above 50 and sunny, warmest about 1. A good day to try a new trail.','From 10 to 4 it is above 50 and sunny, warmest about 1.')
R("That was the television audience for Sunday's game, ProFootballTalk reports.","An average of 27.13 million people watched Sunday's game, ProFootballTalk reports.")
R('<div class="cap">People who watched 49ers&ndash;Cowboys</div>','<div class="cap">Average audience for 49ers&ndash;Cowboys</div>')
R('The pressure is off. Do one thing slowly','The heat is off. Do one thing slowly')
e['body_html']=s
for q in [p,'/home/claude/edition-2026-11-18.json']: json.dump(e,open(q,'w'),ensure_ascii=False,indent=1)
