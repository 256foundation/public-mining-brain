# Decentralized Pool Designs

> Sources: 256 Foundation Telegram group (t.me/the256foundation), 2024-02-24 → 2026-10-07
> Raw: [256F Telegram signal digest](../../raw/history/2026-10-08-256f-telegram-signal.md)
> Updated: 2026-10-08
> Status: Draft

## Overview

The design space beyond the hosted-pool model: template selection (DATUM), trustless payout schemes that avoid custodians, decentralized share accounting (GridPool, P2Poolv2, Dean's sketch), and the small protocol details — pool signatures, coinbase payout limits, midstate handling — that turn out to matter. Much of this is live 256F-adjacent engineering: Hydrapool shares core libs with P2Poolv2, and GridPool runs on an experimental Hydrapool fork.

## Template selection & DATUM

- DATUM (Luke Dashjr's template system) opened up template-creation options outside the big pools; observed with surprise that it wasn't built on Stratum v2 [#1308 · 2024-09-29 · Tyler Stevens] [#1310 · 2024-09-29 · econoalchemist]
- A mined block can carry a 'Mined by POD256'-style identifier via the template [#1311 · 2024-09-29 · Elijah Sanders]
- mempool.space policy: a pool must solve one mainnet block before mempool.space will display its scriptsig; The Space's pool block appeared via Ocean/DATUM because Mechanic contributed Ocean-specific code to mempool — call to generalize for Hydrapool and standardize [#3728 · 2025-11-29 · Ryan] [#3730 · 2025-11-29 · Ryan] [#3732 · 2025-11-29 · Ryan] [#3733 · 2025-11-29 · Ryan] [#3734 · 2025-11-29 · Ryan] [#3741 · 2025-11-29 · Skot Bitaxe]

## The custody problem in PPLNS

- Problem statement: PPLNS pools must custody funds when payouts don't fit in the coinbase; options debated — instant Lightning payouts, atomic swaps of shares for BTC, federated ecash custody [#1560 · 2025-01-31 · jungly 🐕💸] [#1561 · 2025-01-31 · jungly 🐕💸]
- Federated-mint idea: biggest hashers become federation members; combine with Super Testnet's bitpac contracts so a multisig treasury of top contributors governs payouts [#1562 · 2025-01-31 · Karl] [#1564 · 2025-01-31 · Karl]
- jungly's read: that is essentially the radpool design; but he'd 'seen enough question marks' around federations custodying pool funds [#1563 · 2025-01-31 · jungly 🐕💸] [#1565 · 2025-01-31 · jungly 🐕💸]
- Agreed MVP (became Hydrapool): pay directly from coinbase, no custody [#1605 · 2025-02-03 · econoalchemist]
- Coinbase payout-count limits are firmware-shaped: a block with 33 coinbase payout outputs cited as proof of demand for direct-from-coinbase schemes ('V3PS'); caveat: LuxOS caps coinbase addresses at 16, while other software handles 100+ easily [#1697 · 2025-03-07 · econoalchemist] [#1701 · 2025-03-07 · Elijah Sanders]

## Midstate handling (resolved November 2025)

> **Status: Disputed** — resolved
> Legacy lore said hosts must juggle midstates when sending jobs to ASICs. Resolved in-thread: BM1362-era-and-newer chips roll the version field on-chip, jobs are broadcast whole, and midstate management is an FPGA-era leftover [#3519 · 2025-11-21 · Reckless Apotheosis] [#3524 · 2025-11-21 · Ryan] [#3540 · 2025-11-21 · Reckless Apotheosis] [#3562 · 2025-11-21 · Skot Bitaxe] [#3578 · 2025-11-21 · Jstefanop].

## Bitmain I2C & level-shifting archaeology

- S17 hashboards have footprints for level-shifting opamps but they were never populated — 'Seems like Bitmain was concerned'; S19jPros have no level shifters, which makes sense because the IO voltage is much higher than the domain voltage [#2395 · 2025-06-08 · Skot Bitaxe] [#2396 · 2025-06-08 · Skot Bitaxe]
- Most new ASICs have on-chip buffers making external level shifters unnecessary, but Bitmain ASICs still need them — their much higher core voltage (1.2V) [#2432 · 2025-06-10 · Jstefanop] [#2450 · 2025-06-10 · Skot Bitaxe]
- T17 schematic archaeology: the I2C diode temperature sensor is controlled by the ASIC (same on the L7); the S21's BM1368 put the whole measurement circuit internal on-chip, then the BM1370 dropped it [#2566 · 2025-06-30 · Skot Bitaxe] [#2567 · 2025-06-30 · Mæstro Juergen] [#2571 · 2025-06-30 · Skot Bitaxe]
- The S21 Pro has level-shifted I2C lines running the whole hashboard, with special power tabs carrying a little bridge so I2C clk/data run underneath [#2575 · 2025-06-30 · Skot Bitaxe]
- Domain-crossing theories: the 0xAA55 preamble may be charge-pumping the AC-coupled signal; if ASIC IO is in the microamp range, plain dividers with 33 Ω resistors could do the level shifting [#2581 · 2025-06-30 · NebulaMiner] [#2590 · 2025-06-30 · Jstefanop]
- Relevant ASIC registers: 0x58 'IO Drive Strength' and 0x68 'UART Relay' (though neither seems able to change voltage) [#2587 · 2025-06-30 · Skot Bitaxe] [#2588 · 2025-06-30 · Skot Bitaxe]
- The S17 shows op-amp spots but the T17 has none — 'like Bitmain wasn't sure if it was going to work or not' [#2591 · 2025-06-30 · Mæstro Juergen] [#2592 · 2025-06-30 · Skot Bitaxe]

## GridPool (AgentP) — trustless share consensus (June 2026)

- GridPool added an SV1 endpoint for a 2% fee 'to encourage decentralization', running on an experimental fork of Hydrapool: stratum+tcp://stratum.main.gridpool.net:3333 [#4986 · 2026-06-19 · AgentP]; earlier admission: 'not offering Stratum V1 turns a lot of people away at the door' [#4955 · 2026-06-18 · AgentP]
- No sharechain to attack: 'Not possible on Gridpool, there is no sharechain to 51% attack' — it would give no advantage and disadvantage no one [#4991 · 2026-06-19 · AgentP] [#4992 · 2026-06-19 · AgentP]
- Consensus = the "heaviest Winners List" rule: a Winners List of 15 highest-difficulty sharers per template; nodes gossip, trustlessly verify other lists' share proofs (every PoW share with its Slot-0 attribution and headers), total the difficulty, and switch to the strongest list — analogous to Bitcoin's heaviest-chain rule [#5002 · 2026-06-25 · AgentP]
- Compact Share Relay: shares reduced to reconstruction info (Slot-0 address, nonce, time, version) <1200 bytes → single UDP packet, FIBRE-style; mitigates pool splits from last-second shares; untested as of June 2026 [#5003 · 2026-06-25 · AgentP]
- Censorship-resistance argument: a censoring node works on a lower-difficulty list, so even 99%-hashrate censorship should lose economically (author flags it needs more careful gaming) [#5004 · 2026-06-25 · AgentP]
- Pool-hopping rebuttal: the block finder keeps Slot-0 + all transaction fees on their own templates, so a lucky miner's rational move is to point more power at GridPool, not leave [#5000 · 2026-06-25 · AgentP]

> **Status: Disputed** — GridPool pool-hopping & 'loose consensus' (June 2026)
> jungly: classic pool-hopping exposure (win a high-difficulty share, then leave; TTLs punish honest miners) and sync-to-match is not a real consensus protocol — use something explicit à la radpool or p2pool's sharechain; 'I still think pool hopping will be exploited in grid pool' [#4998 · 2026-06-25 · jungly 🐕💸] [#5007 · 2026-06-25 · jungly 🐕💸]. AgentP: hopping 'strikes me as a strategy used by miners who don't understand statistics' — block finders keep Slot-0 + fees, so luck attracts more power, and the heaviest-Winners-List rule is the trustless consensus layer [#5000 · 2026-06-25 · AgentP] [#5002 · 2026-06-25 · AgentP]. Unresolved as of 2026-10-08; jungly notes P2Poolv2 independently landed on the same two ideas (finder bonus; sending work not blocks) [#5007 · 2026-06-25 · jungly 🐕💸].

## P2Poolv2 (2025-2026)

- Repo + community: github.com/p2poolv2/p2poolv2 with a Matrix room [#3333 · 2025-11-18 · jungly 🐕💸]
- Payout-scaling roadmap: Lightning atomic swaps first, then Ark (Steven Roose already has a solution in mind for the exchange problem) [#4461 · 2026-02-19 · jungly 🐕💸]
- Performance: jmeter load tests of the stratum server vs ckpool published in the repo [#4714 · 2026-04-26 · jungly 🐕💸]
- The original p2pool gave the block finder a bonus; P2Poolv2 does the same, and internally debates broadcasting the block vs sending only work (blinded work, like GridPool) [#5007 · 2026-06-25 · jungly 🐕💸]

## Dean's decentralized-pool sketch (November 2025)

- Fully decentralized pool concept: shares logged on a distributed side-network ledger; each Bitcoin block's overflow payout goes into a fresh multisig composed of the current node operators' keys (51% threshold to move funds, only share-submitting nodes included); Stratum V2 for encryption and miner template choice; no central operator [#3319 · 2025-11-13 · Dean]

## SV2 & related experiments

- Community pushing GridPool/Hydrapool to revisit Stratum v2 for encrypted channels and coinbase-address rotation; sv2-apps gallery shared; pool-sig-bytes-for-txs idea ('pool sig should be 4-byte RNG') [#4439 · 2026-02-17 · Deleted Account] [#4440 · 2026-02-17 · Deleted Account] [#4441 · 2026-02-17 · Deleted Account] [#4442 · 2026-02-17 · Deleted Account] [#4444 · 2026-02-17 · jungly 🐕💸]
- RescueMesh v0.1.0-alpha.1 (Marc): experimental, free, non-custodial coordination protocol for privacy-preserving bitcoin rescue research — regtest prototype with encrypted local storage, concealed transaction-set commitments, signed discovery announcements, Proof-of-Help receipts and a loopback-only Stratum V1 primitive; explicitly not a transaction accelerator, no mainnet yet; review wanted on hidden-template validity, miner incentives, DATUM/Stratum V2 integration and decentralized discovery [#5345 · 2026-08-12 · Marc]

## See Also

- [Hydrapool](../pools/hydrapool.md)
- [Pool Payout Schemes](../pools/pool-payout-schemes.md)
- [Mujina](../firmware/mujina.md)
- Different topic: [Pool Choice for Heat Miners](../pools/pool-choice-for-heat-miners.md)
