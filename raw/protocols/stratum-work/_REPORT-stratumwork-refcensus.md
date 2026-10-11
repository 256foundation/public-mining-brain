# REPORT — phase A12 reference sweep (stratum-work / Delving / Optech / arXiv)

> Collected: 2026-10-10 · Agent: stratumwork-refcensus · Postures: EXTRACT (stratum.work, Delving, Optech) + VERBATIM abstract (arXiv)
> All files under raw/protocols/stratum-work/, raw/protocols/reference-census/, raw/industry/arxiv/ only.

## Files delivered (6 captures + this report)

| # | File | Source | HTTP | Bytes | Posture | Status |
|---|---|---|---|---|---|---|
| 1 | stratum-work/stratum-work-homepage--extract.md | https://stratum.work/ | 200 | 26,725 HTML | extract (static SSR text) | OK |
| 2 | stratum-work/bboerst-stratum-work-readme--verbatim.md | raw.githubusercontent.com/bboerst/stratum-work/**main**/README.md | 200 | 9,034 | verbatim (byte-exact) | OK |
| 3 | reference-census/delving-bitcoin-mining-topics--census.md | delvingbitcoin.org /tag/mining, /tag/mining-pools, /tag/stratum-v2 (.json) | 200 ×3 | n/a (JSON) | extract (census) | OK (see discovery) |
| 4 | reference-census/optech-topic-pooled-mining--extract.md | bitcoinops.org/en/topics/pooled-mining/ | 200 | 7,915 HTML | extract | OK |
| 5 | reference-census/optech-topic-selfish-mining--extract.md | bitcoinops.org/en/topics/selfish-mining/ | 200 | 3,366 HTML | extract | OK |
| 6 | industry/arxiv/2605.03770-firmware-distribution-attack-surface--abstract-verbatim.md | arxiv.org/abs/2605.03770 | 200 | 43,393 HTML | verbatim (title/authors/abstract/dates) | OK |

## 1. stratum.work + bboerst/stratum-work (registry `stratum-work`)

- **SSR assessment:** NOT a JS shell. Next.js statically prerendered (`x-powered-by: Next.js`, `x-nextjs-prerender: 1`, `x-nextjs-cache: HIT`); 26,725-byte HTML contains real static chrome (nav, table column headers, timing legend). Live job rows are absent (empty `<tbody>`, placeholders "Waiting for new stratum messages..." / "Disconnected" with title "Disconnected from data stream") — the stream is websocket/SSE client-side, per mission parked; static marketing/about text captured instead.
- **First fetch attempt returned exit 56 / 10 bytes (transient connection reset); retry succeeded — status above is from the successful retry.**
- **Key literals:** meta description: "Web app that streams realtime mining pool stratum v1 messages to a table." — nav: Table ("Main view with table and timing chart"), Timing ("Full screen pool timing visualization"), Sankey ("Sankey diagram visualization"), Infra ("Realtime Stratum infrastructure metrics") — table columns include **BIP-110** — timing legend: Core Fields A/M/C/P/H/V/N/E, Transaction Fields X/L/I/W/U/K/J, OP_RETURN protocols R̶ RSK, C̶ CoreDAO, S̶ Syscoin, H̶ Hathor, E̶ ExSat, O̶ Omni, U̶ Runestone, W̶ WitnessCommitment, T̶ Stacks, B̶ BIP47, Ø̶ empty, Ω̶ other.
- **Repo (GitHub API, verified):** default branch is **main** (mission guessed master — raw master/README.md would 404); description "Web app that streams realtime mining pool stratum messages to a table."; TypeScript; 48 stars / 10 forks; GitHub Pages enabled; homepage https://stratum.work; created 2024-05-28; last push 2026-10-06.
- **How it connects to pools (README verbatim file):** Collector instances dial pools via `stratum+tcp://…:3333` (`--pool-name/--url/--userpass`), capture `mining.notify` → MongoDB + RabbitMQ; backend identifies pool per block via coinbase analysis; web app streams to browser; **all decoding/visualization client-side ("trustless data processing")**; raw feed at `GET /api/stream` (SSE). Idea credited to 0xB10C's primal.net thread.
- **Parks:** live mining.notify stream; /timing, /sankey, /infra subpages; historical API.

## 2. Delving Bitcoin mining census (delving-bitcoin, unregistered, handoff-approved)

