# bitaxeorg/ESP-Miner issue #1354: 50% Hashrate on Bitaxe GT Gamma 800 with v2.11 firmware

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1354
> Collected: 2026-10-07
> Published: 2025-11-16

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1354
- State: closed
- Author: Bradvani
- Opened: 2025-11-16
- Closed: 2025-11-18
- Labels: none

## Description

Hey @mutatrum  , only getting 50% of the device hashrate on the Bitaxe GT800s after the v2.11 esp firmware update. 

<img width="530" height="276" alt="image" src="https://github.com/user-attachments/assets/9f9619a4-8f58-4c60-b795-5cb0d9e25f32" />
<img width="530" height="276" alt="image" src="https://github.com/user-attachments/assets/e80e0920-5638-4265-853b-b9988f92e595" />

Rolled back to 2.10 and it's working fine. 

Settings on both: 
Default, 525 @1150


PS: Encountered 0 errors on updating the Gamma 601s. It's a real eye catcher both on device and OS :))


## Comments

### mutatrum on 2025-11-16

Thank you for moving it to a separate issue.

As for the GT 800, take a look at https://github.com/bitaxeorg/ESP-Miner/discussions/1281. I assume you bought it from somewhere, and didn't manufacture it yourself. This is a bit of a tricky situation, as the design of the GT 800 has not been released yet, but some manufacturers are already producing and selling them, without the final hardware and no official support in the firmware. I'm not sure what firmware they installed on it when they sold it, and if they made custom changes to the firmware. We have no idea exactly what boards have been produced and which type you have, so YMMV. As for now, please try to downgrade to v2.10.1, as it seems that one is working, at least on the 800 prototype as mentioned in the discussion. Next step is to go to the seller, and see if they can make an updated firmware.

### mutatrum on 2025-11-16

Oh, can you verify on the pool side what the hashrate is? In 2.11 the way the hashrate is determined has been changed significantly, so it's possible it's only a reporting issue in the firmware.

### Bradvani on 2025-11-16

Of course. :)

Ah, that makes sense. I picked my device from Bitsoloplayer, they did mention that their firmware update is still being tested. I rolled it back to 2.10 and it just reduced my anxiety in a flash. 

Although, the new www update really helped me discover a flawed ASIC on one of my 800s. 

<img width="421" height="195" alt="Image" src="https://github.com/user-attachments/assets/155b012e-e995-4d16-af42-49f178e1d55b" />

Real banger on the UI, must say! 

### Bradvani on 2025-11-16

Yikes... I updated it back to 2.11 and tried to check the pool data, the displayed hashrate was indeed much lower than with stock firmware, however, on rebooting the miner with v2.11, the display goes blank and the AxeOS page won't load anymore.

So unfortunately I'm locked out and will need to wait for an updated web flasher/ stock firmware for the GT 800 model or a revert from the device manufacturer on steps. 😅

My second GT800 working fine on v2.10. I wish there was a way to use one device to reconfigure the other. Hey @duckaxe @WantClue any luck with getting a hold of GT800 firmware?, my device is from Bitsoloplayer (China).. 🙏

I'd be happy to catch someone at Bitcoin Mena and grab it on a flashdrive, if thats what it takes.
