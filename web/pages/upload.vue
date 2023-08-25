<script setup lang="ts">
import { Calculation } from "../types"

const config = useRuntimeConfig()

const columns = ref<string[]>([])
const rows = ref<string[][]>([])
const selectedColumns = ref<string[]>([])
const firstAnalysisColumn = ref("")
const title = ref("")
const description = ref("")
const fileName = ref("")
const isUploading = ref(false)
const isCreating = ref(false)
const isDisabled = computed(() => isCreating.value || isUploading.value)
const fileUploadError = ref("")
const formSubmitError = ref("")

async function uploadFile(event: Event) {
	fileUploadError.value = ""
	const input = event.target as HTMLInputElement
	isUploading.value = true
	const file = input.files![0]

	// 100MB file size limit
	if (file.size > 100 * 1024 * 1024) {
		fileUploadError.value =
			"File is too large, please select a file smaller than 100MB."
		isUploading.value = false
		return
	}

	const formData = new FormData()
	formData.append("file", file)

	type UploadFileResponse = {
		columns: string[]
		rows: string[][]
		file_name: string
	}

	// TODO: make an api route
	const { data, pending, error } = await useFetch<UploadFileResponse>(
		`${config.public.apiBrowserBase}/file/upload-temp-file`,
		{
			method: "POST",
			body: formData
		}
	)

	if (error.value) {
		fileUploadError.value =
			"An error occurred during file upload. Please try again."
		isUploading.value = false
		return
	}

	if (data.value) {
		columns.value = data.value.columns
		rows.value = data.value.rows
		fileName.value = data.value.file_name
	}
	isUploading.value = false
}

const toggleColumnSelection = (column: string) => {
	if (selectedColumns.value.includes(column)) {
		selectedColumns.value = selectedColumns.value.filter(
			(col) => col !== column
		)
	} else {
		selectedColumns.value.push(column)
	}
}

async function createDatasetAndCalculate() {
	formSubmitError.value = ""
	isCreating.value = true
	const errors = []
	if (!title.value) {
		errors.push("Title is a required field.")
	}
	if (!description.value) {
		errors.push("Description is a required field.")
	}
	if (!selectedColumns.value) {
		errors.push("You must select at least one column.")
	}
	if (!firstAnalysisColumn.value) {
		errors.push("You must select the first column for analysis.")
	}
	if (!fileName.value) {
		errors.push("You must have a file for upload.")
	}

	if (errors.length) {
		formSubmitError.value = errors.join(" ")
		isCreating.value = false
		return
	}
	const body = {
		title: title.value,
		description: description.value,
		selectedColumns: selectedColumns.value,
		firstAnalysisColumn: firstAnalysisColumn.value,
		fileName: fileName.value
	}

	const { data, pending, error } = await useFetch<Calculation>(
		"/api/dataset/create-and-calculate",
		{
			method: "POST",
			body: body
		}
	)
	if (error.value) {
		formSubmitError.value = "An error occurred. Please try again."
		isCreating.value = false
		return
	}
	if (data.value) {
		await navigateTo(`/datasets/${data.value.dataset.id}`)
	}
	isCreating.value = false
}
</script>

