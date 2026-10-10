# 256foundation/asic-rs issue #310: Antminer S21Plus found during scan but ignores sleep/reboot/pool change commands

> Source: https://github.com/256foundation/asic-rs/issues/310
> Collected: 2026-10-07
> Published: 2026-07-09

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 310
- State: open
- Author: Kraitcer
- Opened: 2026-07-09
- Closed: n/a
- Labels: none

## Description

Hi there 👋

I’m using asic-rs via its Python bindings, and while the scanner does find my Antminer S21Plus units without a problem, I’m running into a different issue: the library doesn’t seem to actually control them.

When I try to send commands like:

Enter sleep mode

Reboot the miner

Change mining pool settings

## Comments

### b-rowan on 2026-07-09

Could you confirm what firmware version the miners are?  I wonder if they've changed more functionality in recent updates...

### Kraitcer on 2026-07-09

device_info.firmware — 'AntMiner Stock'
firmware_version — 'Fri Feb 7 11:15:49 CST 2025'

### b-rowan on 2026-07-09

Ok, seems like it's getting the newest implementation.  What does the request look like when you send a sleep command to the miner via the web UI?  Also, when running the function for pause, does it return `True`?

### Kraitcer on 2026-07-09

`pause()` returned `True`, but the device web UI showed no signs that sleep mode was actually applied.

### b-rowan on 2026-07-09

Sleep mode maps to "1" internally, could you confirm if the request from the web UI is also using that value? 

### Kraitcer on 2026-07-09

<img width="1702" height="761" alt="Image" src="https://github.com/user-attachments/assets/e9fd12e8-b8c6-4185-89f5-e818a1de6bea" />

### b-rowan on 2026-07-09

Hmm.  Seems like it might be sending as an int, rather than a string.  I still am not sure why some miners want an int and some want a string, but ill see if I can get some more info.

### b-rowan on 2026-07-09

PR up, install with (`pip install git+https://github.com/b-rowan/asic-rs.git@fix-antminer-sleep`).

### Kraitcer on 2026-07-10

Hi, I tested your fix branch and the problem is still reproducible on my side.

What I changed before testing:

Uninstalled the regular PyPI package
Installed your fix from the branch you provided
Build/install source used: git+[https://github.com/b-rowan/asic-rs.git@fix-antminer-sleep](vscode-file://vscode-app/c:/Users/krait/AppData/Local/Programs/Microsoft%20VS%20Code/fc3def6774/resources/app/out/vs/code/electron-browser/workbench/workbench.html)
Installed commit resolved by pip: 039a4c68e6f34de78045708ee6aed171b73584ba
Then I rebuilt my Python agent into a new EXE with PyInstaller and deployed that EXE on-site
Relevant runtime result from the library side:

pause() returned True
Sleep mode was not confirmed within 90 seconds
Agent response sent back to server:
sleep command accepted for miner 10.22.100.10 (pause() returned True); failed: sleep was not confirmed within 90 seconds

Observed device behavior:

In miner web UI there is still no sign of entering sleep/standby mode

### b-rowan on 2026-07-31

Not sure if this is fixed, we shall see.  Merged the theoretical fix into master.

### b-rowan on 2026-08-31

Any luck with the latest versions?
