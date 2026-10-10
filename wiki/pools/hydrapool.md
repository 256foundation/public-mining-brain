# Hydrapool

> Sources: 256 Foundation Telegram group (t.me/the256foundation), 2024-02-24 → 2026-10-07; 256foundation/hydrapool GitHub (README, docker README, CHANGELOG, releases, issues and PRs), 2025-04 → 2026-10; hydrapool.org home and hardware-tests pages (captured 2026-10-07); 256 Foundation newsletter and website, 2025-05 → 2026-05; 256 Foundation forum, 2026-05 → 2026-07; POD256 episode notes, 2025-04 → 2026-05; X posts by @jungly and @256FOUNDATION, 2025 → 2026; operator observations of live instances (2026-10-07)
> Raw: [256F Telegram signal digest](../../raw/history/2026-10-08-256f-telegram-signal.md); [Hydrapool README](../../raw/pools/hydrapool/github-256foundation-hydrapool.md); [hydrapool.org home](../../raw/pools/hydrapool/hydrapool-org-home.md); [Hydrapool CHANGELOG](../../raw/pools/hydrapool/github-hydrapool-changelog.md); [Hydrapool docker README](../../raw/pools/hydrapool/github-hydrapool-docker-readme.md); [Telehash #4 metrics](../../raw/history/256f-org/2026-05-21-forum-telehash-4-performance-metrics.md)
> Updated: 2026-10-09
> As-Of: 2026-10-09
> Status: Draft

## Overview

Hydrapool is the 256 Foundation's pool server: a simple stratum server written in Rust with extensibility as the main goal, shipping solo and PPLNS modes, paying directly from the coinbase (no custody). It exists because ckpool is very hard to extend — interesting accounting/payout mechanisms mean wading through a decade of built-in proxy/node C code — and datum_gateway is simpler but tethered to the Ocean ecosystem [#2356 · 2025-06-05 · jungly 🐕💸]. Design goal: easy to run, easy to extend and experiment with, with 'lottery with friends' as a first-class use case [#2356 · 2025-06-05 · jungly 🐕💸] [#2358 · 2025-06-05 · jungly 🐕💸] [#2359 · 2025-06-05 · szarka].

It is licensed AGPLv3, works with any bitcoin node that speaks bitcoin RPC, ships Prometheus/Grafana dashboards, and exposes an API so miners can download the PPLNS share accounting and check payouts themselves ([README](../../raw/pools/hydrapool/github-256foundation-hydrapool.md)). The Foundation's own framing is "WordPress for pools": a core platform with payouts as plug-ins (solo, PPLNS, and later Lightning or Ark), plus a P2Pool V2 path toward pooling with no operator at all ([256F projects page](../../raw/history/256f-org/256foundation-org-projects.md)). The Foundation says it has no plans to become a pool operator; the long-term goal is that users host their own instances ([newsletter, May 2025](../../raw/history/256f-newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md)). Internally, Hydrapool uses P2Poolv2's stratum and accounting libraries ([jungly on X, 2026-05-20](../../raw/history/256f-research/2026-10-07-x-notable-jungly-hydrapool.md)).

## At a glance (As-Of 2026-10-09)

| Item | Value | Source |
|---|---|---|
| License / language | AGPLv3, Rust | [README](../../raw/pools/hydrapool/github-256foundation-hydrapool.md) |
| Accounting modes | Solo and PPLNS (solo = a single user receiving 100% of PPLNS) | [README](../../raw/pools/hydrapool/github-256foundation-hydrapool.md); [#3149 · 2025-10-28 · econoalchemist] |
| Payouts | Direct from the coinbase; operator never custodies funds | [README](../../raw/pools/hydrapool/github-256foundation-hydrapool.md) |
| Users per coinbase | 100 by default (see the Disputed note below) | [hydrapool.org](../../raw/pools/hydrapool/hydrapool-org-home.md) |
| Workers | Limited only by the operator's hardware | [README](../../raw/pools/hydrapool/github-256foundation-hydrapool.md) |
| Default ports | Stratum 3333, API 46884, Grafana 3000, Prometheus 9090 | [docker README](../../raw/pools/hydrapool/github-hydrapool-docker-readme.md) |
| Networks | `main`, `testnet4`, `signet` | [docker README](../../raw/pools/hydrapool/github-hydrapool-docker-readme.md) |
| Latest release | v2.6.0, published 2026-06-12 (but see the open issue #44 below) | [releases](../../raw/pools/hydrapool/github-hydrapool-releases.md) |

## Design philosophy

- Direct-from-coinbase payouts (Laurentia-style, no custody) agreed as the MVP; the direct-coinbase payout-count limit is a Bitmain firmware constraint — the trade-off is Antminer stock-firmware incompatibility [#1605 · 2025-02-03 · econoalchemist] [#1607 · 2025-02-03 · jungly 🐕💸]. The newsletter puts that limit at some 16 addresses: an old stock Antminer will not handle a template with more payout addresses than that, while Hydrapool lets the operator configure the number ([newsletter, Sep 2025](../../raw/history/256f-newsletter/2025-09-25-rig-bitcoin-mining-re-imagined.md)); POD256 described it as Bitmain's 15-16 address limit ([newsletter, Nov 2025](../../raw/history/256f-newsletter/2025-11-24-assembling-freedom-11.md)).
- Second concern: large coinbase payout lists eat blockspace — 5,000 miners would consume meaningful blockspace, letting other pools net higher payouts [#1607 · 2025-02-03 · jungly 🐕💸]
- Target users: Bitaxe and Ember One owners who run hardware regardless of fee revenue; iterate later toward federation (fedipool), ecash (hashpool), or Lightning atomic swaps (p2poolv2) [#1608 · 2025-02-03 · econoalchemist] [#1600 · 2025-02-02 · econoalchemist]
- Framed as the decentralization answer to big-pool pain points (ckpool-dev context) [#1711 · 2025-03-11 · jungly 🐕💸] [#1712 · 2025-03-11 · econoalchemist]. The hydrapool.org rationale: pools are centralized, hard to set up and rarely open source, and governments could coerce them (KYC, censoring transactions); easily deployable pools let miners move hashrate away from such choke points ([hydrapool.org](../../raw/pools/hydrapool/hydrapool-org-home.md)). See [Pool Centralization & FPPS](pool-centralization-and-fpps.md).
- Hydrapool vs P2Poolv2 niches (jungly): Hydrapool = run a pool for yourself/your network, hackable accounting and payouts; P2Poolv2 = opinionated, decentralized pool built to scale; they share core libs (stratum, accounting, coinbase) which live in the P2Poolv2 repo [#3915 · 2025-12-10 · jungly 🐕💸] [#3917 · 2025-12-10 · jungly 🐕💸]
- Bring-your-own-node philosophy: connecting your own node is a key feature; node install stays out of scope because sync times are an ordeal, and it keeps Hydrapool independent of node versions [#3155 · 2025-10-28 · jungly 🐕💸]
- Auditability over server-side trust: rather than asking users to trust a share database, the pool exposes validated shares through an API so anyone can audit the PPLNS window, with minimal persistent storage to survive crashes and restarts ([newsletter, Sep 2025](../../raw/history/256f-newsletter/2025-09-25-rig-bitcoin-mining-re-imagined.md)).
- Long-term goals listed on hydrapool.org: alternative payout models such as echash, talking to other Hydra Pool instances via P2Poolv2, encrypted server/client communication and reduced bandwidth ([hydrapool.org](../../raw/pools/hydrapool/hydrapool-org-home.md)).

> **Status: Disputed** — pruned nodes for mining templates
> jungly initially said Bitcoin Core doesn't support getblocktemplate on pruned nodes [#2759 · 2025-08-06 · jungly 🐕💸]; Skot pushed back — pruned nodes keep the full validated UTXO set, which should suffice for templates [#2761 · 2025-08-06 · Skot Bitaxe] [#2763 · 2025-08-07 · Skot Bitaxe]; jungly conceded he might be right and wants to test [#2764 · 2025-08-07 · jungly 🐕💸]; datapoint: szarka mines on OCEAN with multiple pruned Knots nodes, no issues [#2776 · 2025-08-14 · szarka]. Best assessment as of 2026-10-08: pruned-node mining works in practice (szarka's OCEAN setup), formal support question still worth testing.

## Architecture history: ckpool fork to Rust on P2Poolv2 libs

1. **ckpool fork (April 2025).** The first stack (PR #12, 2025-04-10) used docker compose to run bitcoind for signet/testnet4, a ckpool-solo fork that always paid the pool address, a p2poolv2 node capturing shares for flexible payouts, and cpuminer for development ([PR #12](../../raw/pools/hydrapool/2025-04-10-github-hydrapool-pr-12-add-dockerfiles-to-build-hydrapool-so.md)). The public Telehash #2 build paid the 256 Foundation address automatically (any vanity username, no BTC address) and used a dashboard forked from CKstats; it ran on a bare-metal server in Florida with 64 cores and 128 GB of RAM ([newsletter, May 2025](../../raw/history/256f-newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md)).
2. **Rewrite decision (May–July 2025).** Back-end issues forced roughly nine server restarts in the first hours of Telehash #2 ([newsletter, Jun 2025](../../raw/history/256f-newsletter/2025-06-19-you-know-i-m-something-of-a-decentralized-pool-myself.md)). After reviewing Stratum v2 and DATUM, the team chose to write a stratum server from scratch in Rust; benchmarks against CK Pool were comparable ([newsletter, Jul 2025](../../raw/history/256f-newsletter/2025-07-15-the-bigger-they-are-the-harder-they-fall.md)). The early ckpool-extension plans (issues #9–#11: PPLNS, coinbase-only payouts) were closed because the p2pool library's accounting crate and payout mechanism replaced them ([issue #9](../../raw/pools/hydrapool/2025-04-09-github-hydrapool-issue-9-add-pplns-share-accounting-support.md); [issue #10](../../raw/pools/hydrapool/2025-04-09-github-hydrapool-issue-10-payouts-directly-from-coinbase-onl.md); [issue #11](../../raw/pools/hydrapool/2025-04-09-github-hydrapool-issue-11-explore-ckpool-s-pplns-payout-mana.md)).
3. **Compatibility testing on signet (Jul–Sep 2025).** A new test server on signet (`test.hydrapool.org:3333`) was used to validate many miner types, because there is no Stratum v1 standard ([newsletter, Aug 2025](../../raw/history/256f-newsletter/2025-08-18-is-open-source-communism.md)). Over 30 different kinds of miners connected and exposed stratum-handling issues that were fixed ([newsletter, Sep 2025](../../raw/history/256f-newsletter/2025-09-25-rig-bitcoin-mining-re-imagined.md)). The maintainer chose signet over testnet4 because of the state testnet4 was in ([issue #7](../../raw/pools/hydrapool/2025-04-09-github-hydrapool-issue-7-deploy-for-testnet4-to-enable-testi.md)).
4. **Binaries, then Docker again (Oct–Nov 2025).** On 2025-10-23 pool2win said the project had moved away from ckpool and would ship prebuilt binaries rather than run the pool in Docker ([PR #19](../../raw/pools/hydrapool/2025-08-29-github-hydrapool-pr-19-build-add-dockerfile-for-hydra-pool.md)); a Debian package workflow (cargo-deb) arrived in 1.1.9, and by 1.1.14 docker compose (with cosign-signed images) became the primary way to run the pool while the Ansible templates were deprecated ([CHANGELOG](../../raw/pools/hydrapool/github-hydrapool-changelog.md)).
5. **Storage and dashboards.** Shares are stored with p2pool's store crate on RocksDB ([issue #8](../../raw/pools/hydrapool/2025-04-09-github-hydrapool-issue-8-store-all-shares-generated-by-miner.md)); the planned ckpool-style dashboard and per-username filtering were replaced by Grafana dashboards ([issue #4](../../raw/pools/hydrapool/2025-04-09-github-hydrapool-issue-4-ckpool-like-dashboard-for-total-has.md); [issue #6](../../raw/pools/hydrapool/2025-04-09-github-hydrapool-issue-6-add-support-to-filter-by-username-f.md)).
6. **P2Poolv2 libraries.** Each 2.x release bumps the shared libs (for example 2.4.0 moved to p2poolv2 v0.7.0 and 2.5.0 to v0.10.12) ([CHANGELOG](../../raw/pools/hydrapool/github-hydrapool-changelog.md)); the mode logic now lives in those libs, which is where issue #44 originates (see Known issues).

## Running your own instance (operator how-to)

### What you need

- A bitcoin node with RPC and ZMQ block notifications (`zmqpubhashblock`, e.g. `tcp://0.0.0.0:28334` on the node; inside containers use `host.docker.internal`, not localhost) ([docker README](../../raw/pools/hydrapool/github-hydrapool-docker-readme.md)). The node is bring-your-own; the reference walk-through builds a pool server on an old Dell Optiplex 9020 with Ubuntu Server 24.04.3 LTS, Bitcoin Core from Snap with chain data on a 2TB auxiliary drive, and the Hydrapool Docker files ([hydrapool.org](../../raw/pools/hydrapool/hydrapool-org-home.md)).
- Linux. v2.5.3 removed the Windows and Mac builds ([CHANGELOG](../../raw/pools/hydrapool/github-hydrapool-changelog.md)); the README still advertises Linux, Windows and MacOS binaries and is out of date on this point ([README](../../raw/pools/hydrapool/github-256foundation-hydrapool.md)).

### Install methods

| Method | How | Notes |
|---|---|---|
| Docker (recommended) | Download `docker-compose.yml` and `config-example.toml` from the latest release; `docker compose -f docker-compose.yml up` | Starts the pool plus Prometheus/Grafana; images are cosign-signed and verifiable against the github.com/256foundation certificate identity |
| Binaries | `hydrapool-installer.sh` from the releases page | Installs `hydrapool` (runs the pool) and `hydrapool_cli` (query state, generate auth tokens); Docker still recommended for the dashboards |
| Source | `cargo build --release` | Needs Rust 1.88.0 or newer; on Ubuntu 22.04 the distro Rust may need replacing and `libssl-dev`, `pkg-config`, `clang`, `libclang-dev` may be required |

All rows: [README](../../raw/pools/hydrapool/github-256foundation-hydrapool.md).

### config.toml essentials

- Minimum edits: bitcoin RPC URL and credentials, `zmqpubhashblock`, `network`, and `bootstrap_address` (which defaults to the 256 Foundation's donation address) ([docker README](../../raw/pools/hydrapool/github-hydrapool-docker-readme.md)). Since 2.0.0 the default mainnet config uses the Foundation's address ([CHANGELOG](../../raw/pools/hydrapool/github-hydrapool-changelog.md)), so change it.
- `bootstrap_address` receives the reward if a block is found in roughly the first 10-seconds or so after the server boots ([hydrapool.org](../../raw/pools/hydrapool/hydrapool-org-home.md)).
- Optional donation and operator-fee percentages are in basis points (100 = 1%); both are off by default. `pool_signature` (the coinbase tag) can be changed from the default "hydrapool", max 16 bytes ([hydrapool.org](../../raw/pools/hydrapool/hydrapool-org-home.md)); leave it blank to not identify yourself [#4437 · 2026-02-17 · jungly 🐕💸].
- Miners can pass a starting difficulty (`d=`) and a hashrate hint (`h=`) in the stratum password field, alongside suggest-difficulty, so a 1 TH/s Bitaxe and a 1 EH/s fleet can connect without manual tuning ([newsletter, May 2026](../../raw/history/256f-newsletter/2026-05-28-assembling-freedom-27.md)); the feature was on the April 2026 roadmap ([newsletter, Apr 2026](../../raw/history/256f-newsletter/2026-04-11-assembling-freedom-23.md)).

### bitcoin.conf: Docker networking

The compose file runs Hydrapool on an isolated bridged network, so the node must accept RPC from it ([README](../../raw/pools/hydrapool/github-256foundation-hydrapool.md)):

```ini
# node on the same host as Docker
rpcbind=0.0.0.0
rpcallowip=172.16.0.0/12
```

- Containers reach the host as `host.docker.internal`. If the node is on another host, point the RPC URL there and allow the Docker host's IP, because container traffic is NATed ([README](../../raw/pools/hydrapool/github-256foundation-hydrapool.md)).
- Symptom of getting this wrong (resolved): a Docker network missing from `rpcallowip` made bitcoind return 403 Forbidden and Hydrapool panicked with a misleading JSON-parse error; p2poolv2 PR 251 (merged 2025-11-04) now logs bitcoind's HTTP status and message ([issue #32](../../raw/pools/hydrapool/2025-11-03-github-hydrapool-issue-32-better-error-messages-are-needed-w.md)).
- Services wait for full bitcoind sync before starting; a support request was logged to point at an existing bitcoind and multiple nodes for redundancy [#1995 · 2025-05-02 · jungly 🐕💸] [#1996 · 2025-05-02 · Bartholomew]; 2.5.9 stops waiting for chain sync in hydrapool mode ([CHANGELOG](../../raw/pools/hydrapool/github-hydrapool-changelog.md)).

### blockmaxweight: leave room for the coinbase

Every payout output costs block weight. If regular transactions fill the default 4,000,000 WU, Bitcoin Core may reject the template; set `blockmaxweight` lower ([README](../../raw/pools/hydrapool/github-256foundation-hydrapool.md)):

| P2PKH outputs in coinbase | Approx. coinbase weight | Suggested `blockmaxweight` |
|---:|---:|---:|
| 20 | ~2,928 WU | `3997000` |
| 100 | ~13,808 WU | `3986000` |
| 200 | ~27,408 WU | `3972500` |
| 500 | ~68,208 WU | `3930000` |
| 1000 | ~136,208 WU | `3860000` |

SegWit outputs need slightly less room ([README](../../raw/pools/hydrapool/github-256foundation-hydrapool.md)).

> **Status: Disputed** — is 100 users a hard limit?
> The README says the pool only accommodates up to 100 users for coinbase and block weight reasons ([README](../../raw/pools/hydrapool/github-256foundation-hydrapool.md); repeated in the [Nov 2025 newsletter](../../raw/history/256f-newsletter/2025-11-24-assembling-freedom-11.md)). hydrapool.org says 100 unique users in the coinbase is a default that can be raised via the blockmaxweight instructions ([hydrapool.org](../../raw/pools/hydrapool/hydrapool-org-home.md)), and the README's own table goes to 1000 outputs. Best assessment: 100 is the shipped default, not a protocol limit; beyond it, operators trade block space (and fee revenue) for payout count, and old stock Antminers cap out far lower (see Design philosophy).

### Securing a public server

- API auth: generate `auth_user`/`auth_token` with `docker compose run --rm hydrapool-cli gen-auth <USERNAME> <PASSWORD>`, paste into config.toml, then put the same credentials in a custom `prometheus.yml` and in the `docker-compose.yml` healthcheck ([README](../../raw/pools/hydrapool/github-256foundation-hydrapool.md)).
- Default credentials are Grafana admin/admin and Prometheus hydrapool/hydrapool — change both before exposing them ([docker README](../../raw/pools/hydrapool/github-hydrapool-docker-readme.md); [README](../../raw/pools/hydrapool/github-256foundation-hydrapool.md)).
- Put nginx in front of public dashboards and the API ([README](../../raw/pools/hydrapool/github-256foundation-hydrapool.md)).

### Share-audit API

`/pplns_shares` downloads every PPLNS share the pool tracks, with optional `start_time`/`end_time` in RFC3339; `/health` is the health check ([README](../../raw/pools/hydrapool/github-256foundation-hydrapool.md)). The API returned an empty array on 2.2.2 because PPLNS share saving was switched off during the January 2026 telehash to avoid slowdowns; the maintainer planned to restore it as a crate feature ([issue #40](../../raw/pools/hydrapool/2026-02-03-github-hydrapool-issue-40-pplns-api-returns-empty-array.md)).

### Upgrades

`docker compose pull` then `docker compose up -d --force-recreate`. Going from v1.x.x to v2.x.x or higher needs a one-time database reset (`docker compose down -v`) ([README](../../raw/pools/hydrapool/github-256foundation-hydrapool.md)), because 2.0.0 switched to Bitcoin-compatible share serialization and shipped no migration script ([CHANGELOG](../../raw/pools/hydrapool/github-hydrapool-changelog.md)).

## Payout semantics

- The pool is always in PPLNS mode — a single user simply receives 100% of the shares; add a second username/address and the coinbase starts splitting; multiple of your own addresses all share the coinbase [#3149 · 2025-10-28 · econoalchemist] [#3150 · 2025-10-28 · jungly 🐕💸]
- Solo-mode semantics: connect as a single user (any number of workers) and all coinbase goes to that user — no config change needed; an explicit solo_address option considered; the payout-file work also enables single- or multi-address lotto setups, but not multiuser solo [#3960 · 2025-12-15 · jungly 🐕💸] [#3961 · 2025-12-15 · jungly 🐕💸] [#3965 · 2025-12-15 · jungly 🐕💸] [#3969 · 2025-12-15 · jungly 🐕💸] [#3975 · 2025-12-15 · AgentP]
- Telehash mode: with donation at 100%, address validation and PPLNS accounting are skipped so non-address usernames work (2.1.4–2.1.6) ([CHANGELOG](../../raw/pools/hydrapool/github-hydrapool-changelog.md)).
- Custom payout lists: payout_file_path in the p2poolv2 config makes the coinbase builder load payouts from a file (<100 lines, falls back to PPLNS on any error), while Hydrapool fetches from a downstream_payout_url API — ultimate flexibility for reward-sharing schemes like boot.gridlabs.science; tradeoff: that instance becomes custodial by choice [#3928 · 2025-12-12 · AgentP] [#3930 · 2025-12-12 · AgentP] [#3933 · 2025-12-12 · AgentP] [#3946 · 2025-12-13 · AgentP]

### PPLNS window sizing (storage)

For a family-and-friends hashrate-heating pool where some miners run only in winter, a `pplns_ttl_days` above 365 would still reward past work if a block hits in summer. pool2win's estimate: about 100 users need 90-100 GB of disk for a year of shares; the cost scales with users (BTC addresses), not workers, so friends should reuse one address across their miners ([issue #27](../../raw/pools/hydrapool/2025-10-30-github-hydrapool-issue-27-pplns-ttl-days.md)). See [Pool Choice for Heat Miners](pool-choice-for-heat-miners.md).

### Plugin system (planned)

PR #42 (2026-03-19) proposed overriding PPLNS payouts with a local payout file and forwarding high-difficulty shares to an external pool ([PR #42](../../raw/pools/hydrapool/2026-03-19-github-hydrapool-pr-42-custom-user-defined-payouts.md)). Rather than merge that into `main.rs`, the maintainer opened issue #43 for a payout/accounting plugin system: Rust crates or `.so` plugins enabled from config.toml, traits such as `fill_distribution_from_shares` and `build_coinbase_transaction`, limited RocksDB access, a score-based PPLNS plugin as default and `simple_pplns` moved into a plugin ([issue #43](../../raw/pools/hydrapool/2026-03-19-github-hydrapool-issue-43-build-payout-plugin-system.md)). The April 2026 roadmap also lists a gamified dashboard and Lightning payouts ([newsletter, Apr 2026](../../raw/history/256f-newsletter/2026-04-05-pod256-episode-110-newsletter-april-fools-real-progress-open.md)).

## Stratum V2

- Declined SRI crates (2025-12-10): the maintainer said SRI did more than Hydrapool needed, carried technical debt and had tightly coupled APIs; he planned to add SV2 as devices adopt it, starting with encrypted/compressed channels ([issue #37](../../raw/pools/hydrapool/2025-12-10-github-hydrapool-issue-37-use-rust-sv2-crates.md)).
- Issue #41 (average-gary, 2026-02-17) proposes native SV2 Mining Protocol support on the refactored `stratum-core` crate — no Job Declaration or Template Distribution — with SV1 on port 3333 and SV2 on 3334 behind an opt-in `sv2` cargo feature. An end-to-end testnet4 run on 2026-03-04 (Bitaxe → SRI Translator Proxy → Hydrapool, Noise NX on port 3334) had 100+ shares accepted with zero rejections. Interop lessons: send every job as a future job activated by SetNewPrevHash; send all NewMiningJob messages before any SetNewPrevHash in a batch; don't send standard-channel broadcasts to extended-channel-only connections ([issue #41](../../raw/pools/hydrapool/2026-02-17-github-hydrapool-issue-41-feat-stratum-v2-mining-protocol-su.md)).
- The 256 Foundation joined the Stratum V2 Working Group, citing server-side SV2 in Hydrapool and client-side SV2 in Mujina ([256F on X, 2026](../../raw/history/256f-research/2026-10-07-x-256foundation-2026.md)). See [Stratum in Practice](../protocols/stratum-in-practice.md).

## Hardware compatibility

hydrapool.org/hardware-tests asks owners of untested hardware to point at `stratum+tcp://test.hydrapool.org:3333` for 5 to 10 minutes while server logs are watched. The capture lost the green/yellow/red pass/fail colours, so the table below is the set of rows that name a firmware (the ones evidently tested); the other ~100 rows are nameplate specs ([hardware tests](../../raw/pools/hydrapool/hydrapool-org-hardware-tests-html.md)).

| Make / model | Firmware | Hash power (nameplate) | Efficiency |
|---|---|---|---|
| Bitaxe Gamma | ESP Miner v2.7.1 | 1.2 Th/s | 15 J/Th |
| Bitaxe Supra | ESP Miner v2.7.1 | 0.8 Th/s | 17.5 J/Th |
| Futurebit Apollo I | Apollo API v2.0.6 | 3.5 Th/s | 45 J/Th |
| Ember One 00 | test firmware | 3 Th/s | 33.3 J/Th |

Field notes:

- Multi-firmware test day (August 2025) surfaced parsing bugs: Whatsminers sending username "None"; Antminer firmware's subscribe messages formatted in an unanticipated JSON shape breaking parsing; commitment made to publish the message formats each firmware sends [#2751 · 2025-08-06 · csh2000] [#2753 · 2025-08-06 · jungly 🐕💸] [#2755 · 2025-08-06 · jungly 🐕💸]
- Client compatibility: some older Bitaxe firmware versions don't play nice with Hydra Pool — update to latest ESP-Miner release; a Whatsminer M64 wouldn't fully power up or submit shares to Hydra but booted fine on the regular pool [#2740 · 2025-08-05 · econoalchemist] [#2747 · 2025-08-05 · Dylan Seib]
- "Share validation failed: Insufficient work" on V1.1.5 (Knots 29.1, an AvalonMiner 1246 and a Bitaxe) was fixed in v1.1.6 ([issue #21](../../raw/pools/hydrapool/2025-10-25-github-hydrapool-issue-21-share-validation-failed-insufficie.md)).
- Invalid-address authorize: Hydrapool originally closed the connection silently (Public Pool returns error 20; ckpool returns result false). p2poolv2 PR 312 (2026-01-12) adopted ckpool's two-strike policy — first failure returns -401 with a reason, second disconnects ([issue #35](../../raw/pools/hydrapool/2025-11-16-github-hydrapool-issue-35-mining-authorize-with-an-invalid-b.md)). The same log shows a Bitaxe sending `mining.configure` with mask ffffffff and Hydrapool answering version-rolling with mask 1fffe000.
- Hydrapool sends `result`/`error` as null in responses, after the same omission broke Bitaxe on Miningcore pools ([ESP-Miner #916](../../raw/firmware/esp-miner/2025-05-12-github-esp-miner-issue-916-incompatibility-with-miningcore-b.md)).
- Duplicate shares are detected and rejected since 2.1.0 ([CHANGELOG](../../raw/pools/hydrapool/github-hydrapool-changelog.md)).

## Known issues (As-Of 2026-10-09)

> **Status: Open bug** — v2.6.0 ignores `mode = "hydrapool"` (issue #44, opened 2026-10-04)
> The official v2.6.0 binary always builds the sharechain PPLNS payout; its StratumServerBuilder never sets the mode. On testnet4, 99% of the coinbase went to the genesis share's unspendable NUMS address and every share was rejected as low difficulty; the reporter warns a mainnet block found this way would burn almost all of its reward. He traces it to v2.5.3 ("Update to latest p2poolv2 libs") and says the 2.5.9 ASERT-difficulty fix has no effect in the binary for the same reason. A build of `p2poolv2_node` from v0.12.0 with the mode passed correctly paid exactly 1% to the fee address and split the rest 60/40 between two miners by shares ([issue #44](../../raw/pools/hydrapool/2026-10-04-github-hydrapool-issue-44-v2-6-0-ignores-mode-hydrapool-coin.md)). Operators on v2.5.3 or later should test on testnet4/signet and inspect the coinbase before mining mainnet.

- Memory footprint: field report of an old instance at 13.4 GB RAM with 50,000 open sockets (socket leak, several-months-old version) vs the production instance running version 2.5.8 stable at around 1GB of memory usage; fix submitted as PR #605 to p2poolv2 [#5055 · 2026-07-20 · AgentP] [#5059 · 2026-07-21 · AgentP] [#5058 · 2026-07-21 · jungly 🐕💸] [#5063 · 2026-07-21 · AgentP]
- 2.5.5 fixed u64 saturation of the total-valid-shares counter in the Prometheus output ([CHANGELOG](../../raw/pools/hydrapool/github-hydrapool-changelog.md)).
- Leaderboard uses a rolling window — old >1 GH scores flush out [#4623 · 2026-03-18 · szarka] [#4624 · 2026-03-18 · econoalchemist]
- Dashboard anomaly (2026-02-02): the 256F hydrapool dash overstates hashrates — 'my humble underclocked S9 putting out 15.5 and up to 19 Th/s whereas the braiinsOS dashboard shows closer to 10. Same with my Bitaxe, it's definitely not putting out 2.2 Th/s' — flagged as a dash or pool estimation bug [#4380 · 2026-02-02 · PizzAndy]
- Scope guard: Hydrapool is a BTC pool — BC3 (bitcoinIII)/sha3t mining attempts get 'Share rejected (low difficulty share)' [#5459 · 2026-09-06 · Rand Childs]

## Release timeline

GitHub lists 35 releases, all stable, from v1.0.1 (2025-10-22) to v2.6.0 (2026-06-12) ([release history](../../raw/history/256f-research/2026-10-07-github-release-history-key-repos.md)). Publish dates below are from the releases page; changelog dates sometimes differ (e.g. the changelog dates 2.0.1 and 2.0.0 2025-12-24 and 2.4.0 2026-01-24) ([releases](../../raw/pools/hydrapool/github-hydrapool-releases.md); [CHANGELOG](../../raw/pools/hydrapool/github-hydrapool-changelog.md)).

| Version | Published | Notable changes |
|---|---|---|
| v1.0.1 | 2025-10-22 | First GitHub release |
| v1.1.9 | 2025-10-29 | Debian package workflow (cargo-deb) |
| v1.1.13 | 2025-10-30 | Dockerfiles for Hydrapool, Grafana, Prometheus; docker compose file |
| v1.1.18 | 2025-10-31 | Follows 1.1.14: cosign-signed images, docker compose as the primary run method, Ansible deprecated |
| v2.0.1 | 2025-12-26 | 2.0.0 BREAKING: Bitcoin-compatible share serialization (wipe store.db); coinbase distribution in Grafana; Foundation address as default mainnet config |
| v2.1.0 | 2026-01-09 | Duplicate-share rejection; load-test mode ignoring difficulty |
| v2.1.3 | 2026-01-12 | ckpool-style two-strike authorize failure |
| v2.1.4 – v2.1.6 | 2026-01-15 | 100%-donation (telehash) mode skips address validation and PPLNS |
| v2.1.7 | 2026-01-16 | Stop saving chain and PPLNS shares for now (performance) |
| v2.1.9 | 2026-01-18 | Graceful termination (removes Grafana spikes on restart) |
| v2.2.0 | 2026-01-19 | Faster notify broadcast; clean up inactive users/workers |
| v2.4.0 | 2026-02-16 | 2.3.0 yanked; p2poolv2 v0.7.0; used for the February 2026 telehash |
| v2.5.3 | 2026-05-14 | Windows and Mac builds removed (2.5.0: p2poolv2 libs v0.10.12) |
| v2.5.5 | 2026-05-16 | u64 saturation fix in Prometheus output |
| v2.5.8 | 2026-05-19 | Production 256F instance ran 2.5.8 in July 2026 |
| v2.6.0 | 2026-06-12 | Latest; see issue #44 |

Sources for the table rows: [CHANGELOG](../../raw/pools/hydrapool/github-hydrapool-changelog.md); [release history](../../raw/history/256f-research/2026-10-07-github-release-history-key-repos.md); [#4427 · 2026-02-16 · jungly 🐕💸]; [#5058 · 2026-07-21 · jungly 🐕💸].

## History

- 2025-03-27: the Foundation described Hydra Pool as a one-click deployable pool package with Stratum v2 support, built for the complete Ember One system ([256F on X, 2025 H1](../../raw/history/256f-research/2026-10-07-x-256foundation-2025-h1.md)). POD256 #068 pitched it as "The Wordpress of Mining Pools" ([POD256 #068](../../raw/history/pod256/2025-04-17-pod256-068-the-wordpress-of-mining-pools-with-jungly.md)).
- 2025-04-28: early iteration opened to the community for testing at stratum+tcp://stratum.hydrapool.org:3333 — any username works, payouts configured to the 256 Foundation address; stats at stats.hydrapool.org [#1889 · 2025-04-28 · econoalchemist] [#1891 · 2025-04-28 · econoalchemist] [#1904 · 2025-04-29 · econoalchemist]
- That stratum URL served as the Telehash 2025 endpoint (event ran 2025-05-05); username doubles as your leaderboard name [#1937 · 2025-04-30 · econoalchemist] [#2056 · 2025-05-05 · Karl] [#2058 · 2025-05-05 · szarka]
- Signet-instead-of-mainnet bug (October 2025): a release deserialized the wrong genesis ('Invalid genesis block data' panic); root cause was looking for Signet data instead of mainnet; fixed within days [#3142 · 2025-10-22 · Bartholomew] [#3143 · 2025-10-22 · econoalchemist]
- Released on October 26 (2025) and at v1.1.18 by late November ([newsletter, Nov 2025](../../raw/history/256f-newsletter/2025-11-24-assembling-freedom-11.md)); Linux/Mac/Windows packages cut for one-step installs (October 2025) [#3151 · 2025-10-28 · jungly 🐕💸]
- v2.0.1 released for self-hosters (2026-01-07); step-by-step build instructions for the 256F server at hydrapool.org [#4169 · 2026-01-07 · econoalchemist] [#4171 · 2026-01-07 · econoalchemist]
- POD256 #101 (2026-01-14): solo, PPLNS and multi-address coinbase payouts, scalability-tested to 10,000 workers; HashDash visualizes hashrate, workers and share distribution ([newsletter, Jan 2026](../../raw/history/256f-newsletter/2026-01-14-assembling-freedom-13.md)).
- v2.4.0 pushed and used for the February 2026 telehash [#4427 · 2026-02-16 · jungly 🐕💸]
- devpool (rkuester): a fun remix of Hydrapool's container image for tinkering with Mujina, Bitaxe etc. [#3726 · 2025-11-29 · Ryan]
- Operation Bitcoin runs a Hydrapool instance at hydrapool.operationbitcoin.io plus an open-source ob-telehash-dashboard [#5018 · 2026-07-01 · Gabe Lord] [#5048 · 2026-07-17 · Nickamoto]

### Event performance

| Event | Pool build | Result | Source |
|---|---|---|---|
| Telehash #2 (2025-05-05, Austin) | ckpool fork | ~nine restarts early; peak roughly 245 Ph/s and ~2,500 workers (incl. a parallel Public Pool instance at roughly 120 Ph/s); no block | [newsletter, Jun 2025](../../raw/history/256f-newsletter/2025-06-19-you-know-i-m-something-of-a-decentralized-pool-myself.md) |
| First outing of the Rust pool (posted 2026-01-24) | January 2026 performance releases (see timeline) | 1.4EH/s and 1500 peak worker connections | [jungly on X](../../raw/history/256f-research/2026-10-07-x-notable-jungly-hydrapool.md) |
| Telehash #4 (2026-05-19, Bitcoin Park Austin) | Rust pool on an AMD EPYC 9R45 AWS EC2 instance | Peak 2.49 EH/s, average 1.32 EH/s, ~30.81 ZH total work over 6.5 hours; 2231 unique workers, 59 users; 20,754,816 accepted vs 41,377 rejected shares (0.199%); >2,000 simultaneous connections at ~1% CPU; no block | [Telehash #4 metrics](../../raw/history/256f-org/2026-05-21-forum-telehash-4-performance-metrics.md); [newsletter, May 2026](../../raw/history/256f-newsletter/2026-05-28-assembling-freedom-27.md); [jungly on X](../../raw/history/256f-research/2026-10-07-x-notable-jungly-hydrapool.md) |

The scalability-test issue (target: 1000 stratum clients) was closed on 2026-03-19 after optimizations made for the January telehash ([issue #5](../../raw/pools/hydrapool/2025-04-09-github-hydrapool-issue-5-scalability-test-for-hydrapool-setu.md)). Telehash #4 hashrate was concentrated: the top contributor supplied 73.5959% of hashes ([Telehash #4 metrics](../../raw/history/256f-org/2026-05-21-forum-telehash-4-performance-metrics.md)). Which pool found Telehash #1's block 881423 is disputed — see [Solo Blocks Found by Open-Source & Home Miners](../history/open-source-solo-blocks.md).

## Live instances (observed 2026-10-07)

| Instance | Notes | Source |
|---|---|---|
| pool.256foundation.org:3333 (256 Foundation) | Any vanity username or Nostr npub; pays 100% to the Foundation if it finds a block. Web root redirects to dash.256f.org; `/api/v1/query` serves Prometheus without auth. At 2026-10-07T21:22:40Z: 76.14 TH/s from 18 addresses and 45 workers | [hydrapool.org](../../raw/pools/hydrapool/hydrapool-org-home.md); [redirect](../../raw/pools/hydrapool/2026-10-07-pool-256foundation-html-redirect.md); [operator query](../../raw/pools/hydrapool/2026-10-07-pool-256foundation-operator.md) |
| test.hydrapool.org | README's mainnet test instance; serves a Grafana login (appUrl grafana.p2poolv2.org), no public Hydrapool Prometheus API | [test.hydrapool.org](../../raw/pools/hydrapool/2026-10-07-test-hydrapool-org.md) |
| CleanPool (operator Caylon, announced 2026-07-26) | Third-party PPLNS instance: first 1 BTC of its first block funds buildout, then a flat fee; 2.1% of each block to the 256 Foundation (operator claims, not checked on-chain). Templates from a Knots node with `datacarriersize=83`, `rejectparasites=1`, `rejecttokens=1`, `permitbaremultisig=0`. At 2026-10-07T21:33:30Z: 55.76 TH/s, 8 addresses, 12 workers | [CleanPool announcement](../../raw/pools/hydrapool/2026-10-07-cleanpool-caylon.md); [CleanPool page and Prometheus](../../raw/pools/hydrapool/2026-10-07-cleanpool-payouts-filters-prom.md) |
| hydrapool.operationbitcoin.io | Operation Bitcoin instance | [#5018 · 2026-07-01 · Gabe Lord] |

The metric `worker_shares_valid_total` is difficulty-weighted, so its 5-minute rate reads as H/s ([operator query](../../raw/pools/hydrapool/2026-10-07-pool-256foundation-operator.md)). POD256 #101 show notes give the telehash endpoint as pool.256foundation.org:33303 ([POD256 #101](../../raw/history/pod256/2026-01-14-pod256-101-hydrapool-hashdash-and-the-telehash-playbook-open.md)); every other source uses port 3333, so treat 33303 as a typo.

## Packaging for home-node platforms

- Start9: PR #33 (opened 2025-11-06) is still open; the maintainer wants Start9 and Umbrel packages to wrap the released ghcr images rather than carry separate Dockerfiles, and to avoid a hard Nix dependency; the contributor dropped the Nix parts by 2026-02-14 ([PR #33](../../raw/pools/hydrapool/2025-11-06-github-hydrapool-pr-33-add-start9-package.md)). NebulaMiner opened the PRs (November 2025) [#3323 · 2025-11-14 · NebulaMiner].
- Umbrel: on 2026-07-27 a community member got Hydrapool running as a native Umbrel app mining with a Bitaxe; jungly and econoalchemist asked for a PR so the images could be built into the release tooling ([Umbrel forum thread](../../raw/pools/hydrapool/2026-07-27-forum-hydrapool-on-umbrel.md)) [#5254 · 2026-07-27 · 256F Forum].
- Localization: PR #39 (opened 2026-01-31) proposes Chinese (zh-CN) Grafana dashboards and README ([PR #39](../../raw/pools/hydrapool/2026-01-31-github-hydrapool-pr-39-feat-add-chinese-zh-cn-localization.md)).

## Auditable hashrate & the pool-signature debate

- Pool signature is a 16-byte config option (default "hydrapool"); operators rebrand instances by editing config [#3866 · 2025-12-09 · jungly 🐕💸] [#3867 · 2025-12-09 · jungly 🐕💸] [#3869 · 2025-12-09 · jungly 🐕💸]
- Pool anonymity: 'leave it blank to not identify yourself' (like ckpool) — pool tags originally existed to advertise hashrate; counterpoint raised that reported pool hashrate isn't auditable (only Braiins tried making it feasible) [#4436 · 2026-02-17 · Boots Stribling] [#4437 · 2026-02-17 · jungly 🐕💸] [#4438 · 2026-02-17 · Steve Barbour]
- Hydrapool's answer: an optional public API endpoint letting anyone download all shares and audit the pool [#4443 · 2026-02-17 · jungly 🐕💸]
- mempool.space policy: a pool must solve one mainnet block before mempool.space will display its scriptsig; The Space's pool block appeared via Ocean/DATUM because Mechanic contributed Ocean-specific code to mempool — call to generalize it for Hydrapool and standardize [#3728 · 2025-11-29 · Ryan] [#3730 · 2025-11-29 · Ryan] [#3732 · 2025-11-29 · Ryan] [#3733 · 2025-11-29 · Ryan] [#3734 · 2025-11-29 · Ryan] [#3741 · 2025-11-29 · Skot Bitaxe]

## Contradictions & Open Questions

- **100 users: limit or default?** See the Disputed block under blockmaxweight.
- **Platforms.** README advertises Windows/MacOS binaries; changelog removed them in 2.5.3 ([README](../../raw/pools/hydrapool/github-256foundation-hydrapool.md); [CHANGELOG](../../raw/pools/hydrapool/github-hydrapool-changelog.md)).
- **Dates.** Changelog and GitHub publish dates disagree for several 2.x releases; the Telegram announcement of v2.0.1 for self-hosters came on 2026-01-07 [#4169 · 2026-01-07 · econoalchemist]. The changelog also lists two entries headed `[2.5.9] - 2026-06-1222` (sic).
- **Open bug.** Whether issue #44 affects mainnet operators running the official binary in PPLNS mode is unconfirmed by the maintainers as of 2026-10-09.

## See Also

- [Pool Payout Schemes](pool-payout-schemes.md)
- [Pool Choice for Heat Miners](pool-choice-for-heat-miners.md)
- [Public Pool](public-pool.md)
- [Pool Centralization & FPPS](pool-centralization-and-fpps.md)
- [Decentralized Pool Designs](../protocols/decentralized-pool-designs.md)
- [Stratum in Practice](../protocols/stratum-in-practice.md)
- [Solo Blocks Found by Open-Source & Home Miners](../history/open-source-solo-blocks.md)
- [256 Foundation Community Timeline](../history/256f-community-timeline.md)
- [Mujina](../firmware/mujina.md)
- [asic-rs and the Fleet-Tooling Stack](../mining-software/asic-rs.md)
