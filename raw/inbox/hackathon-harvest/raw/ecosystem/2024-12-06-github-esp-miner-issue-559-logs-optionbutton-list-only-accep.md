# bitaxeorg/ESP-Miner issue #559: Logs: OptionButton - List only accepted shares with diff higher than stratumDiff

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/559
> Collected: 2026-10-07
> Published: 2024-12-06

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 559
- State: closed
- Author: seepv
- Opened: 2024-12-06
- Closed: 2025-10-21
- Labels: none

## Description

Would it be possible to hide all Realtime-Logs-Entries with a diff lower than stratumDiff ?

Instead of:
...
₿ (155208313) asic_result: Ver: 2F04C000 Nonce 74640230 diff 258.7 of 1000.
₿ (155212273) asic_result: Ver: 2E9EA000 Nonce 25D70288 diff 1731.0 of 1000.
₿ (155214383) asic_result: Ver: 2F9F0000 Nonce B98C02DA diff 316.9 of 1000.
₿ (155219083) asic_result: Ver: 2410E000 Nonce 68C102A6 diff 376.4 of 1000.
₿ (155221383) asic_result: Ver: 26AF4000 Nonce 1A120262 diff 2463.4 of 1000.
₿ (155223173) asic_result: Ver: 24CEE000 Nonce B35C01C8 diff 1051.1 of 1000.
₿ (155225263) asic_result: Ver: 259F0000 Nonce 233F02A4 diff 485.8 of 1000.
₿ (155225493) asic_result: Ver: 27AB2000 Nonce A3440316 diff 621.4 of 1000.
₿ (155225683) asic_result: Ver: 296BC000 Nonce 2E37018E diff 264.1 of 1000.
₿ (155229713) asic_result: Ver: 29AE4000 Nonce 161C00DE diff 663.3 of 1000.

An OptionButton would than only list these entries (>stratumDiff) :
...
₿ (155212273) asic_result: Ver: 2E9EA000 Nonce 25D70288 diff 1731.0 of 1000.
₿ (155221383) asic_result: Ver: 26AF4000 Nonce 1A120262 diff 2463.4 of 1000.
₿ (155223173) asic_result: Ver: 24CEE000 Nonce B35C01C8 diff 1051.1 of 1000.

## Comments

### mutatrum on 2024-12-08

Some pools have really high stratum difficulty, so that would mean with this change there's hardly any logging.

### mrv777 on 2024-12-10

Could just be a frontend filter if we wanted

### seepv on 2024-12-11

In the frontend it could look like this:

![2024-12_Axe_OS_New_Log_Button](https://github.com/user-attachments/assets/7a184aaf-63c7-4ab2-933a-da94f9ed9660)


### WantClue on 2025-10-21

has been adressed with the filter on the logs
