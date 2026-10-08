# 256foundation/hydrapool issue #27: pplns_ttl_days

> Source: https://github.com/256foundation/hydrapool/issues/27
> Collected: 2026-10-07
> Published: 2025-10-30

- Repository: 256foundation/hydrapool
- Type: issue
- Number: 27
- State: closed
- Author: LocoSlug
- Opened: 2025-10-30
- Closed: 2025-12-10
- Labels: none

## Description

In a hashrate heating pool for family and friends, can Hydra-Pool handle pplns_ttl_days = >365 without melting down? 

Some miners are only running in the winter and if we hit the lottery in the summer I would still want them to be compensated for past work.

Thanks!

## Comments

### pool2win on 2025-11-01

That will work for a small number of users, say a 100 users. For example with a 100 users you need 90-100 GB of disk space to store a year's worth of shares.

I took this chance and here's some calculations on how I arrived at that number: https://github.com/256foundation/hydrapool/wiki/Storage-Requirements

Note, the number here is for users, not workers. Ideally your friends will use the same btcaddress in all their miner configurations.
