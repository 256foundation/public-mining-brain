# bitaxeorg/ESP-Miner issue #245: BM1397_init function signature is incorrect

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/245
> Collected: 2026-10-07
> Published: 2024-07-02

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 245
- State: closed
- Author: 3x3y3z3t
- Opened: 2024-07-02
- Closed: 2024-07-02
- Labels: none

## Description

**Describe the bug**
Function `void BM1397_init(uint64_t, uint16_t)` signature is incompatible with the function pointer `.init_fn` in `AsicFunctions`.

**To Reproduce**
Steps to reproduce the behavior:
1. Go to './components/bm1397/bm1397.c', scroll down to line 286 to check the function's signature.
2. Go to './main/global_states.h', scroll down to line 39 to check the function pointer's signature.
3. See the signature mismatch (return type).

**Expected behavior**
Function pointer expect a `uint8_t fn(uint64_t, uint16_t)`. 
`BM1397_init` should return `uint8_t` instead of `void`.

**Additional context**
This issue emit a warning when compiling main.c (as C), but becomes an error when compiling main.cpp (as C++). I am not sure if this affect any Bitaxe out there with BM1397, but we need to fix the error in order to prepare for C++ support implementation.
