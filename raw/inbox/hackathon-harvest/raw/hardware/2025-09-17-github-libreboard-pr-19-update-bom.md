# 256foundation/libreboard pull request #19: Update BOM

> Source: https://github.com/256foundation/libreboard/pull/19
> Collected: 2026-10-07
> Published: 2025-09-17

- Repository: 256foundation/libreboard
- Type: pull request
- Number: 19
- State: closed
- Author: econoalchemist
- Opened: 2025-09-17
- Closed: 2025-09-18
- Labels: none

## Description

This PR updates the new component fields in the BOM for the voltage regulator upgrade. The PCB has been synchronized from the schematic, however there were a few warnings and errors. The error report is included in the root: "250916_schematic-pcb-error-report.txt". One item remains to be identified on the BOM, reference C27-C29, if we can use a 1206 footprint then I suggest we go with [this capacitor](https://www.digikey.com/en/products/detail/tdk-corporation/C3216X5R1E336M160AC/2792259). Otherwise, we may want to consider a through-board component like [this](https://www.digikey.com/en/products/detail/tdk-corporation/FG22X7R1C336MRT06/5802930).

## Comments

### Schnitzel on 2025-09-18

switched the C27-C29 to the suggested capacitor, updated the BOM with it
