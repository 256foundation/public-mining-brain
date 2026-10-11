# OSMU forum capture report (capture-loop A1)

> Registry ID: osmu-forum
> Captured: 2026-10-10
> Source: https://osmu.xyz (Discourse, site created 2026-05-17)

## Upstream

- 32 public topics / 164 posts via `latest.json` (about.json reports 48 topics; remainder unlisted/deleted). First-ever capture of this forum.

## Captured: 26 topics (all posts, verbatim, HTML→markdown)

39, 28, 87, 100, 102, 80, 99, 77, 98, 90, 89, 72, 78, 76, 40, 53, 31, 38, 32, 35, 34, 29, 33, 27, 24, 11

Total posts captured: 152 (upstream total across all 32 topics: 164). Largest: #39 dvb-WarpPool (60 posts, incl. 42 fetched via `posts.json?post_ids[]=`), #28 Pogolo (16), #100 WarpAxe Gamma (13), #33 BitForge nano (6), #72 / #29 (5).

## Skipped: 6 topics

- #5 — site welcome topic (boilerplate)
- #101 — "Greetings Everyone!" intro, no technical content
- #71 — "Question about OSMU Discord" — community meta only, no signal
- #73 — "Problem with Bitax" — generic support thread (cat-knocked unit; only tip: reseat heatsink, 127° = lost ASIC contact)
- #37 — "BitForge Showoff" — photos only, no technical content
- #30 — "OSMU Solo Group" — Blitzpool operator interest-gauge pitch, zero replies

## Failures

- None. All 32 topic JSONs fetched; all 60 posts of #39 recovered (page 1 + post_ids chunks).

## Notes for wiki consumers

- Signal is ADJACENT-ecosystem only (Bitaxe/ESP-Miner/open-pool), not a 256F deliverable.
- Gems: #39 dvb-WarpPool (Rust solo pool, SV1+SV2, VarDiff per device class, ongoing v1.x–v1.39 release log through 2026-10-10), #28 Pogolo (Golang pool, v1.1.6 adds native SV2), #100/#102 WarpAxe (Rust firmware for Gamma + NerdQAxe++/NerdOctaXe), #99 6-ASIC Ethernet Bitaxe cluster mod (STM32 + PC controller, ~220 units), #87 BTC PoW Lab hybrid solo accounting, #53 S23 BM1373 dump init sequence, #24 BM1370/Gamma primer, #27 canonical Bitaxe intro w/ model table.
- 2.14→2.15 firmware friction cluster: #78 (single-file OTA needs manual dashboard refresh), #40 (error-rate regression after 2.14), #35 (ASIC heat on v2.14.0).
- Topic #67/#66 posts in #39 dated 2026-10-10 (capture day) — forum is active; re-capture recommended in a later loop.
