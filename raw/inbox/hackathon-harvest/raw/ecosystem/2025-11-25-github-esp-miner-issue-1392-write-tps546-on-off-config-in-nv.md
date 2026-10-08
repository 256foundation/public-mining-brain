# bitaxeorg/ESP-Miner issue #1392: Write TPS546 ON_OFF_CONFIG in NVS

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1392
> Collected: 2026-10-07
> Published: 2025-11-25

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1392
- State: open
- Author: mutatrum
- Opened: 2025-11-25
- Closed: n/a
- Labels: none

## Description

Before any custom config, only do this once:
```
smb_write_byte(dev, PMBUS_ON_OFF_CONFIG, 0x18);
smb_write_byte(dev, PMBUS_STORE_USER_ALL, 0x98);
vTaskDelay(100 / portTICK_PERIOD_MS); //important wait
printf("Configurations saved to TPS546 NVM. \n");
```

## Comments

### skot on 2025-11-25

We need to find a way to only do this if it hasn't already been done.

The TPS546 flash nvm only has something like 1000 write cycles. If we just blindly write the nvm on esp-miner every restart we could break the TPS546.
