# WhatToMine — BTC (SHA-256) SSR Profitability Snapshot

> Registry ID: whattomine
> Source: https://whattomine.com/coins/1-btc-sha-256 (via https://whattomine.com)
> Collected: 2026-10-10
> Published: n/d (live SSR snapshot)
> Posture: extract
> As-Of: 2026-10-10

## Method note

WhatToMine serves genuine SSR HTML (homepage 35,685 B; BTC coin page 25,681 B; both HTTP 200). The header ticker strip and the coin-detail stat block are server-rendered. The multi-coin comparison table at `/coins` is JS-loaded (SSR text jumps from nav to footer with no coin rows) — noted as a gap.

## Header ticker strip (SSR, exact values)

Verbatim anchor sequence on the homepage/coin-page nav:

`$82,977 0.1% $8.33 0.6% $2,509 0.2% $0.08 3.6% $63.30 0.9% $0.00 8.7% $522 0.0%`

Mapped to coins via ticker link hrefs (only these four were cleanly attributable):

- BTC: $82,977, +0.1% (class `text-success`), link `/coins/1-btc-sha-256`, title="Bitcoin"
- EthereumClassic: $8.33, −0.6% (class `text-danger`), link `/coins/162-etc-etchash`
- Ethereum: $2,509, +0.2% (success)
- Litecoin: $63.30, −0.9% (danger)

Remaining strip values ($0.08 −3.6%, $0.00 −8.7%, $522 +0.0%) could not be reliably attributed to tickers from SSR markup — left unattributed, not guessed.

## BTC coin detail block (SSR, exact literals)

- Coin: "Bitcoin (BTC)" — "Algorithm: SHA-256"
- Default ASIC profile shown: "580.00 Th/s @ 5,510W" (Bitmain Antminer S23 Hyd)
- "Block time: 9m 28s"
- "Last block: 970,868"
- "Bl. reward: 3.17" / "Bl. reward 24h: 3.14" (BTC, i.e. subsidy + fees as WTM reports it)
- "Difficulty: 132,716,002M" (24h / 3d / 7d all identical: 132,716,002M — flat difficulty window)
- "Nethash: 1,003,540.30 Ph/s" (~1.004 ZH/s)
- "Ex. rate: $82,977.33 (WhiteBIT)"
- "Ex. rate 24h: $82,933.58 (WhiteBIT)" / "3 days: $82,580.86" / "7 days: $84,039.83"
- "Ex. volume 24h: 7,151.899 BTC"
- "Daily emission: 477.809 BTC"
- "Market cap: $1,667,546,859,271"
- "Create 1 BTC in: 3,659.19 Days"
- "Break even in: 0.00 Days"
- Featured hardware: "Bitmain Antminer U3S23H | 1.16 Ph/s, 11020W"

## Interpretation notes

- Implied revenue for the S23 Hyd profile at 580 Th/s ≈ $24.59/day gross (cross-checked on /asics page, see companion capture).
- Difficulty 132.7T with nethash ~1,003.5 Ph/s and BTC $82,977 → WTM's own economics treat ~9.5 W/Th machines at $0.19/kWh as the reference marginal miner.
- Values are exchange-sourced (WhiteBIT) — single-venue price, not blended index.
