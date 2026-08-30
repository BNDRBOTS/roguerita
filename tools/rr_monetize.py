from pathlib import Path

PAY='https://buy.stripe.com/6oU4gz9cfcwG1FG4Qw0oM0x'

p=Path('index.html')
s=p.read_text()
repls={
'<a class="btn-big btn-ghost" href="#pricing">PAY US (OPTIONAL)</a>':f'<a class="btn-big btn-ghost" href="{PAY}" target="_blank" rel="noopener noreferrer">PAY US (OPTIONAL)</a>',
'<span class="hot-tag">MOST POPULAR (IT\'S THE SAME)</span>':'<span class="hot-tag">OPTIONAL SUPPORT · SAME GAMES</span>',
'<div class="price">$0</div>\n        <div class="per">PER MONTH / BILLED NEVER</div>':'<div class="price">$1+</div>\n        <div class="per">ONE TIME / YOU CHOOSE THE AMOUNT</div>',
'''          <li>Everything in FREELOADER</li>\n          <li>The smug feeling of choosing the middle tier</li>\n          <li>Permission to call yourself a Synthlord</li>\n          <li>Same games. We cannot stress this enough</li>''':'''          <li>Everything in FREELOADER</li>\n          <li>Choose any support amount from $1 up</li>\n          <li>No account or subscription</li>\n          <li>Same games — payment is completely optional</li>''',
'''        <!-- ===== GUMROAD ==============================================\n             Paste your Gumroad product link into the href below\n             (it looks like https://YOURNAME.gumroad.com/l/roguerita).\n             That single edit turns this button into real checkout.\n             No keys, no scripts - Gumroad checkout is just a link. -->\n        <a class="price-btn" data-checkout="gumroad" href="#games">ASCEND ▸</a>''':f'''        <a class="price-btn" data-checkout="stripe" href="{PAY}" target="_blank" rel="noopener noreferrer">BACK RITA ▸</a>''',
'''      <p>Yes. They're HTML files. Charging you would require building a checkout page, and we'd rather build another boss. Priorities.</p>''':'''      <p>Yes. All three games are fully playable for free. If you want to back the arcade, the optional SYNTHLORD support tier lets you choose any one-time amount from $1 up.</p>''',
'''    <p class="fine-print">* ALL TIERS INCLUDE THE FULL GAMES BECAUSE THEY'RE HTML FILES AND WE'RE NOT MONSTERS. THE TITAN IS THE MONSTER.</p>''':'''    <p class="fine-print">* ALL THREE GAMES STAY FULLY PLAYABLE AT $0. SYNTHLORD IS OPTIONAL ONE-TIME SUPPORT THROUGH STRIPE.</p>'''
}
for old,new in repls.items():
    if s.count(old)!=1:
        raise SystemExit(f'index anchor mismatch: {old[:80]!r} count={s.count(old)}')
    s=s.replace(old,new,1)
if s.count(PAY)!=2:
    raise SystemExit(f'expected 2 live Stripe links, found {s.count(PAY)}')
p.write_text(s)

p=Path('README.md')
s=p.read_text()
repls={
'**Source snapshot documented here:** `main` at commit `c1496d944865ca3d80575e7cdc6de0e267d56575`.':'**Canonical release branch:** `v3`. GitHub Pages is deployed from `v3`.',
'- All current pricing cards display `$0`.':'- The games remain fully playable at `$0`; the SYNTHLORD card is optional one-time support at a customer-chosen amount of `$1+`.',
'- All current purchase-style calls to action point to internal page sections, not Gumroad or another checkout.':f'- Optional support uses a live Stripe-hosted Payment Link: `{PAY}`.',
'- No network requests, external scripts, external stylesheets, API calls, authentication, analytics, or payment integration are implemented.':'- The games themselves use no network requests, external scripts, authentication, analytics, or backend. Payment is handled externally by Stripe-hosted Checkout; no Stripe secret keys are present in the repository.',
'| **VAPORWAVE V1 — “THE TAPE”** | `games/RogueRita_VaporwaveV1.html` | Endless survival waves against five geometric enemy types | One VHS rewind per run | None | `rita_v1_best` |':'| **VAPORWAVE V1 — “THE TAPE”** | `games/RogueRita_VaporwaveV1.html` | Endless survival waves against five geometric enemy types | One VHS rewind per run | Generated lo-fi WebAudio tape deck | `rita_v1_best` |',
'| **CYBER-ARENA — “BOSS PACK”** | `games/RogueRita_CyberArena_BossPackV1.html` | One titan encounter: wardens, shell, joints, core | Dash-through-projectile Brush Parry | None | `rita_boss_best` |':'| **CYBER-ARENA — “BOSS PACK”** | `games/RogueRita_CyberArena_BossPackV1.html` | One titan encounter: wardens, shell, joints, core | Dash-through-projectile Brush Parry | Generated phase-driven WebAudio war drone | `rita_boss_best` |',
'- Touch hold/drag: aim and auto-fire\n- `Space` hold: bullet time':'- Touch: left virtual stick moves; drag the arena to aim and auto-fire\n- Touch: BULLET TIME button holds bullet time\n- `Space` hold: bullet time',
'- Touch hold/drag: aim and auto-fire\n- `Space`: dash':'- Touch: left virtual stick moves; drag the arena to aim and auto-fire\n- Touch: DASH/PARRY button or double-tap to dash\n- `Space`: dash',
'- three `$0` pricing cards':'- two `$0` joke tiers plus one live `$1+` optional support tier',
'4. Select `main`.':'4. Select `v3`.'
}
for old,new in repls.items():
    if old not in s:
        raise SystemExit(f'README anchor missing: {old[:80]!r}')
    s=s.replace(old,new,1)
# Replace obsolete operator opening with current state while retaining later paid-access/Gumroad notes as future options.
start=s.index('# Operator instruction sheet')
marker=s.index('## 2. Prepare these exact URL values', start)
new='''# Operator instruction sheet\n\n## 1. Current live monetization\n\nROGUE RITA currently uses **public/free play + optional one-time Stripe support**. The complete games remain public under `/games/`; payment does not gate access.\n\n- Live support product: **ROGUE RITA™ Arcade Support**\n- Customer chooses any one-time amount from **$1 USD and up**\n- Checkout is Stripe-hosted; no secret keys or backend code are required\n- Live Payment Link: `'''+PAY+'''`\n\nIf the business model later changes to paid-only access, do not leave the full paid HTML game files in this public Pages repository. Move paid deliverables to private fulfillment first, then replace public play links with demos or checkout links.\n\n## 2. Optional future Gumroad distribution\n\nThe Gumroad placeholders below are not required for the current live Stripe support flow. They are retained only as a future distribution option.\n\n'''
s=s[:start]+new+s[marker+len('## 2. Prepare these exact URL values\n\n'):]
p.write_text(s)
print('monetization patch applied')