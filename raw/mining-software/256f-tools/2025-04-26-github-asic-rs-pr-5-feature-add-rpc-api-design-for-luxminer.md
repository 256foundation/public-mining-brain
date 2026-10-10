# 256foundation/asic-rs pull request #5: feature: add RPC API design for LUXMiner

> Source: https://github.com/256foundation/asic-rs/pull/5
> Collected: 2026-10-07
> Published: 2025-04-26

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 5
- State: closed
- Author: b-rowan
- Opened: 2025-04-26
- Closed: 2025-04-28
- Labels: none

## Description

Attempt a setup for an RPC API (for LUXMiner since that's what I have access to right now).  Couple caveats here  with the way this is being done, to try to add some flexibility in the future:

- The `SendRPCCommand` trait expects a type `T` which in the general case will be `serde_json::Value`, which can be a bit annoying, but the goal with this is that ideally the user should not use this function, and instead internally we can optimize memory usage by parsing the raw socket response directly into a type that contains all the data we want, then discarding the rest of the response.  We would implement a type `LUXMinerDevdetailsData` which would parse only the important data, which could then be put into `MinerData`.  This also solves the same problem as the dynamic `_get_data` function in pyasic in that it will ensure that each unique command is only ever sent 1 time.
- `send_rpc_command` does not take a `MinerCommand` (yet), as I think that type will need to be extended with parameters.  Not sure how best to handle this, so leaving this starting implementation as basic as possible to review the underlying idea.

## Comments

### jpcomps on 2025-04-28

I'm good with the concept. Might be a way to make it fully generic and take in two types (Protocol, MinerType). Will have a think on that but this seems like the right way to go. Apologies for the delay on some of this arch work. Gonna also tag @cfilipescu for some advice. Hopefully in the next couple weeks we will get a chance to dedicate some time to this
