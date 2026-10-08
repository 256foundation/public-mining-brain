# 256foundation/hydrapool: packages/README.adoc

> Source: https://github.com/256foundation/hydrapool/blob/HEAD/packages/README.adoc
> Collected: 2026-10-07
> Published: Unknown

= Packaging for Hydrapool

== Supported packages:

. Debian

= Debian Build Locally Using Docker

== Build docker image

This image runs cargo build --release so that later we use the image
only to build the package.

`docker build -f packages/Dockerfile.debian -t debian-build-hydrapool-package .`

== Build package

`docker run --volume ./:/hydrapool/target debian-build-hydrapool-package`
