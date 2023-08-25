<script setup lang="ts">
useHead({
	title: "Benford's Law Visualizer",
	meta: [
		{
			name: "description",
			content: "A visualization tool to compare data to Benford's law"
		}
	]
})
</script>
<template>
	<div>
		<NuxtLayout>
			<NuxtPage />
		</NuxtLayout>
	</div>
</template>

<!-- Only needed when page transitions are on -->
<!-- <style>
.page-enter-active,
.page-leave-active {
	transition: all 0.3s;
}
.page-enter-from,
.page-leave-to {
	opacity: 0;
	filter: blur(1rem);
}
</style> -->
