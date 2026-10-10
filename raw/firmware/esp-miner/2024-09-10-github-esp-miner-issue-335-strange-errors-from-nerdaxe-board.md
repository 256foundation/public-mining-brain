# bitaxeorg/ESP-Miner issue #335: Strange Errors from Nerdaxe Board

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/335
> Collected: 2026-10-07
> Published: 2024-09-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 335
- State: closed
- Author: nG64
- Opened: 2024-09-10
- Closed: 2024-09-11
- Labels: invalid

## Description

I noticed some Strange behavior on my nerdaxe board. It reboots every now and then randomly, and after some time mining on public pool my difficulty resets, and i get errors in the log, only option is to restart the miner.

Overview
Model:	BM1366
Uptime:	5 hours
WiFi Status:	Connected!
Free Heap Memory:	103436
Version:	v2.1.9-36-gaecb8af-dirty
Board Version:	204


0CCF8000
₿ (18151143) bm1366Module: Invalid job found, 0x30
₿ (18154723) bm1366Module: Job ID: 30, Core: 77/4, Ver: 0CCF8000
₿ (18154733) bm1366Module: Invalid job found, 0x30
₿ (18158313) bm1366Module: Job ID: 30, Core: 77/4, Ver: 0CCF8000
₿ (18158313) bm1366Module: Invalid job found, 0x30
₿ (18161893) bm1366Module: Job ID: 30, Core: 77/4, Ver: 0CCF8000

Current Version: v2.1.9-36-gaecb8af-dirty

URL:	public-pool.io
Port:	21496




## Comments

### MyOwn2C on 2024-09-10

This is for "regular" ESP-Miner
For Nerdaxe related issues, go to their Github
https://github.com/BitMaker-hub/ESP-Miner-NerdAxe
