# 256foundation/emberone00-pcb issue #30: add pads for high side mosfet snubber resistors

> Source: https://github.com/256foundation/emberone00-pcb/issues/30
> Collected: 2026-10-07
> Published: 2025-04-19

- Repository: 256foundation/emberone00-pcb
- Type: issue
- Number: 30
- State: open
- Author: skot
- Opened: 2025-04-19
- Closed: n/a
- Labels: enhancement

## Description

Place an RC snubber across each high-side MOSFET (drain-to-source): try 100 pF + 10 Ω

## Comments

### skot on 2025-04-21

Interesting. The [LM25119 Datasheet](https://www.ti.com/lit/ds/symlink/lm25119.pdf) section says to put the snubber across the **low** side mosfet. The EVM has the values set to 1000pF and 5.1 Ohm. See #27 

<img width="271" alt="Image" src="https://github.com/user-attachments/assets/1348476c-7238-4f2f-bf09-3f11e6671870" />



### skot on 2025-04-21

EVM snubber capacitor is `C2012C0G2A102J`

### GitBobCat on 2025-04-27

If you are dealing with ringing then https://e2e.ti.com/cfs-file/__key/communityserver-discussions-components-files/196/slup100.pdf

Theory says you have Cpar, the parasitic at the node, and Csnb, the capacitor to snub the ringing. Csnb = 3*Cpar. You select the damping resistor, Rdmp, to be the resonant impedance. Rdmp=SQRT(L/Cpar). 

Your L will be the buck inductor, 6u8 in your example schematic. Your Cpar might be guessed at from the Mosfet datasheets. You get a graph of Coss, Ciss and Crss. I forget the sums to hit the value you want and it's a bit wet finger based on Vds.

Alternatively you can scope it with no added components to get an Fr1 for the resonant frequency and then add a known capacitor to get an Fr2 for the shifted, lower, frequency. Then solve Fr1=1/2.Pi.SQRT(LCpar) and Fr2=1/2.Pi.SQRT(L(Cpar+Cadd) for Cpar and select Csnb=3*Cpar etc.

HTH

Oh... the ringing that is being targeted might, is likely to,  be during inductor dry out when the circuit is operating discontinuosly at low load.

Oh... also assume the snubber capacitor is charged and discharged through the input voltage at every switching cycle. E = 1/2CV^2. Multiply that by the switching frequency and you get a good ballpark for how much power the resistor has to dissipate.

### skot on 2025-04-27

Ringing seems to be minimal... the problem is mostly spikes at the switching edges.

### GitBobCat on 2025-04-27

Grumble. Yes, I have seen that one mentioned on the data sheet. I'm uncertain as to why it should be there and if it is a real issue beyond looking bad. Being buck then under load the inductor is always going to reset through the lower mosfet, initially its body source diode. During regen, load dump, it will initially free-wheel back through the upper Mosfet body source diode. Assuming your input supply is stiff also theoretically not a problem.... unless the layout is sloppy. Decouple tight to the upper device. Mosfets, if you buy the right ones, are also rated for repetitive avalanche as long as you do not exceed the transient thermal impedance curves. Whatever way spikes are unclamped inductive energy seeking a way out and, waving a wet finger, with a 20A supply and a 5R1 snubber resistor you'll get a 102 volt spike unless something else catches it so that particular snubber is not really doing anything to those spikes. Measure tight to the Drain Source connection and use the springy ground needle thing on the probe tip collar to see if they are really there.
