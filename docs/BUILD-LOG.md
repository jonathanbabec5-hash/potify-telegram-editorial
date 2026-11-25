# November 25, 2026 · POTIFY Telegram Editorial Kit

**Question.** Give editors an iPhone-friendly way to inspect a Telegram draft and its duplicate history before publication.

**Source and change.** potify_telegram_bot_starter.zip and potify_telegram_iphone_kit.zip. Original Python bot, dependency list and project brief are retained as inert historical reference files. The active local CLI only fingerprints user-supplied text.

**Observed result.** Three offline fingerprint tests passed, covering whitespace normalization, material edits and empty input.

```sh
python3 -m unittest discover -s tests
```

**Next acceptance check.** Compare the same text twice and confirm that the normalized fingerprint matches, with no connection to Telegram or an AI service.

**Owner and decision.** Chance owns the public release and approves campaign copy. The historical starter describes automated posting. The shipped review tool is offline. Current publishing remains subject to Chance’s approval.

This dated record describes the developer package. Verify remote commit and tree in the publication receipt before announcing a GitHub release.
