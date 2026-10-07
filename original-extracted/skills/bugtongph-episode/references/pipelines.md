# Legacy Pipeline Compatibility

## Status

This file is retained only so older episodes and older user prompts remain interpretable. It is no longer the authority for BugtongPH runtime architecture.

The canonical model is defined in `release-channels.md`:

```text
CHANNEL
  production | beta | development

RELEASE
  stable SemVer or prerelease SemVer

WORKFLOW CONTRACT
  workflow-contract-v1
```

Do not create new production/beta/development pipeline IDs.

## Legacy mappings

Old identifiers map as follows:

```text
production-v1   → production channel
experimental-v2 → beta channel
```

`.auto experimental` remains a compatibility alias for `.auto beta`.

## Legacy command handling

When an existing episode or user prompt uses:

```text
.pipeline use production-v1
.pipeline use experimental-v2
```

interpret it as the corresponding channel selection and record the canonical channel internally.

`.pipeline fork <source> <new-id>` is deprecated. Do not use it to create release environments. New experimental work belongs in `development`; behavior intended for real-episode validation belongs in `beta`.

## Separation rule

Never use a pipeline ID to represent:

- a plugin package version;
- a release candidate;
- a runtime channel;
- a visual pair; or
- an episode.

Those are separate dimensions.
