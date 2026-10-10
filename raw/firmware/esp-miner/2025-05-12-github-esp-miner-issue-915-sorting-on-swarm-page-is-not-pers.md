# bitaxeorg/ESP-Miner issue #915: Sorting on swarm page is not persisted

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/915
> Collected: 2026-10-07
> Published: 2025-05-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 915
- State: closed
- Author: bredita
- Opened: 2025-05-12
- Closed: 2025-05-23
- Labels: none

## Description

**Describe the bug**
Sorting miners by hostname works, but inly unitil the next automatic refresh when it defaults back to sorting by IP.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to 'swarm page' (i see my 5 gammas there)
2. Click on 'hostname', notice the sort order
3. wait until next refresh
4. List is now sorted by IP again.

**Expected behavior**
I expect it to maintain whatever sort order I have chosen.

**Hardware (please complete the following information):**
 - Bitaxe HW version: gamma 601
 - ESP-Miner FW version: 2.7.1




## Comments

### bredita on 2025-05-21

fixed in v2.8.0b2.
thank you.

### mutatrum on 2025-05-23

Fixed by #928.
