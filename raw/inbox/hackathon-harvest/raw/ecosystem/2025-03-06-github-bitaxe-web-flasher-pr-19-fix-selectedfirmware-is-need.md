# bitaxeorg/bitaxe-web-flasher pull request #19: fix: selectedFirmware is needed

> Source: https://github.com/bitaxeorg/bitaxe-web-flasher/pull/19
> Collected: 2026-10-07
> Published: 2025-03-06

- Repository: bitaxeorg/bitaxe-web-flasher
- Type: pull request
- Number: 19
- State: closed
- Author: WantClue
- Opened: 2025-03-06
- Closed: 2025-03-06
- Labels: bug

## Description

fixes #18 
selectedFirmware was not needed so I added it to it.

<!-- This is an auto-generated comment: release notes by coderabbit.ai -->
## Summary by CodeRabbit

- **Bug Fixes**
  - Enhanced the flashing process validation to require a firmware selection alongside device and board version. This update ensures that all necessary conditions are met before the flashing process can be initiated, preventing unintended actions.
<!-- end of auto-generated comment: release notes by coderabbit.ai -->

## Comments

### coderabbitai[bot] on 2025-03-06

<!-- This is an auto-generated comment: summarize by coderabbit.ai -->
<!-- walkthrough_start -->

## Walkthrough
The update modifies the `LandingHero` component to enhance the validation logic for the flashing process. A new condition is added to the `handleStartFlashing` function to check for the presence of `selectedFirmware`. The `Button` component's `disabled` property is also updated to include this check, ensuring that the button is disabled if any required selections are missing or if the device is not connected.

## Changes
| File                          | Change Summary                                                                                                                               |
|-------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------|
| `src/.../LandingHero.tsx`     | Added a check for `selectedFirmware` in the `handleStartFlashing` function and updated the `disabled` property of the flash button accordingly. |

## Poem
> I'm a rabbit with a hop so spry,  
> New code ensures things function right.  
> A firmware check joins the crew today,  
> So the flash button waits until it's okay.  
> With cautious steps, we hop along the code path—hip hip hooray!  
> 🐇✨

<!-- walkthrough_end -->
<!-- internal state start -->


<!-- DwQgtGAEAqAWCWBnSTIEMB26CuAXA9mAOYCmGJATmriQCaQDG+Ats2bgFyQAOFk+AIwBWJBrngA3EsgEBPRvlqU0AgfFwA6NPEgQAfACgjoCEYDEZyAAUASpADK2VmgqyjcEj2wAbb5AokAI7Y0riQ4rjedJAARABm8AAeXIgkUWJ0AGLwFMwA7i6eqOR0dDGQBciI2ALM6jT0cuGwntipfADqmLgAwt4h6Bj0qPBKGOIJ0WjIGE4ClJAAjACc/Fi4LZAA4uoAEjX+JNz4iOr4rpBx55BquGiJJGB5JAJgcd7TLRQaMJu88MwXPJuNgKMdUvw4s1ULYUMgCOhaLQAohkJg4dVPAE4pQyAwpsgzIsABwaIwASXWmyUiAYFHg3HE+AwABoUGFUIg7g1mtRmp4JC54CoopAAAapdINbK5AoBMUVaaQDD4MK8EgSeD4NreeTwDAMfpKRp4OHK/B5SBKEhsejkfGooFsqJoWj6ojhfDstFI9RarD6/kKJQ/TKgjaUZjnEhs9RmlU8jZ8tA3bAegTa8byWBK+ZkSBEKjjaKBgIfJnrL0bVAJRJkgyZa5RgJWkh3eDeRBsiNeXyHYKhRjo+boBgO1L0Pk9q6+C3uyAAVRsABkuABtWC4XDcRAcAD0e6I6lgNQ0TGYe9u9xI5yIl/U16eLzeH0QXz3IN8e5WAF0ABSbtuu4HkeGynue953A8t6QY+zyvO8nyUB+PjeN+ywAJT1voxjgFAZD0PgUJoHghCkOQVA8uebDjFwvD8MIojiFIMjyEwShUKo6haDoOEmFAcAjGiWAkQQxBkMoVEsDRnD+GglrVM4FxNOxyhcZo2i6GAhi4aYBiIBQDB7uexzkOMiB7sumBuhgRC7JQ+AaLgiDJAYMTuQYFiQAAguS4kUdQ0SKYCFxEYwOa2dI7ibAwEWkMggY9mKVlDO69kUPgComcy7AoOMGW0Ng+KDIiboVmgfiCt4ozUP6kBckclzXNOr4ILZPAZeOPz2NwojwAkDAVbqbIpuQlpMKlFZmq6xqekGYoRbQUT2HcFC4JkrXugqcTYAaU0IrFogANYoFCEppExWQ5PkhQKsUqr1RdGS0D85JnZKl20DKN3ytNAipOM3abDte11akzlBly1BtHN+puoNNC8mEGYbOgraasV1mXNdcqeMwbTI54H3PYM9ARlgAS4KCGDICQLjDR1GrsPOLWfPOvD4OOlwZcw9WreItk/N5vrlb4shA54YpuogIp0AqHO9Wt8hhUlABCeAEBgWUsKZuVJhyGB+oF8LA5t7Uc1zqDYNwtCBWTXr6oa2BKEGh0MCdVx8OdUpXbKt0/B4qZbsyFQdn4KqWiO0uy8MxEYMrULTvgs55POE1lf6aItrgFAhFwYogMTDQACIavA+JimyBdF3Qqv4C4tAAGqUKczKV+KhdPdKOO3VXSA9My9oC0Q7dikgG1s7Z7fXAX/eD59YoBwgyCxZgpCQGQEUOkGVU1VN3j4EeDA3PIZDVPS7X62jCR+y2UgUK3WD41y6Cdl6I4140JCe54rNvmn6ILYkDoPWLy3lvA0EopnOaPYlCGhcLVZkyAwokESMcNa0RrgggENVY+zNxBRQMFAAAcl6CqkDEE0xgdSUQHwoFIMhBvNB5weRYJqLgje4w/TSAqLiSAgIXaJWXlafqcQyTuRiEYHCBh+KcMIsRUi/lJLRGouwLgVAFJOBCvIFSig1K3B4lpQwsjqLqAAPqjEQGYgImoSDPFoGYqGa0jG6SgAAVgAOwAGYSDLAAGxuK8QAJi8XELxfjbYeIACxeLcX44kbiGACA8QwNxxJaCLAYMSGJcQGBROWEEtxLjZEeIAAxxCCQwTJUS/ECC8WgKJaA/HRLQAwIJywlC5OJAwWgAhyleIYKU4kiwgkeOWF4lxMi8IKFYOYyx1iy52LoGYgiRigA= -->

