# Contributing and Mujina Improvement Proposals

> Sources: Mujina project (mujina.org community page), collected 2026-10-07; 256 Foundation (mujina-mips GitHub README), collected 2026-10-07; 256 Foundation (mujina GitHub README), collected 2026-10-07; 256 Foundation forum (Mujina Dev Call), 2026-05-03; 256 Foundation forum (Mujina Dev Call #2), 2026-05-05; 256 Foundation forum (Mujina Dev Call #4), 2026-06-08
> Raw: [mujina.org community](../../raw/mujina/mujina-org-community.md); [mujina-mips README](../../raw/mujina/github-256foundation-mujina-mips.md); [mujina README](../../raw/mujina/github-256foundation-mujina.md); [Dev Call 1](../../raw/mujina/2026-05-03-forum-mujina-dev-call.md); [Dev Call 2](../../raw/mujina/2026-05-05-forum-mujina-dev-call-2.md); [Dev Call 4](../../raw/mujina/2026-06-08-forum-mujina-dev-call-4-20260615.md)
> Updated: 2026-10-07

## Overview

[Mujina](mujina-firmware.md) is built in public by software and hardware engineers, protocol authors and mining operators. Work happens on GitHub, with the forum and Telegram as side channels. Bugs and ideas start as GitHub discussions. Large design questions become a MIP, a Mujina Improvement Proposal, which is a design document reviewed as a pull request. The first one, MIP-0001, covers the configuration system and REST API.

## Where things happen

- **GitHub:** the source, issues and pull requests. The first dev call named GitHub as the preferred place, in the closest issue, PR or discussion.
- **GitHub Discussions:** questions, ideas and bug triage. The community page says to start here if you are not sure where something belongs.
- **The 256 Foundation forum:** longer threads, and user-oriented discussion and support.
- **Telegram:** real-time chat. The README notes that Telegram is ephemeral, and that decisions and important context belong on GitHub.
- **Dev calls:** regular public calls. See [Mujina Dev Calls](mujina-dev-calls.md).

## How a contribution moves

The first dev call set out the flow:

- Possible bugs start in discussions, get triaged, and are promoted to issues.
- Simple fixes go straight to a PR.
- Prospective features start in discussions, then become draft PRs.
- PRs stay in draft until the author is ready for review and merge.
- PRs should contain one or more small, atomic commits, so the history reads as clear, reviewable steps.

The community page gives the same entry points. For a bug, search existing issues and discussions, then open an Issue Triage discussion. For an idea, open a discussion in the Ideas category before writing code. Every open issue is ready to work on, and issues tagged "good first issue" suit newcomers. The contribution guide in the repository is the canonical reference. The README also points to a code style guide and coding guidelines.

## Skills the project needs

The community page says the project needs more than Rust:

- Board bring-up needs embedded and hardware people, ideally with the board in hand.
- Most ASIC protocol work needs reverse engineers.
- The docs and the website need writers.
- Every driver needs testers with hardware.

No ASIC is needed to start, because the CPU backend runs the whole system. See [Running Mujina](running-mujina.md).

## Mujina Improvement Proposals

A MIP is a design document for a substantial change to Mujina. It is for an area too big to settle in a discussion thread. The idea follows Bitcoin's BIPs and Nostr's NIPs. MIPs live in the mujina-mips repository.

Most ideas start as a GitHub discussion and stay there, where the thread is the record. A few need a document that people will edit and refer back to. Those become MIPs.

The process has two steps:

1. Start in Discussions. Every MIP begins as a discussion, so ideas are seen as they emerge and nobody has to watch the MIP repo.
2. When it needs a document, open a pull request in mujina-mips adding `mip-NNNN-title.md`, and link it from the discussion. The PR is where the document is read and revised.

The README says process beyond that is "intentionally light for now".

## MIP-0001: configuration system and REST API

At Dev Call #2 the group debated how config should persist, and Ryan took the action to write up a design. On 2026-05-31 he reported it done. It had grown into a full set of requirements for Mujina's configuration system and REST API, written up as MIP-0001, the first MIP. He described MIPs then as "a new lightweight design-doc convention".

- The intro thread is GitHub discussion 57, "Configuration system and REST API".
- The MIP itself was opened as pull request 1 in mujina-mips, where review and comments should happen.
- Before Dev Call #4, Ryan reminded attendees to bring their opinions on that discussion.

The text of MIP-0001 is not in `raw/`. The design points raised on the call are in [Mujina Dev Calls](mujina-dev-calls.md).

## The website

The mujina.org site has its own repository and takes pull requests. Every page ends with an edit link. The compatibility matrix depends on the community: whoever maintains a fork or a board driver is asked to keep its row accurate. See [Mujina Hardware Compatibility](hardware-compatibility.md).

## Funding and license

Mujina is run and funded by the 256 Foundation. It takes no donations of its own. To support the work, support the foundation (see [Grants and Funding](../foundation/grants-and-funding.md)). Mujina is licensed under the GNU General Public License v3.0 or later.

## See Also

- [Mujina Firmware](mujina-firmware.md)
- [Mujina Dev Calls](mujina-dev-calls.md)
- [Running Mujina](running-mujina.md)
- [Mujina Hardware Compatibility](hardware-compatibility.md)
- [256 Foundation: Mission and Organization](../foundation/mission-and-organization.md)
