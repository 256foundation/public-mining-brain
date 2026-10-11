# Stratum V1 vs Stratum V2 - whats the real with the new protocol?

> Source: https://osmu.xyz/t/stratum-v1-vs-stratum-v2-whats-the-real-with-the-new-protocol/31
> Collected: 2026-10-10
> Published: 2026-06-01
> Registry ID: osmu-forum

warioishere | 2026-06-01 21:29:04 UTC | #1

# Stratum V2 Explained: SV1 vs SV2, Channel Types, Job Declaration, and the New SV2-UI

Since the SV1/SV2 debate keeps coming up on discord, here is a neutral, hands-on breakdown so we can stop relitigating the same points. Important framing up front: SV2 was designed primarily for *pooled* mining at scale, not specifically for solo. Most of its headline features only make sense in that context. This piece lays out what is actually in the spec, what each part solves, where it is relevant, and then introduces the new **SV2-UI** dashboard that ties it all together — including its move into the Umbrel App Store.

No religion either way. Just keeping the facts straight so you can weigh the real tradeoffs.

## A quick refresher: what Stratum V2 actually is

Stratum V2 (SV2) is the successor to the original Stratum protocol from 2012, back when mining was mostly a hobbyist affair. It was designed by Jan Čapek and Pavel Moravec (Braiins) together with Matt Corallo, and it is now maintained as a vendor-neutral, community-governed open-source effort. The reference codebase is the **Stratum Reference Implementation (SRI)**, developed in the open and supported through OpenSats.

The core idea: SV2 is not one monolithic protocol but a modular set of sub-protocols. You adopt only the components you need, and you can migrate incrementally without ripping out your existing setup. That modularity is the part most “SV1 vs SV2” arguments miss — the answer to “is SV2 worth it?” genuinely depends on which piece you are talking about and who you are.

## SV1 vs SV2 at a glance

| Aspect | SV1 (2012) | SV2 |
|---|---|---|
| Wire format | JSON-RPC plaintext | Binary, encrypted |
| Encryption | None (TLS optional, non-standard) | Noise_NX built in |
| Authentication | Workername / password | Static public-key pinning |
| Template control | Pool decides everything | Optional JDP for miner-side templates |
| Channel model | One connection = one worker | Standard / Extended / Group channels |
| Extensibility | Ad-hoc additions, broken compatibility | TLV extension system |
| Template fetching | getblocktemplate (Core) | Template Distribution Protocol (purpose-built) |
| Designed for | Single miner → pool | Pools, farms, proxies, decentralized template construction |

The headline differences are encryption, miner-side template control, a proper channel model, and a binary wire format. The rest of this article unpacks the ones that matter most in practice.

## The three sub-protocols

**1. Mining Protocol.** The direct SV1 successor. It handles share submission and job distribution between mining devices, proxies, and pools. This is the one sub-protocol every SV2 deployment needs — everything else is optional.

**2. Job Declaration Protocol (JDP).** This is the decentralization feature, and the one worth understanding properly (more below). It lets a miner or farm propose its *own* block template to a pool, instead of mining whatever transaction set the pool hands down.

**3. Template Distribution Protocol (TDP).** The efficient replacement for `getblocktemplate`. Instead of polling, your full node (or a Template Provider) *pushes* fresh templates at the right moments, for example when fees rise enough to justify a new template. Bitcoin Core exposes this via its experimental IPC mining interface, which we will come back to in the Umbrel section. No more templates in fixed intervals, and it can be freely configured. If the fee stays rather stable in the mempool, core sends less fresh templates, if the fee increases over a set threshhold, Core sends a new template right away without waiting.

## Channel types: Standard, Extended, Group

SV2 replaces SV1’s “one connection equals one worker” model with three channel types. The distinction sounds academic until you map it to actual hardware.

