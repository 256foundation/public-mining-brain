# bitaxeorg/ESP-Miner issue #1248: No switch to the fallback pool after restart

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1248
> Collected: 2026-10-07
> Published: 2025-09-25

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1248
- State: closed
- Author: duckaxe
- Opened: 2025-09-25
- Closed: 2025-11-05
- Labels: none

## Description

**Describe the bug**
The following scenario: The primary pool goes offline. Bitaxe switches to fallback 👍. I restart Bitaxe manually. Bitaxe remains on the primary pool and does NOT switch to fallback.

**To Reproduce**
Steps to reproduce the behavior:
1. Set the primary pool to an unavailable pool or shutdown the local pool.
2. Ensure that Bitaxe switches to the fallback pool.
3. Restart Bitaxe.
4. Is Bitaxe remaining in the primary pool?

**Expected behavior**
After restarting, Bitaxe automatically switches to the fallback pool because the primary pool is unavailable.

**Hardware**
 - Bitaxe HW version: Gamma 601
 - ESP-Miner FW version: v2.10.0


## Comments

### WantClue on 2025-10-14

How exactly do you determin that the primary pool is offline, is a socket still created? 
I guess we need to rework the behaviour on no work received to make sure this always works and switches to the fallback

### duckaxe on 2025-10-15

> How exactly do you determin that the primary pool is offline, is a socket still created?

Set the primary pool to the local pool then shutdown the local pool.



### WantClue on 2025-11-04

@duckaxe can you test this behavior again with the recent master branch ? 

### duckaxe on 2025-11-05

@WantClue Now working as expected.
