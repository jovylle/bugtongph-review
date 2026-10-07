# Veo 3.1 Lite — capabilities and hard limits

Source: Google Flow Help, "Learn about Google Flow models & supported features"
(`support.google.com/flow/answer/16352836`), retrieved 2026-10-07. Treat that page as the
authority; re-check it when a release looks wrong, and never restate a number this file does
not carry.

## Capability matrix

| Feature | Veo 3.1 Lite | Notes |
| --- | --- | --- |
| Text to video | 4s, 6s, 8s, both aspect ratios | |
| Frames to video — first frame | 4s, 6s, 8s, both aspect ratios | |
| Frames to video — first + last frame | 4s, 6s, 8s, both aspect ratios | |
| Ingredients / references to video | **8s only**, both aspect ratios | the image sheet is used here |
| Extend videos | **8s only**, from Lite/Fast/Quality source clips | see below |
| Video-to-video editing | **not supported** | |

Other models, for contrast: Veo 3.1 **Fast** cannot extend. Veo 3.1 **Quality** supports
neither ingredients nor extend. Google states that all Veo 3.1 8s videos can be extended but
**only Veo 3.1 Lite can perform the extension**.

Image inputs for frames and ingredients come from Flow's image models (Nano Banana Pro,
Nano Banana 2 Lite, Nano Banana 2.1).

## Rules that follow

1. **Clip 1 is an ingredient generation, so it must be exactly 8 seconds.** "Approximately
   eight seconds" is no longer a preference; a 4s or 6s clip cannot use the image sheet.
2. **Clip 2 is a text-only Extend of that 8-second clip.** No second image, no second sheet.
3. **Lite is the only model this pipeline targets.** Fast cannot extend and Quality cannot
   take ingredients, so either choice breaks one of the two clips.
4. **Panel count is bounded by the 8-second budget.** A 5-strip sheet splits the clip into
   roughly 1.6s per shot including dialogue; 2–3 panels is the sane default and 5 is reserved
   for very short beats. Panel count is chosen at FRAME, and the sheet's layout contract is in
   `frame.md`.
5. **One clip duration, one clip length.** Never plan dialogue that needs more than the
   available 8 seconds minus breathing, pauses, and the ending beat. Use 1.5–2.2
   words/second — natural conversational Tagalog (see `tagalog-pacing.md`).
6. **Frames-to-video is available** (4s/6s/8s). If an episode needs a locked ending state,
   FRAME may produce a first and last frame instead of a single sheet; the clip then uses
   Frames to Video rather than Ingredients. This is an alternative mode, not the default.
