# bitaxeorg/ESP-Miner issue #1156: Block Found screen on display not working correctly.

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1156
> Collected: 2026-10-07
> Published: 2025-07-21

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1156
- State: closed
- Author: Ohio82
- Opened: 2025-07-21
- Closed: 2025-09-28
- Labels: bug, help wanted, accepted

## Description

*Block found!* scroll not scrolling. Screen status stuck on hash rate etc. Couldn't tell I found a block. 


## Comments

### Ohio82 on 2025-07-21

I was expecting to see BLOCK FOUND scrolling across my screen but it was stuck not scrolling on regular info screen. 


Gamma 601, bought off Amazon Cryptovolmine, 1700ghs hash rate and 1200mV, dgb-stratum.solominer.net:3333...

### skot on 2025-07-22

Confirmed this is a display issue with the Block Found screen. 

### ghost on 2025-07-22

Confirmed, "!!! BLOCK FOUND !!!" only shows for a split second (watch the video below real close at time stamp 0:10 and you will see the issue).

Firmware v2.10.0b1

Device mining to a test strat was use to reproduce this issue.

https://github.com/bitaxeorg/ESP-Miner/blob/master/main/screen.c#L411

https://github.com/user-attachments/assets/466dccd5-dcf7-47a2-b22d-1e215803de4b

<img width="353" height="637" alt="Image" src="https://github.com/user-attachments/assets/52b0b18b-1c50-4259-ab59-a56f35b85c49" />

### mutatrum on 2025-09-28

Fixed by #1213
