# SECPOOL — Fee / payout / help disclosures (from the site's own app bundle)

> Source: https://www.secpool.com/ (app bundle /js/app.2efe2684.js — user agreement & i18n strings served by secpool.com) + https://secpoolsupport-hc.zendesk.com (checked)
> Collected: 2026-10-10
> Published: Unknown
> Registry ID: secpool

---

SECPOOL's pages are client-rendered, so this capture extracts the pool's own fee/payout/help disclosures from the JavaScript bundle secpool.com serves, plus the state of its linked help center. Everything below is first-party SECPOOL text unless marked otherwise.

## Fee disclosure (from the site's user agreement, served in the bundle)

- Clause 1.3 (English version in the bundle's own translation): **"We have the right to charge fees for specific services in accordance with applicable agreements ('Rates'). Please refer to the relevant webpage for the specific applicable Rates."**
- Reading: SECPOOL does **not** publish a numeric fee in any static page or bundle string. The fee UI string exists ("费率标准" → "Fees") but values are fetched post-login from the authenticated API.
- **Numeric fee %: not disclosed on site** (checked: static home HTML 2026-10-10, app bundle agreement text).

## Payout scheme and cadence (site's own strings)

- Modes advertised: **FPPS / PPS / PPLNS** (homepage bullet, see home capture); homepage keyword meta advertises **PPS+**; earnings line items include PPAPPS / PPAPPLNS ("FPPS block reward earnings", "FPPS transaction fee earnings" — i.e. FPPS splits block subsidy and estimated tx fees as separate earning categories).
- **"收益每日结算" — "Daily payout settlement."**
- Payout controls: "最小支付 / 起付金额" ("Minimum Payment"), "支付时间" ("Payment time"), "扣款时间" ("Cut Payment Date") — threshold/timing fields exist but **no numeric threshold value is published statically**.
- Multi-wallet: "多钱包按比例接收收益" ("Multi-wallets receive income proportionally"); on-chain payment optimization consolidates payouts across sub-accounts sharing one address.
- A "FPPS 固收" ("FPPS Fixed Earnings") product exists — a fixed-earnings offering layered on FPPS.

## Custody / KYC (site's own strings and config)

- Custodial account model: earnings accrue in a registered SECPOOL account (email + 2FA + sub-accounts) and are paid out to configured wallet addresses; balance/withdrawal UI throughout.
- KYC infrastructure: app config exposes `SECPOOL_KYC_CRYPTOKEY`/`SECPOOL_KYC_CRYPTOIV` (encrypted KYC payload keys) and `kycUid`; SSO at `account-beta.secpool.com`. The full KYC policy text (INFORMED CONSENT, data-collection clauses) is bundled, indicating KYC is part of the account flow.
- Who holds rewards: the pool (account balances until payout) — standard custodial PPS-family model. Non-custodial/SV2/DATUM options: **not mentioned on site**.

## Help / support infrastructure (checked 2026-10-10)

- The app bundle hard-codes the help center as `https://secpoolsupport-hc.zendesk.com`.
- That Zendesk help center **no longer serves**: `https://secpoolsupport-hc.zendesk.com/` and `/hc/en-us`, `/hc/zh-cn` and the Help Center API all return 404/403 and redirect to `zendesk.com/help-center-closed` ("This help center no longer exists" flow). The site's own agreement still directs users to webpages/announcements for rates — so at collection time there was **no publicly reachable fee/help page**.
- Support email per the site's own policy: **help@secpool.com**; in-app AI support + UDesk chat; Telegram alerts bot `t.me/SECPOOL_alert_bot`.
- No public status/incident page found.

## Context (not first-party — labeled as such)

- Hashrate Index "Top 10 Bitcoin Mining Pools for 2026": lists SecPool at ~55 EH/s (4.9%), "continues to expand its footprint across Asia, offering FPPS payouts" — consistent with the site's own FPPS/PPS/PPLNS claim; operator identity still unnamed.
- Spark.money pool comparison: SecPool fee "~5%", payout "FPPS", region "Asia" — third-party estimate, unverified by the site.
- mempool.space pool-share 1w capture in this repo (same day): SECPOOL rank 7, 44 blocks, avgMatchRate 97.93%.
