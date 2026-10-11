# SpiderPool

> Sources: spiderpool.com homepage (browser-rendered; the raw HTML is an empty Next.js shell) + the site's own `_buildManifest.js` route manifest (captured 2026-10-10); mempool.space pool-share API (1w/3m) and network state (2026-10-10)
> Raw: [SpiderPool home (rendered)](../../raw/pools/spiderpool/2026-10-10-spiderpool-home.md); [SpiderPool payout/fee disclosures](../../raw/pools/spiderpool/2026-10-10-spiderpool-payout-fee-disclosures.md); [mempool pool share 1w](../../raw/pools/mempool/2026-10-10-mempool-pool-share-1w.md); [mempool pool share 3m](../../raw/pools/mempool/2026-10-10-mempool-pool-share-3m.md); [mempool network state](../../raw/pools/mempool/2026-10-10-mempool-network-state-snapshot.md)
> Updated: 2026-10-10
> As-Of: 2026-10-10
> Status: Draft

## Overview

SpiderPool is a multi-coin mining pool (site title: "Support Multi-Cryptocurrency Mining | Bitcoin, Litecoin, Dogecoin, and More Coins.") whose BTC card advertises merged same-block rewards — BTC with +FB and DMT-NAT, under a "BTC Same-Block Dual Rewards Now Live! DMT-NAT (NAT) Officially Released!" banner ([home capture](../../raw/pools/spiderpool/2026-10-10-spiderpool-home.md)).

**Capture caveat (As-Of 2026-10-10):** the site is a fully client-rendered Next.js SPA — a raw-HTML fetch returns a ~1.7 KB empty shell (no title, no body text; `__NEXT_DATA__` with empty `pageProps`), so all content below was captured from the page rendered in a real browser; raw-HTML-only pipelines record nothing for this pool ([home](../../raw/pools/spiderpool/2026-10-10-spiderpool-home.md); [fee/payout capture](../../raw/pools/spiderpool/2026-10-10-spiderpool-payout-fee-disclosures.md)).

Scale as displayed on collection day: BTC hashrate 80.88 EH/s, 190,950 miners, total luck 99.72%, last block 970783, network shown as 1.12 ZH/s ([home](../../raw/pools/spiderpool/2026-10-10-spiderpool-home.md)). On mempool.space (same day) SpiderPool ranked #5 in both windows: 73 of 1,072 blocks in the trailing week (0 empty, avg block match rate 99.42%, avg fee delta -0.0871) and 1,102 of 13,346 blocks over 3 months (15 empty, 98.11%) ([1w](../../raw/pools/mempool/2026-10-10-mempool-pool-share-1w.md); [3m](../../raw/pools/mempool/2026-10-10-mempool-pool-share-3m.md)). Network context: 1.02 ZH/s current hashrate, 58% through the epoch, next retarget estimated 2026-10-16 19:39 UTC ([network state](../../raw/pools/mempool/2026-10-10-mempool-network-state-snapshot.md)).

## Fees and payout

