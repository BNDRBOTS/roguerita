# ROGUE RITA™: THE FINAL BATTLE — CYBER-ARENA BOSS PACK

> One titan, painted in ink. You are the eraser.

The Boss Pack is the art-house entry in the series — no neon rainbow, no synth sunset. Just black paper, white ink, one cyan accent reserved exclusively for things you're allowed to hurt, and a sumi-e titan that sways like it's already bored of you. This edition keeps that monochrome discipline and makes the fight worthy of the canvas.

---

## HOW TO PLAY

Open the HTML file in a browser. Click to enter the arena.

| Input | Action |
|---|---|
| **WASD** | Move |
| **Mouse (hold)** | Auto-fire at cursor |
| **SPACE** | Dash (i-frames included) — also your **parry**, see below |
| **P** | Pause |
| **R / tap** | Restart |
| **Touch** | Tap/drag to fire, **double-tap to dash** |

---

## THE FIGHT

Four phases, same as always — the structure was never the problem:

0. **THE WARDENS** — two orbiting cyan minions. The bouncer check.
1. **THE SHELL** — four armor plates on the body.
2. **THE JOINTS** — both shoulders and the crown. *This is where the lasers start.*
3. **THE CORE** — one target, everything the titan has left.

### New boss behavior — telegraphed, then lethal
The original titan only knew "shoot volleys" and "radial burst." Now:

- **LASER SWEEPS (phase 2+)** — a dashed cyan warning line locks onto you, hangs for a beat, then becomes a triple-bleed ink beam. The warning is a courtesy. It will not be extended.
- **HOMING INK ORBS (phase 3)** — cyan-ringed orbs from the crown that track you for a couple of seconds before committing to a trajectory. They're patient. Be less predictable.
- **SHOCKWAVE RINGS (phase 3)** — the body pulses a dashed warning circle, then an expanding ink ring floods the arena. Dash through the band or wear it.

### New cinematics & feel
- **Phase title cards** — "PHASE II — THE JOINTS // SHOULDERS AND CROWN. WATCH THE LASERS."
- **Hit-stop** — the world freezes for a few frames when a plate shatters or a joint severs. Impact you can feel in your teeth.
- **Screen shake**, scaled to the drama
- **TITAN INTEGRITY bar** — three-segment readout (SHELL / JOINTS / CORE) so you always know how much monster is left
- Score popups, start card, pause, best score in `localStorage` (`rita_boss_best`)

---

## 🖌 THE ULTRA-UNIQUE: BRUSH PARRY

The dash was already the best button in the game. Now it's a statement.

**Dash through any boss projectile and you parry it.** The ink shot flips allegiance mid-air — reborn as a white-cyan shard that homes directly at the titan's *current weak point*, with a burst, a breath of hit-stop, +60 score, and a `PARRY +60` popup. The parry window is your dash's i-frames plus a shimmering cyan ring around Rita so you know the brush is live. It even sweeps the whole dash path — dash through a volley and the entire volley changes sides.

Dodging keeps you alive. Parrying wins arguments.

---

## AUDIT — BUGS FOUND & FIXED

| Bug | What it did | Fix |
|---|---|---|
| **Naked HUD** | `.stats-panel`, `.player-name`, `.game-tagline`, `.controls-hint` had responsive media queries adjusting padding/backgrounds… that were **never defined at base**. The HUD rendered as unstyled floating text | Full ink-chip styling added — dark blots, white ink borders, asymmetric brutalist radii, cyan accent shadows — matching what the media queries always assumed existed |

---

## DESIGN LANGUAGE (unchanged, on purpose)

- Monochrome sumi-e: `#050505` paper, `#f4f4f4` ink, and `#62f6ff` cyan used *only* for weak points, warnings, and parries — the accent stays sacred
- Triple-pass ink rendering (`drawInkBlob` / `drawInkLine`) for that wet-brush bleed
- The titan still sways, bobs, and telegraphs with its whole body
- Deliberately silent — ink doesn't need a soundtrack

## TECH NOTES

- Single self-contained HTML file, zero dependencies
- Canvas 2D, `requestAnimationFrame` loop with hit-stop gating
- Segment-distance math for laser beams and dash-path parries
- Desktop + mobile (double-tap dash)
