# bitaxeorg/ESP-Miner issue #772: default github branch should be the latest released version, not a development version.

> Source: https://github.com/bitaxeorg/ESP-Miner/issues/772
> Collected: 2026-10-07
> Published: 2025-03-14

- Repository: bitaxeorg/ESP-Miner
- Type: issue
- Number: 772
- State: closed
- Author: skot
- Opened: 2025-03-14
- Closed: 2025-03-21
- Labels: bug, documentation, enhancement

## Description

Right now github defaults to the master branch, which we have been using as our latest pre-release branch. I think it would be better if there is a way to make the default branch be what AxeOS shows as the latest released version to avoid confusion.

## Comments

### ghost on 2025-03-14

Here's my thought layout .... 

1/ Master branch
2/ Dev branch (Pre-Release - before going to 1)
3/ PR (Pull requests) - branch (where PR's get added to be tested before going to 2)


1 = Master Branch = Current Release Version - No changes should be made here until a new firmware version is released (see 2 below).

2 = Dev Branch (dev-latest) - contains the PR's that have been added / selected for the next release version after test phase (see below).

3 = PR's submitted (based on dev-latest) - This is the test phase - Any changes / additions are tested and issue(s) fixed before being added / selected to be included in the Dev Branch which will be the next release version when made final.

1 & 3 we have, but 2 is missing.

Currently 3 is being used with 1


### skot on 2025-03-14

This sounds good to me! We don't need to actually create anything for 3) since github allows you to checkout any PR (and yoiu can rebase it on any branch you want)

I'll branch the current master into `dev-latest` and then revert master to the last released tag. (v2.5.1 in this case)

### ghost on 2025-03-14

Yes, just to note here, the Dev Branch (dev-latest) is a copy of the Master Branch + any new PR's added to it for the next new firmware release, ie - Pre-Release Firmware. 


### eandersson on 2025-03-15

I would just go with something simpler. Always merge PRs into the `main` branch, and then create release branches; e.g. 2.6.x and cherry-pick all merges from master into that branch. When you are ready to start planning for 2.7.x you create a new branch based on `main` branch and cherry-pick new commits from `main` as needed.

Similar to how esp-idf does it https://github.com/espressif/esp-idf/branches.

### zcht on 2025-03-15

In professional software development with many changes, feature requests etc. pp, the optimal process always looks like this. 

Master branch: is always the final stable version of an application, ideally tagged (e.g. AxeOS version). 

Develop branch: is always the development branch that contains PRs that have already been successfully tested. 

Each PR should have approximately the following structure, including the commit name:

- An issue is opened and worked on, and a new feature branch is created based on the develop branch. Ideally, the branch should be named as follows: feature/GITHUBISSUEID-meaningful-title
- Each commit in the feature branch MUST look like this to help track the changes: #GITHUBISSUEID: name what was changed, in the message enter in detail what was done and why (if necessary). 
- Before EVERY merge of the feature branch, the developer must rebase the branch with the develop branch and, if necessary, resolve merge conflicts. 

Ideally, a pre-release branch will be created from the develop branch BEFORE the release, where everything that has been added to the develop branch will be tested. Likewise, the functionality of already included features must be guaranteed. 

Unit tests would be helpful for this, as would detailed CI tests, which would catch the worst of it. If everything is in order in the pre-release branch, a release can be made to the master branch. 

At least that is the behavior that has been successfully implemented in many large commercial projects, but also in large open source projects, for years. 

At the moment, unfortunately, I see a really poor structure of commits, as well as decisions about whether or not to merge a PR, but the test routines are also not quite optimal. 


if we were to clarify this using this example:

This issue has an ID#772, so the structure of the fix/feature request would look like this. 

```
/master
/develop
/feature/772-default-github-branch
/feature/123-fanzy-new-stuff
/feature/321-fanzy-new-stuff
```

the _/feature/772-default-github-branch_ is a branch from **/develop**

when a commit is made, it looks like this: 

> “#772: adjusting the default branch in xyz”

As you can see, github even automatically links from the issue ID if you implement it that way. 

The advantage of having the issue ID in the commit is that you can quickly jump to the issue in the branch and thus find documented communication, test instructions and problems. This makes administration and further development much easier and significantly increases the quality of development. 


### ghost on 2025-03-15

To add to my post above with the steps and how it should work

![Image](https://github.com/user-attachments/assets/8895fc5f-f3c1-43f9-b43d-0824ece23efe)
