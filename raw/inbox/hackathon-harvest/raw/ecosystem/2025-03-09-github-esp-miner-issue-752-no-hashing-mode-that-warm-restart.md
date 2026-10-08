# bitaxeorg/ESP-Miner issue #752: no-hashing mode that warm restart resolves

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/752
> Collected: 2026-10-07
> Published: 2025-03-09

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 752
- State: closed
- Author: skot
- Opened: 2025-03-09
- Closed: 2025-03-24
- Labels: none

## Description

This is the issue for tracking a 0 GH/s hashrate, 5W power situation that is resolved by pressing the Restart button in AxeOS, or the RESET button on the Bitaxe.

## Comments

### MaSe-Time on 2025-03-10

Ok, my last gasp attempt was to move all three units out of my front cupboard and next to an additional router in my rear outbuilding. Tested pings and all sub 5ms.... 12 hours gone by and no drop outs at all no drop to 5w and stop hashing which requires a hard reset and no stop hashing but still pulling the same power and soft reset starts it again.

Moral of the story, if you think you have adequate wifi signal, you haven't! Move them closer to the router!!

### skot on 2025-03-24

This should be "fixed" in #780 ... meaning that power faults are now shown in AxeOS, and assuming the fault cause is gone, a warm restart should clear.
