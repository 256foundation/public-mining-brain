# bitaxeorg/ESP-Miner issue #1185: bitaxeGT fails to init TPS546 on hard power-on

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1185
> Collected: 2026-10-07
> Published: 2025-08-11

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1185
- State: closed
- Author: skot
- Opened: 2025-08-11
- Closed: 2026-06-05
- Labels: none

## Description

When first plugging in the BitaxeGT 800xxx the TPS546 is not recognized. This seems to be an I2C problem as the display does not init either. Pressing RESET (warm reboot) fixes the problem.

```
I (1315) TPS546: Initializing the core voltage regulator
I (1321) TPS546: Device ID: ff ff ff ff ff ff
E (1326) TPS546: Cannot find TPS546 regulator - Device ID mismatch
E (1333) vcore: VCORE_init(62): TPS546 init failed!
E (1338) system: SYSTEM_init_peripherals(104): VCORE init failed!
I (1345) power_management: Starting
I (1470) http_server: Partition size: total: 2884241, used: 695521
I (1485) http_server: AxeOS version: v2.10.0b1-3-g27c8dc4
I (1486) http_server: Starting HTTP Server
I (1489) dns_server: Socket created
I (1490) dns_server: Socket bound, port 53
I (1494) dns_server: Waiting for data
I (1850) power_management: ASIC Frequency: 525.00MHz
E (1852) i2c.master: i2c_master_transmit_receive(1206): i2c handle not initialized
E (1853) i2c_bitaxe: Unknown device
E (1857) EMC2103: Failed to read fan speed LSB: ESP_ERR_INVALID_ARG
W (1865) power_management: AP mode with invalid temperature reading: -1.0¬∞C - Setting fan to 70%
E (1874) i2c.master: i2c_master_transmit(1195): i2c handle not initialized
E (1882) i2c_bitaxe: Unknown device
E (1886) EMC2103: EMC2103_set_fan_speed(57): Failed to set fan speed
```

## Comments

### WantClue on 2025-08-21

I cannot verify this on my GT prototype

### benjamin-wilson on 2025-10-27

https://github.com/bitaxeorg/ESP-Miner/issues/1291
