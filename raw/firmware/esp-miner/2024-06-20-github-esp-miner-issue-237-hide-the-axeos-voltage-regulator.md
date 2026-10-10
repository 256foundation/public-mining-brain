# bitaxeorg/ESP-Miner issue #237: Hide the AxeOS Voltage Regulator Temperature on hardware that does not support

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/237
> Collected: 2026-10-07
> Published: 2024-06-20

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 237
- State: closed
- Author: skot
- Opened: 2024-06-20
- Closed: 2024-06-21
- Labels: bug

## Description

Only Bitaxe with the TPS546 voltage regulator support measuring this temp. On other machines the AxeOS measurement should be hidden.

Hardware that has the TPS546:
- Ultra 207 and higher
- Supra 402 and higher
- Hex 302 and higher

<img width="284" alt="image" src="https://github.com/skot/ESP-Miner/assets/140785/1a385a94-0a86-4cfb-8f75-9c82b3c1caa7">



## Comments

### benjamin-wilson on 2024-06-21

Rather than look at the specific board versions we can just check if the value is greater than the initialized value of 0. A temperature under 0 seems unlikely even in sub 0 temperatures. 

https://github.com/skot/ESP-Miner/commit/c0a1f0f15a42465d5c2cc449facd01361e49303e
