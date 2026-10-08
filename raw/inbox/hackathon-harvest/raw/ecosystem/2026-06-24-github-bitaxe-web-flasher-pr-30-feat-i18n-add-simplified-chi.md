# bitaxeorg/bitaxe-web-flasher pull request #30: feat(i18n): add Simplified Chinese (zh-CN) localization

> Source: https://github.com/bitaxeorg/bitaxe-web-flasher/pull/30
> Collected: 2026-10-07
> Published: 2026-06-24

- Repository: bitaxeorg/bitaxe-web-flasher
- Type: pull request
- Number: 30
- State: open
- Author: renfei
- Opened: 2026-06-24
- Closed: n/a
- Labels: none

## Description

## Summary

- Add `src/i18n/locales/zh-CN.json` with full Simplified Chinese translations covering all existing keys (`common`, `header`, `hero`, `features`, `instructions`, `status`, `errors`)
- Register `zh-CN` as a supported language in `src/i18n/config.ts`
- Add `简体中文` option to the language selector dropdown in `LanguageSelector.tsx`

## Changes

| File | Change |
|------|--------|
| `src/i18n/locales/zh-CN.json` | New file — complete zh-CN translation |
| `src/i18n/config.ts` | Import and register `zh-CN` resource |
| `src/components/LanguageSelector.tsx` | Add `{ value: 'zh-CN', label: '简体中文' }` to language list |

## Testing

1. Open the app in a Chromium-based browser
2. Open the language selector
3. Choose **简体中文**
4. Verify all UI strings are displayed in Simplified Chinese

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->

## Summary by CodeRabbit

* **New Features**
  * Added Simplified Chinese language support. Users can now select Simplified Chinese as their preferred language for the app interface, with complete translation coverage for all UI elements, including navigation, features, and system messages.

<!-- end of auto-generated comment: release notes by coderabbit.ai -->

## Comments

### coderabbitai[bot] on 2026-06-24

<!-- This is an auto-generated comment: summarize by coderabbit.ai -->
<!-- review_stack_entry_start -->

