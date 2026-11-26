# POTIFY Telegram Editorial Kit

[Complete repository directory tree](docs/DIRECTORY.md)

## Two spaces or a different promise?

A line break added on a phone shouldn’t trick an editor into posting the same message twice. Changing ‘Soil’ to ‘Roots’ really does change the copy. The Telegram Editorial Kit puts those two cases next to one another so the distinction is visible.

The [fingerprint tests](tests/test_review.py) compare those exact examples. The [review utility](src/review.py) runs offline; the historical bot is retained as source reference. A matching fingerprint says something about text, not who authorized it or whether Telegram received it.

Try a line-break-only edit, then change the meaning of one word. Report what matched and what changed using fictional copy. No access token, real conversation, bot deployment or message send is needed.

**Recovered bot source and offline review tool.** Give editors an iPhone-friendly way to inspect a Telegram draft and its duplicate history before publication.

### Setup and usage

Python 3.10 or newer. The project uses the standard library.

```sh
python3 src/review.py examples/draft.txt
```

Check a fictional draft locally. 

### Developer entry points

The two original bot releases share a posting implementation. This edition preserves that implementation as a text reference and provides a local fingerprint tool for editor review. Explore `examples/`, `reference/`, `src/`, `tests/` in the full tree.

### Verification

Three offline fingerprint tests passed, covering whitespace normalization, material edits and empty input.

```sh
python3 -m unittest discover -s tests
```

### Release scope

The historical starter describes automated posting. The shipped review tool is offline. Current publishing remains subject to Chance’s approval. potify_telegram_bot_starter.zip and potify_telegram_iphone_kit.zip. Original Python bot, dependency list and project brief are retained as inert historical reference files. The active local CLI only fingerprints user-supplied text.

[Technical whitepaper](docs/WHITEPAPER.md) · [Marketing and sales plan](docs/MARKETING.md) · [Dated developer log](docs/BUILD-LOG.md)

Existing asset and code terms remain applicable. Public access to a recording, illustration, brand or manuscript does not itself grant commercial reuse rights.
