# bitaxeorg/ESP-Miner issue #446: Swarm - Issue with logs being shown in new Chrome window for any device via it's IP address

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/446
> Collected: 2026-10-07
> Published: 2024-11-02

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 446
- State: closed
- Author: ghost
- Opened: 2024-11-02
- Closed: 2025-04-16
- Labels: none

## Description

**Describe the bug**

I've been testing the latest updates that have been pushed to the 'Master Branch' in the last 24 hours that includes the new AxeOS Theme and Swarm updates.

https://github.com/skot/ESP-Miner/pull/429  &  https://github.com/skot/ESP-Miner/pull/430

First device - Logs output works fine, go to Swarm, then click on any IP address for any one of the devices, new Chrome window opens for that device, Logs don't show, even after refreshing / reloading the page, only starts to work after going to the Swarm page for the 2nd device (or any device via it's IP link).

**To Reproduce**
Steps to reproduce the behavior:

Chrome is the default browser.

1. Go to 'Logs' for first device, click 'Show Logs' - all will be fine here for the first device.
2. Click on 'Swarm' - wait for device list to populate.
3. Click on any one of the devices IP addresses in the list, a new Chrome window will open for that device.

*All steps here onwards are done with the 2nd device in the new browser window for it*

4. Click on 'Logs', then 'Show Logs' - nothing gets displayed in the log window for the device, refreshing / reloading the page does not change anything.
5. Click on 'Swarm' - wait for device list to populate.
6. Click on 'Logs' then click on 'Show Logs' - logs now show in the lower window.

**Expected behavior**
Log output to be shown from the device in the window - this is not happening until you populate the 'Swarm' list for that device (or any device when accessed via it's IP address from the first device).

**Video of the issue can be found in the OSMU discord in the firmware-testing channel.**
_Video showing the issue is too big to upload here._


## Comments

### WantClue on 2025-04-16

This should no longer happen, please tag if it still appears
