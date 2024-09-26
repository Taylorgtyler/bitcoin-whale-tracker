<script lang="ts">
	import type { PageData } from './$types';
	import Table from '../../components/Table.svelte';

	export let data: PageData;

	$: transactions = data.transactions || [];

	const columns = [
		{ key: 'id', label: 'ID' },
		{ key: 'size', label: 'Size' },
		{ key: 'input_value', label: 'Input Value' },
		{ key: 'output_value', label: 'Output Value' },
		{ key: 'fee', label: 'Fee' },
		{ key: 'is_coinbase', label: 'Is Coinbase' },
		{ key: 'block_hash', label: 'Block Hash' },
		{
			key: 'block_time',
			label: 'Block Time',
			format: (value: string) => new Date(value).toLocaleString()
		}
	];
</script>

<h1>Recent Whale Transactions</h1>

{#if transactions.length > 0}
	<Table data={transactions} {columns} itemsPerPage={10} />
{:else}
	<p>No recent transactions available.</p>
{/if}
