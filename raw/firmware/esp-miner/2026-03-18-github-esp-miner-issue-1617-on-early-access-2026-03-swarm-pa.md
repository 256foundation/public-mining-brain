# bitaxeorg/ESP-Miner issue #1617: On early-access-2026-03, swarm page display some information for about 5 seconds, then information disappears

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1617
> Collected: 2026-10-07
> Published: 2026-03-18

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1617
- State: closed
- Author: Hylinus
- Opened: 2026-03-18
- Closed: 2026-05-29
- Labels: none

## Description

**Describe the bug**
On early-access-2026-03, going to the "Swarm" page displays some information for a few seconds. The screen then refreshes but all the information is cleared out.

**To Reproduce**
Steps to reproduce the behavior:
1. On a device flashed with early-access-2026-03, go to 'Swarm' page
2. Notice that the name of your first miner is shown, duplicated across all rows of your swarm.
3. Wait approximately 5 seconds.
4. Notice that information is cleared but miner count remains.

**Expected behavior**
When accessing the "Swarm" page, information about each swarm member should display.

**Screenshots & Photos**
When first accessing the Swarm page, some information is shown:

<img width="1128" height="564" alt="Image" src="https://github.com/user-attachments/assets/a354b45d-d3eb-4130-b62c-f74eab933db6" />

After a few seconds, information is cleared, and user sees this:

<img width="1135" height="513" alt="Image" src="https://github.com/user-attachments/assets/f858dccb-7de7-401f-a31c-896ad6b8349a" />

**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma 601
 - Bitaxe HW vendor: Altair Tech
 - ESP-Miner FW version:  early-access-2026-03

## Comments

### thebiggestgit on 2026-03-19

I also had this when upgrading to this release. Fixed by manually removing the devices from the discovered swarm - click the last trash can remove button for each and autodiscover again.  Fine since doing that. 

### Hylinus on 2026-03-19

> I also had this when upgrading to this release. Fixed by manually removing the devices from the discovered swarm - click the last trash can remove button for each and autodiscover again. Fine since doing that.

You're indeed correct. I removed the first entry during the 5 second delay, but had to refresh the screen a couple of times until the "Auto Scan" button did anything. Attempting to add manually would let me type in the address in the text bar, but the "Add" button would not enable.

### WantClue on 2026-05-28

@mutatrum 

### mutatrum on 2026-05-29

This was exactly why the EA was made, to flush out bugs early in a lot of PRs. This was caused by a bug in #1240 which should be fixed there. The EA release is not going to be updated, but I might make a new EA which includes #1240 after 2.14 is released.
