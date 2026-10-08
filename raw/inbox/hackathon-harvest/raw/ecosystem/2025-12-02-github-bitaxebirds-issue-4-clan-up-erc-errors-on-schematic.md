# bitaxeorg/bitaxeBIRDS issue #4: Clan up ERC errors on schematic

> Source: https://github.com/bitaxeorg/bitaxeBIRDS/issues/4
> Collected: 2026-10-07
> Published: 2025-12-02

- Repository: bitaxeorg/bitaxeBIRDS
- Type: issue
- Number: 4
- State: closed
- Author: penguin359
- Opened: 2025-12-02
- Closed: 2026-02-10
- Labels: none

## Description

While I didn't find anything that looks like a serious error, I recommend cleaning up the ERC errors so that it can be used to easily detect real errors in any future decision revisions. One interesting error I found buried in the current list was this label not connected error on the ASIC sheet:

<img width="632" height="369" alt="Image" src="https://github.com/user-attachments/assets/ba38cb58-2568-412c-b23b-9fe1c2474fb8" />

As far as I can tell, the VDD label isn't used anywhere else in the sheet so nothing seem to be broken, but it would probably good to fix that connection in case it gets used later. Cleaning up the current ERC errors can also help catch similar errors later.

Another simple error to fix is the 12V port going to the data sheet as nothing uses that port within the sheet. Most of the rest of the errors can be fixed by adjusting the pin types to match better. The Power output pins, and probably the inputs on the power output can be combined by using pin stacking and that can make it easier to use the part symbol in schematics as well only presenting one pin on the schematic while keeping them linked with their original identities.

## Comments

### skot on 2025-12-17

good catch, thank you! I'll clean this up.

### skot on 2026-02-09

Okay, I cleaned up a lot of these ERC errors and warnings. Not sure how to fix some of them surrounding the ASIC series power connections.

### penguin359 on 2026-02-13

I've seen two approaches to fixing similar power connection warnings. One has been to assign multiple pin numbers to one pin and the other is to follow the rules for Pin Stacking in KiCad which marks the additional power pins with the same name, but as invisible and type passive.

An example of the former approach can look like this:

<img width="299" height="830" alt="Image" src="https://github.com/user-attachments/assets/73ff22ea-c196-46fc-a37b-0b7b3225986d" />

But that is a bit ugly and the pin numbers probably should just be hidden by default at this point. The other option is to just mark them as excluded violations, of course.
