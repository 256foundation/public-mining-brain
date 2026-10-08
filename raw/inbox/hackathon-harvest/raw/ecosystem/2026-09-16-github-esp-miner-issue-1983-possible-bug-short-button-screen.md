# bitaxeorg/ESP-Miner issue #1983: Possible bug: short-button screen cycling has no exit when no screens were created

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1983
> Collected: 2026-10-07
> Published: 2026-09-16

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1983
- State: open
- Author: plastardhippo
- Opened: 2026-09-16
- Closed: n/a
- Labels: none

## Description

## Describe the bug

An AI-assisted source review found a possible unbounded loop when the display is configured as `NONE`. `screen_next()` keeps trying screen IDs until `screen_show()` succeeds, but the normal screen objects are only created when `is_screen_active` is true.

Could a maintainer confirm whether the input path is reachable in this configuration, or whether another guard prevents it? This is a source-level concern, not a reproduced hardware hang or a diagnosis of a recorded reset.

## To reproduce — proposed, not executed

Use a test fixture or spare device with display type `NONE`, normal mode rather than self-test, and a working short-button input. After initialization, invoke the short-button callback and observe whether it returns. An isolated test can model the no-screen state and assert a bounded number of screen attempts.

## Expected behavior

A button press should return promptly when no display/screens are available, for example through an inactive-display guard or a bounded carousel search.

## Source evidence

Initially reviewed: v2.15.1, commit `78a03e3b5e7600aa8691a7c319ccb4efce72719b`. The relevant development paths remain in `43e9b97ef6053bec44543fccb91f5d020e69be4d`, checked September 16, 2026:

- [Display NONE initialization](https://github.com/bitaxeorg/ESP-Miner/blob/43e9b97ef6053bec44543fccb91f5d020e69be4d/main/display.c#L251-L267) initializes LVGL and a 1x1 display, then returns without activating the normal screen module.
- [Input initialization](https://github.com/bitaxeorg/ESP-Miner/blob/43e9b97ef6053bec44543fccb91f5d020e69be4d/main/system.c#L338-L349) registers `screen_button_press` in normal mode.
- [Short-button callback](https://github.com/bitaxeorg/ESP-Miner/blob/43e9b97ef6053bec44543fccb91f5d020e69be4d/main/screen.c#L910-L927) can call `screen_next`.
- [Screen creation](https://github.com/bitaxeorg/ESP-Miner/blob/43e9b97ef6053bec44543fccb91f5d020e69be4d/main/screen.c#L967-L985) is conditional on `is_screen_active`.
- [Carousel loop](https://github.com/bitaxeorg/ESP-Miner/blob/43e9b97ef6053bec44543fccb91f5d020e69be4d/main/screen.c#L651-L667) has no bounded attempt count; [screen_show](https://github.com/bitaxeorg/ESP-Miner/blob/43e9b97ef6053bec44543fccb91f5d020e69be4d/main/screen.c#L546-L577) checks the selected LVGL object.

The development branch's large-display early return does not appear to cover the 1x1 NONE case. A standalone loop model illustrates nontermination when every candidate fails; it does not exercise LVGL, the physical input, or watchdog behavior.

## Hardware / context

Initial review context: Bitaxe Gamma 602, Solo Satoshi, v2.15.1. The owner's normal working display is not the proposed trigger. Frequency/voltage and pool credentials are unrelated. No device configuration was changed for this check. Existing PR #1870 concerns configurable carousel screens, but I did not find an exact report of this no-display case.
