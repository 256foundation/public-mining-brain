# Source Registry

The persistent list of sources the update loops pull from. This is the contract between the brain and the outside world: registered sources get re-checked on their cadence; unregistered material still gets ingested, but won't be revisited automatically.

**Status: Draft v0.1 — pending gate review.** Tyler's curated sources get added as provided. Rows are never deleted; dead sources move to `dormant`/`dead`.

## Schema

| Column | Values |
|---|---|
| **ID** | kebab-case slug; referenced in raw file headers (`Registry ID:`) |
| **Source** | Human-readable name |
| **URL** | Root URL to monitor |
| **Type** | `site` · `docs` · `repo` · `data` · `report` · `filings` · `forum` · `video` · `wiki` · `book` |
| **Cadence** | How often the loop re-checks: `static` · `weekly` · `monthly` · `quarterly` · `annual` · `event` |
| **Posture** | Capture rule: `verbatim` (full text in raw/) · `extract` (facts/tables with attribution) · `link-only` (metadata + link) |
| **Owner** | Who nominated it: `tyler` · `agent` · `community` |
| **Status** | `active` · `proposed` (not yet verified) · `dormant` · `dead` |

---

## Manufacturers & Hardware

| ID | Source | URL | Type | Cadence | Posture | Owner | Status |
|---|---|---|---|---|---|---|---|
| `bitmain-site` | Bitmain product pages & manuals | https://www.bitmain.com | site | monthly | verbatim | agent | active |
| `microbt-site` | MicroBT Whatsminer product pages | https://www.microbt.com | site | monthly | verbatim | agent | active |
| `canaan-site` | Canaan Avalon product pages | https://www.canaan.io | site | monthly | verbatim | agent | active |
| `bitdeer-sealminer` | Bitdeer SEALMINER (chips + rigs) | https://www.bitdeer.com/shop | site | monthly | verbatim | agent | active |
| `auradine-site` | Auradine Teraflux systems | https://auradine.com | site | monthly | verbatim | agent | active |
| `asicminervalue` | ASIC Miner Value spec/profitability DB | https://www.asicminervalue.com | data | weekly | extract | agent | active |
| `miningnow` | MiningNow ASIC specs (cross-check) | https://miningnow.com | data | weekly | extract | agent | active |

## Firmware

| ID | Source | URL | Type | Cadence | Posture | Owner | Status |
|---|---|---|---|---|---|---|---|
| `braiins-os` | Braiins OS firmware + docs | https://braiins.com/os-firmware | docs | weekly | verbatim | agent | active |
| `luxos-docs` | LuxOS firmware docs (Luxor) | https://docs.luxor.tech/firmware/introduction-to-firmware | docs | weekly | verbatim | agent | active |
| `vnish-site` | Vnish firmware | https://vnish.com | site | weekly | verbatim | agent | active |
| `cgminer-repo` | cgminer (Ckolas) | https://github.com/ckolivas/cgminer | repo | monthly | verbatim | agent | active |
| `bfgminer-repo` | BFGMiner (luke-jr) | https://github.com/luke-jr/bfgminer | repo | monthly | verbatim | agent | active |

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
| `braiins-pool` | Braiins Pool (since 2010) | https://braiins.com/pool | site | monthly | verbatim | agent | active |
| `foundry-pool` | Foundry USA Pool | https://foundrydigital.com | site | monthly | verbatim | agent | active |
| `f2pool` | F2Pool | https://www.f2pool.com | site | monthly | verbatim | agent | active |
| `antpool` | Antpool (Bitmain) | https://www.antpool.com | site | monthly | verbatim | agent | active |
| `viabtc` | ViaBTC | https://www.viabtc.com | site | monthly | verbatim | agent | active |
| `ocean-pool` | OCEAN (decentralized, DATUM) | https://ocean.xyz | site | monthly | verbatim | agent | active |
| `mara-pool` | MARA Pool | https://marapool.com | site | monthly | verbatim | agent | active |
| `poolin` | Poolin | https://www.poolin.me | site | monthly | verbatim | agent | active |
| `btccom-pool` | BTC.com Pool | https://pool.btc.com | site | monthly | verbatim | agent | active |
| `spiderpool` | SpiderPool | https://www.spiderpool.com | site | monthly | extract | agent | proposed |
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
| `betterhash` | BetterHash whitepaper (Fromknecht) | *URL to verify at ingest* | report | static | verbatim | agent | proposed |

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
| `galaxy-research` | Galaxy mining research | https://www.galaxy.com/research/ | report | monthly | extract | agent | proposed |
| `coinshares-research` | CoinShares mining reports | https://www.coinshares.com/research | report | monthly | extract | agent | proposed |

## Industry & Public Miners

| ID | Source | URL | Type | Cadence | Posture | Owner | Status |
|---|---|---|---|---|---|---|---|
| `sec-edgar-miners` | SEC EDGAR: MARA, RIOT, CLSK, CORZ, HUT, IREN, WULF, BTDR filings | https://www.sec.gov/edgar | filings | quarterly | extract | agent | active |
| `mara-ir` | MARA Holdings investor news | https://ir.mara.com | filings | quarterly | verbatim | agent | active |
| `crusoe` | Crusoe (flared gas / wasted energy) | https://www.crusoe.ai | site | monthly | extract | agent | active |
| `upstream-data` | Upstream Data (BlackBox, field gas) | https://www.upstreamdata.ca | site | monthly | extract | agent | active |

## History & Reference

| ID | Source | URL | Type | Cadence | Posture | Owner | Status |
|---|---|---|---|---|---|---|---|
| `bitcoin-wiki` | Bitcoin wiki (Mining, hardware comparison) | https://en.bitcoin.it/wiki/Mining | wiki | static | verbatim | agent | active |
| `bitcoinbook` | Mastering Bitcoin (open source, mining ch.) | https://github.com/bitcoinbook/bitcoinbook | book | static | verbatim | agent | active |
| `bitcointalk-mining` | Bitcointalk mining boards | https://bitcointalk.org | forum | weekly | extract | agent | active |
| `bitcoin-se` | Bitcoin Stack Exchange (mining tags) | https://bitcoin.stackexchange.com | forum | weekly | extract | agent | active |

## Video & Audio (transcript posture)

| ID | Source | URL | Type | Cadence | Posture | Owner | Status |
|---|---|---|---|---|---|---|---|
| `luxos-video-demo` | LuxOS full walkthrough (install→optimize) | https://www.youtube.com/watch?v=ivHBlP3duRg | video | static | extract | agent | active |
| `mining-pod` | The Mining Pod (Blockworks) | *URL to verify at ingest* | video | weekly | extract | agent | proposed |
| `brainstorm-pod` | Brainstorm podcast (Braiins) | *URL to verify at ingest* | video | weekly | extract | agent | proposed |

---

## Proposed but unverified (queue)

| ID | Source | Why | Status |
|---|---|---|---|
| `desiwe-miner` | DesiweMiner hardware | newer ASIC vendor | proposed |
| `giga-energy` | Giga Energy (gas mining) | energy interplay | proposed |
| `hashworks` | Hashworks firmware | firmware landscape | proposed |

## Tyler's seed list

*(to be added — curated sources provided by Tyler land here first, then get rows above)*
