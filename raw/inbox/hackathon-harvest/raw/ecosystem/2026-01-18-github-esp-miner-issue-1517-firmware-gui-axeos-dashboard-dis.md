# bitaxeorg/ESP-Miner issue #1517: Firmware: GUI (AxeOS -Dashboard) / Display Does Not Update for Subsequent Block Finds in the Same Session

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1517
> Collected: 2026-10-07
> Published: 2026-01-18

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1517
- State: closed
- Author: ghost
- Opened: 2026-01-18
- Closed: 2026-02-24
- Labels: none

## Description

The core mining functionality of the device is robust; the miner continues to operate correctly and submit shares. However, there is a limitation in the firmware's user interface (UI) and the associated "block found routine" related to logging and persistent display of block find events.

The routine only reports the first block found in a session to the end-user via the notification in the GUI (AxeOS Dashboard) and the scrolling message on the display on the device. It fails to update the GUI and the display for the second, third, and any subsequent blocks found within that same continuous mining session. This means users are unaware of multiple successful block finds until they independently verify the information on their mining pool's interface or in their wallet's transaction history.

Expected Behavior
The GUI should update to acknowledge the second block find and any block finds thereafter. Ideally, a counter should increment, and a new notification should appear in the Dashboard reflecting that a new block has been found, this info should also be displayed on the small screen along with its specific difficulty value like with the first block that was found.

Actual Behavior
The block found message in the Dashboard remains frozen on the first event's notification. No counter is present or updated, and no new notification appears for subsequent block finds until the device is rebooted, which resets the session.

Info on the small screen, the block found message that scrolls disappears when a 2nd block is found, no updates or info is shown here with the 2nd block being found or any new blocks thereafter.
_Note: This behavior was reliably reproduced in real-world testing using a low-difficulty SHA-256 network (like DigiByte) to facilitate multiple block finds within a short time frame (the mining session)._

Proposed Solution
The "block found routine" in the firmware needs modification to include a persistent counter and a display refresh command for every successful block find notification for that session, the block found routine should be reset when the device is rebooted which it currently does and thus starting the process all over again for the new session.
Session Reset: The block found counter here is reset to zero (0) and starts all over again with logging blocks found.

## Comments

### Painerman on 2026-02-01

I already wrote about this
[https://github.com/bitaxeorg/ESP-Miner/issues/1455#event-21625944823](url)
However, a boor named WantClue closed the application with the note - WantClue closed this as completed on Dec 17, 2025.
I also closed the request to disable snow, which also interferes with the operation of the device marked "not planned."

Some people value special effects over the user's well-being!

### WantClue on 2026-02-24

> I already wrote about this [https://github.com/bitaxeorg/ESP-Miner/issues/1455#event-21625944823](url) However, a boor named WantClue closed the application with the note - WantClue closed this as completed on Dec 17, 2025. I also closed the request to disable snow, which also interferes with the operation of the device marked "not planned."
> 
> Some people value special effects over the user's well-being!

This issue has been resolved and we do not take any shitcoin into consideration. 

### Painerman on 2026-02-25

Wantclue, the main thing is not to overdo it with glue. So you can do nothing and remain with your shameful decisions in full view of everyone! I wish you great shame with this approach! Write "Hello world!" instead of the AxeOS logo, for example! =))
Shitcoin probably isn't a bad idea; you'll be popular with gays! Just ask your mom for permission. I'll give you an idea to develop the topic - assholepool for mining your shitcoins.
