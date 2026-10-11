# A12 reference sweep report — bitcointalk + bitcoin.stackexchange

Agent: forum-census fetcher (phase A12). Collected 2026-10-10. Curl with Chrome 126 UA + `--compressed` throughout. No post dumps — census captures only. Raw HTML kept in OS temp, not in repo.

## Files (3 captures + this report)

| File | Registry | Status | Contents |
|------|----------|--------|----------|
| `2026-10-10-bitcointalk-mining-board-census.md` | bitcointalk-mining | OK | Mining board (board=14) page-1 census: 1 pinned + 39 recent threads (40 rows) with title/topic-id/starter/replies/views/last-post; all 5 child boards w/ topic+post counts; 153-page pagination (~6.1k topics) |
| `2026-10-10-bitcointalk-mining-support-board-census.md` | bitcointalk-mining | OK | Mining support sub-board (board=40) page-1 census: 39 topic rows (page renders 39, not 40), 3 stickies, 188 pages (~7.5k topics, matches 7,514 on parent index) |
| `2026-10-10-bitcoin-se-mining-tags-top-voted-census.md` | bitcoin-se | OK | Top 50 mining-tagged SE questions by vote score (from 598 unique questions swept across 15 tags) + top-voted answer snippets for the top 10 |

## Notable threads (exact titles as displayed)

**bitcointalk Mining (board 14)** — page 1, 2026-10-10:
- Sticky: "BITCOIN MINING INTRO & RULES OF THIS SUBFORUM - READ BEFORE POSTING" (topic 2415854, by -ck, 43,172 views; last post Nov 17, 2017 — the only pinned thread)
- "Bitcoin Mining Pool distribution monthly reports" (topic 5263569, veryhot, 158 replies / 4,434 views — recurring pool-distribution data thread)
- "The first miner has already run towards AI" (topic 5579146, hot, 62 replies — miners→AI pivot theme)
- "Bitcoin Community Revived the Debate over Funding Miners after 2040" (topic 5588539, hot — post-subsidy security debate)
- "My small room needs heat dispenser or somekind" (topic 5566808, hot — heat-reuse adjacent)
- "Any Home Bitcoin Miner Fans Here? Bitaxe Gamma, Avalon Nano 3S, NerdQaxe++" (topic 5537678, hot — home/bitaxe scene)
- "[11.2kW SOLAR/WIND/MAN] NastyMining Green Energy Project ☀💨💪🔋" (topic 1783328, veryhot, long-running OgNasty project thread)
- "Global Hashrate Heatmap" (topic 5586500) and "Starcloud Space mining" (topic 5595348 — freshest activity on the board, Oct 10 2026 02:40 PM)
- Recurring 2026 theme on page 1: miners pivoting to AI / halting sales, hosting offers (Albania €0.12/kWh, Ethiopia $0.01–0.03/kWh, Xinjiang $0.04/kWh), utility tariffs naming crypto mining (Idaho, North Dakota, Texas, BC)

**bitcointalk Mining support (board 40)** — 3 stickies:
- "Where to fix your Asic miners." (topic 5297994, 194 replies / 83,567 views)
- "First time/Small miner reference for getting started." (topic 4636521, 33 replies / 37,846 views)
- "Most Common Mining Issues, Read Before Making a New Post." (topic 5103892, 11 replies / 24,953 views)
- Freshest: "solo.ckpool.org: bestever 592.58T (4.5x network difficulty) with no block credit" (topic 5595799, last post Oct 9 2026)
- Active hardware/support cluster: GekkoScience Terminus A2X, BitAxe Gamma firmware errors, PSU coil whine, solo-mining-with-solar Bitaxe experiments

**bitcoin.stackexchange** — top 3 of 50 by score (all with accepted answers):
1. "What exactly is Mining?" (score 208, 118k views, 2011)
2. "What are bitcoin miners really solving?" (score 163, 297k views, 2013)
3. "How much will transaction fees eventually be?" (score 132, 2011)
- Canonical evergreens in the top 10: "How do you obtain bitcoins?" (131), "Why is 6 the number of confirms…secure?" (124), "How much Bitcoin will I mine right now with hardware X?" (116, 336k views), "How does merged mining work?" (112), "In the ASIC-age, is it worth starting mining Bitcoin at home?" (67, canonical). All top-50 questions were asked 2011–2017 — the canonical mining corpus is old and stable.

## Parks / deviations (honest)

1. **Board ids differ from the brief.** Brief said board=1.0 is the "Mining" board — board 1 is actually "Bitcoin Discussion". Real ids from the live index: Mining = **14**; Mining support = **40** (brief's guess 160 is "Mining (Altcoins)" under Alternate cryptocurrencies). Both census files record this.
2. **Board 40 page 1 renders 39 topic rows**, not 40 (observed, noted in file; 188 pages × 40 ≈ 7,520 ≈ the 7,514 topics shown on the parent index — consistent).
3. **No plain `mining` tag on bitcoin.SE.** "Mining tags top-voted" was satisfied by sweeping the 15-tag mining-* family (mining-theory 831 q, mining-pools 827, mining-profitability 453, mining-reward 437, mining-hardware 436, mining-software 141, gpu-mining 134, solo-mining 122, cpu-mining 103, mining-technical-details 95, mining-setup 91, mining-pool-shares 79, merged-mining 44, selfish-mining 35, cloud-mining 34); 598 unique questions merged, top 50 kept. First 12 tags have has_more=true (each tag's top ~50 swept).
4. **SE HTML is Cloudflare-gated** ("Just a moment…" challenge) for curl; used the official SE API 2.3 (anonymous, no key) instead — ~17 calls, quota 300/day/IP.
5. **Answer snippets truncated** at ~400 chars (verbatim, HTML stripped); 3 of the top-10 have a top-voted answer that is NOT the accepted one (Q8031, Q1170, Q3111) — flagged inline. SE content license CC BY-SA 4.0.
6. **bitcointalk encoding** is ISO-8859-1 declared but mixed with UTF-8 in places; titles decoded utf-8-then-cp1252 per string; a few non-ASCII chars remain imperfect (noted in files).
7. **Thread titles in board lists are as displayed** — a few long titles are truncated by the forum UI itself (e.g. "Non-standard tx (anyone-can-spend OP_N) — 77,943 sats fee for the miner who incl", "…hosting services her").
8. bitcointalk served plain HTML, no bot walls; dates/times are forum-displayed (forum timezone, DST), e.g. "October 10, 2026, 02:40:54 PM".

## Method

- bitcointalk: `GET /` (category/board id discovery) → `GET /index.php?board=14.0` and `?board=40.0`, page 1 only; parsed thread rows (subject, topic id, sticky/lock/hot icons, starter, replies, views, last-post date+user) + child-board stats + pagination.
- SE: API 2.3 `search/advanced` per tag (`sort=votes`, pagesize=50) → merge/dedupe → top 50; `/questions/{ids}/answers?sort=votes&filter=withbody` for top-10 answer snippets.
