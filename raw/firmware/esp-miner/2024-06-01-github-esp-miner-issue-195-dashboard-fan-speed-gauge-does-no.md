# bitaxeorg/ESP-Miner issue #195: Dashboard fan speed gauge does not reflect automatic fan control speed

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/195
> Collected: 2026-10-07
> Published: 2024-06-01

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 195
- State: closed
- Author: skot
- Opened: 2024-06-01
- Closed: 2024-06-01
- Labels: bug

## Description

<img width="385" alt="image" src="https://github.com/skot/ESP-Miner/assets/140785/2b8a461c-4a74-46a6-8ddd-599201d38a28">
<img width="856" alt="image" src="https://github.com/skot/ESP-Miner/assets/140785/fe369694-d2d1-47b8-88a4-e4cec91fe9c0">

Dashboard fan speed gauge does not reflect the actual fan speed. 
To reproduce this:
1. set fan speed to manual
2. set to 100%, save and reset
3. set to Automatic Fan Control, save and reset
4. load the AxeOS dashboard

## Comments

### skot on 2024-06-01

dupe of #141  which is fixed in (pending?) PR #147
