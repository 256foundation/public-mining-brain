# bitaxeorg/ESP-Miner issue #536: Improve Supra (BM1368) die temp readings

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/536
> Collected: 2026-10-07
> Published: 2024-11-30

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 536
- State: open
- Author: skot
- Opened: 2024-11-30
- Closed: n/a
- Labels: enhancement

## Description

This was totally busted on BM1370, we should check on BM1368.

- Make sure the Analog Mux register is set properly. (compare with S21 Dumps)
- Experiment with EMC2101 external temp sensor gain and ideality settings.

## Comments

### WantClue on 2026-05-29

@skot still relevant ?
