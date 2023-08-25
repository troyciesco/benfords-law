<template>
	<section class="max-w-7xl mx-auto container mb-20">
		<h2 class="heading mb-8 text-center">How this visualizer works</h2>
		<div class="space-y-10 flex flex-col items-center xl:block">
			<div class="flex flex-col xl:flex-row gap-5 xl:gap-10 xl:items-center">
				<div class="text-5xl xl:text-[10rem]">1.</div>
				<p class="body-text">
					Upload a dataset as a .csv or .tsv file. Choose the columns that you'd
					like to have available for analysis. The best columns to use are those
					with a large amount of numerical data greater than 1. You can also
					explore other datasets that others have already uploaded.
				</p>
			</div>
			<div
				class="flex flex-col xl:flex-row gap-5 xl:gap-10 xl:items-center xl:justify-end">
				<div class="text-5xl xl:text-[10rem]">2.</div>
				<p class="body-text">
					You'll be taken to the dataset page, where you can see the results of
					the analysis of the first column. The line on the graph represents the
					frequency of a digit expected by Benford's Law, and the bars represent
					the percentage of the data that starts with that digit.
				</p>
			</div>
			<div class="flex flex-col xl:flex-row gap-5 xl:gap-10 xl:items-center">
				<div class="text-5xl xl:text-[10rem]">3.</div>
				<p class="body-text">
					There's also a heatmap that shows the difference between the expected
					percentage for a digit based on Benford's law and the actual results
					from the dataset. If you use a dataset measuring something like MLB
					career games played you'll see a lot of green, signifying the data
					fits nicely in Benford's law. Randomized numbers will produce a lot of
					yellow, red, and gray.
				</p>
			</div>
			<div
				class="flex flex-col xl:flex-row gap-5 xl:gap-10 xl:items-center xl:justify-end">
				<div class="text-5xl xl:text-[10rem]">4.</div>
				<p class="body-text">
					You'll be taken to the dataset page, where you can see the results of
					the analysis of the first column. The line on the graph represents the
					frequency of a digit expected by Benford's Law, and the bars represent
					the percentage of the data that starts with that digit.
				</p>
			</div>
		</div>
	</section>
</template>
