# ROGUE RITA™: VAPORWAVE — V1 "THE TAPE"

> One pentagon. Infinite regret. A sunset that never asked for this.

V1 is the original cut — the silent, mean, arcade-pure version of Rogue Rita. No audio, no mercy, just a neon grid, a gradient sun, and waves of shapes that want you dead. This edition keeps every ounce of that energy and bolts on the stuff the original was clearly dreaming about.

---

## HOW TO PLAY

Open the HTML file in any modern browser. That's it. No install, no build step, no account, no newsletter popup. You're welcome.

| Input | Action |
|---|---|
| **WASD** | Move |
| **Mouse (hold)** | Auto-fire at cursor |
| **SPACE (hold)** | Bullet time — world slows to 30%, you get faster |
| **P** | Pause |
| **R / tap** | Restart after death |
| **Touch** | Tap/drag to aim + fire (mobile works) |

---

## WHAT'S IN THE ARENA

### Enemy roster (new)
The original had one enemy: "pink circle, angry." Now there are five, each with its own silhouette so you can read the battlefield at a glance:

- **DRONE** — the classic pink circle. Walks at you. Honest work.
- **DART** — small cyan diamond. Coasts, then *lunges*. The lunge is the problem.
- **TANK** — big purple hex with a rotating armor ring. Slow, thick, rude.
- **SPLITTER** — orange blob. Kill it and it files for divorce into two **MINIS**.
- **MINI** — tiny, fast, spiteful.

Enemy mix scales by wave — early waves are drones, later waves are a full shape convention.

### Named waves (new)
Every wave gets a title card: *FIRST CONTACT, PINK STATIC, NIGHT DRIVE, CHROME SURF, LASER MALL, DIAL-UP DEMONS, NEON UNDERTOW, GRID LOCK, MIDNIGHT ARCADE, FINAL BROADCAST.* After that the tape loops and it's your problem.

### Combo system (new)
Kills within ~2 seconds of each other chain. Every 5 kills bumps your multiplier (x2, x3, x4…). Score popups show what each kill was worth. The COMBO chip in the HUD burns orange when you're hot. Drop the chain and it all goes back to x1, like it never loved you.

### Feel & effects (new)
- Screen shake scaled to what died
- Muzzle flash + thruster trail
- Floating score popups
- Bullet-time meter with slow-mo tint and vignette
- Start card, pause card, game-over card — all drawn in-canvas, all on-brand
- Best score saved to `localStorage` (`rita_v1_best`)

---

## ◀◀ THE ULTRA-UNIQUE: VHS REWIND

Once per run — **once** — death doesn't stick.

The instant you'd die, the tape scrubs backward. Four seconds of your run play in reverse with genuine VHS damage: slice jitter, a rolling tracking band, a blinking `◀◀ REWIND` OSD in the corner. Then the tape catches, `◀◀ TAPE RESTORED` flashes, and you're back before your mistake with a couple of hit points and brief invincibility.

It's implemented as a ring buffer of game-state snapshots (one every 3 frames, ~80 kept), popped 3-per-frame during the rewind so time visibly runs backward — enemies un-move, bullets un-fly, your bad decision un-happens. One per tape. Spend it with dignity.

---

## AUDIT — BUGS FOUND & FIXED

| Bug | What it did | Fix |
|---|---|---|
| Double wave increment | `wave++` lived in BOTH the kill handler and `manageWaves()`, so waves could skip entirely | Wave advancement now lives only in `manageWaves()` |
| Dirty restart | Restart didn't reset bullet time, time scale, frame counter | Full state reset |
| Game-over layout | Text positioned by magic pixel offsets | Proper `textAlign: center` |
| Space scrolls page | Bullet time scrolled the browser | `preventDefault` |
| Sticky autofire | Releasing mouse off-canvas kept firing forever | `mouseup` on window + `mouseleave` handler |
| "TAP TO RESTART" was a lie | Text said it; code didn't | Now actually restarts |
| Stray `<` at EOF | Cosmetic HTML garbage | Removed |

---

## DESIGN LANGUAGE (unchanged, on purpose)

- Palette: `#00f0ff` cyan / `#ff71ce` pink / `#05ffa1` mint / `#ffb347` orange / `#b967ff` purple on `#0f0b1a`
- Space Grotesk, neo-brutalist asymmetric radii (`42px 12px 42px 12px`), animated border glint
- Scanlines + SVG noise overlays, hand-jittered "rough" shape rendering
- Perspective grid + gradient sun — the sunset stays
- Still **deliberately silent**. V1 is the quiet one. If you want the soundtrack, that's v2's whole personality.

## TECH NOTES

- Single self-contained HTML file, zero dependencies
- Canvas 2D, CSS-pixel sizing (as original), `requestAnimationFrame` loop
- Works desktop + mobile
