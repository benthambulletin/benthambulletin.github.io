# The Sunday Tax — runbook for scheduled runs

Garret's weekly NFL pick 'em. **Free to play for now** (`buyIn` is 0 in season.json); the plan is $5 a week
with the whole pot to the winner once enough people are in (`plannedBuyIn`). Straight-up winners, best record wins the week,
tiebreaker = closest to combined points in the Monday night game. Picks arrive on a Tally form
(form id `RGOakJ`, same link all season). Standings live at **https://benthambulletin.github.io/pool/**
and are rebuilt from `pool/data/season.json` by `pool/build.py`. Commissioner: Garret. Venmo @garretbentham.

**The pool page never links to the paper.** Coworkers and friends play; the Bulletin is family-only. No link, no mention of the Bulletin by name on the pool page.

Everything here runs from a clone of this repo at `/home/claude/benthambulletin.github.io`
(`git pull --rebase` first; `add_repo` owner `benthambulletin` repo `benthambulletin.github.io` with push
access if the clone is missing). Work in `pool/`. Commit author `Claude <noreply@anthropic.com>`.
Push = `git pull --rebase origin main && git push`. The Bulletin's own runs also push here; never touch
anything outside `pool/`.

## Design (locked; last changed Oct 2 at Garret's request)
Board, top to bottom: masthead → sticky tab bar (Standings · Make picks · Rules, identical on `about/`) →
"Sheet received" box (`#ack`, only when the form redirects to `/pool/?filed=1`) → the Now block (week +
status kicker, one plain-English headline sentence computed from kickoffs, the picks button, the
Updated line) [hero, Oct 2: kicker + one big line + subline, by state — countdown to first lock before kickoff; the live game and score while one is on; the leader between games; the champion when final; plus a Next lock bar with a live countdown] → three tiles (players · games final · still open to pick) → the Mugshot box →
**Standings** (hint + dot key; › on rows; a row of dots under each name, one per game that has kicked off: teal right, red wrong, hollow live; tied ranks read T2; the house shows no rank) → **This Week's
Games** (time ET + network; tap a started game for who picked whom; the house is left out of name lists)
→ **The Column** + trash talk → By the Numbers → The Season → How it works box → sign-off. All times on the
board and `about/` are Eastern. Rule and badge words on the board link to `about/` anchors. Eight badges,
no more. Do not add sections, columns, keys, tickers or badges without him asking. Explanatory text goes
on `about/`, never the board.

## Sealed picks (hard rule)
Until a game has kicked off, nothing on the page, in the column, in `updates`, or in any message to
Garret may reveal or hint at anyone's pick for it: no "everyone likes X", no "Y is the only one on the
road team", no consensus counts, no "the room is split", no tiebreaker numbers. score.py enforces this
for the data; the column must obey it too. Before kickoff the column may talk about who has filed, when,
and the trash talk. After kickoff a game's sides are public and fair game. Rule of thumb: if a late
filer could learn anything about the slate from it, cut it.

## Money switch
`data/season.json` → `buyIn`. 0 means free: the page hides pots and payouts and says so; score.py still
reports `pot $0`. When Garret says to turn the money on, set `buyIn` to 5 (from that week forward — do not
restate earlier weeks), update the Tally form's opening TEXT block and its last TEXT block ("The money") to say
$5 a week, Venmo @garretbentham, and tell the Bulletin via `data/requests.md`. Never turn it on without him saying so.

## The three pages are wired together (Oct 2)
- Form → receipt: Tally redirect on completion goes to `/pool/sheet/` (see "Receipt" below), which links to the board. The board's `?filed=1` box is a fallback.
- Form intro TEXT block (`eb81f875-cf82-485b-8818-80a58ac5ace2`) has three parts: the fixed rules line,
  a **This week:** line, and the links `The board · How it works`. Keep the links and the fixed line.
- Form colors/font match the board (cream `#fbf5e4`, ink, teal accent, red button, Lora). The form is on
  Tally's free plan, so the advanced input/button styling is not live; do not add custom CSS.
