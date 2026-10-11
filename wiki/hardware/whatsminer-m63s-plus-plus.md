# Whatsminer M63S++

> Sources: shop.whatsminer.com detail page + official spec file (captured 2026-10-11); ASIC Miner Value + MiningNow snapshots (2026-10-10)
> Raw: [M63S++ shop page + spec file](../../raw/hardware/microbt/2026-10-11-microbt-site-m63s-plus-plus.md); [MicroBT shop catalog + model map](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md); [AMV MicroBT listing](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md); [MiningNow MicroBT rows](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

The hydro efficiency flagship of the current retail catalog — 464 T at 15.5 J/TH on the 70°C-outlet hydro generation, sharing the catalog's best efficiency rating with the air-cooled M60S++ ([MicroBT catalog](../../raw/hardware/microbt/2026-10-10-microbt-site-product-catalog.md)).

## Specs (manufacturer, As-Of 2026-10-11)

Shop banner + tab, verbatim ([M63S++ shop page](../../raw/hardware/microbt/2026-10-11-microbt-site-m63s-plus-plus.md)):

- Hashrate: 464T; Power efficiency: 15.5J/TH; Power on wall: 7192.00W; listing type SPOT (partner channel — "Contact us to buy", onlineorder@microbt.com; no direct checkout), warehouses HK/USA
- Specification tab: PSU "AC380~480V, 3W+ ground, input 10kw"; Size "86mm*483mm*663mm with handle"; Weight "Net weight:29.5kg Gross Weight:32kg" (heavier than the M63/M63S 27.5 kg class); "Coolant demand per machine: About 1L"; power cable custom ≥16A; Ethernet

Official spec file (Chinese edition 神马M63S++, December 2024 — "水冷（出水温度达 70°C）", resolved from the official file index id 27 because the shop page has no attachment section), verbatim:

- 功耗比 (Power Ratio): 15.5J/T±5%
- 算力 (Hashrate): 434T～478T ±10%
- 重量 (Weight): 29.5kg net / 32kg gross; 尺寸（带把手）: 86mm×482.6mm×663mm
- 输入电压 (Input Voltage): AC380V～480V — 输入 10kW; no 功率 (Power on wall) row in the PDF — the banner's 7192.00W is the sole wall figure on record
- Environmental: inlet 25–55 ℃ normal / 25–45 ℃ high-performance; control ±2 ℃; rated flow ≥10 L/min ±10%; pressure ≤400 KPa; medium pure/distilled water + corrosion inhibitor + antifreeze; pH 7–8.7; storage -40–+70 ℃; working humidity 5–85 %RH
- Banner 464T inside the manual range 434–478 T
- Storefront (As-Of 2026-10-11): $4,640 unit price / $10 per TH (HK & USA; partner channel)

## Cross-check (AMV + MiningNow, 2026-10-10)

- AMV: "M63S++ (464 Th)", release Dec 2024, 464 Th/s, 7200 W ([AMV cross-check](../../raw/hardware/asicminervalue/2026-10-10-asicminervalue-microbt.md)) — matches the banner hashrate exactly
- MiningNow: "M63S++ (478TH/s)", 10000 W, 20.92 j/Th, best price $4,168.00, hydro, Dec 2024 ([MiningNow cross-check](../../raw/hardware/miningnow/2026-10-10-miningnow-microbt.md)) — a higher-bin row (478 T = the manual range top)

## Heat-reuse notes

- Hydro, 70°C-outlet generation: 7192.00W wall (banner) across 434–478 T bin range; "About 1L" coolant per machine
- The 29.5 kg net weight (vs 27.5 kg siblings) is the M63S++'s distinguishing hardware delta — denser silicon or added cold plate

## See Also

- [Whatsminer overview](whatsminer-overview.md)
- [Whatsminer M63S](whatsminer-m63s.md)
- [Whatsminer M60S++](whatsminer-m60s-plus-plus.md)
- [Hydronic heat reuse](hydronic-heat-reuse.md)
