# bitaxeorg/ESP-Miner issue #911: Stop mining if pools are not reachable

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/911
> Collected: 2026-10-07
> Published: 2025-05-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 911
- State: closed
- Author: mutatrum
- Opened: 2025-05-12
- Closed: 2026-05-25
- Labels: bug, accepted

## Description

We had an internet outage, and the result was the following:

![Image](https://github.com/user-attachments/assets/6527f9d1-88e3-4ec5-9574-beedfcdddd09)

In this case it would be prudent to stop mining, as it doesn't make sense to keep hashing the same work over and over again.

## Comments

### skot on 2025-05-12

I'd love to get this one fixed soon. I made a "status task" issue a while back. 

My thought is that we have high priority task, running on a long interval that check to make sure mining is happening; stratum server is still sending work, ASIC is still sending shares, vreg is still enabled, etc.

If anything is amiss we should, at the very least show the alert in AxeOS and Bitaxe display.

### mutatrum on 2025-05-12

General status task: #272.

I also saw a video in Discord on stopping/starting the asic: https://discord.com/channels/1091348375301013615/1296092292012179487/1370442421002829924

### ghost on 2025-05-13

Should be nice if there have some kind a method with time limit per task, something like 1-2min even 5min to be safe. 

### mutatrum on 2025-05-28

Depends on #734 

### WantClue on 2025-11-26

Is planned for release 2.13.0

### 0xf0xx0 on 2026-05-25

closed by #1689
