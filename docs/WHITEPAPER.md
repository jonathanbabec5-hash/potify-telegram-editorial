# POTIFY Telegram Editorial Kit
## Whitepaper · public developer edition

**November 25, 2026 · Recovered bot source and offline review tool**

### Goal and audience

Give editors an iPhone-friendly way to inspect a Telegram draft and its duplicate history before publication. The immediate audience is community editors and Telegram maintainers.

### Design and implementation

The two original bot releases share a posting implementation. This edition preserves that implementation as a text reference and provides a local fingerprint tool for editor review. A normalized digest lets a reviewer compare text without sending it to a service. It does not establish who approved a draft or when it was dispatched.

### What a contributor can establish

Three offline fingerprint tests passed, covering whitespace normalization, material edits and empty input. Use the original project brief for vocabulary and preserve exact text, media and destination when conducting a real approval.

### Evidence and outstanding work

The historical starter describes automated posting. The shipped review tool is offline. Current publishing remains subject to Chance’s approval. The next acceptance case is concrete. Compare the same text twice and confirm that the normalized fingerprint matches, with no connection to Telegram or an AI service.

### Place in POTIFY

Validate one paid editorial onboarding session after the team documents a reduction in duplicated work. The marketing plan gives the test window and the evidence for a commercial outcome.

[Source provenance](source.json) · [Build log](BUILD-LOG.md) · [Marketing plan](MARKETING.md)
