# Loki rig builds

> Source: https://forum.heatpunks.org/t/loki-rig-builds/112
> Collected: 2026-10-10
> Published: 2025-05-03
> Registry ID: heatpunks-forum

josh | 2025-05-03 14:51:37 UTC | #1

After messing around with a few types of heat reuse setups, my favorite is still the humble single board S19 loki rig. These are relatively easy to make and there are a few different styles which are ever evolving. I like that they can be functional art and they’re simple for the uninitiated to plug in and understand (“its a space heater that pays you”).

Being single board units lets you spread the hashrate around to different existing circuits in your home so you balance power usage and heat and adding a wifi plug lets you schedule runtime (or get even fancier and automate with a thermostat/homeassistant/etc.).

Main components for each build:

- S19 hashboard (I usually use JPros)

- APW3++ power supply (or APW7 for slightly less performance)

- Power supply cables (4 AWG battery cables)

- Loki chip

- Control board

- Enclosure

- Fans

- Wifi Bridge

- wifi plug (optional but makes it easy to schedule on/off)

## [Mineforheat.com](http://Mineforheat.com) Aluminum

[![0C9F44CD-AC14-4661-9360-354C09C53D98_1_105_c](https://forum.heatpunks.org/uploads/default/optimized/1X/6dc77ce3e934d1a78f4d994a93e5c6318b44d339_2_569x500.jpeg)0C9F44CD-AC14-4661-9360-354C09C53D98_1_105_c946×830 268 KB](https://forum.heatpunks.org/uploads/default/original/1X/6dc77ce3e934d1a78f4d994a93e5c6318b44d339.jpeg)

This was my first build, using the [mineforheat.com](http://mineforheat.com) aluminum case and noctua fans. This enclosure is the best all around in terms of performance and noise in my experience. Fans are a little expensive and weak but very quiet. They are just powerful enough to cool at the settings where the chips start to be voltage-starved.

## “Stackedtoshi” s19

[![45D0BC20-6EEE-46BF-AC46-6B556A0DBA5D_1_105_c](https://forum.heatpunks.org/uploads/default/optimized/1X/81df140db9cdfedfec96fa2873eb41cf73aabb92_2_375x500.jpeg)45D0BC20-6EEE-46BF-AC46-6B556A0DBA5D_1_105_c768×1024 226 KB](https://forum.heatpunks.org/uploads/default/original/1X/81df140db9cdfedfec96fa2873eb41cf73aabb92.jpeg)
[![4D06B82F-1D7D-4381-B513-07118D56A9EA_1_105_c](https://forum.heatpunks.org/uploads/default/optimized/1X/a84eb2f0f5bd35106f1d2d7bcc7eeb1b588b72e7_2_375x500.jpeg)4D06B82F-1D7D-4381-B513-07118D56A9EA_1_105_c768×1024 255 KB](https://forum.heatpunks.org/uploads/default/original/1X/a84eb2f0f5bd35106f1d2d7bcc7eeb1b588b72e7.jpeg)
This build uses two 3000rpm noctua fans and the stock s19 enclosure. It also has two printed air baffles to direct the air over the single board. It’s louder than a 4 fan setup but still acceptable levels in our office. The psu also has a quiet noctua fan installed. The PSU fans are small so the high pitch needs to be managed. You can also quiet these using an inline resistor on the stock fan which is a lot cheaper than a noctua.

## Printed mineforheat

[![10258761-D207-457E-BEB7-743190D41E1A_1_105_c](https://forum.heatpunks.org/uploads/default/optimized/1X/35243b116a396ef3376704a019a89ef509646211_2_375x500.jpeg)10258761-D207-457E-BEB7-743190D41E1A_1_105_c768×1024 242 KB](https://forum.heatpunks.org/uploads/default/original/1X/35243b116a396ef3376704a019a89ef509646211.jpeg)
Same as the aluminum mineforheat case except 3d printed with PETG. Also uses the S19 power supply modified for 120v power. I’ve since added 2 more fans to this one for noise reduction but wanted to play around with a more “compact” setup when I took this photo. Using the APW12 also lets you push hashrate farther provided you have enough cooling.

## Another printed mineforheat

[![956FBC4E-943A-434B-B7D7-DA8742B88506_1_105_c](https://forum.heatpunks.org/uploads/default/optimized/1X/f0206cbc793ac83b1e09df210ebeaa092276f753_2_375x500.jpeg)956FBC4E-943A-434B-B7D7-DA8742B88506_1_105_c768×1024 241 KB](https://forum.heatpunks.org/uploads/default/original/1X/f0206cbc793ac83b1e09df210ebeaa092276f753.jpeg)
I started using Arctic P12max fans here as well as printed TPU gaskets for the fans. These give a good balance of noise/price/performance and are what I like to typically use. I like the translucent PETG since you can use the infill pattern to add some artistic stylings.

## Minimaloki

[![C345C8ED-6FA8-4855-969E-C8C35E34E4CC_1_105_c](https://forum.heatpunks.org/uploads/default/optimized/1X/38e0570936bcc7766d137e0b92a8073f441c0eff_2_666x500.jpeg)C345C8ED-6FA8-4855-969E-C8C35E34E4CC_1_105_c1024×768 235 KB](https://forum.heatpunks.org/uploads/default/original/1X/38e0570936bcc7766d137e0b92a8073f441c0eff.jpeg)
This is the minimaloki design from [https://nakamotomining.com](https://nakamotomining.com). Works similar to the mineforheat enclosure but was a little harder to work with in terms of getting the wiring to fit. I used the stock black and yellow PSU wires and added ring terminals instead of using battery cables like in the other builds.

## Princess miner

[![8D63D4F6-0B26-4F66-85C3-5C214B88BD7C_1_105_c](https://forum.heatpunks.org/uploads/default/optimized/1X/74d87f8956c8b298fd8356f16c44a0b44ef230f7_2_562x499.jpeg)8D63D4F6-0B26-4F66-85C3-5C214B88BD7C_1_105_c940×835 225 KB](https://forum.heatpunks.org/uploads/default/original/1X/74d87f8956c8b298fd8356f16c44a0b44ef230f7.jpeg)
My favorite build so far is the princess. The carry handle is super useful.

## Hunting cabin edition

[![5A25E9AE-1DC1-4BC0-B778-61228F09749B_1_105_c](https://forum.heatpunks.org/uploads/default/optimized/1X/146064c6a7bf9464fb0c8ee4cab50b5a14efea5c_2_666x500.jpeg)5A25E9AE-1DC1-4BC0-B778-61228F09749B_1_105_c1024×768 281 KB](https://forum.heatpunks.org/uploads/default/original/1X/146064c6a7bf9464fb0c8ee4cab50b5a14efea5c.jpeg)
[![5FBC4B29-A29A-4020-AC49-3BE47551AD01_1_105_c](https://forum.heatpunks.org/uploads/default/optimized/1X/cf8278130eb8d82bd3c424d88620e6564e3c00d5_2_375x500.jpeg)5FBC4B29-A29A-4020-AC49-3BE47551AD01_1_105_c768×1024 264 KB](https://forum.heatpunks.org/uploads/default/original/1X/cf8278130eb8d82bd3c424d88620e6564e3c00d5.jpeg)
This one uses two 140mm fans in another attempt to make a more compact rig. It’s louder than a 4 fan but quieter than a dual 120mm fan setup.

I’ll post more rigs once i get some more photos.

Would love to see other peoples loki builds.

-------------------------

tronsington | 2025-05-13 15:31:24 UTC | #2

How difficult are these Loki rigs to build? I’m interested in building one, but am hesitant about killing a machine in the process. Do I need 220v to test or can I just install the Loki chip and go straight to 110v?

-------------------------

thak777 | 2025-05-22 18:47:15 UTC | #3

As long as you’ve got those APW3 or APW7 PSUs, you just plug them into a standard household 120V socket. Super easy.

-------------------------

josh | 2025-05-24 13:54:43 UTC | #4

It’s pretty easy if you’ve ever built a PC. The most “technical” part of the build in my experience is taking apart the PSU to replace the wires powering the hashboard/control board (I usually use 4 AWG battery cables or welding cable with ring terminals) and making the PSU fan quieter by replacing with a noctua or adding an inline resistor.

Another detail is, if you want to give it wifi and have only one power cord, you need to pull power for the wifi bridge from the PSU. I usually use the Vonets wifi bridge and make up an adapter using the USB/barrel jack adapter they include. I cut off the USB end and splice the barrel jack to wires with ring terminals and then either attach those to the PSU directly or stack them on the hashboard power lugs depending on the build. You also need to make sure you retain one of the PCIe power connectors for the control board.

Be very careful to keep + and - separated when connecting the cables to the hashboard especially if your ring terminals are bulky. I really like the [mine4heat hashboard seal](https://www.thingiverse.com/thing:6836764) since it adds some insulation between the lugs.

Main steps I follow:

1. PSU hashboard wires set up (hashboard, control board, wifi bridge)

2. PSU fan replaced/quieted

3. PSU

  voltage mod

4. Hashboard into enclosure

5. Wire up

6. Add fans

7. Install covers

-------------------------

tylerkstevens | 2025-06-10 13:46:45 UTC | #5

Here’s a link to @Trevorbello build tutorial videos:
[https://heatpunks.org/t/loki-rig-build-tutorials-by-trevor-bello-stacking-sats-podcast/31?u=tylerkstevens](https://heatpunks.org/t/loki-rig-build-tutorials-by-trevor-bello-stacking-sats-podcast/31?u=tylerkstevens)

-------------------------

Cody | 2025-07-14 00:07:25 UTC | #6

@josh do you know if you need a loki conversion kit to run an APW3++ S19 at 220v?

I want to create a single board unit that runs on 220v and would prefer not to have to do the loki conversion if it isn’t necessary.

-------------------------

josh | 2025-07-14 13:44:54 UTC | #7

Yeah you’d need the Loki PSS to spoof the power supply since apw3 doesn’t have the data cable between psu and control board even if running 220v.
