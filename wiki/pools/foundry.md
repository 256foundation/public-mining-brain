# Foundry USA Pool

> Sources: foundrydigital.com homepage and Foundry USA Pool product page (real-browser captures, 2026-10-10 — the site Cloudflare-403s plain curl); pool-faq.foundrydigital.com knowledge base, FPPS payout-methodology and fee-tier articles (captured 2026-10-10); mempool.space mining-pool share API, 1w window (2026-10-10); capture-loop A6 pool-landscape report (2026-10-10)
> Raw: [foundrydigital.com homepage](../../raw/pools/foundry/2026-10-10-foundrydigital-home.md); [Foundry USA Pool product page](../../raw/pools/foundry/2026-10-10-foundrydigital-usa-pool.md); [payout methodology + fee tiers (KB)](../../raw/pools/foundry/2026-10-10-pool-faq-foundrydigital-payout-methodology.md); [mempool.space pool share, 1w](../../raw/pools/mempool/2026-10-10-mempool-pool-share-1w.md); [capture report](../../raw/pools/foundry/_REPORT.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Overview

Foundry USA Pool is the Bitcoin mining pool of Foundry Digital LLC (site footer: "© 2026 Foundry Digital LLC"), marketed as a "U.S.-based, institutional-grade Bitcoin mining pool focused on security and reliability. Built by miners for miners" ([product page](../../raw/pools/foundry/2026-10-10-foundrydigital-usa-pool.md)). The parent company frames itself as "a decentralized infrastructure company" that sells "Enterprise Software for Institutional Miners", with a sibling product, the Foundry Zcash Pool, described as "Compliance-first infrastructure, transparent payouts, and dedicated US-based support" ([homepage](../../raw/pools/foundry/2026-10-10-foundrydigital-home.md)). The pool's own headline claim is "The world's #1 Bitcoin mining pool." ([product page](../../raw/pools/foundry/2026-10-10-foundrydigital-usa-pool.md)). For the capture window the block data agrees: mempool.space ranks Foundry USA first over the trailing week with 288 of 1072 blocks, zero empty blocks and a 99% average block match rate, ahead of AntPool (213) and F2Pool (183), against a pool-wide network estimate of 995.45 EH/s (As-Of 2026-10-10) ([mempool.space 1w](../../raw/pools/mempool/2026-10-10-mempool-pool-share-1w.md)).

Payout is FPPS only. The product page says the pool takes on mining risk and provides stable payouts via its FPPS payout mode, alongside a compliance stack: "KYC/AML of Pool Members", payouts "enabled by a market-leading payment processor, with address whitelisting", and "SOC 2 Type 2, and SOC 1 Type 2 accreditation" ([product page](../../raw/pools/foundry/2026-10-10-foundrydigital-usa-pool.md)). The knowledge base documents the full FPPS settlement math — daily PPS base times a trimmed-mean transaction-fee rate, "net of pool fees" ([payout methodology KB](../../raw/pools/foundry/2026-10-10-pool-faq-foundrydigital-payout-methodology.md)) — but publishes no fee percentage anywhere (see Fees and payout).

Capture posture, for anyone re-verifying: foundrydigital.com serves a Cloudflare challenge (HTTP 403) to plain curl, so both foundrydigital.com pages were captured via a real browser session, and the HubSpot knowledge base terminates plain-curl transfers mid-body ([homepage capture note](../../raw/pools/foundry/2026-10-10-foundrydigital-home.md); [capture report](../../raw/pools/foundry/_REPORT.md)).

## Fees and payout

- **Scheme.** Verbatim: "Foundry USA Pool pays out to all pool members according to the Full-Pay-Per-Share (FPPS) payout scheme." The product page repeats it twice ("stable payouts to miners through our" FPPS payout mode; "Consistent FPPS Payouts") ([product page](../../raw/pools/foundry/2026-10-10-foundrydigital-usa-pool.md); [payout methodology KB](../../raw/pools/foundry/2026-10-10-pool-faq-foundrydigital-payout-methodology.md)).
- **Fee percentage: not disclosed on site (checked the product page and the KB pricing-tier article, As-Of 2026-10-10).** The product page promises only a "Clear & consistent fee structure"; the KB capture note records that "no tier table or percentages are stated publicly (checked https://pool-faq.foundrydigital.com/how-is-my-pricing-tier-calculated)" ([product page](../../raw/pools/foundry/2026-10-10-foundrydigital-usa-pool.md); [payout methodology KB](../../raw/pools/foundry/2026-10-10-pool-faq-foundrydigital-payout-methodology.md)).
- **Fee-tier mechanism (the only public pricing documentation).** Foundry "evaluates pricing tiers every quarter based on your Group level hashrate" — all subaccounts in a Group count — with the "Average Quarterly Hashrate" computed by "summing the daily hashrate (as recorded by Foundry USA Pool™ in Daily Statistics) for the given quarter" and dividing by the days in the quarter; the tier set in a quarter applies to the next, and "It may take up to 10 business days into a new quarter for any pricing adjustments to take effect." ([payout methodology KB](../../raw/pools/foundry/2026-10-10-pool-faq-foundrydigital-payout-methodology.md))
- **Daily settlement.** Earnings for the previous UTC day are credited to the subaccount at 01:00:00 UTC; with Auto-Withdrawal on, the balance is "withdrawn to the selected whitelisted wallet addresses, once a day, during 9 AM to 5 PM UTC time" ([payout methodology KB](../../raw/pools/foundry/2026-10-10-pool-faq-foundrydigital-payout-methodology.md)).
- **FPPS math, as documented.** Step 1 sums accepted shares per worker into a daily PPS base; Step 2 computes an FPPS rate from observed blocks, with the transaction-fee numerator "excluding the highest 3 observations and lowest 3 observations, including empty blocks" and a denominator of block subsidies trimmed the same way; the worked example yields an FPPS rate of 105.000%; Step 3 multiplies base × rate, "net of pool fees" ([payout methodology KB](../../raw/pools/foundry/2026-10-10-pool-faq-foundrydigital-payout-methodology.md)).
- **Payout thresholds** (per a sibling KB article, "What are the minimum payout thresholds?", recorded in the capture notes): "minimum withdrawal 0.01 BTC (1M sats) per address on regular days; 2730 sats per address on the last day of each month", applied per address across sub-accounts ([payout methodology KB](../../raw/pools/foundry/2026-10-10-pool-faq-foundrydigital-payout-methodology.md)).

## Custody and access

- **Custodial, compliance-first account model.** "We also maintain SOC compliance and KYC for our Bitcoin mining pool members." Security & permissions bullets: "Payouts enabled by a market-leading payment processor, with address whitelisting", "KYC/AML of Pool Members", "Tiered account permissions", "Enhanced account authentication" ([product page](../../raw/pools/foundry/2026-10-10-foundrydigital-usa-pool.md)). The KB capture note summarizes the posture: rewards paid out by Foundry to KYC/AML'd members at whitelisted addresses via a third-party processor — a custodial model, US-based ([payout methodology KB](../../raw/pools/foundry/2026-10-10-pool-faq-foundrydigital-payout-methodology.md)).
- **Assurances.** "SOC 2 Type 2, and SOC 1 Type 2 accreditation"; "US-based company with dedicated account managers"; "Fully exportable data"; "Low rejected and stale share rates with servers and global relays across the world" ([product page](../../raw/pools/foundry/2026-10-10-foundrydigital-usa-pool.md)).
- **Foundry Donate.** Pool members "can allocate an amount of their earnings to automatically transfer" to nonprofits supporting Bitcoin core developers ([product page](../../raw/pools/foundry/2026-10-10-foundrydigital-usa-pool.md)).
- **Geography.** No geographic restrictions are stated on any captured page; the pitch is US incorporation and institutional compliance. Thresholds and account terms live behind the pool dashboard login (pool.foundrydigital.com), which was not captured ([capture report](../../raw/pools/foundry/_REPORT.md)).

## SV2 / DATUM

Zero Stratum V2 or DATUM mentions on any captured Foundry page (As-Of 2026-10-10). The homepage capture note records that "No fee, payout-scheme, threshold, custody, or SV2 terms are stated on the homepage itself"; the product-page note says "No Stratum V2 / DATUM mention on this page"; and the KB note that "no Stratum V2 / DATUM support mentioned anywhere in the KB nav or pool pages captured" — the KB's only Stratum section covers plain-Stratum proxying ([homepage](../../raw/pools/foundry/2026-10-10-foundrydigital-home.md); [product page](../../raw/pools/foundry/2026-10-10-foundrydigital-usa-pool.md); [payout methodology KB](../../raw/pools/foundry/2026-10-10-pool-faq-foundrydigital-payout-methodology.md)). Foundry does appear in Stratum V2 standardization politics, though — see [Pool Centralization & FPPS](pool-centralization-and-fpps.md) for its 2026 Stratum V2 Working Group membership.

## See Also

- [Pool Payout Schemes](pool-payout-schemes.md)
- [Pool Centralization & FPPS](pool-centralization-and-fpps.md)
- [AntPool](antpool.md)
- [F2Pool](f2pool.md)
- [ViaBTC](viabtc.md)
- [OCEAN](ocean.md)
- [Public Pool](public-pool.md)
- [Stratum in Practice](../protocols/stratum-in-practice.md)
- [Mining Nodes and Templates](../protocols/mining-nodes-and-templates.md)
