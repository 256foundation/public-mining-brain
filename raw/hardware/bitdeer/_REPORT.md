# Capture report — commercial ASIC hardware (capture-loop A7, phase cap 60, ≤20 requests taken)

> Collected: 2026-10-10
> Scope: bitdeer-sealminer, auradine-site, canaan-site
> Method: curl --compressed + Chrome 126 UA; ~1 req/s; HTML stripped to text, product JSON read from embedded page data; Wayback used only for blocked-live canaan.io.

## Captured URLs

### Bitdeer (raw/hardware/bitdeer/ — 6 files)

- ✅ https://www.bitdeer.com/shop (HTTP 200, 93KB gz → catalog + prices + roadmap strip)
- ✅ https://www.bitdeer.com/en/shop/product/P250414000002 (SEALMINER A2; 307→200)
- ✅ https://www.bitdeer.com/en/shop/product/P260105000001 (SEALMINER A2 Pro Air)
- ✅ https://www.bitdeer.com/en/shop/product/P251110000002 (SEALMINER A2 Pro Hydro)
- ✅ https://www.bitdeer.com/en/shop/product/P260328000003 (SEALMINER A4 Ultra Hydro)
- ✅ https://www.bitdeer.com/sealminer/roadmap (SEAL01–SEAL04 chip page)
- Not captured (file cap): A3 Pro/A3 Hydro/A4 Pro/DL1 product pages (key data captured via shop + roadmap files); https://www.bitdeer.com/sealminer/materials

### Auradine (raw/hardware/auradine/ — 5 files)

- ✅ https://auradine.com/products → **301 to https://velaura.ai/products/** (HTTP 200) — Auradine has rebranded to Velaura; Teraflux Bitcoin section intact
- ✅ https://velaura.ai/wp-content/uploads/2025/09/Teraflux™-AT2880-Data-Sheet.pdf (2.2MB, pdftotext)
- ✅ https://velaura.ai/wp-content/uploads/2025/09/Teraflux™-AH3880-Data-Sheet.pdf (1.4MB)
- ✅ https://velaura.ai/wp-content/uploads/2025/02/Teraflux™-AI3680-Data-Sheet.pdf (4.2MB)
- ✅ https://web.archive.org/web/20230815055608/…4nm-launch PR + https://web.archive.org/web/20231207200805/…next-gen PR + https://news.bitcoin.com/u-s-designed-bitcoin-miner-delivers-promising-results/ (lineage: AT1500/AT2860 gen; AT1500 measured 180 TH/s @ 25.34 J/TH high-power, 112 TH/s @ 23.1 J/TH low-power)
- Note: live site has **no per-product HTML pages**; AT1500/AT2860 no longer listed (previous gen; AT2860 official specs = gap, model exists in pyasic fleet lists)

### Canaan (raw/hardware/canaan/ — 6 files, all archive-labeled)

- ❌ https://www.canaan.io/ — HTTP 403 Akamai (tried: full browser headers w/ Accept/Sec-Fetch/Upgrade-Insecure-Requests, http://, https://, apex https://canaan.io/ → 301 → www 403, /site/en/ path, shop.canaan.io)
- ❌ canaanninc.com / canaaninc.com — DNS does not resolve from this sandbox (dead domain). Working IR mirror found instead: **investor.canaan-creative.com** (live ✅, used to corroborate A15Pro/A15/A14 numbers from PRs)
- ✅ https://web.archive.org/web/20260412083808/https://www.canaan.io/miner/ (2026-04-12 snapshot)
- ✅ https://web.archive.org/web/20260611042511/https://www.canaan.io/miner/A15/ (2026-06-11)
- ✅ https://web.archive.org/web/20260512001000/https://www.canaan.io/miner/A14/ (2026-05-12)
- ✅ https://web.archive.org/web/20260410133654/https://www.canaan.io/news/…-a16xp-with-breakthrough-asic-chip-1732 (2026-04-10 snap of 2025-10-29 news)
- ✅ https://web.archive.org/web/20260421104343/https://shop.canaan.io/products/avalon-miner-a15pro-240t (2026-04-21)
- ✅ https://web.archive.org/web/20251006083553/https://shop.canaan.io/products/avalon-miner-a1566ha-500t (2025-10-06)

## Signal lines

