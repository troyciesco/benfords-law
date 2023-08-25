<script setup lang="ts">
import type { Dataset } from "../types"
const props = defineProps<{ dataset: Dataset }>()
const { dataset } = toRefs(props)
</script>

<template>
	<NuxtLink :to="`datasets/${dataset.id}`">
		<div
			class="border border-[#fff8df] border-opacity-10 px-8 py-5 bg-[#222124] shadow-md hover:shadow-lg transition-all hover:shadow-[#3138fb85] duration-300 hover:scale-105">
			<h2 class="text-2xl line-clamp-1 mb-4">{{ dataset.title }}</h2>
			<div class="h-40">
				<p class="mb-8 font-sans line-clamp-5">
					{{ dataset.description }}
				</p>
			</div>
			<span class="italic"
				>{{ dataset.file_columns.length }} column{{
					dataset.file_columns.length === 1 ? "" : "s"
				}}</span
			>
		</div>
	</NuxtLink>
</template>
