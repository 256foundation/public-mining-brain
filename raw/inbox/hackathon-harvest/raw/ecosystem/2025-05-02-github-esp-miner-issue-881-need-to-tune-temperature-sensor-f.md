# bitaxeorg/ESP-Miner issue #881: need to tune temperature sensor for bitaxeGT 800

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/881
> Collected: 2026-10-07
> Published: 2025-05-02

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 881
- State: closed
- Author: skot
- Opened: 2025-05-02
- Closed: 2025-05-27
- Labels: bug, help wanted

## Description

We tuned the gain and ideality settings on the EMC2101 for the BM1370 bitaxeGamma 600. bitaxeGamma Turbo uses the same ASIC, but of course we use a dual temp reader, the EMC2103 and it has different gain and ideality settings.

## Comments

### benjamin-wilson on 2025-05-02

How did I not think of this during heatsink testing 🤦‍♂️

### benjamin-wilson on 2025-05-03

It looks like the slope is correct so we can just apply a -10C offset
