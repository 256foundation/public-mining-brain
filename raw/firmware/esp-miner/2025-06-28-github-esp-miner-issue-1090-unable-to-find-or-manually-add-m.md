# bitaxeorg/ESP-Miner issue #1090: Unable to find or manually add multi-chip devices in Swarm Mode in v2.9.0b6

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1090
> Collected: 2026-10-07
> Published: 2025-06-28

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1090
- State: closed
- Author: Hylinus
- Opened: 2025-06-28
- Closed: 2025-06-29
- Labels: bug, critical

## Description

**Describe the bug**
Multi-chip devices (2 SupraHex with software v2.6.3-TCH-All-In-One) are not being automatically detected, nor can they be manually added in v2.9.0b6.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to/click on 'Swarm' section/menu option.
2. Wait for automatic scan to finish. Or click on 'Automatic Scan' to initiate scan.
3. Notice that multi-chip devices do not populate page.
4. Type in IP address of multi-chip device into 'Manual Addition' text box and click 'Add' button.
5. Notice that multi-chip devices do not populate page.

**Expected behavior**
Multi-chip devices should appear in 'Swarm' section either by automatic scan or manually adding the IP address of the devices.

**Screenshots & Photos**
'Swarm' section in v2.9.0b6 does not display multi-chip devices:
![Image](https://github.com/user-attachments/assets/7860681a-45e0-43cb-8ab1-720b827f8763)

'Swarm' section in v2.6.3-TCH-All-In-One displays multi- and single-chip devices:
![Image](https://github.com/user-attachments/assets/84953984-e819-45fd-b256-8543a0669e41)


**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma 601
 - Bitaxe HW vendor: Altair Tech
 - ESP-Miner FW version: 2.9.0b6


## Comments

### mutatrum on 2025-06-28

Working on it in #1089. Hope to get a fix out this weekend.

### GitCatPurr on 2025-06-28

Came here to post the same issue as @Hylinus.

![Image](https://github.com/user-attachments/assets/eefae71f-cd8e-4555-b10b-da31a6583406)
![Image](https://github.com/user-attachments/assets/6466c12d-163b-40d6-8ac9-450fb186b906)
