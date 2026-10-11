# Luxor Pool

> Sources: luxor.tech/mining landing page + docs.luxor.tech "Revenue & Payments" payout documentation (captured 2026-10-10); mempool.space pool-share API (1w/3m) and network state (2026-10-10)
> Raw: [Luxor mining home](../../raw/pools/luxor/2026-10-10-luxor-tech-mining-home.md); [Luxor docs: Revenue & Payments](../../raw/pools/luxor/2026-10-10-luxor-docs-revenue-payments.md); [mempool pool share 1w](../../raw/pools/mempool/2026-10-10-mempool-pool-share-1w.md); [mempool pool share 3m](../../raw/pools/mempool/2026-10-10-mempool-pool-share-3m.md); [mempool network state](../../raw/pools/mempool/2026-10-10-mempool-network-state-snapshot.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Overview

Luxor Pool is the Bitcoin mining pool of Luxor Technology, pitched on its landing page as a "U.S.-based, SOC 2 Type 2–certified, institutional-grade mining pool" with "transparent FPPS revenue", access to miner financing and real-time reporting ([mining home](../../raw/pools/luxor/2026-10-10-luxor-tech-mining-home.md)). Sign-up and pool operations live at app.luxor.tech, where a single account also covers the wider Luxor ecosystem: LuxOS firmware (300,000+ Bitcoin ASICs, >35 EH/s running it), Commander fleet management, a hardware trading desk ($865mm+ transacted 2022–2025) and hashrate derivatives (120+ participants, >$500mm OTC volume, up to 25 EH/s settled/day) ([mining home](../../raw/pools/luxor/2026-10-10-luxor-tech-mining-home.md)).

Scale (mempool.space, As-Of 2026-10-10): #8 by blocks in the trailing week — 35 of 1,072 blocks, avg block match rate 97.04%, avg fee delta -0.0635 — and #8 over 3 months with 438 of 13,346 blocks (96.11% match rate) ([1w](../../raw/pools/mempool/2026-10-10-mempool-pool-share-1w.md); [3m](../../raw/pools/mempool/2026-10-10-mempool-pool-share-3m.md)). The pool's own page displays 35,000+ BTC paid to its Bitcoin miners ("Paid to Bitcoin Miners"), 113 countries ("Global Miner Network") and >40 EH/s of pool hashrate ([mining home](../../raw/pools/luxor/2026-10-10-luxor-tech-mining-home.md)). Network context: 1.02 ZH/s current hashrate, 58% through the epoch, next retarget estimated 2026-10-16 19:39 UTC (+3.67%) ([network state](../../raw/pools/mempool/2026-10-10-mempool-network-state-snapshot.md)).

The disclosed client base is institutional: page testimonials name Genesis Digital (CTO Philip Salter), Sato, Soluna Holdings (an "Enterprise-Grade Pool Infrastructure" quote praising "compliance, SOC standards, and auditability") and MicroBT, with case studies listed for BitMine (derivatives hedging), TeraWulf (LuxOS deployment), a MicroBT ASIC purchase agreement and Soluna (pool infrastructure) ([mining home](../../raw/pools/luxor/2026-10-10-luxor-tech-mining-home.md)).

Capture note: docs.luxor.tech intermittently blocks plain curl via Cloudflare; the docs capture was taken via the page's own Markdown export, and the docs site is agent-friendly, offering a `/llms.txt` index and `.md`-appended URLs ([docs capture](../../raw/pools/luxor/2026-10-10-luxor-docs-revenue-payments.md)).

## Fees and payout

- **Scheme: FPPS.** The docs define it as paying consistent, predictable earnings based on contributed hashrate, incorporating both block rewards and transaction fees: "Pools using FPPS take on the variance risk, ensuring miners receive stable daily payouts." ([docs](../../raw/pools/luxor/2026-10-10-luxor-docs-revenue-payments.md); the homepage calls it "transparent FPPS revenue" — [mining home](../../raw/pools/luxor/2026-10-10-luxor-tech-mining-home.md)).
- **Fee: no numeric % published.** Luxor frames the fee as a spread on hashrate it buys: "we purchase hashrate from you at a discount to spot FPPS (discount to spot is commonly known as pool fees)" ([docs](../../raw/pools/luxor/2026-10-10-luxor-docs-revenue-payments.md)). Neither the docs nor the landing page publishes a numeric fee rate (As-Of 2026-10-10). Luxor reserves the right to change the FPPS Formula at any time, with changes tracked in its platform changelog ([docs](../../raw/pools/luxor/2026-10-10-luxor-docs-revenue-payments.md)).
- **The FPPS formula is fully published, per block height h:** `FPPS_h = (1/d_h) · (b_h + (1/|L|) · Σ_{i∈L} t_{h-i})` — where b is the block subsidy (currently 3.125 BTC), t a block's transaction fees, d the network difficulty at h, and L a 144-block lookback (~1 day) with fee outliers trimmed (excluding ≤p5 and ≥p95); reward divided by network difficulty yields the FPPS rate per unit hashrate ([docs](../../raw/pools/luxor/2026-10-10-luxor-docs-revenue-payments.md)).
- **Cadence:** three payout frequencies — daily, weekly (user picks the day) and monthly (first day of every month) — processed "shortly after 04:00 UTC" assuming balance requirements are met ([docs](../../raw/pools/luxor/2026-10-10-luxor-docs-revenue-payments.md)).
- **Thresholds:** a subaccount is paid when its balance exceeds the minimum withdrawal threshold plus the withdrawal fee. Published BTC values: threshold 0.001, withdrawal fee 0.000075 — the docs' own example is a balance above 0.001075 BTC ([docs](../../raw/pools/luxor/2026-10-10-luxor-docs-revenue-payments.md)). The same table lists LTC 0.1 (fee 0.001), DOGE 100 (0.01), Sia 100 (0.000001) and ZCash 0.1 (0.005) ([docs](../../raw/pools/luxor/2026-10-10-luxor-docs-revenue-payments.md)).
- Payment settings are defined per subaccount-currency (balance, next payout schedule, frequency, addresses) ([docs](../../raw/pools/luxor/2026-10-10-luxor-docs-revenue-payments.md)).

## Custody and access

- Subaccounts are "independent **Financial accounts**" where mining rewards are credited, each with its own rewards balance, payout settings (wallet addresses, minimum payout thresholds) and worker stats; multiple subaccounts per Workspace — a standard custodial pool-account model, with no non-custodial option mentioned ([docs](../../raw/pools/luxor/2026-10-10-luxor-docs-revenue-payments.md)).
- KYC is not discussed in the payments doc; workspaces and roles govern account access ([docs](../../raw/pools/luxor/2026-10-10-luxor-docs-revenue-payments.md)).
- No status page is linked from the captured pages; the docs promise that formula changes will be announced in the platform changelog, and the landing page footer links only to ToS/privacy ([docs](../../raw/pools/luxor/2026-10-10-luxor-docs-revenue-payments.md); [mining home](../../raw/pools/luxor/2026-10-10-luxor-tech-mining-home.md)).

## SV2 / DATUM

Not mentioned on luxor.tech/mining or in the Revenue & Payments documentation (As-Of 2026-10-10) ([mining home](../../raw/pools/luxor/2026-10-10-luxor-tech-mining-home.md); [docs](../../raw/pools/luxor/2026-10-10-luxor-docs-revenue-payments.md)).

## See Also

- [SECPOOL](secpool.md)
- [MARA Pool](mara-pool.md)
- [SpiderPool](spiderpool.md)
- [Braiins Pool](braiins-pool.md)
- [Pool Payout Schemes](pool-payout-schemes.md)
- [Pool Centralization & FPPS](pool-centralization-and-fpps.md)
- [On-Demand Hashrate](../hashrate-market/on-demand-hashrate.md)
- [Stratum in Practice](../protocols/stratum-in-practice.md)
