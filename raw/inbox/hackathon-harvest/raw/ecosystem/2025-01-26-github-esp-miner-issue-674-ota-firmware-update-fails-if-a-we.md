# bitaxeorg/ESP-Miner issue #674: OTA firmware update fails if a websocket is open

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/674
> Collected: 2026-10-07
> Published: 2025-01-26

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 674
- State: closed
- Author: dustinb
- Opened: 2025-01-26
- Closed: 2025-02-20
- Labels: bug

## Description

**Describe the bug**
OTA firmware update fails if there is a web socket open to the Bitaxe
 
**To Reproduce**
Steps to reproduce the behavior:
1. Open 2 browser tabs to the same Bitaxe
2. Open and start logs in one of them
3. Update the firmware in the other tab
4. Firmware update hangs and eventually shows an error
5. Close the tab with the logging
6. Firmware update completes

**Expected behavior**
Firmware update completes successfully

<img width="945" alt="Image" src="https://github.com/user-attachments/assets/f9122b18-7652-4d9f-90b3-ea2a84a88a64" />

<img width="376" alt="Image" src="https://github.com/user-attachments/assets/e8c19e3d-fe4f-4e57-8083-794062bceada" />

**Hardware (please complete the following information):**
 - Bitaxe HW version: [201, 401, 601]
 - ESP-Miner FW version: [various]
 


## Comments

### WantClue on 2025-02-18

@eandersson would be nice if you could take a look into that.

### eandersson on 2025-02-18

I tried to reproduce this multiple times but never ran into the described issue. Both `esp-miner.bin` and `www.bin` succeeded without issues while viewing realtime logs at the same time.

### eandersson on 2025-02-19

I was finally able to reproduce this issue. It's basically possible to exhaust the httpd stack when combining certain actions e.g. firmware upgrade + streaming logs.
