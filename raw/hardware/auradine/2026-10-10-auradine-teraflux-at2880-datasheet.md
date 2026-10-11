# Auradine Teraflux™ AT2880 — official data sheet (air-cooled)

> Source: https://velaura.ai/wp-content/uploads/2025/09/Teraflux™-AT2880-Data-Sheet.pdf
> Collected: 2026-10-10
> Published: Unknown (PDF footer: "© 2025 Auradine, Inc. All rights reserved"; site upload path dated 2025-09)
> Registry ID: auradine-site

PDF extracted with pdftotext (layout mode). All numbers verbatim.

## Positioning (verbatim)

"The Auradine Teraflux portfolio of Bitcoin miners offers industry-leading performance, quality, uptime, security, and demand response features to deliver the lowest total cost of ownership for Bitcoin mining solutions."

"The Auradine Teraflux AT2880 is an ASIC-based air-cooled Bitcoin miner. Miners can be managed using APIs and a web console that is available for each miner, and with FluxVisionTM (purchased separately), the cloud management solution for pre-deployment configuration and tuning of Auradine miners at scale."

## Hardware Specifications (verbatim table)

| AT2880 Product Specifications | Value |
|---|---|
| Crypto Algorithm | SHA-256 |
| Hashing Performance (TH/s at Joules/TH) | Range: 0-270 TH/s¹ — Normal: 16 J/TH at 180TH/s¹ — Turbo: 18 J/TH at 270 TH/s¹ |
| Operating Temperature Range | -4 to 122°F (-20 to 50°C²) |
| Cooling Mechanism | Air-cooled |
| Power Supply Option A Dual Input | Power: 5000 Watts³, 2 x C20 Input; AC Input Voltage, Nominal, Min/Max: 200-240V, 180 - 264V; AC Input Current: 0-17.6 Amp per input; Power Cables Included: 2 x C19 to C20 |
| Power Supply Option B Single Input | Power: 5000 Watts³, 1 x PA45 Input; AC Input Voltage, Nominal, Min/Max: 208-277V, 180 - 305V; AC Input Current: 0-30 Amp; Power Cables Included: 1 x PA45 to C20 |
| AC Input Frequency | 48-62 Hz |
| Connectivity Options | RJ45 Ethernet 10/100/1000 |
| Dimensions (Length/Width/Height) | 15.5 x 8 x 11.5 inches / 395 x 202 x 290mm |
| Weight | 42.5lbs / 19.3kg |
| Storage Temperature | -40 to 158°F (-40 to 70°C) |
| Operation Humidity, RH | 20-80% RH non-condensing |
| Operation Altitude | 9,840ft (3,000M)⁴ |

Footnotes (verbatim): "Note products are for indoor use only. 1 Preliminary estimates, ±8%, 2 At sea level, 3 PSU spec; system maximum may be slightly lower, 4 Operating temperature will vary based on altitude"

## Software Specifications (verbatim claims)

- **Power Management**: "Auradine is the only hardware OEM to directly integrate with the power grid and Qualified Scheduling Entities (QSEs) such as Voltus. A QSE can modulate power consumption on your mining farm based on demand response to grid supply and load curtailment for cost savings. Power Management is available with FluxVision."
- **EnergyTune™**: "uses Dynamic Voltage and Frequency Scaling (DVFS) to set the desired power consumption (in Joules) per miner… the web console on the miner also allows the operator to select an operating mode of ECO (least power consumed per TH or maximum efficiency) or Turbo (highest TH/s performance)."
- **AutoTemp**: "continuously monitors the internal junction temperature of the ASICs and reduces the TH/s to ensure that the ASICs are operating in a safe zone… enabled on every miner."
- **Hardware-Based Secure Boot**: "hardware-based root of trust secure boot implementation… validates that only digitally signed and trusted code is allowed to run during the boot sequence."
- **APIs**: "leverage the API integration with Foreman or AwesomeMiner for fleet management."
- **FluxVision™**: "cloud management solution for pre-deployment configuration and tuning of Auradine miners at scale… 'miner groups'… Zero Touch Provisioning (ZTP)."
- **DVFS claim (Uptime section)**: "Unlike traditional Bitcoin miners that take ten minutes per iteration and require frequent reboots to adjust the operating frequencies and voltages of the mining ASICs, the Auradine miners have a sophisticated, built-in Dynamic Frequency and Voltage Scaling (DVFS) mechanism that perform these optimizations in half the time."

## Fleet/commercial posture

- FluxVision is purchased separately; per-miner web console + APIs standard. © 2025 Auradine, Inc.; "For more information, visit auradine.com or contact us at info@auradine.com."
