# ViaBTC — Fees page (/pricing): payment methods & fee schedule

> Source: https://www.viabtc.com/pricing
> Collected: 2026-10-10
> Published: Unknown
> Registry ID: viabtc

---

# Fees

## Payment Method

ViaBTC pool supports two payment methods: **PPS+** and **PPLNS**. The default is **PPS+**. You can go to [Settings](https://www.viabtc.com/pool/mining) to choose the method you prefer based on your risk tolerance.

**PPS+** (Pay Per Share Plus) is an enhanced version of the traditional PPS method, with transaction fee distribution added. Under this method, the pool pays miners a theoretical reward for every valid share they submit, providing stable earnings based on their contributed hashrate. Since miners do not bear the risk, the pool assumes the risks of pool luck and orphaned blocks, and therefore charges a relatively higher fee. Transaction fees are distributed separately to miners under the PPLNS as below.

**PPLNS** (Pay Per Last N Shares) distributes rewards based on each miner's share of the pool's total hashrate over the last N difficulty rounds when a valid block is found. Transaction fees are also distributed to miners. The pool charges a small fee for operation and maintenance. Under PPLNS, miners' payouts depend on whether the pool finds blocks. Earnings may fluctuate, but long-term average returns are generally higher.

## Fees — PPS+ Mode

| Mining Earnings | Block Reward | Transaction Fees (Variable) |
|---|---|---|
| Payment Method | PPS | PPLNS |
| Fee Rate | **4%** | **2%** |
| Formula | Shares / Difficulty * Block Reward * (1 − Pool Fee) | Your Hashrate / Pool Hashrate * Reward * (1 − Pool Fee) |
| Rule | Pay out every hour based on the current difficulty | Distributed based on each user's share of the pool's total hashrate over the past 5 difficulty rounds after the block receives 6 confirmations. |

PPS+ Earnings — Note: Average daily earnings are estimated based on data from the past 7 days, but actual earnings may vary. For reference only.

## Fees — PPLNS Mode

| Mining Earnings | Block Rewards + Transaction Fees (Variable) |
|---|---|
| Fee Rate | **2%** |
| Formula | Your Hashrate / Pool Hashrate * Block Reward * (1 − Pool Fee) |
| Rule | Distributed based on each user's share of the pool's total hashrate over the past 5 difficulty rounds after the block receives 6 confirmations. |

## Merged Mining

*(section present on page but content rendered as image/JS in capture — no text)*

---

*Capture notes (2026-10-10):*
- *Fee %: DISCLOSED and itemized — PPS+ mode = 4% on block-reward (PPS) component + 2% on transaction-fee (PPLNS) component; PPLNS mode = 2% flat. This is ViaBTC's public documented fee schedule.*
- *Payout scheme/cadence: PPS+ block-reward portion pays hourly at current difficulty; tx-fee portion paid via PPLNS over past 5 difficulty rounds after 6 block confirmations.*
- *Payout threshold: not stated on /pricing (ViaBTC's documented default BTC minimum payout is 0.001 BTC per its help center / account settings; not re-verified here).*
- *Custody: pool account model with built-in wallet/trading/loans (see homepage capture).*
- *No Stratum V2 / DATUM mention on this page. Page fetched via alternate fetcher (plain curl body transfer killed after headers, exit 56).*
