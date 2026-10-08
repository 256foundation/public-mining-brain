# bitaxeorg/ESP-Miner issue #1813: Was there a validation/activation key or check added to 2.14.1 or 2.14.2?

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1813
> Collected: 2026-10-07
> Published: 2026-07-11

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1813
- State: closed
- Author: iL3GEND88
- Opened: 2026-07-11
- Closed: 2026-07-14
- Labels: none

## Description

Note: Issues are not for customer support, configuration or discussion. For those topics please consult with your HW vendor or the OSMU Discord at: https://osmu.bitaxe.org

**Describe the bug**
A clear and concise description of what the bug is.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to '...'
2. Click on '....'
3. Scroll down to '....'
4. See error

**Expected behavior**
A clear and concise description of what you expected to happen.

**Screenshots & Photos**
If applicable, add AxeOS screenshots and/or photos of your Bitaxe to help explain your problem.

**Hardware (please complete the following information):**
 - Bitaxe HW version: [e.g. Ultra 205, Supra 401, etc]
 - Bitaxe HW vendor: [Where you purchased the Bitaxe, or self-built]
 - ESP-Miner FW version: [e.g. 2.1.1, etc]
 - Hash Frequency:
 - Voltage:
 - Pool URL, Port, User:

**Additional context**
Add any other context about the problem here.

## Comments

### ghost on 2026-07-13

Activation key to make the device(s) work !
No !

Where are you getting the firmware from ? 

### iL3GEND88 on 2026-07-13

I patched the amp limit a little higher. On 2.14.0 it was just fine to OTA. On 2.14.2 the same patch fails. Says validation/activation failed. Just to explain a bit further. I would get a power fault bc of the limit sort of randomly. I'm not raising the device settings any further than that which it would run most of the time. Changed the amp limit and can now run 24/7 at those same settings. 

### ghost on 2026-07-13

Your first post here did not provide details.

Define "patch" here, explain what your doing etc ? 




### mutatrum on 2026-07-13

Please fill in the open questions on your first post.

### iL3GEND88 on 2026-07-14

What I mean by “patch”: I’m binary-editing the compiled esp-miner.bin to raise the TPS546 current-limit constant (the amp cap), then recomputing the ESP32 image integrity so it’s a valid image — the 1-byte XOR segment checksum and the appended SHA-256. I’m not touching anything else in the image. Purpose is just to raise the current ceiling slightly so the device stops throwing intermittent power faults at the settings I already run.

The behavior I’m asking about:
On 2.14.0, the patched image OTA-flashes fine and runs.
On 2.14.2, the byte-identical style of patch (same edit, integrity recomputed the same way) fails OTA with “Validation / Activation Error.”
The clean, unpatched 2.14.2 image flashes fine, so it’s specifically the modified image being rejected.

So my question is whether 2.14.1 or 2.14.2 added an OTA image validation / signature / anti-rollback check that would reject a modified image, that wasn’t present (or wasn’t enforced) in 2.14.0. I noticed 2.14.0 bumped ESP-IDF to 5.5.3 — wondering if OTA validation tightened around then.

Where I’m getting the firmware: the official releases from this repo (bitaxeorg/ESP-Miner) — 2.14.0 and 2.14.2 official esp-miner.bin. Not a third-party build.

Hardware:

HW version: Bitaxe 650 Duo (dual BM1370)
HW vendor: Solo Satoshi
ESP-Miner FW version: 2.14.0 (works patched) vs 2.14.2 (patched rejected)
Hash Frequency: 600 MHz 
Voltage: 1280
Pool: ckpool

I just wanted to understand whether validation was intentionally added in 2.14.1/2.14.2, so I know whether manual patching is simply no longer supported on current firmware. Happy to provide the exact byte offsets I’m editing or logs if useful.
![image](https://github.com/user-attachments/assets/3c21d30f-35e2-41fb-bd37-0dbd6c77e349)

### skot on 2026-07-14

This is probably a poor choice of words for this error message. It just means that the image you are attempting to flash is corrupted or somehow built incorrectly and the ESP32 bootloader is rejecting it rather than attempting to boot it and putting your bitaxe into a bad state.

### mutatrum on 2026-07-14

> What I mean by “patch”: I’m binary-editing the compiled esp-miner.bin to raise the TPS546 current-limit constant (the amp cap) [..]

We didn't add any specific things, you're always free to flash your device. It indeed seems the underlying OTA system rejected the modified firmware. 

Are you trying to change `TPS546_INIT_IOUT_OC_FAULT_LIMIT`? It's probably easier to build a custom firmware, as to be fair I have no idea what checksums/verifications are on the firmware image.

### iL3GEND88 on 2026-07-14

Yes the TPS546_INIT_IOUT_OC_FAULT_LIMIT is what I edited. Thank you for your help. I will build the firmware as you suggested and try it that way. 

### WantClue on 2026-07-14

the build target is not correct and the error message is correct there
