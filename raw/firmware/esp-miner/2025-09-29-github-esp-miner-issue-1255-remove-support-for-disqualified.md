# bitaxeorg/ESP-Miner issue #1255: Remove support for disqualified TPS546D24A voltage regulator in bitaxeGammaTurbo models

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1255
> Collected: 2026-10-07
> Published: 2025-09-29

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1255
- State: open
- Author: skot
- Opened: 2025-09-29
- Closed: n/a
- Labels: enhancement

## Description

The TPS546D24**A** variant voltage regulator has been disqualified for use in the multi-phase BitaxeGT ([bitaxeGT issue #17](https://github.com/bitaxeorg/BitaxeGT/issues/17)). Remove esp-miner support for both TPS546D24**A** `DEVICE_ID` in 800-series `boardversion`. Only TPS546D24**S** `DEVICE_ID` should be supported.

```
static uint8_t DEVICE_ID1[] = {0x54, 0x49, 0x54, 0x6B, 0x24, 0x41}; // TPS546D24A
static uint8_t DEVICE_ID2[] = {0x54, 0x49, 0x54, 0x6D, 0x24, 0x41}; // TPS546D24A
static uint8_t DEVICE_ID3[] = {0x54, 0x49, 0x54, 0x6D, 0x24, 0x62}; // TPS546D24S
```

## Comments

### WantClue on 2025-11-03

any update on this? @skot
