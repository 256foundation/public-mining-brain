# Public Pool

> Sources: OSMU wiki, About Public Pool (captured 2026-10-07); mempool.space API on-chain verification (2026-10-07); @Public_Pool_BTC and @osmu_global posts on X, 2024 → 2026-07; GitHub ecosystem snapshots of benjamin-wilson/public-pool (2026-10-07); bitaxeorg/ESP-Miner GitHub issues and release notes, 2024-02 → 2026-06; 256 Foundation newsletter, 2025-05 → 2026-04; press and media research notes (collected 2026-10-07)
> Raw: [OSMU wiki: About Public Pool](../../raw/hardware/bitaxe-osmu/osmu-wiki-public-pool-about.md); [mempool.space on-chain verification](../../raw/history/256f-research/2026-10-07-mempool-onchain-block-verification.md); [X: open-source mining posts](../../raw/history/256f-research/2026-10-07-x-notable-open-source-mining.md); [X: @Public_Pool_BTC posts](../../raw/history/256f-research/2026-10-07-x-notable-public-pool.md); [GitHub contributor metrics](../../raw/history/256f-research/2026-10-07-github-ecosystem-contributor-metrics.md); [ESP-Miner #1438](../../raw/firmware/esp-miner/2025-12-10-github-esp-miner-issue-1438-100-error-rate-failed-to-receive.md)
> Updated: 2026-10-09
> As-Of: 2026-10-09
> Status: Draft

## Overview

Public Pool is a fully open-source solo Bitcoin mining pool: one repository holds both the stratum server and the web GUI. You can point miners at the official hosted instance at web.public-pool.io, or run your own copy at home; it was written from scratch for easy installation, a modern interface, maintainability and low complexity ([OSMU wiki](../../raw/hardware/bitaxe-osmu/osmu-wiki-public-pool-about.md)). It grew up alongside Bitaxe and the Open Source Miners United (OSMU) community — it was announced on Bitcointalk as "New - Open Source Solo Mining Pool", built with OSMU ([press research](../../raw/history/256f-research/2026-10-07-press-media-talks-research.md)) — and it is the default pool for NerdMiner ([OSMU wiki: Nerdminer](../../raw/hardware/bitaxe-osmu/osmu-wiki-nerdminer-about.md)). Because it is solo, whoever finds a block keeps the whole reward; most of the home-miner blocks of 2025–2026 carry a Public Pool coinbase tag (see [Block record](#block-record)). In June 2026 the hosted instance added Stratum V2.

## Hosted vs self-hosted

| | Hosted (web.public-pool.io) | Self-hosted |
|---|---|---|
| Who runs it | Ben (GitHub benjamin-wilson); the backend runs on hardware under his physical control and only the GUI relies on cloud infrastructure ([OSMU wiki](../../raw/hardware/bitaxe-osmu/osmu-wiki-public-pool-about.md)) | You, typically as an app on a home node |
| Install | Point the miner at the pool | Umbrel and Start9 app stores; OSMU claimed a local instance takes only 30sec to set up on Umbrel ([OSMU on X, 2024](../../raw/history/256f-research/2026-10-07-x-osmu-global-2024.md); [Public Pool on X, 2026-06-05](../../raw/history/256f-research/2026-10-07-x-notable-open-source-mining.md)) |
| Block template | The operator's node | Your own node |
| On-chain coinbase tag | `Public-Pool` | `Public Pool on Umbrel` (the Umbrel app) ([mempool.space verification](../../raw/history/256f-research/2026-10-07-mempool-onchain-block-verification.md)) |
| Failure mode | Operator outages hit everyone at once (see Reliability) | Your node, power and uplink |

The classic argument against self-hosted solo is stale-block risk from a poorly peered home node; see the Telegram debate summarized in [Pool Payout Schemes](pool-payout-schemes.md).

## Connecting a miner

- Stratum endpoints as listed by the pool: `stratum+tcp://public-pool.io:3333` and `stratum+tls://public-pool.io:4333` ([ESP-Miner #1438](../../raw/firmware/esp-miner/2025-12-10-github-esp-miner-issue-1438-100-error-rate-failed-to-receive.md)).
- Older guides use port 21496: it was the ESP-Miner factory default for a Supra 401 in 2024 ([ESP-Miner #447](../../raw/firmware/esp-miner/2024-11-03-github-esp-miner-issue-447-first-time-setup-change-the-messa.md)), the 256 Foundation's 2025 donor guide ([256F mining links, archived 2025-03-23](../../raw/history/256f-org/archive-20250323-256foundation-mining-links-html.md)) and an April 2026 newsletter ([newsletter, Apr 2026](../../raw/history/256f-newsletter/2026-04-11-assembling-freedom-23.md)). ESP-Miner v2.14.0 (2026-06-04) changed its public-pool default to 3333 ([ESP-Miner release notes](../../raw/firmware/esp-miner/github-esp-miner-releases.md); [Bitaxe release records](../../raw/hardware/bitaxe-osmu/bitaxe-firmware-release-records.md)).
- Username is your BTC address plus a worker name (`address.worker`); the newsletter describes the pool as having no fees ([newsletter, Apr 2026](../../raw/history/256f-newsletter/2026-04-11-assembling-freedom-23.md)).
- An invalid address in the username is rejected at `mining.authorize` with error 20, "Authorization validation error"; older AxeOS builds did not surface this to the user ([ESP-Miner #1358](../../raw/firmware/esp-miner/2025-11-16-github-esp-miner-issue-1358-show-pool-stratum-auth-error-on.md); [Hydrapool #35](../../raw/pools/hydrapool/2025-11-16-github-hydrapool-issue-35-mining-authorize-with-an-invalid-b.md)).
- Stratum V2 (hosted instance, since 2026-06-05): enable SV2 in the miner's advanced pool options and supply the pool's public key `9c4zpyJ2ndm4e8sP2uNc1VNCGxYjqaxWS6wUCjk8zFj6njFquH6`. The announcement followed SV2 support in ESP-Miner v2.14.0 and thanks warioishere for implementation details ([Public Pool on X, 2026-06-05](../../raw/history/256f-research/2026-10-07-x-notable-open-source-mining.md)).

## Architecture and stratum behaviour (for builders)

- **Repos.** `benjamin-wilson/public-pool` (server; created 2023-06-10; 451 stars, 158 forks, 19 contributors), `public-pool-ui` (created 2023-06-20; 57 stars, 73 forks) and `public-pool-app` (created 2024-07-12), snapshot 2026-10-07 ([GitHub metrics](../../raw/history/256f-research/2026-10-07-github-ecosystem-contributor-metrics.md)). There are no GitHub releases or tags; development is continuous on main ([release history](../../raw/history/256f-research/2026-10-07-github-release-history-key-repos.md)). In June 2026 the pool said months of improvements had been merged into the main sqlite branch and pushed to the Umbrel and Start9 stores ([Public Pool on X, 2026-06-05](../../raw/history/256f-research/2026-10-07-x-notable-open-source-mining.md)).
- **Implementation.** The stratum server is TypeScript; ESP-Miner developers cite its `StratumV1Client.ts` and `SuggestDifficultyMessage.ts` sources when settling protocol questions ([ESP-Miner #765](../../raw/firmware/esp-miner/2025-03-12-github-esp-miner-issue-765-add-reject-reason-tooltips.md); [ESP-Miner #686](../../raw/firmware/esp-miner/2025-02-02-github-esp-miner-issue-686-mining-suggest-difficulty-sends-i.md)).
- **Reject codes.** Errors come back as arrays such as `[21,"Job not found",""]` (stale) and code 23 `Difficulty too low`; those two are the most common rejects ([ESP-Miner #203](../../raw/firmware/esp-miner/2024-06-05-github-esp-miner-issue-203-roughly-10-of-shares-are-rejected.md); [ESP-Miner #765](../../raw/firmware/esp-miner/2025-03-12-github-esp-miner-issue-765-add-reject-reason-tooltips.md)). In 2024 a Bitaxe saw about 10% of shares rejected on public-pool in bursts of `Job not found` right after clean-jobs notifies ([ESP-Miner #203](../../raw/firmware/esp-miner/2024-06-05-github-esp-miner-issue-203-roughly-10-of-shares-are-rejected.md)).
- **`mining.suggest_difficulty`** takes its params as an array; public-pool's parser was cited as evidence that the array form is the consensus ([ESP-Miner #686](../../raw/firmware/esp-miner/2025-02-02-github-esp-miner-issue-686-mining-suggest-difficulty-sends-i.md)).
- **JSON-RPC envelope.** ckpool and public-pool include `"error":null` in the `mining.configure` response; a Miningcore pool that omitted the field broke Bitaxe parsing ([ESP-Miner #916](../../raw/firmware/esp-miner/2025-05-12-github-esp-miner-issue-916-incompatibility-with-miningcore-b.md)).
- **Duplicate shares.** On April 27 (2025) Public Pool patched a hole where it did not check for duplicate shares: scam NerdMiner firmware submitted each valid share five times to fake five times the hashrate ([newsletter, May 2025](../../raw/history/256f-newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md)). See [Pool Centralization & FPPS](pool-centralization-and-fpps.md) for other pool security incidents.

## Reliability (dated)

- Aug 2024: after public-pool went down for a fiber upgrade, Bitaxes did not reconnect without a manual reset — the socket appeared to stay up while no new work arrived. The ESP-Miner issue was closed 2024-12-27 as fixed by the new fallback-pool feature ([ESP-Miner #269](../../raw/firmware/esp-miner/2024-08-05-github-esp-miner-issue-269-mining-does-not-resume-after-publ.md)).
- Feb 2025: a user's zero accepted shares coincided with public-pool being down; it came back up the same thread ([ESP-Miner #691](../../raw/firmware/esp-miner/2025-02-03-github-esp-miner-issue-691-0-shares.md)).
- Contrast: a TCP RST from Antpool rebooted a Bitaxe, but the same miner on Public Pool (`public-pool.io:21496`) did not hit the problem ([ESP-Miner #105](../../raw/firmware/esp-miner/2024-02-09-github-esp-miner-issue-105-gracefully-handle-tcp-reset.md)).
- Community opinion on hosted reliability is split; see the Disputed block in [Pool Payout Schemes](pool-payout-schemes.md). Practical advice: configure a fallback pool (ESP-Miner supports one) — see [Bitaxe Troubleshooting](../getting-started/bitaxe-troubleshooting.md).

## Block record

mempool.space attributes blocks to Public Pool (pool id 161) by matching the coinbase regexes `Public-Pool` and `Public Pool on Umbrel`. On 2026-10-07 it listed exactly 8 blocks, with `totalReward` 2514629969 (in sats) and avgBlockHealth 99.8 ([mempool.space verification](../../raw/history/256f-research/2026-10-07-mempool-onchain-block-verification.md)):

| Height | UTC (on-chain) | Tag | Instance | Hardware as published |
|---|---|---|---|---|
| 888989 | 2025-03-23 00:30:28 | `Public Pool on Umbrel` | Self-hosted (first ever) | Umbrel forum analysis: "likely a Bitaxe" ([blocks research](../../raw/history/256f-research/2026-10-07-bitaxe-open-source-mining-blocks-found.md)) |
| 920440 | 2025-10-23 19:32:45 | `Public Pool on Umbrel` | Self-hosted (#2 self-hosted) | Six NerdQaxe++ plus one Avalon Q, ~130 TH/s total; the winning NerdQaxe++ rev6 was assembled by the Public Pool developer ([blocks research](../../raw/history/256f-research/2026-10-07-bitaxe-open-source-mining-blocks-found.md); [Public Pool on X](../../raw/history/256f-research/2026-10-07-x-notable-public-pool.md)) |
| 928985 | 2025-12-22 14:50:14 | `Public Pool on Umbrel` | Self-hosted | Not published |
| 937218 | 2026-02-18 11:22:29 | `Public Pool on Umbrel` | Self-hosted | Not published |
| 943466 | 2026-04-03 06:07:40 | `Public-Pool` | Hosted (first; "#5 overall") | NerdOctAxe / NerdQaxe — see Disputed below |
| 947073 | 2026-04-28 22:52:18 | `Public Pool on Umbrel` | Self-hosted | Not published |
| 948146 | 2026-05-06 09:28:35 | `Public Pool on Umbrel` | Self-hosted | Not published |
| 957382 | 2026-07-10 03:30:34 | `Public-Pool` | Hosted (second) | "By a lone Bitaxe" ([Public Pool on X](../../raw/history/256f-research/2026-10-07-x-notable-open-source-mining.md)) |

Near misses the pool has publicized: a 20T share from a NerdQaxe++ (2025-11-07), and a 59T share — 43% of network difficulty — from another NerdOCTAXE about 90 minutes after block 943466 ([Public Pool on X](../../raw/history/256f-research/2026-10-07-x-notable-public-pool.md)). Ahead of the February 2026 difficulty drop the pool posted that solo blocks were about to get 15% easier, target difficulty ~120T (same source). Full cross-pool table, odds framing and verification method: [Solo Blocks Found by Open-Source & Home Miners](../history/open-source-solo-blocks.md).

> **Status: Disputed** — what found block 943466?
> OSMU called it "the first known block of a NerdOctAxe" ([OSMU on X](../../raw/history/256f-research/2026-10-07-x-osmu-global.md)); the 256 Foundation newsletter describes the miner as a ~18.5 TH/s NerdQaxe ([newsletter, Apr 2026](../../raw/history/256f-newsletter/2026-04-11-assembling-freedom-23.md)). The chain records only the `Public-Pool` tag. Best assessment: a NerdOctAxe-class (NerdQaxe-family) miner; the exact model is unverified.

> **Status: Disputed** — block 868790
> A vendor blog claims a Bitaxe Gamma found 868790 on Public Pool; on-chain the coinbase reads `/ViaBTC/` and mempool.space attributes it to ViaBTC, not Public Pool ([mempool.space verification](../../raw/history/256f-research/2026-10-07-mempool-onchain-block-verification.md)). Best assessment: not a Public Pool block.

## Relationship to Bitaxe, OSMU and the 256 Foundation

- **Bitaxe defaults.** ESP-Miner shipped public-pool as the primary pool with solo.ckpool.org as fallback in its 2024 default config ([ESP-Miner #447](../../raw/firmware/esp-miner/2024-11-03-github-esp-miner-issue-447-first-time-setup-change-the-messa.md)), and v2.0.2 added a home-screen quick-link for public-pool users ([ESP-Miner release notes](../../raw/firmware/esp-miner/github-esp-miner-releases.md)).
- **Hardware.** The Public Pool developer also designs miners: he assembled the NerdQaxe++ rev6 that won block 920440 and publicly complained that sellers of his rev 6.1 design were not releasing their changes ([Public Pool on X](../../raw/history/256f-research/2026-10-07-x-notable-public-pool.md)); `benjamin-wilson/qaxe` hosts the NerdQAxe++ rev.7 branch ([GitHub metrics](../../raw/history/256f-research/2026-10-07-github-ecosystem-contributor-metrics.md)).
- **Growth.** In August 2025 the pool posted that network hashrate had grown 2X while open-source miner hashrate grew 10X, from the 201 Ultra to the Nerdqaxe++ ([Public Pool on X](../../raw/history/256f-research/2026-10-07-x-notable-open-source-mining.md)).
- **256 Foundation.** Before Hydrapool, the Foundation's donor guide had supporters mine to Public Pool with the POD256 address as username ([256F mining links](../../raw/history/256f-org/archive-20250323-256foundation-mining-links-html.md)); at Telehash #2 Public Pool ran a parallel instance paying the same address with roughly 120 Ph/s ([newsletter, Jun 2025](../../raw/history/256f-newsletter/2025-06-19-you-know-i-m-something-of-a-decentralized-pool-myself.md)). Hydrapool's authorize-error handling was benchmarked against Public Pool's ([Hydrapool #35](../../raw/pools/hydrapool/2025-11-16-github-hydrapool-issue-35-mining-authorize-with-an-invalid-b.md)). See [Hydrapool](hydrapool.md) for the PPLNS/multi-payout alternative.

## History

| Date | Event | Source |
|---|---|---|
| 2023-06-10 | `benjamin-wilson/public-pool` repo created | [GitHub metrics](../../raw/history/256f-research/2026-10-07-github-ecosystem-contributor-metrics.md) |
| 2023-08-18 | Launch announced on Bitcointalk, built with OSMU | [press research](../../raw/history/256f-research/2026-10-07-press-media-talks-research.md) |
| 2023-09-28 | First fork (an Ergo adaptation); 158 forks by 2026-10-07 | [fork genealogy](../../raw/history/256f-research/2026-10-07-github-fork-genealogy.md) |
| 2024-08-05 | Hosted outage exposes ESP-Miner reconnect gap | [ESP-Miner #269](../../raw/firmware/esp-miner/2024-08-05-github-esp-miner-issue-269-mining-does-not-resume-after-publ.md) |
| 2025-03-23 | First Public Pool block (888989, self-hosted on Umbrel) | [mempool.space verification](../../raw/history/256f-research/2026-10-07-mempool-onchain-block-verification.md) |
| Apr 27, 2025 | Duplicate-share (NerdMiner scam firmware) fix | [newsletter, May 2025](../../raw/history/256f-newsletter/2025-05-05-bitcoin-mining-will-not-be-decentralized-until-it-is-open-so.md) |
| 2025-10-23 | Second self-hosted block (920440) | [mempool.space verification](../../raw/history/256f-research/2026-10-07-mempool-onchain-block-verification.md) |
| 2026-04-03 | First hosted-instance block (943466) | [Public Pool on X](../../raw/history/256f-research/2026-10-07-x-notable-public-pool.md) |
| 2026-06-05 | Stratum V2 on the hosted instance; sqlite-branch update to Umbrel/Start9 | [Public Pool on X](../../raw/history/256f-research/2026-10-07-x-notable-open-source-mining.md) |
| 2026-07-10 | Second hosted block (957382), a lone Bitaxe | [mempool.space verification](../../raw/history/256f-research/2026-10-07-mempool-onchain-block-verification.md) |

## See Also

- [Solo Blocks Found by Open-Source & Home Miners](../history/open-source-solo-blocks.md)
- [Hydrapool](hydrapool.md)
- [Pool Payout Schemes](pool-payout-schemes.md)
- [Pool Choice for Heat Miners](pool-choice-for-heat-miners.md)
- [Pool Centralization & FPPS](pool-centralization-and-fpps.md)
- [Stratum in Practice](../protocols/stratum-in-practice.md)
- [Bitaxe Models](../hardware/bitaxe-models.md)
- [ESP-Miner / AxeOS](../firmware/esp-miner-axeos.md)
- [Bitaxe Troubleshooting](../getting-started/bitaxe-troubleshooting.md)
