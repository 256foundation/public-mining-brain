# bitaxeorg/ESP-Miner issue #1543: 800xxx support for lastest firmware

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1543
> Collected: 2026-10-07
> Published: 2026-02-06

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1543
- State: closed
- Author: dorothymesservey78-hue
- Opened: 2026-02-06
- Closed: 2026-02-07
- Labels: none

## Description

.


## Comments

### mutatrum on 2026-02-07

The 800 is not supported. See https://github.com/bitaxeorg/ESP-Miner/issues/1521#issuecomment-3787400158

### mutatrum on 2026-02-07

800 is not supported in the official firmware. The problem is there have been several prototype iterations. Unfortunately, many people started selling these prototype iterations and expecting the firmware maintainers to support these. This is  impossible, all these prototypes are all called 800 and the firmware can't see what is actually on the board and we don't know what actually has been manufactured. The hardware and firmware for the 801 is different so it might or might not work with newer versions.

You have a few options:
 * Return the device and ask for money back or replacement for a 801;
 * Revert to the firmware which was supplied with the device;
 * Ask the manufacturer to update the firmware for this specific 800 prototype. They know what they built.
