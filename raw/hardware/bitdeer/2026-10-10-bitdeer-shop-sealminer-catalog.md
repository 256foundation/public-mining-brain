# Bitdeer — SEALMINER shop catalog (bitdeer.com/shop)

> Source: https://www.bitdeer.com/shop
> Collected: 2026-10-10
> Published: Unknown
> Registry ID: bitdeer-sealminer

Server-rendered Next.js shop page (HTTP 200, ~93 KB gzipped transfer). Captured live. Lists 13 SEALMINER products; an embedded schema.org `ItemList` gives the canonical product IDs.

## Catalog (order as listed in embedded ItemList, with SSR prices)

| # | Product | URL (bitdeer.com/shop/product/…) | Type (SSR subtitle) | Power | Price shown |
|---|---------|------------------|---------------------|-------|-------------|
| 1 | SEALMINER A3 Pro Hydro | P260225000004 | BTC/BCH/BSV SHA256 Hydro-cooling Miner | 8250W | $9,900 ($15/T); coupon $9,478 ($14.36/T) |
| 2 | SEALMINER A3 Hydro | P260225000003 | BTC/BCH/BSV SHA256 Hydro-cooling Miner | 6750W | $6,750 ($13.5/T); coupon $6,411 ($12.82/T) |
| 3 | SEALMINER A4 Ultra Hydro | P260328000003 | BTC/BCH/BSV SHA256 Hydro-cooling Miner | 8372.7W | (price not shown — "Learn More / Stay tuned") |
| 4 | SEALMINER A4 Pro Air | P260328000001 | BTC/BCH/BSV SHA256 Air-cooling Miner | 3662.4W | (price not shown — Pre-Order) |
| 5 | SEALMINER A4 Pro Hydro | P260328000002 | BTC/BCH/BSV SHA256 Hydro-cooling Miner | 7412W | (price not shown — Pre-Order) |
| 6 | SEALMINER DL1 Air | P260313000002 | Scrypt \| LTC+DOGE Air-cooling Miner | 3725W | (price not shown — Pre-Order) |
| 7 | SEALMINER DL1 Hydro | P260528000001 | Scrypt \| LTC+DOGE Hydro-cooling Miner | 7823W | (price not shown — Pre-Order) |
| 8 | SEALMINER A2 Pro Air | P260105000001 | BTC/BCH/BSV SHA256 Air-cooling Miner | 3874W | $3,380 ($13/T); coupon $3,067 ($11.8/T) |
| 9 | SEALMINER A2 Pro Hydro | P251110000002 | BTC/BCH/BSV SHA256 Hydro-cooling Miner | 7450W | $6,500 ($13/T); coupon $5,897 ($11.8/T) |
| 10 | SEALMINER A3 Air | P250617000001 | BTC/BCH/BSV SHA256 Air-cooling Miner | 3640W | (price not shown — Pre-Order) |
| 11 | SEALMINER A3 Pro Air | P250619000003 | BTC/BCH/BSV SHA256 Air-cooling Miner | 3625W | (price not shown — Pre-Order) |
| 12 | SEALMINER A2 Hydro | P241105000002 | BTC/BCH/BSV SHA256 Hydro-cooling Miner | 7359W | $6,690 ($15/T) |
| 13 | SEALMINER A2 | P250414000002 | BTC/BCH/BSV SHA256 Air-cooling Miner | 3729W | $2,892.8 ($12.8/T) |

- TH/s per model is not printed on the shop SSR listing (only power + price); product pages / embedded landing copy carry hashrates (below).
- SEALMINER A1 (1st gen) is no longer listed in the shop — current-gen only. A1 lineage lives on the roadmap page (see `2026-10-10-bitdeer-sealminer-roadmap-chips.md`).
- Banner seen on shop: "SEALMINER A4 Ultra Hydro 886T | 9.45J/T — Stay tuned" and "SEALMINER A3 Pro Hydro 660T | 12.5J/T — $9,900 ($15/T) / $9,478 ($14.36/T)".
- Minerbase containers upsold alongside: "Minerbase A40-CE — 336 PCS \| ≈12*2.4*2.9M — $26,999"; "Minerbase A40-UL — 336 PCS \| ≈12*2.4*2.9M — $34,999".
- Notice strip: "$0.99 Reservation for Advanced Bitcoin Mining Technology!"

