/** @type {import('tailwindcss').Config} */
export default {
  content: ['./src/**/*.{astro,html,js,jsx,md,mdx,svelte,ts,tsx,vue}'],
  theme: {
    extend: {
      colors: {
        cream: '#FFF8F0',
        'warm-white': '#FFFCF7',

        // Rainbow palette — soft & playful
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
        display: ['Quicksand', 'sans-serif'],
        body: ['Nunito', 'sans-serif'],
      },
    },
  },
  plugins: [],
};