# Reference Binding and Identity Authority

## Purpose

Prevent semantic re-creation of characters when a canonical visual reference asset exists.

## Canonical profile-01 asset

For `profile-01`, the canonical character identity reference asset is exactly:

```text
assets/character-turnaround.png
```

This asset is the visual authority for character identity and appearance.

## Authority order

For character identity, use this precedence:

1. canonical active-profile reference image asset;
2. explicit profile definition derived from that asset;
3. textual continuity rules only for properties not directly visible in the asset.

Textual character descriptions must never override or redesign a visible canonical reference.

## Mandatory render binding

Before `.render` image generation:

```text
ACTIVE PROFILE
→ RESOLVE REFERENCE ASSET
→ BIND REFERENCE AS IMAGE INPUT
→ GENERATE
```

The exact active-profile reference asset must be available to the image-generation request as an image/reference input when the generation capability supports image inputs.

Do not treat merely naming the asset path in a text prompt as equivalent to supplying the image.

## No semantic fallback

If the active-profile reference asset cannot be supplied to the image-generation capability, do not silently reconstruct the characters from descriptive text. Stop IMAGE and report:

```text
IMAGE BLOCKED: canonical active-profile reference asset is not bound to the image-generation request.
```

A visually plausible but newly invented character is a failed render, not an acceptable fallback.

## Reference vs episode render

The canonical profile reference defines who the characters are.

The current episode IMAGE defines the current pose, expression, gaze, hand placement, position, environment, lighting, composition, and shot state.

Never use a previous episode IMAGE as a substitute for the canonical profile reference.

## Frame restriction

FRAME may describe camera composition, but it must not redefine character identity. Descriptions such as age, facial structure, clothing colors, hairstyle, or accessories are continuity constraints only and do not replace the canonical visual reference.

## Identity validation

A render passes identity validation only when the generated characters are recognizably the same canonical profile as the bound reference, allowing only the pose, expression, camera, environment, lighting, and other episode-state changes explicitly required by FRAME.
