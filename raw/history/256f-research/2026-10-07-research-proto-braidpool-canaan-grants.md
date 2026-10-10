# Research: Proto, Braidpool, Canaan open-source, OpenSats/HRF grants (2026-10-07)

> Source: GitHub API + web research (URLs/commands per section)
> Collected: 2026-10-07
> Published: various

## Proto

**Searches run (exact):**
- `gh api orgs/proto` → **404 Not Found**
- `gh api orgs/protoxyz` → exists but is **"Protocol" (pxyz.dev)**, an unrelated app-development tools company (13 public repos, created 2023-01-20). Not Block's Proto.
- `gh api orgs/proto-mining` → **404**; `gh api orgs/protomining` → **404**
- `gh api "search/users?q=proto+type:org"` → 30 orgs; only relevant hit: **`proto-at-block`** (name "Proto", twitter @Bitkeyofficial, created 2023-10-23, 2 public repos: `proto-at-block/bitkey` 223★/42 forks, `proto-at-block/sparrow` 7★/0 forks — Bitkey self-custody **wallet** org, **no mining repos**)
- `gh api "search/repositories?q=proto+rig+OR+proto+mining+in:name,description&per_page=20"` → relevant hits: `block/proto-fleet`, `proto-sdk/proto-api-docs`
- `gh api "search/repositories?q=org:block+mining"` + full `orgs/block/repos?per_page=100` name scan → **`block/proto-fleet` is the only mining-related repo in Block's org**
- Websearch ("Proto Block bitcoin mining proto.xyz open source github Proto Fleet") → proto.xyz Fleet product page links to github.com/block/proto-fleet; Proto blog announcement dated 2025-08-13

**Findings:**

