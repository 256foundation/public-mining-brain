# Foundry USA Pool — Payout Methodology (FPPS) + Fee Tiers (Knowledge Base)

> Source: https://pool-faq.foundrydigital.com/what-is-foundry-usa-pools-payout-methodology
> Collected: 2026-10-10
> Published: Unknown (KB article; illustrative images dated Sep 2023 / Dec 2023)
> Registry ID: foundry-pool

---

# What is Foundry USA Pool's Payout Methodology?

## Foundry USA Pool pays out to all pool members according to the Full-Pay-Per-Share (FPPS) payout scheme.

Foundry USA Pool pays out to all pool members according to the Full-Pay-Per-Share (FPPS) payout scheme. Daily Earnings for the previous UTC day (00:00:00 UTC to 23:59:59 UTC) are calculated and credited daily to the subaccount at 01:00:00 UTC. If Auto-Withdrawal is on, earnings accrued in the Balance would be withdrawn to the selected whitelisted wallet addresses, once a day, during 9 AM to 5 PM UTC time.

There are 3 steps to calculate the FPPS payout for every Foundry USA Pool subaccount.

## Step 1

Foundry USA Pool calculates the daily Pay-Per-Share (PPS) earnings amount denominated in BTC per Subaccount, by summing the daily PPS base earnings for every worker in the subaccount. The daily PPS earnings per worker is based on every accepted share received from that worker in the 24hr contract period (midnight-to-midnight UTC time). The running total increments with every accepted share throughout the day. Accepted share means a share that meets the worker difficulty target.

- Daily PPS Base per Subaccount (formula shown as image in original)

For example, if there are 2 workers in a subaccount, and each worker submits 2 shares during the 24hr contract period: (example table shown as image in original)

## Step 2

Next, calculate the FPPS rate, in order to account for the transaction fee aspect of the FPPS payout, in addition to the PPS base.

- FPPS Rate (formula shown as image in original)

Let n be the number of blocks observed in the contract period and i be the observation after sorting the set of Transaction Fees per Block in ascending order.

The numerator is the sum of Transaction Fees per Block in the contract period excluding the highest 3 observations and lowest 3 observations, including empty blocks.

The denominator is the sum of all Block Subsidies per Block in the contract period excluding the highest and lowest 3 observations.

For example, if 10 blocks were placed during the contract period according to the table, only the middle 4 would be included in the calculation and the FPPS rate would be 105.000%.

## Step 3

Finally calculate the Subaccount FPPS Payout Amount denominated in BTC by multiplying the Daily PPS Base per Subaccount (1) with the FPPS rate (2), **net of pool fees**.

## Definitions

- **Accepted Share**: A share that has a difficulty that meets or exceeds the share difficulty and is neither stale nor rejected. These shares are included as part of the PPS calculations.
- **Stale Share**: A share that has a difficulty that meets or exceeds the share difficulty, but relates to a previous job assigned to the worker.
- **Empty Block**: A Bitcoin block which contains no transactions and thus has no transaction fees.
- **Rejected Share**: A share that has a difficulty that does not meet or exceed the share difficulty.
- **Share Difficulty (Worker difficulty)**: Difficulty required for our pool to accept a share. This difficulty is set on a per worker basis, to ensure that it sends shares at a target rate.
- **Worker**: A mining machine or group of mining machines under the same worker name.
- **Network Difficulty**: Difficulty required to mine a block on the Bitcoin network.
- **Block Subsidy**: Part of the BTC reward for mining a block coming from newly issued BTC; not including the block transaction fees.

---

## Related KB page — How Is My Fee Tier Calculated?

> Source: https://pool-faq.foundrydigital.com/how-is-my-pricing-tier-calculated

Foundry USA Pool™ evaluates pricing tiers every quarter based on your Group level hashrate (all subaccounts in a Group contribute to total hashrate) average in the previous quarter.

**Average Quarterly Hashrate**: The average quarterly hashrate is calculated by summing the daily hashrate (as recorded by Foundry USA Pool™ in Daily Statistics) for the given quarter and dividing it by the number of days in the quarter. This average is used to determine the pricing tier for the following quarter.

**Timing of Tier/Fee Adjustments**: It may take up to 10 business days into a new quarter for any pricing adjustments to take effect.

---

*Capture notes (2026-10-10):*
- *Payout scheme: FPPS, settled daily (previous UTC day), credited 01:00 UTC; auto-withdrawal runs once daily 09:00–17:00 UTC to whitelisted addresses.*
- *Payout threshold (per sibling KB article "What are the minimum payout thresholds?", pool-faq.foundrydigital.com): minimum withdrawal 0.01 BTC (1M sats) per address on regular days; 2730 sats per address on the last day of each month; thresholds apply per address across sub-accounts.*
- *Fee %: NOT published as numbers in the public KB — a "Pool Fees > How Is My Fee Tier Calculated?" article confirms hashrate-based tiered pricing evaluated quarterly, but no tier table or percentages are stated publicly (checked https://pool-faq.foundrydigital.com/how-is-my-pricing-tier-calculated). The product page only says "Clear & consistent fee structure."*
- *Custody: rewards paid out by Foundry (KYC/AML'd pool members, whitelisted addresses, third-party payment processor) — custodial model, US-based.*
- *Knowledge Base sections include "Stratum > Proxy" (Stratum proxy docs) — no Stratum V2 / DATUM support mentioned anywhere in the KB nav or pool pages captured.*
- *pool-faq.foundrydigital.com (HubSpot KB) terminates plain-curl connections mid-transfer; captured via alternate fetcher.*
