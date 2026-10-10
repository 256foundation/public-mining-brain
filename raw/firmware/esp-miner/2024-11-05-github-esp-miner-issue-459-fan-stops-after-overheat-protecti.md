# bitaxeorg/ESP-Miner issue #459: Fan stops after overheat protection overridden

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/459
> Collected: 2026-10-07
> Published: 2024-11-05

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 459
- State: closed
- Author: benjamin-wilson
- Opened: 2024-11-05
- Closed: 2025-04-16
- Labels: none

## Description

Bug reported to me -

After overheat protection was tripped, then resetting it, on the first boot the fan would start turning then stop, causing another rapid overheat condition. This issue would persist across multiple reboots with various fan settings (automatic, manual, max). Downgrading to 2.2.2 solved the issue. 

I think this was on a gamma unit. 

## Comments

### skot on 2024-11-06

I wonder if "invert fan polarity" got checked? That would cause the fan to stop when it's set to 100%

### benjamin-wilson on 2024-11-06

Good call, will check 

### dustinb on 2024-11-06

I had a similar issue on an ultra 204 board.  Went into overheat mode (had to re-apply paste after switching fans).  After disabling overheat mode on every power up the fan would spin initially and then stop and never start again.   I thought something on the board was done.    What fixed it for me was to enable "invert fan polarity" save and reboot.  Now the fan runs with invert fan polarity set either way.
