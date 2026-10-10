# bitaxeorg/ESP-Miner issue #1358: show pool stratum auth error on AxeOS dashboard

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1358
> Collected: 2026-10-07
> Published: 2025-11-16

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1358
- State: open
- Author: skot
- Opened: 2025-11-16
- Closed: n/a
- Labels: none

## Description

If esp-miner fails to authenticate via stratum with the pool, we should propagate this error to the AxeOS dashboard.

example, if I use an invalid mining address with public-pool;

`{"id": 3, "method": "mining.authorize", "params": ["bc1qnp980s5fpp8l94p5cvttntdqy8rvrq74qly2yrfmzkdsntqzlc5qkc4rkq.bitaxe", "x"]}`

it will return;

```
I (15123) stratum_api: rx: {"id":3,"result":null,"error":[20,"Authorization validation error",", bc1qnp980s5fpp8l94p5cvttntdqy8rvrq74qly2yrfmzkdsntqzlc5qkc4rkq"]}
E (15138) stratum_task: setup message rejected: Authorization validation error
```
 
Currently AxeOS does not show the "Authorization validation error" to the user.



## Comments

### mutatrum on 2025-11-16

Which pool does that? Or does it happen if the address in invalid for whatever reason?

### skot on 2025-11-16

> Which pool does that? Or does it happen if the address in invalid for whatever reason?

this happens with public-pool. it's rejecting the mining.authorize because the bitcoin address in the stratum username is not valid (I just changed one letter)

### mutatrum on 2025-11-16

Relevant comment: https://github.com/bitaxeorg/ESP-Miner/pull/1290#issuecomment-3442053373
