<script setup lang="ts">
import {
	Listbox,
	ListboxButton,
	ListboxOptions,
	ListboxOption,
	ListboxLabel
} from "@headlessui/vue"
import Heatmap from "../../components/Heatmap.vue"
import { Calculation, Digit } from "../../types"
const config = useRuntimeConfig()
const route = useRoute()
const { data } = await useDataset(route.params.datasetId as string)

if (!data.value) {
	throw createError({ statusCode: 404, statusMessage: "Dataset Not Found" })
}

const dataset = ref(data)
const currentColumn = ref(
	// @ts-ignore
	route.query.col ?? dataset.value?.calculations[0].column_name
)

// the vue page transitions don't play very nicely with the chart component,
// so switching the transition type kind of gets around that
definePageMeta({
	pageTransition: {
		name: "page",
		mode: "default"
	}
})

const calculation = computed(
	() =>
		dataset.value?.calculations?.find(
			(calc: any) => calc.column_name === currentColumn.value
		)
)

const columnData = computed(() => {
	if (calculation.value) {
		const rowsCount = calculation.value.rows_count
		const rawNumbers = calculation.value.benford_law_distribution
		const percentageResults: number[] = []

		Object.keys(rawNumbers).map((key: string) => {
			const digitKey = key as unknown as Digit
			if (rawNumbers[digitKey] === 0) {
				percentageResults.push(rawNumbers[digitKey])
			} else {
				percentageResults.push(
					parseFloat(((rawNumbers[digitKey] / rowsCount) * 100).toFixed(2))
				)
			}
		})

		return percentageResults
	} else {
		return null
	}
})

const handleGeneratedCalculation = (newCalculation: Calculation) => {
	dataset.value?.calculations?.push(newCalculation)
	currentColumn.value = newCalculation.column_name
}
</script>
<template>
	<main class="flex-grow py-10 max-w-7xl mx-auto">
		<section class="mb-40">
			<div class="flex justify-between gap-4 flex-col md:flex-row container">
				<div>
					<h1 class="heading mb-4">{{ dataset?.title }}</h1>
					<p class="text-md mb-8 max-w-prose">{{ dataset?.description }}</p>
				</div>
				<div>
					<a
						class="text-sm underline md:text-right inline-block md:block mb-8"
						:href="`${config.public.apiBrowserBase}/static/datasets/${dataset?.file_name}`">
						Download original file
					</a>
					<div class="relative justify-items-end mb-4">
						<Listbox v-model="currentColumn">
							<ListboxLabel>Column</ListboxLabel>
							<ListboxButton
								class="relative flex items-center justify-between px-4 py-3 text-left transition-all bg-[#201f22] border rounded-lg border-mono-300 focus:shadow-active focus:ring-primary-500 ring-inset w-56">
								<span>
									{{ currentColumn }}
								</span>
								<nuxt-icon name="chevron-double-down" />
							</ListboxButton>
							<transition
								leave-active-class="transition duration-100 ease-in"
								leave-from-class="opacity-100"
								leave-to-class="opacity-0">
								<ListboxOptions
									class="absolute w-full py-1 mt-1 overflow-auto text-base bg-[#201f22] rounded-md shadow-lg max-h-60 ring-1 ring-black ring-opacity-5 focus:outline-none sm:text-sm z-10">
									<ListboxOption
										v-slot="{ active, selected }"
										v-for="column in dataset?.file_columns"
										:key="column"
										:value="column"
										as="template">
										<li
											:class="[
												active ? 'bg-primary' : '',
												'relative cursor-pointer select-none py-2 px-4 flex items-center gap-3'
											]">
											<span
												:class="[
													selected
														? 'font-semibold text-primary-500'
														: 'font-normal',
													'block'
												]">
												{{ column }}</span
											>
										</li>
									</ListboxOption>
								</ListboxOptions>
							</transition>
						</Listbox>
					</div>
				</div>
			</div>
			<Chart
				v-if="!!calculation"
				:calculation="calculation"
				:column-data="columnData" />
			<NewCalculation
				:is-visible="!calculation"
				:current-column="currentColumn"
				:dataset-id="dataset?.id || ''"
				@on-generated-calculation="
					(newCalculation: any) => handleGeneratedCalculation(newCalculation)
				" />
		</section>
		<Heatmap :column-data="columnData" />
	</main>
</template>
