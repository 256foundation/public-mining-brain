# bitaxeorg/ESP-Miner issue #1079: v2.9.0b5 Swarm is Broken

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1079
> Collected: 2026-10-07
> Published: 2025-06-26

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1079
- State: closed
- Author: GitCatPurr
- Opened: 2025-06-26
- Closed: 2025-06-27
- Labels: bug, critical

## Description

Model: | Supra  (BM1368)

Won't let you add IP when clicking Add. Also Automatic Scan adds lots of blank results and gives multiple timeout errors. Worked fine previously other miners can still see my Supra.

![Image](https://github.com/user-attachments/assets/96bfc10d-0bcd-4a82-a1d4-423803e229e7)

## Comments

### mutatrum on 2025-06-27

Caused by #1029, error handling was unified between initial scan and refresh, this should not be the case.
