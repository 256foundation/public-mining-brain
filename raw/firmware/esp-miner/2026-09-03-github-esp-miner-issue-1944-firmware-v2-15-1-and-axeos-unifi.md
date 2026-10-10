# bitaxeorg/ESP-Miner issue #1944: Firmware (v2.15.1) and AxeOS (Unified) versions do not match. Please make sure to update both www.bin and esp-miner.bin.

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1944
> Collected: 2026-10-07
> Published: 2026-09-03

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1944
- State: closed
- Author: nelwa
- Opened: 2026-09-03
- Closed: 2026-09-03
- Labels: none

## Description

After updating to v2.15.1 via the provided esp-miner.bin file, the Dashboard shows this error:

`Firmware (v2.15.1) and AxeOS (Unified) versions do not match. Please make sure to update both www.bin and esp-miner.bin.`

There is no www.bin file provided in the update section, as they are now merged.

## Comments

### mutatrum on 2026-09-03

That check has actually been removed with #1763, but after the update the dashboard version in the browser is still the old version. Refreshing the dashboard should fix it.

### nelwa on 2026-09-03

Thank you, that worked.