- **Fees, printed on the homepage card, miner's choice: PPLNS 1% / FPPS 4%** ([home](../../raw/pools/spiderpool/2026-10-10-spiderpool-home.md); [fee/payout](../../raw/pools/spiderpool/2026-10-10-spiderpool-payout-fee-disclosures.md)). The capture reads the dual display as: accept variance (PPLNS at 1%) or buy stability (FPPS at 4%) ([fee/payout](../../raw/pools/spiderpool/2026-10-10-spiderpool-payout-fee-disclosures.md)).
- **BTC payout threshold 0.005 BTC; "Payment window: 02:00–10:00 (UTC+0) daily"** for BTC ([home](../../raw/pools/spiderpool/2026-10-10-spiderpool-home.md); [fee/payout](../../raw/pools/spiderpool/2026-10-10-spiderpool-payout-fee-disclosures.md)).
- **No fine print** on what the FPPS 4% includes (e.g. transaction-fee pass-through), and no dedicated fee page exists: the app's route manifest (`_buildManifest.js`) lists /, /calculator, /coinDetail/[coin], /help/term, /spiderFinance, /txAccelerate and dashboards — no /fees route ([home](../../raw/pools/spiderpool/2026-10-10-spiderpool-home.md); [fee/payout](../../raw/pools/spiderpool/2026-10-10-spiderpool-payout-fee-disclosures.md)).
- **Other coins:** LTC at PPS 4% (threshold 0.002) and ETC at PPS 1% (threshold 0.01), both cards marked "Coming soon" ([home](../../raw/pools/spiderpool/2026-10-10-spiderpool-home.md); [fee/payout](../../raw/pools/spiderpool/2026-10-10-spiderpool-payout-fee-disclosures.md)).
- **Endpoints (North America; Asia/Europe regions also listed):** `stratum+tcp://btc-us.spiderpool.com:2309` (alt ports 3333, 1800, 443) and TLS `stratum+ssl://btc-us.spiderpool.com:2310` (alt 2311); SHA256d; displayed stratum difficulty 132.7 TH ([home](../../raw/pools/spiderpool/2026-10-10-spiderpool-home.md)).
- **Failure modes as FAQ titles** ("Balance below threshold, how to withdraw?", "Why was mining income not paid?", "Pool shows paid but no coins received?") — consistent with a custodial balance → on-chain payout model with payment records; answer bodies sit behind the accordion (titles captured) ([home](../../raw/pools/spiderpool/2026-10-10-spiderpool-home.md); [fee/payout](../../raw/pools/spiderpool/2026-10-10-spiderpool-payout-fee-disclosures.md)).

## Custody and access

- **Account model:** email sign-up/sign-in, sub-accounts, watcher mode (read-only sub-account status via watcher link), 2FA (`/user/secondVerify` route) and API access keys (`/accessKey` route); rewards accrue to account balances and are paid to configured wallet addresses ([home](../../raw/pools/spiderpool/2026-10-10-spiderpool-home.md); [fee/payout](../../raw/pools/spiderpool/2026-10-10-spiderpool-payout-fee-disclosures.md)).
- **KYC requirements: not disclosed on site** — no KYC page exists in the route manifest; a Terms page exists at /help/term, but the homepage carries no KYC statement ([fee/payout](../../raw/pools/spiderpool/2026-10-10-spiderpool-payout-fee-disclosures.md)).
- **Operator identity: not shown** on the homepage (only "©2018-2026 All rights reserved") ([home](../../raw/pools/spiderpool/2026-10-10-spiderpool-home.md)).
- **Risk notices live on collection day:** "Notice Regarding Risks Associated with Payout Addresses", "Wallet Address Security Upgrade Notice" and a "Risk Notice Regarding Fake SpiderPool Websites" — the pool itself warns of spoofed domains; a "SpiderPool System Maintenance Notice" banner was displayed and a "System Status Monitor" page is linked in the footer ([home](../../raw/pools/spiderpool/2026-10-10-spiderpool-home.md); [fee/payout](../../raw/pools/spiderpool/2026-10-10-spiderpool-payout-fee-disclosures.md)).

## SV2 / DATUM

Not mentioned on the homepage or in the route manifest (As-Of 2026-10-10) ([home](../../raw/pools/spiderpool/2026-10-10-spiderpool-home.md); [fee/payout](../../raw/pools/spiderpool/2026-10-10-spiderpool-payout-fee-disclosures.md)).

## See Also

- [SECPOOL](secpool.md)
- [Luxor Pool](luxor-pool.md)
- [MARA Pool](mara-pool.md)
- [Braiins Pool](braiins-pool.md)
- [Pool Payout Schemes](pool-payout-schemes.md)
- [Pool Choice for Heat Miners](pool-choice-for-heat-miners.md)
- [Pool Centralization & FPPS](pool-centralization-and-fpps.md)
- [Stratum in Practice](../protocols/stratum-in-practice.md)