[![Review Change Stack](https://storage.googleapis.com/coderabbit_public_assets/review-stack-in-coderabbit-ui.svg)](https://app.coderabbit.ai/change-stack/bitaxeorg/bitaxe-web-flasher/pull/30?utm_source=github_walkthrough&utm_medium=github&utm_campaign=change_stack)

<!-- review_stack_entry_end -->
No actionable comments were generated in the recent review. 🎉

<details>
<summary>ℹ️ Recent review info</summary>

<details>
<summary>⚙️ Run configuration</summary>

**Configuration used**: defaults

**Review profile**: CHILL

**Plan**: Pro

**Run ID**: `09900b8a-11b5-4991-a4e9-323ab604ec8c`

</details>

<details>
<summary>📥 Commits</summary>

Reviewing files that changed from the base of the PR and between 3b941641aada1c2dc615623d76bdff1cc9534693 and 4f1094739cf3930871e815a66ea8c775ce65c1e4.

</details>

<details>
<summary>📒 Files selected for processing (3)</summary>

* `src/components/LanguageSelector.tsx`
* `src/i18n/config.ts`
* `src/i18n/locales/zh-CN.json`

</details>

</details>

---
<!-- walkthrough_start -->

<details>
<summary>📝 Walkthrough</summary>

## Walkthrough

Adds Simplified Chinese (`zh-CN`) language support by introducing a new locale JSON file with 78 translation keys, registering it in the i18next configuration, and adding it as a selectable option in the `LanguageSelector` component.

## Changes

**Simplified Chinese Localization**

| Layer / File(s) | Summary |
|---|---|
| **zh-CN locale file and i18next registration** <br> `src/i18n/locales/zh-CN.json`, `src/i18n/config.ts` | Adds `zh-CN.json` with translations for all UI areas (labels, navigation, hero, features, instructions, flash/log status strings, and browser error), imports it in `config.ts`, and registers it under `'zh-CN'` in the i18next resources map. |
| **LanguageSelector UI entry** <br> `src/components/LanguageSelector.tsx` | Adds `zh-CN` (Simplified Chinese) to the `languages` array so it appears as a selectable option alongside the existing entries. |

## Estimated code review effort

🎯 1 (Trivial) | ⏱️ ~3 minutes

## Poem

> 🐰 A bunny hops east, past the Great Wall so grand,
> New words bloom like flowers across the land.
> `zh-CN` now lives where only one tongue had been,
> Each key unlocks a phrase for eyes yet unseen.
> Hào! The flasher speaks Chinese — how grand a sight! ✨

</details>

<!-- walkthrough_end -->
<!-- pre_merge_checks_walkthrough_start -->

<details>
<summary>🚥 Pre-merge checks | ✅ 5</summary>

<details>
<summary>✅ Passed checks (5 passed)</summary>

|         Check name         | Status   | Explanation                                                                                                                                                                          |
| :------------------------: | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|      Description Check     | ✅ Passed | Check skipped - CodeRabbit’s high-level summary is enabled.                                                                                                                          |
|         Title check        | ✅ Passed | The title accurately describes the main change: adding Simplified Chinese (zh-CN) localization support across multiple files (translation file, i18n config, and language selector). |
|     Docstring Coverage     | ✅ Passed | No functions found in the changed files to evaluate docstring coverage. Skipping docstring coverage check.                                                                           |
|     Linked Issues check    | ✅ Passed | Check skipped because no linked issues were found for this pull request.                                                                                                             |
| Out of Scope Changes check | ✅ Passed | Check skipped because no linked issues were found for this pull request.                                                                                                             |

</details>

<sub>✏️ Tip: You can configure your own custom pre-merge checks in the settings.</sub>

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

Thanks for using [CodeRabbit](https://coderabbit.ai?utm_source=oss&utm_medium=github&utm_campaign=bitaxeorg/bitaxe-web-flasher&utm_content=30)! It's free for OSS, and your support helps us grow. If you like it, consider giving us a shout-out.

<details>
<summary>❤️ Share</summary>

- [X](https://twitter.com/intent/tweet?text=I%20just%20used%20%40coderabbitai%20for%20my%20code%20review%2C%20and%20it%27s%20fantastic%21%20It%27s%20free%20for%20OSS%20and%20offers%20a%20free%20trial%20for%20the%20proprietary%20code.%20Check%20it%20out%3A&url=https%3A//coderabbit.ai)
- [Mastodon](https://mastodon.social/share?text=I%20just%20used%20%40coderabbitai%20for%20my%20code%20review%2C%20and%20it%27s%20fantastic%21%20It%27s%20free%20for%20OSS%20and%20offers%20a%20free%20trial%20for%20the%20proprietary%20code.%20Check%20it%20out%3A%20https%3A%2F%2Fcoderabbit.ai)
- [Reddit](https://www.reddit.com/submit?title=Great%20tool%20for%20code%20review%20-%20CodeRabbit&text=I%20just%20used%20CodeRabbit%20for%20my%20code%20review%2C%20and%20it%27s%20fantastic%21%20It%27s%20free%20for%20OSS%20and%20offers%20a%20free%20trial%20for%20proprietary%20code.%20Check%20it%20out%3A%20https%3A//coderabbit.ai)
- [LinkedIn](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fcoderabbit.ai&mini=true&title=Great%20tool%20for%20code%20review%20-%20CodeRabbit&summary=I%20just%20used%20CodeRabbit%20for%20my%20code%20review%2C%20and%20it%27s%20fantastic%21%20It%27s%20free%20for%20OSS%20and%20offers%20a%20free%20trial%20for%20proprietary%20code)

</details>


<sub>Comment `@coderabbitai help` to get the list of available commands.</sub>

<!-- tips_end -->
