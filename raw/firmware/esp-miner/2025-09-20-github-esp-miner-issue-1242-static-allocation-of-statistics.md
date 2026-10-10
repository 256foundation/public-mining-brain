# bitaxeorg/ESP-Miner issue #1242: Static allocation of statistics data

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1242
> Collected: 2026-10-07
> Published: 2025-09-20

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1242
- State: closed
- Author: mutatrum
- Opened: 2025-09-20
- Closed: 2025-10-28
- Labels: enhancement

## Description

It's leaking ~40kb in 24 hours.

<img width="1915" height="976" alt="Image" src="https://github.com/user-attachments/assets/c2752e20-3cd2-4a14-9164-0cd57cfeed7e" />

## Comments

### duckaxe on 2025-09-20

Where should we look? AxeOS or ESP Miner?

### mutatrum on 2025-09-20

This is heap on the ESP32, so esp-miner. It might have been there already, but the new charts makes it easier to show.

### mutatrum on 2025-09-20

It might just be the statistics task collecting 720 data points.

### mutatrum on 2025-09-20

Confirmed, I let it run for 6 hours on the shortest statistics setting (every 30 seconds for 6 hours). After 6 hours and 10 minutes, this was the graph:

<img width="1915" height="976" alt="Image" src="https://github.com/user-attachments/assets/e5a6317c-6175-43ab-9959-b1ce5532ed2e" />

It might make sense to switch from dynamic allocation to static, if we then run into issues, we can catch the error and still continue running. And I guess this graph will get people asking questions.

### WantClue on 2025-09-20

agreed, a static allocation makes more sense here, this could get confusing if we actually run into a mem leak issue

### duckaxe on 2025-09-21

<img width="1602" height="446" alt="Image" src="https://github.com/user-attachments/assets/74052db9-3754-4ab3-9b91-7cb3a9b1c4ce" />

4h with data logging off.
