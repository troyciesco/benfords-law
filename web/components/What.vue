<template>
	<section
		class="max-w-7xl mx-auto container mb-40 flex flex-col items-center xl:flex-row xl:items-start justify-between">
		<h2 class="heading mb-8 text-center lg:text-left">
			What even is <br class="hidden lg:block" />Benford's Law?
		</h2>
		<div class="space-y-4">
			<p class="body-text">
				First noted by Simon Newcomb in 1881 and later by Frank Benford in 1938,
				Benford's Law is an observation that in many numerical datasets the
				first digit in each number is likely to be small. This means that if you
				were looking at, say, career games played in MLB, you could expect 1 to
				be the first digit about 30% of the time, 2 about 17% of the time, and
				so on.
			</p>
			<p class="body-text">
				This won't apply to every dataset - there's more variance in small
				datasets and if the results are constrained within a certain range, the
				pattern won't be visible. But it happens enough that the results are
				<span class="text-gradient">pretty freaky</span>. This can be used for
				detecting fraud, since randomly generated numbers are usually evenly
				distributed.
			</p>
			<p class="body-text">
				Don't just take my word for it though, read all about it on your high
				school history teacher's
				<a href="https://en.wikipedia.org/wiki/Benford%27s_law">
					least favorite website</a
				>.
			</p>
		</div>
	</section>
</template>
