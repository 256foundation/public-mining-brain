# Source Registry

The persistent list of sources the update loops pull from. This is the contract between the brain and the outside world: registered sources get re-checked on their cadence; unregistered material still gets ingested, but won't be revisited automatically.

**Status: Draft v0.2 — pending gate review.** v0.2 integrates Tyler's seed list (256 Foundation, Hashrate Heatpunks, OSMU, Bitaxe ecosystems). Rows are never deleted; dead sources move to `dormant`/`dead`.

## Schema

| Column | Values |
|---|---|
| **ID** | kebab-case slug; referenced in raw file headers (`Registry ID:`) |
| **Source** | Human-readable name |
| **URL** | Root URL to monitor (`*` = capture-bot fed, see playbook Capture Layer) |
| **Type** | `site` · `docs` · `repo` · `data` · `report` · `filings` · `forum` · `chat` · `social` · `datasheet` · `podcast` · `video` · `wiki` · `book` |
| **Cadence** | How often the loop re-checks: `static` · `weekly` · `monthly` · `quarterly` · `annual` · `event` (bot-driven capture) |
| **Posture** | Capture rule: `verbatim` (full text in raw/) · `extract` (facts/tables with attribution) · `link-only` (metadata + link) |
| **Owner** | Who nominated it: `tyler` · `agent` · `community` |
| **Status** | `active` · `proposed` (not yet verified) · `dormant` · `dead` |

**Community-source rule:** public platforms (Discourse forums, X) may be captured `verbatim`. Gated chats (Telegram, Discord) default to `extract` — knowledge is pulled out with attribution to public handles, personal/private details stripped. Tyler can flip any specific source to `verbatim` at the gate.

---

## 256 Foundation & Project Sites

| ID | Source | URL | Type | Cadence | Posture | Owner | Status |
|---|---|---|---|---|---|---|---|
| `256f-site` | 256 Foundation site (mission, work, newsroom) | https://256foundation.org | site | weekly | verbatim | tyler | active |
| `256f-newsroom` | 256F newsroom (project updates) | https://256foundation.org/newsroom | site | weekly | verbatim | tyler | active |
| `256f-substack` | Assembling Freedom newsletter | https://256foundation.substack.com | site | monthly | verbatim | tyler | dormant |
| `256f-nostr` | 256F Nostr feed | https://primal.net/p/nprofile1qqsqhk42dz0exfcsln4yqmdkjys0nvd7dqndgacpsa7w7pt7njq2uuss2u9cq | social | weekly | extract | tyler | active |
| `hashdash` | Hashdash dashboard (dashboard only — do not scrape; live data via pool Prometheus API, contract in AGENT-PLAYBOOK) | https://dash.256f.org | data | weekly | link-only | tyler | active |
| `tyler-stevens-site` | Tyler Stevens content index (talks, podcasts, panels) | https://www.tylerstevens.me/content | site | monthly | extract | agent | proposed |
| `telehash` | Telehash solo-mining fundraiser events | https://256foundation.org/telehash | site | event | extract | tyler | active |
| `heatpunks-site` | Hashrate Heatpunks site (mission, education, summit archive) | https://www.heatpunks.org | site | weekly | verbatim | tyler | active |
| `osmu-wiki` | OSMU — Open Source Miners United wiki & project index | https://osmu.wiki | wiki | weekly | verbatim | tyler | active |

## Community & Forums

| ID | Source | URL | Type | Cadence | Posture | Owner | Status |
|---|---|---|---|---|---|---|---|
| `256f-forum` | 256 Foundation Discourse forum | https://forum.256foundation.org | forum | weekly | verbatim | tyler | active |
| `heatpunks-forum` | Hashrate Heatpunks Discourse forum | https://forum.heatpunks.org | forum | weekly | verbatim | tyler | active |
| `osmu-forum` | OSMU Discourse forum (General/Pools/Hardware; adjacent ecosystem, not a 256F deliverable; method: `/latest.json` + `/t/<id>.json`, read-only) | https://osmu.xyz | forum | weekly | verbatim | tyler | active |
| `256f-telegram` | 256F Telegram group — history export + live bot | `*` t.me/the256foundation | chat | event | extract | tyler | active |
| `heatpunks-telegram` | Heatpunks Telegram group — history export + live bot | `*` via heatpunks.org group chat | chat | event | extract | tyler | active |
| `osmu-discord` | OSMU Discord server — history export | `*` via osmu.wiki | chat | event | extract | tyler | active |
| `256f-x` | 256F X account — history export + live scrape | `*` https://x.com/256FOUNDATION | social | event | verbatim | tyler | active |
| `heatpunks-x` | Heatpunks X account — history export + live scrape | `*` https://x.com/HashHeatpunks (handle per heatpunks.org footer; @heatpunks-vs-@HashHeatpunks discrepancy parked for B3) | social | event | verbatim | tyler | active |

