# ROGUE RITA™ // ARCADE DIVISION

ROGUE RITA™ is a static browser arcade and storefront containing three self-contained Canvas 2D games. The repository has no build system, package manager, backend, database, framework, or bundled asset pipeline. The site and all three games run directly from HTML files.

**Canonical release branch:** `v3`. GitHub Pages is deployed from `v3`.

## What is actually in this repository

```text
README.md
index.html
games/
├── README_RogueRita_CyberArena_BossPack.md
├── README_RogueRita_VaporwaveV1.md
├── README_RogueRita_v2_Vaporwave.md
├── RogueRita_CyberArena_BossPackV1.html
├── RogueRita_VaporwaveV1.html
└── RogueRita_v2_Vaporwave.html
```

Current source inventory: **8 files / 6,182 lines**.

The previous README listed a `.nojekyll` file, but that file is not present in the repository. No `.nojekyll` file is required for the current filenames and paths.

## Repository behavior

- `index.html` is the public landing page and storefront.
- Every game is one self-contained HTML file under `games/`.
- The three game cards on `index.html` link directly to those public HTML files.
- The games remain fully playable at `$0`; the SYNTHLORD card is optional one-time support at a customer-chosen amount of `$1+`.
- Optional support uses a live Stripe-hosted Payment Link: `https://buy.stripe.com/6oU4gz9cfcwG1FG4Qw0oM0x`.
- The games themselves use no network requests, external scripts, authentication, analytics, or backend. Payment is handled externally by Stripe-hosted Checkout; no Stripe secret keys are present in the repository.
- The CSS names `Space Grotesk`, but no font file or web-font import is included; browsers use it only when locally available, otherwise they fall back to `Courier New` or monospace.
- Scores are stored only in browser `localStorage`.
- No repository-level automated tests, build scripts, service worker, manifest, license file, or deployment workflow are included.

## Run locally

Open `index.html` in a modern browser.

The individual games can also be opened directly:

```text
games/RogueRita_VaporwaveV1.html
games/RogueRita_v2_Vaporwave.html
games/RogueRita_CyberArena_BossPackV1.html
```

No installation or local server is required for the current code.

## Game roster

| Game | File | Core structure | Signature system | Audio | Saved score key |
|---|---|---|---|---|---|
| **VAPORWAVE V1 — “THE TAPE”** | `games/RogueRita_VaporwaveV1.html` | Endless survival waves against five geometric enemy types | One VHS rewind per run | Generated lo-fi WebAudio tape deck | `rita_v1_best` |
| **VAPORWAVE v2 — “THE BROADCAST”** | `games/RogueRita_v2_Vaporwave.html` | V1-style survival plus pickups and a responsive audio engine | Combo-gated Resonance Engine | Generated with WebAudio | `rita_v2_best` |
| **CYBER-ARENA — “BOSS PACK”** | `games/RogueRita_CyberArena_BossPackV1.html` | One titan encounter: wardens, shell, joints, core | Dash-through-projectile Brush Parry | Generated phase-driven WebAudio war drone | `rita_boss_best` |

## Controls

### Vaporwave V1

- `W`, `A`, `S`, `D`: move
- Mouse hold: aim and auto-fire
- Touch: left virtual stick moves; drag the arena to aim and auto-fire
- Touch: BULLET TIME button holds bullet time
- `Space` hold: bullet time
- `P`: pause/resume
- `R` or tap after death: restart

### Vaporwave v2

- `W`, `A`, `S`, `D`: move
- Mouse hold: aim and auto-fire
- Touch hold/drag: aim and auto-fire
- `Space` hold: bullet time
- `P`: pause/resume
- `M`: mute/unmute
- `R` or tap after death: restart

### Cyber-Arena Boss Pack

- `W`, `A`, `S`, `D`: move
- Mouse hold: aim and auto-fire
- Touch: left virtual stick moves; drag the arena to aim and auto-fire
- Touch: DASH/PARRY button or double-tap to dash
- `Space`: dash
- Double-tap on touch: dash
- `P`: pause/resume
- `R` or tap after the run: restart

