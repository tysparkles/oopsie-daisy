import os, re

INDEX = "/Users/leslie/oopsie-daisy/src/pages/index.astro"
CSS   = "/Users/leslie/oopsie-daisy/src/styles/global.css"

with open(INDEX) as f:
    html = f.read()

# ════════════════════════════════════════════════════════════════
# 1. REPLACE MARY KATE (keep only short decorative uses)
# ════════════════════════════════════════════════════════════════

# These are long/prose uses → switch to font-body
long_prose_replacements = [
    # Hero tagline (hard to read at size)
    ('class="font-marykate font-marykate-animated italic text-xl md:text-2xl text-white/85 max-w-lg mx-auto mb-12"',
     'class="font-body text-lg md:text-xl text-white/85 max-w-lg mx-auto mb-12"'),

    # Section descriptions (readability)
    ('class="font-marykate italic text-lg md:text-xl text-contrast-muted mb-8"',
     'class="font-body italic text-base md:text-lg text-contrast-muted mb-8"'),

    # "Cancel anytime" footer text
    ('class="font-marykate italic text-white/75 text-lg"',
     'class="font-body italic text-white/75 text-sm"'),

    # Reviewer quote text
    ('class="font-marykate italic text-contrast leading-relaxed mb-5"',
     'class="font-body italic text-contrast leading-relaxed mb-5"'),
]

for old, new in long_prose_replacements:
    html = html.replace(old, new)
    print(f"Replaced: {old[:60]}...")

# Short decorative uses — KEEP font-marykate:
# - section label (tiny decorative "✦ This Month's Issue ✦")
# - archive gallery hint text
# - pricing italic notes

print(f"Mary Kate replacements done")

# ════════════════════════════════════════════════════════════════
# 2. REDESIGN "WHAT'S IN THE BOX" CARDS
# ════════════════════════════════════════════════════════════════

old_wib_section = '''        <div class="grid md:grid-cols-3 gap-8">

          <!-- Card 1 — Art Print -->
          <div class="paper-card p-8 hover-lift">
            <div class="w-16 h-16 rounded-full bg-coral-pink/20 flex items-center justify-center mb-5">
              <svg class="w-8 h-8" viewBox="0 0 40 40" fill="none">
                <rect x="6" y="8" width="28" height="24" rx="3" stroke="#D45C74" stroke-width="2" fill="none"/>
                <path d="M6 28 L14 20 L20 26 L26 19 L34 28" stroke="#D45C74" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
                <circle cx="13" cy="14" r="3" stroke="#DE7B5B" stroke-width="1.5" fill="none"/>
              </svg>
            </div>
            <h3 class="font-display text-2xl text-contrast mb-3">Art Print</h3>
            <p class="font-body text-contrast-muted leading-relaxed text-sm">Exclusive monthly collectible artwork designed around the current theme and emotional mood of the month.</p>
          </div>

          <!-- Card 2 — Handwritten Letter -->
          <div class="paper-card p-8 hover-lift">
            <div class="w-16 h-16 rounded-full bg-burnt-cinnamon/20 flex items-center justify-center mb-5">
              <svg class="w-8 h-8" viewBox="0 0 40 40" fill="none">
                <path d="M8 12 L20 24 L32 12" stroke="#A55230" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                <rect x="8" y="10" width="24" height="18" rx="2" stroke="#A55230" stroke-width="2" fill="none"/>
                <path d="M8 10 L20 23 L32 10" stroke="#A55230" stroke-width="1.5" fill="none" stroke-linecap="round"/>
              </svg>
            </div>
            <h3 class="font-display text-2xl text-contrast mb-3">Handwritten Letter</h3>
            <p class="font-body text-contrast-muted leading-relaxed text-sm">Inspiration behind the piece, creative thoughts, personal reflections, and current life updates from the studio.</p>
          </div>

          <!-- Card 3 — Surprise Gift -->
          <div class="paper-card p-8 hover-lift">
            <div class="w-16 h-16 rounded-full bg-olive-green/20 flex items-center justify-center mb-5">
              <svg class="w-8 h-8" viewBox="0 0 40 40" fill="none">
                <path d="M20 8 C20 8 10 15 10 24 C10 29 14 33 20 33" stroke="#8A8454" stroke-width="2" fill="none" stroke-linecap="round"/>
                <circle cx="17" cy="22" r="2" fill="#8A8454"/>
                <circle cx="23" cy="24" r="1.5" fill="#8A8454"/>
              </svg>
            </div>
            <h3 class="font-display text-2xl text-contrast mb-3">Surprise Gift</h3>
            <p class="font-body text-contrast-muted leading-relaxed text-sm">Every month includes an extra surprise such as a sticker set, bookmark, colouring sheet, mini activity, or build-your-own creative insert.</p>
          </div>

        </div>'''