<template>
	<main class="py-10 container mx-auto">
		<div class="mb-8 max-w-7xl mx-auto">
			<h1 class="text-5xl">Dataset Upload</h1>
		</div>
		<form class="flex flex-col max-w-7xl mx-auto gap-8">
			<Panel
				title="Step 1: Upload file"
				description="Your file should have at least one column of numerical data greater
					than 1. Accepted file types are .tsv and .csv. Max file size is 100MB.">
				<div class="flex items-center gap-4">
					<label>
						Upload file
						<input
							type="file"
							@change="uploadFile"
							accept=".csv,.tsv,text/csv,text/tab-separated-values" />
					</label>
					<FormAlert
						:is-visible="!!fileUploadError"
						:message="fileUploadError" />
				</div>
			</Panel>
			<Panel
				title="Step 2: Double-check some data"
				description="Take a quick look at your data to make sure it makes sense. It's the
					first five, middle five, and last five of what you uploaded, or all
					rows if there's less than 15 in the file.">
				<div class="overflow-x-auto overflow-y-auto max-h-80">
					<table class="min-w-full min-h-full">
						<thead>
							<tr class="border">
								<th
									class="px-5 text-sm lg:text-base"
									v-for="(column, i) in columns"
									:key="`${column}-${i}`">
									{{ column }}
								</th>
							</tr>
						</thead>
						<tbody>
							<tr class="border" v-for="(row, i) in rows" :key="`row-${i}`">
								<td
									class="px-5 text-sm lg:text-base"
									v-for="(item, i) in row"
									:key="`${item}-${i}`">
									{{ item }}
								</td>
							</tr>
						</tbody>
					</table>
				</div>
			</Panel>
			<Panel
				title="Step 3: Choose analysis columns"
				description="Select the columns you'd like to have available for calculation. Make
					sure to select columns that have mostly numerical data and greater
					than 1. Text, numbers less than 1, etc. will be skipped in
					calculation.">
				<div class="flex flex-wrap items-center gap-8 lg:grid lg:grid-cols-6">
					<div
						v-for="(column, i) in columns"
						:key="`cb-${column}-${i}`"
						class="relative flex items-start">
						<label class="flex h-6 items-center">
							<input
								:id="`cb-${column}-${i}`"
								:name="column"
								type="checkbox"
								@click="() => toggleColumnSelection(column)"
								class="h-4 w-4 rounded border-gray-300 text-indigo-600 focus:ring-indigo-600" />
							<span class="font-medium truncate block ml-3 text-sm">
								{{ column }}
							</span>
						</label>
					</div>
				</div>
			</Panel>
			<Panel
				title="Step 4: Choose first column for analysis"
				description="We run the analysis on columns when they're first viewed, and then
					store the results for subsequent requests. Pick the first column you'd
					like to analyze.">
				<div class="flex flex-wrap items-center gap-4">
					<div
						v-for="(column, i) in selectedColumns"
						:key="`cb-${column}-${i}`"
						class="relative flex items-start">
						<button
							type="button"
							class="px-3 py-1 rounded-full border min-w-[80px]"
							:class="{ 'bg-primary': firstAnalysisColumn === column }"
							@click="() => (firstAnalysisColumn = column)">
							{{ column }}
						</button>
					</div>
				</div>
			</Panel>
			<Panel title="Step 5: Add final info and create!">
				<div>
					<div class="space-y-4 mb-12">
						<label class="flex flex-col">
							<span class="w-60 block mb-1">Title*</span>
							<input
								class="px-4 py-3 transition-all border rounded-lg grow border-mono-300 focus:shadow-active focus:ring-primary ring-inset bg-dark/70"
								type="text"
								v-model="title"
								placeholder="e.g. MLB Batting Career Stats" />
						</label>
						<label class="flex flex-col">
							<span class="w-60 block mb-1">Description</span>
							<textarea
								class="px-4 py-3 transition-all border rounded-lg grow border-mono-300 focus:shadow-active focus:ring-primary ring-inset bg-dark/70"
								rows="4"
								v-model="description"
								placeholder="e.g. This is a dataset all about how my life got flip-turned upside down..." />
						</label>
					</div>
					<div class="flex justify-end">
						<div class="flex flex-col items-end">
							<form @submit.prevent="createDatasetAndCalculate">
								<div class="flex items-center gap-4">
									<FormAlert
										:is-visible="!!formSubmitError"
										:message="formSubmitError" />
									<button
										:disabled="isDisabled"
										type="submit"
										class="btn--primary mb-2">
										{{ isCreating ? "Creating..." : "Create Dataset" }}
									</button>
								</div>
							</form>
							<p class="max-w-prose text-sm">
								We'll create the dataset and calculate the first column for you.
							</p>
						</div>
					</div>
				</div>
			</Panel>
		</form>
		<LoadingOverlay
			:is-open="isUploading || isCreating"
			:message="isUploading ? 'Uploading...' : 'Creating...'" />
	</main>
</template>