## Open-Source Projects (code as primary source)

Monitored via GitHub API: commits, releases, PRs, issues, discussions. Posture applies to derived material (release notes, README/docs) — `verbatim`; issue threads — `extract`.

| ID | Source | URL | Type | Cadence | Posture | Owner | Status |
|---|---|---|---|---|---|---|---|
| `mujina` | Mujina — open mining firmware (Rust, GPLv3) | https://github.com/256foundation/mujina | repo | weekly | verbatim | tyler | active |
| `mujina-mips` | Mujina Improvement Proposals | https://github.com/256foundation/mujina-mips | repo | weekly | verbatim | tyler | active |
| `hydrapool` | Hydrapool — open mining pool (AGPLv3) | https://github.com/256foundation/hydrapool | repo | weekly | verbatim | tyler | active |
| `asic-rs` | asic-rs — ASIC management (Antminer/Whatsminer/Avalon/Bitaxe...) | https://github.com/256foundation/asic-rs | repo | weekly | verbatim | tyler | active |
| `rhap-spec` | RHAP — Raw Hardware Access Protocol spec | https://github.com/256foundation/rhap | repo | weekly | verbatim | tyler | active |
| `rhapd-bitaxe` | RHAP device firmware for Bitaxe Gamma | https://github.com/256foundation/rhapd-bitaxe-gamma | repo | weekly | verbatim | tyler | active |
| `emberone-00-pcb` | Ember One/00 hashboard (KiCAD, CERN OHL) | https://github.com/256foundation/emberone00-pcb | repo | weekly | verbatim | tyler | active |
| `emberone-01-pcb` | Ember One/01 hashboard (Intel BZM2-based) | https://github.com/256foundation/emberone01-pcb | repo | weekly | verbatim | tyler | active |
| `emberone-usbserial-fw` | Ember One USB-serial firmware | https://github.com/256foundation/emberone-usbserial-fw | repo | weekly | verbatim | tyler | active |
| `libreboard` | Libre Board — open control board (CERN OHL) | https://github.com/256foundation/libreboard | repo | weekly | verbatim | tyler | active |
| `hashscope` | HashScope — pool behavior analysis (MITM proxy) | https://github.com/256foundation/HashScope | repo | weekly | verbatim | tyler | active |
| `btc-toolkit` | btc-toolkit — ASIC farm GUI manager (dormant since 2026-01-20; summarized into the asic-rs article) | https://github.com/256foundation/btc-toolkit | repo | weekly | verbatim | tyler | dormant |
| `esp-miner` | ESP-Miner / AxeOS — Bitaxe firmware | https://github.com/bitaxeorg/ESP-Miner | repo | weekly | verbatim | tyler | active |
| `bitaxe-hw` | Bitaxe hardware design files (bitaxeorg) | https://github.com/bitaxeorg | repo | weekly | verbatim | tyler | active |
| `osmu-projects` | OSMU project index (Open Source Miners United: NerdAxe, NerdMiner, AxeOS forks) | https://osmu.wiki | repo | weekly | verbatim | tyler | active |

## Silicon & Datasheets

