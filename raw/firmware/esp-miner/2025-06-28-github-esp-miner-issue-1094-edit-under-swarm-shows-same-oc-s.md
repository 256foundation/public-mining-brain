# bitaxeorg/ESP-Miner issue #1094: Edit under Swarm shows same OC settings for ALL Miners

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1094
> Collected: 2026-10-07
> Published: 2025-06-28

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1094
- State: closed
- Author: Blogster
- Opened: 2025-06-28
- Closed: 2025-06-29
- Labels: bug

## Description

im currently running version Current Version: v2.9.0b6
theres a bug where the oc settings under -> swarm -> are the same for all miners.
For example i have miner 
[192.168.188.148](http://192.168.188.148/)
when i clock on swarm-> edit it shows 606 / 1150
if i open a new tap with http://192.168.188.148/#/settings
it shows 512 / 1150

i did some testing and found that the value of the first miner on swarm i click gets somehow saved and shown on every other miner under swarm -> edit.
So it doesnt fetch the actual value for given miner, it just shows the values retrieved for the first miner u clicked edit on swarm.
Screen from swarm->edit
![Image](https://github.com/user-attachments/assets/4aca4ec9-bc3a-4c4c-93fa-f7fb468ddfba)

screen from x.x.x.148

![Image](https://github.com/user-attachments/assets/f53c1e76-462d-4bd1-a2b2-4e7b51f7709b)
