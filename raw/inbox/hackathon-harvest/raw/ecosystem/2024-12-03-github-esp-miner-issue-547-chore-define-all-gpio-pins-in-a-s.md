# bitaxeorg/ESP-Miner issue #547: Chore: define all GPIO pins in a single place

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/547
> Collected: 2026-10-07
> Published: 2024-12-03

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 547
- State: closed
- Author: mutatrum
- Opened: 2024-12-03
- Closed: 2025-01-04
- Labels: enhancement, good first issue

## Description

Used pins are all over the codebase. Ideally they should be defined in a single header file.

Quick scan found these, there might be others. This needs to be checked against the schema:
```
GPIO_NUM_0    BUTTON_BOOT_GPIO
GPIO_NUM_1    BM####_RST
GPIO_NUM_5    LEDZ_R 
GPIO_NUM_6    LEDZ_G 
GPIO_NUM_7    LEDZ_B 
GPIO_NUM_10   BM####_ENABLE
GPIO_NUM_12   BARREL_CONNECTED
GPIO_NUM_35   LEDX_R 
GPIO_NUM_36   LEDX_G 
GPIO_NUM_37   LEDX_B 
GPIO_NUM_47   I2C_MASTER_SDA_IO
GPIO_NUM_48   I2C_MASTER_SCL_IO
```

## Comments

### WantClue on 2024-12-07

That's a good practice we should do.
