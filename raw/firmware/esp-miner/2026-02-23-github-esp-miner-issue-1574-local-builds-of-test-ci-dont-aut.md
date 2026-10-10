# bitaxeorg/ESP-Miner issue #1574: Local builds of test-ci dont automatically add common.h/c as they are not unique

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1574
> Collected: 2026-10-07
> Published: 2026-02-23

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1574
- State: closed
- Author: adammwest
- Opened: 2026-02-23
- Closed: 2026-02-27
- Labels: bug

## Description

**Issue**
V2.13.0 commit 515666254809da56ec77092023ed6f6415d9d6e2
When building test-ci
and importing common.h/c to a unit test, common.c/h are not correctly linked due to auto discovery failing to add the correct paths

**Reproduce**
create a unit test in /components/asic/test/test_something.c
add include "common.h" to the file
`cd test-ci`
`idf.py build`
the linker will fail

**Fix**
change all references/guards from 
* common.h -> asic_common.h 
* common.c -> asic_common.c
* __COMMON_H -> _ASIC_COMMON_H
