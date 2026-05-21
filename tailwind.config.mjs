/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        'white': 'rgb(220, 211, 209)',
        'tan': '#D4BB9D',
        'dusty-pink': '#D45C74',
        'coral-pink': '#DE7B5B',
        'burnt-cinnamon': '#A55230',
        'olive-green': '#8A8454',
        'espresso': '#4A4336',
        'warm-cream': '#E7C7AF',
        'text-dark': '#4A4336',
        'text-muted': '#6E5D50',
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
