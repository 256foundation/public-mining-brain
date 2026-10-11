# SpiderPool — Home page (www.spiderpool.com, rendered)

> Source: https://www.spiderpool.com/ (Next.js SPA — static HTML is an empty shell; content below captured from the rendered page in a real browser session)
> Collected: 2026-10-10
> Published: Unknown
> Registry ID: spiderpool

---

SpiderPool's homepage (title: "Support Multi-Cryptocurrency Mining | Bitcoin, Litecoin, Dogecoin, and More Coins."). All figures are live site values on collection day.

## Pool stats banner

- BTC hashrate: **80.88 EH/s** · Total luck: **99.72%** · Last block: **970783**
- Miners: **190,950**

## BTC mining card (fee + payout disclosure)

- Coin: **BTC** with merged **+FB, DMT-NAT** ("BTC Same-Block Dual Rewards Now Live! DMT-NAT (NAT) Officially Released!" — same-block dual rewards announcement banner)
- Price: $82,978 · Daily revenue: 0.00000048 BTC/TH (≈ $0.0398 per TH/s)
- Pool hashrate: 80.88 EH/s · Network: 1.12 ZH/s
- **Payout threshold: 0.005** (BTC)
- **Fee: PPLNS 1% / FPPS 4%** — both schemes offered, miner's choice
- Algorithm: SHA256d · Stratum difficulty: 132.7 TH
- **Payment window: 02:00–10:00 (UTC+0) Daily**
- Mining URLs — North America (also Asia / Europe regions): `stratum+tcp://btc-us.spiderpool.com:2309` (alt ports 3333, 1800, 443); TLS `stratum+ssl://btc-us.spiderpool.com:2310` (alt 2311)

## Other coin cards

- **LTC** — Price $63.72; daily revenue 0.00102963/GH; pool hashrate 0 H/s; network 3.15 PH/s; threshold 0.002; **fee PPS 4%** (card shows "Coming soon" markers)
- **ETC** — Price $8.40; threshold 0.01; **fee PPS 1%** (marked "Coming soon")

## Site announcements visible on collection day

- "SpiderPool System Maintenance Notice"
- "Notice Regarding Risks Associated with Payout Addresses"
- "Risk Notice Regarding Fake SpiderPool Websites"
- "Wallet Address Security Upgrade Notice"
- "BTC Same-Block Dual Rewards Now Live! DMT-NAT (NAT) Officially Released!"

## FAQ topics (accordion on homepage; titles as shown)

- Balance below threshold, how to withdraw?
- Why was mining income not paid?
- Pool shows paid but no coins received?
- How to view my earnings and payment history?
- Miner running but pool shows "offline" or "no miner"?
- How to set up Telegram alert notifications?

## Account & tooling surface

- Sign In / Sign Up (email accounts, sub-accounts, watcher mode: "Watcher Check the status of your sub-account at any time" — public watcher link lookup by wallet address/sub-account).
- Footer tools: Stats, Miner Ranking, TxAccelerator, SpiderFinance, SpiderOS, ETH Staking Pool; links to Terms, Privacy policy, Contact us, **System Status Monitor**.
- "Apply for VIP" CTA on the BTC card.

## Not disclosed on the homepage (checked 2026-10-10)

- Custody model details / KYC requirements — the site is account-based with payout addresses, but custody terms and KYC requirements are not stated on the homepage.
- **SV2/DATUM (Stratum V2) support** — not mentioned.
- Fee schedule details beyond the card values (e.g. what FPPS 4% includes) — no dedicated fee page exists in the app's route manifest (checked `_buildManifest.js`; routes: /, /calculator, /coinDetail/[coin], /help/term, /spiderFinance, /txAccelerate, dashboards — no /fees page).
- Operator identity/corporate entity — not shown on the homepage (only "©2018-2026 All rights reserved").
