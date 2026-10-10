# bitaxeorg/ESP-Miner issue #241: Incorrectly named firmware update file disables browse function

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/241
> Collected: 2026-10-07
> Published: 2024-06-21

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 241
- State: closed
- Author: VortexRadar
- Opened: 2024-06-21
- Closed: 2024-10-10
- Labels: bug

## Description

I encountered an issue with the firmware update process on the Bitaxe Supra running version 2.1.8, specifically when attempting to load a firmware file with an unexpected name.

**Steps to Reproduce**:
1. Download a second/newer copy of `esp-miner.bin` while the first/older version is still in the Downloads folder. On a Mac, the new file gets named `esp-miner (1).bin` for example.
2. Attempt to load the new firmware. An error message appears stating "Incorrect file, looking for esp-miner.bin". This is expected behavior.
3. Under "Update Firmware", click the "Browse" button to try and load the correctly named file.

**Expected Result**:
The system should allow browsing to select the correctly named file.

**Actual Result**:
Instead of allowing file browsing, the system errors out again, referencing the incorrect file name from the previous attempt. 

<img width="644" alt="Bitaxe update firmware error" src="https://github.com/skot/ESP-Miner/assets/93548204/3226c36e-1514-44d0-9de5-52834308b752">

**Workaround**:
Refreshing the page restores the ability to browse for a particular file.


## Comments

### skot on 2024-06-21

interesting... I have not done any testing with misnamed bin files. I'll check it out.. thanks!

### skot on 2024-10-10

I think we want to keep this basic filename check. Definitely until we get proper filetype identification working, like in #400 

### VortexRadar on 2024-10-10

> I think we want to keep this basic filename check. Definitely until we get proper filetype identification working, like in #400

I agree that a check is a good idea. The issue is how it keeps erroring out even if you try to upload another file with the correct file name. For example, if you try uploading a beta/test fw with a different file name and it errors, out, if you hit the "Browse" button again in AxeOS, it doesn't let you browse and select a different file. Instead of errors out again saying that the file you previously tried to upload was named incorrectly.
