# bitaxeorg/ESP-Miner issue #1703: AxeOS UI mistakenly warns against partial donation to Sv2 Reference Implementation

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1703
> Collected: 2026-10-07
> Published: 2026-05-21

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1703
- State: open
- Author: plebhash
- Opened: 2026-05-21
- Closed: n/a
- Labels: none

## Description

## intro

Sv2 Reference Implementation (SRI) Pool allows solo mining with a partial donation to the SRI community wallet by setting a specific string pattern Sv2 channel `user_identity`, as documented [here](https://github.com/stratum-mining/sv2-apps/tree/main/pool-apps/pool#solo-mining-mode).

for example, I'm setting my bitaxe for 25% donation:

<img width="1341" height="601" alt="Image" src="https://github.com/user-attachments/assets/9176b56c-a55a-4253-95f0-8240dbe6519a" />

with the configuration above, there's going to be 2 different outputs in the coinbase tx:
- one output with 25% of block rewards going to SRI community wallet address
- one output with 75% of block rewards going to my address

## problem

after configuring my bitaxe as shown above, the main AxeOS UI Dashboard displays:

<img width="1383" height="220" alt="Image" src="https://github.com/user-attachments/assets/b1750c11-a9a8-4230-9368-cf9d3490be1e" />

which isn't true, and is arguably misleading, because it induces the user to think that there's something shady going on.

since I had direct participation in SRI Pool development, and I'm operating the deployment on `stratum2+tcp://75.119.150.111:3333/9auqWEzQDVyd2oe1JVGFLMLHZtCo2FFqZwtKA5gd9xbuEu7PH72`, I know for a fact that there's no scam.

this happens deterministically when I choose a Sv2 Extended Channel (for which AxeOS can decode the coinbase tx outputs and audit the rewards).

if I choose a Sv2 Standard Channel (impossible to decode the coinbase tx outputs), I saw the warning 1x but after switching to Extended Channel I could no longer reproduce it deterministically.

## suggestion

IMO, better warning signs would be:
- for Sv2 Extended Channel (**after decoding and auditing the coinbase tx outputs**):
  - no warning at all; or
  - `⚠️ You only have a partial share in the mining reward`; or
  - some variation of the warning above
- for Sv2 Standard Channel:
  - no warning at all; or
  - `⚠️ Impossible to verify whether you have a share in the mining reward in a Sv2 Standard Channel`; or
  - some variation of the warning above

the current `⚠️ You don't have a share in the mining reward` should only be displayed in case the coinbase tx outputs of a Sv2 Extended Channel are decoded and it's verified that there's 0 BTC going to the user's address (or the reward share is different than the expected)

## tested hardware

this test was conducted with a Bitaxe 401 and a 601, both running `esp-miner.bin` + `www.bin` from [`v2.14.0b3`](https://github.com/bitaxeorg/ESP-Miner/releases/tag/v2.14.0b3)

---

cc @warioishere @gitgab19 @pavlenex

## Comments

### warioishere on 2026-05-21

https://github.com/bitaxeorg/ESP-Miner/pull/1678

i already create a PR to disable the warning for pools that have different payout methods, can be changed if needed, I haven't tested SRI reference pool yet with those strings
