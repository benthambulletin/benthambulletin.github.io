import json
d=json.load(open('site/data/edition-2026-10-18.json')); b=d['body_html']
def R(o,n):
    global b
    assert b.count(o)==1,o[:80]; b=b.replace(o,n)
R("Early voting opens; last day to register","Early voting opens")
R("Saturday, Oct 24, is both the first day of early voting and the last day to register; early voting runs through Nov 1, and polls","Early voting opens Saturday, Oct 24, and runs through Nov 1, and polls")
R("Early voting Oct 24&ndash;Nov 1 &middot; register by Oct 24 &middot; Election Day","Early voting Oct 24&ndash;Nov 1 &middot; Election Day")
R("Saturday: early voting opens and registration closes.","Saturday: early voting opens, and runs through Nov 1.")
R("No public poll; the district leans Republican.","No public poll.")
R("No public poll; the district leans Democratic.","No public poll.")
R("here is everything else our three towns will see","here is everything else our five towns will see")
R("<b>2. The judges (North Tonawanda and Dunkirk).</b>","<b>2. The judges (North Tonawanda, Orchard Park, Dunkirk and Fredonia).</b>")
R("Blakeman leads upstate, where all three of our towns are.","Blakeman leads upstate, where all five of our towns are.")
R("<b>The yes-or-no question:</b> whether the city should borrow up to $18 million for a community center at the Keller Building to replace the old youth and senior centers. It would be paid with a special property tax of about 84 cents per $1,000 of assessed value before any grants; on a house assessed at $150,000, that is about $126 a year, and grants would bring it down.","<b>The yes-or-no question:</b> an $18 million community center at the Keller Building, paid by a special property tax of about 84 cents per $1,000 of assessed value before any grants.")
R("Republicans Gooch, Andres and Bradt face Democrats Mooradian, Kennedy and Osborn.","Republicans Gooch, Andres and Bradt face Mooradian, Kennedy and Osborn.")
R(" In their only debate last Tuesday night they sparred over energy costs, immigration and public safety.","")
R("by about 8 to 9 points in the averages, and Cook moved 11 more House races toward them on Friday.","by about 8 to 9 points in the averages, and Democrats are favored to take the House; Cook moved 11 more House races toward them on Friday.")
R("The Senate is close to a coin flip:","The Senate is a coin flip tilting Democratic:")
R("The president's approval is about 21 points underwater.","The president's approval is 21 to 22 points underwater.")
R("Republican Mike Lawler against Democrat Cait Conley in NY-17, 48 to 46 for Conley in the one independent poll, which Cook calls a toss-up.","Republican Mike Lawler against Democrat Cait Conley in NY-17, which Cook calls a toss-up; Conley leads 48 to 46 in the one independent poll.")
# add Orchard Park and Fredonia after Dunkirk item (before Scottsville)
R('<div class="line"><b>5. Scottsville.</b>','''<div class="line"><b>5. Orchard Park.</b> Congress, 23rd District: Republican Nick Langworthy, the incumbent, against Democrat Aaron Gies. State Senate, 60th District: Republican Gallivan, the incumbent, unopposed. Assembly: Democrat Burke, the incumbent, against Republican Dickson in the 142nd; Republican DiPietro, the incumbent, unopposed in the 147th. Town Justice is on the ballot; candidates not yet certified. No ballot questions. <b>Early voting:</b> Orchard Park Community Activity Center, 4600 California Rd, Oct 24&ndash;Nov 1 (weekdays noon&ndash;9).</div>
<div class="line"><b>6. Fredonia.</b> The same Congress, State Senate and Assembly races as Dunkirk. County Legislature: District 3, Republican Scudder, the incumbent, against Democrat Lee; District 4, Democrat Lewis unopposed. Village Trustee Mulholland and Councilmember Bashaw, both Democrats, are unopposed. No ballot questions. <b>Early voting:</b> County Fairgrounds 4-H Building, 1089 Central Ave, Dunkirk, Oct 24&ndash;Nov 1; on Election Day, Harvest Chapel, 39 Matteson St.</div>
<div class="line"><b>7. Scottsville.</b>''')
R("theballotbrief.com","The Ballot Brief")
d['body_html']=b
for p in ['edition-2026-10-18.json','site/data/edition-2026-10-18.json']: json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('ok')
# --- fourth review fixes ---
d=json.load(open('site/data/edition-2026-10-18.json')); b=d['body_html']
for o,n in [
("<b>5. Orchard Park.</b> Congress, 23rd District: Republican Nick Langworthy, the incumbent, against Democrat Aaron Gies. State Senate","<b>5. Orchard Park.</b> State Senate"),
("The same Congress, State Senate and Assembly races as Dunkirk.","The same State Senate and Assembly races as Dunkirk."),
("<b>NY-23, Dunkirk.</b>","<b>NY-23, Orchard Park, Dunkirk and Fredonia.</b>"),
("winning four of six Republican-held races that are within the polls' margin of error.","winning four of the six Republican-held toss-ups."),
("The justices serve 14-year terms. ",""),
("Democrat Nate McMurray, who ran for Congress in 2018 and 2020.","Democrat Nate McMurray."),
("Saturday: early voting opens, and runs through Nov 1.","Early voting opens Saturday and runs through Nov 1."),
("Early voting opens Saturday, Oct 24, and runs through Nov 1, and polls are open 6 a.m. to 9 p.m. on Election Day, Nov 3.","Early voting runs from Saturday, Oct 24, through Nov 1; polls are open 6 a.m. to 9 p.m. on Election Day, Nov 3."),
]:
    assert b.count(o)==1,o[:60]; b=b.replace(o,n)
d['body_html']=b
for p in ['edition-2026-10-18.json','site/data/edition-2026-10-18.json']: json.dump(d,open(p,'w'),ensure_ascii=False,indent=1)
print('fixed')
