# Hashrate Heater Comparison (consumer & light-commercial)

> Sources: vendor spec pages captured 2026-10-11 (heatbit.com/pages/compare, constellationheating.com/products, superheat resources PDF, hotmine.io store, ry3t.com); *Bitcoin Mining Heat Reuse* (Stevens, 2025) ch. 6 + APP A for unit conversions
> Raw: [Heatbit compare](../../raw/industry/heatbit/2026-10-11-heatbit-compare.md); [Constellation products](../../raw/industry/constellation-heating/2026-10-11-constellation-products.md); [Superheat introduction PDF](../../raw/industry/superheat/2026-10-11-superheat-introduction-pdf.md); [Hotmine store](../../raw/industry/hotmine/2026-10-11-hotmine-home.md); [RY3T](../../raw/industry/ry3t/2026-10-11-ry3t-nova-product.md); [book APP A](../../raw/books/braiins-heat-reuse/11-appendix-a-thermodynamics.md)
> Updated: 2026-10-11
> As-Of: 2026-10-11
> Status: Draft

## Overview

Side-by-side spec matrix for shipped hashrate-heating products, per the specs-not-prices rule: no prices, no earnings projections — those churn and live in the dated raw captures. "n/p" = not published at capture (2026-10-11); gaps are knowledge, not oversights. Vendor identities and evidence anchors live in [Hashrate Heating & Mining Infrastructure Companies](../industry/hashrate-heating-companies.md).

Conversion anchor (book, p. 116): "Quick conversion: 1 kW of power consumption equals roughly 3,412 BTU/hr of heat output." — [ch. 6 extract](../../raw/books/braiins-heat-reuse/06-picking-hardware.md).

## Appliance-class heaters (consumer, air)

| Product | Form | Rated heat | Hashrate | Coverage | Sound | Safety |
|---|---|---|---|---|---|---|
| Heatbit Maxi | standing tower, 3-in-1 (heat/purify) | 5120 BTU | 39 TH/s | 400 sq ft | up to 56 dB at 1500 W | UL certified, tip-over, overheat |
| Heatbit Trio | tower appliance, 3-in-1 | 5120 BTU | 10 TH/s | 400 sq ft | up to 45 dB at 1500 W | UL certified, tip-over, overheat |
| Heatbit Canvas | flat panel, 2-in-1 | 1020 BTU | 10 TH/s | 150 sq ft | "Silent" | UL certified, tip-over, overheat |

All three: HEPA/sensor suite differs (Maxi/Trio have HEPA H12 + VOC/PM2.5 sensors; Canvas is heat+mining only), app + touchscreen controls on Maxi/Trio, Heatbit App only on Canvas. UL certification appears in every row of Heatbit's own compare table.

## Water-heater class (integral compute)

| Product | Form | Rated heat | Hashrate | Recovery claim | Safety |
|---|---|---|---|---|---|
| Superheat H1 / H1C | 50-gal electric water heater, processor replaces the resistive element | n/p (design claim: "same efficiency as conventional heaters") | n/p | 24 gal/hr recovery quoted in the product handbook (marketing, As-Of 2026-10-11) | installation manual + safety shutoffs (manual PDF); CES 2026 award |

Design claim (verbatim): "Superheat revolutionizes the electric water heater by replacing its traditional resistive heating element with a powerful processor. While both convert electricity into heat, the processor also performs valuable computations, delivering hot water with the same efficiency as conventional heaters but without additional energy costs." — [introduction PDF](../../raw/industry/superheat/2026-10-11-superheat-introduction-pdf.md). Community corroboration: firmware ties ASIC clock speed to water temperature [#8609 · 2026-01-08 · Tyler Stevens] — [superheat community anchor](../../raw/industry/superheat/2026-10-11-superheat-home.md); full context in [Hydronic Heat Reuse](hydronic-heat-reuse.md).

## Pool-boiler class (turnkey immersion)

| Product | Form | Continuous heat | Hashrate | Notes |
|---|---|---|---|---|
| Constellation Heater 200T | turnkey immersion pool boiler, 2-miner chassis | 4 kW (≈13,600 BTU/hr) | 200 TH (S21 ASICs included) | "Fully modulating: Eco, Normal, Auto modes"; titanium heat exchanger, Liquid21 fluid included; IP65 enclosure |
| Constellation Heater 400T | 3-miner chassis | 8 kW (≈27,300 BTU/hr) | 400 TH | same platform |
| Constellation Heater 600T | 3-miner chassis | 12 kW (≈41,000 BTU/hr) | 600 TH | outdoor IP65 turnkey pool boiler |

Platform-wide (verbatim fragments from the products capture): "Ethernet or Wi-Fi (2.4 / 5 GHz)" · "220/240 V" supply · "Fully modulating: Eco, Normal, Auto modes" · "Titanium heat exchanger, Liquid21 fluid included" · "IP65 enclosure, over temperature protection" · "1024×768 capacitive touchscreen" doubling as a "Live heater performance and Bitcoin blockchain display".

BTU/hr figures are computed from the book's 3,412 BTU/hr-per-kW conversion, not vendor-published. Salt-water and chlorine compatibility is vendor-claimed via the titanium exchanger.

## Boiler-integrated / storage-coupled (EU)

| Product | Form | Rated heat | Hashrate | Status |
|---|---|---|---|---|
| RY3T ONE | feeds an existing home water/heating system | n/p | n/p | reservation stage; homepage copy + book profile, no spec sheet at capture |
| RY3T NOVA | battery-buffered variant | n/p | n/p | "Wenn die Batterie voll ist, beginnt NOVA zu arbeiten" — when the battery is full, NOVA starts working; JS-rendered site |

## Store-front heater SKUs (Hotmine)

Hotmine's WooCommerce store lists CM-1 "Smart-heater" plus U6 (29 TH/s), WX6 (14 TH/s), X6 (7 TH/s) SKUs — heat-output and acoustic ratings are not published on the captured pages; the store is live but content dates to the 2013–2019 era with CES 2026 press for a mining water heater. Treat as pioneer lineage, not a current spec source.

## The DIY baseline (for scale)

No commercial spec sheet needed for the DIY tier: a full-load S19-class ASIC is a resistive heater with a hashrate attached — that is the entire substitution argument (book ch. 3, pp. 40/43; community builds in [Heater Electrical & 120V Builds](heater-electrical-and-120v-builds.md) and the Loki Kit lineage). Commercial products above are packaged versions of that physics with safety listings bolted on.

## See Also

- [Air-Cooled Hashrate Heating](air-cooled-hashrate-heating.md)
- [Hydronic Heat Reuse](hydronic-heat-reuse.md)
- [Immersion Heat Reuse](immersion-heat-reuse.md)
- [Immersion Fluids](immersion-fluids.md)
- [Whatsminer M64 Hydro Heaters](whatsminer-m64-hydro-heaters.md)
- [Hashrate Heating & Mining Infrastructure Companies](../industry/hashrate-heating-companies.md)
- [Hashrate Heating Products & Installs](../industry/hashrate-heating-products-and-installs.md)
