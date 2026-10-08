# bitaxeorg/ESP-Miner issue #2010: Request more settings for security, to limit hotspot mode

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/2010
> Collected: 2026-10-07
> Published: 2026-09-30

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 2010
- State: open
- Author: filteredreality
- Opened: 2026-09-30
- Closed: n/a
- Labels: none

## Description


**Describe the issue**
When wifi crash or reboots, the device enters wifi setup-mode and anyone can then take control for a while until it reconnects.

**To Reproduce**
Steps to reproduce the behavior:

1. Reboot  a slow wifi, or turn it off.
2. device enters setup-mode.
3. anyone can take control.


**Expected behavior**
Some advanced settings to optionally secure it.

Settings i wish for:
1. Option to limit setup-mode behind a button press to activate, while the screen turns on and show its disconnected. (show a wrench symbol next to wifi symbol or similar, when it fails to connect to wifi.)

2. Option to edit setup-mode ssid name, and give it a random mac-address if possible, so the device looks generic from the outside.
 
3. Add the http authentication onto setup-mode, and optionally not show the device type, only show host name, username and password field. (include a reset password function via push buttons for x seconds maybe?)
https://github.com/bitaxeorg/ESP-Miner/pull/1750



4. Alternative, Option to disable wifi setup-mode in a smart way, that don't hard lock you out. Or edit timeout settings, so setup-mode don't activate so often.


**Hardware (please complete the following information):**
Ultra                         204
Firmware Version	v2.15.3
ESP-IDF Version	v6.0.2


-Thanks for your work :)
