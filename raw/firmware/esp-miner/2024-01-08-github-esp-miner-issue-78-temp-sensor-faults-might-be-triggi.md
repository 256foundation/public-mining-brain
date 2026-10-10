# bitaxeorg/ESP-Miner issue #78: temp sensor faults might be trigging over temp shutdown

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/78
> Collected: 2026-10-07
> Published: 2024-01-08

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 78
- State: closed
- Author: skot
- Opened: 2024-01-08
- Closed: 2024-10-10
- Labels: question

## Description

Some users have reported the Bitaxe running at normal temps and then all of the sudden going into the low hash freq "over temp shutdown" mode.

It's suspected that the EMC2101 might return erroneous temperatures or go into a fault mode every now and then causing this.

## Comments

### benjamin-wilson on 2024-01-13

We need some more info about this - i've never encountered it. erroneous readings or soldering issues? counterfeit IC?
