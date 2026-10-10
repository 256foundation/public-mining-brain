# Mining Nodes & Block Templates

> Sources: POD256 transcripts (2025-04 → 2026-09)
> Raw: [POD256 e090](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-15-e090.md); [POD256 e111](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-04-10-e111.md); [POD256 e113](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-04-22-e113.md); [POD256 e123](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-10-e123.md); [POD256 e124](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-17-e124.md); [POD256 e089](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-05-e089.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Overview

A miner's hashboards never see transactions: they hash an 80-byte header, and whoever builds the block template (normally the pool) decides what goes in the block. Mining to your own node moves that decision home. Through 2025 and 2026 the POD256 hosts kept returning to the same practical problem: a node has been the expensive, slow-to-sync part of a home mining stack, so few home miners run one. Their proposed fixes are pruned nodes, AssumeUTXO snapshots, Utreexo nodes such as Floresta, push-based templates from Bitcoin Core v30's IPC interface, and putting the node inside the miner's own control board. Pool-side designs that consume these templates are covered in [Decentralized Pool Designs](decentralized-pool-designs.md); the wire protocols are in [Stratum V1 & V2 in Practice](stratum-in-practice.md).

## Who builds the template

- Scott's framing: mining machines are far removed from transactions. They only run SHA-256 twice on an 80 byte header, and transaction selection is done by whoever builds the block template, which is the pool in ordinary pooled mining ([POD256 e099](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-12-17-e099.md)).
- Eco's point on DATUM and SV2: both let miners select transactions, but the pool still controls the coinbase and so the payouts, which limits how far either can decentralize ([POD256 e099](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-12-17-e099.md)).
- Average Gary's comparison: DATUM brings template creation and block propagation to the LAN, but Stratum V2 does all of that too, and DATUM Prime (OCEAN's server side) is not open source, while the DATUM gateway is ([POD256 e090](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-15-e090.md)).
- Scott's preferred architecture (April 2026): a one-click, DATUM-like app on the user's node that builds templates, talks SV2 upstream to any pool, and serves local miners over SV1. His critique of DATUM is that it only supports OCEAN ([POD256 e113](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-04-22-e113.md)).
- Ryan floated a "mini job source" in Mujina that connects straight to bitcoind with no pool layer; in Mujina, pool connections are called job sources ([POD256 e102](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-01-30-e102.md)). Agent P went further on a Bitaxe: with Codex he modified ESP-Miner so the Bitaxe builds its own template over RPC to his node, fetches the payout split from his GridPool node, and submits shares with no Stratum layer, all on the ESP32 ([POD256 e116](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-06-10-e116.md)).

### Economic nodes

- The hosts distinguish non-economic nodes (a plug-in node nobody mines or broadcasts through) from economic nodes connected to miners and wallets. They argued a home miner bought for heat, paired with a node, becomes an economic node by default ([POD256 e089](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-05-e089.md)).
- Average Gary: every economic node starts as a non-economic one, and hashrate makes a node "more densely economic" because it enforces its view by making blocks ([POD256 e090](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-15-e090.md)).
- The hosts' conclusion in the nodes-vs-miners debate (August 2026): both matter. Nodes validate, but blocks only come from miners pointing at nodes they choose, and a home node controls its local mempool and relay, not the network ([POD256 e123](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-10-e123.md)).
- A shared community setup: a Colorado group of about 80 members shares a space node, a Lightning node and a DATUM gateway for templates, with the DATUM showing about "a 120 workers" (2025-10-05) ([POD256 e089](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-05-e089.md)).

## Why home miners skip the node

- History: when the Bitaxe started, CKPool was incompatible with current Bitcoin Core's getblocktemplate after Con Kolivas paused maintenance, so there was no turnkey way to mine to your own node. Ben created Public Pool partly to fill that gap ([POD256 e111](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-04-10-e111.md)). Eco recalled that in 2020 it was "next to impossible for a non developer to mine to their own node" ([POD256 e112](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-04-15-e112.md)).
- Sync time on small hardware: Eco's Raspberry Pi four with four gigabytes of RAM took about sixteen days just to sync before Public Pool worked on it, and the hardware failed a couple of weeks later ([POD256 e090](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-15-e090.md)). His Raspberry Pi 4 IBD went from "four days" in an earlier article to "over two weeks" in 2025, which he attributed to UTXO-set growth; a Core developer suggested block validation may not be using the ARM CPU's hardware crypto accelerators ([POD256 e087](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-09-17-e087.md)).
- Scott said one motivation for Hydrapool was that running Public Pool plus a Bitcoin node on a Raspberry Pi was very painful ([POD256 e124](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-17-e124.md)).
- Cost: Scott put a full archival node at around $600 and noted it gives a miner no extra lottery tickets, so many pass on it ([POD256 e124](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-17-e124.md)). In e123 he said traditional nodes need a one-and-a-half or two terabyte NVMe SSD, which he called a non-starter for a cheap box ([POD256 e123](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-10-e123.md)).

