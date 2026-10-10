# bitaxeorg/ESP-Miner issue #1541: [AxeOS][Dashboard][Block Header] Incorrect coin in Value and Output field

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1541
> Collected: 2026-10-07
> Published: 2026-02-06

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1541
- State: closed
- Author: grymster
- Opened: 2026-02-06
- Closed: 2026-02-06
- Labels: none

## Description

I do BCH solo mining at my local pool (ckpool) + full node (bitcoin-cash-node:v28.0.1).
In dashboard there is a 'Block Header' area which has fields Value and Output.
In both fields it shows '3.12588200 **BTC**'

<img width="537" height="188" alt="Image" src="https://github.com/user-attachments/assets/14e3b2b7-1478-4381-8e06-891a77d124ae" />

Steps to reproduce the behavior:
1. Go to 'Pool'.
2. Set data of your BCH pool and restart.
3. Go to 'Dashboard'.
4. Scroll down to 'Block Header'
5. See '3.12588200 **BTC**'

Expected behavior:
1. Go to 'Pool'.
2. Set data of your BCH pool and restart.
3. Go to 'Dashboard'.
4. Scroll down to 'Block Header'
5. See '3.12588200 **BCH**'


 - Bitaxe HW version: Gamma 601
 - Bitaxe HW vendor: AliExpress
 - ESP-Miner FW version: v2.13.0b5
 - Hash Frequency: not relevant
 - Voltage: not relevant
 - Pool URL, Port, User: my local pool settings


## Comments

### mutatrum on 2026-02-06

Duplicate of #1540. Input is welcome there, as it's a non-trivial issue.
