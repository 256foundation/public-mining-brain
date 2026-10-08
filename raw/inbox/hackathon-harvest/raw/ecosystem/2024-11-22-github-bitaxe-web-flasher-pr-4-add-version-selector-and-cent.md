# bitaxeorg/bitaxe-web-flasher pull request #4: add version selector and centralize data maintenance

> Source: https://github.com/bitaxeorg/bitaxe-web-flasher/pull/4
> Collected: 2026-10-07
> Published: 2024-11-22

- Repository: bitaxeorg/bitaxe-web-flasher
- Type: pull request
- Number: 4
- State: closed
- Author: w3irdrobot
- Opened: 2024-11-22
- Closed: 2024-11-24
- Labels: none

## Description

- refactor selectors to use a single selector component
- refactor data to be a bit more structured and exist in its own file
- add firmware selector allowing a user to select older versions if they'd like.

the main thing i wanted to do here was add a selector version. however, as i started on it, i noticed that updating selectors and the underlying data used in the site was in multiple places. so i did a bit of a refactor to put all the data used in a single file. now in the future, whether you're adding a new firmware version, board, or device, it's all in one file.

hopefully you find this useful. i used the old one and am looking forward to using this new one.

## Comments

### w3irdrobot on 2024-11-23

I pulled these firmware files from https://github.com/skot/ESP-Miner/releases/tag/v2.3.0

however I understand if you wanna upload these yourself to ensure integrity.