**Standard Channel — for end mining devices.** A Standard Channel receives only Standard Jobs and is what a single ASIC unit uses: a Bitaxe, a NerdQAxe, an industrial hashboard talking directly. The key constraint is search space. A Standard Channel covers roughly 280 TH/s of work per nTime value before it needs to roll nTime. For a home miner that is enormous headroom, so a Standard Channel is exactly right — simple, lightweight, no extranonce gymnastics. Disadvantage

A Standard Channel never handles the coinbase transaction itself. The upstream pool or proxy computes the full merkle root and sends it in the `NewMiningJob` message; the device only rolls the nonce, version bits (BIP320), and nTime over that fixed root. It receives neither the coinbase prefix/suffix nor the merkle path, so it cannot perform extranonce rolling and cannot influence the coinbase outputs — transaction selection and the payout destination are determined entirely upstream. This is also why a Standard Channel tops out around 280 TH/s per nTime value: without access to the coinbase, its only entropy is the nonce, version rolling, and nTime.

**Extended Channel — for proxies and high-hashrate setups.** An Extended Channel supports extranonce rolling, which lets a single channel parcel out a far larger search space across many devices in parallel. This is what you want when one logical connection sits in front of a lot of hashrate — a proxy aggregating a fleet, or an industrial setup that would otherwise blow past the per-channel search space. For a single home unit it is overkill; for a farm it is the whole point.

An Extended Channel, by contrast, receives the coinbase prefix and suffix plus the merkle path instead of a finished root. The downstream inserts and rolls its own extranonce, reconstructs the merkle root locally, and thereby unlocks a far larger search space.

**Group Channel — for proxies aggregating many devices.** A Group Channel lets a proxy bundle multiple Standard Channels together and distribute work efficiently using Extended Jobs. It is a pure farm/proxy feature: it exists so a proxy can manage hundreds of downstream miners without opening hundreds of independent upstream connections.

The short version: **Standard for the device in your hand, Extended for the proxy or big iron in front of a fleet, Group for the proxy that fans work out to many devices.** A solo miner with a Bitaxe never touches anything but a Standard Channel or and Extented Channel.

## Job Declaration: controlling your own block templates

This is the feature that actually addresses mining centralization, so it deserves more than a table row.

In the SV1 world, the pool decides everything that goes into a block. It chooses which transactions are included and which are left out. You contribute hashrate, the pool controls block composition. Across the network, a handful of pools end up deciding what the majority of Bitcoin’s block space looks like — and some of those pools are really proxies for others. That concentration is a censorship-resistance problem: whoever picks the transactions can, in principle, exclude them too.

The **Job Declaration Protocol** flips this. Two roles do the work:

- The **Job Declarator Client (JDC)** runs on *your* side. It builds a block template locally, against your own Bitcoin node, choosing your own transaction set. If you find a block, your JD-Client broadcasts the block to the network, and not the pool.
- The **Job Declarator Server (JDS)** runs on the pool side. It receives your declared template, keeps a synchronized mempool so it can reconstruct what you proposed, and the pool then limits itself to share accounting and verifies the payouts. The Pool just evaluates, if you did not exclude the pools fee output from the coinbase transaction.

The result is that you can keep the variance smoothing of pooled payouts, steady income instead of solo lottery, while reclaiming control over what goes into the blocks you help find. The pool no longer holds exclusive authority over transaction selection. This is the structural reason SV2 matters for Bitcoin beyond raw efficiency: it turns pooled miners from passive hashers back into active participants in block construction.

A few honest caveats. JDP only does anything if the pool you mine to runs a JDS, it is a two-sided feature. You also need to run your own Bitcoin node, because the whole premise is that *you* assemble the template. And for a pure solo miner with their own node, JDP is redundant: if you already have a node and you are not sharing payouts, you simply mine directly to your node and choose your own transactions anyway. JDP is the answer specifically for people who want pooled payouts *and* template sovereignty at the same time.

## How the node feeds the template: TDP and Bitcoin Core’s IPC interface

