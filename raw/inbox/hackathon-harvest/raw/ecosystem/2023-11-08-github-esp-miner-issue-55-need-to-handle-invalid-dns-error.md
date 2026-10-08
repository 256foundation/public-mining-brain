# bitaxeorg/ESP-Miner issue #55: Need to handle Invalid DNS error

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/55
> Collected: 2026-10-07
> Published: 2023-11-08

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 55
- State: closed
- Author: johnny9
- Opened: 2023-11-08
- Closed: 2024-01-08
- Labels: none

## Description

Entering an invalid DNS name as the stratumurl crashes the application. This is likely a different error flow than  unable to resolve DNS

Example domain name "BTC.global.Luxor.texh"

A curl command can help get your device out of the loop.

curl -X PATCH      -H "Content-Type: application/json"      -d '{"flipscreen":0,"invertscreen":0,"stratumURL":"BTC.global.Luxor.tech","stratumPort":21496,"stratumUser":"address.bitaxeUltra","ssid":"ssid","wifiPass":"password","coreVoltage":1250,"frequency":485}'      http://192.168.1.79/api/system
