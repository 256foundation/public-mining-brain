# bitaxeorg/ESP-Miner issue #1378: Unable to connect to wifi network that doesn't have a password.

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1378
> Collected: 2026-10-07
> Published: 2025-11-23

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1378
- State: closed
- Author: philipbishop1990
- Opened: 2025-11-23
- Closed: 2025-11-29
- Labels: none

## Description

Latest version of firmware will not allow connection to wifi networks that dont have a password. Previous versions did allow this. There was a similar issue with Nerdaxe Gamma which someone has fixed for me in latest pre-release trial.

To reproduce, connect to a wifi network that doesn't have a password. Remove all entries from password box and hit save, an error displays and action cant be completed. Unable to restart with the wifi details to connect to network.

Current hack is to roll back to previous version of firmware, connect to the network and re-update the device firmware to latest. Wifi details remain saved.

Hardware being used Bitaxe Gamma 601 by DTV running v.2.11.0

Previously seen oj Nerdaxe Gamma. Fix communicated to me by person solving 

I (2043) wifi station: WiFi password empty, using WIFI_AUTH_OPEN


## Comments

### mutatrum on 2025-11-24

How did you configure it to use an open network? And in what way doesn't it work with 2.11? 

AFAIK we haven't support open networks at all, as one issue with using an open network is that anyone on such a network can change the settings of your device, they are inherently unsafe.

### shufps on 2025-11-24

Coincidentally on the Nerd*axe FW someone had the same problem.

The solution to just use `WIFI_AUTH_OPEN` or so on a blank password, then it worked.

### mutatrum on 2025-11-24

Related: #348.
