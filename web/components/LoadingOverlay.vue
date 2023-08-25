<script setup lang="ts">
const props = defineProps<{ isOpen: boolean; message: string }>()
const { isOpen, message } = toRefs(props)
</script>

<template>
	<Transition>
		<div
			v-if="isOpen"
			class="fixed top-0 left-0 w-full h-[100vh] bg-dark/70 flex flex-col items-center justify-center z-[999] backdrop-blur-sm">
			<p class="text-light font-bold text-3xl">
				{{ message }}
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
