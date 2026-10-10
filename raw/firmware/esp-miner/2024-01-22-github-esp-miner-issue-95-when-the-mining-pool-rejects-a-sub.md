# bitaxeorg/ESP-Miner issue #95: When the mining pool rejects a submission, the rejected shares are not correctly incremented.

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/95
> Collected: 2026-10-07
> Published: 2024-01-22

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 95
- State: closed
- Author: AxisRay
- Opened: 2024-01-22
- Closed: 2024-02-25
- Labels: bug

## Description

As shown in the picture, my submission was rejected by the pool.
![image](https://github.com/skot/ESP-Miner/assets/6546326/8da004b7-c968-4ff6-ade9-0df12f7ae0b5)
However, the `result` field in the returned JSON data is `null`.
https://github.com/skot/ESP-Miner/blob/23599cf46f3668af58d252915b347fa14eedd8cf/components/stratum/stratum_api.c#L123-L141
So, in the above code, the result of `if (result_json != NULL && cJSON_IsBool(result_json)) {` is false
Because `null` is not vaild bool value.
Therefore, message->response_success is not being assigned correctly.


## Comments

### skot on 2024-02-16

Ah, good catch. this would be nice to get fixed so we can see how many shares are _actually_ rejected

### benjamin-wilson on 2024-02-25

Fixed https://github.com/skot/ESP-Miner/commit/feda6609c10b1c37b14fa4f7366f16e4949c30a0
