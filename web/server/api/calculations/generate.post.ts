import { Calculation } from "../../../types"

const config = useRuntimeConfig()

export default defineEventHandler(async (event): Promise<Calculation> => {
	const body = await readBody(event)
	const req = {
		column_name: body.columnName
	}
	const calculation = await $fetch<Calculation>(
		`${config.public.apiBase}/datasets/${body.datasetId}/calculations`,
		{
			method: "POST",
			body: JSON.stringify(req)
		}
	)
	return calculation
})
