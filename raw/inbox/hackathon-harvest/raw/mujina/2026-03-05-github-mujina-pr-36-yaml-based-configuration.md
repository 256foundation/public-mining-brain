# 256foundation/mujina pull request #36: yaml based configuration

> Source: https://github.com/256foundation/mujina/pull/36
> Collected: 2026-10-07
> Published: 2026-03-05

- Repository: 256foundation/mujina
- Type: pull request
- Number: 36
- State: open
- Author: jbride
- Opened: 2026-03-05
- Closed: n/a
- Labels: none

## Description

Details of implementation can be found [here](https://github.com/jbride/mujina/blob/config/docs/configuration.md).

## Comments

### jayrmotta on 2026-03-10

Hey @jbride, good job with the pull request mate! I wish GitHub would allow me to submit a proper review, so I'll do it with comments for now.

Found an issue with the CPU miner config:

```
▪ MUJINA__DAEMON__LOG_LEVEL=debug \
MUJINA__API__LISTEN=0.0.0.0:7785 \
MUJINA__POOL__URL=stratum+tcp://public-pool.io:3333 \
MUJINA__POOL__USER=myuser \
MUJINA__POOL__PASSWORD=mypassword \
MUJINA__BACKPLANE__USB_ENABLED=false \
MUJINA__BOARDS__CPU_MINER__ENABLED=true \
MUJINA__BOARDS__CPU_MINER__THREADS=4 \
cargo run -p mujina-miner --bin mujina-minerd
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.24s
     Running `target/debug/mujina-minerd`
09:07:16 INFO  daemon: USB discovery disabled (backplane.usb_enabled = false)
09:07:16 INFO  daemon: CPU miner enabled
               threads=4, duty=50
09:07:16 INFO  daemon: Started.
09:07:16 INFO  daemon: For debugging, set RUST_LOG=mujina_miner=debug or trace.
09:07:16 INFO  backplane: CPU miner board connected.
               board=CPU Miner, threads=4, duty=50
09:07:16 INFO  job_source::stratum_v1: Waiting for hash threads before connecting
               pool=stratum+tcp://public-pool.io:3333
09:07:16 ERROR backplane: Failed to create CPU miner board
               board=CPU Miner, error=Configuration error: CPU miner not configured (MUJINA_CPU_MINER not set)
09:07:16 INFO  api::server: API server listening.
               url=http://0.0.0.0:7785
09:07:16 WARN  api::server: API server is bound to a non-localhost address (0.0.0.0). This exposes the API to the network without authentication.
^C09:07:21 INFO  daemon: Received SIGINT.
09:07:21 INFO  scheduler: Mining status.
               uptime=5s, hashrate=--, shares=0
09:07:21 INFO  daemon: Exiting.
```

I asked my LLM to provide a fix and then it provided [this solution](https://github.com/user-attachments/files/25869195/mujina-rs-changes.patch), maybe you want to port it to your branch.


### jayrmotta on 2026-03-10

Another improvement would be replacing or removing references to the old environment variables. Found instances on the following files:

- docs/api.md
- mujina-miner/src/cpu_miner/config.rs
- mujina-miner/src/cpu_miner/mod.rs
- .github/DISCUSSION_TEMPLATE/issue-triage.yml
- docs/cpu-mining.md
- mujina-miner/src/bin/cli.rs
- README.md
- mujina-miner/src/bin/minerd.rs
- mujina-miner/src/stratum_v1/client.rs
- docs/container.md

Some of the mentions are in the context of explaining this PR's changes but some are just residue, if left like that it might confuse and misinform future developers.

### jayrmotta on 2026-03-10

nit: Maybe we should find ways to avoid committing real config files by accident and leaking secrets? For one we could add `mujina.yaml` to .gitignore.

### jayrmotta on 2026-03-19

Hey @jbride, following up to see if you will continue with this implementation? I think this would be really useful. 

If you want to make me a contributor in your fork I can amend/add the fixes and improvements there as well.

### rkuester on 2026-03-19

I realize it would be helpful if I took a look at this sooner rather than later. Thanks for your patience!

### jbride on 2026-04-16

Sorry about the delay.
Thanks for the feedback.
I'll get on it.

### jbride on 2026-04-16

Hey @jayrmotta .
Please take a look at the latest.
Thanks again for the review.
Now synced with latest in main branch.

### jbride on 2026-04-22

@jayrmotta Sounds good.  The following is a summary of changes with the latest commit:

- Remove unimplemented BitaxeConfig and HashThreadConfig from config
  struct and example YAML
- Drop MUJINA_CONFIG_FILE_PATH and MUJINA_DEFAULT_CONFIG_PATH bootstrap
  env vars; config file path is now CLI-only via --config
- Replace named CLI flags (--pool-url, --log-level, etc.) with a
  generic --set key=value flag using the same dot-path namespace as
  the YAML config, giving full coverage without coupling CLI names
  to internal struct fields
- Update integration tests, docs, and example YAML to match

### jbride on 2026-04-29

Hello @jayrmotta .   Any other suggestions you may have before @rkuester reviews this PR ?

### jayrmotta on 2026-05-02

Hey @jbride! Sorry it took me long to answer, been a bit hectic over here.

At this point I would also like a third person to run and review it. Looking forward to having this in the main branch.

### jbride on 2026-05-03

Thanks @jayrmotta .
@rkuester :  please review and provide feedback.  thank you.

### average-gary on 2026-05-18

From dev call: @rkuester to write up feedback so there are specifics on config design to discuss 

### rkuester on 2026-05-31

Thanks for all the work here, @jbride, and for your patience through the back-and-forth. Thanks @jayrmotta too for the careful testing and review along the way.

Digging into this PR on [dev call #2](https://forum.256foundation.org/t/mujina-dev-call-2/34) is what made me realize we should pin down what we actually want from configuration before reviewing an implementation line by line. That's the "write up config design specifics" item from the call. I've now done that, written up as MIP-0001, the first Mujina Improvement Proposal:

https://github.com/256foundation/mujina-mips/pull/1

(Also introduced in an Ideas discussion, #57, for anyone following along there.)

A couple of things worth saying. The requirements are a draft for discussion, not a spec to go implement, and I'd much rather you and @jayrmotta poke holes in them first, so comments and line suggestions on that PR are very welcome, especially where they conflict with what you ran into building this. And since this PR is the reason the requirements exist and remains a valuable reference for them, I'd like to keep it open while we converge on them rather than do a line-by-line review right now.

Once we're agreed on the requirements, let's plan the implementation together. They reach beyond what this PR set out to do (runtime changes made through the API and persisted, live subscriptions to changes, etc.), so the realistic shape is an incremental path rather than one big change, and this PR is a strong starting point for that.

Please don't read any of this as the work being tossed. It's the opposite. My next step is walking the dev-call group through the requirements for review, and I'd like to have you both in that.
