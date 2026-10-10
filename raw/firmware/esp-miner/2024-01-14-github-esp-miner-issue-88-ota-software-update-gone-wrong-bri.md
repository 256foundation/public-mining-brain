# bitaxeorg/ESP-Miner issue #88: OTA software update gone wrong, bricked miner.

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/88
> Collected: 2026-10-07
> Published: 2024-01-14

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 88
- State: closed
- Author: Habies
- Opened: 2024-01-14
- Closed: 2024-01-15
- Labels: none

## Description

After a ota update my miner stopped working.
No more display and no wifi.
Is it possible to update the esp32 with a USB to serial interface?
My miner does not have a usb connector.
The board is a JDHX Bit Lottery BM1397 v3.8
Is there a tuturial how to flash the esp32 with a usb-serial converter or a esp-programmer?

## Comments

### skot on 2024-01-14

You need to reprogram the ESP32-S3 using the ESP-PROG programmer and bitaxetool and/or esptool software. There are several generic ESP32 tutorials out there on this.

unfortunately the manufacturer of your bitaxe has decided to modify the design and not publish documentation on their changes, so you’re on your own there.

### WantClue on 2024-01-15

You can also use A Serial-to-USB Bridge. I did this in one of my first videos about it. It does require a bit of soldering of steady hands with all the pins.
With this information now I close this issue.
