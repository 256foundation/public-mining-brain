# bitaxeorg/ESP-Miner issue #1188: "Power Fault Detected" miner too sensitive, faulting even on proven good PSU

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1188
> Collected: 2026-10-07
> Published: 2025-08-13

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1188
- State: closed
- Author: github12101
- Opened: 2025-08-13
- Closed: 2025-09-07
- Labels: none

## Description

**Describe the bug**
"Power Fault Detected" on any ATX PSU I've tried

**To Reproduce**
Connect miner to ATX PSU via DC barrel plug
It will never start mining, instead displaying "Power Fault Detected. Check your Power Supply." in the dashboard

**Expected behavior**
Miner works correctly

**Hardware (please complete the following information):**
Device Model:	Gamma (BM1370)
Firmware Version:	v2.9.0
AxeOS Version:	v2.9.0
ESP-IDF Version:	v5.4.1
Board Version:	601

Voltage, Frequency: happens on ALL frequencies and voltages, even lowest possible ones

**Please note: When connected to OEM brick PSU (5V 6.0A 30W Sunshine Technological Co., Ltd., China) supplied with the device, it works fine. Hashes 24/7 for days on end at 1.2 TH/s, no problems.** But not with ATX PSU.
I don't want to use OEM brick, I want 80Plus Gold efficient ATX supply from a working 24/7 computer next to it, hence my report.

<img width="2548" height="1074" alt="Image" src="https://github.com/user-attachments/assets/4a936d56-3c2a-463a-8e0c-936daa0d7929" />

Please note how miner is measuring voltage as 5.1V but still refuses to mine.
The miner is most likely hunting for the tiniest spike of low voltage, and once detected, it stops mining completely, making it impossible to operate on ATX power supply. Please consider lowering this sensitivity, so I can operate miner with a typical ATX PSU.

Caught this in Realtime logs:
```
₿ (13773) TPS546: Status: 0x2841
₿ (13774) TPS546: The voltage regulator is turned off
₿ (13778) TPS546: TPS546 INPUT Status: 00
₿ (13782) TPS546: The output voltage is NOT within the regulation window. PGOOD pin is asserted.
```

Steps I've tried to remedy this:

- Tried:
GameMax 1050W
Dell 360W
OCZ 600W
All I've been using for years in PCs, they have proven good 5V supply. Tried 4-pin Molex and SATA connectors.
- On GameMax 1050W, I've watched voltage on two multimeters through entire miner startup procedure, nominal voltage is 5.2V, it drops to 5.08V to go back up again to 5.18V. Never seen voltage dropping below 5.08V, but miner still doesn't mine on this PSU.
- Adding 4700uF 6.3V capacitor to screw terminal holding two wires going to DC barrel, to smooth voltage out, then tried two 2200uF 25V capacitors, no change.
- Replaced DC barrel plug to another one, exactly the same as OEM brick uses, no change.

## Comments

### github12101 on 2025-08-13

In ESP-Miner/main/power/vcore.c file I found:

```
static TPS546_CONFIG TPS546_CONFIG_GAMMA = {
    /* vin voltage */
    .TPS546_INIT_VIN_ON = 4.8,
    .TPS546_INIT_VIN_OFF = 4.5,
```

Is it that? that 4.5V is the lower limit? Once reached even for a tiniest moment, miner is stopping mining altogether?

### skot on 2025-08-19

Yes that's correct. The 5V Bitaxes have a very narrow VIN range, unfortunately.

Make sure your power connectors are very good. Doesn't matter how many watts your PSU if the connector is too high resistance it will fault the Bitaxe.

### github12101 on 2025-08-22

I see. That's very unfortunate. I ordered a brand new Bitaxe Gamma and got the exact same result. I'm going to sell it immediately as brand new – I don't want a flawed device. I'll also sell the used unit I bought. I have plenty of 5V available and don't need more AC-DC power units cluttering everything. So, Bitaxe devices are unfortunately a no for me.

### WantClue on 2025-09-07

This issue will be closed. The narrowed down 5V VIN range will not be adapted.

### github12101 on 2025-09-10

Since you are enforcing usage of chinese OEM power bricks with 5.3V output, instead of allowing high quality ATX PSUs from working with this device, I won't be using them. Already sold all my devices.

### skot on 2025-09-10

> Since you are enforcing usage of chinese OEM power bricks with 5.3V output, instead of allowing high quality ATX PSUs from working with this device, I won't be using them. Already sold all my devices.

Not sure what you mean. Any PSU that can deliver a steady 5.0V (to the voltage regulator -- beware crappy barrel plugs) at the required current will work well.
