# Hydrapool

> Sources: 256 Foundation Telegram group (t.me/the256foundation), 2024-02-24 → 2026-10-07
> Raw: [256F Telegram signal digest](../../raw/history/2026-10-08-256f-telegram-signal.md)
> Updated: 2026-10-08
> As-Of: 2026-10-08
> Status: Draft

## Overview

Hydrapool is the 256 Foundation's pool server: a simple stratum server written in Rust with extensibility as the main goal, shipping solo and PPLNS modes, paying directly from the coinbase (no custody). It exists because ckpool is very hard to extend — interesting accounting/payout mechanisms mean wading through a decade of built-in proxy/node C code — and datum_gateway is simpler but tethered to the Ocean ecosystem [#2356 · 2025-06-05 · jungly 🐕💸]. Design goal: easy to run, easy to extend and experiment with, with 'lottery with friends' as a first-class use case [#2356 · 2025-06-05 · jungly 🐕💸] [#2358 · 2025-06-05 · jungly 🐕💸] [#2359 · 2025-06-05 · szarka].

## Design philosophy

- Direct-from-coinbase payouts (Laurentia-style, no custody) agreed as the MVP; the direct-coinbase payout-count limit is a Bitmain firmware constraint — the trade-off is Antminer stock-firmware incompatibility [#1605 · 2025-02-03 · econoalchemist] [#1607 · 2025-02-03 · jungly 🐕💸]
- Second concern: large coinbase payout lists eat blockspace — 5,000 miners would consume meaningful blockspace, letting other pools net higher payouts [#1607 · 2025-02-03 · jungly 🐕💸]
- Target users: Bitaxe and Ember One owners who run hardware regardless of fee revenue; iterate later toward federation (fedipool), ecash (hashpool), or Lightning atomic swaps (p2poolv2) [#1608 · 2025-02-03 · econoalchemist] [#1600 · 2025-02-02 · econoalchemist]
- Framed as the decentralization answer to big-pool pain points (ckpool-dev context) [#1711 · 2025-03-11 · jungly 🐕💸] [#1712 · 2025-03-11 · econoalchemist]
- Hydrapool vs P2Poolv2 niches (jungly): Hydrapool = run a pool for yourself/your network, hackable accounting and payouts; P2Poolv2 = opinionated, decentralized pool built to scale; they share core libs (stratum, accounting, coinbase) which live in the P2Poolv2 repo [#3915 · 2025-12-10 · jungly 🐕💸] [#3917 · 2025-12-10 · jungly 🐕💸]
- Bring-your-own-node philosophy: connecting your own node is a key feature; node install stays out of scope because sync times are an ordeal, and it keeps Hydrapool independent of node versions [#3155 · 2025-10-28 · jungly 🐕💸]

> **Status: Disputed** — pruned nodes for mining templates
> jungly initially said Bitcoin Core doesn't support getblocktemplate on pruned nodes [#2759 · 2025-08-06 · jungly 🐕💸]; Skot pushed back — pruned nodes keep the full validated UTXO set, which should suffice for templates [#2761 · 2025-08-06 · Skot Bitaxe] [#2763 · 2025-08-07 · Skot Bitaxe]; jungly conceded he might be right and wants to test [#2764 · 2025-08-07 · jungly 🐕💸]; datapoint: szarka mines on OCEAN with multiple pruned Knots nodes, no issues [#2776 · 2025-08-14 · szarka]. Best assessment as of 2026-10-08: pruned-node mining works in practice (szarka's OCEAN setup), formal support question still worth testing.

## History & releases

- 2025-04-28: early iteration opened to the community for testing at stratum+tcp://stratum.hydrapool.org:3333 — any username works, payouts configured to the 256 Foundation address; stats at stats.hydrapool.org [#1889 · 2025-04-28 · econoalchemist] [#1891 · 2025-04-28 · econoalchemist] [#1904 · 2025-04-29 · econoalchemist]
- That stratum URL served as the Telehash 2025 endpoint (event ran 2025-05-05); username doubles as your leaderboard name [#1937 · 2025-04-30 · econoalchemist] [#2056 · 2025-05-05 · Karl] [#2058 · 2025-05-05 · szarka]
- Signet-instead-of-mainnet bug (October 2025): a release deserialized the wrong genesis ('Invalid genesis block data' panic); root cause was looking for Signet data instead of mainnet; fixed within days [#3142 · 2025-10-22 · Bartholomew] [#3143 · 2025-10-22 · econoalchemist]
- Linux/Mac/Windows packages cut for one-step installs (October 2025) [#3151 · 2025-10-28 · jungly 🐕💸]
- v2.0.1 released for self-hosters (2026-01-07); step-by-step build instructions for the 256F server at hydrapool.org [#4169 · 2026-01-07 · econoalchemist] [#4171 · 2026-01-07 · econoalchemist]
- v2.4.0 pushed and used for the February 2026 telehash [#4427 · 2026-02-16 · jungly 🐕💸]
- Packaging: NebulaMiner opened PRs including a Start9 package (November 2025); Hydrapool ran as a native Umbrel app by July 2026 [#3323 · 2025-11-14 · NebulaMiner] [#5254 · 2026-07-27 · 256F Forum]
- devpool (rkuester): a fun remix of Hydrapool's container image for tinkering with Mujina, Bitaxe etc. [#3726 · 2025-11-29 · Ryan]
- Operation Bitcoin runs a Hydrapool instance at hydrapool.operationbitcoin.io plus an open-source ob-telehash-dashboard [#5018 · 2026-07-01 · Gabe Lord] [#5048 · 2026-07-17 · Nickamoto]
- Scope guard: Hydrapool is a BTC pool — BC3 (bitcoinIII)/sha3t mining attempts get 'Share rejected (low difficulty share)' [#5459 · 2026-09-06 · Rand Childs]

## Payout semantics

- The pool is always in PPLNS mode — a single user simply receives 100% of the shares; add a second username/address and the coinbase starts splitting; multiple of your own addresses all share the coinbase [#3149 · 2025-10-28 · econoalchemist] [#3150 · 2025-10-28 · jungly 🐕💸]
- Solo-mode semantics: connect as a single user (any number of workers) and all coinbase goes to that user — no config change needed; an explicit solo_address option considered; the payout-file work also enables single- or multi-address lotto setups, but not multiuser solo [#3960 · 2025-12-15 · jungly 🐕💸] [#3961 · 2025-12-15 · jungly 🐕💸] [#3965 · 2025-12-15 · jungly 🐕💸] [#3969 · 2025-12-15 · jungly 🐕💸] [#3975 · 2025-12-15 · AgentP]
- Custom payout lists: payout_file_path in the p2poolv2 config makes the coinbase builder load payouts from a file (<100 lines, falls back to PPLNS on any error), while Hydrapool fetches from a downstream_payout_url API — ultimate flexibility for reward-sharing schemes like boot.gridlabs.science; tradeoff: that instance becomes custodial by choice [#3928 · 2025-12-12 · AgentP] [#3930 · 2025-12-12 · AgentP] [#3933 · 2025-12-12 · AgentP] [#3946 · 2025-12-13 · AgentP]

## Auditable hashrate & the pool-signature debate

- Pool signature is a 16-byte config option (default "hydrapool"); operators rebrand instances by editing config [#3866 · 2025-12-09 · jungly 🐕💸] [#3867 · 2025-12-09 · jungly 🐕💸] [#3869 · 2025-12-09 · jungly 🐕💸]
- Pool anonymity: 'leave it blank to not identify yourself' (like ckpool) — pool tags originally existed to advertise hashrate; counterpoint raised that reported pool hashrate isn't auditable (only Braiins tried making it feasible) [#4436 · 2026-02-17 · Boots Stribling] [#4437 · 2026-02-17 · jungly 🐕💸] [#4438 · 2026-02-17 · Steve Barbour]
- Hydrapool's answer: an optional public API endpoint letting anyone download all shares and audit the pool [#4443 · 2026-02-17 · jungly 🐕💸]
- mempool.space policy: a pool must solve one mainnet block before mempool.space will display its scriptsig; The Space's pool block appeared via Ocean/DATUM because Mechanic contributed Ocean-specific code to mempool — call to generalize it for Hydrapool and standardize [#3728 · 2025-11-29 · Ryan] [#3730 · 2025-11-29 · Ryan] [#3732 · 2025-11-29 · Ryan] [#3733 · 2025-11-29 · Ryan] [#3734 · 2025-11-29 · Ryan] [#3741 · 2025-11-29 · Skot Bitaxe]

## Operations quirks (As-Of 2026-10-08)

- Setup: services wait for full bitcoind sync before starting; support request logged to point at an existing bitcoind and multiple nodes for redundancy [#1995 · 2025-05-02 · jungly 🐕💸] [#1996 · 2025-05-02 · Bartholomew]
- Multi-firmware test day (August 2025) surfaced parsing bugs: Whatsminers sending username "None"; Antminer firmware's subscribe messages formatted in an unanticipated JSON shape breaking parsing; commitment made to publish the message formats each firmware sends [#2751 · 2025-08-06 · csh2000] [#2753 · 2025-08-06 · jungly 🐕💸] [#2755 · 2025-08-06 · jungly 🐕💸]
- Client compatibility: some older Bitaxe firmware versions don't play nice with Hydra Pool — update to latest ESP-Miner release; a Whatsminer M64 wouldn't fully power up or submit shares to Hydra but booted fine on the regular pool [#2740 · 2025-08-05 · econoalchemist] [#2747 · 2025-08-05 · Dylan Seib]
- Memory footprint: field report of an old instance at 13.4 GB RAM with 50,000 open sockets (socket leak, several-months-old version) vs the production instance running version 2.5.8 stable at around 1GB of memory usage; fix submitted as PR #605 to p2poolv2 [#5055 · 2026-07-20 · AgentP] [#5059 · 2026-07-21 · AgentP] [#5058 · 2026-07-21 · jungly 🐕💸] [#5063 · 2026-07-21 · AgentP]
- Leaderboard uses a rolling window — old >1 GH scores flush out [#4623 · 2026-03-18 · szarka] [#4624 · 2026-03-18 · econoalchemist]
- Dashboard anomaly (2026-02-02): the 256F hydrapool dash overstates hashrates — 'my humble underclocked S9 putting out 15.5 and up to 19 Th/s whereas the braiinsOS dashboard shows closer to 10. Same with my Bitaxe, it's definitely not putting out 2.2 Th/s' — flagged as a dash or pool estimation bug [#4380 · 2026-02-02 · PizzAndy]

## See Also

- [Pool Payout Schemes](pool-payout-schemes.md)
- [Decentralized Pool Designs](../protocols/decentralized-pool-designs.md)
- [asic-rs and the Fleet-Tooling Stack](../mining-software/asic-rs.md)
