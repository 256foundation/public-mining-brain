# Auradine Teraflux™ AH3880 — official data sheet (hydro-cooled)

> Source: https://velaura.ai/wp-content/uploads/2025/09/Teraflux™-AH3880-Data-Sheet.pdf
> Collected: 2026-10-10
> Published: Unknown (PDF footer: "© 2025 Auradine, Inc. All rights reserved"; site upload path dated 2025-09)
> Registry ID: auradine-site

PDF extracted with pdftotext (layout mode). All numbers verbatim.

## Positioning (verbatim)

"The Auradine Teraflux AH3880 is an ASIC-based hydro-cooled Bitcoin miner. Miners can be managed using APIs and a web console that is available for each miner, and with FluxVisionTM (purchased separately), the cloud management solution for pre-deployment configuration and tuning of Auradine miners at scale."

## Hardware Specifications (verbatim table)

| AH3880 Product Specifications | Value |
|---|---|
| Crypto Algorithm | SHA-256 |
| Hashing Performance (TH/s at Joules/TH) | Range: 0-600TH/s¹ — Eco: 14.3J/TH at 400TH/s¹ — Mid: 15.8J/TH at 500TH/s¹ — Turbo: 17.5J/TH at 600 TH/s¹ |
| Cooling Mechanism | Hydro |
| Coolant per miner | Approximately 1L |
| Coolant Temperature Range | 10°C to 60°C |
| Coolant Flow Rate | ~5L/min to 20L/min |
| Power | 10000 Watts² |
| Power Supply AC Input Voltage, Nominal, Min/Max (Three phase AC input) | 380-480V, 320-528V |
| Power Supply AC Input Current | 20 Amps per phase |
| Power Supply AC Input Frequency | 48-62Hz |
| Power Cable | 1 x SA2-30 to SA2-30 |
| Connectivity Options | RJ45 Ethernet 10/100/1000 |
| Dimensions (Length/Width/Height) | 26.2 x 19.1 x 3.5 inches / 665 x 485.65 x 88 mm |
| Weight | 64 lbs / 29 kg |
| Storage Temperature | -40 to 158°F (-40 to 70°C) |
| Operation Humidity, RH | 20-80% RH non-condensing |
| Operation Altitude | 9,840ft (3,000M)³ |

Footnotes (verbatim): "1) Estimates using PG25 liquid coolant, ±8%, 2) PSU spec; system maximum may be slightly lower, 3) Operating temp will vary based on altitude"

## Software Specifications (verbatim claims)

- Same stack as AT2880: Power Management (QSE/Voltus grid integration, "available with FluxVision"), EnergyTune™ (ECO/Turbo modes via DVFS), AutoTemp, "User-friendly Interface and API Support" (Foreman / AwesomeMiner integration), FluxVision™ with ZTP.
- Note: this AH3880 sheet omits the "Hardware-Based Secure Boot" section that appears in the AT2880 and AI3680 sheets.

## Fleet/commercial posture

- 3-phase 380-480V input; 10 kW PSU class; rack-mount form factor (665 x 485.65 x 88 mm, 2U-style); hydro loop ~1 L coolant per miner.
- Related announcement (2025-03, Business Wire, not captured in full): "The rack-mounted hydro miner achieves an exceptional 600TH/s with efficiency as low as 14.5J/TH in normal mode… Flexible Power Management allows maximum power usage of up to 10KW… with ability to scale down to 1,800 watts… Integrated OLED Screen… Advanced Liquid Detection quickly identifies leaks." (cited for context; numbers verbatim from that release)
