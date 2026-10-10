# bitaxeorg/ESP-Miner issue #213: AxeOS based firmware updates fail

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/213
> Collected: 2026-10-07
> Published: 2024-06-10

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 213
- State: closed
- Author: skot
- Opened: 2024-06-10
- Closed: 2024-12-01
- Labels: bug

## Description

In some cases the AxeOS dashboard firmware updater fails, leaving the Bitaxe in a state where it does not boot. 
Usually the failure happens during the `www.bin` image update. 
In all of these cases (afaik) the bitaxe can be recovered with a USB firmware flash.

## Comments

### tdb3 on 2024-06-12

Do users encountering the issue see a particular error response (e.g. one of the 500 reason phrases returned)?  Could help see what error is encountered frequently.

Looking at the code below, it would make sense that the Bitaxe is left in a state where it doesn't boot with the web interface available.  The partition is being erased optimistically with the assumption that the subsequent write/update will work.  If it doesn't, there wouldn't be a www.bin to load on next boot.

https://github.com/skot/ESP-Miner/blob/11107a3d321e6d69b85cf6889d11ce9961446ed3/main/http_server/http_server.c#L422-L457

Not sure if we have enough space for this, but some devices handle this by having two partitions and flipping between the two.  Updates are written to the partition not currently being used.  On next boot, the updated partition is tried.  If loading is unsuccessful, execution falls back / fails safe to the partition that still functions, and the update can be tried again.

One alternative, if space is a luxury, would be to have three partitions, two that are very minimal in size to support bare-bones recovery, and the last to contain the bulk of the app.

`POST_OTA_update()` appears to do something similar with OTA updates (juggling more than one OTA partition).
https://github.com/skot/ESP-Miner/blob/11107a3d321e6d69b85cf6889d11ce9961446ed3/main/http_server/http_server.c#L462-L506



### WantClue on 2024-12-01

With recovery page this is been closed as fixed.
