# bitaxeorg/ESP-Miner issue #1450: Problems with my internet provider and the ESP32 and BITAXE won't connect

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1450
> Collected: 2026-10-07
> Published: 2025-12-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1450
- State: open
- Author: AngelSerra
- Opened: 2025-12-12
- Closed: n/a
- Labels: none

## Description

My internet provider, Movistar+ or Telefonica, in Spain has blocked all ESP32s and similar devices like cameras from connecting directly to the router. I can't connect any device directly to the router; I can only connect the ESP32 through a switch. I think many people in Spain are experiencing the same issue. They must have changed something in the firmware of my internet provider, Movistar+ or Telefonica. Today, December 12, 2025, there's an update for the fiber optic router. My mobile phone is also affected; I can't connect directly to the router. Is there any solution? My Bitaxe, after its power supply was damaged by lightning during the DANA storm, is now working, but it's giving me an error. I can't connect it to the router, and through the switch, it doesn't provide the maximum speed; it doesn't connect properly. Is there any modification I can make to allow a direct connection?

## Comments

### kukulle-hood on 2025-12-12

@AngelSerra 
Boah, ...these are a buch of problems and steps to solve.
I think the easiest way would be to turn off the WLAN of your original router, take and try a second router and operate this in WAN-Mode (behind the original one).
Turn on the WLAN on the second router and use this second router as primary connection point for your miners.

Or use your mobile phone hotspot as an intermediate connection point for your miners untill you have solved and repaired the problems with your supplier.

This are my only ideas for the moment.

Good luck,
Robert

### AngelSerra on 2025-12-12

I received a message from my internet provider stating that WPA or WEP encryption methods are not compatible with WPS (2.0). If you select either of these methods, WPS functionality will be disabled on your router. WPA devices are no longer compatible with your router. Update your device's firmware to the latest version of the Wi-Fi encryption system; otherwise, the devices will not work. Is there any possibility of this update for my Bitaxe?

### Travetown on 2025-12-13

No, there isn't. 
You need a Wi-Fi router/repeater (with 2.4 GHz and WPA support !) that you should connect to your existing router via LAN. 


### mutatrum on 2025-12-15

We could also look into adding WPS support. https://github.com/espressif/esp-idf/blob/master/examples/wifi/wps/README.md

For now, best chance would to get another router and use that for your home Wi-Fi, disabling the Wi-Fi of the existing router. Strange move by the ISP to disable all that.
