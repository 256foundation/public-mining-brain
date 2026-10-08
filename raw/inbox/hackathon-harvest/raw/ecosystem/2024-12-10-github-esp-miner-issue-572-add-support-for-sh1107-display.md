# bitaxeorg/ESP-Miner issue #572: Add support for SH1107 display

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/572
> Collected: 2026-10-07
> Published: 2024-12-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 572
- State: closed
- Author: mutatrum
- Opened: 2024-12-10
- Closed: 2025-06-22
- Labels: enhancement, good first issue

## Description

There is a 128x64 OLED display with the same pinout and almost similar form factor of the current display. The driver is also very similar to the SSD1306 display.

![image](https://github.com/user-attachments/assets/cdf3c059-07c9-489e-9fbd-8d357bd88509)

https://nl.aliexpress.com/item/1005006045870999.html

Feature would be to add a config field in the NVS to select the display.

Secondary function would be a `no display` option, for the people who want to take the display off. This could skip the initial errors on the I2C bus trying to find the display.

## Comments

### mutatrum on 2025-04-01

There is now also an 128x128 SH1107 I2C display which should be pin compatible.

![Image](https://github.com/user-attachments/assets/8833dfce-ef1b-4027-a7fa-4e532e293e16)

https://www.amazon.com/HiLetgo-SH1107-128x128-Display-Optinal/dp/B0CFF17DGH

### mutatrum on 2025-05-08

Unfortunately, the 128x128 - which is yuge - is not pin compatible, the order of the pins is different. 🤦 

![Image](https://github.com/user-attachments/assets/2bd9a73e-2786-4084-adb0-ad66d1a43d82)

### skot on 2025-05-09

That looks a little too big, IMO (bitaxeIMAX 😂)

I like the 128x64 a lot

### mutatrum on 2025-05-12

There's no such thing as too big. It's almost the same size as the fan, which could make for some really awesome aesthetic.

### skot on 2025-05-12

it would be awesome to do some graphics. 

### mutatrum on 2025-05-13

There are also 4-pin I2C greyscale displays, which makes a lot of sense for graphics. 

https://github.com/bitbank2/ssd1327

1 bit displays are tricky, especially on such low resolutions. Best one could do is either dials, bars, or sparkline graphs.