| ID | Source | URL | Type | Cadence | Posture | Owner | Status |
|---|---|---|---|---|---|---|---|
| `tyler-datasheets` | Tyler's silicon datasheet collection (BM13xx, S19/S21 BMPs, Whatsminer, Seal chips, Intel BZM2...) | *provided files land in raw/inbox/* | datasheet | static | verbatim | tyler | active |
| `legitlist` | legitlist — community-vetted registry of legit Bitaxe units vs clones | https://github.com/bitaxeorg/legitlist | repo | weekly | verbatim | agent | proposed |
| `naja-duo` | Bitaxe Naja Duo — next-gen dual-chip prototype board | https://github.com/bitaxeorg/naja-duo | repo | event | verbatim | agent | proposed |
| `bitaxebirds` | BitaxeBIRDS — Intel BZM2 research board (docs, issues, PRs; upstream dormant, fully consumed per audit) | https://github.com/bitaxeorg/bitaxeBIRDS | repo | event | verbatim | agent | dormant |
| `block-watcher-site` | Block-Watcher website (256F org) | https://github.com/256foundation/Block-Watcher-website | repo | monthly | verbatim | agent | proposed |
| `public-datasheets` | Publicly circulated ASIC datasheets + teardown analyses | *URLs verified per document at ingest* | datasheet | monthly | extract | agent | proposed |

## Manufacturers & Hardware

| ID | Source | URL | Type | Cadence | Posture | Owner | Status |
|---|---|---|---|---|---|---|---|
| `bitmain-site` | Bitmain product pages & manuals | https://www.bitmain.com | site | monthly | verbatim | agent | active |
| `microbt-site` | MicroBT Whatsminer product pages | https://www.microbt.com | site | monthly | verbatim | agent | active |
| `canaan-site` | Canaan Avalon product pages | https://www.canaan.io | site | monthly | verbatim | agent | active |
| `bitdeer-sealminer` | Bitdeer SEALMINER (chips + rigs) | https://www.bitdeer.com/shop | site | monthly | verbatim | agent | active |
| `auradine-site` | Auradine Teraflux systems | https://auradine.com | site | monthly | verbatim | agent | active |
| `desiwe-miner` | DesiweMiner hardware (acquired by Bitdeer 2024-06 — $140M all-stock, FreeChain Inc.; standalone site defunct, reseller listings only; fold coverage into `bitdeer-sealminer` + a history note) | *site defunct — see bitdeer-sealminer* | datasheet | static | extract | agent | dormant |
| `asicminervalue` | ASIC Miner Value spec/profitability DB | https://www.asicminervalue.com | data | weekly | extract | agent | active |
| `miningnow` | MiningNow ASIC specs (cross-check) | https://miningnow.com | data | weekly | extract | agent | active |

## Firmware

| ID | Source | URL | Type | Cadence | Posture | Owner | Status |
|---|---|---|---|---|---|---|---|
| `braiins-os` | Braiins OS firmware + docs | https://braiins.com/os-firmware | docs | weekly | verbatim | agent | active |
| `luxos-docs` | LuxOS firmware docs (Luxor) | https://docs.luxor.tech/firmware/introduction-to-firmware | docs | weekly | verbatim | agent | active |
| `vnish-site` | Vnish firmware | https://vnish.com | site | weekly | verbatim | agent | active |
| `hashworks` | Hashworks firmware — PHANTOM: no firmware vendor by this name exists (HashWorks = 2022 mining hedge fund; hashworks.co = deadpooled Indian services firm) | *no vendor found* | site | static | extract | agent | dead |
| `cgminer-repo` | cgminer | https://github.com/ckolivas/cgminer | repo | monthly | verbatim | agent | active |
| `bfgminer-repo` | BFGMiner | https://github.com/luke-jr/bfgminer | repo | monthly | verbatim | agent | active |

## Mining Software & Farm Management

| ID | Source | URL | Type | Cadence | Posture | Owner | Status |
|---|---|---|---|---|---|---|---|
| `foreman-docs` | Foreman mine management (OBM) | https://foreman.mn | docs | monthly | verbatim | agent | active |
| `foreman-api` | Foreman API knowledge base | https://support.foreman.mn | docs | monthly | verbatim | agent | active |
| `braiins-manager` | Braiins Manager site control | https://braiins.com/manager | site | monthly | verbatim | agent | active |
| `luxor-commander` | Luxor Commander fleet software | https://luxor.tech/commander | site | monthly | verbatim | agent | active |
| `awesome-miner` | Awesome Miner | https://www.awesomeminer.com | site | monthly | extract | agent | active |
| `simplemining` | SimpleMining OS | https://simplemining.net | site | monthly | extract | agent | active |
| `nicehash` | NiceHash marketplace | https://www.nicehash.com | site | monthly | extract | agent | active |

