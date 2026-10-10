# bitaxeorg/ESP-Miner issue #187: Swarm devices showing up multiple times

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/187
> Collected: 2026-10-07
> Published: 2024-05-27

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 187
- State: closed
- Author: RuneStone0
- Opened: 2024-05-27
- Closed: 2024-12-01
- Labels: bug

## Description

**Describe the bug**
Its possible to add the same device/IP multiple times to the swarm. Sometimes, I've experienced even adding a single IP would end up in adding two entries. So, something is off no the page where you manage your swarm.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to Swarm
2. Add e.g. 192.168.86.40
3. Add the same IP again (e.g. 192.168.86.40)
4. See two entries on the list

**Expected behavior**
Check that only one unique (hostname/IP) can be added to the swarm.

**Screenshots & Photos**
![swarm-dup](https://github.com/skot/ESP-Miner/assets/6630442/3636d81a-f86c-4e1e-900b-1c83cfe91b75)


## Comments

### WantClue on 2024-12-01

Fixed with recent swarm update.
