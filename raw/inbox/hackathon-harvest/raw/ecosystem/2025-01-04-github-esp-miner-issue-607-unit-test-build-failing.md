# bitaxeorg/ESP-Miner issue #607: unit test build failing

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/607
> Collected: 2026-10-07
> Published: 2025-01-04

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 607
- State: closed
- Author: tdb3
- Opened: 2025-01-04
- Closed: 2025-01-27
- Labels: none

## Description

**Describe the bug**
Compilation issues when building for unit tests, starting with commit 61042d93ae0b0e54c4a0020dd87b2803f6fd369d

**To Reproduce**
```
cd ESP-Miner
git checkout master
git checkout 61042d93ae0b0e54c4a0020dd87b2803f6fd369d
cd test
idf.py build
```

**Expected behavior**
Unit test build is successful.

**Log**
```
idf.py build
...
/home/dev/myrepos/ESP-MinerAlt/ESP-Miner/components/asic/bm1368.c: In function '_reset':
/home/dev/myrepos/ESP-MinerAlt/ESP-Miner/components/asic/bm1368.c:18:25: error: 'CONFIG_GPIO_ASIC_RESET' undeclared (first use in this function); did you mean 'GPIO_ASIC_RESET'?
   18 | #define GPIO_ASIC_RESET CONFIG_GPIO_ASIC_RESET
      |                         ^~~~~~~~~~~~~~~~~~~~~~
/home/dev/myrepos/ESP-MinerAlt/ESP-Miner/components/asic/bm1368.c:125:20: note: in expansion of macro 'GPIO_ASIC_RESET'
  125 |     gpio_set_level(GPIO_ASIC_RESET, 0);
      |                    ^~~~~~~~~~~~~~~
/home/dev/myrepos/ESP-MinerAlt/ESP-Miner/components/asic/bm1368.c:18:25: note: each undeclared identifier is reported only once for each function it appears in
   18 | #define GPIO_ASIC_RESET CONFIG_GPIO_ASIC_RESET
      |                         ^~~~~~~~~~~~~~~~~~~~~~
/home/dev/myrepos/ESP-MinerAlt/ESP-Miner/components/asic/bm1368.c:125:20: note: in expansion of macro 'GPIO_ASIC_RESET'
  125 |     gpio_set_level(GPIO_ASIC_RESET, 0);
      |                    ^~~~~~~~~~~~~~~
/home/dev/myrepos/ESP-MinerAlt/ESP-Miner/components/asic/bm1368.c: In function 'BM1368_init':
/home/dev/myrepos/ESP-MinerAlt/ESP-Miner/components/asic/bm1368.c:18:25: error: 'CONFIG_GPIO_ASIC_RESET' undeclared (first use in this function); did you mean 'GPIO_ASIC_RESET'?
   18 | #define GPIO_ASIC_RESET CONFIG_GPIO_ASIC_RESET
      |                         ^~~~~~~~~~~~~~~~~~~~~~
/home/dev/myrepos/ESP-MinerAlt/ESP-Miner/components/asic/bm1368.c:246:34: note: in expansion of macro 'GPIO_ASIC_RESET'
  246 |     esp_rom_gpio_pad_select_gpio(GPIO_ASIC_RESET);
      |                                  ^~~~~~~~~~~~~~~
ninja: build stopped: subcommand failed.
...
```

**Additional context**
Building on the previous commit (f454b0c41bd51c7e08864a255404d57b5d2516ab) seems ok.
https://github.com/skot/ESP-Miner/blob/master/doc/unit_testing.md


## Comments

### eandersson on 2025-01-10

When you have some time can you take a look at this PR? https://github.com/skot/ESP-Miner/pull/634

### tdb3 on 2025-01-11

> When you have some time can you take a look at this PR? #634

Thanks. Took a look at it. Great work!
I checked out head of the #634 branch (4a07ee4c8baafed880f30238750be5eb01aec2fc), and unit test building was successful. Will close the Issue once #634 is merged.