## Pools

| ID | Source | URL | Type | Cadence | Posture | Owner | Status |
|---|---|---|---|---|---|---|---|
| `256f-hydrapool` | Hydrapool 256F instance (pool.256foundation.org) | https://pool.256foundation.org | site | monthly | verbatim | tyler | active |
| `braiins-pool` | Braiins Pool (since 2010) | https://braiins.com/pool | site | monthly | verbatim | agent | active |
| `foundry-pool` | Foundry USA Pool | https://foundrydigital.com | site | monthly | verbatim | agent | active |
| `f2pool` | F2Pool | https://www.f2pool.com | site | monthly | verbatim | agent | active |
| `antpool` | Antpool (Bitmain) | https://www.antpool.com | site | monthly | verbatim | agent | active |
| `viabtc` | ViaBTC | https://www.viabtc.com | site | monthly | verbatim | agent | active |
| `ocean-pool` | OCEAN (decentralized, DATUM) | https://ocean.xyz | site | monthly | verbatim | agent | active |
| `mara-pool` | MARA Pool | https://marapool.com | site | monthly | verbatim | agent | active |
| `poolin` | Poolin | https://www.poolin.me | site | monthly | verbatim | agent | active |
| `btccom-pool` | BTC.com Pool | https://pool.btc.com | site | monthly | verbatim | agent | active |
| `spiderpool` | SpiderPool | https://www.spiderpool.com | site | monthly | extract | agent | active |
| `secpool` | SECPOOL | https://www.secpool.com | site | monthly | extract | agent | active |
| `luxor-pool` | Luxor Pool | https://luxor.tech/mining | site | monthly | verbatim | agent | active |
| `public-pool` | Public Pool (solo/hobbyist) | https://web.public-pool.io | site | monthly | verbatim | agent | active |
| `ckpool` | ckpool / solo.ckpool.org | https://github.com/ckolivas/ckpool | repo | static | verbatim | agent | active |
| `binance-pool` | Binance Pool | https://pool.binance.com | site | monthly | verbatim | agent | active |

## Protocols & Standards

| ID | Source | URL | Type | Cadence | Posture | Owner | Status |
|---|---|---|---|---|---|---|---|
| `stratum-v2` | Stratum V2 protocol + spec repo | https://stratumprotocol.org | docs | weekly | verbatim | agent | active |
| `sv2-repo` | stratum-mining/sv2 implementation | https://github.com/stratum-mining/sv2 | repo | weekly | verbatim | agent | active |
| `bip-22-23` | BIP 22/23 getblocktemplate | https://github.com/bitcoin/bips | repo | static | verbatim | agent | active |
| `bip-310` | BIP 310 Stratum extensions | https://github.com/bitcoin/bips/blob/master/bip-0310.mediawiki | repo | static | verbatim | agent | active |
| `bitcoin-core` | Bitcoin Core (node/template source) | https://github.com/bitcoin/bitcoin | repo | monthly | extract | agent | active |
| `mempool-space` | Mempool.space network/pool stats | https://mempool.space | data | weekly | extract | agent | active |
| `betterhash` | BetterHash — Matt Corallo's draft BIP (absorbed into Stratum V2; the "(Fromknecht)" attribution is wrong, no Fromknecht whitepaper found; canonical text in TheBlueMatt/bips — locate exact branch/path via GitHub API at capture) | https://github.com/TheBlueMatt/bips | report | static | verbatim | agent | active |
| `braidpool` | Braidpool — P2P pool with hashrate futures (dev branch daily; pre-testnet) | https://github.com/braidpool/braidpool | repo | monthly | verbatim | agent | active |
| `p2pool-v2` | P2Poolv2 — P2P pool reboot (pool2win; live public testnet4 pool; Hydrapool deployment mode in README) | https://github.com/pool2win/p2pool-v2 | repo | monthly | verbatim | agent | active |
| `blitz-pool` | Blitz Pool — non-custodial SV1+SV2 solo/PPLNS pool (multi-output coinbase; hobbyist scale) | https://blitzpool.yourdevice.ch | site | monthly | extract | agent | active |
| `stratum-work` | stratum.work — live stratum visualizer + source | https://stratum.work · https://github.com/bboerst/stratum-work | site | monthly | extract | agent | active |

