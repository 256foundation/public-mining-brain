# bitaxeorg/ESP-Miner issue #1199: Skip web_ui_dist when nothing changed in AxeOS

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1199
> Collected: 2026-10-07
> Published: 2025-08-20

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1199
- State: closed
- Author: mutatrum
- Opened: 2025-08-20
- Closed: 2025-11-19
- Labels: none

## Description

The build always rebuilds and packages AxeOS, even though nothing changes. This is a fairly long process, and would be nice if this is skipped to have faster incremental build times when working on the firmware in vscode.

## Comments

### ghost on 2025-08-21

Break up the build process into two parts (if it's possible).

build = full build (I use this method after doing a fullclean).

build www = Website only

build esp = Firmware only




### mutatrum on 2025-08-21

I was thinking about making the `web_ui_dist` conditional on file change dates. I tried but failed.

### ruchus on 2025-09-20

What about to rename directory ESP-Miner\main\http_server\ **axe-os** for something more generic as for example **front-end** or **ui** ?

I know it's not important thing, but it's more in line with making bitaxe an open platform ready to create more UIs.

In my case, I have to copy the axwell-ui source code into Axeos directory. Nothing wrong, I just expect to find a generic directory where I can add my web code. In any case, it works !

But, if you break up the build process into two parts....  possibly already will be separated.

<img width="373" height="357" alt="Image" src="https://github.com/user-attachments/assets/aa474088-34c0-41b1-a6e7-2cd5d8b5ac9f" />
