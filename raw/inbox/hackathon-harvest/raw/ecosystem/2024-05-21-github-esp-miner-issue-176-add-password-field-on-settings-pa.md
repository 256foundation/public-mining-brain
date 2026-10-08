# bitaxeorg/ESP-Miner issue #176: Add `password` field on Settings page (for `mining.authorize`)

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/176
> Collected: 2026-10-07
> Published: 2024-05-21

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 176
- State: closed
- Author: plebhash
- Opened: 2024-05-21
- Closed: 2024-05-26
- Labels: enhancement

## Description

The AxeOS UI only allows the user to type in a `username`, but not a `password`.

DEMAND Pool allows [Solo SV1 mining](https://www.dmnd.work/#solo-sv1), but that requires the `password` field for authentication (`mining.authorize`). It is where the bitcoin address is informed.

![image](https://github.com/skot/ESP-Miner/assets/147345153/36f88782-87bc-438f-aab5-e8b5626ed436)

Therefore, it would be desirable to add a `password` field to the AxeOS Settings UI.

cc @Fi3 @AlejandroDeLaTorre

## Comments

### Fi3 on 2024-05-21

I confirm that in order to mine in solo mode with sv1 with demand you need to be able to insert a password. 

### benjamin-wilson on 2024-05-24

Maybe I'm missing something but there is already an input for a stratum password in settings.
![image](https://github.com/skot/ESP-Miner/assets/1399163/2b9118c3-ba3f-40b2-a903-7d75e3917c58)


### plebhash on 2024-05-26

 my BitAxe firmware is probably out of date, sorry for the noise

### plebhash on 2024-05-29

@benjamin-wilson how do I download or generate a `www.bin` so I can update my UI?

### plebhash on 2024-05-29

> @benjamin-wilson how do I download or generate a `www.bin` so I can update my UI?

found the answer:

- make sure [ESP IDF](https://docs.espressif.com/projects/esp-idf/en/stable/esp32/get-started/linux-macos-setup.html#get-started-linux-macos-first-steps) is available on your system ([here's a `shell.nix` I wrote for this](https://github.com/plebhash/ESP-Miner/blob/nix/shell.nix))
- `idf.py build`

the build artifacts will be inside `build` (including `www.bin`, which came from my original question)

### benjamin-wilson on 2024-05-29

There's also the `www.bin` on the releases page. If there's no UI changes I don't upload one.
https://github.com/skot/ESP-Miner/releases/tag/v2.1.3
