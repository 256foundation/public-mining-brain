# Braiins Pool

> Sources: braiins.com/pool + Braiins Academy (Rewards & Payouts; Stratum V2 manual), captured 2026-10-10 (single combined capture); mempool.space pool-share API (1w/3m) and network state (2026-10-10)
> Raw: [Braiins Pool overview & fees](../../raw/pools/braiins-pool/2026-10-10-braiins-pool-overview-fees.md); [mempool pool share 1w](../../raw/pools/mempool/2026-10-10-mempool-pool-share-1w.md); [mempool pool share 3m](../../raw/pools/mempool/2026-10-10-mempool-pool-share-3m.md); [mempool network state](../../raw/pools/mempool/2026-10-10-mempool-network-state-snapshot.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Overview

Braiins Pool is the rebranded Slush Pool — mining since 2010 and billed by the pool itself as "the world's longest running mining pool" ([overview capture](../../raw/pools/braiins-pool/2026-10-10-braiins-pool-overview-fees.md)). The product page's hero banner reads THE WORLD'S LONGEST RUNNING MINING POOL — 1.3M+ BTC Mined since 2010, with live stats of pool hashrate 13.91 EH/s, 177,359 active workers, 13,112 active users, all-time mined 1,294,383 BTC and reward system FPPS; hero claims also include "Instant LN Payouts", "Secure & Non-KYC" and "Most profitable FPPS" ([overview](../../raw/pools/braiins-pool/2026-10-10-braiins-pool-overview-fees.md)).

Scale (mempool.space, As-Of 2026-10-10): #10 by blocks in the trailing week — 14 of 1,072 blocks, avg block match rate 99.06%, avg fee delta -0.0932 — and #11 over 3 months with 204 of 13,346 blocks (96.74% match rate); a separate Braiins Solo pool (solo.braiins.com) holds rank #23 in the 3m table with 1 block ([1w](../../raw/pools/mempool/2026-10-10-mempool-pool-share-1w.md); [3m](../../raw/pools/mempool/2026-10-10-mempool-pool-share-3m.md)). Network context: 1.02 ZH/s current hashrate, 58% through the epoch, next retarget estimated 2026-10-16 19:39 UTC ([network state](../../raw/pools/mempool/2026-10-10-mempool-network-state-snapshot.md)).

Account feature set: multiple Financial Accounts with reward splitting in any ratio, customizable payout timing (daily/weekly/monthly), worker management with regex filtering and hashrate alerts, access profiles/API keys, API plus CSV/JSON export, a mobile app, and multilingual support (English, Russian, Spanish, Farsi, Chinese) ([overview](../../raw/pools/braiins-pool/2026-10-10-braiins-pool-overview-fees.md)).

## Fees and payout

- **Pool fee: 2.5% on FPPS; 0% when mining via Braiins OS.** The homepage pitches "0% pool fees when you mine with Braiins OS", and the Academy's Stratum V2 manual ties the 0% fee to mining via Braiins OS ([overview](../../raw/pools/braiins-pool/2026-10-10-braiins-pool-overview-fees.md)).
- **Transaction-fee proceeds are shared with miners.** The FPPS spec is documented with worked examples: every share is guaranteed a reward of the coinbase reward cut (proportional to shares at network difficulty) plus a transaction-fees cut (trimmed average block fee across the difficulty period), after which the 2.5% fee is subtracted — the docs' worked example: gross 0.00000200 BTC/TH/day → net 0.00000195 BTC at 2.5% ([overview](../../raw/pools/braiins-pool/2026-10-10-braiins-pool-overview-fees.md)).
- **Published payout table:** on-chain payout free at 0.005 BTC and above, 0.0001 BTC fee under 0.005 BTC; Lightning payouts free (min 1 satoshi, max 0.005 BTC — 500,000 sats); minimum payout 0.0002 BTC; minimum free payout 0.005 BTC; maximum payout 5 BTC ([overview](../../raw/pools/braiins-pool/2026-10-10-braiins-pool-overview-fees.md)).
- **Cadence:** "Payouts are created daily at 9.00 UTC"; on-chain confirmation typically takes 1-2 hours, while Lightning payouts are confirmed within a couple of minutes ([overview](../../raw/pools/braiins-pool/2026-10-10-braiins-pool-overview-fees.md)).
- Thresholds are customizable per Financial Account in Payout Settings; payout rules can be schedule-based (daily/weekly/monthly) or threshold-triggered, and an Immediate Payout can be requested once the balance exceeds the minimum ([overview](../../raw/pools/braiins-pool/2026-10-10-braiins-pool-overview-fees.md)).
- Braiins Pool runs its own Lightning node with channels to major wallet operators; failed or invoice-expired LN payouts are returned to balance ([overview](../../raw/pools/braiins-pool/2026-10-10-braiins-pool-overview-fees.md)).

## Custody and access

- The homepage states "Secure & Non-KYC" — no KYC gate is advertised for pool participation ([overview](../../raw/pools/braiins-pool/2026-10-10-braiins-pool-overview-fees.md)).
- Custodial account model: rewards accrue in pool Financial Accounts with balances and transaction ledgers; payouts are sent to external wallets on-chain or over Lightning ([overview](../../raw/pools/braiins-pool/2026-10-10-braiins-pool-overview-fees.md)).
- Who can join: open sign-up (Log in / Sign up on the page); no membership restrictions stated ([overview](../../raw/pools/braiins-pool/2026-10-10-braiins-pool-overview-fees.md)).
- No status page or incident history on the captured pages; the live stats widget (hashrate, workers, users, all-time mined) is the only health surface, and no incident notices were displayed on collection day ([overview](../../raw/pools/braiins-pool/2026-10-10-braiins-pool-overview-fees.md)).

## Stratum V2

- **Supported (As-Of 2026-10-10).** The Academy carries a dedicated Stratum V2 Manual: "Stratum V2 is a new protocol for pooled mining that we developed in collaboration with Bitcoin developer Matt Corallo", noting that Stratum V2 is implemented in the Braiins OS firmware ([overview](../../raw/pools/braiins-pool/2026-10-10-braiins-pool-overview-fees.md)).
- Pool side: default SV2 port 3336, with the pool public key in the URL path authenticating the endpoint (anti-man-in-the-middle protection for hashrate); Stratum V1 remains supported; SV2 requires Braiins OS — stock firmware is unsupported ([overview](../../raw/pools/braiins-pool/2026-10-10-braiins-pool-overview-fees.md)).
- **DATUM is not mentioned** in Braiins' SV2 documentation (DATUM is OCEAN's distinct SV2 template-delivery implementation); Braiins' docs note miners "will eventually" work on their own block templates ([overview](../../raw/pools/braiins-pool/2026-10-10-braiins-pool-overview-fees.md)).
- Legacy note: older firmware should use the legacy endpoint `v2.stratum.slushpool.com` to keep the 0% fee ([overview](../../raw/pools/braiins-pool/2026-10-10-braiins-pool-overview-fees.md)).

## See Also

- [SECPOOL](secpool.md)
- [Luxor Pool](luxor-pool.md)
- [MARA Pool](mara-pool.md)
- [SpiderPool](spiderpool.md)
- [Pool Payout Schemes](pool-payout-schemes.md)
- [Pool Centralization & FPPS](pool-centralization-and-fpps.md)
- [Public Pool](public-pool.md)
- [Stratum in Practice](../protocols/stratum-in-practice.md)
