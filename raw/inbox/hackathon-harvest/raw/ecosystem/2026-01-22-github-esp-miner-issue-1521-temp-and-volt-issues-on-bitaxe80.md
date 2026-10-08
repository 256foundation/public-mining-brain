# bitaxeorg/ESP-Miner issue #1521: temp and volt issues on bitaxe800

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1521
> Collected: 2026-10-07
> Published: 2026-01-22

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1521
- State: closed
- Author: jkapnisakis
- Opened: 2026-01-22
- Closed: 2026-01-22
- Labels: none

## Description



**Hardware (please complete the following information):**
 - Bitaxe HW version: 800
 - Bitaxe HW vendor: ebay
 - ESP-Miner FW version: 2.12.2
 - Hash Frequency: 550
 - Voltage:1150
 - Pool URL, Port, User: https://solostats.ckpool.org/users/bc1qkqwweam5w270t5fqpfy66yqwxrsxpdazdruaa6

**Additional context**

![Image](https://github.com/user-attachments/assets/0b9e7ffd-5a9f-470f-b653-dbbb88fd76af)

<img width="971" height="110" alt="Image" src="https://github.com/user-attachments/assets/df8e99a4-047d-44d5-9bcf-3607735553c7" />


## Comments

### jkapnisakis on 2026-01-22

was working fine w/ v 2.12, started after upgrade to 2.12.2


Device Model | GammaTurbo
Board Version | 800
ASIC Type | 2x BM1370

Firmware Version | v2.12.2
AxeOS Version | v2.12.2
ESP-IDF Version | v5.5.1


### AngelChinchillo on 2026-01-22

The problem appears in versions [v2.13.0b2](https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.13.0b2)
 and [v2.12.2](https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.12.2)

It works fine in [v2.13.0b1](https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.13.0b1)
 and [v2.12.0](https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.12.0)

I think the problem might be because the device_config for the 800 was removed, but I’m not sure.

https://github.com/bitaxeorg/ESP-Miner/pull/1479/files


### ghost on 2026-01-22

This device is not supported, it's a development unit that's why it does have x's in it's model name.
800(x,xx,xxx,xxxx).

https://github.com/bitaxeorg/ESP-Miner/issues/1498#issuecomment-3734345025

### bonifacio123 on 2026-01-22

This should get you working again - you'll have to download the firmware file first and set the path to it and the csv file:

bitaxetool --config config-801.cvs --firmware esp-miner-factory-801-v2.13.0b2.bin

### jkapnisakis on 2026-01-22

reflashed and working again,

### mutatrum on 2026-01-22

The problem is that some 800 models were shipped with an old firmware that had some form of support for some stages of development and some got shipped with custom firmware. There are several development versions out there, so there is no single 800 board version and we have no way of knowing what is on a board, unless it's a released version. If you have trouble running it or want newer firmware, I suggest you contact the seller to supply updated firmware, or get it exchanged for a release version.

Closing this as duplicate of #1498 and #1499.