<!-- internal state end -->
<!-- finishing_touch_checkbox_start -->

<details>
<summary>✨ Finishing Touches</summary>

- [ ] <!-- {"checkboxId": "7962f53c-55bc-4827-bfbf-6a18da830691"} --> 📝 Generate Docstrings

</details>

<!-- finishing_touch_checkbox_end -->
<!-- tips_start -->

---



<details>
<summary>🪧 Tips</summary>

### Chat

There are 3 ways to chat with [CodeRabbit](https://coderabbit.ai?utm_source=oss&utm_medium=github&utm_campaign=bitaxeorg/bitaxe-web-flasher&utm_content=19):

- Review comments: Directly reply to a review comment made by CodeRabbit. Example:
  - `I pushed a fix in commit <commit_id>, please review it.`
  - `Generate unit testing code for this file.`
  - `Open a follow-up GitHub issue for this discussion.`
- Files and specific lines of code (under the "Files changed" tab): Tag `@coderabbitai` in a new review comment at the desired location with your query. Examples:
  - `@coderabbitai generate unit testing code for this file.`
  -	`@coderabbitai modularize this function.`
- PR comments: Tag `@coderabbitai` in a new PR comment to ask questions about the PR branch. For the best results, please provide a very specific query, as very limited context is provided in this mode. Examples:
  - `@coderabbitai gather interesting stats about this repository and render them as a table. Additionally, render a pie chart showing the language distribution in the codebase.`
  - `@coderabbitai read src/utils.ts and generate unit testing code.`
  - `@coderabbitai read the files in the src/scheduler package and generate a class diagram using mermaid and a README in the markdown format.`
  - `@coderabbitai help me debug CodeRabbit configuration file.`

Note: Be mindful of the bot's finite context window. It's strongly recommended to break down tasks such as reading entire modules into smaller chunks. For a focused discussion, use review comments to chat about specific files and their changes, instead of using the PR comments.

### CodeRabbit Commands (Invoked using PR comments)

- `@coderabbitai pause` to pause the reviews on a PR.
- `@coderabbitai resume` to resume the paused reviews.
- `@coderabbitai review` to trigger an incremental review. This is useful when automatic reviews are disabled for the repository.
- `@coderabbitai full review` to do a full review from scratch and review all the files again.
- `@coderabbitai summary` to regenerate the summary of the PR.
- `@coderabbitai generate docstrings` to [generate docstrings](https://docs.coderabbit.ai/finishing-touches/docstrings) for this PR.
- `@coderabbitai resolve` resolve all the CodeRabbit review comments.
- `@coderabbitai configuration` to show the current CodeRabbit configuration for the repository.
- `@coderabbitai help` to get help.

### Other keywords and placeholders

- Add `@coderabbitai ignore` anywhere in the PR description to prevent this PR from being reviewed.
- Add `@coderabbitai summary` to generate the high-level summary at a specific location in the PR description.
- Add `@coderabbitai` anywhere in the PR title to generate the title automatically.

### CodeRabbit Configuration File (`.coderabbit.yaml`)

- You can programmatically configure CodeRabbit by adding a `.coderabbit.yaml` file to the root of your repository.
- Please see the [configuration documentation](https://docs.coderabbit.ai/guides/configure-coderabbit) for more information.
- If your editor has YAML language server enabled, you can add the path at the top of this file to enable auto-completion and validation: `# yaml-language-server: $schema=https://coderabbit.ai/integrations/schema.v2.json`

### Documentation and Community

- Visit our [Documentation](https://docs.coderabbit.ai) for detailed information on how to use CodeRabbit.
- Join our [Discord Community](http://discord.gg/coderabbit) to get help, request features, and share feedback.
- Follow us on [X/Twitter](https://twitter.com/coderabbitai) for updates and announcements.

</details>

<!-- tips_end -->
