# bitaxeorg/ESP-Miner issue #304: Add build instructions

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/304
> Collected: 2026-10-07
> Published: 2024-08-20

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 304
- State: closed
- Author: Sjors
- Opened: 2024-08-20
- Closed: 2024-12-01
- Labels: none

## Description

**Describe the bug**

As mentioned in #112 there are currently no instructions for how to build the firmware from source.

I suggest adding a separate `build.md` for this, so the README can focus on how install pre-compiled binaries.

If the process is similar to other esp firmware, then it should be enough to link to existing documentation and note any important differences.

## Comments

### WantClue on 2024-08-20

There are instructions in the wiki section and on the osmu.wiki 

### Sjors on 2024-08-20

Ah here? https://osmu.wiki/axeos/compile

In that case just adding that link to the README should do the trick.

I'll give it a try!

### ffrediani on 2024-08-21

@Sjors when you do a build, could you try add the necessary stuff to have LWIP IPv6 support are per #263 ?
Perhaps adding some extra headers/compile settings can make it to communicate with IPv6 destinations (test on solo6.ckpool.org:3333) and other stuff that may require code adjustments can be looked later.

### Sjors on 2024-08-26

I was able to create a binary, but when uploading it the UI (v2.1.8 from the "factory") just says "Working" and it never updates. The downloaded bin does work.

It's probably a good idea to have someone, who unlikely me knows what they're doing, start with a fresh macOS install and then writes all the dependencies down. I've previously done some ESP IDF building for Home Assistant stuff, so it's possibly my system is in a confused state.

I'll try to attach the broken binary here.



### Sjors on 2024-08-26

[broken-v2.1.10.zip](https://github.com/user-attachments/files/16748764/broken-v2.1.10.zip)


### skot on 2024-08-26

The UI (www) image is much more prone to failure since it's so much bigger. It's possible the update failed and your image is actually good. Maybe try recovering with flasher.bitaxe.org and then try the update again?

### Sjors on 2024-08-26

I only tried the self-compiled `esp-miner.bin`, which is what got stuck. I then used the official 2.1.0 release which worked fine (first `esp-miner.bin` and then `www`).

I might just try the build & upgrade process again for the next release (candidate).

One thing that would make the process easier to debug is to have a separate upload and install step in the UI (and perhaps an additional sanity check).

### ffrediani on 2024-08-28

@Sjors did you enable the IPv6 significant flags for AxeOs to communicate in IPv6 in this build ?

### Sjors on 2024-08-28

@ffrediani no, I wanted to just get it to work, IPv4 was fine for now.

### ffrediani on 2024-08-28

Oh dear !
