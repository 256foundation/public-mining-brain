# bitaxeorg/ESP-Miner issue #289: AxeOS overview shows "WiFi Status: Retrying"

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/289
> Collected: 2026-10-07
> Published: 2024-08-14

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 289
- State: closed
- Author: skot
- Opened: 2024-08-14
- Closed: 2024-10-10
- Labels: bug

## Description

the AxeOS Logs tab in the overview section shows "WiFi Status: Retrying xx" even though WiFi is connected and working fine.

<img width="387" alt="image" src="https://github.com/user-attachments/assets/849eceeb-a50f-4f33-b97a-7b01701804df">


## Comments

### WantClue on 2024-08-14

Add some logging to the retrying function and let's see why this gets called. Haven't seen this in any of my tested devices.
