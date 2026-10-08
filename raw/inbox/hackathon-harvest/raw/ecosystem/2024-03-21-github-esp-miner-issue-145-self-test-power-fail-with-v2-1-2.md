# bitaxeorg/ESP-Miner issue #145: SELF TEST POWER: FAIL with v2.1.2 and v2.1.3 and BItAxe Supra PCB Rev 401

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/145
> Collected: 2026-10-07
> Published: 2024-03-21

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 145
- State: closed
- Author: hanleyp
- Opened: 2024-03-21
- Closed: 2024-04-05
- Labels: none

## Description

SELF TEST POWER: FAIL with v2.1.2 and v2.1.3 and BItAxe Supra PCB Rev 401

**To Reproduce**
Steps to reproduce the behavior:
1. Upgrade to v2.1.2 or v2.1.3 using asp-miner.bin via web or esp-miner-factory-401-v2.1.2/3 using web.
2. Reboot and see failure.
This always occurs for me with v2.1.2 and v2.1.3. v2.1.1 is working (no SELF TEST). But I had to restore with esp-miner-factory-205-v2.1.1.bin.

**Expected behavior**
SELF TEST POWER: PASS

**Hardware (please complete the following information):**
 - Bitaxe HW version: Supra 401
 - Bitaxe HW vendor: altairtech.io
 - ESP-Miner FW version: 2.1.3 and 2.1.3
 - Voltage:1.2V


## Comments

### hanleyp on 2024-03-21

Looks like 'power_consumption_pass' is set to < 13, but I'm getting higher.

I was able to get it to update to v2.1.3 by setting frequency down to 400 (just below 13W) and using the web interface to update the fw.

### MyOwn2C on 2024-03-21

> Looks like 'power_consumption_pass' is set to < 13, but I'm getting higher.
> 
> I was able to get it to update to v2.1.3 by setting frequency down to 400 (just below 13W) and using the web interface to update the fw.

Maybe better to use v2.1.1 until the self-test issue is resolved. 
Per the release notes v2.1.1 should work with Supra (since v2.1.0)
I have Ultra 1366 and I am staying at v2.1.1 for now.


### Shen on 2024-05-21

Why is this issue closed? It's still not working.

### skot on 2024-05-21

> Why is this issue closed? It's still not working.

What's not working for you, specifically?

### Shen on 2024-05-21

> What's not working for you, specifically?

SELF TEST POWER: FAIL
Bitaxe HW version: Supra 400
Bitaxe HW vendor: d-central.tech
ESP-Miner FW version: 2.1.3 (with https://wantclue.github.io/bitaxe-web-flasher/)
Voltage:1.2V

With V 2.1.1 the system boots regulary.

### skot on 2024-05-21

Are you using the "factory" image? This is only for first-time programming (ie at a factory). Please try the "just update" image if you are not already.

### Shen on 2024-05-21

> Are you using the "factory" image? This is only for first-time programming (ie at a factory). Please try the "just update" image if you are not already.

Yes, I used the "factory"-Image. Which other file is the right one? esp-miner.bin and www.bin don't work. The BitAxe is doing nothing if I flash this files.
I tried to just update. SELF TEST POWER: FAIL

### skot on 2024-05-21

Ah, ok I think we have a confusing setup here. I'll release a new esp-miner with this cleared up, hopefully. https://github.com/skot/ESP-Miner/issues/177

in the mean time can you use v2.1.1?

### Shen on 2024-05-21

Yes, thank you!
I will try out the new version when it is ready.
