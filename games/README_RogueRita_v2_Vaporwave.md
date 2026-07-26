# ROGUE RITA™: VAPORWAVE — v2 "THE BROADCAST"

> Same sunset. Now it has a band.

v2 is the production cut — DPI-aware rendering, safe-area insets, a full WebAudio synth rig, mobile handling that actually respects your notch. This edition keeps all of that engineering and turns the dial until the speaker cones flex.

---

## HOW TO PLAY

Open the HTML file in a browser. Click once to start (that click also wakes the audio engine — browsers are paranoid like that).

| Input | Action |
|---|---|
| **WASD** | Move |
| **Mouse (hold)** | Auto-fire at cursor |
| **SPACE (hold)** | Bullet time — and the soundtrack dives underwater with you |
| **P** | Pause |
| **M** | Mute |
| **R / tap** | Restart after death |
| **Touch** | Tap/drag to fire; full mobile support |

---

## WHAT'S NEW

### Enemy roster
Same five-archetype lineup as V1 — **DRONE, DART, TANK, SPLITTER, MINI** — because a shared bestiary across the series is a feature, not laziness. Darts lunge, tanks wear rotating armor rings, splitters multiply out of spite.

### Power-ups (new)
~12% of kills drop a bobbing pickup chip. Grab it before it blinks out:

- **T — TRIPLE SHOT** · three-round spread for 12 seconds
- **S — SHIELD** · eats one hit, stacks to two, draws a dashed ring around you
- **O — OVERDRIVE** · doubles your fire rate and turns your shots amber for 8 seconds

### Combo system
Chain kills to climb multipliers (x2 every 5 kills). Popups show the math. Lose the chain, lose the bonus — and, more painfully, lose the band (see below).

### Feel & effects
Screen shake, hit flashes, score popups, thruster trail, named wave banners with fanfare stingers, slow-mo tint + vignette, canvas-drawn start/pause/game-over cards, best score in `localStorage` (`rita_v2_best`).

---

## 🎹 THE ULTRA-UNIQUE: THE RESONANCE ENGINE

v2 was already the game with a synthesizer where its heart should be, so its signature feature is this: **the soundtrack is generative, and you have to earn it.**

A 112 BPM synthwave loop is scheduled in real time through WebAudio (proper lookahead scheduler, not `setTimeout` amateur hour). It's built in layers, and layers only wake up while your combo multiplier holds:

| Tier | Multiplier | The band so far |
|---|---|---|
| 0 | x1 | Kick + hats. A drum machine alone in a mall. |
| 1 | x2 | + sawtooth bassline (A-minor, obviously) |
| 2 | x3 | + 16th-note square arp |
| 3 | x4+ | + pad swells. FULL BAND. You did this. |

Drop your combo and the layers fall away one by one, which is somehow more devastating than losing health. A RESONANCE meter above the bullet-time bar shows which layers you've earned.

And the flex: holding **bullet time sweeps a lowpass filter across the entire music bus** — the whole mix ducks underwater at 420 Hz while the world slows, then blooms back to 16 kHz when you let go. Every SFX still cuts through on its own bus.

---

## AUDIT — BUGS FOUND & FIXED

| Bug | What it did | Fix |
|---|---|---|
| Double wave increment | `wave++` in both the kill handler and `manageWaves()` — waves could skip | Single source of truth in `manageWaves()` |

Yes, just the one — v2's original code was already the responsible sibling. Everything else here is additive.

## PRESERVED ENGINEERING (untouched, because it was right)

- DPR-aware canvas with pixel-ratio cap, `ResizeObserver` + `visualViewport` handling
- Safe-area inset padding for notched phones
- Audio graph: sources → buses → compressor → master (0.22); shared noise buffer; stereo panning by screen position
- Audio suspend/resume on tab visibility; unlock on first gesture
- Coarse-pointer detection swaps the control hint text

## DESIGN LANGUAGE (unchanged, on purpose)

Same vaporwave DNA as V1: `#00f0ff` / `#ff71ce` / `#05ffa1` / `#ffb347` / `#b967ff` on `#0f0b1a`, Space Grotesk, glinting asymmetric border, scanlines + noise, perspective grid, gradient sun, pill-chip HUD. "ROGUE RESONANCE // 2026" stays on the marquee — in this version it's finally literal.

## TECH NOTES

- Single self-contained HTML file, zero dependencies
- Canvas 2D + WebAudio, `requestAnimationFrame` loop, lookahead music scheduler (25ms tick / 120ms horizon)
- Desktop + mobile
