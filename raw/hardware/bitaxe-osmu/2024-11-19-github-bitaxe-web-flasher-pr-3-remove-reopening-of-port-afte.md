# bitaxeorg/bitaxe-web-flasher pull request #3: remove reopening of port after flashing

> Source: https://github.com/bitaxeorg/bitaxe-web-flasher/pull/3
> Collected: 2026-10-07
> Published: 2024-11-19

- Repository: bitaxeorg/bitaxe-web-flasher
- Type: pull request
- Number: 3
- State: closed
- Author: w3irdrobot
- Opened: 2024-11-19
- Closed: 2024-11-20
- Labels: none

## Description

after successful flashing, we are attempting to reopen the serial port but it fails because it's already open. this pr simply removes the reopening since it doesn't appear to be needed.

closes #2
