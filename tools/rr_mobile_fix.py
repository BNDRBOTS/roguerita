from pathlib import Path

G = Path('games')

CSS = r'''
/* Mobile controls are additive. Desktop layout/gameplay remains unchanged. */
.mobile-controls{display:none}
@media (max-width:900px),(pointer:coarse){
  .stats-panel,.game-tagline,.controls-hint,.player-name,.top-hud{pointer-events:none}
  .controls-hint{display:none}
  .mobile-controls{display:block;position:absolute;inset:0;z-index:35;pointer-events:none}
  .mobile-stick{position:absolute;left:calc(16px + var(--sal));bottom:calc(16px + var(--sab));width:116px;height:116px;border-radius:50%;border:2px solid rgba(255,255,255,.52);background:rgba(5,5,12,.30);box-shadow:inset 0 0 24px rgba(255,255,255,.06),0 0 18px rgba(0,240,255,.16);pointer-events:auto;touch-action:none}
  .mobile-stick-knob{position:absolute;left:50%;top:50%;width:48px;height:48px;margin:-24px 0 0 -24px;border-radius:50%;background:rgba(255,255,255,.86);border:2px solid #00f0ff;box-shadow:0 0 14px rgba(0,240,255,.7);pointer-events:none}
  .mobile-actions{position:absolute;right:calc(16px + var(--sar));bottom:calc(16px + var(--sab));display:flex;flex-direction:column;align-items:flex-end;gap:10px;pointer-events:none}
  .mobile-action{min-width:78px;min-height:52px;padding:8px 10px;border-radius:20px 6px 20px 6px;border:2px solid #00f0ff;background:rgba(15,11,26,.82);color:#f4f4f4;font:800 11px/1.15 "Courier New",monospace;letter-spacing:.8px;box-shadow:3px 3px 0 rgba(255,113,206,.45);pointer-events:auto;touch-action:none}
  .mobile-action:active,.mobile-action.is-active{transform:translate(2px,2px);box-shadow:none}
  .mute-btn{top:calc(14px + var(--sat));right:calc(14px + var(--sar));pointer-events:auto}
  .player-name{right:calc(12px + var(--sar));bottom:calc(10px + var(--sab))}
}
'''

BOSS_CSS = CSS.replace('#00f0ff','#62f6ff').replace('rgba(15,11,26,.82)','rgba(10,10,10,.82)').replace('rgba(255,113,206,.45)','rgba(255,255,255,.22)')

HTML_BULLET = r'''
    <div class="mobile-controls">
      <div class="mobile-stick" id="mobileStick" aria-label="Move"><div class="mobile-stick-knob" id="mobileStickKnob"></div></div>
      <div class="mobile-actions"><button class="mobile-action" id="mobilePause" type="button">PAUSE</button><button class="mobile-action" id="mobileSpecial" type="button">BULLET<br>TIME</button></div>
    </div>
'''

HTML_BOSS = r'''
    <div class="mobile-controls">
      <div class="mobile-stick" id="mobileStick" aria-label="Move"><div class="mobile-stick-knob" id="mobileStickKnob"></div></div>
      <div class="mobile-actions"><button class="mobile-action" id="mobilePause" type="button">PAUSE</button><button class="mobile-action" id="mobileSpecial" type="button">DASH<br>PARRY</button></div>
    </div>
'''

