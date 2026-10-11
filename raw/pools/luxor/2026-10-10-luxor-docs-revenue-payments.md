# Luxor Pool — docs: Revenue & Payments (FPPS formula, payouts, thresholds)

> Source: https://docs.luxor.tech/platform/mining/revenue-payments (captured via the page's own Markdown export; note Cloudflare intermittently blocks plain curl on docs.luxor.tech)
> Collected: 2026-10-10
> Published: Unknown
> Registry ID: luxor-pool

---

Luxor's official payout documentation ("Revenue & Payments", Luxor Platform → Mining Pool). Content below is the doc's own text, condensed where repetitive.

## Payout scheme: FPPS

- "Full Pay-Per-Share (FPPS) is a mining pool payment model that ensures miners receive consistent and predictable earnings based on their contributed hash rate… incorporating both block rewards and transaction fees into miner payouts."
- "Pools using FPPS take on the variance risk, ensuring miners receive stable daily payouts."
- **Fee framing (their own words):** "Luxor is a purchaser of hashrate. FPPS pools purchase hashrate from miners at an agreed rate. In the case of Luxor, **we purchase hashrate from you at a discount to spot FPPS (discount to spot is commonly known as pool fees)**." → The fee is expressed as a discount to spot FPPS; **no numeric fee % is published in the docs**.
- Luxor reserves the right to change the FPPS Formula at any time; changes are tracked in their changelog.

## Luxor FPPS formula (per block height)

`FPPS_h = (1/d_h) · (b_h + (1/|L|) · Σ_{i∈L} t_{h-i})`

- h = latest block height; d = network difficulty at h; b = block subsidy (currently 3.125 BTC); t = transaction fees of a specific block
- Lookback n = **144 blocks** (~1 day); L = that window with fee outliers trimmed, excluding ≤p5 and ≥p95
- Reward (subsidy + trimmed-average fees) divided by network difficulty = FPPS rate per unit hashrate

## Accounts & custody

- Subaccounts are "independent **Financial accounts**… where you are credited your mining rewards" — each with its own rewards balance, payout settings (wallet addresses, minimum payout thresholds), and worker stats; multiple subaccounts per Workspace. Standard **custodial pool-account model** (rewards held in the account until payout); no non-custodial or SV2/DATUM option mentioned in this doc.
- KYC: not discussed in this doc; workspaces/roles govern account access.

## Payout cadence and thresholds (published values)

Three payout frequencies:

- **Daily** — processed every day
- **Weekly** — once per week, user picks the day
- **Monthly** — first day of every month

Eligibility: balance must exceed min withdrawal threshold **plus** withdrawal fee. Published table:

| Pool | Min threshold | Withdrawal fee |
|---|---:|---:|
| Bitcoin | 0.001 | 0.000075 |
| LTC | 0.1 | 0.001 |
| DOGE | 100 | 0.01 |
| Sia | 100 | 0.000001 |
| ZCash | 0.1 | 0.005 |

- Example given: BTC subaccount needs balance > **0.001075 BTC** at the scheduled cycle to be paid.
- "In all cases, payments are processed **shortly after 04:00 UTC**, assuming balance requirements are met."
- Payment settings are defined per subaccount-currency (balance, next payout schedule, frequency, addresses).

## Incidents / status

- Not covered in this doc; no status page linked from it. The docs do promise formula changes will be announced in the platform changelog (docs.luxor.tech/platform/changelog).
- Docs site is agent-friendly: `/llms.txt` index and `.md` appended URLs.
