<script setup lang="ts">
const props = defineProps<{ isVisible: boolean }>()
const { isVisible } = toRefs(props)
</script>

<template>
	<Transition>
		<div
			v-show="isVisible"
			class="w-full h-[50vh] flex flex-col items-center justify-center mt-20 md:mt-20 container">
			<p class="text-xl md:text-2xl mb-8 max-w-prose text-center">
				We don't have any datasets yet!<br class="hidden md:block" />
				Why don't you upload the first one?
			</p>
			<img
				class="h-96 w-auto mb-8"
				src="/404-astro.png"
				alt="astronaut by planet" />
			<NuxtLink class="btn--primary text-2xl" to="/upload">
				Upload a Dataset
			</NuxtLink>
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