JDP and the Template Distribution Protocol need a fast, well-timed way to get fresh templates out of a full node. Modern pools do not busy-poll `getblocktemplat,` they have not for years. They subscribe to Bitcoin Core’s ZMQ notifications (typically `hashblock`) to learn the instant a new tip arrives, then call `getblocktemplate` to rebuild on top of it. That handles the “a block was just found, rebuild now” case well enough. What ZMQ plus `getblocktemplate` cannot do cleanly is the *economic* refresh: there is no efficient notification for “fees have risen enough that a new template is worth it” — the per-transaction topics (`rawtx`/`hashtx`) fire on every mempool event, far too noisy to drive template rebuilds — so pools fall back to rebuilding on a timer. On top of that, `getblocktemplate` serializes the full transaction set on every call and has no native push for a block-after-next template. Those are the real gaps, not “polling.”

Bitcoin Core 30.0 introduced an **experimental IPC mining interface** that closes exactly those gaps. Started with the right flags, the node listens on a Unix socket and lets external mining software request templates and submit solved blocks over IPC. Crucially, it *pushes* a fresh template the moment the tip changes **and** when fees cross a threshold, and it sends the lightweight header/merkle information first, deferring the heavy transaction data — none of which `getblocktemplate` plus ZMQ can do efficiently..

This IPC interface is the quiet enabler behind everything above. Without an efficient template feed, miner-side template construction would be too slow to be practic

## The rest of the spec, briefly

A few more pieces round out SV2. They matter, but they are not where the solo-vs-pool argument lives.

**Noise Protocol Framework (Noise_NX).** Authenticated encryption is built into the protocol, not bolted on like TLS-over-stratum. It provides confidentiality, integrity, authentication via static public-key pinning, and forward secrecy by default, with no PKI required — the pool publishes its authority pubkey and the miner pins it. The big practical win is preventing hashrate-hijacking man-in-the-middle attacks that swap pool credentials and redirect your work. Note that neither Noise nor TLS hides traffic timing or endpoint patterns; that is simply not what either is designed for.

**TLV extension system.** Optional fields use Type-Length-Value encoding and are negotiated per connection, so new features can be added backward-compatibly without breaking existing implementations or hard-forking the wire format.

**Binary framing.** SV2 drops SV1’s JSON-RPC for a lean binary format. The project cites roughly 60% bandwidth reduction for pools and 70% for miners; other sources put the range anywhere from 30% to 90% depending on workload. The honest read: this is real and meaningful at pool scale, but marginal for an individual home miner, since both SV1 and SV2 messages comfortably fit in single TCP packets at that volume.

## Honest take per use case

- **Solo home miner (Bitaxe / NerdQAxe to a pool):** Encryption is the main practical benefit. JDP does not apply — if you have your own node, mine directly to it. Bandwidth savings are irrelevant at single-miner scale, and there is no payout or performance change. No urgency to switch.
- **PPLNS pool participant:** JDP is the big one. Run a JDC against your own node, propose your own templates, and still get the variance smoothing of pooled payouts. This is where SV2 actually attacks mining centralization. Requires pool-side JDS support and your own node.
- **Industrial farm:** Extended and Group channels, Noise encryption against hashrate hijacking, and real bandwidth savings at scale. Add job declaration if the operator wants template sovereignty.
- **Pool operator:** Bandwidth savings, a modern security baseline, the TLV extension system for future-proofing, and a JDS to offer template decentralization as a feature.

Anyone selling SV2 as a magic latency or performance fix for individual home miners is overselling it. Anyone dismissing SV2 entirely because “it doesn’t matter for solo” is missing that solo was never the design target — and that the centralization problem it solves is a network-level concern that affects everyone.

## SV2-UI: a setup wizard and dashboard for the whole stack

