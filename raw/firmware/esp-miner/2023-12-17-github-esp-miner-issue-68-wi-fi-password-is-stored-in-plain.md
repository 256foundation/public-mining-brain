# bitaxeorg/ESP-Miner issue #68: Wi-Fi password is stored in plain text.

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/68
> Collected: 2026-10-07
> Published: 2023-12-17

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 68
- State: closed
- Author: ray77
- Opened: 2023-12-17
- Closed: 2024-01-07
- Labels: none

## Description

Available for everyone here:
http://ip/api/system/info

## Comments

### skot on 2023-12-17

@benjamin-wilson can we omit the WiFi passwd from the API?

### benjamin-wilson on 2023-12-18

Yes

### benjamin-wilson on 2024-01-07

Fixed https://github.com/skot/ESP-Miner/commit/84c06110f60c7c382ea4ad742ee9018d3daf8ec3

### johnny9 on 2024-01-07

Does the web ui handle the missing value?

### benjamin-wilson on 2024-01-07

It does but I should probably put in a fake placeholder 

### ray77 on 2024-01-08

> It does but I should probably put in a fake placeholder

or any hash, generated from a unique esp device id, wifi-password and mac address.
This would still be a real, fairly secure password that can be used by the ESP to log in.
just an idea.

On the other hand, once the intruder is in the network (port forwarding from outside), he can at least grill the miner - the Wifi password is then pretty much irrelevant.
