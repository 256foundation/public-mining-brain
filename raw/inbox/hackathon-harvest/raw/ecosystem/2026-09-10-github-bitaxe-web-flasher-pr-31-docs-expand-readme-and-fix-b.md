# bitaxeorg/bitaxe-web-flasher pull request #31: docs: expand readme and fix broken Discord badge

> Source: https://github.com/bitaxeorg/bitaxe-web-flasher/pull/31
> Collected: 2026-10-07
> Published: 2026-09-10

- Repository: bitaxeorg/bitaxe-web-flasher
- Type: pull request
- Number: 31
- State: open
- Author: SurefireStudios
- Opened: 2026-09-10
- Closed: n/a
- Labels: none

## Description

`+121 / -1`; the single deleted line is the broken Discord badge, and every other line is preserved word for word.

## The Discord badge is dead

`dcbadge.vercel.app` has been taken down and returns 404, so the first thing at the top of the readme is a broken image.

Repointed at `dcbadge.limes.pink`, the maintained successor, with the same invite code — verified rendering as *Open Source Miners United: 13057 MEMBERS*.

## The browser requirement wasn't documented

This is the change I'd most encourage taking: the flasher calls `navigator.serial.requestPort()`, so it only works in Chromium-based browsers.

The app already says so at runtime via `errors.browserCompatibility`, but the readme didn't, so a Firefox or Safari user found out only after connecting hardware.

There's now a Requirements section stating it up front, with the reminder that a charge-only USB cable won't work.

## Supported devices

A table of all 11 devices and their board versions, read from `src/components/firmware_data.json`, so someone can check their board revision without opening the app.

## Everything else added

The seven-step usage flow, taken from `src/i18n/locales/en.json` so it matches what the UI shows rather than drifting from it.

That firmware versions are fetched live from GitHub releases with drafts and pre-releases filtered out, and what **Keep configuration** does.


## Comments

### coderabbitai[bot] on 2026-09-10

<!-- This is an auto-generated comment: summarize by coderabbit.ai -->
<!-- review_stack_entry_start -->

<a href="https://app.coderabbit.ai/change-stack/bitaxeorg/bitaxe-web-flasher/pull/31#gh-light-mode-only"><img src="https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg" alt="Review Change Stack" width="202" height="32"></a><a href="https://app.coderabbit.ai/change-stack/bitaxeorg/bitaxe-web-flasher/pull/31#gh-dark-mode-only"><img src="https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui-dark.svg" alt="Review Change Stack" width="202" height="32"></a>

<!-- review_stack_entry_end -->
<!-- walkthrough_start -->

<details>
<summary>📝 Walkthrough</summary>

## Walkthrough

The README was expanded with project branding, requirements, usage instructions, supported devices, features, development commands, technology details, deployment information, contribution guidance, community links, and license information.

### Changes

**README documentation**

|Layer / File(s)|Summary|
|---|---|
|**Project overview and usage** <br> `readme.md`|The README adds a centered project header, badges, browser and cable requirements, usage steps, firmware version notes, and configuration behavior.|
|**Supported devices and features** <br> `readme.md`|The README adds supported device and firmware repository tables, feature details, and a documentation link.|
|**Development and project information** <br> `readme.md`|The README documents local npm commands, the technology stack, GitHub Pages deployment, contribution steps, community details, and the GPLv3 license.|

**Estimated code review effort:** 1 (Trivial) | ~5 minutes

</details>

<!-- walkthrough_end -->
<!-- final_review_risk_start -->
**Merge Risk:** _🔵 Low_ · up to `0368e`
<!-- final_review_risk_coverage:{"sourceCommitId":"0368eaa515029f2c7b2f496a94967b9259df47a6","coveredCommitId":"0368eaa515029f2c7b2f496a94967b9259df47a6","kind":"reviewed"} -->

The README is usable, but its heading structure and browser-support table have minor accessibility issues, and one feature label needs wording cleanup. Since no runtime behavior changed, the PR remains low risk and mergeable with bounded documentation follow-up.
<!-- final_review_risk_end -->
<!-- pre_merge_checks_walkthrough_start -->

<details>
<summary>🚥 Pre-merge checks | ✅ 5</summary>

<details>
<summary>✅ Passed checks (5 passed)</summary>

|         Check name         | Status   | Explanation                                                                                                                                                                                               |
| :------------------------: | :------- | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|     Docstring Coverage     | ✅ Passed | No functions found in the changed files to evaluate docstring coverage. Skipping docstring coverage check. Docstring coverage is scoped to functions touched by this diff. Analyzed 0 functions across 0… |
|     Linked Issues check    | ✅ Passed | Check skipped because no linked issues were found for this pull request.                                                                                                                                  |
| Out of Scope Changes check | ✅ Passed | Check skipped because no linked issues were found for this pull request.                                                                                                                                  |
|      Description Check     | ✅ Passed | Check skipped - CodeRabbit’s high-level summary is enabled.                                                                                                                                               |
|         Title check        | ✅ Passed | The title clearly identifies both primary changes: expanding the README and fixing the broken Discord badge.                                                                                              |

</details>

</details>

<!-- pre_merge_checks_walkthrough_end -->
<!-- finishing_touch_checkbox_start -->

<details>
<summary>✨ Finishing Touches</summary>

<details>
<summary>🧪 Generate unit tests (beta)</summary>

- [ ] <!-- {"checkboxId": "f47ac10b-58cc-4372-a567-0e02b2c3d479", "radioGroupId": "utg-output-choice-group-unknown_comment_id"} -->   Create PR with unit tests

</details>

</details>

<!-- finishing_touch_checkbox_end -->
<!-- tips_start -->

---

Thanks for using [CodeRabbit](https://coderabbit.ai?utm_source=oss&utm_medium=github&utm_campaign=bitaxeorg/bitaxe-web-flasher&utm_content=31)! It's free for OSS, and your support helps us grow. If you like it, consider giving us a shout-out.

<details>
<summary>❤️ Share</summary>

- [X](https://twitter.com/intent/tweet?text=I%20just%20used%20%40coderabbitai%20for%20my%20code%20review%2C%20and%20it%27s%20fantastic%21%20It%27s%20free%20for%20OSS%20and%20offers%20a%20free%20trial%20for%20the%20proprietary%20code.%20Check%20it%20out%3A&url=https%3A//coderabbit.ai)
- [Mastodon](https://mastodon.social/share?text=I%20just%20used%20%40coderabbitai%20for%20my%20code%20review%2C%20and%20it%27s%20fantastic%21%20It%27s%20free%20for%20OSS%20and%20offers%20a%20free%20trial%20for%20the%20proprietary%20code.%20Check%20it%20out%3A%20https%3A%2F%2Fcoderabbit.ai)
- [Reddit](https://www.reddit.com/submit?title=Great%20tool%20for%20code%20review%20-%20CodeRabbit&text=I%20just%20used%20CodeRabbit%20for%20my%20code%20review%2C%20and%20it%27s%20fantastic%21%20It%27s%20free%20for%20OSS%20and%20offers%20a%20free%20trial%20for%20proprietary%20code.%20Check%20it%20out%3A%20https%3A//coderabbit.ai)
- [LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fcoderabbit.ai&mini=true&title=Great%20tool%20for%20code%20review%20-%20CodeRabbit&summary=I%20just%20used%20CodeRabbit%20for%20my%20code%20review%2C%20and%20it%27s%20fantastic%21%20It%27s%20free%20for%20OSS%20and%20offers%20a%20free%20trial%20for%20proprietary%20code)

</details>


<sub>Comment `@coderabbitai help` to get the list of available commands.</sub>

<!-- tips_end -->
