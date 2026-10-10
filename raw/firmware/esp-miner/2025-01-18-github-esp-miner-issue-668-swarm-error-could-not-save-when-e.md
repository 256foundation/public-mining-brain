# bitaxeorg/ESP-Miner issue #668: Swarm error: "could not save" when entering IP address

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/668
> Collected: 2026-10-07
> Published: 2025-01-18

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 668
- State: closed
- Author: Ben-in-Chicago
- Opened: 2025-01-18
- Closed: 2025-01-19
- Labels: none

## Description

Note: Issues are not for customer support, configuration or discussion. For those topics please consult with your HW vendor or the OSMU Discord at: https://osmu.bitaxe.org

**Describe the bug**
Since updating to v2.5.0, an error is presented when attempting to add devices to the Swarm menu.

**To Reproduce**
On the Swarm menu of any BitAxe, enter the IP address of another BitAxe. The error "Could not save" is shown and the device is not added to the Swarm.

**Expected behavior**
Device is added.

**Screenshots & Photos**

![Image](https://github.com/user-attachments/assets/53c5fef1-523a-410c-8f26-8c8b93a7f0a5)

**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma, Supra and Ultra
 - Bitaxe HW vendor: 
 - ESP-Miner FW version: 2.5.0
 - Hash Frequency:
 - Voltage:
 - Pool URL, Port, User:

**Additional context**
I was running v2.3.0 on the Supra and Ultra and v2.4.0 on the Gamma when Swarm previously worked.


## Comments

### ghost on 2025-01-19

When updating or downgrading the firmware you need to flash both the "esp-miner.bin" & "www.bin" files for that firmware version to the device otherwise your going to have problems.

### Ben-in-Chicago on 2025-01-19

Thanks! I just need to figure out how to change the display back to the prior view. The bright red isn't desired.

Edit: nvm this version has display options
