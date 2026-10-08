# bitaxeorg/ESP-Miner issue #104: esp-miner API needs Documentation

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/104
> Collected: 2026-10-07
> Published: 2024-02-06

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 104
- State: closed
- Author: mroxso
- Opened: 2024-02-06
- Closed: 2024-03-22
- Labels: documentation, help wanted, good first issue

## Description

Hey y'all.
My first Bitaxe (202 Board) has booted up the first time and it works great!

Now:
I wanted to do some stuff with the API. (Seems like it has some?)
But I couldn't find any documentation about it.
Is there no documentation?

## Comments

### github-block on 2024-02-07

You can check your miners using the following API:
http://bitaxe-ip-addr/api/system/info


### thalpius on 2024-02-07

I don't think it's documented, but it's easy to figure out what requests it support by checking the code:
https://github.com/skot/ESP-Miner/blob/23599cf46f3668af58d252915b347fa14eedd8cf/main/http_server/http_server.c

Or use the developer tools and see what requests are sent when using the UI. Documentation would be great though. Creating a PR and adding it to the readme would be great.

### skot on 2024-02-07

This is a great feature request for someone to contribute to the project!

I think the readme is a good place for the API documentation.

### mroxso on 2024-02-08

Thank you!
Maybe I will document it when I have some free time for it!

### avylera on 2024-02-15

Hello, I would love to contribute to this project by documenting the API. 

### Mithun-1431 on 2024-02-21

Hi, I also like contributing to the project. Please reach out.

### mroxso on 2024-03-14

I created a Pull Request. Feel free to comment and/or contribute
#135
