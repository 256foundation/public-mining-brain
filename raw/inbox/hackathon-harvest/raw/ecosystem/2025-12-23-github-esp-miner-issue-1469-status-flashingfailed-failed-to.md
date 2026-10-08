# bitaxeorg/ESP-Miner issue #1469: status.flashingFailed: Failed to download firmware from GitHub. Please try again.

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1469
> Collected: 2026-10-07
> Published: 2025-12-23

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1469
- State: closed
- Author: jesusinsomnio
- Opened: 2025-12-23
- Closed: 2025-12-24
- Labels: none

## Description

Hello,

I have a Bitaxe Gamma 601 that has been mining well for 2 months without any issues. Yesterday, I turned it off by unplugging it and moved it to a different location. When I plugged it back in, it no longer worked properly: the Bitaxe continues mining correctly, and I can see it on public-pool, but I can't access it through the Bitaxe web page. I can see the IP on the screen, but I can't connect to it as I did before. Also, on the screen, I see the SSID of the Wi-Fi it's connected to, but on the bottom line, it shows the SSID it has when it connects for the first time (BITAXE_XXXX).

I’ve tried flashing it through the web interface, with the USB-C connected, powering it on, pressing RESET and BOOT simultaneously, releasing RESET first and then BOOT, and when trying to flash through the web, I get the error: status.flashingFailed: Failed to download firmware from GitHub. Please try again. I’ve also tried pressing BOOT, connecting the USB-C, releasing BOOT, and the error while flashing is the same. It's like it can’t find GitHub’s DNS. I’ve pinged GitHub from my PC, and it responds. I’ve tried changing DNS settings on the router, changed the Bitaxe IP, and it still does the same. It mines, but I can’t access the web page to modify settings, and on the screen, part of the factory settings and part of the current configuration appear.

What else can I do?


## Comments

### WantClue on 2025-12-24

wrong repo, please move this issue over to https://github.com/bitaxeorg/bitaxe-web-flasher

Issue is known and is already been worked on
