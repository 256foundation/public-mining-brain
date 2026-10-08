# bitaxeorg/ESP-Miner issue #842: Spelling error for BM1397

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/842
> Collected: 2026-10-07
> Published: 2025-04-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 842
- State: closed
- Author: adammwest
- Opened: 2025-04-12
- Closed: 2025-04-16
- Labels: accepted

## Description

**Issue**
Spelling error [here](https://github.com/bitaxeorg/ESP-Miner/blob/master/components/asic/include/]bm1397.h#L12)
```c
#define BM1937_SERIALTX_DEBUG true // should be BM1397_SERIALTX_DEBUG 
#define BM1937_SERIALRX_DEBUG false
```

there could be other misspellings



**Solution**
Refactor bm1397.h and bm1397.c
to use `BM1397` instead of `BM1937`

## Comments

### WantClue on 2025-04-16

good catch, fixed
