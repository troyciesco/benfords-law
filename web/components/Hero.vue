<template>
	<section
		class="py-40 container mx-auto flex flex-col justify-center items-center">
		<h1
			class="text-[4rem] md:text-[8rem] mb-6 text-center leading-[0.95] tracking-tighter">
			Benford's Law<br /><span class="text-gradient">Visualizer</span>
		</h1>
		<p class="max-w-prose text-center text-2xl mb-16">
			Upload data. Look at numbers. Nod thoughtfully.
		</p>
		<div class="flex items-center gap-4">
			<NuxtLink class="border py-2 px-2 md:px-4" to="/datasets"
				>Explore Datasets</NuxtLink
			>
			<NuxtLink class="btn--primary" to="/upload">Upload Dataset</NuxtLink>
		</div>
	</section>
</template>
