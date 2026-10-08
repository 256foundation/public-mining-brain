# bitaxeorg/ESP-Miner issue #811: BUG: Where did the average hashrate line go?

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/811
> Collected: 2026-10-07
> Published: 2025-04-01

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 811
- State: closed
- Author: jtsmith0101
- Opened: 2025-04-01
- Closed: 2025-04-01
- Labels: none

## Description


**Describe the bug**
Since at least version 2.5.0, the histogram for the asic hashrate included an average hashrate line.  This appears to be missing in 2.6.1.

**To Reproduce**
Update to 2.6.1

**Expected behavior**
Unless discontinued, I expected to see the hashrate, asic temp, and an average hashrate (I guess this was computed and displayed a rolling 30 minutes or so)

**Screenshots & Photos**
If applicable, add AxeOS screenshots and/or photos of your Bitaxe to help explain your problem.

**Hardware (please complete the following information):**
 - Bitaxe HW version: [Gamma 601]
 - Bitaxe HW vendor: [Where you purchased the Bitaxe, or self-built]
 - ESP-Miner FW version: [2.6.1]


![Image](https://github.com/user-attachments/assets/f6af9c69-c0d6-4cd4-b606-3298ee552abf)



## Comments

### mutatrum on 2025-04-01

It moved to the card at the top:

![Image](https://github.com/user-attachments/assets/39e93e8e-a0cf-4aab-a659-919bab599e8c)

See #633 for context. In short, average hash rate makes more sense as a single value instead of a graph line.

### jtsmith0101 on 2025-04-01

Ha!  Fair enough
