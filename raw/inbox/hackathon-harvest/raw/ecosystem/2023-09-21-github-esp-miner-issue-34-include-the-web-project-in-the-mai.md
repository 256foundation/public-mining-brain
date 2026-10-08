# bitaxeorg/ESP-Miner issue #34: Include the web project in the main build proccess

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/34
> Collected: 2026-10-07
> Published: 2023-09-21

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 34
- State: closed
- Author: benjamin-wilson
- Opened: 2023-09-21
- Closed: 2023-09-24
- Labels: enhancement

## Description

Building the web project is often overlooked, we should include it in the main build process. 

## Comments

### johnny9 on 2023-09-21

If we do this we need to make sure it can work with incremental building. 

Another option is to move the web to it's own repo and manage releases there. The web UI will likely not be updated as regularly as the firmware so it can have a separate release cycle.
