# bitaxeorg/ESP-Miner issue #1207: Feature request / Enhancement

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1207
> Collected: 2026-10-07
> Published: 2025-08-26

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1207
- State: open
- Author: liepaja2028-maker
- Opened: 2025-08-26
- Closed: n/a
- Labels: none

## Description

It would be very useful to add an automatic frequency and voltage adjustment system in AxeOS with the following logic:
	1.	Dynamic control:
	•	Miner should automatically increase frequency and voltage up to user-defined maximum values.
	•	At the same time, the system should continuously monitor ASIC temperature and VRM/regulator temperature.
	•	If temperature exceeds user-defined thresholds, the system should automatically lower frequency and voltage down to user-defined minimum values.
	2.	Power limit compliance:
	•	Miner should not exceed a user-defined power consumption limit (e.g., 30 W).
	•	Menu interface should allow setting frequency/voltage ranges and power limit.
	3.	Idle mode (pool or internet connection lost):
	•	If main and backup pool are unavailable, or if Wi-Fi/Internet connection is lost, miner should automatically reduce frequency and voltage to minimum values.
	•	This will reduce heat, noise, and power consumption while idle.
	•	Once pool or internet connection is restored, miner should automatically return to the previous working settings.

This functionality would provide automatic safe overclocking/undervolting, extend hardware life, improve energy efficiency, and give users more flexibility.

## Comments

### Travetown on 2025-08-27

https://github.com/bitaxeorg/ESP-Miner/pull/1152#issue-3240038880
A few things are already in the pipeline.

### skot on 2025-08-27

I think sort of advanced control is better suited for a separate application, interfacing with esp-miner via the API.

### mutatrum on 2025-08-28

Point 3: #927
