# bitaxeorg/ESP-Miner issue #507: xQueueReceive() in SYSTEM_task() appears to be blocking waiting for button presses

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/507
> Collected: 2026-10-07
> Published: 2024-11-22

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 507
- State: closed
- Author: skot
- Opened: 2024-11-22
- Closed: 2024-11-22
- Labels: bug

## Description

OSMU Discord member Benc98 noticed the third parameter to xQueueReceive(), `wait_time` appears to be blocking. 
We probably don't want this task blocking.
https://github.com/skot/ESP-Miner/blob/29a543da76ba5fd19e07f43da87214613d67455a/main/system.c#L251-L274

## Comments

### skot on 2024-11-22

duplicate of #506