## Implementation details

### Landing page

`index.html` contains all landing-page HTML, CSS, and JavaScript.

Its only JavaScript is a decorative desktop mouse-follow effect for `.hero-sun`. The page contains:

- sticky navigation
- hero section
- three playable game cards
- feature grid
- two `$0` joke tiers plus one live `$1+` optional support tier
- fictional testimonials
- FAQ
- footer

The three game buttons use relative paths, so the site can run from GitHub Pages or from a local folder.

### Vaporwave V1 — The Tape

V1 uses a CSS-pixel Canvas 2D render loop driven by `requestAnimationFrame`.

Source-defined behavior includes:

- five starting health
- enemy types: `drone`, `dart`, `tank`, `splitter`, and `mini`
- score multipliers that increase every five chained kills
- a 120-frame combo window
- bullet time that slows the simulation to `0.3`
- named wave banners
- continuous hold-fire at a 140 ms interval
- best-score persistence under `rita_v1_best`
- one rewind per run when enough state history exists

The rewind records one snapshot every three frames and keeps up to 80 snapshots. On a lethal hit, it replays stored state backward, restores at least two health, grants temporary invincibility, and consumes the run’s single rewind.

### Vaporwave v2 — The Broadcast

v2 retains the survival structure and adds a more defensive browser/mobile implementation:

- device-pixel-ratio-aware canvas rendering, capped at `3`
- `ResizeObserver`
- `visualViewport` resize handling
- safe-area inset support
- visibility-based audio suspend/resume
- pointer-specific control text

Its pickups are generated on roughly 12% of enemy kills:

- `triple`: three-shot spread for 720 frames
- `shield`: absorbs one hit and stacks to two
- `overdrive`: adds a second firing interval for 480 frames

The WebAudio graph is created after user interaction and contains separate music and SFX buses, a music low-pass filter, a dynamics compressor, and a master gain.

The Resonance Engine runs at 112 BPM through a 25 ms look-ahead scheduler:

1. x1 combo: kick and hats
2. x2 combo: bass added
3. x3 combo: arpeggio added
4. x4 or higher: pad layer added

Bullet time moves the music filter toward 420 Hz and restores it toward 16 kHz afterward.

### Cyber-Arena Boss Pack

The Boss Pack is a fixed multi-stage encounter with seven player health.

The encounter is coded as:

1. **Wardens:** two orbiting minions with eight HP each
2. **Shell:** four armor plates with five HP each
3. **Joints:** two shoulders and the crown with seven HP each
4. **Core:** one core with 18 HP

Boss attacks include:

- aimed hand volleys
- radial projectile bursts
- telegraphed laser lines in later phases
- homing orbs in the core phase
- expanding shockwave rings in the core phase

A dash grants brief invincibility and an 18-frame parry window. Projectiles intersecting the dash path are converted into homing player projectiles. Each successful parry adds 60 points.

The game also contains hit-stop, screen shake, phase banners, an integrity bar, touch double-tap dash handling, victory presentation, and best-score persistence under `rita_boss_best`.

## GitHub Pages deployment

For this exact repository structure:

1. Open the repository’s **Settings**.
2. Open **Pages**.
3. Choose **Deploy from a branch**.
4. Select `v3`.
5. Select `/ (root)`.
6. Save.

The landing page uses only relative game paths, so no path rewrite is required.

---

# Operator instruction sheet

## 1. Current live monetization

ROGUE RITA currently uses **public/free play + optional one-time Stripe support**. The complete games remain public under `/games/`; payment does not gate access.

- Live support product: **ROGUE RITA™ Arcade Support**
- Customer chooses any one-time amount from **$1 USD and up**
- Checkout is Stripe-hosted; no secret keys or backend code are required
- Live Payment Link: `https://buy.stripe.com/6oU4gz9cfcwG1FG4Qw0oM0x`

