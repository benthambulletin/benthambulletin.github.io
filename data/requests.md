# Requests from Garret

Read this before every run. Dated items run on that date; standing items apply every day until removed.
When Garret asks for something in chat, add it here and push in the same turn.

## Standing

- **Jets: go gentle**, for Tommy's sake. Report the game honestly, no pile-on. Bills and Jets stay even in space.
- **Next Jets and Bills games** go on the Family Today calendar.
- **Home Wire order:** try Scottsville first; if nothing, run at least one Rochester, NY headline. Dunkirk (not Jamestown) for the Chautauqua beat. North Tonawanda only when there is real news.
- **The Stars** are computed from that day's real planetary positions and aspects (ephem, 4° orb): Aries (Kaylani, Luka), Cancer (Gregg), Leo (Leah, Tommy), Virgo (Derek, Joanne), Scorpio (Ariel, Claire, Garret).
- **Luka is 3** (born April 19, 2023). Check any age math.
- **The Ledger** never repeats a number or story used elsewhere in the same edition, or the day before.
- **Weather answer:** if Garret asks about rain or storms, answer in the reply as well as in the paper.
- **No analytics / no view counter.** Decided.
- **No AI-generated images of real people** (Josh Allen, family). Use supplied photos, credited.
- **Migraine log (from Sept 27):** pull the Tally form obWNYP every morning; the Family Today ask box links to https://tally.so/r/obWNYP. Who and when only. (The Barograph itself was retired Oct 21.)

- **The Sunday Tax (from Sept 29): Tuesdays, Wednesdays and Thursdays** run a small bordered box in The Gridiron, headed "The Sunday Tax," with: the pick link **https://tally.so/r/RGOakJ**, the standings link **https://benthambulletin.github.io/pool/**, and one line — while `pool/data/season.json` has `buyIn` 0: "Free to play for now, straight-up winners, bragging rights on the line; a $5 buy-in may come later. Sheets lock at each kickoff; first game Thu <time>." Once `buyIn` is 5: "$5 a week, straight-up winners, the pot to the best record. Sheets lock at each kickoff; first game Thu <time>." It is open to friends and coworkers too, not just family — say "anyone with the link." Read `pool/data/season.json` for the current week number and the Thursday kickoff. Tuesday's box also names last week's winner (and payout only when `buyIn` was on) if `weeks[N-1].status` is final. No box Fri–Mon; the Sunday paper may mention the pot in a line if there is room. Never edit anything under `pool/`.

- **The Ballot mirrors /election/ (Garret, Oct 18).** The paper's Ballot section and any election item are a summary of `election/data.json`, the tracker Garret built. Every poll, rating, margin, candidate name, party label, date and early-voting site must match that file as of the morning's run; no number the tracker doesn't carry, no wording that contradicts its bottom line. Read `election/data.json` before writing the Ballot, and give the reviewer the file to compare against.
- **Every web address is a link (Garret, Oct 18).** Older readers won't copy and paste. Any tally.so, benthambulletin.github.io or other URL in the paper is an `<a href>`; qc.py now fails on an unlinked one.

