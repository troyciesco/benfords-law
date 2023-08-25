// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
	runtimeConfig: {
		public: {
			apiBase: "http://localhost:5001",
			apiBrowserBase: "http://localhost:5001"
		}
	},
	modules: ["@nuxtjs/tailwindcss", "nuxt-icons"],
	css: ["~/assets/css/main.css"],
	// devtools: { enabled: true },
	app: {
		// pageTransition: { name: "page", mode: "out-in" },
		head: {
			title: "Benford's Law Visualizer",
			htmlAttrs: {
				lang: "en"
			}
		}
	}
})
