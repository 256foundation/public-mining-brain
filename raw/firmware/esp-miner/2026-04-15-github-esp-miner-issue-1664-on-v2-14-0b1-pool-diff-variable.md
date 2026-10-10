# bitaxeorg/ESP-Miner issue #1664: On v2.14.0b1, Pool Diff variable returned as decimal with 12-digit accuracy instead of an integer value

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1664
> Collected: 2026-10-07
> Published: 2026-04-15

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1664
- State: closed
- Author: Hylinus
- Opened: 2026-04-15
- Closed: 2026-04-16
- Labels: none

## Description

**Describe the bug**
On v2.14.0b1, the pool difficulty value is being returned as a decimal with an accuracy of 12 digits as opposed to an integer.

**To Reproduce**
Steps to reproduce the behavior:
This is visible in any section of the UI where the pool difficulty is displayed: on the dashboard as well as the swarm page.

**Expected behavior**
Pool difficulty should be returned as an integer instead of a decimal.

**Screenshots & Photos**
Dashboard's Pool Section:
<img width="237" height="93" alt="Image" src="https://github.com/user-attachments/assets/43962a2e-af3d-4785-af96-40a7b335200d" />

Swarm Page Section:
<img width="411" height="119" alt="Image" src="https://github.com/user-attachments/assets/5122ddfe-7919-43d4-8d08-e11934845026" />

**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma 601
 - Bitaxe HW vendor: Altair Tech
 - ESP-Miner FW version: 5.5.3


## Comments

### Hylinus on 2026-04-15

Possibly related to the above issue, in the logs, the difficulty is shown as a negative integer. Let me know if you would like a different issue opened for this:

<img width="641" height="61" alt="Image" src="https://github.com/user-attachments/assets/0e7459ba-caa1-4705-9d2f-96f8485b4b72" />

### Hylinus on 2026-04-16

My "issue" [may not be an issue](https://github.com/bitaxeorg/ESP-Miner/issues/1592) after all. I should read the release notes more thoroughly. Please feel free to close. If I need to open one for the negative number in the logs, let me know and would be happy to oblige.

### mutatrum on 2026-04-16

The log has a bug, that's fixed in #1661. As for the fractional, it seems your pool has fractional difficulty, although it has a lot of fractional digits?

### Hylinus on 2026-04-16

Closing non-issue. Using Miningcore to mine DBG on an Umbrel server, which seems to set the difficulty as shown.