- `about/` anchors the board links to: `#locks #sealed #tiebreak #mugshot #trash` and `#b-<badge id>`.
  Keep those ids if you edit the page. Its week strip reads `data/page.json` live; nothing to update.
- **Games come off the form at kickoff.** Tally can't lock one question, so every REFRESH/UPDATE run
  hides (`configure_blocks` visibility, isHidden true on the game's TITLE block) each game that has kicked
  off, plus its slot heading once every game under it has, then `publish_form`. NEW WEEK un-hides every
  game TITLE and heading before rewriting them. score.py already voids any pick sent after kickoff;
  hiding just stops people from making one.

## Added Oct 2 (Garret asked for these)
- **Receipt:** the form's redirect on completion is `https://benthambulletin.github.io/pool/sheet/?filed=1&g0={{q0}}…&g15={{q15}}&t={{tiebreak}}&n={{name}}`
  using the question uuids (the `questionUuid` column of the Tally ledger, NOT the block uuids), name LAST.
  `sheet/` shows a screenshot-ready receipt from those values in the player's own browser and strips them
  from the address bar; nothing is stored or published. If a week has fewer games (byes), rebuild the URL
  so g<i> matches slate order. Keep it.
- **Past weeks:** build.py writes a frozen page for every final week except the current one at
  `/pool/weeks/<N>/` and lists them under "Past Weeks" on the board. Archived pages never refetch page.json.
- **Calendar:** build.py writes `/pool/week.ics` (the week's first kickoff and first Sunday kickoff still ahead,
  each with a 1-hour reminder). The board links it under the picks button while games are open. Commit it.
- **Live scores:** REFRESH/UPDATE runs set `games[i].live` (e.g. `Bills 17–14 · 3rd qtr`, leader first) and
  `games[i].liveAt` (UTC ISO) for games in progress, from the sports data tool or ESPN's scoreboard; unset
  them when a game goes final. Never guess a score; if none is reliable, leave `live` out.

- **Link preview + home-screen icon:** `og.png` (1200×630) and `icon.png` (180×180) are static; the board, `about/` and `sheet/` carry the og/apple-touch-icon tags. Don't regenerate them weekly.

## Files
- `data/season.json` — the only state. `currentWeek`, `weeks{N}` (games with ISO kickoffs, winners,
  scores, players, trash, column, tiebreakTotal, weekWinners, weekPayout, status pre/live/final),
  `form.questions` (Tally question ids: name, tiebreak, trash, and the 16 game questions in slate order),
  `aliases` (lowercase name → display name, for people who type their name three ways).
  **Kaylani & Luka are one entrant, always** — any of "Kaylani", "Luka", "Kaylani & Luka" etc. maps to
  "Kaylani & Luka"; never split them. Add new aliases when a known person files under a new spelling;
  never merge two different people.
- `score.py submissions.json [--final]` — scores the current week from a saved Tally fetch. Enforces
  the rules; do not re-derive them by hand. It also computes per-player rank, movement since the last
  run, games left, max possible, alive/out/clinched, who is on each side of every game that has kicked
  off (`games[].sides`), the "what decides it" list, and appends a line to `weeks{N}.updates` (the
  log, kept in the data but not shown on the page) whenever the number of decided games changes. Picks for games that have not kicked off never
  leave the script. Run it every time, even when no new game is final: it refreshes entrants and sides.
- `build.py` — renders `index.html` from `season.json`, and writes `data/page.json` (the same page data). The
  page fetches `page.json` past the phone's cache on load, on return to the tab, and every ten minutes, and
  re-renders if it is newer — so a cached `index.html` still shows the live board. Commit both.
- `template.html` — the page. Change design here, never in `index.html`.
- `about/index.html` — the static "How it works" page (rules, full badge key, who Claude is). The badge
  list there duplicates the `BADGE` table in `template.html`; change both. The money switch also
  rewrites its "Free to play right now" paragraph. Everything explanatory lives there, not on the board.

## Run: NEW WEEK (Tuesday morning)
Idempotence first: if `season.json` `currentWeek` already equals the coming week's number AND the
Tally form's first game title already names that week's Thursday game, do nothing except send
Garret the one-line message below.
1. Coming week = the NFL week whose Thursday game is next. Fetch the slate from
   https://www.nfl.com/schedules/2026/by-week/week-N and cross-check one other schedule site.
   Kickoffs to UTC (ET = UTC-4 until Nov 1, then UTC-5). Note London/international games in `when`.
   Also record each game's network in `games[].tv` (`CBS`, `FOX`, `NBC`, `ESPN/ABC`, `Prime Video`,
   `NFL Network`, …) from NFL.com's weekly "How to watch" article, cross-checked against one other
   listing. If a network isn't announced yet, leave `tv` out; never guess. The board shows it next to the time.
   Byes are fine: fewer than 16 games is fine, but then the form must have exactly that many game
   questions (remove extras with Tally `remove_questions`; the ids left in `form.questions.games`
   must be in slate order and match count).
