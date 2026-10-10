# bitaxeorg/ESP-Miner issue #52: Interrupt startup loop

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/52
> Collected: 2026-10-07
> Published: 2023-10-26

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 52
- State: closed
- Author: benjamin-wilson
- Opened: 2023-10-26
- Closed: 2024-01-09
- Labels: none

## Description

If the wifi credentials are correct but the pool information is not or the pool is not available/compatible the system will continuously restart. 

## Comments

### SACREDHAZE1 on 2023-11-23

HOW TO RESET SETTINGS MANUALY ON HARDWARE MINE HAS THIS ISSUE

### benjamin-wilson on 2023-11-23

> HOW TO RESET SETTINGS MANUALY ON HARDWARE MINE HAS THIS ISSUE

Please refrain from using caps lock... 

Anyway, turn off the wifi router or move it out of range and the bitaxe will create its own SSID again so you can connect directly.

### SACREDHAZE1 on 2023-11-23

still has same issue mines 2 accepted and wifi reset

----- Original Message -----
From: "Benjamin Wilson" ***@***.***>
To: "skot/ESP-Miner" ***@***.***>
Cc: "JACOB FASTJE" ***@***.***>, "Comment" ***@***.***>
Sent: Thursday, November 23, 2023 9:24:28 AM
Subject: Re: [skot/ESP-Miner] Interrupt startup loop (Issue #52)

> HOW TO RESET SETTINGS MANUALY ON HARDWARE MINE HAS THIS ISSUE

Please refrain from using caps lock... 

Anyway, turn off the wifi router or move it out of range and the bitaxe will create its own SSID again so you can connect directly.

-- 
Reply to this email directly or view it on GitHub:
https://github.com/skot/ESP-Miner/issues/52#issuecomment-1824610449
You are receiving this because you commented.

Message ID: ***@***.***>


### benjamin-wilson on 2023-11-23

Ok that does not fall under this issue then, please contact the place you purchased it from or OSMU discord help channel for configuration/pool help.

### benjamin-wilson on 2023-12-08

I've run into more situations where this can happen. We need a general way to catch a boot loop.
