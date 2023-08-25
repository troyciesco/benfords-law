import { Dataset } from "../types"

export default async function useDatasets() {
	const { data, pending, error } = await useFetch<Dataset[]>(`/api/datasets`)

	return { data, pending, error }
}
