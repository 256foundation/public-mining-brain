# bitaxeorg/bitaxe-web-flasher issue #2: Flashing fails after flash complete

> Source: https://github.com/bitaxeorg/bitaxe-web-flasher/issues/2
> Collected: 2026-10-07
> Published: 2024-11-18

- Repository: bitaxeorg/bitaxe-web-flasher
- Type: issue
- Number: 2
- State: closed
- Author: w3irdrobot
- Opened: 2024-11-18
- Closed: 2024-11-20
- Labels: none

## Description

something must have changed in the last few days that seems to have broken flashing. i'm able to connect to my bitaxe, start flashing, and see logs pop up as it flashes. However, at flashing 100%, it then outputs a failure with

```
Flashing failed: Failed to execute 'open' on 'SerialPort': The port is already open.. Please try again.
```

Based on the git history, i'm assuming it's something in this commit: https://github.com/bitaxeorg/bitaxe-web-flasher/commit/e30e160d5f9cf36d5dc09b34541a31331e0d1be7
