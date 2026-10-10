# bitaxeorg/ESP-Miner issue #191: Missing www-bin binary for 2.1.6 so AxeOS is not showing the file for being updated from the user interface

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/191
> Collected: 2026-10-07
> Published: 2024-05-31

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 191
- State: closed
- Author: alejandroperezlopez
- Opened: 2024-05-31
- Closed: 2024-06-04
- Labels: none

## Description

According to the github action that ran for v2.1.6 : https://github.com/skot/ESP-Miner/actions/runs/9245502196

The `www-bin` binary was generated but it's missing on the `releases` for v2.1.6

https://github.com/skot/ESP-Miner/releases/tag/v2.1.6

![Screenshot 2024-05-31 at 18 23 04](https://github.com/skot/ESP-Miner/assets/1321052/572ad412-70d7-4c41-8b7f-67f0fe62522c)

This is causing that AxeOS is showing just the `esp-miner.bin` available for being updated from the AxeOS web interface.

## Comments

### skot on 2024-06-04

it is fine to update just esp-miner.bin if those are the only changes. But we'll start adding both for people coming from older versions.
