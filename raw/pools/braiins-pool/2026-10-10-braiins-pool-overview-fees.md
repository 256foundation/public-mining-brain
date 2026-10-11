# Braiins Pool — pool overview, rewards & fees (braiins.com/pool + academy)

> Source: https://braiins.com/pool
> Secondary: https://academy.braiins.com/en/braiins-pool/rewards-and-payouts/ + https://academy.braiins.com/en/braiins-pool/stratum-v2-manual
> Collected: 2026-10-10
> Published: Unknown
> Registry ID: braiins-pool

---

Combined capture of Braiins Pool's product page and its Academy fee/payout documentation (single file, per capture budget). Braiins Pool is the rebranded **Slush Pool — "the world's longest running mining pool"**, mining since **2010**.

## What braiins.com/pool says (2026-10-10)

- Positioning: "Earn steady FPPS rewards, choose flexible on-chain or Lightning payouts, and pay **0% pool fees when you mine with Braiins OS**."
- Hero claims: "THE WORLD'S LONGEST RUNNING MINING POOL — 1.3M+ BTC Mined since 2010" · "Instant LN Payouts" · "**Secure & Non-KYC**" · "Most profitable FPPS".
- Real-time stats displayed on the page: Pool hashrate **13.91 EH/s** · Active workers **177,359** · Active users **13,112** · All-time mined **1,294,383 BTC** · Reward system: **FPPS**.
- Feature set: multiple "Financial Accounts" (reward splitting in any ratio), customizable payout timing (daily/weekly/monthly), worker management with regex filtering and hashrate alerts, access profiles/API keys ("safely share access… without sacrificing the security of your funds" — bank-account-style transaction overview), multilingual support (English, Russian, Spanish, Farsi, Chinese), API + CSV/JSON export, mobile app.
- Footer/history links: "Slush Pool" (legacy site slushpool.com still live), Stratum V2 product pages, "Rewards & Fees" → academy.

## Fees (Academy: Rewards & Payouts — "Payouts & Fees")

"Braiins Pool currently applies the following fee to provide the pool mining service." Proceeds from transaction (network) fees are shared with miners.

| Item | Value |
|---|---|
| **Pool fee (FPPS)** | **2.5%** |
| Pool fee with Braiins OS firmware | **0%** (homepage claim; SV2 manual note ties the 0% fee to mining via Braiins OS) |
| Payout fee — on-chain, 0.005 BTC and above | free |
| Payout fee — on-chain, under 0.005 BTC | 0.0001 BTC |
| Payout fee — Lightning Network | free |
| Minimum payout | 0.0002 BTC |
| Minimum free payout | 0.005 BTC |
| Maximum payout | 5 BTC |
| Lightning limits | min 1 satoshi, max 0.005 BTC (500,000 sats) |

- **Cadence:** "Payouts are created daily at 9.00 UTC. Confirmation for on-chain payouts typically takes 1-2 hours… Lightning payouts are confirmed within couple of minutes."
- Payout thresholds are **customizable per Financial Account** in Payout Settings; payout rules can be schedule-based (daily/weekly/monthly) or threshold-triggered; an **Immediate Payout** can be requested once balance exceeds the minimum.
- **FPPS spec (documented with worked examples):** every share is guaranteed a reward = coinbase reward cut (proportional to shares at network difficulty) + transaction fees cut (trimmed average block fee across the difficulty period, awarded proportionally); the 2.5% fee is then subtracted. Example given: gross 0.00000200 BTC/TH/day → net 0.00000195 BTC at 2.5%.

## Custody / KYC

- Homepage states **"Secure & Non-KYC"** — no KYC gate advertised for pool participation.
- Custodial account model: rewards accrue in pool "Financial Accounts" with balances and transaction ledgers; payouts sent to external wallets (on-chain or Lightning). Braiins Pool runs its **own Lightning node** with channels to major wallet operators for LN payouts; failed/invoice-expired LN payouts are returned to balance.
- Who can join: open sign-up (Log in / Sign up on the page); no membership restrictions stated.

## Stratum V2 / DATUM

- The pool **supports Stratum V2**: Academy has a dedicated "Stratum V2 Manual" — "Stratum V2 is a new protocol for pooled mining that we developed in collaboration with Bitcoin developer Matt Corallo… Stratum V2 is implemented in our firmware Braiins OS." Pool side: default SV2 port **3336**, pool public key in the URL path authenticates the endpoint (anti-man-in-the-middle for hashrate); Stratum V1 still supported. SV2 requires Braiins OS firmware (stock firmware unsupported).
- **DATUM is not mentioned** (DATUM is OCEAN's distinct SV2 template-delivery implementation; Braiins' SV2 docs note miners "will eventually" work on their own block templates).
- Historical footnote: older firmware should use legacy endpoint `v2.stratum.slushpool.com` to keep the 0% fee.

## Incidents / status

- No status page or incident history on the captured pages; the pool page's live stats widget (hashrate, workers, users, all-time mined) is the only health surface. No incident notices were displayed on collection day.
- mempool.space cross-reference (this repo, same day): Braiins Pool ranked #10 with 14 blocks in the trailing week; a separate "Braiins Solo" pool (solo.braiins.com) ranked #23.
