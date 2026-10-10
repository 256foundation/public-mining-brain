# bitaxeorg/ESP-Miner issue #767: selftest hangs with no responses to the hash test

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/767
> Collected: 2026-10-07
> Published: 2025-03-13

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 767
- State: closed
- Author: skot
- Opened: 2025-03-13
- Closed: 2025-03-26
- Labels: bug, enhancement, help wanted

## Description

When the ASIC never sends a response to the hash test (for whatever reason), the selftest appears to hang. We should add a timeout so that we can show a ASIC FAIL or similar test result in the log and on the OLED

Current situation with a malfunctioning ASIC:
```
I (10124) bm1370Module: Setting Frequency to 512.50MHz (512.50)
tx: [55 AA 51 09 00 08 40 A6 02 30 07]
I (10224) bm1370Module: Setting Frequency to 518.75MHz (518.75)
tx: [55 AA 51 09 00 08 40 A8 02 30 03]
I (10324) bm1370Module: Setting Frequency to 525.00MHz (525.00)
tx: [55 AA 51 09 00 10 00 00 1E B5 0F]
I (10424) self_test: 1 chips detected, 1 expected
I (10424) bm1370Module: Setting max baud of 1000000 
tx: [55 AA 51 09 00 28 11 30 02 00 03]
I (10434) serial: Changing UART baud to 1000000
I (11434) bm1370Module: Setting ASIC difficulty mask to 7
tx: [55 AA 51 09 00 14 00 00 00 E0 04]
I (11434) self_test: Sending work
-> hangs here, forever. No result shown in the log or on OLED
```