new_wib_section = '''        <div class="grid md:grid-cols-3 gap-6">
          <!-- Sparkle daisy left -->
          <svg class="hidden md:block absolute left-[-2rem] top-[6rem] w-10 h-10 opacity-40 animate-flower-sway" style="animation-duration:9s;" viewBox="0 0 50 50" fill="none"><circle cx="25" cy="25" r="5" fill="#DE7B5B"/><ellipse cx="25" cy="9" rx="4" ry="7" fill="#DE7B5B" transform="rotate(0 25 25)"/><ellipse cx="25" cy="9" rx="4" ry="7" fill="#DE7B5B" transform="rotate(60 25 25)"/><ellipse cx="25" cy="9" rx="4" ry="7" fill="#DE7B5B" transform="rotate(120 25 25)"/><ellipse cx="25" cy="9" rx="4" ry="7" fill="#DE7B5B" transform="rotate(180 25 25)"/><ellipse cx="25" cy="9" rx="4" ry="7" fill="#DE7B5B" transform="rotate(240 25 25)"/><ellipse cx="25" cy="9" rx="4" ry="7" fill="#DE7B5B" transform="rotate(300 25 25)"/><circle cx="25" cy="25" r="5" fill="#D4BB9D"/></svg>

          <!-- Card 1 — Art Print — sticker style -->
          <div class="sticker-card sticker-card-art relative" style="transform:rotate(-2deg);">
            <!-- washi tape -->
            <div class="absolute top-[-6px] left-1/2 -translate-x-1/2 w-14 h-5 z-20" style="background:repeating-linear-gradient(45deg,rgba(222,123,91,0.55),rgba(222,123,91,0.55) 3px,rgba(231,199,175,0.3) 3px,rgba(231,199,175,0.3) 6px);"></div>
            <!-- card body -->
            <div class="bg-warm-cream rounded-2xl p-6 pt-8 shadow-xl shadow-coral-pink/15 border-2 border-coral-pink/20 relative">
              <!-- sparkle top right -->
              <span class="absolute top-3 right-3 text-coral-pink/40 animate-sparkle text-xs">✦</span>
              <span class="absolute top-5 right-6 text-dusty-pink/30 animate-sparkle text-[10px]" style="animation-delay:0.8s;">✦</span>
              <!-- illustration -->
              <div class="flex justify-center mb-4">
                <svg width="64" height="64" viewBox="0 0 80 80" fill="none" class="animate-flower-sway" style="animation-duration:10s;">
                  <!-- canvas/easel frame -->
                  <rect x="14" y="12" width="52" height="42" rx="4" fill="#FDF6EC" stroke="#D45C74" stroke-width="2"/>
                  <rect x="18" y="16" width="44" height="34" rx="2" fill="#FDF6EC"/>
                  <!-- mountain/landscape sketch inside -->
                  <path d="M18 46 L30 30 L40 38 L50 26 L62 46" stroke="#DE7B5B" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
                  <circle cx="54" cy="24" r="4" fill="#FA9DAA" opacity="0.6"/>
                  <!-- daisy on canvas -->
                  <circle cx="38" cy="27" r="2" fill="#D45C74"/>
                  <ellipse cx="38" cy="22" rx="1.5" ry="3" fill="white" opacity="0.8" transform="rotate(0 38 27)"/>
                  <ellipse cx="38" cy="22" rx="1.5" ry="3" fill="white" opacity="0.8" transform="rotate(72 38 27)"/>
                  <ellipse cx="38" cy="22" rx="1.5" ry="3" fill="white" opacity="0.8" transform="rotate(144 38 27)"/>
                  <ellipse cx="38" cy="22" rx="1.5" ry="3" fill="white" opacity="0.8" transform="rotate(216 38 27)"/>
                  <ellipse cx="38" cy="22" rx="1.5" ry="3" fill="white" opacity="0.8" transform="rotate(288 38 27)"/>
                  <!-- easel legs -->
                  <path d="M40 54 L40 68" stroke="#D4BB9D" stroke-width="2" stroke-linecap="round"/>
                  <path d="M28 68 L40 54 L52 68" stroke="#D4BB9D" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" fill="none"/>
                  <!-- paintbrush -->
                  <path d="M62 18 L68 12" stroke="#A55230" stroke-width="1.5" stroke-linecap="round"/>
                  <ellipse cx="69" cy="11" rx="2" ry="3" fill="#A55230" transform="rotate(45 69 11)"/>
                </svg>
              </div>
              <!-- text -->
              <h3 class="font-display text-xl text-contrast text-center mb-2">Art Print</h3>
              <p class="font-body text-xs text-contrast-muted text-center leading-relaxed">Exclusive monthly collectible artwork — a little universe in print.</p>
              <!-- sticker embellishments bottom -->
              <div class="flex justify-between items-center mt-3">
                <svg width="16" height="16" viewBox="0 0 50 50" fill="none"><circle cx="25" cy="25" r="4" fill="#DE7B5B"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(0 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(60 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(120 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(180 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(240 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(300 25 25)"/><circle cx="25" cy="25" r="4" fill="#D4BB9D"/></svg>
                <span class="font-marykate italic text-[10px] text-coral-pink/50">8×10"</span>
                <svg width="16" height="16" viewBox="0 0 50 50" fill="none"><circle cx="25" cy="25" r="4" fill="#DE7B5B"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(0 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(60 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(120 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(180 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(240 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(300 25 25)"/><circle cx="25" cy="25" r="4" fill="#D4BB9D"/></svg>
              </div>
            </div>
          </div>

          <!-- Card 2 — Handwritten Letter — romantic journal style -->
          <div class="sticker-card sticker-card-letter relative" style="transform:rotate(1deg);">
            <div class="absolute top-[-6px] left-1/2 -translate-x-1/2 w-14 h-5 z-20" style="background:repeating-linear-gradient(45deg,rgba(212,92,116,0.5),rgba(212,92,116,0.5) 3px,rgba(231,199,175,0.3) 3px,rgba(231,199,175,0.3) 6px);"></div>
            <div class="bg-warm-cream rounded-2xl p-6 pt-8 shadow-xl shadow-dusty-pink/15 border-2 border-coral-pink/20 relative">
              <span class="absolute top-3 right-3 text-dusty-pink/40 animate-sparkle text-xs">✦</span>
              <span class="absolute top-6 right-5 text-coral-pink/30 animate-sparkle text-[10px]" style="animation-delay:1.2s;">✦</span>
              <!-- letter/envelope illustration -->
              <div class="flex justify-center mb-4">
                <svg width="64" height="64" viewBox="0 0 80 80" fill="none" class="animate-flower-sway" style="animation-duration:12s;">
                  <!-- envelope -->
                  <rect x="10" y="22" width="60" height="40" rx="3" fill="#FDF6EC" stroke="#D45C74" stroke-width="2"/>
                  <path d="M10 22 L40 46 L70 22" stroke="#D45C74" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>
                  <path d="M10 22 L40 46 L70 22" stroke="#DE7B5B" stroke-width="1" stroke-linecap="round" stroke-linejoin="round" fill="none" stroke-dasharray="3,3"/>
                  <!-- heart seal -->
                  <path d="M40 32 C38 28 33 28 33 32 C33 36 40 40 40 40 C40 40 47 36 47 32 C47 28 42 28 40 32Z" fill="#D45C74" opacity="0.8"/>
                  <!-- handwritten squiggles on envelope -->
                  <path d="M16 52 Q22 50 28 52 Q34 54 40 52" stroke="#DE7B5B" stroke-width="1" stroke-linecap="round" fill="none" opacity="0.6"/>
                  <path d="M44 52 Q50 50 56 52 Q60 53 64 52" stroke="#DE7B5B" stroke-width="1" stroke-linecap="round" fill="none" opacity="0.6"/>
                  <!-- pencil -->
                  <path d="M66 14 L72 8" stroke="#A55230" stroke-width="2" stroke-linecap="round"/>
                  <polygon points="72,8 75,11 72,14" fill="#A55230"/>
                  <rect x="65" y="14" width="2" height="6" rx="1" fill="#FA9DAA" transform="rotate(-45 66 14)"/>
                </svg>
              </div>
              <h3 class="font-display text-xl text-contrast text-center mb-2">Handwritten Letter</h3>
              <p class="font-body text-xs text-contrast-muted text-center leading-relaxed">Personal notes, studio stories, inspiration & little fragments of life.</p>
              <div class="flex justify-between items-center mt-3">
                <svg width="16" height="16" viewBox="0 0 50 50" fill="none"><circle cx="25" cy="25" r="4" fill="#DE7B5B"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(0 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(60 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(120 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(180 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(240 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(300 25 25)"/><circle cx="25" cy="25" r="4" fill="#D4BB9D"/></svg>
                <span class="font-marykate italic text-[10px] text-coral-pink/50">sealed w/ care</span>
                <svg width="16" height="16" viewBox="0 0 50 50" fill="none"><circle cx="25" cy="25" r="4" fill="#DE7B5B"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(0 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(60 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(120 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(180 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(240 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(300 25 25)"/><circle cx="25" cy="25" r="4" fill="#D4BB9D"/></svg>
              </div>
            </div>
          </div>

          <!-- Card 3 — Surprise Gift — chaotic sticker energy -->
          <div class="sticker-card sticker-card-gift relative" style="transform:rotate(2deg);">
            <div class="absolute top-[-6px] left-1/2 -translate-x-1/2 w-14 h-5 z-20" style="background:repeating-linear-gradient(45deg,rgba(138,132,84,0.5),rgba(138,132,84,0.5) 3px,rgba(231,199,175,0.3) 3px,rgba(231,199,175,0.3) 6px);"></div>
            <div class="bg-warm-cream rounded-2xl p-6 pt-8 shadow-xl shadow-olive-green/15 border-2 border-olive-green/30 relative">
              <span class="absolute top-3 right-3 text-olive-green/40 animate-sparkle text-xs">✦</span>
              <span class="absolute top-5 right-6 text-dusty-pink/30 animate-sparkle text-[10px]" style="animation-delay:0.5s;">✦</span>
              <span class="absolute top-6 right-10 text-coral-pink/30 animate-sparkle text-[8px]" style="animation-delay:1.8s;">✦</span>
              <!-- gift/sticker packs illustration -->
              <div class="flex justify-center gap-1 mb-4 flex-wrap">
                <!-- sticker pack 1 -->
                <svg width="32" height="36" viewBox="0 0 40 45" fill="none" class="animate-flower-sway" style="animation-duration:7s;">
                  <rect x="4" y="8" width="32" height="28" rx="4" fill="#FA9DAA" opacity="0.3" stroke="#D45C74" stroke-width="1.5"/>
                  <circle cx="12" cy="18" r="4" fill="#FA9DAA"/>
                  <circle cx="20" cy="14" r="3" fill="#DE7B5B"/>
                  <circle cx="28" cy="18" r="4" fill="#FA9DAA"/>
                  <circle cx="16" cy="26" r="3" fill="#DE7B5B"/>
                  <circle cx="24" cy="24" r="4" fill="#FA9DAA"/>
                  <path d="M4 8 L20 0 L36 8" fill="#FA9DAA" opacity="0.4" stroke="#D45C74" stroke-width="1.5" stroke-linejoin="round"/>
                </svg>
                <!-- sticker pack 2 -->
                <svg width="28" height="36" viewBox="0 0 40 45" fill="none" class="animate-flower-sway" style="animation-duration:11s;animation-delay:0.5s;">
                  <rect x="4" y="8" width="32" height="28" rx="4" fill="#DE7B5B" opacity="0.25" stroke="#A55230" stroke-width="1.5"/>
                  <!-- star shapes -->
                  <path d="M20 14 L22 18 L26 18 L23 21 L24 25 L20 22 L16 25 L17 21 L14 18 L18 18 Z" fill="#DE7B5B" opacity="0.8"/>
                  <circle cx="13" cy="26" r="2.5" fill="#D45C74" opacity="0.6"/>
                  <circle cx="27" cy="26" r="2.5" fill="#D45C74" opacity="0.6"/>
                  <path d="M4 8 L20 0 L36 8" fill="#DE7B5B" opacity="0.4" stroke="#A55230" stroke-width="1.5" stroke-linejoin="round"/>
                </svg>
                <!-- mini bookmark -->
                <svg width="16" height="40" viewBox="0 0 24 50" fill="none" class="animate-flower-sway" style="animation-duration:9s;animation-delay:1s;">
                  <path d="M4 4 L20 4 L20 46 L12 38 L4 46 Z" fill="#FDF6EC" stroke="#8A8454" stroke-width="1.5" stroke-linejoin="round"/>
                  <circle cx="12" cy="16" r="3" fill="#FA9DAA" opacity="0.7"/>
                  <circle cx="12" cy="26" r="2" fill="#DE7B5B" opacity="0.7"/>
                </svg>
              </div>
              <h3 class="font-display text-xl text-contrast text-center mb-2">Surprise Gift</h3>
              <p class="font-body text-xs text-contrast-muted text-center leading-relaxed">Sticker sets, bookmarks, colouring sheets & tiny dopamine inserts.</p>
              <div class="flex justify-between items-center mt-3">
                <svg width="16" height="16" viewBox="0 0 50 50" fill="none"><circle cx="25" cy="25" r="4" fill="#DE7B5B"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(0 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(60 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(120 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(180 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(240 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(300 25 25)"/><circle cx="25" cy="25" r="4" fill="#D4BB9D"/></svg>
                <span class="font-marykate italic text-[10px] text-olive-green/60">dopamine mail</span>
                <svg width="16" height="16" viewBox="0 0 50 50" fill="none"><circle cx="25" cy="25" r="4" fill="#DE7B5B"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(0 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(60 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(120 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(180 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(240 25 25)"/><ellipse cx="25" cy="12" rx="3" ry="5" fill="#FA9DAA" opacity="0.7" transform="rotate(300 25 25)"/><circle cx="25" cy="25" r="4" fill="#D4BB9D"/></svg>
              </div>
            </div>
          </div>

        </div>'''

html = html.replace(old_wib_section, new_wib_section)
print("What's In The Box cards replaced")

with open(INDEX, "w") as f:
    f.write(html)
print("index.astro written")