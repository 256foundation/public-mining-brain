# bitaxeorg/ESP-Miner issue #482: Please add the current BitAxeDifficulty (1000, 1024, 2048 ...) to the system information page

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/482
> Collected: 2026-10-07
> Published: 2024-11-15

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 482
- State: closed
- Author: seepv
- Opened: 2024-11-15
- Closed: 2024-12-05
- Labels: none

## Description

Please add the current BitAxeDifficulty (1000, 1024, 2048 ...) to the system information Page:
# Get system information
curl http://YOUR-BITAXE-IP/api/system/info

## Comments

### tdb3 on 2024-11-17

Could you please provide a bit more info on what is desired?  For example, the difficulty of the last submitted share?  Something else?

### WhiteyCookie on 2024-11-17

The api did not provide this kind of information 

### seepv on 2024-11-17

@tdb3 The main goal is logging e.g. with a graph in NodeRed.
My BitAxe (HW 204) seams to ramp up from 1000 to 2048/4096, then down to 1024, but after some time get stuck at 1000. Without this info a verification is hard.
The effectiveness (Hashrate) at 1024/2048 seams to be higher than at 1000 but again hard to verify.
[ Bitaxe 204; AxeOS v2.3.0 ]

### tdb3 on 2024-11-17

Opened PR #489 to address this.

### tdb3 on 2024-12-04

@seepv, since #489 included the requested capability, I'm thinking this Issue is resolved.

### seepv on 2024-12-05

@tdb3, #489 resolves it - Thanks - I close this issue.
