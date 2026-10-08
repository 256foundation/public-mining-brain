# bitaxeorg/ESP-Miner issue #631: Add QR reader to the Stratum User field in AxeOS

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/631
> Collected: 2026-10-07
> Published: 2025-01-09

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 631
- State: open
- Author: skot
- Opened: 2025-01-09
- Closed: n/a
- Labels: help wanted

## Description

Grandma isn't loving the part of Bitaxe setup where she has to type in her public key in order to solo mine. Is it possible to add a javascript QR reader to the Stratum User field so Grandma can just scan her Jade or SeedSigner HWW to easily input this?

## Comments

### WantClue on 2025-02-18

Seems like we can't implement this, iOS requires https to access the camera module. It's imposed by apple and we won't serve AxeOS over https or through a native app. Unless we develop a native iOS app for Bitaxe this can't be implemented


### skot on 2025-02-18

Let's keep this open. Maybe someone can figure it out.
