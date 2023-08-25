<script setup lang="ts">
import { BENFORDS_LAW_ARR } from "../constants"

const props = defineProps<{ columnData: number[] | null }>()
const { columnData } = toRefs(props)

const diffs = computed(() => {
	if (columnData.value) {
		const results: number[] = []
		BENFORDS_LAW_ARR.map((item: number, index: number) => {
			results.push(parseFloat((columnData.value![index] - item).toFixed(2)))
		})
		return results
	} else {
		return null
	}
})
</script>

<template>
	<section v-if="columnData" class="container">
		<h2 class="text-4xl mb-8">
			Difference Between Column and Benford's Law Expected Results
		</h2>
		<div class="grid grid-cols-3">
			<div
				class="relative px-4 py-10 md:py-20 border bg-gray-400 flex flex-col items-center justify-center"
				:class="{
					'bg-green-400/80 border-green-600': Math.abs(diff) < 2,
					'bg-gray-400/80 border-gray-600':
						Math.abs(diff) >= 2 && Math.abs(diff) < 5,
					'bg-yellow-400/80 border-yellow-600':
						Math.abs(diff) >= 5 && Math.abs(diff) < 10,
					'bg-red-400/80 border-red-600': Math.abs(diff) >= 10
				}"
				v-for="(diff, index) in diffs"
				:key="`${index + 1}-${diff}`">
				<span
					class="absolute left-4 bottom-0 text-2xl md:text-7xl opacity-50 text-white"
					>{{ index + 1 }}</span
				>
				<span class="font-bold text-xl md:text-5xl"
					>{{ diff > 0 ? "+" : "" }}{{ diff }}%</span
				>
			</div>
		</div>
	</section>
</template>
