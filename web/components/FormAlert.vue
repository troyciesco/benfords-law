<script setup lang="ts">
const props = defineProps<{
	isVisible: boolean
	message?: string
}>()
const { isVisible, message } = toRefs(props)
</script>

<template>
	<Transition>
		<div
			v-show="isVisible"
			class="border-4 border-danger-700 px-8 py-4 bg-danger-800/60">
			<p class="text-danger-200 font-mono">
				{{ message || "An error occurred." }}
			</p>
		</div>
	</Transition>
</template>

<style scoped>
.v-enter-active,
.v-leave-active {
	transition: opacity 0.5s ease;
}

.v-enter-from,
.v-leave-to {
	opacity: 0;
}
</style>
