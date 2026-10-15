# The Ballot — /election/ refresh rules

`/election/` is a public tracker Garret shares by link: https://benthambulletin.github.io/election/. It is separate from the daily paper. One job: every morning through Nov 4, 2026, bring `election/data.json` up to date and rebuild.

## Files
- `election/data.json` — every number on the page. Each row keeps its `url` (source). Keys: `as_of`, `updated_at`, `bottom_line` (six items, `order`/`headline`/`detail`), `what_changed` (list of plain sentences; empty if nothing moved), `generic_ballot`, `approval`, `senate`, `control`, `ny_governor`, `ny_house`, `local`, `key_dates`, `history` (one row per day: date, generic_ballot, trump_net, dem_senate_odds, hochul_margin).
- `election/build.py` — renders `index.html` from data.json. Run `python3 election/build.py` from the repo root. Never type a number into build.py or index.html.

## Each run
1. Research, in this order, and read the date inside each page, not the "updated" badge: Silver Bulletin generic-ballot page; RealClearPolling generic ballot and Senate toss-up map (the race pages for ME, OH, TX, IA, KS and any new toss-up); Cook Senate ratings (note rating changes); Wikipedia's Trump approval tracker table (the Oct-8-style per-tracker rows and average); Polymarket/Kalshi Senate odds (any reporting site is fine, dated); Emerson, Marist, Siena for NY governor; Emerson/Siena for NY-17; any NY-01 or NY-04 poll; WGRZ/WIVB/Niagara Gazette/Ken-Ton Bee for Niagara County and North Tonawanda ballot news.
2. Update data.json. Replace a row's poll only with a newer one; keep the row's `note` current (prior poll, rating moves). Rewrite `bottom_line` so it reads true today — six items, one line each, plain English, no cheerleading, no endorsements. Fill `what_changed` with what actually moved since yesterday (rating changes, a new poll that shifted a lead, a candidate event); leave it empty if nothing did. Append today's `history` row. Set `as_of` to today and `updated_at` to now (Eastern, ISO).
3. `python3 election/build.py`, then render at 390px with Playwright and Read the screenshot; check no "None", no "—" where a number should be, dates correct.
4. `git pull --rebase`, commit `Ballot — Month D` with only `election/` changed, push. Confirm the page serves (`curl -s https://benthambulletin.github.io/election/ | grep -c "Updated <today>"`).
5. Say nothing to Garret unless the run failed or something big moved (a rating change in a Senate toss-up, a NY poll outside the prior range) — then one line with SendUserMessage.

## Rules
- Never print a number without a dated source row in data.json. If a source can't be read today, keep yesterday's row and say so in `what_changed` ("RCP Senate average not refreshed today").
- Margins are Democrat minus Republican. `cook_rating` uses Cook's words.
- Nov 4 run: results special — replace polls with results where called (AP), keep the layout. After Nov 4 the task should be deleted.
- Don't touch anything outside `election/`.
