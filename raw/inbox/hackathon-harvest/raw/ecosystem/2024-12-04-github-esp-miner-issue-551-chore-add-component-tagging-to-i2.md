# bitaxeorg/ESP-Miner issue #551: Chore: Add component tagging to i2c errors

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/551
> Collected: 2026-10-07
> Published: 2024-12-04

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 551
- State: closed
- Author: mutatrum
- Opened: 2024-12-04
- Closed: 2025-01-04
- Labels: enhancement

## Description

If there's a problem with i2c, it throws errors but it's unclear for which device this is. Errors should be annotated by the device id or even better, device tag.

## Comments

### mutatrum on 2024-12-04

```E (8014) i2c.master: I2C transaction unexpected nack detected
E (8014) i2c.master: s_i2c_synchronous_transaction(880): I2C transaction failed
E (8014) i2c.master: i2c_master_transmit_receive(1118): I2C transaction failed
E (10024) i2c.master: I2C transaction unexpected nack detected
E (10024) i2c.master: s_i2c_synchronous_transaction(880): I2C transaction failed
E (10024) i2c.master: i2c_master_transmit_receive(1118): I2C transaction failed
E (12034) i2c.master: I2C transaction unexpected nack detected
E (12034) i2c.master: s_i2c_synchronous_transaction(880): I2C transaction failed
E (12034) i2c.master: i2c_master_transmit_receive(1118): I2C transaction failed
```
