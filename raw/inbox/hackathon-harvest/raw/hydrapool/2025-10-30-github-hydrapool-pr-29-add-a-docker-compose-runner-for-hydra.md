# 256foundation/hydrapool pull request #29: Add a docker compose runner for hydrapool's stack

> Source: https://github.com/256foundation/hydrapool/pull/29
> Collected: 2026-10-07
> Published: 2025-10-30

- Repository: 256foundation/hydrapool
- Type: pull request
- Number: 29
- State: closed
- Author: pool2win
- Opened: 2025-10-30
- Closed: 2025-10-30
- Labels: none

## Description

- Build hydrapool optimised docker image
- Build prom and grafana images for moving configs in there
- Hydrapool config.toml is mounted, so user can provide a new config. Otherwise the defaults from the hydrapool image are used.
- Add github workflow to build images for docker. Once this is done, I'll edit compose file to not build the image, but use the latest or corresponding version one.
- Since this PR is a giant blob, also adding changelog in this PR :)
