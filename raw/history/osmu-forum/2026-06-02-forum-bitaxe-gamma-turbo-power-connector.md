# Bitaxe Gamma Turbo & power connector

> Source: https://osmu.xyz/t/bitaxe-gamma-turbo-power-connector/32
> Collected: 2026-10-10
> Published: 2026-06-02
> Registry ID: osmu-forum

Guepi | 2026-06-02 11:24:08 UTC | #1

Hi there !

I wanna build a Bitaxe Gamma Turbo (with 2 BM1370).

After getting the files for ordering the PCB and the list of materials (BOM), I’ve noticed that the power connector isn’t found in Digikey website :

- J1 (with the reference XT30PW-M) which is the connector for the power.

This one seems to be a yellow connector that fits with a power unit with a XT30 connector ?

1. Why this is no more a barrel jack connector for the power connexion ?
2. For this board, with two BM1370 and a predictible overclocking of it, does a XT30 is enough or should I move to XT60 connector ?
3. Is it better to have a power unit like a portable computer one (black, solid, no opening) or like a desktop computer PSU (small, with a power button, and opening that let the air goes in) ?
4. Whatever I choose, does I need to have a new power unit, or may I adapt an old one with the good connector, maybe like a 65W HP power unit that may be 20 years old ?

-------------------------

WantClue | 2026-06-03 18:08:06 UTC | #2

Hey Guepi and welcome to the build! Good eye on the BOM — and the short version is that everything you’re seeing is correct and intentional. The connector change all comes back to one thing: the Gamma Turbo runs on **12V**, not 5V like the single-chip Bitaxe boards. Once you know that, your four questions mostly answer themselves.

**1. Why an XT30 instead of a barrel jack?**

Two reasons, both tied to the dual-chip design. First, the GT moved from a 5V input to a 12V input. Second, it pulls a lot more current — stock draw is around 43W, and the official supply for it is rated 12.4V / 10A (124W) to leave headroom. A small 5.5×2.1mm barrel jack is really only happy up to ~5A; push sustained higher current through one and you get heating, voltage drop, and eventually a loose, high-resistance (or arcing) connection. The XT30 comes from the RC/drone world, where it’s designed for exactly this: low resistance, a positive locking fit that won’t vibrate loose, and proper high-current handling.

The part itself (Amass **XT30PW-M**) is just the *board-mount, male* version of the XT30 — the “PW” is the PCB-mount body and the “-M” is male, so your power cable will end in a **female** XT30. Digikey doesn’t always stock the PCB-mount Amass variant, but it’s a totally standard part — any RC/hobby shop, Amazon, AliExpress, or an Amass distributor will have it. Just make sure you get the PCB-mount version (with the legs/pads), not the wire solder-cup version.

**2. Is XT30 enough, or should I go XT60?**

XT30 is plenty — no need to change. Even the most conservative rating for an XT30 is ~15A continuous (30A peak), and the better-tested figures are much higher with decent wire. At 12V, the official 124W supply is only ~10A, and even an aggressive overclock keeps you comfortably under the XT30’s rating. So you’re nowhere near its limit.

Also worth knowing: the PCB is laid out specifically for the XT30 footprint, so swapping to an XT60 isn’t a drop-in change anyway

**3. Sealed brick vs. desktop ATX-style PSU?**

For a single GT, a good sealed 12V brick is the cleaner choice: quiet, compact, nothing to configure, and it sits on the desk.

**4. Can I reuse an old supply, like a 20-year-old 65W HP unit?**

This is the one to be careful with — please check the label before connecting anything. Two problems with that HP brick:

- **Voltage:** old HP laptop adapters are almost always **18.5V or 19V**, not 12V. The GT expects 12V. Feeding ~19V into a 12V board risks frying it. So unless the label literally says **12V DC**, don’t use it, no matter how easy it’d be to fit an XT30.
- **Wattage:** even if it *were* 12V, 65W ≈ 5.4A at 12V. Stock draw is already ~43W, which leaves almost nothing for the overclocking you’re planning. The official supply is 124W for exactly that reason.

-------------------------

Guepi | 2026-06-03 18:46:42 UTC | #3

Wouah !

Thank you @WantClue for your complete answer with all the answers clearly explained.

For the old computer power unit, yes it’s 18.5 V.

I guess I could have changed the values of C1 (33 uF) and C2 (10 uF) on the power schema in order to transform the 18.5 V into a 12V.

But since the overclocking will be difficult, I’d prefer to stay on “recommanded” power unit.

-------------------------

skot | 2026-06-10 12:03:31 UTC | #4

We also needed a physically backwards incompatible power connector with the move to 12V so I don’t smoke all my old 5V bitaxes  :sweat_smile:
