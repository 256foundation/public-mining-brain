# 256foundation/mujina pull request #109: build(deps): use cargo's own min-publish-age and gate PRs on it

> Source: https://github.com/256foundation/mujina/pull/109
> Collected: 2026-10-07
> Published: 2026-09-04

- Repository: 256foundation/mujina
- Type: pull request
- Number: 109
- State: closed
- Author: rkuester
- Opened: 2026-09-04
- Closed: 2026-09-04
- Labels: none

## Description

Move the dependency cooldown into cargo and gate pull requests on it.

Cargo's own `min-publish-age` setting ([RFC 3923]) now holds every crate release back for seven days before it may enter `Cargo.lock`, set in `.cargo/config.toml`. It is nightly-only until cargo 1.100, the next stable release, so the `deps` recipes run `cargo +nightly` for now. cargo-cooldown and `cooldown.toml` go away: it skipped the cooldown for a single-crate update because it read the crate name as a workspace selector (dertin/cargo-cooldown#23), and it could not cover a plain `cargo update`.

[RFC 3923]: https://rust-lang.github.io/rfcs/3923-cargo-min-publish-age.html

A new pull-request job, "Check dep cooldown", fails when the lock gains a crates.io version younger than the window relative to the base branch. The script reads publish times from cargo's local index cache and never opens a connection of its own; `just check-dep-cooldown` runs it locally. A young version that has to go in, such as a security fix, fails the job and a maintainer merges with the reason in the pull request.

CONTRIBUTING.md documents the related workflows.

Parts of this scheme are inspired by Mullvad's mullvad/mullvadvpn-app#10798: a check of the versions added by a pull request, and `pubtime` from the crates.io index used. We make a few improvements: reading cargo's local cache  instead of reading the index via the network, avoiding an allowlist, running inside our build container, and having unit tests.

### Follow-up

When cargo 1.100 is released: drop the `[unstable]` table and the `+nightly` from the `deps` recipes, require 1.100 through `rust-toolchain.toml`, and move the CI image to the 1.100 tag. An issue will track it.


## Comments

### SusanGithaigaN on 2026-10-02

As per the last discussion in #115, you mentioned that this PR is still open to review. When working on #118, I came across this error when I ran `just checks`. I tested on the PR branch and on main, and still got the same error:

**Environment:** Python 3.10.12, Ubuntu 22.04.5 LTS

```
susan@susan-githaiga:~/development/open-source/mujina$ just checks
cargo fmt --check
cargo clippy --release --locked -- -D warnings
    Finished `release` profile [optimized] target(s) in 0.58s
python3 -B -m unittest discover -s scripts -p '*_test.py'
E......
======================================================================
ERROR: check_dep_cooldown_test (unittest.loader._FailedTest)
----------------------------------------------------------------------
ImportError: Failed to import test module: check_dep_cooldown_test
Traceback (most recent call last):
  File "/usr/lib/python3.10/unittest/loader.py", line 436, in _find_test_path
    module = self._get_module_from_name(name)
  File "/usr/lib/python3.10/unittest/loader.py", line 377, in _get_module_from_name
    __import__(name)
  File "/home/susan/development/open-source/mujina/scripts/check_dep_cooldown_test.py", line 26, in <module>
    check_dep_cooldown = load_script()
  File "/home/susan/development/open-source/mujina/scripts/check_dep_cooldown_test.py", line 22, in load_script
    loader.exec_module(module)
  File "/home/susan/development/open-source/mujina/scripts/check-dep-cooldown", line 24, in <module>
    import tomllib
ModuleNotFoundError: No module named 'tomllib'


----------------------------------------------------------------------
Ran 7 tests in 0.004s

FAILED (errors=1)
error: recipe `test-scripts` failed on line 31 with exit code 1
```
<br>

**Cause:** [`scripts/check-dep-cooldown` line 24](https://github.com/256foundation/mujina/blob/main/scripts/check-dep-cooldown#L24), added in this PR, imports `tomllib`, which has only been in the standard library since Python 3.11. 

**Same bug, another setup:** #119 reports the same missing `tomllib` error with Python 3.9 from macOS Xcode. CONTRIBUTING.md doesn't list Python yet, and the default `python3` on both Ubuntu 22.04 (3.10) and the macOS Xcode tools (3.9) is older than 3.11.

Documenting the requirement helps people set up correctly, but on its own it doesn't change the behavior: on 3.10, `just checks` still fails with the same error. As I see it, there are two options:


1. **Support older Python versions** by falling back to `tomli` when `tomllib` isn't available. This adds `tomli` as a dev dependency below 3.11, and CONTRIBUTING would still need a note so contributors know to install it

2. **Require 3.11+ and enforce it.** Add a version check (in the script or the `test-scripts`), so that contributors see "Python 3.11+ required" instead of a `ModuleNotFoundError`. This adds no dependency.

---
Which direction would you prefer?
