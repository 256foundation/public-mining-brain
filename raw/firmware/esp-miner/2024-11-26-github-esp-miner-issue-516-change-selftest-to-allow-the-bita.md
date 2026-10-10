# bitaxeorg/ESP-Miner issue #516: change selftest to allow the bitaxe to boot, even if tests fail

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/516
> Collected: 2026-10-07
> Published: 2024-11-26

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 516
- State: closed
- Author: skot
- Opened: 2024-11-26
- Closed: 2025-01-06
- Labels: enhancement

## Description

Currently if one of the selftest tests fail, the Bitaxe will be stuck in selftest mode forever, essentially bricking the Bitaxe for those who don't know how to flash the nvs.

I think that no matter if tests pass or fail we should set nvs selftest=0 and boot normally after the user presses the BOOT button.

Of course it should be very obvious on the OLED and in the logs that tests have failed, so that both users and factories are aware.

## Comments

### skot on 2024-11-26

Also, once we have this functionality then it makes sense to use factory images (selftest=1) on the webflasher @WantClue 

### benjamin-wilson on 2024-11-26

selftest=0 should only happen _**after**_ the user presses the BOOT button, so that it can be power cycled and re-tested. 

### skot on 2024-11-26

I suppose we could get fancy and require a long press on BOOT to restart (and set selftest=0) if there is a failure?

### skot on 2024-11-28

This is addressed in PR #524 

### benjamin-wilson on 2024-12-22

> selftest=0 should only happen _**after**_ the user presses the BOOT button, so that it can be power cycled and re-tested.

When the self test passes, it should not self test again though, sorry if this was miscommunicated. This issue arose when trying to flash 2.4.2.
@skot 

### skot on 2024-12-22

> > selftest=0 should only happen _**after**_ the user presses the BOOT button, so that it can be power cycled and re-tested.
> 
> 
> 
> When the self test passes, it should not self test again though, sorry if this was miscommunicated. This issue arose when trying to flash 2.4.2.
> 
> @skot 

I thought maybe you'd want to test the boot button as that final test. Fine with me either way.
