/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/**/*.html'],
  theme: {
    extend: {
      transitionProperty:{
        'width':'width',
        'height':'height'
      }
    },
  },
  plugins: [],
}
