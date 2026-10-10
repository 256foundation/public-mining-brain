# bitaxeorg/bitaxeBIRDS issue #5: Part value mismatch with listed distributor part number

> Source: https://github.com/bitaxeorg/bitaxeBIRDS/issues/5
> Collected: 2026-10-07
> Published: 2026-02-02

- Repository: bitaxeorg/bitaxeBIRDS
- Type: issue
- Number: 5
- State: closed
- Author: penguin359
- Opened: 2026-02-02
- Closed: 2026-02-10
- Labels: none

## Description

The capacitors designated C60-C64 used for the various, unused REFCLK outputs from the BZM2 chips appear to have an incorrect manufacturer and distributor part number listed in the BOM metadata. Their value of 120 pF seems to be correct and matches the reference I have for them, but the part numbers listed in the BOM are for a 0.1 μF capacitor and the larger value might cause extra loading on the circuit if used.

## Comments

### recklessnode on 2026-02-02

Incorrect BoM and part:
CAP CER 0.1UF 10V X5R 0402 (0402X104K100CT)
Digikey PN in Schematic: 1292-1639-1-ND

### skot on 2026-02-10

good catch! fwiw I definitely built my BIRDS with these incorrect 0.1uF caps.. it seems to be working alright. I'll update the BOM though.
