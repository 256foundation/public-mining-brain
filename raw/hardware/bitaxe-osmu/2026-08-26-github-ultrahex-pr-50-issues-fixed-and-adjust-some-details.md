# bitaxeorg/ultraHex pull request #50: Issues fixed , and adjust some details.

> Source: https://github.com/bitaxeorg/ultraHex/pull/50
> Collected: 2026-10-07
> Published: 2026-08-26

- Repository: bitaxeorg/ultraHex
- Type: pull request
- Number: 50
- State: closed
- Author: TDX33029
- Opened: 2026-08-26
- Closed: 2026-09-30
- Labels: none

## Description

1.Add a pull-up resistor to the RI pin at the end of the chip chain.This is to prevent the board from being unresponsive due to the internal pull-up on certain batches of chips not working.
2.Directly connect TPS546D24‘s AGND and GND ,remove the original net-tie'
<img width="547" height="262" alt="image" src="https://github.com/user-attachments/assets/702e274e-e764-488f-9608-68605b0dfaae" />
3.Remove one PCB DRC check rules called "Padstack issue",this rule will throw four errors which was casued by switch button's footprint,It's no big deal and exists in the original project
4.The two external Capacitor will no longer draw in PCB , Before this, converting from the schematic to the PCB would give two errors saying there are unlinked footprints.
<img width="855" height="510" alt="image" src="https://github.com/user-attachments/assets/0c02c27f-cf75-4410-aac5-38b95cae47a4" />
5.The fixed project have passed DRC checks，without Errors or Warnings
<img width="319" height="121" alt="image" src="https://github.com/user-attachments/assets/ba44e199-241b-4dde-bc79-8c24725a0216" />

where changed?
<img width="628" height="499" alt="Capture" src="https://github.com/user-attachments/assets/69a26421-000e-48bd-b4f0-221d80b76ca6" />



## Comments

### skot on 2026-09-19

I think the net-tie is the correct way to do this in KiCad as per the TPS546D24 datasheet comment to only connect AGND and GND at a single point.

### skot on 2026-09-19

Good catch on #1, the RI pullup should be added. I'll take a look at #3 and #4.

### TDX33029 on 2026-09-24

Okay, I've checked all the details on my device and made sure they work fine. As for those two extra electrolytic capacitors, they're still in the schematic, just no longer shown on the PCB.
