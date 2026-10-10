# bitaxeorg/ESP-Miner issue #1476: ASIC Temp chart misleading on multi chip units

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1476
> Collected: 2026-10-07
> Published: 2025-12-31

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1476
- State: closed
- Author: bonifacio123
- Opened: 2025-12-31
- Closed: 2026-08-11
- Labels: good first issue, design

## Description

On multi-chip units it seems the graph is charting the ASIC Temps for ASIC #1 (800 GT in this example). For this metric I would think the highest temperature value of all the ASIC's should be used. Thank you.


<img width="1452" height="637" alt="Image" src="https://github.com/user-attachments/assets/cd620573-c8ac-4126-86a9-d46a9d1c805e" />


<img width="506" height="649" alt="Image" src="https://github.com/user-attachments/assets/e14405ce-8619-41ac-acd9-702a78cd525a" />

## Comments

### mutatrum on 2026-06-02

See #1730
