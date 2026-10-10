# bitaxeorg/ESP-Miner issue #570: Add quick link template settings field

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/570
> Collected: 2026-10-07
> Published: 2024-12-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 570
- State: open
- Author: robwoodgate
- Opened: 2024-12-10
- Closed: n/a
- Labels: good first issue, design

## Description

I just submitted [a PR](https://github.com/skot/ESP-Miner/pull/569) to include solohash as a quicklink... it made me think it might be a good idea to have a settings field for primary/fallback pools to allow users to set their own pool stats quick link without needing to wait for it to be added via PR.

It will also prevent the getQuickLink() method getting out of hand over time.

eg: 
<img width="509" alt="example-pool-stats-template-field" src="https://github.com/user-attachments/assets/79a16206-e4c6-471a-9c06-c217b71bbf89">



## Comments

### WantClue on 2024-12-11

I like this idea, and we should implement something like that the only issue is, that probably every pool does have a different endpoint 😢
