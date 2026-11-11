"""No. 140 review fixes (pre-publish)."""
import json
P='/home/claude/site/data/edition-2026-11-11.json'
e=json.load(open(P)); b=e['body_html']
def R(o,n,c=1):
    global b; assert b.count(o)==c,(o[:50],b.count(o)); b=b.replace(o,n)
R('off Buffalo, Wednesday','off Buffalo, Tuesday'); R('off Rochester, Wednesday','off Rochester, Tuesday')
R('<h3>The First Freeze, at Last</h3>','<h3>A First 32 at Dawn</h3>')
R('<p>Dunkirk and Scottsville got there three weeks ago, with 28 at Dunkirk and 32 at the Rochester airport on Oct. 21. Both stood at 36 this morning, which is the normal low for Nov. 11.</p>',
  '<p>Dunkirk and Scottsville had dawn readings that cold three weeks ago, 28 at Dunkirk and 32 at the Rochester airport on Oct. 21. Both stood at 36 this morning, about the normal low for the date at Buffalo and Rochester.</p>')
R('<p>Late, but not the latest. In 2017 Buffalo and Rochester both waited until Nov. 8 for a first freeze, the Northeast Regional Climate Center at Cornell says, giving Rochester its second-longest frost-free season in records back to 1872 and Buffalo its fifth-longest since 1874.</p>',
  '<p>Late, but it has run later. In 2017 Buffalo and Rochester each went 212 days, from Apr. 8 to Nov. 7, without a freeze, the Northeast Regional Climate Center at Cornell says. That was Rochester\'s second-longest frost-free season in records back to 1872 and Buffalo\'s fifth-longest since 1874.</p>')
R(' The Cisco deal was the team\'s only move.',' The Jets made no trades on deadline day.')
R('A freezing, clear dawn, then clouds; rain by late evening','A freezing, clear dawn, then clouds; showers possible after 7, rain overnight')
R('<div class="v">After 7</div><div class="s">p.m., 90%</div>','<div class="v">90%</div><div class="s">overnight</div>')
R(' It costs $5, you pick the winners straight up, the best record takes the pot, and each game locks at its kickoff.',
  ' $5 a week, straight-up winners, the pot to the best record; anyone with the link can play. Sheets lock at each kickoff; first game Thursday at 8:15, Commanders at Giants.')
R('<div>Commanders at Giants, 8:15; Sunday Tax sheets start locking</div>','<div>Sunday Tax sheets start locking, 8:15</div>')
R('Hooker, 28 and in his eighth season,','Hooker, in his eighth season,')
R(' Buffalo Rumblings,','')
R('and I start growing again four days before Christmas.','and I don\'t start growing again until a few days before Christmas.')
e['body_html']=b; e['headline']='A first 32 at dawn · Bills trade for a safety · Stacy Keach dies at 85'
json.dump(e,open(P,'w'),indent=1); json.dump(e,open('/home/claude/edition-2026-11-11.json','w'),indent=1)
