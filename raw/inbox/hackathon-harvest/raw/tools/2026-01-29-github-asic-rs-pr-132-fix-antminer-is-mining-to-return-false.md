# 256foundation/asic-rs pull request #132: Fix antminer is_mining to return false when hashrate is zero

> Source: https://github.com/256foundation/asic-rs/pull/132
> Collected: 2026-10-07
> Published: 2026-01-29

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 132
- State: closed
- Author: glitchpixelz
- Opened: 2026-01-29
- Closed: 2026-02-20
- Labels: none

## Description

Issue: bitmain-work-mode can show normal ("0") even when the miner is overheated and has 0 hashrate, so is_mining ends up true.

Fix: Only report is_mining as true when hashrate is > 0 (when hashrate is available). This keeps the existing work-mode checks and stops the false “mining” state at zero hashrate.

## Comments

### b-rowan on 2026-01-29

I think is_mining is intended to indicate whether the miner SHOULD be mining, not whether or not it truly is.  Might be worth changing the name to mining_enabled or something, but I think representing to the user that this miner is not in sleep mode but just sucks is a different state than having a miner in sleep mode.

Just want to make sure that this aligns with that idea, we can discuss if y'all want to change it.

### glitchpixelz on 2026-01-29

You're right and thought about this at first and totally undermined the idea with the broad definition of the "stopped" work mode value, but in reality this is "not mining = enabled". Yes the intent is to distinguish if the miner is truly mining or not and it does suck two states as we know of now but also a good thing.

So to be correct we would have to implement something like GetMiningEnabled and would look something like
| MiningEnabled | IsMining | Meaning |
|---|---|---|
| false | false | sleeping / stopped |
| true  | false | should mine but not hashing (overheat, failure, pool issue) |
| true  | true  | normal mining |



### b-rowan on 2026-01-29

> So to be correct we would have to implement something like GetMiningEnabled

I don't mind this idea, but then isn't `is_mining` just a calculated value directly from hashrate?  Is there another thing we would want to check when calculating this? If not, I think we should leave that check to the end user inside business logic, no reason for us to add a value for `hashrate == 0`...

### glitchpixelz on 2026-01-29

There are other calculations we could add in like tracking the last accepted share timestamp. I’ve seen cases where the GUI and even the scans looks “frozen,” and the miner appears to be hashing, but in reality the last accepted share was hours ago. It’s a tricky failure mode I caught last summer.

### glitchpixelz on 2026-02-05

Added a MiningMode enum (enabled and disabled) to replace original is_mining and kept ismining as "Whether the miner is currently hashing."
