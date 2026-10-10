# bitaxeorg/ESP-Miner issue #639: Access error after applying firmware v2.5.0b1

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/639
> Collected: 2026-10-07
> Published: 2025-01-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 639
- State: closed
- Author: Master0ne
- Opened: 2025-01-10
- Closed: 2025-01-11
- Labels: none

## Description

After updating firmware to v2.5.0b1 trying to update website gives the following error:

![Screenshot from 2025-01-10 08-54-16](https://github.com/user-attachments/assets/b8ced898-4b1a-4d5d-8c41-c29b73e2a595)

The Swarm page then also can not access data of that Bitaxe anymore:

![grafik](https://github.com/user-attachments/assets/18ae1ee7-f95e-4261-96f6-f2c310cbe0dd)

A downgrade of firmware is then also not possible anymore using the Bitaxe's website:

![grafik](https://github.com/user-attachments/assets/506b8b9b-c5cb-4203-929c-8083e70ae85c)


## Comments

### skot on 2025-01-11

There was a bug in 2.5.0b1. You should give the latest 2.5.0b6 a try. You'll need to resurrect your bitaxe over USB with the web flasher -> https://flasher.bitaxe.org

### alexnb7 on 2025-01-11

Yeah, let us know if it works👍🏻

### Master0ne on 2025-01-12

Unfortunately the same problem with v2.5.0b6. Had to go back to v2.4.5 again using the bitaxetool.
