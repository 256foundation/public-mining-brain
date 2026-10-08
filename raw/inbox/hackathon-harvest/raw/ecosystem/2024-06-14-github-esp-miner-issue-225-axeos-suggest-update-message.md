# bitaxeorg/ESP-Miner issue #225: AxeOS suggest update message

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/225
> Collected: 2026-10-07
> Published: 2024-06-14

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 225
- State: closed
- Author: WantClue
- Opened: 2024-06-14
- Closed: 2024-06-21
- Labels: enhancement

## Description

I suggest to add to the settings page a note: Update available consider updating

If current version < release tag

## Comments

### mutatrum on 2024-06-20

I think you said on live stream: if it's hashing, don't upgrade. And considering the flack Braiins got with their phone home stuff, maybe even put the current release check behind a button. Don't call out unsolicited for anything.

### skot on 2024-06-20

in this case it's the UI calling GitHub from whatever machine has loaded AxeOS.. and it will totally still mine if that hardcoded URL doesn't respond.

But yes, we do need to be careful here. I like the button to manually check idea. @benjamin-wilson what do you think?

### benjamin-wilson on 2024-06-21

https://github.com/skot/ESP-Miner/commit/9140d0911119ed8df6dd0e365b69c63432baf755

Added a button
