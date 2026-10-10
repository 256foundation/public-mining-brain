# 256foundation/hydrapool issue #37: Use rust *_sv2 crates?

> Source: https://github.com/256foundation/hydrapool/issues/37
> Collected: 2026-10-07
> Published: 2025-12-10

- Repository: 256foundation/hydrapool
- Type: issue
- Number: 37
- State: closed
- Author: notmandatory
- Opened: 2025-12-10
- Closed: 2025-12-10
- Labels: none

## Description

Have you guys considered leveraging the crates in https://github.com/stratum-mining/stratum? They are also rust and should be high quality. Could be helpful for some of the lower level protocol stuff. 

@econoalchemist this the the project I mentioned at NashBitDevs. 

## Comments

### pool2win on 2025-12-10

Hi @notmandatory . We did consider the SRI crates. We found they did a lot more than we needed. But more importantly the SRI code base had a lot of technical debt that the SRI developers are aware of this. We didn't want to inherit that debt really.

I tried to make some PRs but found my hands were tied behind my backs because the interfaces between the various SRI components were tightly coupled - as in changing one required changing a lot of other components as they had tight API dependencies and update release versions etc. It sounded painfully slow to change things as they already had commitments from downstream consumers who were experimenting with SRI and production usage.

We do want to support sv2 devices once they become more generally available. We will most likely focus on the encrypted/compressed channels first.

### notmandatory on 2025-12-10

Makes sense, good to know you already evaluated them. Hopefully they'll mature and be more useful as sv2 devices become more common.
