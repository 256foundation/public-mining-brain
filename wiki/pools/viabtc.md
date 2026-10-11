# ViaBTC

> Sources: viabtc.com homepage (alternate-fetcher capture, 2026-10-10 — the Nuxt SPA kills plain-curl body transfers); viabtc.com/pricing fee schedule (captured 2026-10-10); mempool.space mining-pool share API, 1w window (2026-10-10); capture-loop A6 pool-landscape report (2026-10-10)
> Raw: [viabtc.com homepage](../../raw/pools/viabtc/2026-10-10-viabtc-home.md); [viabtc.com/pricing (Fees)](../../raw/pools/viabtc/2026-10-10-viabtc-pricing-fees.md); [mempool.space pool share, 1w](../../raw/pools/mempool/2026-10-10-mempool-pool-share-1w.md); [capture report](../../raw/pools/foundry/_REPORT.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Overview

ViaBTC is an all-in-one mining pool whose site pairs mining with exchange-like services: the homepage navigation runs "Pool, Assets, Loans, Resources, Tool, Blog, APP", and the marketing counts "serving 150+ countries and regions" and "reaching over one million users worldwide", with an AICPA SOC badge displayed in the footer ([homepage](../../raw/pools/viabtc/2026-10-10-viabtc-home.md)). On mempool.space's trailing-week ranking ViaBTC is fourth with 105 of 1072 blocks and a 98.91% average block match rate, behind Foundry USA (288), AntPool (213) and F2Pool (183) (As-Of 2026-10-10) ([mempool.space 1w](../../raw/pools/mempool/2026-10-10-mempool-pool-share-1w.md)).

Payout methods are "PPS+ and PPLNS payment methods" with what the homepage calls an "industry-leading hourly earnings payment method" and the "lowest orphan rate across the network for higher mining earnings" ([homepage](../../raw/pools/viabtc/2026-10-10-viabtc-home.md)). Note on scale stats: the homepage's live stats strip (pool hashrate, miners, earnings) loads via JS and only its labels were captured, so no self-reported ViaBTC hashrate is on file — the mempool.space ranking above is the independent count ([homepage](../../raw/pools/viabtc/2026-10-10-viabtc-home.md)).

## Fees and payout

- **Two methods, PPS+ default.** "ViaBTC pool supports two payment methods:" PPS+ and PPLNS, and "The default is" PPS+ — switchable in Settings "based on your risk tolerance" ([pricing](../../raw/pools/viabtc/2026-10-10-viabtc-pricing-fees.md)).
- **PPS+ is itemized: 4% + 2%.** The block-reward component is paid as PPS at a "4%" fee; the transaction-fee component is distributed PPLNS-style at "2%". Verbatim framing of why PPS+ costs more: "Since miners do not bear the risk, the pool assumes the risks of pool luck and orphaned blocks, and therefore charges a relatively higher fee." The PPS block-reward portion is scheduled to "Pay out every hour based on the current difficulty"; the fee portion is "Distributed based on each user's share of the pool's total hashrate over the past 5 difficulty rounds after the block receives 6 confirmations." (As-Of 2026-10-10) ([pricing](../../raw/pools/viabtc/2026-10-10-viabtc-pricing-fees.md)).
- **PPLNS mode: 2% flat.** Under PPLNS, rewards (block reward plus transaction fees) are distributed "over the last N difficulty rounds when a valid block is found" at a 2% fee, with the pool's own caveat: "Earnings may fluctuate, but long-term average returns are generally higher." ([pricing](../../raw/pools/viabtc/2026-10-10-viabtc-pricing-fees.md)).
- **Payout-fee claim.** The homepage advertises "zero-fee payouts" for mining earnings under Assets Management ([homepage](../../raw/pools/viabtc/2026-10-10-viabtc-home.md)).
- **Payout threshold: not stated on /pricing (checked 2026-10-10).** The pricing capture note records a help-center default of "documented default BTC minimum payout is 0.001 BTC" but flags it "not re-verified here" — treat the 0.001 BTC figure as unverified on this capture ([pricing](../../raw/pools/viabtc/2026-10-10-viabtc-pricing-fees.md); [capture report](../../raw/pools/foundry/_REPORT.md)).
- **Garbled section — merged mining fees.** The /pricing page's Merged Mining section is present but its "content rendered as image/JS in capture — no text", so merged-mining fee percentages could not be captured and are not quoted here ([pricing](../../raw/pools/viabtc/2026-10-10-viabtc-pricing-fees.md); [capture report](../../raw/pools/foundry/_REPORT.md)).

## Custody and access

- **Custodial pool account with built-in financial services.** Assets Management offers a "Built-in multi-cryptocurrency wallet for deposits and withdrawals" and "crypto-to-crypto trading with Auto Conversion"; Financial Services offers "Collateral-Pledged Loans: borrow and repay anytime for flexible funding" — rewards land in a ViaBTC-held account by default ([homepage](../../raw/pools/viabtc/2026-10-10-viabtc-home.md)).
- **Assurance and support posture.** AICPA SOC badge displayed; help center at support.viabtc.com (Zendesk); the homepage FAQ list covers worker management, Smart Mining, Auto Conversion, watcher URLs, VIP fee applications and Fee Coupons ([homepage](../../raw/pools/viabtc/2026-10-10-viabtc-home.md)).
- **KYC/geography: not stated on the captured pages** (homepage and /pricing) — no KYC, threshold, or geographic-eligibility text was captured; those live in the help center and terms, which were not captured ([homepage](../../raw/pools/viabtc/2026-10-10-viabtc-home.md); [pricing](../../raw/pools/viabtc/2026-10-10-viabtc-pricing-fees.md); [capture report](../../raw/pools/foundry/_REPORT.md)).

## SV2 / DATUM

Zero Stratum V2 or DATUM mentions on the captured ViaBTC pages (As-Of 2026-10-10): the homepage capture note records "No Stratum V2 / DATUM mention on homepage" and the pricing note the same for /pricing ([homepage](../../raw/pools/viabtc/2026-10-10-viabtc-home.md); [pricing](../../raw/pools/viabtc/2026-10-10-viabtc-pricing-fees.md)).

## See Also

- [Pool Payout Schemes](pool-payout-schemes.md)
- [Pool Centralization & FPPS](pool-centralization-and-fpps.md)
- [Foundry USA Pool](foundry.md)
- [AntPool](antpool.md)
- [F2Pool](f2pool.md)
- [OCEAN](ocean.md)
- [Stratum in Practice](../protocols/stratum-in-practice.md)
- [Mining Nodes and Templates](../protocols/mining-nodes-and-templates.md)
