# bitaxeorg/ESP-Miner issue #816: extranonce_2 It is not clear how the value increase is implemented in the code.

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/816
> Collected: 2026-10-07
> Published: 2025-04-01

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 816
- State: closed
- Author: vaavdeev
- Opened: 2025-04-01
- Closed: 2025-04-07
- Labels: none

## Description

the ESP-Miner code iterates over all nonce values.
Stratum server transmits the length of extranonce_2.
It is not clear where in the code the work with increasing the value of extranonce_2 is implemented.


## Comments

### KillerInk on 2025-04-01

https://github.com/bitaxeorg/ESP-Miner/blob/d3486df71823c6b8e7163db9893760a64b8eeca8/main/tasks/stratum_task.c#L333-L335

https://github.com/bitaxeorg/ESP-Miner/blob/d3486df71823c6b8e7163db9893760a64b8eeca8/main/tasks/create_jobs_task.c#L75-L81

https://github.com/bitaxeorg/ESP-Miner/blob/d3486df71823c6b8e7163db9893760a64b8eeca8/components/stratum/mining.c#L113-L124

so you get the length only once when the client subscribe and a new session is open

### vaavdeev on 2025-04-01

I think I found this place in the create_jobs_task file.

.....
generate_work(GLOBAL_STATE, mining_notification, extranonce_2);

                // Increase extranonce_2 for the next job.
                extranonce_2++;
....
