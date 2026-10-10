# bitaxeorg/bitaxeGamma pull request #57: Add TPS82130 for wide-VIN support

> Source: https://github.com/bitaxeorg/bitaxeGamma/pull/57
> Collected: 2026-10-07
> Published: 2026-02-22

- Repository: bitaxeorg/bitaxeGamma
- Type: pull request
- Number: 57
- State: open
- Author: korbin
- Opened: 2026-02-22
- Closed: n/a
- Labels: none

## Description

This PR adds a TPS82130SIL power module to the BOM for wide-VIN support.

With this change, the user can now supply 5V-16V without issue. The fan remains powered via 5V for compatibility.

This PR re-uses existing resistor and capacitor values for a total of one unique BOM item added (at a cost of ~$0.60.)

---

I've also added a DNP 0805 jumper to allow bridging VIN<->5V for legacy behavior.

## Comments

### justnate787-lang on 2026-02-23

Another attempt to cover up my stolen ip