JS = r'''
function installMobileControls(specialMode){
  const stick=document.getElementById('mobileStick'),knob=document.getElementById('mobileStickKnob'),pauseBtn=document.getElementById('mobilePause'),specialBtn=document.getElementById('mobileSpecial');
  if(!stick||!knob||!pauseBtn||!specialBtn)return;
  const pressed={w:false,a:false,s:false,d:false};let pointerId=null;
  const send=(key,type='keydown')=>window.dispatchEvent(new KeyboardEvent(type,{key,bubbles:true,cancelable:true}));
  function setKey(k,on){if(pressed[k]===on)return;pressed[k]=on;send(k,on?'keydown':'keyup')}
  function vector(x,y){const dead=.28;setKey('a',x<-dead);setKey('d',x>dead);setKey('w',y<-dead);setKey('s',y>dead)}
  function releaseStick(){vector(0,0);knob.style.transform='translate(0px,0px)';pointerId=null}
  function moveStick(e){if(e.pointerId!==pointerId)return;const r=stick.getBoundingClientRect(),m=r.width*.32;let dx=e.clientX-r.left-r.width/2,dy=e.clientY-r.top-r.height/2,L=Math.hypot(dx,dy);if(L>m){dx=dx/L*m;dy=dy/L*m}knob.style.transform=`translate(${dx.toFixed(1)}px,${dy.toFixed(1)}px)`;vector(dx/m,dy/m)}
  stick.addEventListener('pointerdown',e=>{if(e.pointerType==='mouse')return;e.preventDefault();e.stopPropagation();pointerId=e.pointerId;try{stick.setPointerCapture(pointerId)}catch(_){}moveStick(e)});
  stick.addEventListener('pointermove',e=>{if(e.pointerId===pointerId){e.preventDefault();moveStick(e)}});
  stick.addEventListener('pointerup',e=>{if(e.pointerId===pointerId)releaseStick()});stick.addEventListener('pointercancel',e=>{if(e.pointerId===pointerId)releaseStick()});stick.addEventListener('lostpointercapture',releaseStick);
  pauseBtn.addEventListener('pointerdown',e=>{e.preventDefault();e.stopPropagation();send('p');setTimeout(()=>send('p','keyup'),40)});
  if(specialMode==='hold-space'){
    let spid=null;const off=()=>{if(spid===null)return;send(' ','keyup');spid=null;specialBtn.classList.remove('is-active')};
    specialBtn.addEventListener('pointerdown',e=>{e.preventDefault();e.stopPropagation();spid=e.pointerId;specialBtn.classList.add('is-active');send(' ','keydown');try{specialBtn.setPointerCapture(spid)}catch(_){}});
    specialBtn.addEventListener('pointerup',off);specialBtn.addEventListener('pointercancel',off);specialBtn.addEventListener('lostpointercapture',off);window.addEventListener('blur',off);
  }else specialBtn.addEventListener('pointerdown',e=>{e.preventDefault();e.stopPropagation();send(' ','keydown');setTimeout(()=>send(' ','keyup'),40)});
  window.addEventListener('blur',releaseStick);window.addEventListener('pagehide',()=>{releaseStick();send(' ','keyup')});
}
'''

def once(s,old,new,label):
    n=s.count(old)
    if n!=1: raise RuntimeError(f'{label}: expected 1 anchor, found {n}')
    return s.replace(old,new,1)

def source(name):
    core=G/(Path(name).stem+'_core.html')
    p=G/name
    return (core if core.exists() else p).read_text()

# V1
name='RogueRita_VaporwaveV1.html'; s=source(name)
s=once(s,'<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">','<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">','v1 viewport')
s=once(s,'    <style>\n','    <style>\n        :root { --sat: env(safe-area-inset-top,0px); --sab: env(safe-area-inset-bottom,0px); --sal: env(safe-area-inset-left,0px); --sar: env(safe-area-inset-right,0px); }\n','v1 root')
s=once(s,'        @media (max-width: 900px), (pointer: coarse) {\n            .stats-panel { right: 72px; }\n        }\n</style>','        @media (max-width: 900px), (pointer: coarse) {\n            .stats-panel { top: calc(12px + var(--sat)); left: calc(12px + var(--sal)); right: calc(72px + var(--sar)); }\n            .game-tagline { top: calc(102px + var(--sat)); }\n        }\n'+CSS+'</style>','v1 css')
s=once(s,'    <div class="controls-hint" id="controlHint">\n        [ WASD + MOUSE | SPACE: BULLET TIME | P: PAUSE | M: MUTE ]  ·  TAP/DRAG TO FIRE\n    </div>\n</div>','    <div class="controls-hint" id="controlHint">\n        [ WASD + MOUSE | SPACE: BULLET TIME | P: PAUSE | M: MUTE ]  ·  TAP/DRAG TO FIRE\n    </div>\n'+HTML_BULLET+'</div>','v1 html')
s=once(s,"        const hintEl = document.getElementById('controlHint');\n        // mobile-first: touch players get touch instructions, not a keyboard manual\n        if (window.matchMedia('(pointer: coarse)').matches) {\n            hintEl.textContent = '[ TAP/DRAG TO FIRE · 🔊 BUTTON: VOLUME ]';\n        }","        const hintEl = document.getElementById('controlHint');\n        const touchMode = window.matchMedia('(pointer: coarse)').matches || ('ontouchstart' in window);\n        if (touchMode) hintEl.textContent = '[ LEFT STICK: MOVE · DRAG ARENA: FIRE · BULLET TIME / PAUSE BUTTONS ]';",'v1 touch mode')
s=once(s,'        // ----- GAME STATE (optimized, no lag) -----',JS+"\n        installMobileControls('hold-space');\n\n        // ----- GAME STATE (optimized, no lag) -----",'v1 controls js')
s=once(s,"                    'WASD MOVE · MOUSE FIRE · SPACE BULLET TIME',\n                    'ONE VHS REWIND PER RUN. SPEND IT WISELY.',\n                    'CLICK / TAP TO START'","                    ...(touchMode ? ['LEFT STICK MOVE · DRAG ARENA TO FIRE','HOLD BULLET TIME BUTTON TO SLOW THE WORLD','TAP TO START'] : ['WASD MOVE · MOUSE FIRE · SPACE BULLET TIME','ONE VHS REWIND PER RUN. SPEND IT WISELY.','CLICK / TAP TO START'])",'v1 start copy')
s=s.replace("const touch = e.touches[0];\n            handleMove(touch.clientX, touch.clientY);","const touch = e.targetTouches[0] || e.changedTouches[0];\n            if (!touch) return;\n            handleMove(touch.clientX, touch.clientY);")
(G/name).write_text(s)