## Series claims (verbatim from embedded page data)

### SEALMINER A2 (SEAL02 chip)

- "Powered by the SEAL02 Bitcoin mining chip, the SEALMINER A2 pushes the hashrate limits—up to 226TH/s for the air-cooling model and 446TH/s for the hydro-cooling model. Hashrate like never before."
- A2 Hydro banner: "Equipped with Bitdeer's advanced SEAL02 chip, this powerhouse achieves 446 TH/s at a super-efficient 16.5J/TH."
- A2 temps: "The air-cooling model operates stably from -20°C to 50°C, while the hydro-cooling model performs flawlessly from 20°C to 55°C." (per Bitdeer test data)

### SEALMINER A2 Pro

- A2 Pro Air: "As an upgraded series of A2 models, SEALMINER A2 Pro Air Cooling undergoes powerful chip optimizations, once again achieving a lower power efficiency ratio—delivering higher mining efficiency with lower costs."
- A2 Pro Air PSU: "has been enhanced with an optimized power supply, increasing efficiency to 97%."
- A2 Pro Air noise: "features an optimized flow field design and custom fan blade structure, producing noise levels 3-4dB lower than mainstream industry products."
- A2 Pro Hydro: "optimized at the chip level to achieve a lower energy efficiency ratio of 14.9J/TH and a hashrate of 500-530TH/s"
- A2 Pro Hydro thermal: "raises the inlet temperature from 55°C to 60°C while maintaining outlet temperatures up to 70°C" (2U server form factor)

### SEALMINER A3 series

- "Built on the same A3 chip, the lineup spans 240–690 TH/s across air- and hydro-cooling variants—flexible enough for plug-and-play setups or high-throughput mining farms."
- "With A3 Pro models reaching 12.5 J/TH and A3 models between 13.5–14 J/TH, the A3 series sets a new bar for energy-to-performance optimization."
- "A3 All models are equipped with high-efficiency power supplies achieving up to 97% efficiency"
- "A3 Air-cooling models feature compact builds for flexible site compatibility and strong thermal performance; hydro-cooling models use a 2U server form factor for dense racking and centralized maintenance."
- "A3 Air-cooling units run 3–4 dB quieter than typical models; hydro-cooling units are near-silent"

### SEALMINER A4 series

- Title verbatim: "SEALMINER A4 — Hashrate up to 900 TH/s, Power efficiency as low as 9.45 J/TH"
- "From up to 900 TH/s* on the A4 Ultra Hydro, to 730 TH/s* at the upper end of the A4 Pro Hydro range, and 360 TH/s* for the A4 Pro Air, the A4 series defines a clear hashrate tier."
- "Led by the A4 Ultra Hydro, we've pushed power efficiency down to 9.45 J/TH* , shattering the 10-point ceiling. The A4 Pro series also maintains a stable 10.9 J/TH* ."
- Thermal: "the A4 Ultra Hydro and A4 Pro Hydro ensure stable operations across a broad spectrum of 20°C to 55°C" / "the A4 Pro Air features a refined thermal architecture capable of thriving in extreme conditions from -20°C to 50°C"

### SEALMINER DL1 (Scrypt — new product category)

- DL1 Hydro: "SEALMINER DL1 Hydro is designed for large-scale Scrypt mining environments requiring greater deployment density, thermal consistency, and infrastructure efficiency. Combining stable Scrypt compute with a compact 2U server architecture and hydro cooling system, DL1 Hydro is engineered for modern mining facilities while reducing logistics and operations management pressure." ("High-Density Scrypt Compute, Delivered in 2U")
- Coins named: LTC, DOGE (plus BELLS, JKC, LKY, PEP as "algorithmic compatibility only").

## Variance disclaimer (verbatim)

- "Note: Product performance may vary by ±10% in hashrate and ±5% in power efficiency. Final specifications are based on delivered units."
- "*The actual hash rate and power efficiency of each product delivered may vary by ±10% and ±5% respectively. These figures are for reference only, and the actual product delivered shall prevail."

## Gaps

- Per-model TH/s and J/TH not printed on the shop listing for Pre-Order/Learn-More items (A4 Pro Air, A4 Pro Hydro, DL1 Air, DL1 Hydro, A3 Air, A3 Pro Air) — available only via the series narrative above or product pages (client-rendered spec tabs).
- Shop page itself has no per-product dimension/noise data.
