# The Space Radiant Floor Demo Site - Hashrate Boiler Testing

> Source: https://forum.heatpunks.org/t/the-space-radiant-floor-demo-site-hashrate-boiler-testing/139
> Collected: 2026-10-10
> Published: 2025-06-10
> Registry ID: heatpunks-forum

tylerkstevens | 2025-06-10 13:38:18 UTC | #1

Hey all,

Wanted to let you know that @tronsington and I have received two unique M64 based boilers to test. The RY3T mini, thanks to Christian at [RY3T](https://ry3t.com). And the HS05, courtesy of PG at [Heat Core](https://heatcore.tech).

These units will be installed into a radiant floor system at [The Space](https://denver.space). We’ll make sure to document our process and findings here.

Let us know if you have any specific questions!

[![IMG_0297](https://forum.heatpunks.org/uploads/default/optimized/1X/2b7a12e980dbe873465cf0a951b4a80b4f98c36a_2_375x500.jpeg)IMG_02971920×2560 281 KB](https://forum.heatpunks.org/uploads/default/original/1X/2b7a12e980dbe873465cf0a951b4a80b4f98c36a.jpeg)
[![IMG_0357](https://forum.heatpunks.org/uploads/default/optimized/1X/1428aba09776f069f3527287040b5c62b2993672_2_666x500.jpeg)IMG_03571920×1440 313 KB](https://forum.heatpunks.org/uploads/default/original/1X/1428aba09776f069f3527287040b5c62b2993672.jpeg)

-------------------------

power2bit | 2025-06-11 08:08:01 UTC | #2

What are the pecs of the power input in those cabinets?

Would be a bit counterintuitive if they require 3-phase, given that the M64 is specifically built for single-phase home use.

-------------------------

Satoshi | 2025-06-11 09:21:11 UTC | #3

same question here i would be wondering how the singe phase is managed by RY3T mini. Two input Cables? Should not be 3 Phase correct? I mean the M64 was probably for a reason designed to be singe Phase.

-------------------------

tylerkstevens | 2025-06-11 14:03:17 UTC | #4

I’ll have to go look up the exact connector type. But it seems to be a normal 30 Amp plug for single phase, 220 V.

-------------------------

tylerkstevens | 2025-06-23 16:31:33 UTC | #5

Radiant install in progress. 1/2" PEX. Will do 5 zones across the two first floor sides of our building. As close to 300 ft runs as possible. Using the aluminum heat transfer plates to spread the heat out across the sub floor boards.

[![IMG_0521](https://forum.heatpunks.org/uploads/default/optimized/1X/b2928ecaabd9cff6ebedf599c3015b77ca5791db_2_666x500.jpeg)IMG_05211920×1440 243 KB](https://forum.heatpunks.org/uploads/default/original/1X/b2928ecaabd9cff6ebedf599c3015b77ca5791db.jpeg)
[![IMG_0524](https://forum.heatpunks.org/uploads/default/optimized/1X/f70e88821ae84b6d144458b4a1c119986ae51492_2_666x500.jpeg)IMG_05241920×1440 249 KB](https://forum.heatpunks.org/uploads/default/original/1X/f70e88821ae84b6d144458b4a1c119986ae51492.jpeg)
[![IMG_0528](https://forum.heatpunks.org/uploads/default/optimized/1X/4175cfa33d7fe215f5dc53216cd99bf18bb363e2_2_375x500.jpeg)IMG_05281920×2560 315 KB](https://forum.heatpunks.org/uploads/default/original/1X/4175cfa33d7fe215f5dc53216cd99bf18bb363e2.jpeg)

-------------------------

tylerkstevens | 2025-08-11 21:54:06 UTC | #6

30 Amp, 220 V. Same for each unit. We wired them up with a standard L6-30 receptacle.

-------------------------

tylerkstevens | 2025-08-11 21:55:57 UTC | #7

Both the RY3T Mini and Heatcore HS05 units have PDUs built in to the boiler. Single power cable into the boiler. Then a connector sends power to the M64 miner. I’ll start a unique thread for the RY3T Mini and HS05 respectively so we can organize information. I’ll keep this thread dedicated to our Radiant floor demo site at The Space.

-------------------------

tylerkstevens | 2025-08-11 22:06:15 UTC | #8

The [Exergy](https://exergyheat.com) radiant floor install at our office in [The Space](https://denver.space) is finally complete.

This took a bit longer than expected to be completed. We ended up hiring professionals to help us complete the job in a timely manner.

The plumbers did good work with the wall portion of the loop. There were a few pain points that required fixing, however:

- Circulator pump on the wall. We needed this installed to ensure future hashrate heating boilers can be tested in the system. The RY3T Mini actually includes a heating loop pump inside the boiler. So this was not obvious at first.

- Mixing Valve. We requested a mixing valve to blend the hot zone supply and cold zone return (essentially configuring how much water goes to the miner to be heated). This will help us ensure we don’t overheat the floor boards with excessively hot water from the miner. Our plumbers accidentally installed the mixing valve in the wrong place, mixing the return temp the the boiler. They didn’t understand why we’d want to mix out of the boiler. Good to know.

Also, we ended up needing 6 zones.

[![IMG_0947](https://forum.heatpunks.org/uploads/default/optimized/1X/a09e7017045a829b2bcfbf984d7f7b0688ee4fe6_2_666x500.jpeg)IMG_09471920×1440 311 KB](https://forum.heatpunks.org/uploads/default/original/1X/a09e7017045a829b2bcfbf984d7f7b0688ee4fe6.jpeg)
[![IMG_0949](https://forum.heatpunks.org/uploads/default/optimized/1X/d459d0f162b504c1d38ee0197f023f31b95b5274_2_375x500.jpeg)IMG_09491920×2560 527 KB](https://forum.heatpunks.org/uploads/default/original/1X/d459d0f162b504c1d38ee0197f023f31b95b5274.jpeg)
[![IMG_1006](https://forum.heatpunks.org/uploads/default/optimized/1X/d2db7c61dfcd59f47c0abde9650a66a63f6cc2d3_2_375x500.jpeg)IMG_10061920×2560 619 KB](https://forum.heatpunks.org/uploads/default/original/1X/d2db7c61dfcd59f47c0abde9650a66a63f6cc2d3.jpeg)

-------------------------

tylerkstevens | 2025-08-21 14:47:59 UTC | #9

System is up and running. We tested out the heated floors for the first time yesterday. [Here](https://x.com/tylerkstevens/status/1958282054686158971) are my initial reactions.

Came back in this morning after letting the system run overnight and I’m pretty sure we have an air lock in zone 5 and 6. No flow. Bubbles in the flow meter. Will troubleshoot today!

-------------------------

tylerkstevens | 2025-08-21 19:22:10 UTC | #10

Thermal Imaging
[![signal-2025-08-21-131236_003](https://forum.heatpunks.org/uploads/default/optimized/1X/4521514f39990b33bc44442b8cd6a5887e51952a_2_375x500.jpeg)signal-2025-08-21-131236_0031080×1440 177 KB](https://forum.heatpunks.org/uploads/default/original/1X/4521514f39990b33bc44442b8cd6a5887e51952a.jpeg)
[![FLIR_20250821_122505_263](https://forum.heatpunks.org/uploads/default/optimized/1X/4cb40ddaa677eb0c95ec0b4a478f09c47449224f_2_375x500.jpeg)FLIR_20250821_122505_2631080×1440 110 KB](https://forum.heatpunks.org/uploads/default/original/1X/4cb40ddaa677eb0c95ec0b4a478f09c47449224f.jpeg)

-------------------------

tylerkstevens | 2025-08-22 17:56:50 UTC | #11

Radiator installed out back so we can choose to heat the floors or dump heat outside in the summer. We have 20kW of solar on the building, so this lets us mine full time.

[x.com](https://x.com/tylerkstevens/status/1958945829605318945)

#### https://x.com/tylerkstevens/status/1958945829605318945

@

-------------------------

Cody | 2025-08-29 02:19:29 UTC | #12

Your setup looks sooo good!!  Is there control functionality to ramp up and down or do you have to dump heat to the radiator if the floors reject it?

-------------------------

tylerkstevens | 2025-08-29 14:38:52 UTC | #13

We are building the logic to “step” up and down in wattage with the default high, medium, low settings on the whatsminer firmware. But We’d prefer to control exact wattage. That elusive firmware problem looms over us ([Whatsminer M64 Firmware - Dynamic Power Adjustment?](https://heatpunks.org/t/whatsminer-m64-firmware-dynamic-power-adjustment/161))

So most likely a mix of step changes and bang-bang. Still in development.

-------------------------

Pleb_Ed | 2025-11-10 22:53:53 UTC | #14

Any recommendations on a heat exchanger if I want to use a similar setup to heat a pool?

-------------------------

Cody | 2025-11-14 15:50:13 UTC | #15

Pools would need a titanium heat exchanger.  They usually come in “tube and shell” style.  Not sure on sizing, that would depend on a lot of factors.  @Exergy might have the math chops to sort that out.

-------------------------

Plunger | 2026-01-29 23:39:15 UTC | #16

This is such a cool project. You guys did a great job. I get amped up when I see stuff like this happening now. Makes me excited to get my own project going.
