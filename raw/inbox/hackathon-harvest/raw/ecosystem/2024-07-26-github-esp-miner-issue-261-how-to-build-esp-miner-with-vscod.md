# bitaxeorg/ESP-Miner issue #261: How to build esp-miner with VSCode in Devcontainer?

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/261
> Collected: 2026-10-07
> Published: 2024-07-26

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 261
- State: closed
- Author: pixeldoc2000
- Opened: 2024-07-26
- Closed: 2024-07-31
- Labels: none

## Description

As discussion is not enabled, I have to create an issue for this.

I am trying to build current esp-miner master on Windows with VSCode in Devcontainer.

This is what I did:

1. Clone master
2. Open master with VSCode
3. Let VSCode start Devcontainer in Docker on WSL2
4. Select ESP-IDF 5.4.0 (looks like the project is supposed to build with ESP-IDF 5.1.x ?)
5. Start bash in Devcontainer to install missing stuff:
```
idf_tools.py install-python-env

curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg

NODE_MAJOR=18
echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list

apt-get update

apt-get install nodejs
```
6. Build in Devcontainer
7. Flash esp-miner.bin via Webinterface, Answer from Webserver: `Validation / Activation Error`

I was not able to successfully build with ESP-IDF 5.1.2 or ESP-IDF 5.2.x

It looks like there was some Info about building esp-miner in readme, but not anymore or outdated?

What am I doing wrong, or can it only be flashed via UART?

## Comments

### pixeldoc2000 on 2024-07-26

Only realized now there are current dev builds available in GitHub actions: https://github.com/skot/ESP-Miner/actions/
