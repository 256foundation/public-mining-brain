# bitaxeorg/ESP-Miner issue #1154: In v2.10.0b1's Swarm page, some buttons are grayed out as if disabled but still function

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1154
> Collected: 2026-10-07
> Published: 2025-07-19

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1154
- State: closed
- Author: Hylinus
- Opened: 2025-07-19
- Closed: 2025-09-11
- Labels: question

## Description

**Describe the bug**
In the Swarm page of FW v2.10.0b1, the "Refresh List" and remove device from list buttons are present but grayed out. They still function as expected, but give the appearance of being disabled/unusable. 

**To Reproduce**
Steps to reproduce the behavior:
1. Go to "Swarm" page.
2. Notice that the "Refresh List" and trashcan (remove device from list) buttons are grayed out, as if disabled.
3. Pressing the button performs the expected action.

**Expected behavior**
The button should be bright colored to denote it being enabled.

**Screenshots & Photos**
"Refresh List" and trashcan (remove device from list) buttons in v2.10.0b1 look grayed out/disabled.
<img width="313" height="64" alt="Image" src="https://github.com/user-attachments/assets/6d489fb5-0cbe-4155-9c09-5ccbe202ad56" />
<img width="201" height="89" alt="Image" src="https://github.com/user-attachments/assets/22979994-429d-4e50-a6e8-4d1f853fc90b" />

"Refresh List" and trashcan (remove device from list) buttons in v2.9.0 do not look grayed out/disabled.
<img width="298" height="53" alt="Image" src="https://github.com/user-attachments/assets/d3e3711b-3feb-4fe6-ab0e-efce815eb1ed" />
<img width="198" height="85" alt="Image" src="https://github.com/user-attachments/assets/6025a508-1e06-4b19-8f55-71ee6ad162fc" />

**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma 601
 - Bitaxe HW vendor: Altair Tech
 - ESP-Miner FW version: 2.10.0b1

## Comments

### WantClue on 2025-08-21

@Hylinus have you tested this on the recent beta ?

### Hylinus on 2025-08-22

> [@Hylinus](https://github.com/Hylinus) have you tested this on the recent beta ?

@WantClue, the issue is still present in v.2.10.0b3. The button(s) look grayed out but are clickable.

### Hylinus on 2025-09-05

Button issue still present in release v2.10.0

### duckaxe on 2025-09-10

Gray is the secondary color used within the app. It is used for buttons that are less important than primary buttons. Rarely used buttons, such as _Cancel_, are colored gray. The _Refresh LIst_ button is also rarely used because it performs a periodic scan, which is why the secondary color is used. Same logic for the remove button.

### Hylinus on 2025-09-11

Thanks for the info @duckaxe. Closing issue.
