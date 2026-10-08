# 256foundation/mujina issue #4: Task: Add basic Bitaxe Gamma communication

> Source: https://github.com/256foundation/mujina/issues/4
> Collected: 2026-10-07
> Published: 2025-04-18

- Repository: 256foundation/mujina
- Type: issue
- Number: 4
- State: closed
- Author: rkuester
- Opened: 2025-04-18
- Closed: 2025-11-15
- Labels: none

## Description

Prove communication with a Bitaxe Gamma running bitaxe-raw firmware by sending initialization commands, hardcoded jobs, and receiving results. Accept the device path as a CLI argument. Log all communication events for verification.

## Comments

### rkuester on 2025-04-30

#### Status Update
As of today, 6d9a76d5, we've made it to the point of setting up a Bitaxe Gamma with bitaxe-raw and establishing basic communication with the ASIC. While the functionality itself is a humble beginning, the primary focus at this stage of the project has been on setting the right design and direction in software.

<img width="703" alt="Image" src="https://github.com/user-attachments/assets/69a4ceee-c659-4d5a-815e-007dc2a2de5e" />

### rkuester on 2025-04-30


Along the way, some troubleshooting and contribution to bitaxe-raw was necessary:

* bitaxeorg/bitaxe-raw#1
* bitaxeorg/bitaxe-raw#2
* bitaxeorg/bitaxe-raw#3
* bitaxeorg/bitaxe-raw#4
* bitaxeorg/bitaxe-raw#5

As well as reporting a minor issue with Bitaxe Gamma:

* bitaxeorg/bitaxeGamma#37