# v2
name='RogueRita_v2_Vaporwave.html'; s=source(name)
s=once(s,'.mute-btn:active { transform: translate(2px, 2px); box-shadow: none; }\n.top-hud { right: 76px; }\n</style>','.mute-btn:active { transform: translate(2px, 2px); box-shadow: none; }\n.top-hud { right: 76px; }\n@media (max-width:900px),(pointer:coarse){.top-hud{top:calc(10px + var(--sat));left:calc(10px + var(--sal));right:calc(76px + var(--sar))}}\n'+CSS+'</style>','v2 css')
s=once(s,'    <div class="controls-hint" id="controlHint">\n      [ WASD + MOUSE | SPACE: BULLET TIME | P: PAUSE | M: MUTE ] · TAP/DRAG TO FIRE\n    </div>\n  </div>','    <div class="controls-hint" id="controlHint">\n      [ WASD + MOUSE | SPACE: BULLET TIME | P: PAUSE | M: MUTE ] · TAP/DRAG TO FIRE\n    </div>\n'+HTML_BULLET+'  </div>','v2 html')
s=once(s,'      const hintEl = document.getElementById("controlHint");\n      const wrapper = canvas.parentElement;','      const hintEl = document.getElementById("controlHint");\n      const touchMode = window.matchMedia("(pointer: coarse)").matches || ("ontouchstart" in window);\n      const wrapper = canvas.parentElement;','v2 touch mode')
s=once(s,'      function clamp(value, min, max) {',JS+"\n      installMobileControls('hold-space');\n\n      function clamp(value, min, max) {",'v2 controls js')
s=once(s,'            "WASD MOVE · MOUSE FIRE · SPACE BULLET TIME",\n            "KEEP THE COMBO ALIVE — THE BAND ONLY PLAYS FOR WINNERS",\n            "CLICK / TAP TO START"','            ...(touchMode ? ["LEFT STICK MOVE · DRAG ARENA TO FIRE","HOLD BULLET TIME · KEEP THE COMBO ALIVE","TAP TO START"] : ["WASD MOVE · MOUSE FIRE · SPACE BULLET TIME","KEEP THE COMBO ALIVE — THE BAND ONLY PLAYS FOR WINNERS","CLICK / TAP TO START"])','v2 start copy')
s=once(s,'      hintEl.textContent = window.matchMedia("(pointer: coarse)").matches\n        ? "[ TAP/DRAG TO FIRE · 🔊 BUTTON: VOLUME ]"\n        : "[ WASD + MOUSE | SPACE: BULLET TIME | P: PAUSE | M: MUTE ] · TAP/DRAG TO FIRE";','      hintEl.textContent = touchMode\n        ? "[ LEFT STICK: MOVE · DRAG ARENA: FIRE · BULLET TIME / PAUSE BUTTONS ]"\n        : "[ WASD + MOUSE | SPACE: BULLET TIME | P: PAUSE | M: MUTE ] · TAP/DRAG TO FIRE";','v2 hint')
s=s.replace('const touch = e.touches[0];\n        if (!touch) return;','const touch = e.targetTouches[0] || e.changedTouches[0];\n        if (!touch) return;')
(G/name).write_text(s)

