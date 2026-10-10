# bitaxeorg/bitaxe-web-flasher pull request #11: Build images with Docker and Flash

> Source: https://github.com/bitaxeorg/bitaxe-web-flasher/pull/11
> Collected: 2026-10-07
> Published: 2025-01-05

- Repository: bitaxeorg/bitaxe-web-flasher
- Type: pull request
- Number: 11
- State: open
- Author: dustinb
- Opened: 2025-01-05
- Closed: n/a
- Labels: good first issue

## Description

Moved from https://github.com/skot/ESP-Miner/pull/606

added ability to set expressif/idf version
updated web flasher to append local images to the released ones already in firmware_data.json

## Comments

### WantClue on 2025-01-26

I think the best approach woul be to create a new branch off of that. It does not fit into the main branch, main branch needs to run on gh pages and provide the user all the data. Your approach is nice but focused on home use
