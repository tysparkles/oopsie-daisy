/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        // ─── Core paper palette ───
        'cake-batter':  '#F7E4C4',
        'warm-white':   '#FDF6EC',
        'warm-cream':   '#F6DFC6',
        'tan':          '#D4BB9D',

        // ─── Brand colours ───
        'dusty-pink':    '#D45C74',
        'raspberry':     '#D44A65',
        'lip-gloss':     '#FA9DAA',
        'coral-pink':    '#DE7B5B',
        'tangerine':     '#FF9243',
        'burnt-cinnamon':'#A55230',
        'olive-green':   '#8A8454',
        'vine-green':    '#A8BB3E',

        // ─── Accents ───
        'sky-lavender': '#C5B5D4',
        'sky-blue':      '#B5D4EB',
        'soft-lavender': '#D5C6E8',
        'pale-mint':     '#C5E4CB',
        'soft-peach':    '#F9D5C0',
        'pale-rose':    '#E8C4B8',

        // ─── Text ───
        'espresso':      '#4A4356',
        'text-dark':     '#3D2B2B',
        'text-muted':    '#7A6464',
        'text-raspberry':'#D44A65',
      },
      fontFamily: {
        display:   ['Fat Kat', 'cursive'],
        marykate:  ['MaryKate', 'cursive'],
        heading:   ['Nunito', 'sans-serif'],
        body:      ['Nunito', 'sans-serif'],
      },
      boxShadow: {
        'soft':   '0 4px 20px rgba(74, 67, 86, 0.10)',
        'float':  '0 8px 32px rgba(74, 67, 86, 0.15)',
        'sticker':'0 2px 8px rgba(0,0,0,0.15)',
        'paper':  '4px 4px 0 rgba(74, 67, 86, 0.08)',
      },
      animation: {
        'float-slow':  'float 8s ease-in-out infinite',
        'float-med':   'float 5s ease-in-out infinite',
        'float-fast':  'float 3s ease-in-out infinite',
        'drift':       'drift 12s ease-in-out infinite',
        'wiggle':      'wiggle 3s ease-in-out infinite',
        'pulse-soft': 'pulse-soft 4s ease-in-out infinite',
        'spin-slow':   'spin 20s linear infinite',
      },
    },
  },
  plugins: [],
};
