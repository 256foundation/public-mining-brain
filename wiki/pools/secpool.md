# SECPOOL

> Sources: secpool.com home shell + the site's own served app bundle (`/js/app.2efe2684.js` — user agreement, i18n strings) and the state of the secpool Zendesk help center (captured 2026-10-10); mempool.space pool-share API (1w/3m) and network state (2026-10-10)
> Raw: [SECPOOL home](../../raw/pools/secpool/2026-10-10-secpool-home.md); [SECPOOL fee/payout/help disclosures](../../raw/pools/secpool/2026-10-10-secpool-payout-fee-disclosures.md); [mempool pool share 1w](../../raw/pools/mempool/2026-10-10-mempool-pool-share-1w.md); [mempool pool share 3m](../../raw/pools/mempool/2026-10-10-mempool-pool-share-3m.md); [mempool network state](../../raw/pools/mempool/2026-10-10-mempool-network-state-snapshot.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Overview

SECPOOL is a BTC/SHA256 mining pool at secpool.com, self-described with the tagline "Safe & stable, your reliable choice" ([home capture](../../raw/pools/secpool/2026-10-10-secpool-home.md)). The site is a Vue.js single-page application — the static HTML serves only a shell — so everything recorded here comes from the site's own shell HTML and its served app bundle (UI strings and agreements) ([home](../../raw/pools/secpool/2026-10-10-secpool-home.md)). The site self-describes as trilingual (Chinese, English, Russian UI bundles baked into the app) with a USD/CNY currency selector, and its own meta keywords advertise PPS+ alongside BTC/SHA256/ASIC positioning ([home](../../raw/pools/secpool/2026-10-10-secpool-home.md)).

Scale (mempool.space, As-Of 2026-10-10): SECPOOL ranked #7 by blocks in the trailing week — 44 of 1,072 blocks, avg block match rate 97.93%, avg fee delta -0.0601 — and #7 over 3 months with 561 of 13,346 blocks (95.82% match rate) ([1w](../../raw/pools/mempool/2026-10-10-mempool-pool-share-1w.md); [3m](../../raw/pools/mempool/2026-10-10-mempool-pool-share-3m.md)). Match rate and fee delta are mempool.space's template-match observables, not pool-published fees ([1w](../../raw/pools/mempool/2026-10-10-mempool-pool-share-1w.md)). Network context: 1.02 ZH/s current hashrate, 58% through the epoch, next retarget estimated 2026-10-16 19:39 UTC (+3.67%) ([network state](../../raw/pools/mempool/2026-10-10-mempool-network-state-snapshot.md)).

As a third-party scale check, Hashrate Index's "Top 10 Bitcoin Mining Pools for 2026" lists SecPool at ~55 EH/s (4.9%) and says it "continues to expand its footprint across Asia, offering FPPS payouts" — consistent with the site's own FPPS/PPS/PPLNS claim; operator identity still unnamed ([fee/payout capture, context](../../raw/pools/secpool/2026-10-10-secpool-payout-fee-disclosures.md)).

The signal here includes absence (As-Of 2026-10-10): no numeric fee, no minimum-payout value, no operator identity and no SV2/DATUM mention anywhere on the public site — and the help center the site's own app links is closed ([home](../../raw/pools/secpool/2026-10-10-secpool-home.md); [fee/payout](../../raw/pools/secpool/2026-10-10-secpool-payout-fee-disclosures.md)).

## Fees and payout

- **Numeric fee: not disclosed on site.** The user agreement served in the app bundle defers to unpublished rates: "We have the right to charge fees for specific services in accordance with applicable agreements ('Rates'). Please refer to the relevant webpage for the specific applicable Rates." ([fee/payout capture](../../raw/pools/secpool/2026-10-10-secpool-payout-fee-disclosures.md)). A fee UI string exists ("费率标准" → "Fees"), but values are fetched post-login from the authenticated API — no static value anywhere ([fee/payout](../../raw/pools/secpool/2026-10-10-secpool-payout-fee-disclosures.md)).
- **Modes advertised:** the homepage feature bullet reads "Multiple modes: FPPS/PPS/PPLNS. Automatic payout distribution, real-time transparency. Enjoy stable earnings." ([home](../../raw/pools/secpool/2026-10-10-secpool-home.md)); the site's own keyword meta advertises PPS+, and earnings line items include PPAPPS / PPAPPLNS (FPPS block-reward and transaction-fee earnings shown as separate categories) ([home](../../raw/pools/secpool/2026-10-10-secpool-home.md); [fee/payout](../../raw/pools/secpool/2026-10-10-secpool-payout-fee-disclosures.md)).
- **Cadence:** "Daily payout settlement" ([home](../../raw/pools/secpool/2026-10-10-secpool-home.md)).
- **Promo and product strings:** a "0费率" ("0 Fee") zero-fee promotion banner exists in the homepage UI bundle — with no standing numeric fee published in the static HTML — and a "FPPS 固收" ("FPPS Fixed Earnings") product tier exists ([home](../../raw/pools/secpool/2026-10-10-secpool-home.md)).
- **Payout controls without values:** Minimum Payment / Payment time / Cut Payment Date fields exist, but no numeric threshold value is published statically ([fee/payout](../../raw/pools/secpool/2026-10-10-secpool-payout-fee-disclosures.md)). Multi-wallet proportional receiving ("多钱包按比例接收收益") and "On-chain payment optimization" — consolidating payouts across sub-accounts that share one address — are advertised ([home](../../raw/pools/secpool/2026-10-10-secpool-home.md)).
- Homepage earnings-widget metrics include PPS+ per-hashrate yesterday earnings ("PPS+ yesterday's earnings per 1 TH/s"), a PPS+ earn rate, average block value and Lucky % ([home](../../raw/pools/secpool/2026-10-10-secpool-home.md)).

## Custody and access

- **Custodial account model.** Email sign-up with 2FA, observer links, sub-accounts and worker management; rewards accrue in the registered SECPOOL account and are paid out to configured wallet addresses, with minimum-payment and payment-history fields throughout ([home](../../raw/pools/secpool/2026-10-10-secpool-home.md); [fee/payout](../../raw/pools/secpool/2026-10-10-secpool-payout-fee-disclosures.md)).
- **KYC machinery is present** in the app config (`SECPOOL_KYC_CRYPTOKEY`, `kycUid` session fields, SSO via account-beta.secpool.com), and a full KYC policy text (informed-consent and data-collection clauses) is bundled — indicating KYC is part of the account flow ([home](../../raw/pools/secpool/2026-10-10-secpool-home.md); [fee/payout](../../raw/pools/secpool/2026-10-10-secpool-payout-fee-disclosures.md)).
- **Operator identity: not disclosed.** No company name, address or registration information appears in the static shell or the app bundle; the agreement refers only to "本公司" ("the Company") ([home](../../raw/pools/secpool/2026-10-10-secpool-home.md)).
- **Support infrastructure is thinned.** The app bundle hard-codes its help center as `https://secpoolsupport-hc.zendesk.com`, but that Zendesk help center no longer serves — its root, `/hc/en-us`, `/hc/zh-cn` and the Help Center API all return 404/403 and redirect to `zendesk.com/help-center-closed` ("This help center no longer exists" flow) — so at collection time there was no publicly reachable fee or help page ([fee/payout](../../raw/pools/secpool/2026-10-10-secpool-payout-fee-disclosures.md)). Remaining surfaces: help@secpool.com (the site's own policy contact), an in-app AI assistant plus UDesk chat, and the Telegram alert bot `t.me/SECPOOL_alert_bot`; no public status/incident page was found ([home](../../raw/pools/secpool/2026-10-10-secpool-home.md); [fee/payout](../../raw/pools/secpool/2026-10-10-secpool-payout-fee-disclosures.md)).

## SV2 / DATUM

Not mentioned anywhere in the shell HTML or the app-bundle strings (As-Of 2026-10-10) ([home](../../raw/pools/secpool/2026-10-10-secpool-home.md)). The pool runs a standard custodial PPS-family account model; non-custodial or SV2/DATUM options are not mentioned on site ([fee/payout](../../raw/pools/secpool/2026-10-10-secpool-payout-fee-disclosures.md)).

## See Also

- [Luxor Pool](luxor-pool.md)
- [MARA Pool](mara-pool.md)
- [SpiderPool](spiderpool.md)
- [Braiins Pool](braiins-pool.md)
- [Pool Payout Schemes](pool-payout-schemes.md)
- [Pool Centralization & FPPS](pool-centralization-and-fpps.md)
- [Pool Choice for Heat Miners](pool-choice-for-heat-miners.md)
- [Stratum in Practice](../protocols/stratum-in-practice.md)
