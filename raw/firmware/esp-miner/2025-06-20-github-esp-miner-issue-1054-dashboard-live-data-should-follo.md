# bitaxeorg/ESP-Miner issue #1054: Dashboard live data should follow statistics settings

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1054
> Collected: 2026-10-07
> Published: 2025-06-20

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1054
- State: closed
- Author: mutatrum
- Opened: 2025-06-20
- Closed: 2025-11-28
- Labels: none

## Description

Currently, new data is added to the dashboard graph every few seconds. If there's historical data loaded on the dashboard, this data will be pushed out as the frequency of live data does not match the historical data. This should be aligned.

F.e. if the statistics show 3 days (over 720 points), new data should only be added to the graph every 6 minutes to keep the scope of the graph the same.

## Comments

### mutatrum on 2025-06-20

This is on reload, with 72 hours of data:
![Image](https://github.com/user-attachments/assets/bb829cad-dd57-4237-98f5-c8bac753d0af)
This is after receiving live data for a day:
![Image](https://github.com/user-attachments/assets/0cc05203-d592-4846-82d9-b7646168a4de)

### mutatrum on 2025-11-28

Fixed by #1351
