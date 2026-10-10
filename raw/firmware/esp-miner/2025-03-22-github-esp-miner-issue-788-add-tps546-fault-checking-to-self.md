# bitaxeorg/ESP-Miner issue #788: add TPS546 fault checking to selftest

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/788
> Collected: 2026-10-07
> Published: 2025-03-22

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 788
- State: closed
- Author: skot
- Opened: 2025-03-22
- Closed: 2025-03-24
- Labels: documentation, enhancement, help wanted, good first issue, design

## Description

I think it would be useful to check and report the status of all the TPS546 faults and warnings during the selftest.

## Comments

### skot on 2025-03-22

this can be as simple as calling VCORE_check_fault() somewhere in selftest and printing the result to the log. Just gotta figure out where in the selftest is the most useful.

### JasonB1833 on 2025-03-22

I threw VCORE_check_fault() just after the voltage regulator testing as I figured these two should be close together since they are related to voltage regulation anyways, not sure if this exactly what you're looking for but I'm open to suggestions, this just seemed like the quickest answer

![Image](https://github.com/user-attachments/assets/349a5f57-9f05-4272-93d0-6f7de7907886)

### skot on 2025-03-22

> I threw VCORE_check_fault() just after the voltage regulator testing as I figured these two should be close together since they are related to voltage regulation anyways, not sure if this exactly what you're looking for but I'm open to suggestions, this just seemed like the quickest answer


I didn't know you were working on this.. I just made PR #789. Turns out that VCORE_check_fault() only fails if there is a I2C error with the TPS546. I had to also look at GLOBAL_STATE->SYSTEM_MODULE.power_fault for the test result.


### JasonB1833 on 2025-03-22

@skot all good, I didn't announce my presence because I had fairly limited time and wasn't sure if I could get it done in a timely manner. regardless it gave me more time to delve into the codebase which can only help.


### skot on 2025-03-24

fixed via #789
