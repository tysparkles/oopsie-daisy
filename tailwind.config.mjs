/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        cream: '#FFF8F0',
        'warm-white': '#FFFCF7',

        'rainbow-red': '#FF6B8A',
        'rainbow-orange': '#FFA552',
        'rainbow-yellow': '#FFD93D',
        'rainbow-green': '#6BCB77',
        'rainbow-blue': '#4D96FF',
        'rainbow-purple': '#C77DFF',
        'rainbow-pink': '#FF8FAB',

        'text-dark': '#2D2A26',
        'text-muted': '#7A7166',
      },
      fontFamily: {
        display: ['Retro Mother', 'cursive'],
        retro: ['Retro Mother', 'cursive'],
        magic: ['Magic Retro', 'cursive'],
        body: ['Nunito', 'sans-serif'],
      },
    },
  },
  plugins: [],
};