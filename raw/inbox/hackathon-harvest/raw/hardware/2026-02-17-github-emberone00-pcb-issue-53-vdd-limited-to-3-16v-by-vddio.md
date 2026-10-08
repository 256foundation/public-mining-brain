# 256foundation/emberone00-pcb issue #53: VDD limited to ~3.16V by VDDIO LDO minimum input voltage

> Source: https://github.com/256foundation/emberone00-pcb/issues/53
> Collected: 2026-10-07
> Published: 2026-02-17

- Repository: 256foundation/emberone00-pcb
- Type: issue
- Number: 53
- State: open
- Author: rkuester
- Opened: 2026-02-17
- Closed: n/a
- Labels: bug

## Description

**Hardware Version:** v5 (9f75f0c)

## Summary

VDD cannot be raised above ~3.16V (0.26V per chip). Beyond that, the VDDIO LDOs in the upper domains lose regulation because their effective input voltage drops below the part's 2.1V minimum.

The VDDIO LDOs (MCP1824T-*) have a minimum input voltage of 2.1V. From the [datasheet](https://ww1.microchip.com/downloads/en/DeviceDoc/22070a.pdf):

> The minimum VIN must meet two conditions: VIN >= 2.1V and VIN >= VOUT(MAX) + VDROPOUT(MAX).

With the fixed 5V LDO supply and voltage-stacked ASICs, the first condition ceases to be met in the highest-voltage domain once total VDD exceeds ~3.16V.

## Analysis

The ASIC chain stacks 12 chips in series. Each domain's local ground sits at `(VDD / 12) * N` above board ground, where N is the domain index (0 = lowest, 11 = highest). The LDOs all share a common 5V input rail, so the effective input voltage for domain N is:

    V_IN = 5V - (VDD / 12) * N

For the highest domain (N=11):

    V_IN = 5V - (VDD * 11/12)

Setting `V_IN = 2.1V` (the LDO minimum) and solving for VDD:

    VDD_max = (5V - 2.1V) * 12/11 = 3.16V

Above ~3.16V total VDD, the top domain's LDO drops below its minimum input voltage. As VDD increases further, more domains fall out of spec.

## Observed symptoms

No matter how I try to raise frequency and voltage, the ASICs (starting with the last in the chain) start turning into oscillators at approximately VDD = 3.12V. This is consistent with the VDDIO LDO losing regulation and the IO interface becoming unreliable. The oscillations on RO propagate back through the entire chain.

## Software workaround

At VDD = 3.1V (0.26V per chip), the chain runs stably up to ~225 MHz, producing ~1.6 TH/s.

## Comments

### skot on 2026-02-17

Good catch @rkuester 

The fix, as I see it is to boost the USB 5V up to 6V for the ASIC domain VDDIO power rail. This puts the voltage right at the MCP1824T-* LDO VIN max of 6V (abs max 6.5V)

This allows us to turn VDD up to 4.25V (approx. 0.354V per ASIC) before the last domain LDO VIN drops below 2.1V. Of course domain imbalance could still cause problems, but when operating at the nominal 3.6VDD (~0.3V per ASIC) the last domain LDO VIN is 2.7V with lots of headroom.

I will look into it some more, but I think this boost regulator could take the place of the TPS22919 load switch on v5. The boost reg enable pin could be used to switch the VDDIO power on and off, like the load switch does now.

Doing it this way is nice because it preserves the ability to communicate with the ASICs when VDD is off.

### skot on 2026-02-17

todo: 
1. hack a v5 board to manually inject 6V to the VDDIO LDOs.
2. Test the current needed on the VDDIO LDO rail to size the boost regulator.

### skot on 2026-02-18

> 1. hack a v5 board to manually inject 6V to the VDDIO LDOs.
> 2. Test the current needed on the VDDIO LDO rail to size the boost regulator.

1. manually injecting 6V. Mining seems to be working at VDD=3.6V and 500MHz hash frequency.
2. It's drawing 60mA

### skot on 2026-02-20

added a 6V boost regulator to address this in ddfc8d9
