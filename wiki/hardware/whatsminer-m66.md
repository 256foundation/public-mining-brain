# Whatsminer M66

> Sources: shop.whatsminer.com detail page + official manual (captured 2026-10-11); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [M66 shop page + manual](../../raw/hardware/microbt/2026-10-11-microbt-site-m66.md); [MicroBT shop catalog + model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md); [AMV MicroBT listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md); [MiningNow MicroBT rows](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The immersion-cooled 19.9 J/TH rung — 276 T banner rating, compact 267.5×147×401 mm chassis, oil-side spec sheet (coolingId 14, "Insulating liquid (S5X/S3X)").

## Specs (manufacturer, As-Of 2026-10-11)

Shop banner + tab, verbatim ([M66 shop page](../../raw/hardware/microbt/2026-10-11-microbt-site-m66.md)):

- Hashrate: 276T; Power efficiency: 19.9J/TH; Power on wall: 5492.40W; listing type SPOT, warehouses HK/USA
- Specification tab: PSU "AC380~480V"; Size "267.5mmX147mmX401mm with handle"; Weight "Net weight: 16kg Weight with packaging materials: 17kg"; power cable "Custom made，≥16A" (full-width comma as printed); Ethernet

Official manual (English, October 2024 — Immersion Cooling), verbatim:

- Power Ratio: 19.9 J/T ± 5 %
- Hashrate: 240 T –276 T ± 10 %
- Weight 16 kg (Net) / 17 kg (Gross); Size with handle 267.5 × 147 × 401 mm; AC 380 V –480 V
- Environmental: inlet liquid 25–55 ℃ normal / 25–45 ℃ high-performance mode; control accuracy ±2 ℃; rated flow **≥24 L/min** (immersion-class flow, vs ≥10 L/min hydro); medium "Insulating liquid (S5X/S3X)" — dielectric oil, not water; storage humidity 5–95 %RH
- The manual has NO Power On Wall row (immersion edition) — the banner's 5492.40W is the sole wall figure (= 276T × 19.9 J/T exactly)
- Shop banner 276T matches the manual range top; no per-machine coolant volume stated anywhere (unlike the ~1 L hydro units)
- Storefront (As-Of 2026-10-11): $2,208 unit price / $8 per TH (HK & USA)

## Cross-check (AMV + MiningNow, 2026-10-10)

- AMV: "M66 (280 Th)", release Nov 2023, 280 Th/s, 5572 W ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md))
- MiningNow: "M66 (276TH/s)", 5492 W, 19.9 j/Th, best price $4,301.12, hydro-tagged, Oct 2023 ([MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md)) — MiningNow's cooling tag says "hydro" while the manufacturer sheet says Immersion Cooling; the AMV/MN coverage note flags exactly this M63/M66 cooling-tag unreliability. The manufacturer sheet governs.
- Banner 276T matches the manual range top (240–276 T); AMV's 280 Th row is the +10% envelope neighbor.

## Heat-reuse notes

- Immersion: 5492 W wall draw into dielectric oil at ≥24 L/min — heat export requires an oil-compatible loop (S5X/S3X insulating liquid), not a water loop
- Inlet band 25–55 ℃; no fan, no noise row — fully liquid-side thermal design

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M66S](whatsminer-m66s.md)
- [Whatsminer M76](whatsminer-m76.md)
- [Immersion heat reuse](immersion-heat-reuse.md)
