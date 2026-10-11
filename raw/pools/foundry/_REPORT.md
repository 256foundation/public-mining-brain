# Capture Report — major mining pools (capture-loop A6, pool landscape)

> Agent: pool-landscape capture subagent
> Date: 2026-10-10
> Scope: Foundry USA Pool, AntPool, F2Pool, ViaBTC, OCEAN (home + fee/payout terms page each)
> Registry IDs: foundry-pool, antpool, f2pool, viabtc, ocean-pool

## Captured (11 files)

### Foundry USA Pool (raw/pools/foundry/) — 3
1. `2026-10-10-foundrydigital-home.md` — foundrydigital.com homepage (browser capture; curl 403 Cloudflare)
2. `2026-10-10-foundrydigital-usa-pool.md` — pool product page foundrydigital.com/foundry-usa-pool-3/ (FPPS named; KYC/AML; SOC 1/2; fee % not numeric)
3. `2026-10-10-pool-faq-foundrydigital-payout-methodology.md` — pool-faq.foundrydigital.com FPPS methodology + fee-tier note + thresholds (0.01 BTC / 2730-sat month-end)

### AntPool (raw/pools/antpool/) — 2
4. `2026-10-10-antpool-home.md` — antpool.com home (SPA; 209 EH/s; FPPS/PPS/PPLNS in untranslated Chinese; sanctions consent gate)
5. `2026-10-10-antpool-help-fees-payout.md` — Zendesk help: Miners Settings & Fees + daily payout time (fee table is an image; 0.005 BTC default min payout; daily 9:00 processing; individual+institutional KYC articles)

### F2Pool (raw/pools/f2pool/) — 2
6. `2026-10-10-f2pool-home.md` — f2pool.com home (per-coin fee banners live on page: BTC FPPS 4% / PPLNS 2%; merged mining)
7. `2026-10-10-f2pool-help-payout-schemes-thresholds.md` — Zendesk fee/scheme/threshold table (updated 2026-10-09) + payout-window and no-payout-fee cross-refs

### ViaBTC (raw/pools/viabtc/) — 2
8. `2026-10-10-viabtc-home.md` — viabtc.com home (PPS+/PPLNS named; zero-fee payouts claim; AICPA SOC badge)
9. `2026-10-10-viabtc-pricing-fees.md` — /pricing documented fee schedule (PPS+ = 4% PPS + 2% PPLNS-txfee; PPLNS = 2%; hourly PPS payout; 5-difficulty-round window; 6 confirmations)

### OCEAN (raw/pools/ocean/ — NEW FILES ONLY; existing 5 DATUM-docs captures untouched) — 2
10. `2026-10-10-ocean-xyz-home.md` — ocean.xyz home (21.74 Eh/s banner; block 970835 4h ago; 2%/1% DATUM fee; TIDES; non-custodial; no KYC; SOC 1/2 Type 2; Lightning BOLT12)
11. `2026-10-10-ocean-xyz-docs-terms.md` — /docs/terms ToS (last updated 2026-08-04): 2% contractual fee, TIDES-only entitlement, non-custodial/permissionless, Wyoming law, chain-split policy

## Skipped / not captured (reasons)

- foundrydigital.com Terms and Conditions page (generic site ToS, effective 2023-02-01, no fee schedule — viewed in browser, judged not capture-worthy; no-automated-scraping clause noted)
- pool.foundrydigital.com dashboard/login (login-walled; foundryusapool.com redirects there)
- antpool.gitbooks.io legacy help center (stale, ETH-era fee table; referenced in capture notes only)
- antpoolsupport-hc Zendesk KYC user-guide articles (existence noted; not captured)
- f2pool.io/mining/support fee table (duplicated Zendesk content; cross-referenced in capture notes)
- ViaBTC /terms, support.viabtc.com payout-threshold article (threshold noted as "not re-verified" in pricing capture; budget spent)
- ViaBTC /pricing Merged Mining section (renders as image/JS; no text)

## Failures / quirks

- foundrydigital.com + www: Cloudflare 403 to plain curl (both hosts). Captured via real-browser session.
- pool-faq.foundrydigital.com (HubSpot KB), antpoolsupport-hc.zendesk.com, f2pool.zendesk.com, www.antpool.com, www.f2pool.com, www.viabtc.com, ocean.xyz: all return HTTP 200/403 then terminate the curl body transfer (curl exit 56, "HTTP 200, 0 bytes") — consistent TLS/JA3 fingerprint filtering of curl. Captured via alternate fetcher / browser. NO site was capturable with plain `curl --compressed` today except none — every target required a fallback.
- AntPool homepage "Transparent Earnings" section ships untranslated Chinese in EN locale (garble noted in file).
- AntPool fee percentages exist only inside an embedded image in the Zendesk article; no numeric BTC fee is published in any crawlable text.
- Foundry fee tier percentages likewise not published (tier mechanism documented, numbers absent).

## Signal lines

1. **Fee disclosure is the exception, not the rule**: F2Pool (FPPS 4% / PPLNS 2% for BTC, full per-coin table, updated 2026-10-09) and ViaBTC (PPS+ 4%+2%, PPLNS 2%, with payout formulas) publish exact numbers; OCEAN states a flat 2% (1% DATUM) in both marketing and binding ToS; AntPool buries its fee table in an image and its Zendesk article is from 2022; Foundry publicly documents only a quarterly "fee tier" mechanism — no percentage anywhere on-site. The legacy public numbers (AntPool PPS+ 4%, gitbook era) may be outdated.
2. **Payout schemes**: Foundry = FPPS only (daily, net of fees, trimmed-mean txfee rate); AntPool = PPS/PPLNS/FPPS selectable; F2Pool = FPPS default or PPLNS for BTC (+PPS/PPS+ on alts); ViaBTC = PPS+ (default) or PPLNS with hourly settlement; OCEAN = its own TIDES pro-rata scheme, explicitly rejecting FPPS/PPLNS as approximation/custody models.
3. **Custody posture splits cleanly into two camps**: Foundry (KYC/AML + whitelisted addresses + third-party payment processor, US SOC-audited), AntPool (individual + institutional KYC, Bitmain-affiliated, sanctions/mainland-China gate) are custodial accounts; F2Pool and ViaBTC are custodial but payout-fee-free with ViaBTC adding exchange-like services (auto-conversion, loans); OCEAN is the outlier — fully non-custodial coinbase-direct payouts, no account, "No KYC, only payout address", with sub-threshold balances contractually remaining OCEAN's property until payout.
4. **SV2/DATUM mentions: only OCEAN** — DATUM (its own decentralized-template protocol, positioned as the answer where "Sv2 wouldn't be a viable solution") is core to its product and even prices its fee (1% for DATUM users); zero Stratum V2 mentions surfaced on Foundry, AntPool, F2Pool, or ViaBTC marketing/help pages captured (Foundry KB has a "Stratum Proxy" section only — plain Stratum).
5. **Anti-automation posture is now universal among majors**: every pool site tested either Cloudflare-challenges (Foundry) or TLS-fingerprint-kills curl mid-transfer (AntPool, F2Pool, ViaBTC, OCEAN, plus all three Zendesk/HubSpot help centers); reliable crawl of this landscape requires a real browser or fingerprint-resilient fetcher, and ViaBTC additionally renders its merged-mining fee content as images.
