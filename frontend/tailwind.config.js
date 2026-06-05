module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      backdropBlur: {
        xs: '2px',
        sm: '4px',
      },
      colors: {
        glass: {
          light: 'rgba(255, 255, 255, 0.7)',
          lighter: 'rgba(255, 255, 255, 0.8)',
        }
      }
    },
  },
  plugins: [],
}
