# bitaxeorg/bitaxeBIRDS pull request #3: Fix the TX_IN pull-down resistor to pull down to GND_L

> Source: https://github.com/bitaxeorg/bitaxeBIRDS/pull/3
> Collected: 2026-10-07
> Published: 2025-11-30

- Repository: bitaxeorg/bitaxeBIRDS
- Type: pull request
- Number: 3
- State: closed
- Author: penguin359
- Opened: 2025-11-30
- Closed: 2026-02-10
- Labels: none

## Description

This updates the schematic to fix the pull-down resistor used for TX_IN so that it will pull all the way down to GND_L when the signal goes low. This resolves issue #2 with the bitaxe BIRDS board. The PCB layout was also updated to match the schematic at all three level transitions. It is currently DRC clean in the report. The route changes were kept to a minimum despite the length diff caused by KiCad recalculating the copper pours.

- **TX_IN modified to pull low to GND_L in level shifter (Closes: #2)**
- **Added footprint library configuration so KiCad can find bitaxe.pretty**
- **Rerouoted the traces for the pull-down resistor on TX_IN for each level**
