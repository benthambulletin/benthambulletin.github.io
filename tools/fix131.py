import json
P=['/home/claude/edition-2026-11-02.json','/home/claude/site/data/edition-2026-11-02.json']
e=json.load(open(P[1]));b=e['body_html']
def R(a,c):
    global b
    assert b.count(a)==1,a[:50]; b=b.replace(a,c)
R('<h3>Jamestown &middot; Jayhawks to Nationals</h3><p>Jamestown Community College\'s women\'s soccer team beat fifth-ranked Mohawk Valley 2&ndash;1 in Batavia Saturday to win the Region 3 title, the <i>Observer</i> reports. The win sends the Jayhawks to the national junior-college tournament.</p>',
  '<h3>Dunkirk &middot; A Lung Doctor at Brooks-TLC</h3><p>Brooks-TLC Hospital System has added Dr. Mandeep Sidhu, a specialist in lung disease and critical care, to treat breathing problems for patients across Chautauqua County, the <i>Observer</i> reports. Her work runs from complex lung conditions and long-term breathing illnesses to the sickest patients, who need machines to help them breathe.</p>')
R('rises at 12:43 a.m., sets at 2:01 p.m.','sets at 2:01 p.m. and rises again at 12:43 a.m. tonight')
R('Mars and Jupiter rise near midnight, with the moon right beside them by 1 a.m.','Mars and Jupiter rise near midnight, and the crescent moon follows them up at 12:43 a.m., not far below Jupiter.')
R('A slight chance of a shower, then partly sunny and 71 in North Tonawanda; 24 percent chance of rain.','A slight chance of a shower between 7 and 10 a.m., then partly sunny and 71 in North Tonawanda; 20 percent chance of rain.')
R('picked the act for the second straight year.','picked the act; it\'s the second year the two have chosen the Lions\' Thanksgiving performer.')
R('and his office expects a full recovery.','and his office says it is optimistic he will make a full recovery.')
R('Detroit beat Minnesota 19&ndash;15, so no team is unbeaten.','Detroit handed Minnesota its first loss, 19&ndash;15, so no team is unbeaten.')
R('Geno Smith threw for 290 yards and touchdowns to I. Williams and A. Mitchell, B. Allen ran 21 yards for another, and Sanders made all four field goals.','Geno Smith threw for 290 yards and two touchdowns, the Jets ran 21 yards for a third, and Sanders made all four field goals.')
R('and secret until the day I\'m tallied.','and secret even after I\'m tallied.')
R('and last won a state title, in a lower class, in 2023.','and won a lower-class state title in 2023.')
R('Low <b>52&deg;</b> tonight &middot; light southwest wind','Low <b>52&deg;</b> tonight &middot; light south wind')
R("skewers Korea's cosmetic skin-care business","skewers Korea's cosmetic skin-clinic business")
R('the Dunkirk Observer','the Dunkirk <i>Observer</i>') if 'the Dunkirk Observer' in b else None
e['body_html']=b
for p in P: json.dump(e,open(p,'w'),ensure_ascii=False,indent=1)
print('ok')
