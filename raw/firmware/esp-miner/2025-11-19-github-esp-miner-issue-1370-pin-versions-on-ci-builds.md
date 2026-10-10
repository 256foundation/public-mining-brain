# bitaxeorg/ESP-Miner issue #1370: Pin versions on CI builds

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1370
> Collected: 2026-10-07
> Published: 2025-11-19

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1370
- State: closed
- Author: mutatrum
- Opened: 2025-11-19
- Closed: 2025-11-24
- Labels: none

## Description

Local build:
<img width="822" height="285" alt="Image" src="https://github.com/user-attachments/assets/06e29232-24f3-403a-96b5-23aa740d585d" />

GitHub workflow:
<img width="645" height="191" alt="Image" src="https://github.com/user-attachments/assets/df5e812d-0857-4545-b42b-e6517d975465" />

It seems the local build picks locked versions, while GitHub picks the latest version. The GH build needs to be pinned as well.

As reported by @STSMiner1 on Discord.
