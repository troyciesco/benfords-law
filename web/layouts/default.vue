<script lang="ts" setup></script>

<template>
	<div class="flex flex-col min-h-screen">
		<Header />
		<div class="grow">
			<slot />
		</div>
		<Footer />
	</div>
</template>

<style scoped></style>
