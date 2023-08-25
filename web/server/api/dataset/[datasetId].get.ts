import { Dataset } from "../../../types"

const config = useRuntimeConfig()

export default defineEventHandler(async (event): Promise<Dataset> => {
	const dataset = await $fetch<Dataset>(
		`${config.public.apiBase}/datasets/${event.context.params!.datasetId}`
	)

	return dataset
})
