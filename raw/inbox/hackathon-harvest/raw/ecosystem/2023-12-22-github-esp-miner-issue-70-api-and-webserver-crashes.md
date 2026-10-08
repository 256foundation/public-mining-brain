# bitaxeorg/ESP-Miner issue #70: API and Webserver crashes

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/70
> Collected: 2026-10-07
> Published: 2023-12-22

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 70
- State: closed
- Author: ray77
- Opened: 2023-12-22
- Closed: 2024-01-08
- Labels: none

## Description

When many requests come in (eg. many Home Assistant restarts for testing), the web server (Web-App & API) crashes.
However, mining continues. Sometimes after a certain time everything is ok again without restarting.
I've set the polling frequency to the sensor to one minute and it seems to work well.

## Comments

### WantClue on 2024-01-08

This is probably due to the limited capabilities of the ESP32S3 and not a specific issue. Therefore this issue will be closed.
