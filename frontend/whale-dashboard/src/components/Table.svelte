<script lang="ts">
	type RowData = Record<string, any>;
	type PaginationItem = number | '...';

	export let data: RowData[];
	export let columns: { key: string; label: string; format?: (value: any) => string }[];
	export let itemsPerPage = 10;

	let currentPage = 1;
	$: totalPages = Math.ceil(data.length / itemsPerPage);
	$: paginatedData = data.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage);

	function nextPage() {
		if (currentPage < totalPages) currentPage++;
	}

	function prevPage() {
		if (currentPage > 1) currentPage--;
	}

	function goToPage(page: number) {
		if (page >= 1 && page <= totalPages) currentPage = page;
	}

	function getPaginationRange(
		current: number,
		total: number,
		display: number = 5
	): PaginationItem[] {
		if (total <= display) {
			return Array.from({ length: total }, (_, i) => i + 1);
		}

		let start = Math.max(current - Math.floor(display / 2), 1);
		let end = Math.min(start + display - 1, total);

		if (end === total) {
			start = Math.max(end - display + 1, 1);
		}

		let range: PaginationItem[] = Array.from({ length: end - start + 1 }, (_, i) => start + i);

		if (start > 1) {
			range.unshift('...');
			if (start > 2) {
				range.unshift(1);
			}
		}

		if (end < total) {
			range.push('...');
			if (end < total - 1) {
				range.push(total);
			}
		}

		return range;
	}

	$: paginationRange = getPaginationRange(currentPage, totalPages);
</script>

<div class="table-container">
	<table class="table">
		<thead>
			<tr>
				{#each columns as column}
					<th>{column.label}</th>
				{/each}
			</tr>
		</thead>
		<tbody>
			{#each paginatedData as row}
				<tr>
					{#each columns as column}
						<td>
							{#if column.format}
								{@html column.format(row[column.key])}
							{:else}
								{row[column.key]}
							{/if}
						</td>
					{/each}
				</tr>
			{/each}
		</tbody>
	</table>

	<div class="pagination">
		<button
			on:click={prevPage}
			disabled={currentPage === 1}
			class="pagination-button"
			class:pagination-button-disabled={currentPage === 1}
		>
			Previous
		</button>
		{#each paginationRange as page}
			{#if typeof page === 'number'}
				<button
					on:click={() => goToPage(page)}
					class="pagination-button"
					class:pagination-button-active={currentPage === page}
				>
					{page}
				</button>
			{:else}
				<span class="px-3 py-1">...</span>
			{/if}
		{/each}
		<button
			on:click={nextPage}
			disabled={currentPage === totalPages}
			class="pagination-button"
			class:pagination-button-disabled={currentPage === totalPages}
		>
			Next
		</button>
	</div>
</div>
