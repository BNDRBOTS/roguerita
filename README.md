# ROGUE RITA™ // ARCADE DIVISION

Three hand-built arcade games about a pentagon named **Rita** who has never once been safe, plus the storefront that sells them for exactly $0.

No build step. No dependencies. No `npm install`. Every game is a single HTML file — the entire stack is "a browser."

## 🚀 Deploy to GitHub Pages (the whole point)

1. Create a new repository on GitHub (public, any name — `roguerita` works).
2. Drag **everything in this folder** (including the `games/` folder) into the repo — either through **Add file → Upload files** on github.com, or `git add . && git commit && git push` if you're fancy.
3. Go to **Settings → Pages → Source**, pick **Deploy from a branch**, choose `main` and `/ (root)`. Save.
4. Wait ~1 minute. Your arcade is live at `https://<your-username>.github.io/<repo-name>/`.

That's it. The site is `index.html`, the PLAY buttons link straight into `games/`, and every path is relative — it works on Pages, on a thumb drive, or double-clicked from your desktop like it's 1997.

## 🗂 What's in the box

```
index.html                                  ← the ROGUE RITA™ site (start here)
.nojekyll                                   ← tells GitHub Pages to serve files as-is
games/
  RogueRita_VaporwaveV1.html                ← "THE TAPE" — silent cut, VHS REWIND
  RogueRita_v2_Vaporwave.html               ← "THE BROADCAST" — loud cut, RESONANCE ENGINE
  RogueRita_CyberArena_BossPackV1.html      ← "THE FINAL BATTLE" — ink cut, BRUSH PARRY
  README_RogueRita_VaporwaveV1.md           ← full manual + bug-fix audit for V1
  README_RogueRita_v2_Vaporwave.md          ← full manual + audit for v2
  README_RogueRita_CyberArena_BossPack.md   ← full manual + audit for the Boss Pack
```

## 🎮 The roster, in one breath

| Game | Vibe | Signature move |
| --- | --- | --- |
| **VAPORWAVE V1** — "The Tape" | Silent neon survival | **◀◀ VHS REWIND** — one death per run gets vetoed; the tape scrubs 4s backward |
| **VAPORWAVE v2** — "The Broadcast" | Same sunset, full synth rig | **🎹 RESONANCE ENGINE** — generative synthwave that adds band members as your combo climbs |
| **CYBER-ARENA** — "The Final Battle" | Sumi-e ink, one titan, four phases | **🖌 BRUSH PARRY** — dash through ink shots to send them home |

## 🕹 Controls (all three)

- **WASD** move · **mouse / hold** fire · **tap-drag** on mobile
- **SPACE** — bullet time (V1/v2) or dash (Boss Pack, double-tap on touch)
- **P** pause · **R** restart · **M** mute (v2 only — the others were born silent)

## 🧪 QA receipts

Every file here survived an automated audit: rendered and screenshot-verified on desktop and mobile viewports, then runtime-played headlessly — start, fight, pause, die, restart — with zero console errors, verified death/rewind/parry paths, and best-score persistence checked against localStorage.

---

ROGUE RITA™ · EST. 2026 · zero investors, zero chill