- **YES — Proto has public open-source presence, hosted under Block's org:**
  - **`block/proto-fleet`** — "Proto Fleet. Mining management software. Evolved."
    - created 2026-03-26 | pushed 2026-10-07 (actively developed, pushed day of collection)
    - 56 stars | 16 forks | 16 contributors (via `Link:` header `page=16; rel="last"`)
    - License: Apache-2.0 | homepage: https://docs.proto.xyz
    - https://github.com/block/proto-fleet
    - Announced 2025-08-13 in "Proto Rig and Proto Fleet: A paradigm shift in bitcoin mining" (https://proto.xyz/blog/posts/proto-rig-and-proto-fleet-a-paradigm-shift); described as "free, open-source fleet management software, being built in the open on GitHub" (@BitcoinatBlock on X). proto.xyz/products/fleet: "Open source. No fees. Full control."
- **`proto-sdk/proto-api-docs`** — "Interactive API documentation for the Proto mining device" — created 2025-09-20 | pushed 2026-02-26 | 0★/0 forks. Owner `proto-sdk` is a **user** account (display name "Osmosis", account created 2024-12-18), **not** an official org — affiliation with Proto unconfirmed, likely third-party. https://github.com/proto-sdk/proto-api-docs
- **None found:** no GitHub org named proto / protoxyz (Block's) / proto-mining / protomining; no Proto Rig hardware-design (schematic/PCB/firmware) repo found under Block or elsewhere — Fleet software is the only official Proto open-source release located.

## Braidpool

Search: `gh api "search/repositories?q=braidpool&per_page=10"` + `gh api orgs/braidpool` + `orgs/braidpool/repos?per_page=100` (org created 2023-09-08, 19 public repos).

| repo | created | pushed | stars | forks | contributors |
|---|---|---|---|---|---|
| **braidpool/braidpool** | 2021-02-09 | 2026-09-30 | 147 | 108 | **14** (Link header `page=14; rel="last"`) |
| pool2win/braidpool (original repo, cited in OpenSats Feb-2024 grant) | 2024-01-25 | 2024-07-17 | 8 | 4 | — |

- Main repo: https://github.com/braidpool/braidpool — "a scalable peer to peer bitcoin mining pool with support for hashrate futures"; license AGPL-3.0; topics: bitcoin, bitcoin-mining, frost, p2pool. Activity has moved from `pool2win/braidpool` to the `braidpool` org.
- Other org repos (mostly forks/aux, low stars): `braidpool/stratum` (pushed 2026-09-03), `braidpool/cpuminer` (2025-09-01), `braidpool/rust_cpunet_miner` (3★, pushed 2026-07-13), `braidpool/sv2-apps` (Stratum V2 pool/miner apps, 2026-05-01, pushed 2026-09-03), `braidpool/ckpool` (unofficial clone), forks of `bitcoin`, `rust-bitcoin`, `rust-bech32`, plus assorted AI-experiment repos.
- Funded by OpenSats (Feb 2024) and HRF (Jan 2026 round) — see Grants section.

## Canaan canaan-creative

Search: `gh api orgs/canaan-creative` (Canaan.io, "ASIC", org created 2012-01-24, 26 public repos, blog https://canaan.io) + `orgs/canaan-creative/repos?per_page=100`.

Top 10 by stars:

| repo | created | pushed | stars | forks |
|---|---|---|---|---|
| Canaan-Creative/cgminer | 2013-03-28 | 2019-07-01 | 49 | 42 |
| Canaan-Creative/cgminer-openwrt-packages | 2013-01-29 | 2019-06-25 | 48 | 69 |
| Canaan-Creative/Avalon_Nano3s | 2025-01-23 | 2025-01-23 | 43 | 10 |
| Canaan-Creative/Avalon-extras | 2013-01-29 | 2019-05-13 | 31 | 41 |
| Canaan-Creative/MM | 2013-04-08 | 2024-12-05 | 30 | 23 |
| Canaan-Creative/luci | 2013-01-29 | 2019-04-04 | 18 | 29 |
| Canaan-Creative/Avalon-Management-System | 2014-08-14 | 2019-02-22 | 14 | 20 |
| Canaan-Creative/avalon10-docs | 2019-09-02 | 2020-03-02 | 12 | 12 |
| Canaan-Creative/avalon7-docs | 2016-08-23 | 2017-03-23 | 9 | 10 |
| Canaan-Creative/Avalon-nano | 2014-02-18 | 2017-08-28 | 8 | 10 |

- Incumbent-manufacturer open-source history: Canaan open-sourced its Avalon stack from **2013** (cgminer fork, OpenWrt packages, web GUI, Avalon-extras, Miner Manager) — the earliest/first ASIC maker to ship open firmware. Most repos dormant since ~2019.
- **Recent activity resumed 2024-12 → 2025:** `MM` pushed 2024-12-05; new repos `Avalon_Nano3s` (2025-01-23), `avalon_family` (2025-09-23, pushed 2025-09-24, 6★/2 forks), `Avalon_mm` (2025-10-30, pushed 2025-11-05, 5★/4 forks) — aligning with the open-sourced Avalon Nano 3/3S home-miner line.
- Also in org: `avalon6/7/8/9/10-docs` developer documentation series, `Avalon-USB-converter`, `fms`/`fms-core` (firmware management), OpenWrt archives.

## Grants

Searches: websearch "OpenSats grant Bitaxe open source mining announcement", "HRF Bitcoin Development Fund grant mining Bitaxe/Braidpool/256 Foundation"; direct fetches of OpenSats blog waves 4, 11, 12, 16 and HRF press release pages; https://opensats.org/projects/bitaxe.

**OpenSats (General Fund, project grants):**

1. **2024-02-25 — Fourth Wave of Bitcoin Grants** — https://opensats.org/blog/bitcoin-grants-feb-2024
   - **The Bitaxe** — first ASIC bitcoin miner in ~a decade with fully open-source hardware + firmware; repo skot/bitaxe (GPL-3.0). First OpenSats support for Bitaxe.
   - **Braidpool** — decentralized P2P bitcoin mining pool (Schnorr/Taproot); repo pool2win/braidpool (MIT).
2. **2025-05-14 — Eleventh Wave of Bitcoin Grants** — https://opensats.org/blog/eleventh-wave-of-bitcoin-grants
   - **BitShoka** (kuenrg153/bitshoka; GPL v3 & CERN OHL S v2) — reverse-engineering MicroBT KF1950 ASIC protocol, integrating into bitaxeorg/ESP-Miner, producing a MicroBT-based BitAxe variant; notes Kenya BitAxe assembly since Dec 2024.
   - **256 Foundation** — fully open-source Bitcoin mining stack: Ember One hashboard, Mujina Mining Firmware, Libre Board, Hydra Pool (github.com/256-Foundation; GPL v3 & CERN OHL S v2).
   - **Renewal: P2Pool v2** (pool2win/p2pool-v2) — evolved from p2pool, includes Braidpool (Feb 2024 grant) follow-on.
3. **2025-07-08 — Twelfth Wave of Bitcoin Grants** — https://opensats.org/blog/twelfth-wave-of-bitcoin-grants
   - **Hashpool and Axepool** (vnprc/hashpool; MIT) — accountless mining pool issuing eHash ecash tokens per share (modified Stratum V2); Axepool = proxy layer for small miners "such as Bitaxes".
4. **2026-02-04 — Sixteenth Wave of Bitcoin Grants** — https://opensats.org/blog/sixteenth-wave-of-bitcoin-grants
   - **Stratum V2** — grant to developer Lucas Balieiro for Stratum V2 Reference Implementation (stratum-mining/stratum; Apache-2.0/MIT) testing/tooling.
- Bitaxe project page listing these waves: https://opensats.org/projects/bitaxe
- **NerdMiner: none found** in OpenSats announcements checked (waves 4, 11, 12, 16 + Bitaxe project page).

**HRF — Bitcoin Development Fund (BDF):**

1. **2026-01-13 (Q4 2025 round) — 1.3B sats to 22 projects** — https://hrf.org/latest/hrfs-bitcoin-development-fund-announces-support-for-22-projects-worldwide/
   - **Stratum V2 (SRI)** — funding developer bit-aloo (github.com/Shourya742) full-time on Stratum V2 performance/integration/maintenance.
   - **Braidpool** (github.com/braidpool/braidpool) — funding developer Mohd Zaid on P2P open-source mining pool.
2. **(approx) Sept 2024 — BDF round, 1B sats / 20 projects** — per X post @femilonge (2024-09 (approx)) and LinkedIn: includes **256 Foundation** ("mission to make Bitcoin mining free & open starts with the Bitaxe initiative") — announcement page not directly fetched; date approximate.
3. **2026-08-25 — BDF round, 500M+ sats / 16 projects** — HRF **renewed support for the 256 Foundation** (per 256foundation.org/newsroom/hrf-renews-support; HRF press release "HRF Grants 500M+ Satoshis to 16 Freedom Tech Projects Worldwide", https://hrf.org/latest/hrf-grants-500m-satoshis-to-16-freedom-tech-projects-worldwide/).
- HRF BDF cumulative: $9.6M in BTC to 319 projects in 62 countries since 2020 (per Jan 2026 press release).
