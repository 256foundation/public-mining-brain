# bitaxeorg/ESP-Miner issue #1993: Bug: Failed to parse SRI donation string

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1993
> Collected: 2026-10-07
> Published: 2026-09-23

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1993
- State: open
- Author: johnnyasantoss
- Opened: 2026-09-23
- Closed: n/a
- Labels: bug, enhancement

## Description

**Describe the bug**
When using a SRI defined donation username string[^sri-donation] dashboard doesn't detect address in coinbase.

**To Reproduce**
Steps to reproduce the behavior:
1. Define username as such `sri/donate/<prct>/<addr>[/<worker>]` or `sri/<addr>[/<worker>]`
2. Connect to a SV2 pool running SRI
3. Go to dashboard
4. See error

**Expected behavior**
ESP miner to split this string pattern too and show the correct info on dashboard

**Screenshots & Photos**
If applicable, add AxeOS screenshots and/or photos of your Bitaxe to help explain your problem.

<img width="374" height="77" alt="Image" src="https://github.com/user-attachments/assets/173f647c-4868-4fb9-b049-c4e757e3ba8a" />

**Hardware (please complete the following information):**
 - Bitaxe HW version: 601
 - Bitaxe HW vendor: SoloSatoshi
 - ESP-Miner FW version: 2.14.1
 - Hash Frequency: 1TH/s
 - Voltage: In 5.1V / asic 1.09V
 - Pool URL, Port, User: `75.119.150.111:3333`

[^sri-donation]: See https://github.com/stratum-mining/sv2-apps/tree/main/pool-apps/pool#user-identity-patterns => `sri/donate/<prct>/<addr>[/<worker>]`

## Comments

### plebhash on 2026-09-23

hi, SRi maintainer here

as some of you might know, SRI maintains a "solo pool" at `stratum2+tcp://75.119.150.111:3333/9auqWEzQDVyd2oe1JVGFLMLHZtCo2FFqZwtKA5gd9xbuEu7PH72`

(tbh I hate that we call this a "Pool"... in Sv2 lingo this is a "Mining Protocol Server", or a "Mining Server"... but that's another discussion 🤓 so I'll stick with terminology everyone is familiar with)

---

a few months ago, I proposed [a Github Discussion](https://github.com/stratum-mining/sv2-apps/discussions/288) around the idea of leveraging the Sv2 `user_identity` field to build a little DSL syntax to enable hybrid donation/solo mining, where the miner can choose to donate a percentage of the coinbase tx revenue to SRI community wallet.

this has been implemented and is deployed on SRI community solo pool (and it's baked into the main UX flow of [`sv2-ui` on Umbrel](https://apps.umbrel.com/app/sv2-ui).

so I agree with what @johnnyasantoss is reporting here. The UI is misleading the user to believe they're not getting properly paid, while that's not (entirely) true. I did not inspect the code, but I would assume that its doing some kind of naive verification on coinbase tx outputs, which misses the fact that the solo mining payout output does exist, it's simply not 100% of the template revenue.

this functionality is not exclusive to donations to SRI community wallet. any solo pool operator can set their own. ideally AxeOS should continue auditing coinbase outputs, but with refined logic that avoids mis-labeling.

the specific deployment on `75.119.150.111` is maintained by [Stratum V2 Reference Implementation (SRI)](https://stratumprotocol.org/) community.

donations on this specific deployment go to SRI community wallet, which is formed by individual contributors funded with grants by agencies like Spiral, OpenSats, Vinteum, Btrust, HRF, and others. speaking for my self, I've been funded to work full-time FOSS on SRI since 2024. I started my journey as a plebminer, and as my username tries to convey, pleb mining will always be part of my philosophy (even if most of my time nowadays ends up channeled for "big mining" stuff).

2026 has been pivotal for us, as adoption is increasing and we witness marvelous things like Sv2 as a first class citizen on AxeOS. We would love to continue engaging with AxeOS community to make sure it is 100% Sv2 spec compliant.

---

TLDR: It would be great if AxeOS UI were able to help the solo mining user understand that there's a in-band mechanism for them to choose how much they want to donate to the solo pool operator.

not necessarily advertising for donations to SRI community wallet, but supporting this donation syntax in general

### kragent66-glitch on 2026-09-24

Hi, I'd like to pick this up and implement the refined coinbase output auditing logic to correctly handle the Stratum V2 user_identity field for hybrid donation/solo mining.

### 0xf0xx0 on 2026-09-24

yeah, axeOS assumes the sv1 `address.worker` convention and searches for an exact match in the txouts (https://github.com/bitaxeorg/ESP-Miner/blob/master/main/http_server/axe-os/src/app/components/home/home.component.html#L561). Is this something that'll be defined in the spec?

### plebhash on 2026-09-24

> Is this something that'll be defined in the spec?

not in the near future.

currently this is merely a convention within SRI (which motivates the `sri/` prefix)

if this ever gets formalized into `sv2-spec`, the right approach would be extensions

the DSL on `user_identity` strings tries to KISS, because I'm not sure the Sv2 solo mining ecosystem is mature enough to deserve a protocol extension yet

---

with that said, this is just a creative (yet perfectly valid) usage of base Sv2 Mining Protocol

the core issue here is that this warning misleads the user into believing that there's something wrong with their solo mining rewards, despite the fact that they're willingly opting into a donation scheme

### 0xf0xx0 on 2026-09-24

seems interestin, might adopt it for pogolo x3 

ill whip up a pr to fix this uwu