# Boss
name='RogueRita_CyberArena_BossPackV1.html'; s=source(name)
s=once(s,'<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">','<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no, viewport-fit=cover">','boss viewport')
s=once(s,'    <style>\n','    <style>\n        :root { --sat: env(safe-area-inset-top,0px); --sab: env(safe-area-inset-bottom,0px); --sal: env(safe-area-inset-left,0px); --sar: env(safe-area-inset-right,0px); }\n','boss root')
s=once(s,'    @media (max-width: 980px), (pointer: coarse) {\n        .stats-panel { right: 72px; }\n    }\n</style>','    @media (max-width: 980px), (pointer: coarse) {\n        .stats-panel { top: calc(12px + var(--sat)); left: calc(12px + var(--sal)); right: calc(72px + var(--sar)); }\n        .game-tagline { top: calc(118px + var(--sat)); left: calc(12px + var(--sal)); right: calc(12px + var(--sar)); }\n    }\n'+BOSS_CSS+'</style>','boss css')
s=once(s,'    <div class="controls-hint" id="controlHint">\n        [ WASD + MOUSE + SPACE: DASH | P: PAUSE | M: MUTE ] · TAP/DRAG TO FIRE · DOUBLE TAP TO DASH · DASH THROUGH INK TO PARRY\n    </div>\n</div>','    <div class="controls-hint" id="controlHint">\n        [ WASD + MOUSE + SPACE: DASH | P: PAUSE | M: MUTE ] · TAP/DRAG TO FIRE · DOUBLE TAP TO DASH · DASH THROUGH INK TO PARRY\n    </div>\n'+HTML_BOSS+'</div>','boss html')
s=once(s,"    const objectiveEl = document.getElementById('objectiveDisplay');\n    // mobile-first: touch players get touch instructions, not a keyboard manual\n    if (window.matchMedia('(pointer: coarse)').matches) {\n        document.getElementById('controlHint').textContent = '[ TAP/DRAG TO FIRE · DOUBLE-TAP TO DASH/PARRY · 🔊 BUTTON: VOLUME ]';\n    }","    const objectiveEl = document.getElementById('objectiveDisplay');\n    const touchMode = window.matchMedia('(pointer: coarse)').matches || ('ontouchstart' in window);\n    if (touchMode) document.getElementById('controlHint').textContent = '[ LEFT STICK: MOVE · DRAG ARENA: FIRE · DASH/PARRY / PAUSE BUTTONS ]';",'boss touch mode')
s=once(s,'    let viewW = 0, viewH = 0, dpr = 1;',JS+"\n    installMobileControls('tap-space');\n\n    let viewW = 0, viewH = 0, dpr = 1;",'boss controls js')
s=once(s,"            ctx.fillText('DASH THROUGH INK SHOTS TO PARRY THEM BACK', viewW / 2, viewH / 2 + 38 * oScale);","            ctx.fillText(touchMode ? 'LEFT STICK MOVE · DRAG ARENA TO FIRE · DASH/PARRY BUTTON' : 'DASH THROUGH INK SHOTS TO PARRY THEM BACK', viewW / 2, viewH / 2 + 38 * oScale);",'boss start copy')
s=s.replace('const touch = e.touches[0];\n        const now = performance.now();','const touch = e.targetTouches[0] || e.changedTouches[0];\n        if (!touch) return;\n        const now = performance.now();')
s=s.replace('const touch = e.touches[0];\n        handleMove(touch.clientX, touch.clientY);','const touch = e.targetTouches[0] || e.changedTouches[0];\n        if (!touch) return;\n        handleMove(touch.clientX, touch.clientY);')
(G/name).write_text(s)

# Storefront: factual/mobile-only corrections, no redesign.
p=Path('index.html'); s=p.read_text()
s=s.replace('<meta name="viewport" content="width=device-width, initial-scale=1.0">','<meta name="viewport" content="width=device-width, initial-scale=1.0, viewport-fit=cover">',1)
s=s.replace('No music. Your heartbeat is the soundtrack.','A lo-fi tape-deck synthwave loop rides under the neon. Your heartbeat can still keep time.')
s=s.replace('<div class="ico">��️</div>','<div class="ico">✍️</div>')
s=s.replace("<summary>Why doesn't V1 or the Boss Pack have music?</summary>\n      <p>V1 is the quiet one — the silence is load-bearing. The Boss Pack is ink; ink doesn't need a soundtrack. If you want the band, v2 has an entire generative engine that only plays for winners. Go be a winner.</p>","<summary>Why does each game sound different?</summary>\n      <p>V1 runs a lo-fi tape-deck synthwave loop, v2 uses a generative combo-driven band, and the Boss Pack uses a phase-driven industrial war drone. Each soundtrack follows its own game mechanic.</p>")
s=s.replace('    .nav-inner { padding: 12px 16px; }','    nav { padding-top: env(safe-area-inset-top, 0px); }\n    .nav-inner { padding: 12px max(16px, env(safe-area-inset-right, 0px)) 12px max(16px, env(safe-area-inset-left, 0px)); }')
p.write_text(s)

# Remove the temporary wrapper architecture after writing direct canonical games.
for pattern in ('*_core.html','mobile-play.html','mobile.html'):
    for p in G.glob(pattern): p.unlink()

print('Rogue Rita direct mobile patch applied')
