/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        // ─── Core palette ───
        'cake-batter':  '#F7E4C4',  // warm cream background
        'warm-white':   '#FDF6EC',

        // ─── Brand colours ───
        'vine-green':   '#A8BB3E',
        'lip-gloss':    '#FA9DAA',
        'tangerine':    '#FF9243',
        'raspberry':    '#D44A65',

        // ─── Accents ───
        'sky-blue':      '#B5D4EB',
        'soft-lavender': '#D5C6E8',
        'pale-mint':     '#C5E4CB',
        'peach-cream':   '#F9D5C0',

        // ─── Text ───
        'text-dark':    '#3D2B2B',
        'text-muted':   '#7A6464',
        'text-raspberry':'#D44A65',
      },
      fontFamily: {
        display: ['Fat Kat', 'cursive'],
        retro:   ['Fat Kat', 'cursive'],
        heading: ['Poppins', 'sans-serif'],
        body:    ['Nunito', 'sans-serif'],
      },
      boxShadow: {
        'soft':   '0 4px 20px rgba(212, 74, 101, 0.12)',
        'float':  '0 8px 32px rgba(212, 74, 101, 0.18)',
        'sticker':'0 2px 8px rgba(0,0,0,0.15)',
        'paper':  '4px 4px 0 rgba(61,43,43,0.08)',
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