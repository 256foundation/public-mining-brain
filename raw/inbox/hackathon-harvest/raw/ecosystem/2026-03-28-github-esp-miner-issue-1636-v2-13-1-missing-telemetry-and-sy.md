# bitaxeorg/ESP-Miner issue #1636: [v2.13.1] Missing telemetry and system logs (Voltage/Current/Temp/Fan) on GammaTurbo (Board 800)

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1636
> Collected: 2026-10-07
> Published: 2026-03-28

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1636
- State: closed
- Author: benjacusu
- Opened: 2026-03-28
- Closed: 2026-03-28
- Labels: none

## Description



**Describe the bug**
After updating to v2.13.1, the dashboard no longer displays telemetry data for voltage, current, or temperature. The system displays a "Low Voltage" warning and performance has dropped to ~2.14 TH/s (previously ~2.4 TH/s).

Crucially, the system logs show no records of voltage, current, or temperature verifications, and fan checks are also missing. It appears the monitoring services are either not initializing or failing silently.

**To Reproduce**

1- Flash Bitaxe GammaTurbo with Firmware/AxeOS v2.13.1.
2- Access the AxeOS web interface and check the dashboard.
3- Observe the "Low Voltage" warning and empty telemetry fields.
4- Go to the Log section and notice the complete absence of sensor or fan telemetry entries.

**Expected behavior**
Telemetry data and fan status should be visible on the dashboard and regularly reported in the system logs.

**Screenshots & Photos**
![Image](https://github.com/user-attachments/assets/23f7aae5-e8dd-41be-9eef-6749012122f6)

**Hardware** 

- Bitaxe HW version: GammaTurbo (Board 800)
- Bitaxe HW vendor: Bitsoloplayer
- ESP-Miner FW version: v2.13.1
- Hash Frequency: 2.14TH/s
- Voltage: 12
- Pool URL, Port, User: PublicPool on Umbrel

*Additional context*

- ASIC Type: 2x BM1370
- ESP-IDF Version: v5.5.2
- AxeOS Version: v2.13.1
- Board Version: 800

The lack of log entries suggests a communication failure (possibly I2C) or a service initialization error in this specific firmware version for the Board 800.

The performance drop is likely due to the system entering a "safe mode" or thermal throttling because it cannot verify temperatures.

## Comments

### mutatrum on 2026-03-28

The 800 board is not supported, see https://github.com/bitaxeorg/ESP-Miner/issues/1543#issuecomment-3864555742 for more details.
