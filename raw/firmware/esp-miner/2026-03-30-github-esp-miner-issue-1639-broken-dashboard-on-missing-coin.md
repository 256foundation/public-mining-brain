# bitaxeorg/ESP-Miner issue #1639: Broken dashboard on missing coinbase outputs

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/1639
> Collected: 2026-10-07
> Published: 2026-03-30

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 1639
- State: closed
- Author: johnnyasantoss
- Opened: 2026-03-30
- Closed: 2026-04-24
- Labels: question

## Description

**Describe the bug**
When connecting to sv2-translator proxy it fails to show dashboard. Looking at the console logs it shows an error trying to access `length` in `coinbaseOutputs`.

**To Reproduce**
Steps to reproduce the behavior:
1. Connected to stratumv2-translator proxy (sv1->sv2) using sv2-ui
2. Look at the dashboard

**Expected behavior**
Show normal stats

**Screenshots & Photos**

<img width="1243" height="644" alt="Image" src="https://github.com/user-attachments/assets/b7213ce4-c27b-42f0-b850-96f1ece84dac" />

**Hardware (please complete the following information):**
 - Bitaxe HW version: Gamma 601
 - Bitaxe HW vendor: SoloSatoshi
 - ESP-Miner FW version: 2.13.1
 - Hash Frequency: 490 MHz
 - Voltage: 1060 mV
 - Pool URL, Port, User: local

**Additional context**



## Comments

### mutatrum on 2026-03-30

Can you test with #1634?

### WantClue on 2026-04-20

any feedback @johnnyasantoss ? 

### johnnyasantoss on 2026-04-22

I tried building from the PR #1634 but it failed to build.
```
[3/57] Completed 'bootloader'
FAILED: openapi_generate.stamp /workspace/build/openapi_generate.stamp
cd /workspace/main/http_server/axe-os && /usr/bin/npm i && /usr/bin/npm run generate:api && /opt/esp/tools/cmake/3.30.2/bin/cmake -E touch /workspace/build/openapi_generate.stamp
ninja: build stopped: subcommand failed.
ninja failed with exit code 1, output of the command is in the /workspace/build/log/idf_py_stderr_output_12226 and /workspace/build/log/idf_py_stdout_output_12226
```

### johnnyasantoss on 2026-04-22

Building on `master` also failed

### mutatrum on 2026-04-22

Delete `sdkconfig` and run `idf.py set-target esp32-s3`, for a full rebuild.

### johnnyasantoss on 2026-04-23

it still fails with the following error on the devcontainer:
```
Error: /bin/sh: 1: java: not found

    at /workspace/main/http_server/axe-os/node_modules/@openapitools/openapi-generator-cli/main.js:2:49316
    at ChildProcess.exithandler (node:child_process:424:5)
    at ChildProcess.emit (node:events:519:28)
    at maybeClose (node:internal/child_process:1101:16)
    at Socket.<anonymous> (node:internal/child_process:456:11)
    at Socket.emit (node:events:519:28)
    at Pipe.<anonymous> (node:net:346:12)
```

after installing `apt install default-jdk-headless` it did work.

Flashed (with a bit a of trouble with regards to merging the bin, maybe my fault for not fully reading the docs) and installed.

Now it works!!

### johnnyasantoss on 2026-04-23

Thank you! @mutatrum 

/cc @plebhash FYI

### plebhash on 2026-04-23

what was the root cause?

or more specifically, I'm curious to know what about sv2-translator behavior was breaking things on ESP-miner?

### johnnyasantoss on 2026-04-24

> what was the root cause?

from what I understood from the PR diff it seems to be missing (js undef) some expected structure in the coinbase tx. I can't really confirm as I don't have full picture of this codebase. Maybe @mutatrum can shine some light here.

### mutatrum on 2026-04-24

#1634 made the coinbase card display on the dashboard more defensive. Before it assumed some fields were available, which wasn't correct and made the dashboard not show up.

Sidenote: the java requirement will be dropped at some point in the future with #1597. Currently, master should already be buildable without java installed.

### johnnyasantoss on 2026-04-25

@mutatrum will this be released soon? Ty for the fix
