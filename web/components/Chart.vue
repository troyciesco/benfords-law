<script setup lang="ts">
import { BENFORDS_LAW_ARR } from "../constants"
import { Calculation } from "../types"

const props = defineProps<{
	calculation: Calculation
	columnData: number[] | null
}>()
const { calculation, columnData } = toRefs(props)
const series = computed(() => [
	{
		name: calculation.value.column_name,
		type: "column",
		data: columnData.value
	},
	{
		name: "Benford's Law",
		type: "line",
		data: BENFORDS_LAW_ARR
	}
])

const options = {
	chart: {
		zoom: {
			enabled: false
		},
		height: 600,
		type: "line",
		toolbar: {
			show: false
		}
	},
	colors: ["#8068f0", "#df1683"],
	stroke: {
		width: [0, 4]
	},
	dataLabels: {
		enabled: true,
		textAnchor: "middle",
		offsetY: 0,
		enabledOnSeries: [0],
		formatter: function (val: number) {
			return `${val}%`
		},
		background: {
			foreColor: "#fff8df",
			borderColor: "#fff8df"
		}
	},
	labels: [1, 2, 3, 4, 5, 6, 7, 8, 9],
	xaxis: {
		title: {
			text: "First Digit",
			style: {
				color: "#fff8df"
			}
		},
		type: "numeric",
		tickAmount: "dataPoints",
		decimalsInFloat: 0,
		labels: {
			style: {
				colors: "#fff8df"
			}
		}
	},
	yaxis: [
		{
			title: {
				text: "Frequency (%)",

				style: {
					color: "#fff8df"
				}
			},
			labels: {
				formatter: function (val: number) {
					return `${val}%`
				},
				style: {
					colors: "#fff8df"
				}
			}
		}
	],
	legend: {
		position: "top",
		labels: {
			colors: "#fff8df"
		}
	},
	tooltip: {
		theme: "dark",
		x: {
			formatter: (label: string) => `First Digit: ${label}`
		}
	}
}
</script>

<template>
	<div v-if="!!calculation" class="w-full h-[600px] px-2 md:container">
		<ClientOnly>
			<apexchart
				:key="series"
				height="600"
				width="100%"
				:options="options"
				:series="series"></apexchart>
		</ClientOnly>
		<div class="mt-4 container">
			<p v-if="calculation" class="text-sm italic">
				processed rows: {{ calculation.rows_count }}, skipped rows:
				{{ calculation.skipped_rows_count }}
			</p>
		</div>
	</div>
</template>
