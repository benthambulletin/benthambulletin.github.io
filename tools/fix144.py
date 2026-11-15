import json
p='/home/claude/site/data/edition-2026-11-15.json'; e=json.load(open(p)); s=e['body_html']
def R(a,b):
    global s
    assert s.count(a)==1,a[:50]; s=s.replace(a,b)
R('For a gas-heated house, this winter should cost about what last winter did, and the weather will matter more than the rates. A cold January moves a bill far more than $9.',
  'One catch for this family: National Grid sells gas mainly in central and eastern New York. In most of Western New York the gas comes from National Fuel, and around Rochester from RG&amp;E, so the $9 figure shows which way gas bills are heading, not what a house here will pay. The electric forecast is the one that applies where National Grid delivers the power: plan on $22 to $39 more over the winter. Either way, the weather will matter more than the rates.')
R('<b>Why gas barely moves.</b>','<b>Why the bill has two parts.</b>')
R('The price of gas itself is down, but delivery charges are up under a three-year rate plan the state approved in August 2025, which pays for new equipment and for replacing about 112 miles of leak-prone gas pipe, FingerLakes1 reports. One eats most of the other.',
  'Delivery charges are rising under a three-year rate plan the state approved in August 2025, which includes replacing about 112 miles of leak-prone gas pipe, FingerLakes1 reports. Even so, the company expects the typical gas bill to come in slightly lower.')
R('last February they said the electricity they buy for customers cost 36 to 44 percent more than a year before, so','last February they said supply prices, the cost of the energy itself, were up more than 44 percent for NYSEG customers and nearly 36 percent for RG&amp;E customers from a year before, so')
R('Wilson High School beat St. Lawrence in a state semifinal Saturday in Moravia and will play for a state championship, the <i>Lockport Journal</i> reports. Abigail Labarre scored the goal that let coach Jeff Hart start emptying his bench.',
  'Wilson High School pulled away in the second half to beat St. Lawrence in a state semifinal Saturday in Moravia and earn a place in the state championship game, the <i>Lockport Journal</i> reports. Abigail Labarre\'s goal put it out of reach, and coach Jeff Hart began sending in his bench.')
R('<div class="cap">Days to Christmas</div><div class="big">40</div>','<div class="cap">Days to New Year\'s Day</div><div class="big">47</div>')
R('Counting from this morning. That is six Sundays, including this one.','Counting from this morning. The year has 46 days left in it after today.')
R('Cancellations carried into Saturday as airlines cleared the backlog.','The disruption carried into Saturday as airlines worked through the backlog.')
R('cried at a long ovation','cried at a huge ovation')
R('Oprah Winfrey inducted the late Luther Vandross, Oasis, Sade and Queen Latifah went in too, and U2 opened','Oprah Winfrey inducted the late Luther Vandross; Oasis, Sade and Queen Latifah went in too; and U2 opened')
R('Dry after the early sprinkle and stuck at 43 from late morning through dusk.','Dry after the early sprinkle and holding in the low to mid 40s from late morning through dusk.')
R('To make room, they released Te\'Cory Couch.','They also released Te\'Cory Couch.')
R('Last week: a slide from 60 on Tuesday to 41 on Friday, with the coldest dawn 32 on Wednesday. This week climbs back: 49 Monday, then sunny and 54 to 57 Tuesday through Thursday.','Last week: forecast highs slid from 60 on Tuesday to 41 on Friday, with the coldest dawn 32 on Wednesday. This week climbs back: 49 Monday, then sun and 54 to 57 Tuesday through Thursday.')
R('so delivery charges are set to keep rising after this winter.','so delivery charges are likely to keep climbing after this winter.')
R('The moon sits across from you. Someone else','The moon is on the far side of the sky from you. Someone else')
R('Read the message twice before answering it.','Count to five before you hit send.')
R('<b>Games.</b> Bills at the Jets today at 1:00;','<b>Games.</b> Bills at the Jets this afternoon;')
R('Dolphins at Bills, 1:00; Jets at Chargers, 4:05','Dolphins at Bills, 1:00; Jets at Chargers')
e['body_html']=s
for q in [p,'/home/claude/edition-2026-11-15.json']: json.dump(e,open(q,'w'),ensure_ascii=False,indent=1)
print('fixed')
