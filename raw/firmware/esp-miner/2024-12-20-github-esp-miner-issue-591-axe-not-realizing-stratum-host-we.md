# bitaxeorg/ESP-Miner issue #591: Axe not realizing stratum host went down and loops old work

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/591
> Collected: 2026-10-07
> Published: 2024-12-20

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 591
- State: closed
- Author: BitcoinMechanic
- Opened: 2024-12-20
- Closed: 2026-05-24
- Labels: none

## Description

**Describe the bug**
If the pool goes down the axe may not notice if it hasn't found any shares to submit in some amount of time. Unclear what that is.

**To Reproduce**
1. Set high difficulty with DATUM or similar
2. Go for extended period without shares (give it an hour to be on the safe side)
3. Kill DATUM
4. Axe will continue mining without having anywhere to submit shares and without getting fresh jobs

**Expected behavior**
After 30 seconds or so the Axe should realize it's not doing anything useful any more and fail over to pool #2

**Screenshots & Photos**


**Hardware (please complete the following information):**
 - Bitaxe HW version: The 650GH one, firmware v2.4.1
 - Bitaxe HW vendor: Booth at Nashville conf 2024
 - ESP-Miner FW version: [e.g. 2.1.1, etc]
 - Hash Frequency:
 - Voltage:
 - Pool URL, Port, User:
