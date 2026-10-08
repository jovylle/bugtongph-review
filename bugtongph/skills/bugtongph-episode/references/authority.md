# bugtongPH — Authority & Project Identity

## Purpose

This file defines the project-level rules and source precedence for bugtongPH.

## Authoritative layers

1. **Subject source** — one of two, chosen by the content pipeline:
   - **Notion `bugtongPH Riddle Database`** (riddle pipeline) — riddle identity, stored wording,
     answer, source/metadata, usage status; connection and record contract in
     `notion-riddle-database.md`;
   - **the model-invented TOPIC** (topic pipeline) — the locked topic and angle, stated openly,
     with no answer; see `topic.md`.

2. **Active Character + Art Style + Voice profile**
   - character identity
   - appearance
   - reference assets
   - art/material language
   - scale conventions
   - voice/speech identity

3. **Approved SCRIPT**
   - story
   - environment
   - physical states
   - dialogue
   - speakers
   - timing
   - feasibility

4. **Validated IMAGE** — the shot-reference sheet
   - current Clip 1 pose/state
   - camera composition
   - environment
   - lighting
   - current visual progression
   - at CLIPS, **the authority for everything visible**: face, build, clothing construction,
     surface material, scale. Text does not restate what the sheet shows.

5. **`active-pair-runtime.md`**
   - parameterizes legacy hard-coded references so they use the active profile
   - carries the identity modes (`text` / `attached`) and the asset-availability rule

6. **Veo / Google Flow references**
   - provider-oriented prompt construction
   - camera
   - motion
   - dialogue
   - audio
   - timing
   - feasibility

7. **OVERVIEW / IMAGE PROMPT**
   - locked-state review and prompt assembly, text only

## Project identity

Each episode is one setting + one believable situation + one active character profile + one
subject, where the subject is either a database-backed bugtong (riddle pipeline) or a
model-invented topic (topic pipeline) — never both.

The project should feel coherent within the selected profile and art direction. New profiles are allowed, but they must remain isolated from legacy or other profiles.

## Core continuity principle

A later stage may refine execution but may not silently rewrite a higher-priority source.
