<script setup lang="ts">
const props = defineProps<{ title: string; description?: string }>()
const { title, description } = toRefs(props)
</script>

<template>
	<div class="panel">
		<h2
			class="text-3xl"
			:class="{ 'mb-2': !!description, 'mb-6': !description }">
			{{ title }}
		</h2>
		<p v-if="description" class="max-w-prose mb-4">
			{{ description }}
		</p>
		<slot />
	</div>
</template>

<style scoped>
.panel {
	@apply border border-light border-opacity-10 px-8 py-10 bg-[#222124] shadow-md;
}
</style>
