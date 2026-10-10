# bitaxeorg/ESP-Miner issue #273: mining.subscribe submits characters that it shouldn't in 2.1.9

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/273
> Collected: 2026-10-07
> Published: 2024-08-07

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 273
- State: closed
- Author: Ondalf
- Opened: 2024-08-07
- Closed: 2024-08-08
- Labels: enhancement

## Description

**Describe the bug**
mining.subscribe method sends extra characters (space and () ) on connect.
Should be rather strictly non-spaced and no extra character string, since pools does wipe those off as trash and/or attempt for sql/js/html inject.
Current format is
```
[\"bitaxe/%s (%s)\"]
```
in https://github.com/skot/ESP-Miner/blob/master/components/stratum/stratum_api.c#L309-L320
I suggest changing it to
```
[\"bitaxe/%s-%s\"]
```
or
```
[\"bitaxe/%s/%s\"]
```

**To Reproduce**
Connect miner with this feature present into pool with strict cleanup rules for strings before pushing them to DB. Read: all yiimp based ones. The stratums will NOT read it, nor store it as it contains unallowed characters.

**Expected behavior**
Keep submitted strings consistent.

**Screenshots & Photos**
N/A

**Hardware (please complete the following information):**
Any.

**Additional context**
N/A
