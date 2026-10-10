# bitaxeorg/ESP-Miner issue #21: Change the polarity of the fan speed control signal on the EMC2101

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/21
> Collected: 2026-10-07
> Published: 2023-08-31

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 21
- State: closed
- Author: skot
- Opened: 2023-08-31
- Closed: 2023-09-30
- Labels: bug, enhancement, good first issue

## Description

This is related to a HW change on the Ultra; https://github.com/skot/bitaxe/issues/58

Due to the way the EMC2101 works when we set the default fan speed to 100%, it also "inverts" the PWM signal that controls the fan speed (on 4pin fans).

Ideally there would be a way in ESP-Miner to detect that the board is an Ultra and configure the EMC2101 to run with inverted polarity. This will be the standard going forward, so this change is essentially to support the older BM1397 bitaxen.

## Comments

### johnny9 on 2023-09-24

Is this resolved with https://github.com/skot/ESP-Miner/commit/d4affd7ebb3971f8c7e186734f6cc09b4de1ce42?

### benjamin-wilson on 2023-09-24

Yes I think so