- **No barometric pressure in the paper (Garret, Oct 21: "remove the barometric pressure stuff").** Barograph section, pressure tile and every pressure line are gone from No. 120 on. Middle tile is sunset time. The migraine log line moves to Family Today. See CLAUDE.md section 6.
- **The family gets the link by text at 8:00 a.m. (Garret, Oct 21).** His iPhone texts https://benthambulletin.github.io to the family group ("Gang of Seven") daily at 8:00. The paper must be live, reviewed and final by then; any post-8:00 change goes to people who already opened it, so get the cover and fixes in before 8 when possible.
- **Read-aloud uses a recorded natural voice (Garret, Oct 22).** Nobody should have to download anything for it to sound good. See CLAUDE.md, reader tools.
- **Reader tools (Garret, Oct 21: "hell yes").** Every edition carries "Read it to me" (the browser reads the paper aloud) and "Bigger print" (remembered per device) at the top. Built into `tools/site.py`; no analytics, nothing sent anywhere. Don't remove them.
- **Traveler's Weather (Garret, Oct 21).** When someone in the family is traveling, show the weather where they're going for every day of the trip. See CLAUDE.md, `data/travel.json`.
- **Daily Ballot through Nov 2 (Garret, Oct 21).** `tools/ballot_box.py`; see CLAUDE.md section 10.
- **Form photos stay private (Garret, Oct 21).** Encrypted pipeline only; see CLAUDE.md, the family form.
- **/election/ is a separate tracker (Oct 14).** It has its own daily task and rules in `election/CLAUDE.md`. The paper may link to it (https://benthambulletin.github.io/election/) but never builds it or edits `election/`.
- **Family form (Oct 4):** https://tally.so/r/rjxDpl — check every morning, run entries automatically per CLAUDE.md, hold only anything unkind or private and flag it to Garret.

- **Migraine log `who` (Oct 30):** take the person from the visible "Who is this for?" answer, never the hidden `who` field — that one is just the pre-fill from the link (Garret's link opens as Garret, so Mom's Oct 29 entry was mis-tagged and dropped).

## Dated

- **Sun Nov 1, 2026 — Sunday Spotlight: the month in migraine.** (Monthly research run, Oct 27.) A quiet month for the family's own medicines: no news on Qulipta or Ubrelvy, nothing new on the PACAP drug or Biohaven's TRPM3 pill. What did happen, Sept 27–Oct 27:
  - **Migraine and endometriosis travel together more than anyone counted.** A Mayo Clinic pooled analysis of 35 studies and about 13 million women, presented Oct 20 at the American Neurological Association meeting, found women with endometriosis (a painful condition where womb-lining tissue grows outside the womb) had about 2.3 times the odds of migraine; short billing records may miss most women who have both. An association, not proof of cause; worth a mention to a doctor for anyone with both kinds of pain. (https://www.newswise.com/articles/migraine-endometriosis-overlap-far-more-than-recognized-analysis-of-13-million-finds ; https://www.healio.com/news/neurology/20261020/overlap-between-migraine-endometriosis-may-be-underacknowledged)
  - **A new kind of rescue pill reached final-stage trials.** TriGemX Bio (Oct 1) started phase 3, the last round of testing before an FDA application, for elismetrep, a pill that blocks TRPM8, a "cold-sensing" switch on the nerves of the face and head. No new numbers yet; first results expected mid-2027. (https://www.biospace.com/press-releases/trigemx-bio-announces-94m-financing-and-initiation-of-phase-3-trials-for-elismetrep-a-potential-first-in-class-treatment-for-migraine)
  - **A small reassurance on heart and stroke.** A Swiss clinic followed 17 people with a past stroke, mini-stroke or heart disease who took CGRP-blocking migraine drugs (the family Garret's preventive belongs to) for up to five years: no new strokes or heart problems, and 13 of 17 cut their migraine days at least in half. Tiny and uncontrolled, so call it modest. (https://bioengineer.org/migraine-drug-safety-reassuring-in-patients-with-prior-stroke-and-heart-disease-small-study-finds/ — Journal of Neurology, doi 10.1007/s00415-026-14099-z)
  - **Background (not new this month): the September prevention guideline.** The neurologists' and headache doctors' updated guideline (AAN/AHS, Neurology, Sept 2026) rated atogepant with high or moderate confidence for both occasional and chronic migraine, but names no single first-choice drug; doctor and patient pick by effect, side effects, safety and cost. (https://www.neurologylive.com/view/aan-ahs-issue-updated-guideline-pharmacologic-migraine-prevention-adults-faqs)
  - **Background: the PACAP drug.** Lundbeck's bocunebart blocks PACAP, a second migraine messenger besides CGRP; it cut migraine days in a mid-stage trial in June, and a phase 3 update is expected by year's end. Nothing new in October. (https://www.lundbeck.com/us/newsroom/2026/lundbeck-presents-positive-phase-iib-data-for-bocunebart-lu-ag09222)
  - **The family's own month (Tally obWNYP, Sept 27–Oct 27), counts and days only:** four logged migraines: Garret two (Oct 6, Oct 23), Joanne one (Oct 9), Gregg one (Oct 6). One of the four started overnight. Garret and Gregg logged the same day, Oct 6. Re-pull the form Sunday morning in case more come in. **No pressure / barometer line** (Garret, Oct 21, overrides the research task's "what the glass was doing"); never symptoms or medication by person.
  - Say in the section that an AI wrote it.
- **Sun Nov 1 — Sunday Question answers:** Gregg sent his (form, Oct 25): best costume was "the man from Mercury" — an old motorcycle helmet with the dashboard and backup lights from a Mercury, run off a motorcycle battery, wrapped in black, six inches taller; won first place at Mickey Rats in Jamestown. (Leave out the prize and the ride-home line.)
- **Oct 23 / Oct 25 — birthday stretch:** Claire's edition on the 23rd; one joint Garret + Ariel edition on the 25th.

## Done

- Oct 28, No. 126 — Gregg's fog question ran as Question of the Day; Chautauqua Ridge moonrise cover from spool.
- Sep 26, No. 94 — nor'easter Long Island update; answered "rain tomorrow?" (30% after 5 p.m. Sunday).
- Sep 27, No. 95 — cannabis-seed Spotlight; Toby cover; Luka get-well line. Published by the 7:20 check (scheduled 6:59 run did not push).
- Sep 28, No. 96 — Mars into Leo in the Stars; built by the 6:59 in-session run.
- Sep 29, No. 97 — Port Bay cover (Garret, Sat Sep 26); first edition from the Morning feed and hourly Barograph.
- Sep 30, No. 98 — Luka bedtime cover (Garret, Tue night).
- Oct 1, No. 99 — Luka bedtime cover, then swapped to Garret's backyard doe photo (Thu a.m.).
- Oct 2, No. 100 — the hundredth edition; Luka bedtime cover added after publish (Garret, 7:25); Family Today ask box now points to the Tally form.
- Oct 3, No. 101 — Friday night football sunset cover (Garret, 7:03).
- Oct 4, No. 102 — Luka doctor cover from spool (Garret, Sat 3 p.m.); month-in-migraine Spotlight run; October voice and palette in force.
- Oct 6, No. 104 — Luka stairs cover from spool; first Sunday Tax box (Week 5, Devin won Week 4).
- Oct 11, No. 109 — Barograph note (Garret's call); lake-effect Spotlight with the AI-forecasting (Isaias/NYT) beat.
- Oct 18, No. 116 — Ariel's Sunday answer (pumpkin) ran; ballot Spotlight.
- Barograph analysis — superseded: ran early on Garret's own history (Oct 10); Barograph retired from the paper Oct 21.
