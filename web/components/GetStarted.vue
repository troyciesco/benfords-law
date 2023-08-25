<template>
	<section
		class="max-w-7xl mx-auto container mb-20 flex flex-col items-center justify-center">
		<h2 class="heading mb-8 text-center">
			Ready to <br class="md:hidden" />try it out?
		</h2>
		<div class="flex items-center gap-4">
			<NuxtLink class="border py-2 px-2 lg:px-4" to="/datasets"
				>Explore Datasets</NuxtLink
			>
			<NuxtLink class="btn--primary" to="/upload">Upload Dataset</NuxtLink>
		</div>
	</section>
</template>
