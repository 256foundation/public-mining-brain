# bitaxeorg/bitaxe-web-flasher issue #10: Change "Flashing 100% Completed" to something else to stop confusion

> Source: https://github.com/bitaxeorg/bitaxe-web-flasher/issues/10
> Collected: 2026-10-07
> Published: 2024-12-29

- Repository: bitaxeorg/bitaxe-web-flasher
- Type: issue
- Number: 10
- State: closed
- Author: uKnowMister
- Opened: 2024-12-29
- Closed: 2025-01-10
- Labels: enhancement, good first issue

## Description

Can we change "Flashing 100% completed" at the end of the flashing process to something else? Some people disconnect the miner from the computer at this point, even though the flashing process hasn't actually finished yet. Maybe change it to "Flashing Data 100%, work still in progress. Leave the device plugged in." Or simply display "Flashing 99%" and only show 100% once the flashing process is truly completed.

## Comments

### dustinb on 2025-01-05

I noticed this also.   Flashing 99% would work without any new translations. 

There is this translation for a completed step that I've never seen.  I think the restart happens so fast it's not visible

https://github.com/bitaxeorg/bitaxe-web-flasher/blob/22f799c3a7d638393c83be1023b8400c5d3195eb/src/i18n/locales/en.json#L65

Question, is that message enough to step people from unplugging?  Could show it when it gets to 100% here

https://github.com/bitaxeorg/bitaxe-web-flasher/blob/22f799c3a7d638393c83be1023b8400c5d3195eb/src/components/LandingHero.tsx#L270


### WantClue on 2025-01-07

That's a good idea
