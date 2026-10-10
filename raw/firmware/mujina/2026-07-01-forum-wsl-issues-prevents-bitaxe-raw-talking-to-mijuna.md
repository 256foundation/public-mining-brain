# WSL issues prevents bitaxe-raw talking to Mijuna

> Source: https://forum.256foundation.org/t/wsl-issues-prevents-bitaxe-raw-talking-to-mijuna/64
> Collected: 2026-10-07
> Published: 2026-07-01

ixtech.xyz | 2026-07-01 13:58:35 UTC | #1

I ran into dead-ended trying to get Mujina talking to my Bitaxe Gamma over WSL2+usbipd. Flashed bitaxe-raw at current HEAD and Mujina discovers the device fine, but every control-frame write hangs. Ran that all the way down and it turns out the *control* CDC ACM endpoint on the ESP32-S3 isn't being drained — I can flood 4 KB into the ASIC UART port in 340 ms, but identical write to the control port times out at 2 s. Confirmed with pyserial (dtr=True), raw shell echo, and Mujina's tokio-serial. So the block is inside bitaxe-raw, not on the Mujina side or in the frame format. I was able to get Mujina to build in WSL no problem and use the CPU mining, and the dashboard shows up fine.

Filed an issue on bitaxe-raw with reproducer: [Control CDC ACM endpoint not drained on Bitaxe Gamma over USB-IP (works fine for ASIC UART) · Issue #14 · bitaxeorg/bitaxe-raw](https://github.com/bitaxeorg/bitaxe-raw/issues/14). Not certain whether it's a real firmware bug or a usbipd interaction — haven't tested native Linux yet.

-------------------------

Unknown_aadhi | 2026-07-01 14:03:17 UTC | #2

Hey @ixtech.xyz , I have a PR with a windows driver code for mujina , can you try it with that ?

-------------------------

ixtech.xyz | 2026-07-03 01:34:44 UTC | #3

Where is that PR? I was able to get mujina to work on my windows machine using cpu mining fine..it was the bitaxe-raw that wasnt working. I was going to try s19jpro next

-------------------------

Unknown_aadhi | 2026-07-03 01:40:51 UTC | #4

https://github.com/256foundation/mujina/pull/75

It is PR #75 , sometimes I had issue with my bitaxe not working with WSL driver . Try it with this and lmk

-------------------------

ixtech.xyz | 2026-07-05 18:02:36 UTC | #5

That helped, but I still need to make some code changes and some other fixes on the USB side. I was able to finally get it working here on Windows with the help of Claude. Here’s the dashboard I have running for it.I’ll be making a PR soon on to the main repo and get this thing loaded in, and I can show you what I’ve done.

![image|690x462](upload://w4ZMQFVmaLCarLeFQBxH04MUZoT.jpeg)

-------------------------

ixtech.xyz | 2026-07-05 19:47:02 UTC | #6

[feat: native Windows support for Bitaxe mining by IxTechCrypto · Pull Request #76 · 256foundation/mujina](https://github.com/256foundation/mujina/pull/76)

-------------------------
