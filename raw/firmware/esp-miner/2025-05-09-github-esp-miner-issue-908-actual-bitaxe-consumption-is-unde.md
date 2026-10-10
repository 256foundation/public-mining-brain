# bitaxeorg/ESP-Miner issue #908: Actual Bitaxe Consumption is Underestimated

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/908
> Collected: 2026-10-07
> Published: 2025-05-09

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 908
- State: open
- Author: cicoph
- Opened: 2025-05-09
- Closed: n/a
- Labels: none

## Description

I ran some tests on Gamma using a smart plug to measure actual power consumption. From my tests with the default settings, I got the following results:

Gamma: 14 W
Plug: 24 W

With a bit of overclocking:
Gamma: 21 W
Plug: 35 W

Is it possible that there’s a bug in the power measurement on Axeos?

I repeated the test with different settings and other systems to check for measurement errors of the smart plug. I found that the plug with the power supply turned on consumes 3 W. However, when doing the calculations, the actual power output shown on Axeos still doesn’t add up. Has anyone else run similar tests?

## Comments

### Nexus9090 on 2025-05-09

I'm running a Gamma also fractionally overclocked 550Mhz.

The results at the plug you're seeing are due to the inefficieny in the mains power supply, this varies significantly with the quality of the power supply brick and if it has synchronous rectification or not. The low/mid end 30W supplies tend to only be ~80-85% efficient with some of the better ones achiving 85-90%

With the PSU I have I'm seeing  
Gamma: 17W  
Plug: 20W
Off load the PSU draws less than 0.4W

With the results you mention, it suggest the PSU you have is low end and low efficiency.

If every last watt matters to you, you might want to look at getting a GAN type power supply as these offer the highest efficiency typically in excess of 90% efficient. Most of these seem to be offered with USB-C connectors, so an adaptor will be needed to provide power to the BitAxe.

Its worth shopping around a bit and checking the specifications in detail, they can be a bit missleading.

### NilByte on 2025-05-09

I'm running underclocked 494MHz, asic voltage 1.02V on a 30W PSU.

Gamma: 15W
Plug: 17.1W

Check if you run the latest firmware. There was a release increasing the displayed power consumption by 5W. 

### mutatrum on 2025-05-10

Silly idea maybe, but this could to be user configurable as well. Current devices can only guess what the extra consumption is, and if it's configurable one can check with a wall meter.

### Nexus9090 on 2025-05-10

The problem with a user setting to offset the power brick efficiency is that the efficiency of a power brick typically isn't linear nor flat, so it might be n=80% at 25% load it might be n=85% at 50% load and n=79% at 100% load. 

Most flyback "brick/plugtop" power supplies tend to be worse efficiency at light load and are normally optimial from around 20-80% of load, even so they can have sweet-spots that'll add 3-4% in a narrow load range especially with QR-Flyback types which tend to be higher efficiency overall. 

So the efficiency of a PSU adapter/brick is a very difficult metric to manage since there's so many different PSU designs available, introducing a fixed offset would only be good for a fixed load condition and a known PSU type. Additionally, it'd require some kind of calibration in order to be accurate.

Personally I think it better to report the load at the DC jack since it is a true representation of what the board is actually consuming and let those users who are interested in the "at plug" performance choose a PSU that can deliver the efficiency they're looking for.

### seepv on 2025-05-10

Also an issue, for the Plug, could be the kind of measurement.

Small wattage and e.g. inductive loads, are problematic for some plugs.
The Tasmota-Plug of mine measures 0W with an v204 only attached.
