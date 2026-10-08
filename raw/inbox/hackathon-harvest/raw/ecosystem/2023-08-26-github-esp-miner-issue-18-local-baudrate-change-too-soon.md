# bitaxeorg/ESP-Miner issue #18: local baudrate change too soon

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/18
> Collected: 2026-10-07
> Published: 2023-08-26

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 18
- State: closed
- Author: Georges760
- Opened: 2023-08-26
- Closed: 2023-08-26
- Labels: none

## Description

In `ASIC_task` :
```c
    int baud = BM1397_set_max_baud();
    SERIAL_set_baud(baud);
```

I observed this :
![image](https://github.com/skot/ESP-Miner/assets/1989461/546d52a5-3f09-4d11-8d16-c78f5d077feb)

The SERIAL_set_baud() is applyed before the full command is send at old baudrate.

In that case, the BM1397 will never change its baudrate, and never receive any jobs, so it will appear as a chip that doesn't find any nonce, and the current FW implementation is happy with that comportement.

We should:
- add a delay between BM1397_set_max_baud() and SERIAL_set_baud() above (1ms should be enough)
- add a way to detect the asic is not finding any nonce

## Comments

### benjamin-wilson on 2023-08-26

Added delay
https://github.com/skot/ESP-Miner/commit/0ceb4532a4f5741c64346de21414b8e6f493e931

Even if we detect the asic is not finding any nonces there's not a lot we can do about it, probably a hardware issue in that case? If there is a specific scenario can you open another issue?

### johnny9 on 2023-08-28

If this is a one time thing we can add a sanity check similar to the bm1397 unit test that feeds in a known midstate to check that we're setup. 

### skot on 2023-08-28

We could put something on the display and reset the ASIC.. try and get it unstuck.
