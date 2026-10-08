# bitaxeorg/ESP-Miner issue #123: Bitaxe 201 no log with 2.1.0 - which factory firmware for flashing?

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/123
> Collected: 2026-10-07
> Published: 2024-03-06

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 123
- State: closed
- Author: TheRockaXXX
- Opened: 2024-03-06
- Closed: 2024-03-15
- Labels: none

## Description

After the update via https://github.com/WantClue/bitaxe-web-flasher (I need to flash it, because the update over the web interface failed with artifacts on the lcd and a not working bitaxe), I can't get any log information in the web interface. It stays empty.

Also I looked for the right firmware for the 201 board: I only can find the 204 or 205 versions a a file without number. Which one is the right one for 201 with BM1366?

Thank you!

## Comments

### MyOwn2C on 2024-03-07

usually esp-miner.bin works for all models.
The factory files contain default configuration for each ASIC type


### TheRockaXXX on 2024-03-10

Thank you. I upgraded with esp-miner.bin and it worked.