## Making the node cheap

Scott's proposal (August 2026) is an "ideally $100 box" that home miners plug in and point their miners at, so they mine to their own node and build their own templates ([POD256 e123](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-10-e123.md)).

### Pruned nodes

Scott argued pruned nodes are fully validating and a perfectly good node to mine to. He said Con Kolivas (transcribed "Dr. Konkolovas") and Eric Voskuil of Libbitcoin confirmed this to him ([POD256 e123](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-10-e123.md)). In e124 he repeated that mining to a pruned node need not be expensive ([POD256 e124](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-17-e124.md)).

> **Status: Disputed** — are templates from a pruned node riskier?
> A commenter (John Stefanopoulos, per the hosts) worried that templates from pruned nodes risk including already-spent UTXOs. Scott countered that the disk-corruption risk is the same on archival nodes, and that he is not proposing flaky SD cards ([POD256 e123](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-10-e123.md)). Unresolved on the show. Note that the objection as relayed is about storage reliability, not about pruning itself, since a pruned node keeps the full UTXO set it validates against.

### AssumeUTXO

AssumeUTXO snapshots have their checksum baked into Bitcoin Core, so a pruned node can start mining right away while full block download and validation continue in the background. Any node can generate its own snapshot at any block height. Tyler tried a snapshot on a Raspberry Pi and said it helped ([POD256 e123](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-10-e123.md); [POD256 e124](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-17-e124.md)).

### Floresta and Utreexo

- Floresta is a Rust node built on Utreexo, a Merkle-tree accumulator of the UTXO set. In August 2026 it could not build block templates (only empty, coinbase-only blocks) and needed block-submission work; mining support is on its roadmap ([POD256 e123](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-10-e123.md); [POD256 e124](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-17-e124.md)).
- Scott's status report (e124): Floresta needs Utreexo proof servers, and only two seemed to exist (in Korea, 200 blocks behind the tip); proof servers take longer to sync than a Core IBD, and Floresta's AssumeUTXO snapshots were a couple hundred thousand blocks behind. A cheap-box plan would need many more proof servers ([POD256 e124](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-17-e124.md)).
- Scott synced a Floresta node on a low-end Raspberry Pi in twenty hours, versus a month or more normally. Floresta's lead developer (Davidson) showed him a gum-pack-sized embedded Linux board intended as a mining node ([POD256 e124](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-17-e124.md)).

### Other implementations

- Eric Voskuil's Libbitcoin reported full initial block download in less than an hour, on heavy-duty hardware ([POD256 e123](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-10-e123.md)).
- The hosts see Bitcoin Core's dominance as a risk mitigated by libbitcoinkernel work. Libbitcoin is an independent implementation; Knots is a Core fork with a single maintainer. Miners commonly run lightly customized Core builds (for example for template construction) without touching consensus ([POD256 e119](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-07-08-e119.md)).

## Getting templates out of the node

### Polling vs push: Bitcoin Core v30 IPC

Bitcoin Core v30 introduced a multi-process architecture, with node, wallet and GUI as separate processes talking over IPC. The Stratum V2 template provider uses this IPC interface to get push-based templates instead of polling getblocktemplate, with options such as fee deltas and template frequency, without Core having to maintain SV2 code ([POD256 e090](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-15-e090.md)). Earlier history: Stratum itself exists because Core's getwork RPC could not provide work fast enough for modern miners ([POD256 e112](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-04-15-e112.md)).

### blocknotify and the DATUM-on-StartOS gotcha

Every pool needs to learn about new blocks immediately (`blocknotify`). Per Dylan, DATUM on StartOS reportedly only worked with Knots, because Core on StartOS could not configure blocknotify to the DATUM service, even though the DATUM client is open source ([POD256 e124](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-17-e124.md)).

