# 256foundation/libreboard issue #15: Feature request: a momentary pushbutton for eMMC boot mode selection

> Source: https://github.com/256foundation/libreboard/issues/15
> Collected: 2026-10-07
> Published: 2025-05-28

- Repository: 256foundation/libreboard
- Type: issue
- Number: 15
- State: closed
- Author: rkuester
- Opened: 2025-05-28
- Closed: 2025-06-09
- Labels: enhancement

## Description

I propose adding a momentary pushbutton in parallel with the existing boot jumper header that temporarily grounds the boot select pin when pressed during power-on. This would remove the hassle of finding and positioning jumpers, significantly improving the Mujina Firmware flashing process for developers and end users.

Currently, enabling USB bootloader mode on the CM5 daughterboard requires manually placing a jumper across the boot header pins, which is cumbersome during frequent development cycles. Since all CM5-compatible compute modules with eMMC don't boot from SD card, using the boot select jumper to enter USB loader mode is critical for programming these modules with rpiboot. I've tested this behavior using a jumper as a momentary connection and confirmed the CM5 only needs the boot pin pulled low for a few seconds after power is applied—once the boot sequence completes, the CM5 enters loader mode and waits for programming via USB.

## Comments

### Schnitzel on 2025-05-30

great! will definitely add this!

### Schnitzel on 2025-06-09

this has been implemented in the newest version - see the secondary button on the left/top edge

![Image](https://github.com/256-Foundation/Libre-Board/blob/main/assets/renders/face_top.png?raw=true)
