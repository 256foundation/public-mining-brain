# 256foundation/asic-rs pull request #6: feature: BTMiner V3 RPC + Backend

> Source: https://github.com/256foundation/asic-rs/pull/6
> Collected: 2026-10-07
> Published: 2025-04-29

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 6
- State: closed
- Author: b-rowan
- Opened: 2025-04-29
- Closed: 2025-05-30
- Labels: none

## Description

Add support for BTMiner V3 RPC API and a basic backend framework.

Draft for review to ACK data parsing concept.  See `miners/backends/btminer.rs`.

## Comments

### b-rowan on 2025-05-01

Ready for full review and testing.  This only implements stuff for V3 API (> 2025), but will work on V2 eventually.  V2 requires checking the miner version as part of identification, so that's a PITA.  @s0kil offered to test, so adding for additional review.

### b-rowan on 2025-05-01

The more I think about this, the more I feel this solution is a bit hacky, and isn't composed very well.  It seems like trying to get too far into the type system with the deserialization to an intermediate type just ends up coupling that data together way too tightly.

I feel like going back to a way similar to how pyasic was architected may be better for data gathering, EG `GetMac` trait which implements 2 methods, `get_mac` and `parse_mac`.  The get method would handle API calls, then call the parse method with the required data.  This helps decouple random data, allows for better testing, and also adds the ability to require specific traits as a prerequisite for other functions at a later date (maybe `Box<impl GetMac>` or similar).

Not sure of what others have for thoughts on this?  Might make a separate branch to try to implement that.