2. Previous week must be `final` before moving on. If it is not, run the SCORE steps for it first.
   A week with no entry in `weeks{}` was not played (Week 3 was never sent out); skip it.
3. Write `weeks{N}` in season.json (copy the shape of an existing week; players/trash empty,
   status `pre`, `opensAt` = now in UTC — score.py ignores submissions older than that, so last
   week's sheets never bleed into this week), set `currentWeek`, `updated`.
   The house entry's picks are NOT stored: score.py draws them at run time from the week's seed
   (`sundaytax-2026-w<N>`), so they never sit in the public data. Store only
   `weeks{N}.housePicks = {"trash": <one dry line in Claude's voice>}`. Claude is on the board, tagged House,
   never wins the week, never counts toward clinch/out math, and its picks are sealed like everyone's.
4. Update the Tally form IN PLACE (`load_form` RGOakJ first, then `update_text` on the block uuids
   the ledger shows): the form title `The Sunday Tax — Week N`; each game TITLE block's text
   `Away at Home — Day time · NETWORK` in slate order (drop the ` · NETWORK` part when `tv` is unknown); each game's two MULTIPLE_CHOICE_OPTION texts (away first,
   then home); the tiebreaker TITLE `Total combined points in <MNF away> at <MNF home>`; the heading
   texts (Thursday / Sunday 1:00 PM / Sunday afternoon / Prime time) if the slate shape differs.
   Rewrite the **This week:** line in the intro block: last week's winner and record, and whose
   mugshot is up if there is one (e.g. `<b>This week:</b> Mike took Week 4 at 12–4. Leah's on the
   mugshot.`); if last week wasn't played, the first game and its kickoff. Never anything about picks.
   Then `publish_form`. Question ids do not change when text changes; if you had to
   add or remove a game question, update `form.questions.games` to match, in order.
5. `python3 build.py`, commit `Pool: Week N slate`, push. Confirm
   https://benthambulletin.github.io/pool/ shows Week N (cache-bust with `?N`).
6. Message Garret (SendUserMessage), one line: `Week N is up — https://tally.so/r/RGOakJ — first game
   Thu <time>.` Nothing else unless something failed; then say exactly what, in one line.

## Run: REFRESH (hourly, 8 am–11 pm) and UPDATE (Sunday 4:47 / 7:47 / 11:47 pm) and SCORE (Tuesday 12:20 am, --final)
All three are the same steps; they differ only in what has finished. The Sunday runs are timed to the
1:00, 4:25 and Sunday-night windows so the board moves right after each block of games.
1. `fetch_submissions` for RGOakJ with limit 200; save the entire result verbatim to
   `/home/claude/subs.json` with the Write tool.
2. Scores: for every game in `weeks{N}` whose `winner` is null and whose kickoff has passed, find the
   final. Use the sports data tool if present, otherwise search the web (ESPN or NFL.com scoreboard
   for that date). Only FINAL games get a `winner` (team nickname exactly as in `games[].away/home`,
   or `TIE`) and a `score` like `24–17`. In-progress games stay null. For SCORE, every game must be
   final and `tiebreakTotal` = both MNF teams' points added together.
