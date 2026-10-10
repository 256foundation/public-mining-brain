# bitaxeorg/ESP-Miner issue #841: Building FW bin: boot_comm: mismatch chip ID, expected 9, found 0

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/841
> Collected: 2026-10-07
> Published: 2025-04-12

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 841
- State: closed
- Author: dskvr
- Opened: 2025-04-12
- Closed: 2025-04-16
- Labels: none

## Description

I have been building and flashingg `ESPMiner` for a couple months now. However, recently, when attempting to load the successfully built binary [`esp-miner.bin`] I get the error `boot_comm: mismatch chip ID, expected 9, found 0`

I was making some changes to the firmware, and so assumed it was my fault, but when checking out `tags/v0.6.3`, building and attempting to update with that binary, I am getting the same error. If download the pre-built binary, presumably also built from `tags/v0.6.3` and attempt to load it, the firmware updates without this error; so unlikely this is a device/gui issue. 

I cannot find the error string "mismatch chip ID" anywhere in the source code, so I am assuming this is an `ESP-IDF` error. 

I am pretty sure I have read all documentation on building from source, and have attempted to find anyone having the same issue to no prevail which is why I am posting this issue.

My local `ESP-IDF` version is `5.4`

```
Activating ESP-IDF 5.4
Setting IDF_PATH to '/Users/sandwich/esp/esp-idf'.
* Checking python version ... 3.8.4
* Checking python dependencies ... OK
* Deactivating the current ESP-IDF environment (if any) ... OK
* Establishing a new ESP-IDF environment ... OK
* Identifying shell ... zsh
* Detecting outdated tools in system ... OK - no outdated tools found
* Shell completion ... Autocompletion code generated
```

Possibly related to #833 

## Comments

### mutatrum on 2025-04-15

Can you make sure you're building for the ESP32-S3?

And are you sure about `tags/v0.6.3`? I assume you mean v2.6.3?

### WantClue on 2025-04-16

please move this over to the discussion tab introduced today 🚀
