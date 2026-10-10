# bitaxeorg/ESP-Miner issue #765: Add reject reason tooltips

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/765
> Collected: 2026-10-07
> Published: 2025-03-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 765
- State: closed
- Author: mutatrum
- Opened: 2025-03-12
- Closed: 2025-04-22
- Labels: documentation, enhancement, design

## Description

Now the reject reasons are visible in AxeOS, it would be nice to a tooltip explaining them. People ask questions about them on a regular basis, and having a bit more information would be a nice educational tool.

Taken from [ckpool](https://bitbucket.org/ckolivas/ckpool/src/bb7b0aebe08ed99d45b8701af2d65bfcdbef0932/src/libckpool.h?at=master#lines-285):
```
Invalid nonce2 length
Worker mismatch
No nonce
No ntime
No nonce2
No job_id
No username
Invalid array size
Params not array
Valid
Invalid JobID
Stale
Ntime out of range
Duplicate
Above target
Invalid version mask
```

The most common ones are `Above target` and `Stale`. All the other ones are probably fatal errors.

From [public-pool](https://github.com/benjamin-wilson/public-pool/blob/fda3f21b7189f95e40cafb24967202d973362711/src/models/StratumV1Client.ts#L476):

```
Subscription validation error
Configuration validation error
Authorization validation error
Suggest difficulty validation error
Mining Submit validation error
Job not found
Duplicate share
Difficulty too low
```

Here `Job not found` (aka stale) and `Difficulty too low` are the most common ones.

Any other mining pool software we need to consider? As with the preceding issues here, this is all a 'best effort' attempt, as these things can change outside of our control. However, with some limited effort it could benefit quite a bit.
