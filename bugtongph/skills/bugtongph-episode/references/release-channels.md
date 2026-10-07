# Release Channels and Runtime Versions

## Purpose

Separate the runtime environment from the installed plugin package, workflow contract, visual profile, and episode state.

The old `production-v1` / `experimental-v2` model is retired as the primary architecture. Do not create new pipeline IDs for production, beta, or development work.

## Canonical dimensions

Every active episode has these independent dimensions:

```text
CHANNEL
  production | beta | development

RELEASE
  stable SemVer or prerelease SemVer recorded for the run

WORKFLOW CONTRACT
  workflow-contract-v1 (or a newer explicitly declared contract)

PROFILE
  profile-01 | profile-02 | ...

EPISODE
  riddle + location + environment + profile + script + frame + image + clips
```

Do not treat any one dimension as another.

## Channel semantics

### production

Stable, user-facing behavior. Production is read-only with respect to experimentation. Do not introduce unvalidated beta or development behavior into this channel.

### beta

Beta is a code-identical runtime copy of production. Use beta to test the exact current production behavior in an isolated channel before introducing beta-only changes.

Beta MUST NOT select a different renderer, alternate prompt system, different reference-binding rules, different validation gates, or different stage contracts.

### development

Unreleased implementation and rule work. Development is allowed to change while being built. Development output is not considered production-safe unless promoted through beta validation and then an explicit production release.

## Release semantics

The plugin package version is the version actually installed by the ChatGPT plugin runtime. Channel selection is a logical execution mode inside the plugin and must not be described as simultaneously installing multiple plugin packages.

Use SemVer for package/release identity:

```text
0.5.0
0.5.1-beta.1
0.5.1-beta.2
0.5.1
```

Prerelease labels such as `-beta.1` identify candidates. A stable release is promoted by publishing the corresponding stable package version. Never represent promotion as changing a pipeline ID.

## Workflow contract

The workflow contract describes behavior that must remain true across channels unless a new contract is explicitly declared.

Current contract:

```text
workflow-contract-v1

RIDDLE → LOCATION → ENVIRONMENT → PROFILE → SCRIPT → FRAME → OVERVIEW → IMAGE PROMPT → IMAGE → CLIPS
```

The contract owns the stage boundaries and invariants.

Production and beta always use the exact same implementation snapshot. Development may diverge.

## Episode recording

When a run starts or resumes, record:

```text
CHANNEL
RELEASE
WORKFLOW CONTRACT
PROFILE
```

For an unfinished run, the recorded channel has priority. Do not silently move a run from production to beta or development.

An explicit user-requested channel switch is allowed. Preserve completed stages only when the target channel states that their contract remains valid. Otherwise regenerate the affected stage and all downstream dependents.

## Commands

### Preferred

```text
.channel
.channel list
.channel use production
.channel use beta
.channel use development

.release
.release info

.workflow
.workflow info
```

`.auto production`, `.auto beta`, and `.auto dev` are explicit run-routing shortcuts.

### Compatibility aliases

Older episodes and user prompts may still contain:

```text
.pipeline use production-v1
.pipeline use experimental-v2
```

Interpret them as:

```text
production-v1  → production
experimental-v2 → beta
```

Do not create new aliases or pipeline IDs from these legacy names. `.pipeline fork` is deprecated and should not create new production/beta environments.

## Promotion model

For future divergent work, the intended direction is:

```text
development
    ↓
beta candidate
    ↓
real-episode validation
    ↓
explicit promotion
    ↓
production release
```

At the current release, however, beta is intentionally held at exact production parity as requested.

Whenever beta is held at parity, this file and `.render` must say so without pinning a
version number. The installed package version is the single source of release truth and
is reported by `.release`; do not restate it in skill prose.
