# bitaxeorg/ESP-Miner issue #1025: Missing frequency adjustments on Axe OS 2.8.x UI ?

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1025
> Collected: 2026-10-07
> Published: 2025-06-11

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1025
- State: closed
- Author: BenoistP
- Opened: 2025-06-11
- Closed: 2025-06-11
- Labels: none

## Description

Hello,

Seems frequency/voltage tweaking is no longer possible
(Sliders were previously shown using 'inspect')

**To Reproduce**
Steps to reproduce the behavior:
1. Go to /#/settings
2. Click on F12 (or right click on page, select 'Inspect''
3. Under 'Settings' section 'Frequency' should display sliders in place of drop down list of frequency
4 Please see snapshot

**Expected behavior**
Sliders should allow customizing frequency insted of a 'fixed' list
Same applies to 'Voltage' setting

**Screenshots & Photos**

![Image](https://github.com/user-attachments/assets/5b91fa36-4d37-4ae4-bff6-b1e44de01935)

**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma
 - Bitaxe HW vendor: Plebstyle
 - ESP-Miner FW version: 2.8.1
 - Hash Frequency: 625 Mhz / 1.3 Th
 - Voltage: 1200
 - Pool URL, Port, User:

**Additional context**
Was properly vorking unde 2.6.x version, no idea if it was already missing in 2.7.x


## Comments

### BenoistP on 2025-06-11

Correct snapshot
![Image](https://github.com/user-attachments/assets/92bcbcfd-c4a5-4d45-93a0-62066d39cf83)

I've checked in changelogs and didn't find a clue about a change regarding freq/voltage adjustments, maybe I missed someting

### mutatrum on 2025-06-11

Unfortunately, browsers broke this functionality and we replaced it with a URL parameter. It's described here:
https://github.com/bitaxeorg/ESP-Miner?tab=readme-ov-file#unlock-settings

Thank you for the extensive issue report!

### BenoistP on 2025-06-11

Thanks !

### zachchan105 on 2025-07-19

> Unfortunately, browsers broke this functionality and we replaced it with a URL parameter. It's described here: https://github.com/bitaxeorg/ESP-Miner?tab=readme-ov-file#unlock-settings
> 
> Thank you for the extensive issue report!

I tried this

🎉 The ancient seals have been broken!
⚡ Unlimited power flows through your miner...
🔧 You can now set custom frequency and voltage values.
⚠️ Remember: with great power comes great responsibility!

Although this is supposed to unlock the settings, the options for restart or save don't become an option when I change any values and I don't know why this is happening. Disable overclock mode is the only button I can press.

### zachchan105 on 2025-07-19

> > Unfortunately, browsers broke this functionality and we replaced it with a URL parameter. It's described here: https://github.com/bitaxeorg/ESP-Miner?tab=readme-ov-file#unlock-settings
> > Thank you for the extensive issue report!
> 
> I tried this
> 
> 🎉 The ancient seals have been broken! ⚡ Unlimited power flows through your miner... 🔧 You can now set custom frequency and voltage values. ⚠️ Remember: with great power comes great responsibility!
> 
> Although this is supposed to unlock the settings, the options for restart or save don't become an option when I change any values and I don't know why this is happening. Disable overclock mode is the only button I can press.

lol updated www.bin firmware no problem now 👍
