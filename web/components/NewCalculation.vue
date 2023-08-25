<script setup lang="ts">
import { Calculation } from "../types"

const props = defineProps<{
	isVisible: boolean
	currentColumn: string
	datasetId: string
}>()
const { isVisible, currentColumn, datasetId } = toRefs(props)
const isGenerating = ref(false)
const calculationError = ref("")

watch(currentColumn, () => {
	calculationError.value = ""
})

const emit = defineEmits<{
	(e: "onGeneratedCalculation", newCalculation: Calculation): void
}>()

const generateCalculation = async () => {
	calculationError.value = ""
	isGenerating.value = true
	const body = {
		datasetId: datasetId.value,
		columnName: currentColumn.value
	}

	const { data, pending, error } = await useFetch<Calculation>(
		"/api/calculations/generate",
		{
			method: "POST",
			body
		}
	)
	if (error.value) {
		calculationError.value =
			"There was an error running the calculation, please try again."
	}
	if (data.value?.column_name) {
		emit("onGeneratedCalculation", data.value)
	}
	isGenerating.value = false
}
</script>

<template>
	<Transition>
		<div
			v-show="isVisible"
			class="w-full min-h-[50vh] flex flex-col items-center justify-center mt-20 md:mt-20 container">
			<p class="text-xl md:text-2xl mb-8 max-w-prose text-center">
				There is no calculation for the column "{{ currentColumn }}" yet,<br
					class="hidden md:block" />
				but this astronaut would be happy to take care of that for you.
			</p>
			<img
				class="h-96 w-auto mb-8"
				src="/astronaut-see-thru.png"
				alt="astronaut doing math" />
			<button
				class="btn--primary text-2xl disabled:opacity-70"
				@click="generateCalculation"
				:disabled="isGenerating">
				{{ isGenerating ? "Calculating..." : "Calculate" }}
			</button>
			<div class="mt-4">
				<FormAlert
					:is-visible="!!calculationError"
					:message="calculationError" />
			</div>
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
