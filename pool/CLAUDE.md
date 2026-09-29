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

## Sealed picks (hard rule)
Until a game has kicked off, nothing on the page, in the column, in the Ticker, or in any message to
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
  Ticker) whenever the number of decided games changes. Picks for games that have not kicked off never
  leave the script. Run it every time, even when no new game is final: it refreshes entrants and sides.
- `build.py` — renders `index.html` from `season.json`.
- `template.html` — the page. Change design here, never in `index.html`.
- `about/index.html` — the static "How it works" page (rules, full badge key, who Claude is). The badge
  list there duplicates the `BADGE` table in `template.html`; change both. The money switch also
  rewrites its "Free to play right now" paragraph. Everything explanatory lives there, not on the board.
- `preview/index.html` — a simulated live Sunday for design feedback. Delete it once Garret is done.

## Run: NEW WEEK (Tuesday morning)
Idempotence first: if `season.json` `currentWeek` already equals the coming week's number AND the
Tally form's first game title already names that week's Thursday game, do nothing except send
Garret the one-line message below.
1. Coming week = the NFL week whose Thursday game is next. Fetch the slate from
   https://www.nfl.com/schedules/2026/by-week/week-N and cross-check one other schedule site.
   Kickoffs to UTC (ET = UTC-4 until Nov 1, then UTC-5). Note London/international games in `when`.
   Byes are fine: fewer than 16 games is fine, but then the form must have exactly that many game
   questions (remove extras with Tally `remove_questions`; the ids left in `form.questions.games`
   must be in slate order and match count).
2. Previous week must be `final` before moving on. If it is not, run the SCORE steps for it first.
   A week with no entry in `weeks{}` was not played (Week 3 was never sent out); skip it.
3. Write `weeks{N}` in season.json (copy the shape of an existing week; players/trash empty,
   status `pre`, `opensAt` = now in UTC — score.py ignores submissions older than that, so last
   week's sheets never bleed into this week), set `currentWeek`, `updated`.
   Then draw the house entry's picks, exactly like this and nothing cleverer:
   `rng = random.Random(int(hashlib.sha256(b"sundaytax-2026-w<N>").hexdigest(),16))`, then for each
   game in slate order `rng.choice([away, home])`, then `tb = rng.randint(37,52)`. Store as
   `weeks{N}.housePicks = {"picks": {"0": team, ...}, "tb": tb, "trash": <one dry line in Claude's voice>}`.
   The seed is public so anyone can verify the coin wasn't tuned. Claude is on the board, tagged House,
   never wins the week, never counts toward clinch/out math, and its picks are sealed like everyone's.
4. Update the Tally form IN PLACE (`load_form` RGOakJ first, then `update_text` on the block uuids
   the ledger shows): the form title `The Sunday Tax — Week N`; each game TITLE block's text
   `Away at Home — Day time` in slate order; each game's two MULTIPLE_CHOICE_OPTION texts (away first,
   then home); the tiebreaker TITLE `Total combined points in <MNF away> at <MNF home>`; the heading
   texts (Thursday / Sunday 1:00 PM / Sunday afternoon / Prime time) if the slate shape differs.
   Then `save_form` with status PUBLISHED. Question ids do not change when text changes; if you had to
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
   (b) the Thursday-night run that scores TNF, (c) the three Sunday window runs, and (d) the final.
   Every other hourly run leaves `column` exactly as it is, even when new sheets arrive — the Board
   and the Ticker carry the facts; the column is a voice, not a log.
5. `python3 build.py`, commit (`Pool: Week N update` / `Pool: Week N final`), push, confirm live.
6. UPDATE runs send nothing unless something failed. SCORE sends Garret one short message: winner
   (and payout only if `buyIn` > 0), one line per player with record, entrant count, and the standings
   link. While `buyIn` is 0 never mention money, pots, Venmo or collecting.

## Run: ROLL CALL (Thursday evening)
Fetch submissions, list who has submitted for the current week (normalized names) and the entry count
and pot. Send Garret one message: names in, and "nag list" = last week's entrants who haven't submitted.
No page rebuild.

## By the Numbers
score.py writes `weeks{N}.stats` from games that have kicked off: per-game split counts and who was in
the minority, upset count, best pick (fewest right, who), nobody-had, the room's record on the Bills
game and the Jets game, and the house entry's line. The column should lean on these: name the
contrarian who hit, the room that whiffed, the homer who got taxed. Never before kickoff.

## Badges
score.py awards the weekly badges (crown, backdoor, wolf, coin, homer, traitor, dead, sweep, early,
buzzer, bigmouth) and build.py the season ones (cellar, bridesmaid, iron, streak). The key is on `about/`.
Two are the commissioner's call and go in `weeks{N}.awards` as `{"name": ..., "badge": "prophet",
"note": "said Derek goes 0-for-16; he went 3-13"}`: **prophet** (trash talk that came true) and, if a
run wants to hand out **bigmouth** by judgment rather than by the last-place rule, the same way. Award
prophet only on the FINAL run, only when the trash talk made a checkable claim that checked out.

## Rules (fixed)
Latest submission before each game's kickoff counts for that game. Submitted after a game starts →
that game void, rest count. Tied game → nobody. Winner = most correct; tie → closest to MNF combined
total; still tied → split. Blank tiebreaker = worst guess. Skipping a week is free. All trash talk is
published exactly as written.
