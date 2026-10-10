# bitaxeorg/ESP-Miner issue #1649: Remove/Replace "You don't have a share in the coinbase reward" for 256 Foundation pool

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1649
> Collected: 2026-10-07
> Published: 2026-04-06

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1649
- State: open
- Author: adamdecaf
- Opened: 2026-04-06
- Closed: n/a
- Labels: none

## Description

**Describe the bug**
After upgrading to 2.13.x there's a banner telling me about how I don't receive a coinbase payout on the [256 foundation's pool](https://dash.256f.org/). 

**Expected behavior**
I would argue that the 256 foundation's pool is a special case because it's a hash donation pool which supports projects like esp-miner. Instead of a warning could we see a "Thank you for supporting open source mining" banner? 

**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma 
 - ESP-Miner FW version: `2.13.1`
 - Pool URL, Port, User: `pool.256foundation.org`


## Comments

### 0xf0xx0 on 2026-04-06

you can disable the coinbase decoding on the pool settings page, the feature is intended to alert users to scam solo pools. 

<img width="422" height="92" alt="Image" src="https://github.com/user-attachments/assets/a5e92f26-0baa-4c01-a391-e873026f8d9a" />
