# bitaxeorg/ESP-Miner issue #1322: TPS546 fault-related shutdown reason is not being shown.

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1322
> Collected: 2026-10-07
> Published: 2025-11-04

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1322
- State: open
- Author: skot
- Opened: 2025-11-04
- Closed: n/a
- Labels: bug

## Description

The TPS546D24 voltage regulator can monitor it's inputs, outputs and internal temperature and automatically shutdown if  any of these configurable limits are exceeded. When the TPS546D24 shuts down because of a fault, it is _supposed_ to set the specific fault type in the `STATUS_WORD` register (and the corresponding detail registers).

For some reason we're not always getting the fault type bits set in `STATUS_WORD`

to reproduce, take a gitaxeGamma 601 with a dark horse heatsink and remove one of the four spring pins. This lifts the heatsink up enough that it's no longer making good contact with the ASIC. Now when you power up the bitaxe, you can actually hear a buzzing from the regulator when it first turns on. After a second the regulator will shutdown (as it should). The problem is that `STATUS_WORD` remains at 0x0840 which corresponds to;

PGOOD -> The output voltage is NOT within the regulation window. PGOOD pin is asserted.
OFF -> The unit is NOT converting power for any reason including simply not being enabled.

0x0840 doesn't show any faults, and in fact this is the same STATUS_WORD we see before the regulator is enabled.

Because this appears to be a fault-related shutdown, I would like to see a bit set in `STATUS_WORD` to indicate the fault type. If one of these other bits is set, we can propigate this to AxeOS and show a more helpful error to the user than just "power supply fault"

Table 7-4. Fault Protection Summary on pg. 31 of the [TPS546D24S datasheet](https://www.ti.com/lit/ds/symlink/tps546d24s.pdf) shows all of the fault reasons.

## Comments

### skot on 2025-11-04

<img width="821" height="1192" alt="Image" src="https://github.com/user-attachments/assets/1d6eb35e-e18b-4c7e-b9ff-da694ccd47de" />