7. **Duration sets the clip count — 8 seconds per clip, always.** 16 seconds of story is
   Clip 1 (8s) plus Clip 2 (a text-only Extend of Clip 1's final state, 8s). 24 seconds is
   three chained 8s extends. There is no single 16-second clip on this model, so never write
   a prompt for one, and never let a script be presented as "16 seconds" without stating that
   it is two clips.
8. **Extend inherits from the LAST SECOND of the source clip.** Google's own Veo model page
   states it directly: *"Extend clips into longer, more dynamic videos. Use the last second of
   your first shot to continue the story – while maintaining visual and audio consistency."*
   (`deepmind.google/models/veo/`, retrieved 2026-10-07.)

   Consequences: the final second of every clip is a designed handoff, not dead time. Plan it
   in CLIPS for the outgoing clip — stable framing, characters settled rather than mid-motion,
   a completed line or clear silence, ambience continuous — and restate that same final second
   verbatim in the incoming clip's inherited state. A clip that ends mid-gesture or mid-word
   hands the extension a motion it cannot resolve.

## Extend inheritance — the last second

| Outgoing clip | What the extension receives |
| --- | --- |
| final second | poses, gaze, expression, clothing, props, environment, lighting, scale, camera |
| final second | ambience, speaker state, whether a line completed or silence fell |
| anything not in the final second | **nothing** — it is not inherited |

Design the ending beat into that second deliberately. This is also why an ending beat is
budgeted (0.5–1.0s) in `tagalog-pacing.md` rather than being left to chance.

## Extend audio — why a second clip comes back silent

Reported cause chain, from Google's own release notes plus consistent community reports:

1. **Extend's audio is recent.** Google: audio came to Extend (and Frames to Video) with the
   Veo 3.1 update in **October 2025**; audio reached Ingredients to Video later, in early 2026
   ("for the first time, we're also bringing audio to existing capabilities like 'Ingredients
   to Video', 'Frames to Video' and 'Extend'"). Anything extended through an older path has no
   audio by design.
2. **The extend step used to drop the model.** The most-cited community cause: extending a clip
   **downshifted to a model without audio** (Veo 2), so the extension came back silent even
   though the source clip had sound. Reports also note the model picker behaves differently on
   extended clips. Today the Flow help page is explicit — extending requires **Veo 3.1 Lite**,
   the only model that can extend — but the failure mode to check for is still "which model
   actually ran the extend".
3. **Only the last second is inherited.** If the source clip's final second is dead air — no
   ambience, no voice energy, dialogue already finished — the extension has nothing audio to
   continue and tends to return silent pictures.
4. **Audio-block prompt adherence is unreliable.** Community reports describe Veo refusing or
   dropping the audio block on some content regardless of how it is worded, and dense sound
   design (singing, overlapping dialogue, layered effects) failing on the audio branch while
   the silent version of the same prompt succeeds.
5. **Scene Builder is not the extend path.** Reported: extending from a Scene Builder scene no
   longer works; you must extend from the individual clip. Extending the wrong artifact loses
   audio continuity.

### Rules for Clip 2

- **Specify the audio explicitly** in the Extend prompt: name the ambience, name the next
  speaker and their exact line, and restate voice characteristics. Never leave Clip 2's audio
  implicit and hope it inherits.
- **Never let Clip 1 end in dead silence.** Its final second must carry live ambience and voice
  energy, because that second is the only audio source the extension gets.
- **Keep Clip 2's audio simple.** One speaker at a time, no singing, avoid dense overlapping
  sound design. When the audio branch fails, **simplify the audio spec first — do not rewrite
  the visual prompt**, which changes a picture that was already correct.
- **Extend the individual Clip 1 clip**, not a Scene Builder scene or a concatenation.
- **Check the model on the extend step.** It must be Veo 3.1 Lite. If the picker shows a lesser
  model, stop and fix that before extending rather than shipping a silent clip.
- **If Clip 2 still arrives silent, treat it as an audio-branch failure**: regenerate with only
  the audio section changed, and never accept the silent take silently. If it keeps failing,
  say so and offer the documented fallback — a separate recorded or synthesized voice line laid
  over the clip in post — flagged as post-production work outside this pipeline.

Community reports above are user reports, not Google statements; they are listed because they
match a repeatable failure, and the protocol is built to detect and recover from it either way.


## Veo 3.2 status

**Not in Google Flow.** As of 2026-10-07 the Flow model page
(`support.google.com/flow/answer/16352836`) lists only **Veo 3.1 (Lite / Fast / Quality)** and
**Gemini Omni Flash 1.1**; the DeepMind Veo page mentions only Veo 3.1. Everything circulating
about "Veo 3.2" — an Artemis engine, world-model physics, 30-second native generation,
"Ingredients 2.0" — comes from third-party leak and aggregator articles with no Google source
and a release window that has already passed.

**Do not target Veo 3.2, do not cite it as a capability, and do not plan around 30-second
native generation.** If the user asks, say exactly this: the leaks are unverified, Flow does
not list it, and the pipeline's 8-second ingredient/extend model is what actually exists.

When a new model does ship, re-read that help page and update this file — the pipeline's
duration rules change the moment a native 30s model actually lands.

For reference, other models on the same page and why they are not used here: **Gemini Omni
Flash 1.1** does 4s/6s/8s/10s with video-to-video editing and custom voices, but does not
support Extend yet; **Veo 3.1 Fast** cannot extend; **Veo 3.1 Quality** supports neither
ingredients nor extend. Lite is the only model that covers both of this pipeline's two clips.

## What this file must never claim

- An output resolution for Veo 3.1 Lite. The help page does not state one here; do not
  invent `720p`, `1080p`, or `4K`.
- A clip length other than 4s, 6s, or 8s for Lite text/frames generation, or other than 8s
  for ingredients and extend.
- Any credit cost. Costs change; point the user at Flow's prompt box.

## Prompt length

No prompt-length limit is published for these models. `clips.md` gives the house target
length (Clip 1 700–1200 words, Clip 2 600–1000) — that is this project's standard for
specificity, not a platform cap. Say so rather than presenting it as a limit.
