# 256foundation/hydrapool pull request #33: add start9 package

> Source: https://github.com/256foundation/hydrapool/pull/33
> Collected: 2026-10-07
> Published: 2025-11-06

- Repository: 256foundation/hydrapool
- Type: pull request
- Number: 33
- State: open
- Author: Georges760
- Opened: 2025-11-06
- Closed: n/a
- Labels: none

## Description

to be tested

## Comments

### LocoSlug on 2025-11-06

If appropriate, I would like to suggest adding the config option pplns_ttl_days. Thanks in advance. 

### pool2win on 2025-11-18

Hi @Georges760 thanks for taking the time to work on the start9 package. It is much needed.

Caveat: I have never built a start9 package, so it is really nice you are helping us out here. Also, sorry for not seeing this earlier. I wasn't monitoring telegram.

Couple of big overall points:

1. We have docker files in the docker folder. We actually have a github action that builds them an include the docker images in the releases. Is there no to reuse those docker images? That was kind of my hope that we can take those images from ghcr.io and use them for start9/umbrel etc.
2. I am not a nix user, can we avoid depending on nix? It will just take me a LOT of effort to try and run things locally and testing them before we can merge things.

Regarding the dockerfiles, if the issue is that we need entrypoints in a certain way, can we build images for s9 are simple wrapper around the release images? I want to avoid having to maintain multiple docker files for the same service.

### Georges760 on 2025-11-19

Nix is not a hard requirement, the flake i added is just for nix user to have a build setup in no time. Any other user (like you) can continue building on their system as you do currently. (I am on NixOS so I hd to do this nix flake in order to build hydrapool, so I commited them to to let other nix users profit from them too).

As of start9, I never did a pkg neither. It is my first one, and i largely abused vibe coding instead of reading properly the documentation for it. I beleive it is based on the 3 docker images you made. My current undersatnding is that the real start9 SDK should be installed on the build system and then my code should allow to build the packages. It is currently using a stub for this SDK.
I guess we need someone who actually knows about start9 packages and tell us if my PR is usefull or not.

### pool2win on 2025-11-20

Yeah, I agree. At least maybe have a start9 device around so we can properly test everything works too.

If you do want to share nix stuff, it might be an idea to have a separate PR for nix only. Or, I think @econoalchemist won't mind if we did a brand new repo called hydrapool-nix where we have the nix setup of hydrapool. 

### Georges760 on 2025-11-20

i can make a separate PR for Nix user support to build HydraPool.

There is no need a of a new repo, the nix flake are highly dependant on the project to be build, so usually they live in the same repo. It is like the docker build, they are not mandatory to build the pool project itself. But user wanting to use them can.

### pool2win on 2025-11-20

OK. Lets do that. Let's put things in a nice clean separate directory with
a README. Thanks again for doing this.

On Thu, 20 Nov 2025 at 17:47, Georges ***@***.***> wrote:

> *Georges760* left a comment (256foundation/hydrapool#33)
> <https://github.com/256foundation/hydrapool/pull/33#issuecomment-3559051585>
>
> i can make a separate PR for Nix user support to build HydraPool.
>
> There is no need a of a new repo, the nix flake are highly dependant on
> the project to be build, so usually they live in the same repo. It is like
> the docker build, they are not mandatory to build the pool project itself.
> But user wanting to use them can.
>
> —
> Reply to this email directly, view it on GitHub
> <https://github.com/256foundation/hydrapool/pull/33#issuecomment-3559051585>,
> or unsubscribe
> <https://github.com/notifications/unsubscribe-auth/ASU3SYNHYYXGPGWBRZJEW5T35XWDFAVCNFSM6AAAAACLK4FXSWVHI2DSMVQWIX3LMV43OSLTON2WKQ3PNVWWK3TUHMZTKNJZGA2TCNJYGU>
> .
> You are receiving this because you commented.Message ID:
> ***@***.***>
>


### Georges760 on 2026-02-14

Removed any NixOS specific. Only the Start9 package build.

I can't test it on my start9 for now as it is down for a while. But it build fine.

### pool2win on 2026-02-16

> Removed any NixOS specific. Only the Start9 package build.
> 
> I can't test it on my start9 for now as it is down for a while. But it build fine.

Nice! Should we ask anyone on osmu discord to test the build for you?
