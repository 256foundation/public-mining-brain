# bitaxeorg/ESP-Miner issue #785: v2.6.0b11 bricks 403 board

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/785
> Collected: 2026-10-07
> Published: 2025-03-21

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 785
- State: closed
- Author: jusincase99
- Opened: 2025-03-21
- Closed: 2025-03-22
- Labels: none

## Description

The v2.6.0b11 update causes the 403 board to fail to reboot at all. All there is is a black screen and no activity at all.



## Comments

### skot on 2025-03-21

Uh oh! That's not good. I'll take a look today. Can you tell us what method you used to flash v2.6.0b11?

Is there any log output?

### jusincase99 on 2025-03-21

I used the bitaxetool method with a usb c data cable connection. I didn't collect an output log, not sure of the commands to use to get one. I could re flash if you can tell me the bitaxetool commands to use to generate the log?


### skot on 2025-03-21

If you're already connected over USB you can just open a serial terminal at 115200 baud.

### jusincase99 on 2025-03-21

I'm not, I flashed back to the previous 10 build and am over wi fi so I have to rehook it up and open the bitaxe tool.

On Friday, March 21st, 2025 at 1:00 PM, skot ***@***.***> wrote:

> If you're already connected over USB you can just open a serial terminal at 115200 baud.
>
> —
> Reply to this email directly, [view it on GitHub](https://github.com/bitaxeorg/ESP-Miner/issues/785#issuecomment-2744325713), or [unsubscribe](https://github.com/notifications/unsubscribe-auth/BO5HZOUJUSYAHFFFPTT4B4L2VRVUJAVCNFSM6AAAAABZPP5LJCVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDONBUGMZDKNZRGM).
> You are receiving this because you authored the thread.Message ID: ***@***.***>
>
> [skot]skot left a comment [(bitaxeorg/ESP-Miner#785)](https://github.com/bitaxeorg/ESP-Miner/issues/785#issuecomment-2744325713)
>
> If you're already connected over USB you can just open a serial terminal at 115200 baud.
>
> —
> Reply to this email directly, [view it on GitHub](https://github.com/bitaxeorg/ESP-Miner/issues/785#issuecomment-2744325713), or [unsubscribe](https://github.com/notifications/unsubscribe-auth/BO5HZOUJUSYAHFFFPTT4B4L2VRVUJAVCNFSM6AAAAABZPP5LJCVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDONBUGMZDKNZRGM).
> You are receiving this because you authored the thread.Message ID: ***@***.***>

### jusincase99 on 2025-03-21

No error log when flashing, appears to finish flashing goes to the restart then c prompt just fine but then the 403 just has a blank screen, fan won't run even after pressing the restart and trying an unplug form the electric and replug it back in.

On Friday, March 21st, 2025 at 1:52 PM, C P ***@***.***> wrote:

> I'm not, I flashed back to the previous 10 build and am over wi fi so I have to rehook it up and open the bitaxe tool.
>
> On Friday, March 21st, 2025 at 1:00 PM, skot ***@***.***> wrote:
>
>> If you're already connected over USB you can just open a serial terminal at 115200 baud.
>>
>> —
>> Reply to this email directly, [view it on GitHub](https://github.com/bitaxeorg/ESP-Miner/issues/785#issuecomment-2744325713), or [unsubscribe](https://github.com/notifications/unsubscribe-auth/BO5HZOUJUSYAHFFFPTT4B4L2VRVUJAVCNFSM6AAAAABZPP5LJCVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDONBUGMZDKNZRGM).
>> You are receiving this because you authored the thread.Message ID: ***@***.***>
>>
>> [skot]skot left a comment [(bitaxeorg/ESP-Miner#785)](https://github.com/bitaxeorg/ESP-Miner/issues/785#issuecomment-2744325713)
>>
>> If you're already connected over USB you can just open a serial terminal at 115200 baud.
>>
>> —
>> Reply to this email directly, [view it on GitHub](https://github.com/bitaxeorg/ESP-Miner/issues/785#issuecomment-2744325713), or [unsubscribe](https://github.com/notifications/unsubscribe-auth/BO5HZOUJUSYAHFFFPTT4B4L2VRVUJAVCNFSM6AAAAABZPP5LJCVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDONBUGMZDKNZRGM).
>> You are receiving this because you authored the thread.Message ID: ***@***.***>

### jusincase99 on 2025-03-21

Here are screen shots for you[Screenshot 2025-03-21 144342.png][Screenshot 2025-03-21 144225.png][20250321_144447.jpg]

On Friday, March 21st, 2025 at 2:07 PM, C P ***@***.***> wrote:

> No error log when flashing, appears to finish flashing goes to the restart then c prompt just fine but then the 403 just has a blank screen, fan won't run even after pressing the restart and trying an unplug form the electric and replug it back in.
>
> On Friday, March 21st, 2025 at 1:52 PM, C P ***@***.***> wrote:
>
>> I'm not, I flashed back to the previous 10 build and am over wi fi so I have to rehook it up and open the bitaxe tool.
>>
>> On Friday, March 21st, 2025 at 1:00 PM, skot ***@***.***> wrote:
>>
>>> If you're already connected over USB you can just open a serial terminal at 115200 baud.
>>>
>>> —
>>> Reply to this email directly, [view it on GitHub](https://github.com/bitaxeorg/ESP-Miner/issues/785#issuecomment-2744325713), or [unsubscribe](https://github.com/notifications/unsubscribe-auth/BO5HZOUJUSYAHFFFPTT4B4L2VRVUJAVCNFSM6AAAAABZPP5LJCVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDONBUGMZDKNZRGM).
>>> You are receiving this because you authored the thread.Message ID: ***@***.***>
>>>
>>> [skot]skot left a comment [(bitaxeorg/ESP-Miner#785)](https://github.com/bitaxeorg/ESP-Miner/issues/785#issuecomment-2744325713)
>>>
>>> If you're already connected over USB you can just open a serial terminal at 115200 baud.
>>>
>>> —
>>> Reply to this email directly, [view it on GitHub](https://github.com/bitaxeorg/ESP-Miner/issues/785#issuecomment-2744325713), or [unsubscribe](https://github.com/notifications/unsubscribe-auth/BO5HZOUJUSYAHFFFPTT4B4L2VRVUJAVCNFSM6AAAAABZPP5LJCVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDONBUGMZDKNZRGM).
>>> You are receiving this because you authored the thread.Message ID: ***@***.***>

### jusincase99 on 2025-03-21

Screenshots of reflash back to ob10, 403 working perfectly with that build.[20250321_145823.jpg][403 board v10.png]

On Friday, March 21st, 2025 at 2:49 PM, C P ***@***.***> wrote:

> Here are screen shots for you[Screenshot 2025-03-21 144342.png][Screenshot 2025-03-21 144225.png][20250321_144447.jpg]
>
> On Friday, March 21st, 2025 at 2:07 PM, C P ***@***.***> wrote:
>
>> No error log when flashing, appears to finish flashing goes to the restart then c prompt just fine but then the 403 just has a blank screen, fan won't run even after pressing the restart and trying an unplug form the electric and replug it back in.
>>
>> On Friday, March 21st, 2025 at 1:52 PM, C P ***@***.***> wrote:
>>
>>> I'm not, I flashed back to the previous 10 build and am over wi fi so I have to rehook it up and open the bitaxe tool.
>>>
>>> On Friday, March 21st, 2025 at 1:00 PM, skot ***@***.***> wrote:
>>>
>>>> If you're already connected over USB you can just open a serial terminal at 115200 baud.
>>>>
>>>> —
>>>> Reply to this email directly, [view it on GitHub](https://github.com/bitaxeorg/ESP-Miner/issues/785#issuecomment-2744325713), or [unsubscribe](https://github.com/notifications/unsubscribe-auth/BO5HZOUJUSYAHFFFPTT4B4L2VRVUJAVCNFSM6AAAAABZPP5LJCVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDONBUGMZDKNZRGM).
>>>> You are receiving this because you authored the thread.Message ID: ***@***.***>
>>>>
>>>> [skot]skot left a comment [(bitaxeorg/ESP-Miner#785)](https://github.com/bitaxeorg/ESP-Miner/issues/785#issuecomment-2744325713)
>>>>
>>>> If you're already connected over USB you can just open a serial terminal at 115200 baud.
>>>>
>>>> —
>>>> Reply to this email directly, [view it on GitHub](https://github.com/bitaxeorg/ESP-Miner/issues/785#issuecomment-2744325713), or [unsubscribe](https://github.com/notifications/unsubscribe-auth/BO5HZOUJUSYAHFFFPTT4B4L2VRVUJAVCNFSM6AAAAABZPP5LJCVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDONBUGMZDKNZRGM).
>>>> You are receiving this because you authored the thread.Message ID: ***@***.***>

### jusincase99 on 2025-03-21

0b12 seems to be working perfectly. Thanks!
