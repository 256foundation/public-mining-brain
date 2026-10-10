# bitaxeorg/ESP-Miner issue #515: Feature: configuration for screensaver timeout

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/515
> Collected: 2026-10-07
> Published: 2024-11-25

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 515
- State: closed
- Author: terratec
- Opened: 2024-11-25
- Closed: 2025-11-05
- Labels: enhancement

## Description

I would like to be able to turn the display on/off.

What do you think about the following implementation?
![boot-button](https://github.com/user-attachments/assets/a1c22a68-bc21-4f99-9571-fb8a73adca65)


## Comments

### mutatrum on 2024-11-25

What you could do is add a screensaver value, e.g. turn off after x seconds/minutes, or 0 to not turn it off.  If you press the boot button, screen turns on again for the same amount of time. That way it's a simpler configuration and we don't overload the button functionality.

I'm currently reworking button and screen behaviour to combine #510 into #434.

### terratec on 2024-11-25

Thanks, that sounds great. I will use it as practice.

### terratec on 2024-11-26

![screen-timeout-number](https://github.com/user-attachments/assets/c7399698-0144-4984-955f-cf4214427b31)

or maybe:
![screen-timeout-slider](https://github.com/user-attachments/assets/114cc490-c257-4a47-92e7-059256336f73)

or:
![screen-timeout-only-slider](https://github.com/user-attachments/assets/8b438d84-94d4-4dbe-ba3e-5141fdfac164)

### skot on 2024-11-28

Man I wish we had _one more_ button on the Bitaxe to use for UI

### mutatrum on 2024-11-29

You can have different lengths of long press. So normal click, normal long
press (> 200ms or so) and hold (> 2 seconds).

On Thu, 28 Nov 2024, 01:58 Skot, ***@***.***> wrote:

> Man I wish we had *one more* button on the Bitaxe to use for UI
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/skot/ESP-Miner/issues/515#issuecomment-2505067940>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ANN34JWADQ25YWIKXEF2YNL2CZTERAVCNFSM6AAAAABSNKKYPOVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZDKMBVGA3DOOJUGA>
> .
> You are receiving this because you commented.Message ID:
> ***@***.***>
>


### mutatrum on 2025-11-05

Fixed by #525