- **Discovery:** **No `/c/mining/` category exists** (`/c/mining/l/latest.json` → 404; `/categories.json` shows only Implementation 226 / Protocol Design 326 / Economics 14 / Philosophy 26 / Meta 19). Mining is tracked by **tags**. Census built from tags: **#mining (10 topics, complete), #mining-pools (6), #stratum-v2 (5) → 14 unique topics** (mission hoped ~20; the tag simply has this many — nothing omitted).
- **Key literals (top engagement):** "P2share: how to turn any network (or testnet!) into a bitcoin miner" (ID 2093, 27 replies, 986 views, 2025-11-07); "Analyzing Mining Pool Behavior to Address Bitcoin Core's Double Coinbase Reservation Issue" (ID 1351, 16 likes); "[Research] A clockless vardiff strands a slowing miner" (ID 2718, 10 likes); "SV2 Extensions for Payout Verification and Job Size at Scale" (2805) + "New Extension Proposal for Stratum V2" (2809), both 2026-08-14; "Stratum v2 Noise Protocol: BIP324 nuggets?" (413, 2024-01-15).
- Discourse JSON API (clean SSR-adjacent structured data) used for the census; site itself is SSR.

## 3. Bitcoin Optech mining topics (optech, unregistered, handoff-approved)

- `/en/topics/mining/` → **404**; `/en/topics/stratum-v2/` → **404**; `llms.txt` → 404; sitemap.xml contains 0 `<loc>` entries. Verified against the full topics index (https://bitcoinops.org/en/topics/ — 158 topics, fully SSR static Jekyll): no generic mining topic, no stratum-v2 topic. Mining-adjacent topics that DO exist: pooled-mining, selfish-mining, block-withholding, asicboost, difficulty-adjustment-algorithms, time-warp.
- Captured the two core mining topic pages (2 files, within the 1–2 spec): **pooled-mining** (subtitle "Also covering Betterhash, Braidpool, Stratum, and Stratum v2" — 29 "stratum" occurrences; full protocol history verbatim: getwork → GBT (BIPs 22/23) → Stratum v1 (<200 bytes/job, no member validation, "BIPs 40 and 41 were reserved for Stratum v1, documentation for them has never been provided") → Betterhash → Stratum v2 → BraidPool; payout schemes PPS/FPPS/PPLNS/TIDES; 23 newsletter mentions 2018→2026-09-18) and **selfish-mining** (1/3-threshold narrative, 6 mentions).
- **Direct evidence found for the wiki handoff:** the pooled-mining page's newsletter list includes "2024-07-19 — Stratum.work website with real-time visualization of Stratum messages from several mining pools" (`/en/newsletters/2024/07/19/#real-time-stratum-visualization-tool-released`) — the Optech primary source behind the 256F newsletters' secondhand citation.
- Optech = full SSR static HTML on every page fetched; no JS-shell issues.

## 4. arXiv 2605.03770 (arxiv-firmware)

- **ID was correct** (no 404, no search needed). Title verbatim: "Firmware Distribution as Attack Surface: A Security Study of ASIC Cryptocurrency Miners". Authors: Pierre Pouliquen, Hadrien Barral, David Naccache, Thibaut Heckmann, Antoine Houssais. v1 Tue 5 May 2026 14:00:54 UTC; v2 Wed 6 May 2026. cs.CR + cs.SE. "20 pages, 7 figures. Submitted to a security conference."
- Abstract captured verbatim (both `citation_abstract` meta and visible blockquote match). Stratum-relevant literal: vulnerabilities "including firmware phishing and the exploitation of miners still operating over **Stratum V1**"; 134 firmware images across Bitmain, MicroBT, Canaan, Iceriver (>99% of deployed miners).
- arxiv.org abstract page: fully SSR.

## Parks (honest list)

1. stratum.work live websocket/SSE job data and the Timing/Sankey/Infra views — websocket/JS-delivered; only static text captured (per mission instruction).
2. Delving topic bodies (OP posts + replies) — census-only posture; fetchable per-topic via `/t/<id>.json` when needed.
3. Optech: no stratum-v2 topic page to capture (404, confirmed against 158-topic index); other mining-adjacent topic pages (block-withholding, asicboost, difficulty-adjustment-algorithms, time-warp) not captured — out of scope.
4. Optech llms.txt absent; sitemap.xml empty of URLs — topic discovery done via the rendered topics index instead.
5. Views/likes fields for Delving topics outside the #mining listing — not fetched (only #mining page carries them).

## Notes for wiki integration

- wiki/protocols/stratum-in-practice.md can now cite bboerst/stratum-work directly (README verbatim + homepage + Optech 2024-07-19 newsletter item) instead of secondhand via 256F newsletters.
- Delving mining content must be cited by tag, not category — there is no mining category to link.
