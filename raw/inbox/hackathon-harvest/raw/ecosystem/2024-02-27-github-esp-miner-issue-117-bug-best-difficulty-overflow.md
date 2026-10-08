# bitaxeorg/ESP-Miner issue #117: [BUG] Best Difficulty Overflow

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/117
> Collected: 2026-10-07
> Published: 2024-02-27

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 117
- State: closed
- Author: weixiongmei
- Opened: 2024-02-27
- Closed: 2024-04-05
- Labels: bug, help wanted

## Description

/Volumes/SSD/Codes/ESP/ESP-Miner/components/bm1397/include/bm1397.h:14:38: warning: overflow in conversion from 'long long int' to 'int' changes value from '4294967296' to '0' [-Woverflow] 14 | static const u_int64_t NONCE_SPACE = 4294967296;

## Comments

### benjamin-wilson on 2024-03-15

Can you add more context here, this seems to be an error about NONCE_SPACE not Best Difficulty. It's also a const so not sure how you're getting this issue.

### weixiongmei on 2024-03-15

@benjamin-wilson I think it's a compiler issue, the variable that stores the best difficulty is overflow, I compiled the firmware myself and testing to prove what's the problem yet, but since then, I haven't got the BD higher than 4.29G yet..

### skot on 2024-04-05

this has been fixed in #155
