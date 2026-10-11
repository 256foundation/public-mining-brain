# SECPOOL — Home page (www.secpool.com)

> Source: https://www.secpool.com/
> Collected: 2026-10-10
> Published: Unknown
> Registry ID: secpool

---

Site is a Vue.js single-page application (iView UI kit); static HTML serves only a shell ("We're sorry but SECPOOL doesn't work properly without JavaScript enabled."). The readable content below is what the site itself discloses in its shell HTML and its own served app bundle (`/js/app.2efe2684.js`, UI strings and agreements) on collection day.

## What the site discloses about itself

- **Title:** "SECPOOL 安全稳定，可靠之选 | SECPOOL" — tagline "安全稳定，可靠之选" = "Safe & stable, your reliable choice".
- **Meta author:** SECPOOL.
- **Meta description (site's own):** "SECPOOL,secpool.com,BTC mining pool,digital currency mining pool,SHA256 mining,miner,ASIC,mining with ASIC,mining pool,bitcoin mining pool,SHA256,BTC,PPS+,BTC矿池,数字货币矿池,SHA256挖矿,矿机,ASIC,矿机挖矿,矿池,比特币矿池,майнинг-пул BTC…" — the site's own keywords advertise **PPS+** as a payout scheme, alongside BTC/SHA256/ASIC positioning.
- **Languages:** Chinese, English, Russian (site self-describes as 三语; UI i18n bundles for zh/en/ru are baked into the app bundle).
- **Currencies displayed:** USD, CNY (UI currency selector).

## Payout claims (from the site's own UI strings)

- "FPPS/PPS/PPLNS 多模式，收益自动分配、实时透明，稳享收益" → **"Multiple modes: FPPS/PPS/PPLNS. Automatic payout distribution, real-time transparency. Enjoy stable earnings."** (homepage feature bullet)
- "收益每日结算" → **"Daily payout settlement"** (homepage feature bullet)
- "全球稳定网络" → "Global stable network" — "顶级技术团队 + 分布式架构，百万级矿机并发，全球节点 7×24 小时" (top-tier tech team + distributed architecture, million-miner concurrency, global nodes 24/7)
- Homepage earnings widget strings: "PPS+昨日收益 (1TH/s)" ("PPS+ yesterday's earnings per 1 TH/s"), "PPS+收益比例" ("PPS+ Earn Rate"), "块平均收益" ("Average Block Value"), "Lucky %"
- Promo string "0费率" ("0 Fee") exists in the homepage UI bundle (a zero-fee promotion banner; no standing numeric fee is published in the static HTML).
- Product string "FPPS 固收" ("FPPS Fixed Earnings") — a fixed-earnings product tier.
- Earnings-mode labels in the app: PPS / PPLNS / SOLO / FPPS / PPAPPS / PPAPPLNS earnings line items.

## Accounts, custody and access (from the site's own UI/protocol strings)

- Registered-account model: email sign-up/login, 2FA (bind/unbind, password change), observer links, sub-accounts, worker management — i.e. a **custodial pool account** from which rewards are paid out to configured wallet addresses ("收款地址", "最小支付: Minimum Payment:", "支付记录 Payment History", "多钱包按比例接收收益" = multi-wallets receive income proportionally).
- KYC machinery is present in the app config (`VUE_APP_CRYPTOKEY: "SECPOOL_KYC_CRYPTOKEY"`, `kycUid` session fields, SSO via `account-beta.secpool.com`).
- "链上打款优化" ("On-chain payment optimization"): payouts to the same address configured across multiple SECPOOL sub-accounts are consolidated to speed up on-chain payment.

## Not disclosed on the site (checked 2026-10-10)

- **Numeric pool fee (%)** — not in the static HTML; the site's user agreement defers to "relevant webpages" (see the payout/fee disclosures capture).
- **Minimum payout threshold value** — the UI has the fields but no static value.
- **Who operates SECPOOL** — no company name, address, or registration info in the static shell or app bundle; the agreement refers only to "本公司" ("the Company"). Identity not disclosed on site.
- **SV2/DATUM (Stratum V2) support** — not mentioned anywhere in the shell HTML or app bundle strings.
- **Status/incident page** — none on site; a Telegram alert bot (t.me/SECPOOL_alert_bot) exists for miner alarms.

## Contact / support endpoints found

- Email (site's own privacy policy & agreement): **help@secpool.com**
- Help center link baked into the app: `https://secpoolsupport-hc.zendesk.com` (see the payout/fee disclosures capture — the Zendesk help center is now closed)
- AI customer-service widget and UDesk chat button on the app.
