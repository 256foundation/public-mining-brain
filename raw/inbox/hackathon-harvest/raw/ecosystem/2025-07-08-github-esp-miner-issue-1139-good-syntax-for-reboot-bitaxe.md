# bitaxeorg/ESP-Miner issue #1139: Good syntax for reboot bitaxe

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1139
> Collected: 2026-10-07
> Published: 2025-07-08

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1139
- State: closed
- Author: Ricco59163
- Opened: 2025-07-08
- Closed: 2025-07-09
- Labels: none

## Description

I have a many gamma 601 and I want to reboot on with a http command or script command 
I use 
http://192.168.1.200/api/v1/reboot
curl -X POST http://192.168.1.200/api/v1/reboot

but don't work

thx for help

## Comments

### ghost on 2025-07-08

# System restart action
curl -X POST http://YOUR-BITAXE-IP/api/system/restart
