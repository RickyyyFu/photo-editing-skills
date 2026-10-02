# Image-Generation Workflow and Prompt Specification

Use descriptive visual language. Never include `Roberta Mazzone`, `_lagiuditta`, or another living creator's name as a style token in a final production prompt.

## 1. Create an originality delta

Before writing the prompt, change at least four elements from any public reference:

- Geographic setting or season
- Architecture or interior program
- Subject identity and action
- Wardrobe silhouette or accent color
- Camera position or framing device
- Time of day or weather
- Narrative object or local ritual
- Aspect ratio or sequence role

Do not recreate a recognizable published composition with only cosmetic changes.

## 2. Select the generator strategy

- **Single image**: use one primary composition recipe and one light event.
- **Series/contact sheet**: keep place, palette, subject, and material anchors stable while changing shot scale and action.
- **Image edit**: name only the requested changes; preserve identity, geometry, and unrequested content. Use the image-editing tool when available.
- **Reference-led generation**: describe the traits to borrow and the structural changes that ensure an original result. Include only references the user may use.

## 3. Use the prompt grammar

Write the production prompt in this order:

1. **Medium and story beat** — editorial travel photograph, hospitality image, environmental portrait, architectural still life, or closing detail.
2. **Place-specific subject** — identify local material, climate, architecture, or ritual.
3. **Unforced action or human trace** — one quiet action, a partial figure, or evidence of recent presence.
4. **Composition** — threshold, foreground veil, stable verticals, negative space, small figure, layered depth, or textural compression.
5. **Light event** — window shaft, side light, low backlight, reflected water, warm interior/cool exterior, or soft early light.
6. **Palette** — three to six colors with one relationship, such as warm ochre against muted sea blue.
7. **Lens feel and depth** — natural perspective or mild compression; moderate shallow depth while retaining environmental context.
8. **Surface and finish** — plaster, linen, stone, wood, dust, water shimmer, natural skin, restrained warmth, optional fine grain.
9. **Output constraints** — aspect ratio, orientation, realism, no text/logos/watermark, and series continuity if needed.

### Prompt skeleton

```text
[Medium and narrative beat] in [specific place and season].
[Subject] is [quiet, believable action], integrated into [architecture/landscape].
Compose with [primary recipe], [foreground/midground/background relationship], stable verticals and intentional negative space.
[Natural light event] creates [shadow/highlight behavior].
Palette: [colors and warm/cool relationship].
[Natural or mildly compressed perspective], [depth-of-field intent], tactile [materials], realistic skin and fabric, restrained color, slight warmth, optional fine grain.
[Aspect/orientation and continuity constraints]. Original composition; no artist-name style tags.
```

Avoid an unprioritized comma cloud. Every clause must control subject, space, light, color, or texture.

## 4. Write negative guidance

For generators that support a negative prompt, start with only the failures relevant to the brief:

```text
studio flash, glamour pose, direct-to-camera influencer smile, neon palette,
busy logos, generic resort showroom, unrelated props, ultrawide distortion,
plastic skin, extreme HDR, crunchy clarity, aggressive orange-and-teal grade,
fake sun rays, excessive haze, heavy vignette, text, watermark
```

For generators without negative prompts, convert the list to positive constraints:

- Use natural directional light only.
- Keep the gesture unperformed and the subject connected to the place.
- Preserve believable materials, skin, shadows, and perspective.
- Use restrained warm color and one site-specific accent.
- Keep logos, signage, and written text out of frame.

## 5. Build a coherent series

Create a continuity sheet before generating:

| Anchor | Lock | Vary |
| --- | --- | --- |
| Place | Architecture, material, climate | Micro-location and camera position |
| Person | Age range, hair, wardrobe base | Gesture, distance, facing direction |
| Light | Time window and color relationship | Direct, reflected, or filtered expression |
| Palette | Four base colors and one accent | Accent presence and shadow density |
| Finish | Contrast, warmth, grain policy | Flare or motion blur on one or two frames |
| Story | One mood sentence | Beat: arrival, threshold, action, detail, residue |

Generate a small candidate set with deliberate variation. Do not produce six paraphrases of the same shot.

## 6. Refine by diagnosis

Change one or two prompt components at a time:

- If it looks staged, replace a pose with a task and move the subject farther from camera.
- If it looks generic, add a local material, ritual, climate cue, or architectural constraint.
- If it looks like a postcard, add a foreground veil, human trace, or imperfect lived detail.
- If it looks too commercial, remove props, logos, symmetry, and polished smiles.
- If it looks muddy, protect one luminous plane and simplify the palette.
- If it looks synthetic, reduce adjectives and specify physical light, material, perspective, and action.
- If it looks derivative, change the composition recipe, setting, action, and sequence role.

## 7. Deliver prompt metadata

Alongside each final prompt, state:

- Sequence beat
- Aspect ratio
- Locked continuity anchors
- One intentional variation
- Negative guidance
- Originality changes from any provided reference

Then score the proposed result with [quality-checklist.md](quality-checklist.md).