### Pool software on your node

- Hydrapool's prerequisites are a Bitcoin node and Docker; setup is a few commands to fetch config files, edit a few parameters and update bitcoin.conf to match ([POD256 e097](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-12-03-e097.md)). Eco's guide used Bitcoin Core via Snap and noted any node supporting RPC works, Knots included ([POD256 e100](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-12-31-e100.md)). See [Hydrapool](../pools/hydrapool.md).
- Con Kolivas made self-hosting CKPool solo a one-line command ([POD256 e087](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-09-17-e087.md)). Public Pool was later packaged for Umbrel and Start9 ([POD256 e111](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-04-10-e111.md)). See [Public Pool](../pools/public-pool.md).
- Average Gary's StartOS packaging of SV2: a solo pool is essentially stateless (no share tracking unless paying others), and Start9 automation can rotate to the next HD wallet address when a block pays the current one ([POD256 e090](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-15-e090.md)).
- Classroom variant: Ryan's "Dev Pool" Docker Compose stack runs a Bitcoin node on a private Signet with Hydrapool, a mempool explorer and a dashboard, and enforces its own network difficulty (retargeting about every 10 blocks for roughly thirty-second blocks) so CPU miners and Bitaxes can find blocks in a workshop ([POD256 e118](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-06-24-e118.md)).

## Mempool policy shapes your template

- Core vs Knots (as of 2025-10-05): Core proposed changes to default mempool and relay policy; Knots reverts them, exposes more parameters and ships a more restrictive default aimed at data "spam". Scott's objection was that Core was removing knobs rather than just changing defaults ([POD256 e089](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-10-05-e089.md)).
- Collateral damage from template filters: at launch OCEAN's template filter rejected Samourai Whirlpool TX0 transactions, which carry an OP_RETURN output ([POD256 e119](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-07-08-e119.md)).
- A node of your own also gives local data without third-party APIs. Scott suggested UTXOracle, which infers the BTC/USD price from round-dollar bands in on-chain amounts using only your node, as a privacy-preserving price feed for miner displays ([POD256 e110](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-04-01-e110.md)).

## Node inside the miner

- The LibreBoard has an M.2 NVMe slot. Scott suggested a 32 or 64 gig drive, which he guessed would be "in the $20 range", plus a pruned node could put a node inside the miner itself. FutureBit already ships a node plus miner, but the hosts called it expensive and slow to sync ([POD256 e123](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-10-e123.md)). In e124 he added that the LibreBoard's compute-module eMMC could hold a pruned or Utreexo node and avoid a two terabyte SSD ([POD256 e124](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-17-e124.md)).
- Eco's LibreBoard design goals: run a full node, run Hydrapool, and bridge to heating systems ([POD256 e113](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-04-22-e113.md)).
- Proof of concept: Schnitzel's battery-powered "Doom Axe" ran a LibreBoard with Mujina and Hydrapool plus a full node on an SSD, with a Bitaxe as the hashing device ([POD256 e114](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-05-13-e114.md)). See [Libre Board & Mining Control Boards](../hardware/libre-board-and-control-boards.md).
- Plug-and-play idea (Scott and Tyler): a home node running StartOS could auto-discover and provision a new miner over Bluetooth, pulling pool and address settings from a Hydrapool package config ([POD256 e095](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2025/2025-11-19-e095.md)).

## Contradictions & Open Questions

- Pruned-node template safety: see the Disputed block above ([POD256 e123](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-10-e123.md)).
- Floresta proof-server availability and template support were roadmap items as of August 2026 ([POD256 e124](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-17-e124.md)).
- Whether Core on StartOS can now set blocknotify for DATUM: the hosts said a recent StartOS overhaul "might be possible now" ([POD256 e124](../../raw/history/pod256/transcripts/2026-10-07/transcripts/2026/2026-08-17-e124.md)).

## See Also

- [Stratum V1 & V2 in Practice](stratum-in-practice.md)
- [Decentralized Pool Designs](decentralized-pool-designs.md)
- Different topic: [Hydrapool](../pools/hydrapool.md)
- Different topic: [Public Pool](../pools/public-pool.md)
- Different topic: [Libre Board & Mining Control Boards](../hardware/libre-board-and-control-boards.md)
- Different topic: [Mujina](../firmware/mujina.md)
