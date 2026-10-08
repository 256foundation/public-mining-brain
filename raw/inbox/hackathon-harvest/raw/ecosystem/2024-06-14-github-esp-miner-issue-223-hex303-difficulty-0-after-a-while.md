# bitaxeorg/ESP-Miner issue #223: hex303 Difficulty 0 after a while in VK pool

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/223
> Collected: 2026-10-07
> Published: 2024-06-14

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 223
- State: closed
- Author: kakawlala
- Opened: 2024-06-14
- Closed: 2024-06-25
- Labels: none

## Description

After my hex303 connects to the VK mining pool, difficulty 0 will appear after about 4 hours.  The device is still connected and the voltage, current, and power are normal.  It is not caused by overheating (you need to restart hex303 before the difficulty will appear again).    After changing to a public pool, it will still function normally for up to 8 hours.

![Screenshot_20240613-133102_Chrome](https://github.com/skot/ESP-Miner/assets/89348834/d1d6a20d-ea1f-4525-9571-d2b71800fab6)

![Screenshot_20240613-133056_Chrome_1](https://github.com/skot/ESP-Miner/assets/89348834/45272724-0a2d-4126-b6f1-db309b0f27dd)

At 3AM, the hex difficulty level was 0 again. I changed hex303 to connect to the Public Pool and it ran normally for 8 hours (from 3AM to 1PM); then I switched hex303 to connect to the VK mining pool again, and I could see 3PM & 7PM & 11PM.  A total of 3 times of difficulty 0, you need to reopen hex303 to continue working.

![Screenshot_20240615-002207_Chrome (1)](https://github.com/skot/ESP-Miner/assets/89348834/1de73959-cf8b-4a49-9443-98235dedd687)

![Screenshot_20240615-002123_Chrome_1](https://github.com/skot/ESP-Miner/assets/89348834/94dd2b94-53d2-4303-96dd-15d487845308)


The same situation occurs when using 302 and 302 rebase branches.


## Comments

### kakawlala on 2024-06-25

Make 4 units of hex303 and observe that the other 3 units do not have this phenomenon. Please close the discussion on this issue first.
