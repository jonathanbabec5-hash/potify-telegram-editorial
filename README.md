# POTIFY Telegram Editorial Kit

[Complete repository directory tree](docs/DIRECTORY.md)

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
