# Rotating images — update these paths when you add images to public/media/rotating/
IMAGES = [
    "/media/prints/girl .png",
    "/media/prints/tulip selfie.png",
    "/media/prints/toastt.png",
    "/media/prints/matcha.png",
    "/media/prints/cherry blossom.png",
    # ↑ Add more images here as you drop them into public/media/rotating/
    # e.g. "/media/rotating/my-image.png",
]

import os, re

INDEX   = "/Users/leslie/oopsie-daisy/src/pages/index.astro"
CSS     = "/Users/leslie/oopsie-daisy/src/styles/global.css"
LAYOUT  = "/Users/leslie/oopsie-daisy/src/layouts/Layout.astro"

# ── Build strip HTML ───────────────────────────────────────────────────────────
def build_strip(images):
    items = []
    for i, src in enumerate(images):
        alt = os.path.basename(src, ".*").replace("-", " ").replace("_", " ").title()
        items.append(
            f'<div class="rotate-img-wrap">'
            f'<img src="{src}" alt="{alt}" class="rotate-img" loading="{"eager" if i < 2 else "lazy"}"/>'
            f'</div>'
        )
    # Duplicate for seamless loop
    return "\n".join(items) + "\n" + "\n".join(items)

strip_html  = build_strip(IMAGES)
strip_count = len(IMAGES)

print(f"Rotating images: {strip_count}")
for s in IMAGES: print(f"  {s}")

# ── Gallery HTML ──────────────────────────────────────────────────────────────
new_gallery = f"""        <!-- ── ROTATING IMAGE GALLERY (endless loop) ── -->
        <!-- To change images: update the IMAGES list in endless_rotate.py -->
        <div class="relative">

          <!-- Arrow nav -->
          <button id="gallery-left" class="absolute left-0 top-1/2 -translate-y-1/2 z-10 w-10 h-10 rounded-full bg-warm-cream/90 border-2 border-coral-pink/40 text-coral-pink shadow-lg hover:bg-coral-pink hover:text-white flex items-center justify-center gallery-nav-btn" style="--rot:-5deg;" aria-label="Previous">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M15 18l-6-6 6-6"/></svg>
          </button>
          <button id="gallery-right" class="absolute right-0 top-1/2 -translate-y-1/2 z-10 w-10 h-10 rounded-full bg-warm-cream/90 border-2 border-coral-pink/40 text-coral-pink shadow-lg hover:bg-coral-pink hover:text-white flex items-center justify-center gallery-nav-btn" style="--rot:5deg;" aria-label="Next">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round"><path d="M9 18l6-6-6-6"/></svg>
          </button>

          <!-- Rotating strip -->
          <div class="archive-gallery-wrap" id="archive-gallery-wrap">
            <div class="archive-gallery-strip" id="archive-gallery-strip">
{strip_html}
            </div>
          </div>

          <!-- Hint -->
          <div class="mt-4 flex items-center justify-center gap-2">
            <span class="text-coral-pink/40 text-xs animate-float-slow">✦</span>
            <p class="font-heading text-[10px] text-text-muted/50 tracking-widest uppercase">Rotating collection &middot; {strip_count} images</p>
            <span class="text-coral-pink/40 text-xs animate-float-slow" style="animation-delay:1s;">✦</span>
          </div>
        </div>

        <div class="text-center mt-8">
          <p class="font-marykate italic text-text-muted text-lg">More issues added every month &mdash; join to collect them all.</p>
        </div>"""

# ── Inject into index.astro ───────────────────────────────────────────────────
with open(INDEX) as f:
    html = f.read()

old_start = '        <!-- ── ENDLESS ARCHIVE GALLERY ── -->'
old_end   = '        <div class="text-center mt-8">\n          <p class="font-marykate italic text-text-muted text-lg">More issues added every month &mdash; join to collect them all.</p>\n        </div>'

idx_start = html.find(old_start)
idx_end   = html.find(old_end)
if idx_start != -1 and idx_end != -1:
    idx_end += len(old_end)
    html = html[:idx_start] + new_gallery + html[idx_end:]
    print(f"Gallery replaced ({idx_end - idx_start} → {len(new_gallery)} chars)")
else:
    print(f"ERROR: start={idx_start}, end={idx_end}")

with open(INDEX, "w") as f:
    f.write(html)
print("index.astro updated")

# ── Update global.css ─────────────────────────────────────────────────────────
with open(CSS) as f:
    css = f.read()

rotate_css = """
/* ══════════════════════════════════════════════════════════════
   ROTATING IMAGE GALLERY
══════════════════════════════════════════════════════════════ */

.archive-gallery-wrap {
  overflow: hidden;
  position: relative;
}

.archive-gallery-strip {
  display: flex;
  align-items: center;
  gap: 1.5rem;
  width: max-content;
  will-change: transform;
}

.rotate-img-wrap {
  width: 16rem;
  height: 20rem;
  flex-shrink: 0;
  border-radius: 1.5rem;
  overflow: hidden;
  border: 2px solid rgba(212, 92, 116, 0.2);
  box-shadow: 0 8px 32px rgba(90, 50, 30, 0.1);
  background: #f5ede4;
}

.rotate-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  display: block;
  transition: transform 0.4s ease;
}

.rotate-img-wrap:hover .rotate-img {
  transform: scale(1.05);
}

@media (max-width: 640px) {
  .rotate-img-wrap { width: 13rem; height: 16rem; }
}
"""

css = re.sub(
    r"/\* ══════════════════════════════════════════════════════════════\n   ENDLESS GALLERY SCROLL.*?/\* ══════════════════════════════════════════════════════════════\n \*/",
    "",
    css,
    flags=re.DOTALL
)
css = css.rstrip() + "\n" + rotate_css

with open(CSS, "w") as f:
    f.write(css)
print("global.css updated")

# ── Update Layout.astro JS ────────────────────────────────────────────────────
with open(LAYOUT) as f:
    layout = f.read()

new_js = """
<script>
  (function() {
    var wrap  = document.getElementById('archive-gallery-wrap');
    var strip = document.getElementById('archive-gallery-strip');
    var leftBtn  = document.getElementById('gallery-left');
    var rightBtn = document.getElementById('gallery-right');
    if (!wrap || !strip) return;

    var pos       = 0;
    var speed     = 1.0;
    var isHovered = false;
    var rafId     = null;

    function cardW() { return (window.innerWidth < 640 ? 13 : 16) * 16 + 1.5 * 16; }
    if (leftBtn)  leftBtn.addEventListener('click',  function(){ wrap.scrollLeft -= cardW(); });
    if (rightBtn) rightBtn.addEventListener('click', function(){ wrap.scrollLeft += cardW(); });

    wrap.addEventListener('mouseenter',  function(){ isHovered = true;  cancelAnimationFrame(rafId); });
    wrap.addEventListener('mouseleave',  function(){ isHovered = false; rafId = requestAnimationFrame(tick); });
    wrap.addEventListener('touchstart', function(){ isHovered = true;  cancelAnimationFrame(rafId);  }, {passive:true});
    wrap.addEventListener('touchend',   function(){ isHovered = false; rafId = requestAnimationFrame(tick); }, {passive:true});

    wrap.addEventListener('scroll', function() {
      var maxScroll = strip.scrollWidth - wrap.clientWidth;
      if (wrap.scrollLeft >= maxScroll - 2) { wrap.scrollLeft = 1; pos = 1; }
      if (wrap.scrollLeft <= 0) { wrap.scrollLeft = maxScroll - wrap.clientWidth - 1; pos = wrap.scrollLeft; }
    }, {passive:true});

    function tick() {
      if (!isHovered) {
        pos += speed;
        var max = strip.scrollWidth - wrap.clientWidth;
        if (pos >= max) pos = 1;
        wrap.scrollLeft = pos;
      }
      rafId = requestAnimationFrame(tick);
    }
    rafId = requestAnimationFrame(tick);
  })();

  var revealEls = document.querySelectorAll('.scroll-reveal');
  if (revealEls.length > 0) {
    var obs = new IntersectionObserver(function(entries) {
      entries.forEach(function(e) { if (e.isIntersecting) { e.target.classList.add('is-visible'); obs.unobserve(e.target); } });
    }, {threshold:0.1, rootMargin:'0px 0px -40px 0px'});
    revealEls.forEach(function(el){ obs.observe(el); });
  }

  var petals = document.querySelectorAll('.animate-petal-fall');
  window.addEventListener('scroll', function() {
    var sc = window.scrollY;
    petals.forEach(function(p, i) { p.style.transform = 'translateY(' + (sc * (0.05 + i * 0.02)) + 'px)'; });
  }, {passive:true});
</script>
"""

layout = re.sub(r"<script>[\s\S]*?</script>", new_js.strip(), layout, count=1)
with open(LAYOUT, "w") as f:
    f.write(layout)
print("Layout.astro updated")