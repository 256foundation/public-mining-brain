# bitaxeorg/ESP-Miner issue #94: About board version distinction

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/94
> Collected: 2026-10-07
> Published: 2024-01-21

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 94
- State: closed
- Author: kakawlala
- Opened: 2024-01-21
- Closed: 2024-03-07
- Labels: documentation

## Description

I got my device from Bitcoin Merch and it has 201 printed on the board.  After updating to version 2.0.7.bin, the power management distinction shows that the board is 204.  I'm really curious if this distinction is correct?

![P_20240121_154244_1](https://github.com/skot/ESP-Miner/assets/89348834/e71e4be1-cff8-48c9-adde-da680595e7f1)

![Screenshot_20240121-153600_Chrome_1](https://github.com/skot/ESP-Miner/assets/89348834/7315927b-4556-41cc-9e5f-c772a5121f66)

Check the 204 board on the Internet. The welding position of ESP32-S3-WROOM-1 should be aligned with the board.
Is my board really 204 instead of 201?

![52-large_default_1](https://github.com/skot/ESP-Miner/assets/89348834/33a7c00b-57fb-4e52-87ed-5c0540824560)



## Comments

### StarGateMiner on 2024-01-21

I just updated and my board version says: Board Version 0.11? is this version 201? wonder why its showing in this format.

### WantClue on 2024-01-21

This is something that needs to be adjusted from the manufacture side.
But for the web flasher this is also an issue. I keep this one open until I do have different board version flashs available and keep you posted

### MyOwn2C on 2024-03-06

Buy from legit sellers to avoid issues. 
Bitaxe being FOSS, there are many vendors that cut corners or make other modifications, and that could cause issues with new releases of ESP-Miner. 

https://bitaxe.org/legit.html
