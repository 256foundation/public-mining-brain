# Pool Payout Schemes

> Sources: 256 Foundation Telegram group (t.me/the256foundation), 2024-02-24 → 2026-10-07
> Raw: [256F Telegram signal digest](../../raw/history/2026-10-08-256f-telegram-signal.md)
> Updated: 2026-10-08
> As-Of: 2026-10-08
> Status: Draft

## Overview

How pools actually pay miners, why custody shows up, and what the community considers the honest trade-offs. The recurring 256F position: any pooled pool is a middleman, and there is a cost to that 'in both money and freedom' [#780 · 2024-04-07 · Skot Bitaxe] — which is why direct-from-coinbase payout designs get so much attention here.

## The core mechanics (community explainer)

- FPPS requires a custodian because it pays a constant expected value over time; PPLNS instead pays on share value submitted in a window near when a block is found [#717 · 2024-04-06 · Brett Rowan]
- Pooling math: 1% of hashrate in a 50% pool → the pool finds ~50% of blocks and you get 2% of each; same expected value as solo, just smoothed [#737 · 2024-04-06 · Brett Rowan]
- SPPLNS (proposed for a trustless public pool): pay the highest-n miners directly from the coinbase, with everyone else rotating through remaining coinbase payout slots — slightly more stable than solo, no custodian [#719 · 2024-04-06 · Brett Rowan] [#729 · 2024-04-06 · Brett Rowan] [#730 · 2024-04-06 · Brett Rowan]
- 'Solo pool' = hosted solo/lottery mining: whole block or nothing; the value-add is that they run the node + stratum job generation so you don't have to [#716 · 2024-04-06 · Skot Bitaxe] [#734 · 2024-04-06 · Skot Bitaxe] [#740 · 2024-04-06 · Brett Rowan]
- Large pools' difficulty algorithms aren't built for kh/s-class devices (NerdMiner/Bitaxe), which is why tiny hashers get rejected on big pools [#749 · 2024-04-06 · Jstefanop]

## Solo & coinbase-direct pools in the wild

- Laurentia Pool (spun up by Dr. Con & MFB) pays directly from the coinbase; been around a few years as of April 2024 [#762 · 2024-04-06 · econoalchemist]
- FutureBit funded a FOSS grant that modernized solo.ckpool for individual use; ships in Apollo OS 2, runs on any hardware, efficient enough for a Raspberry Pi; one user ran a 10 PH / 100-worker farm off a single Apollo [#953 · 2024-05-17 · Jstefanop] [#954 · 2024-05-17 · Jstefanop] [#962 · 2024-05-18 · Jstefanop] [#963 · 2024-05-18 · Jstefanop]
- Public Pool is another self-hosted solo pool option; the classic argument against self-hosted solo is stale-block risk, which a cloud service could mitigate with proper peering [#966 · 2024-05-19 · Skot Bitaxe] [#969 · 2024-05-19 · Skot Bitaxe]
- Wilson pool (Wilson Mining, factory-direct Whatsminer sellers): low pool fees, 130 TH minimum payout; community members pointed hashrate at it to test in mid-2024; they also run a proxy for smaller miners [#1031 · 2024-06-05 · Barnminer Barnmyna] [#1028 · 2024-06-05 · B] [#1048 · 2024-06-08 · Barnminer Barnmyna]
- Block 899826 mined by Solo CK for ₿3.15133486 (June 2025); szarka noted CK's template was just default Core — 'any block not mined by Antpool or Foundry is a good block' [#2317 · 2025-06-04 · ₿usiness Cat] [#2324 · 2025-06-04 · szarka] [#2329 · 2025-06-04 · szarka]
- Who mines solo and why: speculation that big solo-block hash is often rented lottery mining [#2338 · 2025-06-05 · Steve Barbour] [#2331 · 2025-06-04 · Elijah Sanders]

> **Status: Disputed** — Public Pool reliability (April 2025)
> One-word endorsement from econoalchemist [#1787 · 2025-04-06 · econoalchemist] vs Barnminer: loves it for low-hashrate use but the hosted service has had notable disruptions, is 'not the level of CKPool by any means', and the public instance had never mined a block (self-hosted instances have) [#1808 · 2025-04-13 · Barnminer Barnmyna]. For easy solo mining at ~3 PH, Public Pool's web UI first, dockerized self-hosting later [#1787 · 2025-04-06 · econoalchemist] [#1788 · 2025-04-06 · econoalchemist] [#1789 · 2025-04-06 · econoalchemist] [#1792 · 2025-04-06 · econoalchemist].

## Centralization: three distinct risks (April 2024 debate)

- Taxonomy (Alex Brammer): pool-template concentration = censorship risk; pool-stratum concentration = 51%-attack (hashrate control) risk; too much hash under one legal entity = a third vector [#812 · 2024-04-18 · Alex Brammer] [#814 · 2024-04-18 · Alex Brammer] [#820 · 2024-04-18 · Zack Bomsta]
- Debate consensus: control of block creation / censorship is the bigger near-term threat, not an outright 51% attack [#819 · 2024-04-18 · Jstefanop] [#835 · 2024-04-18 · Jstefanop] [#838 · 2024-04-18 · Jstefanop] [#836 · 2024-04-18 · Alex Brammer]

> **Status: Disputed** — 51% attack feasibility
> Jstefanop: 51% attacks are "fud vestiges" of early mining; a successful reorg now takes roughly a thousand exahash [#827 · 2024-04-18 · Jstefanop] [#833 · 2024-04-18 · Jstefanop]; Alex Brammer countered with a well-funded pool hiding 51% behind proxy front-ends [#828 · 2024-04-18 · Alex Brammer] [#836 · 2024-04-18 · Alex Brammer] [#837 · 2024-04-18 · Alex Brammer]; landed on 'not impossible just much harder', with template censorship the bigger threat [#838 · 2024-04-18 · Jstefanop].

- AntPool is offshore but not beyond US reach: one regulated US customer threatening to move hashrate forces compliance; regulators could bar US miners from pools processing any sanctioned transactions; AntPool could serve separate templates to US customers but has historically been poor at it [#844 · 2024-04-19 · Skot Bitaxe] [#860 · 2024-04-19 · Skot Bitaxe] [#861 · 2024-04-19 · Skot Bitaxe] [#862 · 2024-04-19 · Skot Bitaxe]
- US tolerance of domestic mining expansion read as strategic: Washington wants hashrate under US-controlled companies [#842 · 2024-04-19 · Skot Bitaxe] [#843 · 2024-04-19 · Skot Bitaxe]
- The pool-capture scenario is a core argument for FOSS mining infrastructure 'needed yesterday' [#853 · 2024-04-19 · econoalchemist] [#849 · 2024-04-19 · econoalchemist]

## See Also

- [Hydrapool](hydrapool.md)
- [Decentralized Pool Designs](../protocols/decentralized-pool-designs.md)
- [On-Demand Hashrate](../hashrate-market/on-demand-hashrate.md)
- Same topic: [Pool Choice for Heat Miners](pool-choice-for-heat-miners.md)
