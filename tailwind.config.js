/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js",
    "./node_modules/flowbite/**/*.js"
  ],
  darkMode: 'class',
  theme: {
    extend: {
      // colors: {
      //   primary: '#000000',
      //   secondary: '#52057B',
      //   tertiary: '#892CDC',
      //   quaternary: '#BC6FF1',
      // }
    },
  },
  plugins: [
    require("flowbite/plugin")
  ]
}