If the business model later changes to paid-only access, do not leave the full paid HTML game files in this public Pages repository. Move paid deliverables to private fulfillment first, then replace public play links with demos or checkout links.

## 2. Optional future Gumroad distribution

The Gumroad placeholders below are not required for the current live Stripe support flow. They are retained only as a future distribution option.

Replace every placeholder below with your real URL:

```text
GUMROAD_STORE_URL=https://YOUR-GUMROAD-STORE
GUMROAD_V1_URL=https://YOUR-GUMROAD-V1-PRODUCT
GUMROAD_V2_URL=https://YOUR-GUMROAD-V2-PRODUCT
GUMROAD_BOSS_URL=https://YOUR-GUMROAD-BOSS-PRODUCT
GUMROAD_BUNDLE_URL=https://YOUR-GUMROAD-BUNDLE
GUMROAD_LICENSE_URL=https://YOUR-GUMROAD-COMMERCIAL-LICENSE
```

There is no configuration file or environment variable system in this repository. URLs must be placed directly in `index.html`.

## 3. Top-level Gumroad links

Open `index.html`.

### Navigation button

Find this exact anchor:

```html
<a class="nav-cta" href="#pricing">INSERT COIN</a>
```

Replace it with:

```html
<a class="nav-cta" href="GUMROAD_STORE_URL" target="_blank" rel="noopener noreferrer">INSERT COIN</a>
```

### Hero payment button

Find:

```html
<a class="btn-big btn-ghost" href="#pricing">PAY US (OPTIONAL)</a>
```

Replace it with:

```html
<a class="btn-big btn-ghost" href="GUMROAD_BUNDLE_URL" target="_blank" rel="noopener noreferrer">PAY US (OPTIONAL)</a>
```

## 4. Per-game card links

### Donation / pay-what-you-want mode

Keep the existing direct play buttons unchanged:

```html
<a class="btn-big btn-primary play-btn" href="games/RogueRita_VaporwaveV1.html">▶ INSERT TAPE</a>
<a class="btn-big btn-primary play-btn" href="games/RogueRita_v2_Vaporwave.html">▶ GO LIVE ON AIR</a>
<a class="btn-big btn-primary play-btn" href="games/RogueRita_CyberArena_BossPackV1.html">▶ FACE THE TITAN</a>
```

Add one Gumroad anchor immediately **after** each corresponding play anchor:

```html
<a class="price-btn" href="GUMROAD_V1_URL" target="_blank" rel="noopener noreferrer">GET / SUPPORT THE TAPE ▸</a>
```

```html
<a class="price-btn" href="GUMROAD_V2_URL" target="_blank" rel="noopener noreferrer">GET / SUPPORT THE BROADCAST ▸</a>
```

```html
<a class="price-btn" href="GUMROAD_BOSS_URL" target="_blank" rel="noopener noreferrer">GET / SUPPORT THE BOSS PACK ▸</a>
```

### Paid-access mode

Replace the three direct public game anchors instead:

```html
<a class="btn-big btn-primary play-btn" href="GUMROAD_V1_URL" target="_blank" rel="noopener noreferrer">▶ GET THE TAPE</a>
<a class="btn-big btn-primary play-btn" href="GUMROAD_V2_URL" target="_blank" rel="noopener noreferrer">▶ GET THE BROADCAST</a>
<a class="btn-big btn-primary play-btn" href="GUMROAD_BOSS_URL" target="_blank" rel="noopener noreferrer">▶ GET THE BOSS PACK</a>
```

Then remove the corresponding complete paid HTML files from the public repository or replace them with intentionally limited demos:

```text
games/RogueRita_VaporwaveV1.html
games/RogueRita_v2_Vaporwave.html
games/RogueRita_CyberArena_BossPackV1.html
```

## 5. Pricing-card Gumroad links

The current pricing buttons all return visitors to `#games`.

### FREELOADER button

Find:

```html
<a class="price-btn" href="#games">START DYING ▸</a>
```

For a free or pay-what-you-want bundle, replace it with:

```html
<a class="price-btn" href="GUMROAD_BUNDLE_URL" target="_blank" rel="noopener noreferrer">START DYING ▸</a>
```

### SYNTHLORD button

Find:

```html
<a class="price-btn" href="#games">ASCEND ▸</a>
```

Replace it with:

```html
<a class="price-btn" href="GUMROAD_BUNDLE_URL" target="_blank" rel="noopener noreferrer">ASCEND ▸</a>
```

### TITAN SLAYER button

Find:

```html
<a class="price-btn" href="#games">GO CORPORATE ▸</a>
```

Replace it with:

```html
<a class="price-btn" href="GUMROAD_LICENSE_URL" target="_blank" rel="noopener noreferrer">GO CORPORATE ▸</a>
```

## 6. Required copy corrections when charging money

Do not add paid checkout links while leaving contradictory `$0` and “already unlocked” claims in place.

In `index.html`, review and update all of these exact current claims:

```text
THREE TIERS. ALL OF THEM ARE JOKES. ALL OF THEM WORK.
The games are files. You already have them.
$0
FOREVER / NO CATCH / WE CHECKED
All three games, fully unlocked
$0
PER MONTH / BILLED NEVER
Same games. We cannot stress this enough
$0
PER YEAR / SAVE 100% ANNUALLY
* ALL TIERS INCLUDE THE FULL GAMES BECAUSE THEY'RE HTML FILES...
Is it really free?
Yes. They're HTML files. Charging you would require building a checkout page...
```

Also review these broader public-access claims before using paid-access mode:

```text
No login wall between you and dying beautifully.
NO ACCOUNTS
No account.
The games are files. You already have them.
```

Keep those claims only when they remain literally true.

## 7. Optional Gumroad embed script

Plain Gumroad links require no script and preserve the repository’s dependency-free architecture.

Only add a Gumroad-provided overlay/embed script when you intentionally want that behavior. Place any such script at the end of `index.html`, immediately before:

```html
</body>
```

Do not place payment scripts inside any game HTML file unless the game itself must display checkout controls.

## 8. Final verification

After editing:

1. Search the repository for `GUMROAD_`. No placeholders should remain.
2. Search `index.html` for `href="#pricing"` and confirm any remaining internal jump is intentional.
3. Search `index.html` for `href="#games"` and confirm any remaining internal jump is intentional.
4. Click every top-level, game-card, and pricing-card checkout link.
5. Test each Gumroad URL in a private/incognito browser window.
6. Confirm external links include `target="_blank"` and `rel="noopener noreferrer"`.
7. In paid-access mode, directly request all three former `/games/*.html` URLs and verify the full paid games are no longer publicly accessible.
8. Verify the landing page still loads from the GitHub Pages project path.
9. Verify each remaining playable game starts, pauses, restarts, and stores its best score.
10. Verify v2 audio starts only after a user gesture and that `M` still mutes it.

## Source integrity snapshot

```text
README.md                                      9cd79a69263d5ac48f7fef052d59a6b820e91a1c
index.html                                     dc6b1901a009abb05115a30b7a4edf8187f0d744
games/README_RogueRita_CyberArena_BossPack.md 770704d9e4d06bc8a7b081e08493243609ed77fb
games/README_RogueRita_VaporwaveV1.md         50cc3945c390aeccb509fe814cc51443622d83bc
games/README_RogueRita_v2_Vaporwave.md        09a3b3379e8d4f53d054026bd4a3b070369504ac
games/RogueRita_CyberArena_BossPackV1.html    4055d3474c62fe40241259d4923c302fc02bde16
games/RogueRita_VaporwaveV1.html              492dfe2c300f3daad98afa8a84a6758a5e4ecc77
games/RogueRita_v2_Vaporwave.html             1a41aa1bdb2a9d49ad19b10caf5473b507869935
```