3. `python3 score.py /home/claude/subs.json` (add `--final` for Monday). Read its output.
4. Write the column: set `weeks{N}.column` to 2–4 short paragraphs in the voice of a wise-ass
   commissioner: who is leading, who is bleeding, the dumbest pick of the day, who is overdue, and —
   when `decides` is non-empty — which open game the week turns on and who is on each side. Name
   names. Read score.py's output (movement, out, clinched, DECIDES) and write from it. Never mention a
   pick, a lean, or a consensus for any game that has not kicked off (see Sealed picks). Trash talk from
   the form is printed automatically under the column, unedited — never soften, cut, or comment on it.
   Under 120 words on Sunday, up to 180 for the final.
   **Cadence:** the column is rewritten only by (a) the first run of the week that finds any entrants,
   (a2) the 8:07 a.m. refresh EVERY day (before kickoff: who has filed, who hasn't, trash talk; after: standings,
   who's bleeding, what's next — sealed rule still applies),
   (b) the Thursday-night run that scores TNF, (c) the three Sunday window runs, and (d) the final.
   Every other hourly run leaves `column` exactly as it is, even when new sheets arrive — the Board
   carries the facts; the column is a voice, not a log.
5. `python3 build.py`, commit (`Pool: Week N refresh` / `update` / `final`), push, confirm live. **Every run
   pushes, even when nothing changed** — the page's "Updated" line only moves when a push lands, and that
   line is how people know the board is alive. A commit an hour is fine.
6. UPDATE runs send nothing unless something failed. SCORE sends Garret one short message: winner
   (and payout only if `buyIn` > 0), one line per player with record, entrant count, the standings
   link, and the mugshot reminder (see The Mugshot). While `buyIn` is 0 never mention money, pots, Venmo or collecting.

## The Mugshot
The week's winner picks one loser, and that person's face runs on the board the following week in a
framed box under the tiles. The winner sends Garret the photo; Garret sends it here in chat.
When it arrives: crop it square around the face (PIL, `ImageOps.exif_transpose`, ~600px), save as
`faces/w<N>.jpg` where N is the week it will show, and set `weeks{N}.face =
{"photo": "/pool/faces/w<N>.jpg", "who": <loser>, "by": <winner>, "week": <week won>, "line": ""}`
(`line` is optional — one dry sentence if Garret gives one). Rebuild and push. `face` is null or absent
when there is none; the box does not render. The SCORE message to Garret ends with
"<winner> picks the mugshot for next week — send me the photo." Never generate or alter a face;
only crop what Garret sends. If the photo isn't in by the Tuesday new-week run, the week runs without
one and the box stays empty; it can be added any day after.

## Run: ROLL CALL (Thursday evening)
Fetch submissions, list who has submitted for the current week (normalized names) and the entry count
(and the pot only if `buyIn` > 0). Send Garret one message: names in, and "nag list" = last week's entrants who haven't submitted.
No page rebuild.

## By the Numbers
score.py writes `weeks{N}.stats` from games that have kicked off: per-game split counts and who was in
the minority, upset count, best pick (fewest right, who), nobody-had, the room's record on the Bills
game and the Jets game, and the house entry's line. The column should lean on these: name the
contrarian who hit, the room that whiffed, the homer who got taxed. Never before kickoff.

## Badges
Eight, no more: score.py awards **crown** (leading the week; the winner at final), **cellar** (Porta Potty,
last place this week), **wolf** (only one right on a game), **homer** (took the Bills or Jets, they lost)
**coin** (behind Claude) **dead** (mathematically out of the week) and **buzzer** (first sheet inside the last hour before Thursday kickoff); build.py computes **streak** (On Fire, 3+ straight correct picks across
weeks). Crown, coin and porta potty wait until three games are final (Garret, Oct 2). Garret cut the rest because the board got busy. Do not add badges without him asking. The key
is on `about/`.

## Rules (fixed)
Latest submission before each game's kickoff counts for that game. Submitted after a game starts →
that game void, rest count. Tied game → nobody. Winner = most correct; tie → closest to MNF combined
total; still tied → split. Blank tiebreaker = worst guess. Skipping a week is free. All trash talk is
published exactly as written.
