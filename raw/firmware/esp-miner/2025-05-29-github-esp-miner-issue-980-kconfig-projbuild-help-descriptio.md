# bitaxeorg/ESP-Miner issue #980: Kconfig.projbuild "help" descriptions incorrect and duplicated

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/980
> Collected: 2026-10-07
> Published: 2025-05-29

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 980
- State: closed
- Author: Nexus9090
- Opened: 2025-05-29
- Closed: 2025-05-30
- Labels: none

## Description


Help descriptions in Kconfig.projbuild are duplicated and incorrect

For example the help for **config GPIO_ASIC_ENABLE** is **GPIO pin for I2C data line (SDA)**. Which is clearly the wrong description for this item.

Others also duplicate **GPIO pin for I2C clock line (SCL).**

Presently I'm unable to commit edits otherwise I'd have made the changes myself, perhaps someone can tidy this up when they're doing some housekeeping.

Thanks!

Snippet from Kconfig.projbuild:-

```
config GPIO_ASIC_ENABLE
            int "ASIC enable GPIO pin"
            default 10
            help
                GPIO pin for I2C data line (SDA).

        config GPIO_PLUG_SENSE
            int "Barrel plug sense GPIO pin"
            default 12
            help
                GPIO pin for I2C clock line (SCL).

        config GPIO_I2C_SDA
            int "I2C SDA Pin"
            default 47
            help
                GPIO pin for I2C clock line (SCL).
            
        config GPIO_I2C_SCL
            int "I2C SCL Pin"
            default 48
            help
                GPIO pin for I2C clock line (SCL).
```
