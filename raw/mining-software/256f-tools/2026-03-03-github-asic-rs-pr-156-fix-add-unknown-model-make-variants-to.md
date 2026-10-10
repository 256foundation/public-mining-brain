# 256foundation/asic-rs pull request #156: fix: add Unknown model/make variants to handle unrecognized models

> Source: https://github.com/256foundation/asic-rs/pull/156
> Collected: 2026-10-07
> Published: 2026-03-03

- Repository: 256foundation/asic-rs
- Type: pull request
- Number: 156
- State: closed
- Author: DanNicolau
- Opened: 2026-03-03
- Closed: 2026-03-04
- Labels: none

## Description

Previously, miners with undefined or unrecognized model strings would be dropped from scan results, making them invisible to detection. This was particularly problematic for devices with all hashboards down.

This change adds MinerModel::Unknown and MinerMake::Unknown variants to gracefully handle these cases. The Unknown variants follow the same pattern as other models, returning None for hardware specifications as recommended.

Fixes #155

## Comments

### moonbootspleb on 2026-03-03

Haven't deeply examined the flow but seems like this could get dicey for devices with very slow responses. Has that been considered?

### DanNicolau on 2026-03-03

Maybe you can expand on that thought for me to better understand @moonbootspleb . I don't think this would have a significant impact since the only occurence this would show up is if a user is running a rig with no hashboards alive, which hopefully should be uncommon.

### b-rowan on 2026-03-03

> Haven't deeply examined the flow but seems like this could get dicey for devices with very slow responses. Has that been considered?

I believe the case you're thinking of returns a `ModelDetectionError::NoModelResponse`, not an unknown model.  We should only be returning an unknown model if we explicitly know that it's a miner, we've gotten a proper response, etc, but the model is missing or not defined.

### moonbootspleb on 2026-03-03

Yes, Ryan will hopefully get to documenting and providing an issue for such a case at our qa site today.
