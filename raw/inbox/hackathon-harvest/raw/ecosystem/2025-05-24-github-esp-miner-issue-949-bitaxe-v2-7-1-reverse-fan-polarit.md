# bitaxeorg/ESP-Miner issue #949: Bitaxe v2.7.1 Reverse Fan Polarity not saving

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/949
> Collected: 2026-10-07
> Published: 2025-05-24

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 949
- State: closed
- Author: sharpharpy
- Opened: 2025-05-24
- Closed: 2025-05-24
- Labels: wontfix

## Description

**Describe the bug**
Installed 2.7.1 and noticed in settings that Reverse FAN polarity was unticked (it was ticked prior to upgrading on v2.6.5).

**To Reproduce**
Steps to reproduce the behavior:
1. Settings - tick reverse fan polarity.
2. Click on 'SAVE'
3. Restart Miner
4. Go back in Settings and Reverse Fan polarity is Unticked

**Expected behavior**
The reverse fan polarity setting should persist

**Screenshots & Photos**
Go try it yourself, i tried on 2 bitaxe gammas, both same exhibit same behaviour.,

**Hardware (please complete the following information):**
 Bitaxe gamma
default settings from day 1, no settings changed
 - ck pool


## Comments

### WantClue on 2025-05-24

Hey there, the fan polarity option has been removed from AxeOS.
If you perform updates, make sure to update the esp-miner.bin and the www.bin always
