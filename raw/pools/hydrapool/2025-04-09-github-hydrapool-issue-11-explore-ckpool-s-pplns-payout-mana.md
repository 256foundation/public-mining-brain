# 256foundation/hydrapool issue #11: Explore ckpool's PPLNS payout management

> Source: https://github.com/256foundation/hydrapool/issues/11
> Collected: 2026-10-07
> Published: 2025-04-09

- Repository: 256foundation/hydrapool
- Type: issue
- Number: 11
- State: closed
- Author: pool2win
- Opened: 2025-04-09
- Closed: 2025-10-29
- Labels: none

## Description

I expect the payout goes to a pool address and the splitting of rewards happens later.

We will need to send a coinbase from the rust node to ckpool, which should then use this coinbase. This will be an interesting piece of work.

## Comments

### pool2win on 2025-10-29

Replaced by p2pool lib's payout mechanism.
