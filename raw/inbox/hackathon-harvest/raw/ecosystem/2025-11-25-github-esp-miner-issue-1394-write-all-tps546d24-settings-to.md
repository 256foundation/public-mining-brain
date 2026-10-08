# bitaxeorg/ESP-Miner issue #1394: Write ALL TPS546D24 settings to operating RAM

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1394
> Collected: 2026-10-07
> Published: 2025-11-25

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1394
- State: open
- Author: skot
- Opened: 2025-11-25
- Closed: n/a
- Labels: enhancement

## Description

We need to expand the TPS546_CONFIG (defined in TPS546.h, set in vcore.c) struct to include ALL TPS546D24 settings. These should be written to the regulator RAM over PMBUS after identifying it.

Currently some of the settings are left at defaults, some of those coming from the pin strapping resistors, which we don't want to use anymore.

This is related to #1392 

## Comments

### skot on 2025-11-25

See the complete list of commands in the [TPS546D24S datasheet](https://www.ti.com/lit/gpn/tps546d24s), section 7.5.1

To determine what the proper settings are, many of them can be read from a single-chip TPS546D24-based bitaxe with current firmware that is still set to use pinstrapping values.

### WantClue on 2025-11-30

Do we have a pcb without the pin strapping already? Adding this to the nvm of the TPS should be fairly quick, already have something prepared but needs to be tested
