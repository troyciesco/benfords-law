import { Dataset } from "../../types"

const config = useRuntimeConfig()
export default defineEventHandler(async (event): Promise<Dataset[]> => {
	const data = await $fetch<Dataset[]>(`${config.public.apiBase}/datasets`)
	return data
})