1. **SEALMINER lineup + prices (bitdeer.com/shop, 2026-10-10):** 13 current models — A2 $2,892.8 (226T/3729W/16.5J/T, Sold-Out), A2 Hydro $6,690 (7359W), A2 Pro Air $3,380→$3,067 (260T/3874W/14.9J/T, Sold-Out), A2 Pro Hydro $6,500→$5,897 (500T/7450W/14.9J/T, Sold-Out), A3 series 240–690 TH/s @ 13.5–14 J/TH (A3 Pro Hydro $9,900→$9,478 = $14.36/T, 8250W), A4 series to 900 TH/s @ 9.45 J/TH (A4 Ultra Hydro 886T/8372.7W/9.45J/T "Stay tuned", A4 Pro Air/Hydro Pre-Order), plus new **Scrypt DL1** LTC+DOGE line (Air 3725W / Hydro 7823W, Pre-Order); chips SEAL01 (Q1'24, 18.1 J/TH) → SEAL02 (Q3'24, 13.5) → SEAL03 (Q1'25, 9.7) → SEAL04 (Q4'25, 6–7 target; A4 9.45 J/TH, mass production expected Q3 2026); A1 (SEAL01, 226T-class 18.1 J/TH, 20–23 J/TH system) no longer in shop.
2. **Auradine posture — enterprise/fleet-first, now under Velaura brand:** auradine.com 301s to velaura.ai; lineup is AT2880 air (40–270 TH/s, 16/18 J/TH), AH3880 hydro (100–600 TH/s, Eco 14.3 @ 400T / Mid 15.8 @ 500T / Turbo 17.5 @ 600T, 10 kW 3-phase, ~1 L coolant), AI3680 single-phase immersion (40–365 TH/s, 16/19 J/TH, warranty restricted to Bitcool 888 + Shell S3X), plus a sellable **3nm ASIC (0.87 TH/s @ 12 W, 8×8 mm)** and 1–2 MW modular containers (100–200 miners); FluxOS firmware (EnergyTune, Secure Boot, SV2) + FluxVision cloud (grid/QSE demand response via Voltus, ZTP, Foreman/AwesomeMiner APIs); contact form says "Minimum Order 500 units" and no prices are published — consumer/DIY is not the target; Gen-3 systems (9.8 J/TH eco, third-gen ASIC) announced 2025-11-12 but model numbers/pricing not yet published.
3. **Canaan outcome: PARKED LIVE, CAPTURED VIA ARCHIVE (per allowed fallback):** canaan.io + shop.canaan.io = Akamai 403 for every header/http-https/regional variant tried; canaanninc.com is a dead domain (DNS NXDOMAIN — the live IR mirror is investor.canaan-creative.com, which was used live to corroborate). All 6 Canaan files are Wayback snapshots dated within ~6 months (2025-10-06 → 2026-06-11), labeled with snapshot URLs. Spec baseline secured: **A15Pro-221T (221T/3662W/16.8J/TH, from $2,762.50), A15Pro+ 240T (240T/3720W/15.5J/TH ±3%, $3,600 = $15/T, US-TX stock), A15XP (209T/3667W/17.8J/TH, $2,299), A15-194T (194T/3647W/18.8J/TH), A1566HA-500T hydro (500T ±5%/8064W ±10%/16.8J/TH ±3%, $5,800 = $11.6/T), A14 series (A1446 133T @ 27.1J/TH $1,248; A1466 162T @ 23.3J/TH $1,603.8)**, and the newer **A16 series launch (A16XP-300T @ 12.8 J/TH ±5%, 300 TH/s ±5%, 220–277 V; A16-282T @ 13.8 J/TH)** — A16, not A15, is Canaan's current air-cooled flagship as of Oct 2025.
4. **Cross-vendor efficiency ladder (air-cooled flagships, listed specs):** Bitmain-class parity check — Canaan A16XP 12.8 J/TH (300T) < Canaan A15Pro+ 15.5 < Bitdeer A2 Pro Air 14.9 (260T) < Auradine AT2880 16 (180T normal) < Canaan A15Pro 16.8 (221T) < Bitdeer A2 16.5→roadmap refresh claims 14.9; hydro: Bitdeer A4 Ultra 9.45 J/TH (886T) and SEAL04 target 6–7 J/TH vs Canaan A1566HA 16.8 J/TH hydro (500T) vs Auradine Gen-3 hydro 9.8 J/TH eco (600T) — Bitdeer/Auradine Gen-3+ hydro now lead Canaan's listed hydro by ~1.7×.
5. **Gaps to re-hunt (image-only or absent):** Bitdeer per-model full spec sheets are image-only PNGs (URLs saved in each product file — OCR candidates: dimensions, fan curves, temperature tables); Canaan A16XP/A16-282T shop product pages + A1566 launch PR text not captured (file cap); Auradine AT2860 official specs never published in archived PRs (model exists in pyasic); Auradine Gen-3 model numbers/pricing pending; all Bitdeer/Auradine/Canaan prices exclude shipping/duties.

## Posture notes

- Bitdeer retail-first (USD prices, crypto payment, 7-day ship, coupon pricing), Auradine fleet/enterprise (500-unit minimum, no prices), Canaan both (shop.canaan.io retail + bulk-order flows, US-TX stock for A15Pro+).
- Rebrand risk: Auradine → Velaura means future captures should target velaura.ai (auradine.com still resolves).
- Wayback CDX rate-limits (HTTP 429) were hit; requests spaced 15–120 s — keep that margin for future archive pulls.
