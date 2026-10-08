# 256foundation/asic-rs issue #191: MinerFactory drops otherwise identifiable miners when model parsing fails

> Source: https://github.com/256foundation/asic-rs/issues/191
> Collected: 2026-10-07
> Published: 2026-03-19

- Repository: 256foundation/asic-rs
- Type: issue
- Number: 191
- State: closed
- Author: egesayinEB
- Opened: 2026-03-19
- Closed: 2026-03-20
- Labels: none

## Description

Hi, I think there is a discovery bug in `MinerFactory`.

From the README/docs, my understanding is that `MinerFactory` should discover miners on the network, figure out the right backend, and return a usable miner object.

Right now it looks like discovery can get far enough to know what kind of miner it is, but still drop it completely if the exact model string is not in the current model aliases.

I hit this with a stock AntMiner control board with model  `BHB42XXX`.

What I get from the miner:

- `GET /` returns `401 Unauthorized` with `WWW-Authenticate: Digest realm="antMiner Configuration"`
- `GET /cgi-bin/get_system_info.cgi` returns:
  - `minertype: "Antminer BHB42XXX"`
- `GET /cgi-bin/miner_type.cgi` returns:
  - `subtype: "AMLCtrl_BHB42XXX"`

So this miner is:

- reachable
- stock AntMiner
- speaking the expected stock web API
- probably Amlogic-based from the `subtype`

But it still gets dropped from discovery.

From reading the code, it looks like this is what happens:

1. `parse_type_from_web()` identifies it as stock AntMiner
2. `get_miner()` then calls `make.get_model(ip)` before selecting a backend
3. `get_model_antminer()` reads `minertype` and tries to parse `"Antminer BHB42XXX"` as `AntMinerModel`
4. that string is not covered by the current model aliases
5. model parsing fails, and the miner disappears from discovery

I think it should instead have unknown model type and still return the miner instead of dropping it. 

Proposed  behavior:
- if make/firmware detection succeeds, but the exact model string is unknown, the miner should still be returned
- the model could be `MinerModel::Unknown(raw_model_string)`
- backend selection for stock miners should still work when the make is known, even if the model is unknown

Also I found out that ePIC already handle this better, because it can fall back to `MinerModel::Unknown(...)` instead of failing outright. Non-ePIC paths do not seem to do that consistently. I think it would be better if other makes could handle it in a similar way. 

Please correct me if I am missing something or let me know if you have any questions about the issue

## Comments

### b-rowan on 2026-03-19

Yeah this is something we should fix.  What is the real model of that machine being identified as BHB42XXX?

### egesayinEB on 2026-03-19

> Yeah this is something we should fix. What is the real model of that machine being identified as BHB42XXX?

I am not exactly sure, it is an amlogic bitmain board with no hashboards connected, Antminer BHB42XXX is the only thing shown on dashboard or I could get from api calls. 

### b-rowan on 2026-03-19

Ahh, good to know.   I'll fix this then, and make sure it isn't linked to any specific miner.

### b-rowan on 2026-03-19

Try that branch out if possible, it should be fixed there, but I can't test it since I don't have a (modern) antminer CB.

### egesayinEB on 2026-03-20

> Try that branch out if possible, it should be fixed there, but I can't test it since I don't have a (modern) antminer CB.

Thank you for the quick fix, just tested and it works