## Economics, Data & Research

| ID | Source | URL | Type | Cadence | Posture | Owner | Status |
|---|---|---|---|---|---|---|---|
| `braiins-insights` | Braiins mining dashboard + calc | https://insights.braiins.com | data | weekly | extract | agent | active |
| `hashrate-index` | Hashrate Index (Luxor) data + research | https://hashrateindex.com | data | weekly | extract | agent | active |
| `hashprice-docs` | Hashprice index methodology | https://docs.luxor.tech/hashrateindex/hashprice | docs | static | verbatim | agent | active |
| `cbeci` | Cambridge CBECI consumption index | https://ccaf.io/cbnsi/cbeci | data | monthly | extract | agent | active |
| `cbeci-methodology` | CBECI methodology pages | https://ccaf.io/cbnsi/cbeci/methodology | docs | static | verbatim | agent | active |
| `cambridge-report` | Cambridge Digital Mining Industry Report | https://www.jbs.cam.ac.uk (2025 report PDF) | report | annual | verbatim | agent | active |
| `minermag` | TheMinerMag news + public-miner stats | https://theminermag.com | data | weekly | extract | agent | active |
| `whattomine` | WhatToMine profitability calc | https://whattomine.com | data | weekly | extract | agent | active |
| `galaxy-research` | Galaxy mining research | https://www.galaxy.com/research/ | report | monthly | extract | agent | active |
| `coinshares-research` | CoinShares mining reports | https://www.coinshares.com/research | report | monthly | extract | agent | active |
| `elektronics-dev` | Rapha Zagury's curated mining data (dataset "coming soon") | https://elektronics.dev/about | data | event | link-only | agent | active |

## Industry & Public Miners

| ID | Source | URL | Type | Cadence | Posture | Owner | Status |
|---|---|---|---|---|---|---|---|
| `sec-edgar-miners` | SEC EDGAR: MARA, RIOT, CLSK, CORZ, HUT, IREN, WULF, BTDR filings | https://www.sec.gov/edgar | filings | quarterly | extract | agent | active |
| `mara-ir` | MARA Holdings investor news | https://ir.mara.com | filings | quarterly | verbatim | agent | active |
| `crusoe` | Crusoe (flared gas / wasted energy) | https://www.crusoe.ai | site | monthly | extract | agent | active |
| `upstream-data` | Upstream Data (BlackBox, field gas) | https://www.upstreamdata.ca | site | monthly | extract | agent | active |
| `giga-energy` | Giga Energy (mining containers + blog; pivoted to AI energy infra, mining container + blog content active) | https://www.gigaenergy.com | site | monthly | extract | agent | active |
| `exergy-docs` | Exergy hashrate-heating & solar docs | https://docs.exergyheat.com | docs | monthly | verbatim | agent | proposed |
| `exergy-calculators` | Exergy calculator source (heating + solar monetization math) | https://github.com/exergyheat/webapp-calculators | repo | monthly | verbatim | agent | proposed |
| `exergy-forum` | Exergy customer community (verify public Discourse at capture; else extract) | https://support.exergyheat.com | forum | weekly | verbatim | agent | proposed |

## History & Reference

| ID | Source | URL | Type | Cadence | Posture | Owner | Status |
|---|---|---|---|---|---|---|---|
| `bitcoin-wiki` | Bitcoin wiki (Mining, hardware comparison) | https://en.bitcoin.it/wiki/Mining | wiki | static | verbatim | agent | active |
| `bitcoinbook` | Mastering Bitcoin (open source, mining ch.) | https://github.com/bitcoinbook/bitcoinbook | book | static | extract | agent | active |
| `braiins-books` | Braiins Publishing mining books (Handbook, Economics, Glossary, Ultimate Guide, Heat Reuse) — free PDFs; Glossary/Ultimate PDFs are email-gated at braiins.com; Heat Reuse (Tyler Stevens, 2025, ISBN 978-80-909253-2-8, foreword by Paul Jin Li) distributed free at braiins.com/books/bitcoin-mining-heat-reuse — ingested from the author's final per-chapter production PDFs | https://braiins.com/books | book | static | extract | agent | active |
| `learnmeabitcoin` | Learn Me A Bitcoin — technical mining pages | https://learnmeabitcoin.com/technical/mining/ | docs | static | verbatim | agent | active |
| `bitcointalk-mining` | Bitcointalk mining boards | https://bitcointalk.org | forum | weekly | extract | agent | active |
| `bitcoin-se` | Bitcoin Stack Exchange (mining tags) | https://bitcoin.stackexchange.com | forum | weekly | extract | agent | active |

