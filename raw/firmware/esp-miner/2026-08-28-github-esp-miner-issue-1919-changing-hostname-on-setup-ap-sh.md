# bitaxeorg/ESP-Miner issue #1919: Changing hostname on setup AP shouldn't reload the page

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1919
> Collected: 2026-10-07
> Published: 2026-08-28

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1919
- State: open
- Author: mutatrum
- Opened: 2026-08-28
- Closed: n/a
- Labels: none

## Description

While connected to the setup AP, changing the hostname will redirect the user, however, if a proper SSID and password is already filled in, this is not taken into account. On reload, the new SSID/password are filled in, but the restart button is greyed out because the page doesn't see the values as changed. 

Changing SSID and/or password and forcing a restart should take priority over the redirect when changing the hostname.
