# bitaxeorg/ESP-Miner issue #671: Error - while update esp-miner.bin and www.bin - Unauthorized

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/671
> Collected: 2026-10-07
> Published: 2025-01-22

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 671
- State: closed
- Author: cooper64-prog
- Opened: 2025-01-22
- Closed: 2025-02-17
- Labels: none

## Description

**Describe the bug**
Updates cannot be installed; they run up to 100% and then report an error.
When updating both files, I receive the following error message after the update:

www.bin -> Error - Http failure response for http://bitaxe/api/system/OTAWWW: 401 Unauthorized 
esp-miner.bin -> Unauthorized

A friend of mine is experiencing the same issue with updates.

**To Reproduce**
Steps to reproduce the behavior:
1. download Latest Release: v2.5.1
2. start Updates

**Screenshots & Photos**
![Image](https://github.com/user-attachments/assets/406e1dbc-b9ff-491d-b68d-faf69ea2b4c3)
![Image](https://github.com/user-attachments/assets/f670d982-94ce-45fe-9b4f-bc9a01fef056)

If applicable, add AxeOS screenshots and/or photos of your Bitaxe to help explain your problem.

**Hardware (please complete the following information):**
Model: | BM1370
WiFi Status: | Connected!
Free Heap Memory: | 8391596
Version: | v2.5.0
ESP-IDF Version: | v5.4
Board Version: | 601


## Comments

### cooper64-prog on 2025-01-22

I fogot: the same Problem I had before also in the preveus version 2.5.0 with:
www.bin ->Error - Http failure response for http://bitaxe/api/system/OTAWWW: 401 Unauthorized

### mrv777 on 2025-01-22

In 2.5.0 you can't use the hostname, you have to use the IP address

### diegorodriguezv on 2025-01-25

Same problem here but only for the `www.bin` file.
I used http;//bitaxe and it updated the `esp-miner.bin` file correctly. When I tried the `www.bin` it showed the `401: Unauthorized` error.
After trying again with the ip it worked ok. The Current Version panel apparently shows the version of the firmware.
How can I check the version of the website?
Also, could the error message be a little more helpful? Like `401: Unauthorized, try again using the device IP`

### mutatrum on 2025-02-06

#657

I'll give it a try to fix it.

### eandersson on 2025-02-06

> [#657](https://github.com/skot/ESP-Miner/issues/657)
> 
> I'll give it a try to fix it.

I tried to implement something like this, basically if the origin matches the hostname, look it up, and if it matches the origin IP pass it. The lookup was just to verify that DNS was setup, resolvable and matching the device ip.
https://github.com/skot/ESP-Miner/pull/669/files#diff-b92a1982bb82df47ec29d7c8b425023f334ec820176646b59970905c61ebc5e4R114
