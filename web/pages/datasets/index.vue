<script setup lang="ts">
const { data: datasets } = await useDatasets()
</script>
<template>
	<main class="container mx-auto py-10">
		<div class="max-w-7xl mx-auto">
			<h1 class="text-5xl mb-4">Explore Datasets</h1>
			<p class="mb-8 text-lg max-w-prose">
				Here you'll find datasets that other people have uploaded. Wasn't that
				nice of them?
			</p>
		</div>
		<NoDatasets :is-visible="!datasets || datasets.length === 0" />
		<div
			v-if="datasets && datasets.length > 0"
			class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-20 max-w-7xl mx-auto">
			<DatasetCard
				v-for="dataset in datasets"
				:key="`${dataset.title}-${dataset.id}`"
				:dataset="dataset" />
		</div>
	</main>
</template>
