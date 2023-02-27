/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ['./templates/**/*.html','./shop/forms.py'],
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
