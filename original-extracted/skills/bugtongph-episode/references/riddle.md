# bugtongPH — Riddle Selection & Integrity

## Absolute source rule

The **only permitted operational source for a bugtong used by bugtongPH is the connected Notion database `bugtongPH Riddle Database`.**

Every new riddle selection must originate from an actual record returned by the connected Notion database. This applies to `.riddle`, `.plot` auto-entry, `.auto`, and `.auto fresh`.

Do not select, invent, paraphrase, or substitute a riddle from:

- model knowledge or memory;
- prior conversation content;
- previous episode state when starting a fresh run;
- web search results;
- external websites;
- generated examples;
- arbitrary user-provided text unless that exact text is being explicitly added to the Notion database first;
- a stale or cached list that has not been confirmed against the connected Notion database.

If the Notion database is unavailable, inaccessible, or does not return a suitable record, stop at RIDDLE and report that the project database is unavailable or no suitable database record exists. Never fall back to another source.

## Database authority

The Notion database `bugtongPH Riddle Database` is authoritative for:

- riddle selection
- riddle identity
- stored riddle wording
- answer
- source information
- riddle metadata
- usage status
- episode usage
- setting
- project notes

The database record may itself contain provenance such as an external source URL. That provenance does **not** make the external source an alternate selection source. Selection must still come from the Notion record.

## `.riddle` behavior

`.riddle` is a selection menu, not an automatic selection command.

When `.riddle` is invoked:

1. Query the connected `bugtongPH Riddle Database`.
2. Determine applicable constraints.
3. Find a small batch of eligible unused records, defaulting to 5 when enough records exist.
4. Display the exact stored Riddle wording from those returned records.
5. Display the stored Answer because this is an internal production picker.
6. Do not choose on the user's behalf.
7. Wait for explicit selection.
8. Only then set that exact Notion record as the active RIDDLE state.

Do not report a riddle as database-backed unless the actual selected record came from the current Notion query.

## `.auto` behavior

`.auto` may auto-select a riddle, but the auto-selected riddle must be chosen from a record actually returned by the connected Notion `bugtongPH Riddle Database` during the current new run.

The answer may be used internally for integrity validation, but it must remain hidden from audience-facing creative stages.

## `.auto fresh` behavior

`.auto fresh` resets episode-local state and starts immediately. It must perform a fresh Notion riddle query and select a new eligible record from that query. It must not reuse the previous episode's riddle merely because it was already known in the conversation.

## `.auto resume` behavior

`.auto resume` may preserve the already-selected riddle from the active episode checkpoint because it is continuing an existing run rather than selecting a new riddle. It must not replace that riddle with a remembered, generated, or externally sourced alternative.

## Selection integrity

The selected riddle must preserve:

- exact Notion wording
- stored answer
- source/provenance metadata when available
- usage/status information when needed

Do not silently rewrite the stored wording. Any deliberate modification must be treated as generated content, not as the database original.

## Riddle and story separation

Never use the hidden answer to construct the story, environment, props, actions, camera emphasis, or other visual clues.

The riddle should remain genuinely unanswered.
