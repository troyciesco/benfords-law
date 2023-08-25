import { Dataset } from "../types"

export default async function useDataset(datasetId: string) {
	const { data, pending, error } = await useFetch<Dataset>(
		`/api/dataset/${datasetId}`
	)
	return { data, pending, error }
}
