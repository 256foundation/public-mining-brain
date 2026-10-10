# 256foundation/emberone00-pcb issue #58: Consider ESD protection on the reset pushbutton

> Source: https://github.com/256foundation/emberone00-pcb/issues/58
> Collected: 2026-10-07
> Published: 2026-03-16

- Repository: 256foundation/emberone00-pcb
- Type: issue
- Number: 58
- State: open
- Author: rkuester
- Opened: 2026-03-16
- Closed: n/a
- Labels: none

## Description

The reset pushbutton will be touched by human fingers, so it's worth considering ESD protection. The boot pushbutton already has some series resistance, but the reset button does not.

Hardware version: v5 (9f75f0c)

## Comments

### skot on 2026-03-21

added in v6.1

### rkuester on 2026-03-21

LGTM. It may technically breach the layout guidelines for the TVS (see section 7.4.2 of the [datasheet](https://www.ti.com/lit/ds/symlink/tpd1e10b06.pdf)), but it's probably not a big deal, especially with the 1k series resistors present.
