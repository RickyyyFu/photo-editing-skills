# Quality Checklist

Run this checklist on a shoot plan, prompt set, generated image, edit, or sequence before delivery.

## Hard failures

Any hard failure means `revise`, regardless of score:

- The output claims to be official, affiliated, authorized, or endorsed.
- A final generation prompt uses `Roberta Mazzone`, `_lagiuditta`, or another living creator's name as a style tag.
- The plan intentionally recreates a recognizable published composition without meaningful structural changes.
- The work confuses `_lagiuditta` with the Naples-based photographer using `@robertamazzoneph`.
- The output invents a camera body, lens, preset, film stock, or fixed grain recipe as a documented fact.
- A directed portrait lacks an appropriate consent plan, or a fragile/private location is exposed without reason.
- Local culture is reduced to a prop, costume, or false ritual.

## Scorecard

Score each dimension `0`, `1`, or `2`:

- `0` — absent, contradictory, or generic
- `1` — present but weak, inconsistent, or under-specified
- `2` — specific, coherent, and useful

| Dimension | 0 | 1 | 2 |
| --- | --- | --- | --- |
| Place specificity | Generic destination | Some cues | Materials, climate, architecture, or ritual make the place distinct |
| Story interval | Only a hero image | Implied mood | Clear in-between moment, ritual, or residue |
| Architectural composition | Accidental space | Some structure | Lines, negative space, layers, and verticals intentionally organize the frame |
| Natural light | Flat or synthetic | Plausible but vague | Physical source, direction, time, and shadow behavior are clear |
| Color restraint | Noisy or preset-driven | Mostly coherent | Limited palette with purposeful warm/cool relationship |
| Human state | Performed or disconnected | Neutral | Task-based, absorbed, small-scale, or represented by a truthful trace |
| Wardrobe and props | Compete or feel placed | Acceptable | Belong to climate, culture, movement, and story |
| Material texture | Plastic or overprocessed | Some texture | Linen, plaster, stone, wood, water, skin, or weather remain tactile |
| Technical plausibility | Contradictory | Usable | Lens feel, depth, exposure, and motion serve the scene |
| Restraint | Too many effects | One excess | Every element has a job; effects remain secondary |
| Originality | Near-copy | Some changed elements | At least four structural differences and a new narrative purpose |
| Series cohesion | Repetitive or inconsistent | Partial continuity | Stable anchors plus meaningful shot-scale and beat variation |

Maximum score: `24`.

- **20-24**: pass, assuming no hard failure.
- **16-19**: revise the three lowest dimensions.
- **0-15**: rebuild from the mood sentence and a smaller DNA selection.

Composition, light, human state, and originality must each score at least `1`.

## Prompt-specific checks

- [ ] The prompt follows subject/action → place → composition → light → palette → lens/depth → texture → constraints.
- [ ] The main action is plausible and unforced.
- [ ] The environment has narrative agency.
- [ ] The light is physically possible.
- [ ] The palette names a relationship, not a pile of colors.
- [ ] The prompt avoids an adjective cloud and unsupported gear claims.
- [ ] Negative guidance targets actual risks in the prompt.
- [ ] The aspect ratio serves the composition.
- [ ] Series prompts lock continuity without becoming duplicates.
- [ ] The production prompt contains no creator-name style tag.

## Shoot-specific checks

- [ ] The scout plan includes exact light windows and fallback weather.
- [ ] The shot list varies establishing, threshold, human, detail, and residue beats.
- [ ] Wardrobe and props fit climate and place.
- [ ] Subject direction uses tasks rather than beauty poses.
- [ ] RAW/manual guidance is adapted to available equipment.
- [ ] Interior/exterior contrast has a believable exposure plan.
- [ ] The edit recipe preserves texture, rich shadows, and plausible color.
- [ ] Consent, access, cultural respect, and geotag risk are addressed.

## Image or edit checks

- [ ] Vertical lines and horizon are intentional.
- [ ] Foreground obstruction helps immersion rather than blocking the subject accidentally.
- [ ] Highlight detail survives in sky, water, skin, or light fabric where it matters.
- [ ] Shadows retain depth and are not lifted into flat gray.
- [ ] Skin, fabric, plaster, wood, stone, water, and snow look physically distinct.
- [ ] Warmth is slight enough that whites and cool environments remain believable.
- [ ] Grain, flare, haze, vignette, and blur are optional accents, not a blanket effect.
- [ ] There is no accidental text, logo, watermark, malformed anatomy, or impossible reflection.

## Revision protocol

1. Name the three lowest-scoring dimensions.
2. Make one concrete change for each dimension.
3. Preserve the strongest existing decision.
4. Re-score only after the changes are visible in the plan, prompt, or image.
5. Report `pass` or `revise` with the final score and any remaining uncertainty.
