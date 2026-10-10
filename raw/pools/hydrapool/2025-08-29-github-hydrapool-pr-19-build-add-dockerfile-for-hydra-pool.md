# 256foundation/hydrapool pull request #19: build: add dockerfile for Hydra-Pool

> Source: https://github.com/256foundation/hydrapool/pull/19
> Collected: 2026-10-07
> Published: 2025-08-29

- Repository: 256foundation/hydrapool
- Type: pull request
- Number: 19
- State: closed
- Author: adamdecaf
- Opened: 2025-08-29
- Closed: 2025-10-23
- Labels: none

## Description

<details>
<summary>Docker build</summary>

```
$ docker build -t hydrapool-server -f docker/Dockerfile.hydrapool . 
[+] Building 0.4s (16/16) FINISHED                                                                                           docker:orbstack
 => [internal] load build definition from Dockerfile.hydrapool                                                                          0.0s
 => => transferring dockerfile: 838B                                                                                                    0.0s
 => [internal] load metadata for docker.io/library/rust:1.89-slim-bookworm                                                              0.2s
 => [internal] load metadata for docker.io/library/debian:stable-slim                                                                   0.2s
 => [internal] load .dockerignore                                                                                                       0.0s
 => => transferring context: 136B                                                                                                       0.0s
 => [builder 1/6] FROM docker.io/library/rust:1.89-slim-bookworm@sha256:21e2ac30e72a6d5b6d667b573eadad0578be9a5a99bac0b2b99b3d37795f90  0.0s
 => [stage-1 1/4] FROM docker.io/library/debian:stable-slim@sha256:8810492a2dd16b7f59239c1e0cc1e56c1a1a5957d11f639776bd6798e795608b     0.0s
 => [internal] load build context                                                                                                       0.0s
 => => transferring context: 117B                                                                                                       0.0s
 => CACHED [stage-1 2/4] WORKDIR /app                                                                                                   0.0s
 => CACHED [builder 2/6] RUN apt-get update && apt-get install -y --no-install-recommends     libbsd-dev     build-essential     pkg-c  0.0s
 => CACHED [builder 3/6] WORKDIR /usr/src/app                                                                                           0.0s
 => CACHED [builder 4/6] COPY Cargo.toml Cargo.lock ./                                                                                  0.0s
 => CACHED [builder 5/6] COPY src ./src                                                                                                 0.0s
 => CACHED [builder 6/6] RUN cargo build --release                                                                                      0.0s
 => CACHED [stage-1 3/4] COPY --from=builder /usr/src/app/target/release/hydrapool /app/hydrapool                                       0.0s
 => CACHED [stage-1 4/4] RUN apt-get update && apt-get install -y --no-install-recommends     libbsd0     libzstd1     ca-certificates  0.0s
 => exporting to image                                                                                                                  0.0s
 => => exporting layers                                                                                                                 0.0s
 => => writing image sha256:c1da28a31b1beade73d8b7eb9c5bc9443db5b2b32a8af6776bd9cb6e41f04879                                            0.0s
 => => naming to docker.io/library/hydrapool-server                                                                                     0.0s
```

</details>

<details>
<summary>Running</summary>

```
$ docker run -it -v $(pwd)/config.toml:/etc/hydrapool/config.toml hydrapool-server --config /etc/hydrapool/config.toml 
$ echo $?
1
```

</details>

I don't have ckpool, etc running so the failure is probably from hydrapool being unable to connect. Maybe we need some logging to indicate that? 

Also, it looks like CI only runs on commits to `main` and tags, so CI won't test this PR. IMO we should be building docker images on every PR so they stay updated / working. 

Fixes: https://github.com/256-Foundation/Hydra-Pool/issues/14 

## Comments

### pool2win on 2025-10-23

Hi @adamdecaf - thanks for digging into this. I totally missed the alerts about this in my emails.

We are have moved from ckpool and are no longer using docker for running the pool. Instead we are going to ship prebuilt binaries so that admins can download a binary and run the pool - or build from source as they wish.

We will keep docker for running a new prometheus based dashboard for pool and user hashrate.

We have updated the README with the installer based instructions.

Once again, thanks for digging into the problems and helping with the docker fixes. Maybe you'll find the new process easier.

### adamdecaf on 2025-10-23

No worries. I heard about the switch on the 256 podcast. Docker is useful for running the binary in cloud environments, umbres, etc so I'd suggest offering a scratch + binary image. 

I'll keep an eye out for other issues I can tackle. I'm not very familiar with rust.
