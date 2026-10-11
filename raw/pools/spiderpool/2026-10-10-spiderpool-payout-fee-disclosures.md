# SpiderPool — Payout / fee disclosures (homepage cards + route manifest)

> Source: https://www.spiderpool.com/ (rendered homepage) + https://www.spiderpool.com/_next/static/zIUTRCnQKt3AzUKqSpttt/_buildManifest.js (route manifest)
> Collected: 2026-10-10
> Published: Unknown
> Registry ID: spiderpool

---

SpiderPool publishes its fee and payout parameters on the homepage coin cards rather than on a dedicated fee page. This capture consolidates everything the site discloses about money flow as of 2026-10-10, and records what it does not.

## Fee schedule (as displayed on the homepage)

| Coin | Schemes offered | Fee | Payout threshold | Payment cadence |
|---|---|---:|---:|---|
| BTC (+FB, DMT-NAT merged) | **PPLNS 1% / FPPS 4%** | 0.005 BTC | Daily, 02:00–10:00 (UTC+0) window |
| LTC | **PPS 4%** | 0.002 | card marked "Coming soon" |
| ETC | **PPS 1%** | 0.01 | card marked "Coming soon" |

- The dual fee display (PPLNS 1% vs FPPS 4%) is the miner's choice: accept variance (PPLNS, 1%) or buy stability (FPPS, 4%).
- No fine print anywhere on the homepage about what the FPPS fee includes (e.g. transaction-fee pass-through treatment).

## Payout mechanics (as displayed)

- **Payment window: 02:00–10:00 (UTC+0) daily** for BTC.
- Threshold for BTC: **0.005** (units implicit BTC); LTC 0.002; ETC 0.01.
- FAQ topics address the failure modes: withdrawing below threshold, "why was mining income not paid", "pool shows paid but no coins received" — indicating a custodial balance → on-chain payout model with payment records. (FAQ answer bodies are behind the accordion; titles captured.)
- Payout-address risk notices are live on the homepage ("Notice Regarding Risks Associated with Payout Addresses", "Wallet Address Security Upgrade Notice") — consistent with address-based custodial payouts.
- Watcher mode exists (read-only sub-account status via watcher link) — no custody implication by itself.

## Custody / KYC

- Account model: email sign-up/sign-in, sub-accounts, watcher links, API/access keys (`/accessKey` route), 2FA (`/user/secondVerify` route). Rewards accrue to account balances and are paid to configured wallet addresses.
- **KYC requirements: not disclosed on site** (no KYC page in the route manifest; Terms page exists at /help/term but the visible homepage carries no KYC statement).
- Who holds rewards: the pool (account balance) until threshold payout — standard custodial PPS-family model per the site's own payout FAQ framing.

## SV2/DATUM and incidents

- **SV2/DATUM (Stratum V2): not mentioned** anywhere in the homepage or route manifest.
- Incidents/status: the site links a **"System Status Monitor"** page (footer) and displays a "SpiderPool System Maintenance Notice" banner on collection day; a "Risk Notice Regarding Fake SpiderPool Websites" is also live — the pool itself warns of spoofed domains.

## Capture method note (garble/usability status)

- `curl` of https://www.spiderpool.com returns a ~1.7 KB empty Next.js shell (no title, no body text; `__NEXT_DATA__` has empty `pageProps`) — **the site is unusable without JS rendering**. All content above was captured from the page rendered in a browser. Raw-HTML-only pipelines will record nothing for this pool.
- The route manifest (`/_buildManifest.js`) is fetchable statically and confirms there is no dedicated fee/help-center page beyond `/help/term`.
- mempool.space cross-reference (same day, this repo): SpiderPool ranked #5 with 73 blocks in the trailing week, avgMatchRate 99.42%.
