import { Calculation, Dataset } from "../../../types"

const config = useRuntimeConfig()

export default defineEventHandler(
	async (event): Promise<Calculation | null> => {
		const body = await readBody(event)
		const req = {
			title: body.title,
			description: body.description,
			file_name: body.fileName,
			file_columns: body.selectedColumns
		}
		const datasetResponse = await $fetch<Dataset>(
			`${config.public.apiBase}/datasets`,
			{
				method: "POST",
				body: JSON.stringify(req)
			}
		)
		let calculation = null
		if (datasetResponse) {
			const calculationRequest = { column_name: body.firstAnalysisColumn }
			const calculationResponse = await $fetch<Calculation>(
				`${config.public.apiBase}/datasets/${datasetResponse!.id}/calculations`,
				{
					method: "POST",
					body: JSON.stringify(calculationRequest)
				}
			)
			calculation = calculationResponse
		}
		return calculation
	}
)
