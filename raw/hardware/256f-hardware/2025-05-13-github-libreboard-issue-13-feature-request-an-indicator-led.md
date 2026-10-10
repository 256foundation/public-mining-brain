# 256foundation/libreboard issue #13: Feature request: an indicator LED identical to that of the emberOne

> Source: https://github.com/256foundation/libreboard/issues/13
> Collected: 2026-10-07
> Published: 2025-05-13

- Repository: 256foundation/libreboard
- Type: issue
- Number: 13
- State: open
- Author: rkuester
- Opened: 2025-05-13
- Closed: n/a
- Labels: enhancement

## Description

The emberOne has an RGB LED module we'll use in software for indicating presence, faults, etc. It's on the same board edge as the power rails. It would be nice if Libre Board had the same indicator, and if it were visible in parallel if the boards were all connected via a power rails.

## Comments

### Schnitzel on 2025-05-30

@rkuester thats a great idea, how would you expect to talk to it? the CM5 has LEDs but they are reserved for it's own purpose. Would the RGB via i2c make most sense? something like https://www.seeedstudio.com/BlinkM-I2C-Controlled-RGB-LED-p-836.html (not with these costs, but basically an rgb led that you can control via i2c)

### rkuester on 2025-06-05

I'd use the same [SK6812](https://www.adafruit.com/product/4691) @skot is using on the emberOne. It'll be slick if the hash boards and Libre board match.

The SK6812 uses an unlocked, one-pin data interface. It definitely requires connection to a SPI-capable data line on a Linux-based machine, to meet the timing requirements. Bit-banging from bare metal or a RTOS on a microcontroller might work to meet the SK6812's timing requirements, but Linux can't counted on to bit-bang that precisely.

It'll leave it to you to decide which SPI-capable pin this should be. Taking a quick glance at the CM5, it seems there are possibilities both on the HAT-compatible 40-pin header and exclusively on the 100-pin connectors. Putting it on the 40-pin's signals probably makes it more compatible with alternate compute modules. The LED does not need the SPI clock nor MISO. To not consume that SPI bus completely, I'd gate the signal to the LED with a chip select (driven low when off).

I considered the similar but easier-to-bit-bang [SK9822](https://learn.adafruit.com/adafruit-dotstar-leds/overview), which has a clock and data signal, but I didn't see any right-angle versions of those.

### rkuester on 2025-06-05

> The SK6812 uses an unlocked, one-pin data interface. It definitely requires connection to a SPI-capable data line on a Linux-based machine, to meet the timing requirements. Bit-banging from bare metal or a RTOS on a microcontroller might work to meet the SK6812's timing requirements, but Linux can't counted on to bit-bang that precisely.

For completeness, I'll mention that we could likely implement something fancy using the PIO on the RPi CM5 to delegate timing requirements to hardware without using SPI per se. However, this approach is quite specific to the CM5 and might cut off our compatibility with other compute modules.

### Schnitzel on 2025-06-09

this has been added in the newest version - see the 3rd LED from the top left:

![Image](https://github.com/256-Foundation/Libre-Board/blob/main/assets/renders/face_top.png?raw=true)

I used the exact same LED as on the emberOne, still need to decide how exactly we connect it (it's not routed yet) leaving this open for this. 

### Schnitzel on 2025-09-24

find i2c driver to run the LED
