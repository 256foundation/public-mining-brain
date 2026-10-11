# AntPool

> Sources: antpool.com homepage (real-browser capture, 2026-10-10 — the SPA kills plain-curl body transfers); ANTPOOL Zendesk help center, "Miners Settings & Fees" (published 2022-12-14) and "When is the daily payout time?" (published 2022-12-12), both captured 2026-10-10; mempool.space mining-pool share API, 1w window (2026-10-10); capture-loop A6 pool-landscape report (2026-10-10)
> Raw: [antpool.com homepage](../../raw/pools/antpool/2026-10-10-antpool-home.md); [Zendesk: Miners Settings & Fees + daily payout time](../../raw/pools/antpool/2026-10-10-antpool-help-fees-payout.md); [mempool.space pool share, 1w](../../raw/pools/mempool/2026-10-10-mempool-pool-share-1w.md); [capture report](../../raw/pools/foundry/_REPORT.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Overview

AntPool brands itself "World Leading BTC Mining Pool" and is the Bitmain-affiliated pool: the help center lists "BITMAIN, BITFUFU, ANTALPHA" as strategic partners, and the capture notes record that "AntPool is operated by Bitmain" ([homepage](../../raw/pools/antpool/2026-10-10-antpool-home.md); [Zendesk help](../../raw/pools/antpool/2026-10-10-antpool-help-fees-payout.md)). It is a large multi-coin pool: the homepage coin table self-reports 209 EH/s of BTC hashrate alongside BCH, LTC, ETC, ZEC, DASH, HNS, KDA, DGB, CKB, RVN, KAS, XMR, ALPH and Fractal Bitcoin, with the most recent BTC block at height 970856 captured 2026-10-10 19:49 (As-Of 2026-10-10) ([homepage](../../raw/pools/antpool/2026-10-10-antpool-home.md)). On mempool.space's trailing-week ranking AntPool is second with 213 of 1072 blocks and a 97.54% average block match rate, behind Foundry USA (288) and ahead of F2Pool (183) (As-Of 2026-10-10) ([mempool.space 1w](../../raw/pools/mempool/2026-10-10-mempool-pool-share-1w.md)).

Accounts are custodial pool accounts with a "three-level account system" — "Register with mailbox and you will have an account, sub-account, group, three-level account system" — plus shared-account authorization for farms, APP/Mail/SMS/WeChat alerting, and globally distributed nodes so that "miners will be automatically allocated to their nearest nodes to ensure the stability of mining and to avoid delay of hashrate submission." ([homepage](../../raw/pools/antpool/2026-10-10-antpool-home.md); [Zendesk help](../../raw/pools/antpool/2026-10-10-antpool-help-fees-payout.md))

Access is gated by an informed-consent modal covering sanctions and Chinese mainland residency (see Custody and access), and the site itself is a JS-heavy SPA whose English locale ships untranslated Chinese — the homepage "Transparent Earnings" bullet reads 支持FPPS、PPS、PPLNS等多种收益方式，每天自动分配和支付，收益数据实时透明。 with the capture's translation: "Supports FPPS, PPS, PPLNS and other earning methods, automatically distributed and paid daily, earnings data real-time and transparent." Block ages likewise render as "2h52min前" in EN mode ([homepage](../../raw/pools/antpool/2026-10-10-antpool-home.md)).

## Fees and payout

- **Payout schemes.** The help center states: "ANTPOOL supports four payment methods: PPS, PPLNS, FPPS (with effect from July 13, 2020)." — naming three, PPS, PPLNS and FPPS, selectable in Settings "based on your risk tolerance level" ([Zendesk help](../../raw/pools/antpool/2026-10-10-antpool-help-fees-payout.md)). The homepage's (untranslated) marketing names the same three with daily automatic settlement ([homepage](../../raw/pools/antpool/2026-10-10-antpool-home.md)).
- **Fee percentages: not disclosed in crawlable text (checked the Zendesk "Miners Settings & Fees" article, As-Of 2026-10-10).** The article's "Mining addresses and fees" section presents its fee/address table only as an embedded image — the capture note records "Percentages are NOT given in article text" ([Zendesk help](../../raw/pools/antpool/2026-10-10-antpool-help-fees-payout.md)). The article dates to December 14, 2022 (author "Susie"), so even its descriptive text is old: its FPPS description cites a "fixed block reward (current 6.25 BTC) + package transaction fee", a pre-2024-halving figure ([Zendesk help](../../raw/pools/antpool/2026-10-10-antpool-help-fees-payout.md)).
- **Legacy numbers, historical only.** A stale AntPool gitbook (antpool.gitbooks.io, ETH era) listed "PPS+ 4% / PPLNS 0% for BTC with 0.001 BTC minimum payout" — recorded in the capture notes as historical, and not confirmed anywhere current ([Zendesk help](../../raw/pools/antpool/2026-10-10-antpool-help-fees-payout.md); [capture report](../../raw/pools/foundry/_REPORT.md)).
- **Scheme descriptions (2022 article).** FPPS is full PPS — "The actual income of FPPS is not affected by the pool's luck." — with the payment distribution including the fixed block reward plus packaged transaction fees; PPLNS pays on the last N shares, with the note that "Transaction fees not paid out to miners are for maintenance and bonus for our engineers." ([Zendesk help](../../raw/pools/antpool/2026-10-10-antpool-help-fees-payout.md))
- **Thresholds and cadence.** "The default minimum payout value for Bitcoin is 0.005 BTC." (user-adjustable in Settings); other coins verbatim: "The minimum payout value is 0.001 for LTC, ZEC and DASH, 0.01 for BCH, 0.1 for XMC and 1 for BTM. Earnings less than the minimum payout value cannot be paid." Payment runs once daily: "Payment will only be initiated when your balance is above the minimum payout threshold", and accounts are processed at 9 o'clock daily — if the threshold is only reached after that day's settlement, payment waits until the next day (timezone unstated in the article; the capture note records legacy docs saying Beijing time) (As-Of 2026-10-10) ([Zendesk help](../../raw/pools/antpool/2026-10-10-antpool-help-fees-payout.md)).
- **Merged mining.** Configured per coin in Settings — for LTC, "configure DOGE wallet address for merged mining" ([Zendesk help](../../raw/pools/antpool/2026-10-10-antpool-help-fees-payout.md)).

## Custody and access

- **Custodial account model.** Rewards accumulate in the pool account and are paid out by AntPool to a wallet configured under Settings ([Zendesk help](../../raw/pools/antpool/2026-10-10-antpool-help-fees-payout.md)).
- **KYC, individual and institutional.** The same help-center section carries an "ANTPOOL Individual KYC User Guide" and an "ANTPOOL Institutional KYC User Guide" (existence noted in the capture; article bodies not captured) ([Zendesk help](../../raw/pools/antpool/2026-10-10-antpool-help-fees-payout.md); [capture report](../../raw/pools/foundry/_REPORT.md)).
- **Geography / sanctions gate.** The homepage consent modal requires users to confirm they are not residents of sanctioned or crypto-restricted jurisdictions, verbatim: "You are not a citizen or resident of Cuba, Iran, North Korea, Syria, or any other country or region sanctioned by relevant national governments or international institutions." and "You are not a citizen or resident of any country or region that restricts or prohibits cryptocurrency-related activities, including but not limited to the mainland of China." Users also "unconditionally and irrevocably waive the right of recourse" if local law makes use illegal (As-Of 2026-10-10) ([homepage](../../raw/pools/antpool/2026-10-10-antpool-home.md)).
- **Support surface.** Customer service email support@antpool.com; miner setup uses Bitmain's IP Reporter tool and the "sub-account.miner ID" username format ([homepage](../../raw/pools/antpool/2026-10-10-antpool-home.md); [Zendesk help](../../raw/pools/antpool/2026-10-10-antpool-help-fees-payout.md)).

## SV2 / DATUM

Zero Stratum V2 or DATUM mentions on the captured AntPool pages (As-Of 2026-10-10): the homepage capture note records "No Stratum V2 / DATUM mention on homepage", and the Zendesk capture note records the same for both help articles ([homepage](../../raw/pools/antpool/2026-10-10-antpool-home.md); [Zendesk help](../../raw/pools/antpool/2026-10-10-antpool-help-fees-payout.md)). AntPool is nonetheless among the pools that joined the Stratum V2 Working Group in 2026 — see [Pool Centralization & FPPS](pool-centralization-and-fpps.md).

## See Also

- [Pool Payout Schemes](pool-payout-schemes.md)
- [Pool Centralization & FPPS](pool-centralization-and-fpps.md)
- [Foundry USA Pool](foundry.md)
- [F2Pool](f2pool.md)
- [ViaBTC](viabtc.md)
- [OCEAN](ocean.md)
- [Stratum in Practice](../protocols/stratum-in-practice.md)
- [Mining Nodes and Templates](../protocols/mining-nodes-and-templates.md)
