export type Digit = 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9

export type Dataset = {
	id: string
	title: string
	description?: string
	file_name: string
	file_columns: string[]
	calculations?: Calculation[]
}

export type Calculation = {
	id: string
	benford_law_distribution: { [K in Digit]: number }
	column_name: string
	rows_count: number
	skipped_rows_count: number
	dataset: Dataset
}
