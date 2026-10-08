# 256foundation/mujina-mips pull request #1: MIP-0001: Configuration and API

> Source: https://github.com/256foundation/mujina-mips/pull/1
> Collected: 2026-10-07
> Published: 2026-05-31

- Repository: 256foundation/mujina-mips
- Type: pull request
- Number: 1
- State: closed
- Author: rkuester
- Opened: 2026-05-31
- Closed: 2026-09-27
- Labels: none

## Description

MIP-0001 sets out the requirements for Mujina's configuration system and REST API: one tree of named nodes unifying defaults, config files, environment variables, command-line arguments, and the API, with values that are readable, subscribable, validated, and persisted across restarts.

This PR is where the document is read and revised, so comments and line suggestions go here. For comfortable reading, the rendered view is easier than the diff: https://github.com/rkuester/mujina-mips/blob/mip-configuration-and-api/mip-0001-configuration-and-api.md

It grew out of reviewing the YAML-configuration PR (256foundation/mujina#36) on [dev call #2](https://forum.256foundation.org/t/mujina-dev-call-2/34) and the earlier "static config file" discussion (https://github.com/256foundation/mujina/discussions/23), which it subsumes.

Please poke holes.


## Comments

### jayrmotta on 2026-07-27

Hey @rkuester, I could work on this next, but since it's a big proposal we could have a series of changes that will take us closer to the vision step by step.

Here's how I see this being introduced incrementally:
1. Replace the current configuration stub with a tree shaped configuration. No cascade, no files, no API exposure, no persistence yet.
2. Implement API reads the tree (read-only). 
3. Read config files and merge them respecting the priority defined in the spec. No writes for now.
4. Introduce in-memory writes over the API so we have parity with the current implementation but also prepares for the persistent config change.
5. Introduce a persist config API to safely write the current values so that they survive across restarts.
6. Introduce websockets to allow config changes subscription, so that clients can observe and react to changes.

We could introduce 1 and 2 together since the only config write we have is to pause/resume mining, and that would be kept as is.

Let me know if I forgot anything. Thoughts?

### rkuester on 2026-07-27

Hey, @jayrmotta. Yes, go for it. I suggest we do it in the context of a concrete feature or two. How about we use pool configuration?

The smaller the PRs, the better. It doesn't have to be one long series with everything in it. Baby steps, and it can grow in place organically.

I've created a tracking issue: https://github.com/256foundation/mujina/issues/83
