# bitaxeorg/ESP-Miner issue #1380: Hashrate error percentage over 100%

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1380
> Collected: 2026-10-07
> Published: 2025-11-23

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1380
- State: closed
- Author: riotandhelo
- Opened: 2025-11-23
- Closed: 2025-11-29
- Labels: question

## Description

Hello everyone, I have the following problem: my Bitax Gamma 601 v2.11.0 keeps causing these errors. Everything runs normally for hours, then suddenly the hashrate shoots up, and the hash error rises to over 100%.

<img width="398" height="269" alt="Image" src="https://github.com/user-attachments/assets/17c79d14-51b7-4c89-8082-3a4914bc3ae6" />

 - Bitaxe HW version: Bitaxe Gamma 601
 - Bitaxe HW vendor: ebay
 - ESP-Miner FW version: v2.11.0
 - Hash Frequency: 825
 - Voltage: 5.1
 - I'm using a full node and I'm having a problem with public pool and CK pool.

## Comments

### mutatrum on 2025-11-24

Thank you for opening an issue, I've seen this reported, but haven't investigated yet. Is it correct that the pool does report the nominal hashrate?

### riotandhelo on 2025-11-24

Is it true that the pool reports the nominal hashrate? What do you mean by that? If the problem occurs again, should I upload a log file?

### mutatrum on 2025-11-24

The pool keeps reporting about 1.7 Th/s when this happens? So from the pool side, it looks like the device is happily hashing as normal?

### riotandhelo on 2025-11-24

The upper value, i.e., 2.25, goes up or even higher; if that happens, it won't find any more shares.

### riotandhelo on 2025-11-24

<img width="1570" height="693" alt="Image" src="https://github.com/user-attachments/assets/e1c77c5a-864d-4284-aefc-9c439ad6c36c" />

### mutatrum on 2025-11-24

Please post images directly to GitHub.

### mutatrum on 2025-11-24

This looks like #1053.

### riotandhelo on 2025-11-24

#1053. But there was no solution there, or did I miss something?

### mutatrum on 2025-11-24

> [#1053](https://github.com/bitaxeorg/ESP-Miner/issues/1053). But there was no solution there, or did I miss something?

No, we have not been able to reliably reproduce that issue. I'm also not 100% it's the same issue, just wanted to link them.

### riotandhelo on 2025-11-25

I've now tested it with the older firmware and various settings, but it keeps happening. I'll try it with the default settings now. Could it also be a hardware problem?

### WantClue on 2025-11-29

> [#1053](https://github.com/bitaxeorg/ESP-Miner/issues/1053). But there was no solution there, or did I miss something?

The flatline of death issue has been reported a couple of times. The only plausible understanding is some sort of a bug out of the chip, I had received such a device but was not able to reproduce the issue. It appears to be related to too high frequency settings. I have only seen this on very hard overclocked devices

### WantClue on 2025-11-29

Also with increased frequency the error rate will increase as well

### mutatrum on 2025-11-29

Closing as discussed on Discord:

> I currently have the following settings: Freq. 750 Core 1250. However, I increased the input voltage slightly to 5.4V, and since then the problems have disappeared.
