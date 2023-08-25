const colors = require("tailwindcss/colors")

/** @type {import('tailwindcss').Config} */
module.exports = {
	content: [],
	theme: {
		extend: {
			colors: {
				primary: "#3139FB",
				secondary: "#df1683",
				accent: "#8068f0",
				dark: "#18171A",
				light: "#fff8df",
				danger: colors.rose
			},
			fontFamily: {
				sans: ["Glacial Indifference"],
				mono: ["Share Tech Mono"],
				headline: ["Big Shoulders Inline Text"]
			}
		}
	},
	plugins: [
		require("@headlessui/tailwindcss"),
		require("@tailwindcss/typography"),
		require("@tailwindcss/aspect-ratio"),
		require("@tailwindcss/forms"),
		require("@tailwindcss/container-queries")
	]
}