## Podcasts & Video (transcript posture)

| ID | Source | URL | Type | Cadence | Posture | Owner | Status |
|---|---|---|---|---|---|---|---|
| `pod256` | POD256 — 256F podcast (127+ eps, weekly) | https://www.pod256.org | podcast | weekly | extract | tyler | active |
| `luxos-video-demo` | LuxOS full walkthrough (install→optimize) | https://www.youtube.com/watch?v=ivHBlP3duRg | video | static | extract | agent | active |
| `mining-pod` | The Mining Pod (Blockspace Media, not Blockworks — ~486 eps 2021–2026; paused 2026-01; content moved to The Blockspace Podcast) | *paused — see blockspace-podcast* | podcast | static | extract | agent | dormant |
| `brainstorm-pod` | Braiins podcast feed (no "Brainstorm" show found — ID kept, low priority, low cadence) | https://podcasts.apple.com/us/podcast/braiins/id1726335273 | podcast | monthly | extract | agent | active |
| `blockspace-podcast` | The Blockspace Podcast (successor to The Mining Pod) | https://podcasts.apple.com/us/podcast/the-blockspace-podcast/id1729672815 | podcast | weekly | extract | agent | active |
| `heatpunk-summit-2025` | Undermine Summit 2025 archive talks (14 recorded talks + YouTube playlist; HPS 2026 archive also exists — covered via A3) | https://www.heatpunks.org/summit/2025 | video | event | extract | agent | active |

---

## Proposed but unverified (queue)

The 2026-10-10 verification pass (capture-loop A0) promoted the four queue entries below into the category tables above — IDs preserved, rows never deleted:

- `desiwe-miner` → Manufacturers & Hardware (`dormant` — acquired by Bitdeer 2024-06, standalone site defunct)
- `giga-energy` → Industry & Public Miners (`active` — URL verified live)
- `hashworks` → Firmware (`dead` — phantom, no such firmware vendor)
- `heatpunk-summit-2025` → Podcasts & Video (`active`, cadence `event` — 14 recorded talks verified)

## Notes on Tyler's seed list (integrated above)

- Telegram/Discord/X **history exports** land in `raw/inbox/` and are triaged like any source; **live bots** (TG watchers, X scraper, GitHub monitors) feed the same pipeline — contract documented in `automation/AGENT-PLAYBOOK.md` → Capture Layer.
- Gated chats default to `extract` posture for PII hygiene; flip any source to `verbatim` at the gate if the community is comfortable.
- NDA'd silicon datasheets: verify redistribution rights per document; NDA'd ones stay `link-only` or out of the public repo.
- **Book-source rule** (Tyler, 2026-10-10): books → `extract` posture. Key information and learnings with chapter attribution + link to the freely distributed PDF. No full-text dumps; extract files in raw/ must carry the exact literals the article cites (grounding invariant still applies). Flip a specific book to verbatim only if load-bearing.
- **No-massive-data rule** (Tyler, 2026-10-10): the wiki holds key information and pointers, not massive datasets or thousands of lines of source code. Live data endpoints get `link-only` registry rows + a pointer cite in affected articles + one row in `meta/data-resources.md`.
- **Specs-not-prices rule** (Tyler, 2026-10-11): ASIC miners trade like commodities — machine prices churn constantly and are not wiki knowledge. Machine articles exist for the detailed spec sheet (hashrate, power on wall, efficiency, electrical, thermal, acoustic, form factor, cooling-class measurement conventions); the completeness goal is **every current-gen SKU in each manufacturer's live catalog**. Prices appear only as dated As-Of evidence inside a captured sheet row or a Disputed block — never as a wiki claim or headline, and never refreshed as a maintenance task. Prior-gen SKUs stay out unless load-bearing.
