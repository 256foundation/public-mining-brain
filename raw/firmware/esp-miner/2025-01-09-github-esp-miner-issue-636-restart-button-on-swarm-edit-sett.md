# bitaxeorg/ESP-Miner issue #636: Restart button on Swarm edit settings pages does not restart the target Bitaxe

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/636
> Collected: 2026-10-07
> Published: 2025-01-09

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 636
- State: closed
- Author: skot
- Opened: 2025-01-09
- Closed: 2025-01-12
- Labels: bug

## Description

- In AxeOS on "Bitaxe A" open the Swarm tab
- Click on the edit icon for a different Bitaxe, "Bitaxe B"
- change some settings, click save then restart.

Bitaxe A gets restarted, not Bitaxe B

## Comments

### benjamin-wilson on 2025-01-09

@mrv777 

### Barnminer on 2025-01-10

Mine seems to be restarting the last in the list (3rd Bitaxe). When changing settings and restarting both Bitaxe A & B appears it is restarting C. 
![Screenshot 2025-01-10 071849](https://github.com/user-attachments/assets/b0e6ec7e-55d4-446a-8a56-37d48cbb5813)


### mrv777 on 2025-01-10

I'm thinking its just this, but haven't tested yet:
https://github.com/skot/ESP-Miner/pull/642/files

### skot on 2025-01-12

fixed in #642
