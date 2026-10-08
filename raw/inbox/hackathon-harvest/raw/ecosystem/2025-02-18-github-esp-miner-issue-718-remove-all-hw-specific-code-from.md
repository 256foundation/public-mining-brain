# bitaxeorg/ESP-Miner issue #718: Remove all HW specific code from AxeOS

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/718
> Collected: 2026-10-07
> Published: 2025-02-18

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 718
- State: closed
- Author: skot
- Opened: 2025-02-18
- Closed: 2025-03-27
- Labels: enhancement, help wanted

## Description

The Axeos front end needs to get all HW specific config info from abstracted functions in:

- Thermal functions like fan and temp sensing in /main/thermal/thermal.c
- Power monitoring and voltage regulation in /main/power/power.c and /main/power/vcore.c
- ASIC support in /asic/asic.c

Introduced in https://github.com/skot/ESP-Miner/pull/698

## Comments

### w3irdrobot on 2025-02-21

i can help with this if you want if you need it. 

### w3irdrobot on 2025-02-21

actually, this is interesting. unless i'm misunderstanding something, it looks like the places we update the `GLOBAL_STATE` already pull from those HW-abstracted functions. so i'm not sure i fully understand what new is being asked for.

### skot on 2025-02-21

I think @WantClue has fixed some of these issues recently. And there is also the gauge range issue #699 if you want to check it out.
