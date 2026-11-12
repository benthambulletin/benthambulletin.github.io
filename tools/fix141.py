"""No. 141 review fixes (pre-publish)."""
import json
P='/home/claude/site/data/edition-2026-11-12.json'
e=json.load(open(P)); b=e['body_html']
def R(o,n):
    global b; assert b.count(o)==1,(o[:50],b.count(o)); b=b.replace(o,n)
R('<h3>Jets Add a Big Lineman</h3><p>The Jets signed defensive lineman Isaiahh Loudermilk, a 6-foot-7 former Steeler, to their practice squad, Gang Green Nation reports.</p>',
  '<h3>Jets: A Look at a Big Lineman</h3><p>Quiet at Jets camp. Gang Green Nation sizes up Isaiahh Loudermilk, the 6-foot-7 former Steeler who joined the practice squad last month.</p>')
R("I fall without getting hurt, I'm measured in inches, and I can close a school without saying a word. What am I?",
  "I open when the sky does and spend sunny days folded in a closet. The wind's favorite trick is turning me inside out. What am I?")
R('<b>Question of the Day:</b> Snow.','<b>Question of the Day:</b> An umbrella.')
R("That is ESPN's count across ABC, ESPN and its other channels, ProFootballTalk reports.","That is ESPN's count across ABC, ESPN, ESPN2, NFL Network and ESPN Deportes, ProFootballTalk reports.")
R('in a race that took more than a week to settle, CBS projects.','in a race that stayed up in the air for days, CBS projects.')
R("Four starting offensive linemen were limited in Wednesday's practice, the first of the week, though every Bill took part,","Four starting offensive linemen were listed as limited after Wednesday's walk-through, the first practice of the week, though every Bill took part,")
R('say they will develop it themselves.','say they will develop it themselves, as 88 senior apartments.')
e['body_html']=b
json.dump(e,open(P,'w'),indent=1); json.dump(e,open('/home/claude/edition-2026-11-12.json','w'),indent=1)
