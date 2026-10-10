# bitaxeorg/ESP-Miner issue #1093: Add pool difficulty to Swarm for Bitaxe Devices

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1093
> Collected: 2026-10-07
> Published: 2025-06-28

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1093
- State: closed
- Author: MidwestChris
- Opened: 2025-06-28
- Closed: 2025-07-01
- Labels: enhancement, good first issue

## Description

Note: Issues are not for customer support, configuration or discussion. For those topics please consult with your HW vendor or the OSMU Discord at: https://osmu.bitaxe.org

**Describe the bug**
Swarm on Nerdaxe displays pool difficulty for the nerd devices but does not show this for the Bitaxe devices.  

![Image](https://github.com/user-attachments/assets/51818c53-c88f-42e7-952a-63baef3c9c05)


## Comments

### mutatrum on 2025-06-28

NerdAxe has `poolDifficulty` on `/api/system/info`. Would make sense to do this as well.

### mutatrum on 2025-06-29

It's already available in the info endpoint, but it's called `stratumDifficulty`. Not sure what's wisdom here.

![Image](https://github.com/user-attachments/assets/6dcd9a6b-acdf-4afe-a1aa-cb0c5ea572f9)