All of the above is powerful and, until recently, fiddly to wire together by hand. The new **SV2-UI** project (from the stratum-mining organization) closes that gap. It is a unified setup wizard and monitoring dashboard for Stratum V2 mining, with its first tagged release (v0.1.0) landing in March 2026. Under the hood it is a React/TypeScript frontend with a small Node backend that orchestrates the SV2 containers for you via Docker.

What it does, in three parts:

**Setup wizard.** It walks you through configuration: choose solo or pool mining, pick a pool, set your expected hashrate for initial difficulty tuning, and enter your username or Bitcoin address. In Job Declaration mode it also helps you select your OS and Bitcoin network and auto-computes the IPC socket path to your node.

**Container orchestration.** Rather than asking you to hand-assemble roles, it starts and manages the Translator Proxy (the SV1-to-SV2 bridge, so existing SV1 firmware still connects) and — when you want template sovereignty — the JD Client. It handles graceful shutdown of those containers too.

**Monitoring dashboard.** Real-time stats: pool connection status, total hashrate from connected miners, active workers, shares sent to the pool, and a hashrate history chart.

It also maps cleanly onto the three deployment modes discussed above:

- **Pool mining (no JD):** `Pool ← Translator ← SV1 miners`
- **Pool mining with Job Declaration:** `Pool ← JDC ← Translator ← SV1 miners`, with your own Bitcoin Core node feeding templates into the JDC
- **Solo mining:** `Solo pool ← Translator ← SV1 miners`

On supported pools, the project already lists Braiins (pool / no-JD), the SRI Solo Pool (JD / solo), and **Blitzpool** for solo, PPLNS and Group-Solo mining, which is available in the wizard’s pool selection. That last one matters here: it means you can point the SV2-UI Translator at Blitzpool’s solo endpoint and get the full dashboard experience — connection status, hashrate, workers, shares — out of the box, without hand-editing TOML configs.

This is deliberately not an installation walkthrough — the project’s README covers the Docker commands and platform-specific socket mounting if you want them. The point here is conceptual: SV2-UI is the layer that finally makes the channel types, the translator, and optional job declaration approachable from a single screen.

## Coming to Umbrel

The piece that turns this from “nice for people comfortable with Docker” into “one click for everyone running a node” is the move into the **Umbrel App Store**. The Stratum V2 maintainers are actively working to publish SV2-UI as a native UmbrelOS app, tracked in the project’s issue thread for that effort. As of late May 2026 it is still pre-publication — there is a first round of testing underway and a handful of open issues to clear — but the direction is set: a one-click deploy that gives Umbrel node operators the SV2 dashboard without touching a terminal.

This dovetails with work on the node side. Umbrel’s Bitcoin Node app now ships Bitcoin Core v31.0 with an optional IPC mining interface for Stratum V2 apps — the same IPC mining interface described earlier. In other words, the two halves are converging: a node that can feed templates over IPC, and a one-click dashboard that can consume them. For anyone already running Bitcoin on an Umbrel box, that is the shortest path yet to experimenting with SV2 — and, with Job Declaration, to building and mining your own templates against your own node while still pointing hashrate at a solo/pplns pool like Blitzpool.

## Bottom line

SV2 is where the protocol layer is heading because it solves real problems — just not every problem for every user. For a solo home miner staying on SV1, there is no payout disadvantage today. For pooled mining at any scale, SV2 brings genuine technical and structural improvements, especially around encryption and template decentralization via JDP. The channel model is straightforward once you map it to hardware: Standard for your device, Extended and Group for proxies and farms. And the new SV2-UI — soon a one-click Umbrel app — is what finally makes all of it approachable, with Blitzpool already in the pool list for solo miners who want to try it.

Keep the facts straight, and the tradeoffs sort themselves out.

-------------------------

skot | 2026-06-19 01:04:08 UTC | #2

Excellent SV2 overview, thanks Wario!

I wish we had standard channels back when developing stratum in esp-miner.. that would have made things so much easier :sweat_smile:
