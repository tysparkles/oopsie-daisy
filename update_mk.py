import re

with open("src/pages/index.astro") as f:
    content = f.read()

# 1. Bump MaryKate sizes (existing sections)
# Hero tagline: text-xl md:text-2xl → text-2xl md:text-3xl
content = content.replace(
    'class="font-marykate italic text-xl md:text-2xl text-white/80',
    'class="font-marykate italic text-2xl md:text-3xl text-white/80'
)
# This Month quote: text-lg → text-xl
content = content.replace(
    'class="font-marykate italic text-lg text-contrast-muted mb-8 leading-relaxed">\n              "There\'s',
    'class="font-marykate italic text-xl text-contrast-muted mb-8 leading-relaxed">\n              "There\'s'
)
# Archive tagline: text-lg → text-xl
content = content.replace(
    'class="font-marykate italic text-text-muted text-lg">More issues',
    'class="font-marykate italic text-text-muted text-xl">More issues'
)
# Behind studio intro: text-lg → text-xl
content = content.replace(
    'class="font-marykate italic text-contrast-muted text-lg">\n            Artist',
    'class="font-marykate italic text-contrast-muted text-xl">\n            Artist'
)
# Cancel anytime line
content = content.replace(
    'class="font-marykate italic text-contrast-muted text-lg">Cancel',
    'class="font-marykate italic text-contrast-muted text-xl">Cancel'
)

# 2. All 4 testimonials: font-retro → font-marykate
content = content.replace(
    '<p class="font-retro italic text-contrast leading-relaxed mb-5">\n              "Opening',
    '<p class="font-marykate italic text-contrast leading-relaxed mb-5">\n              "Opening'
)
content = content.replace(
    '<p class="font-retro italic text-contrast leading-relaxed mb-5">\n              "I have a gallery',
    '<p class="font-marykate italic text-contrast leading-relaxed mb-5">\n              "I have a gallery'
)
content = content.replace(
    '<p class="font-retro italic text-contrast leading-relaxed mb-5">\n              "The matcha one',
    '<p class="font-marykate italic text-contrast leading-relaxed mb-5">\n              "The matcha one'
)
# Testimonial 4
content = content.replace(
    '<p class="font-retro italic text-contrast leading-relaxed mb-5">\n              "This subscription',
    '<p class="font-marykate italic text-contrast leading-relaxed mb-5">\n              "This subscription'
)

open("src/pages/index.astro", "w").write(content)

# Verify
new = open("src/pages/index.astro").read()
mk_count = new.count('font-marykate')
print(f"font-marykate occurrences: {mk_count}")

# Check testimonials
for q in ['Opening my Oopsie', 'I have a gallery', 'The matcha one', 'This subscription']:
    idx = new.find(q)
    if idx > 0:
        snippet = new[idx-60:idx+30]
        font_class = [c for c in snippet.split() if c.startswith('class=')][-1][:30]
        print(f"  {q[:20]}: {font_class}")