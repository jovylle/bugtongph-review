# Notion Riddle Database — connection contract

This file defines how the pipeline talks to the authoritative riddle source. Read it
before any `.riddle`, `.script` auto-entry, `.auto`, or `.auto fresh` run.

## Source of truth

The only permitted riddle source is the connected Notion database named
`bugtongPH Riddle Database`. It is accessible through the registered Notion app declared
in the plugin's `.app.json`. If the Notion app connection is not available or not
authenticated, RIDDLE falls back to the bundled set — see "Blocked states" below.

## Resolving the database

1. Search the connected Notion workspace for a database whose title is exactly
   `bugtongPH Riddle Database`.
2. If exactly one match exists, use it for the whole run and record its id in episode state.
3. If several match, list them and ask the user which one to use. Never guess.
4. If none match, stop and report the blocker. Do not substitute a page, a view, or a
   different database.

The resolved database id is episode state. Reuse it when resuming; do not re-resolve
mid-run unless the user says the source changed.

## Expected record fields

Query the database and map its properties by role. Accept the usual Notion variations
(`Riddle` / `Bugtong`, `Answer` / `Sagot`, `Used` / `Status`).

| Role | Meaning | Required |
| --- | --- | --- |
| Riddle text | Exact stored bugtong wording, preserved verbatim | yes |
| Answer | Stored answer; operator-visible only, never audience-facing | yes |
| Source / provenance | Where the riddle came from, when recorded | no |
| Usage status | Whether the record has already been used for an episode | no |

Never rewrite, normalize, or paraphrase the stored riddle wording. If you deliberately
change it, treat the result as generated content, not as the database original.

## Selection rules

- Prefer records whose usage status is unused or not yet produced.
- `.riddle` returns a short batch (default 5 when enough records exist) as a menu and
  waits for an explicit pick. It never chooses for the user.
- `.auto` and `.script` auto-entry may pick one eligible record, but only from records
  actually returned by the current query.
- `.auto fresh` must run a new query and pick a new eligible record.
- `.auto resume` keeps the riddle already recorded in the active checkpoint.
- **A record with an empty cell for the selected language is not eligible.** Skip it. Never
  translate, romanize, or adapt another language's wording to fill that gap. If the query returns
  no record carrying the selected language, report the language as unavailable from this source,
  fall back (bundled set), or stop at RIDDLE — see `riddle.md` "The selected language is not a
  translation instruction".

## Marking usage

After an episode completes CLIPS, update the record's usage status if the database has
such a property. Never mark a record used before the episode is finished, and never
silently delete or archive a record.

## Blocked states

Notion being unavailable is **no longer a blocker** — the picker falls back to the bundled set
(`bundled-riddles.md`) and states that it has done so.

Report the blocker and stop at RIDDLE only when:

- the Notion app connection is unavailable or unauthenticated **and** `assets/riddles.json` cannot
  be read;
- the `bugtongPH Riddle Database` resolves but returns no record with usable riddle text **and**
  the bundled set is exhausted or unreadable.

Never fall back to model memory, earlier conversation content, web search, or a generated
riddle. A blocked RIDDLE is a correct outcome; an invented riddle is a pipeline failure.
