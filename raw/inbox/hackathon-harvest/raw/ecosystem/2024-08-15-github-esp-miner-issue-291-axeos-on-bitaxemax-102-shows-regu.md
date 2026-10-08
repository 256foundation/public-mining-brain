# bitaxeorg/ESP-Miner issue #291: AxeOS on bitaxeMax 102 shows regulator temperature (which doesn't exist)

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/291
> Collected: 2026-10-07
> Published: 2024-08-15

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 291
- State: closed
- Author: skot
- Opened: 2024-08-15
- Closed: 2024-10-10
- Labels: bug, good first issue

## Description

<img width="388" alt="image" src="https://github.com/user-attachments/assets/ca667efd-3cd7-493e-b895-52b357cb4a4a">

The BitaxeMax doesn't have a regulator that provides temperature. This gauge should be hidden on 102 / 2.2 HW

<img width="345" alt="image" src="https://github.com/user-attachments/assets/01861527-1db6-4e84-907a-f55f38c697a7">


## Comments

### mrv777 on 2024-09-28

Is this still a bug?
I see `*ngIf="info.vrTemp > 0"` so I would think it only shows if it has a positive value, but maybe the BM1397 returns something odd?

### skot on 2024-10-10

I am not seeing the regulator temp on my Max. appears to be fixed
