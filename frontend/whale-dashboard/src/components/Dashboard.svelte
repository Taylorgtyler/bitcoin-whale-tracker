<script lang="ts">
	import EChartsComponent from './EChartsComponent.svelte';
	import type { ChartData } from '$lib/types';
	// Dummy data for a bar chart
	const barChartData: ChartData = {
		xAxis: ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'],
		series: [
			{
				name: 'Sales',
				type: 'bar',
				data: [120, 200, 150, 80, 70, 110, 130]
			}
		]
	};

	// Dummy data for a line chart
	const lineChartData: ChartData = {
		xAxis: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
		series: [
			{
				name: 'Revenue',
				type: 'line',
				data: [1000, 1500, 2000, 1800, 2200, 2400]
			}
		]
	};

	// Dummy data for a multi-series chart
	const multiSeriesData: ChartData = {
		xAxis: ['Q1', 'Q2', 'Q3', 'Q4'],
		series: [
			{
				name: 'Product A',
				type: 'bar',
				data: [120, 140, 160, 180]
			},
			{
				name: 'Product B',
				type: 'bar',
				data: [100, 110, 130, 140]
			}
		]
	};
</script>

<div class="dashboard">
	<div class="col-span-2">
		<EChartsComponent title="Weekly Sales" data={barChartData} />
	</div>
	<div class="col-span-1">
		<EChartsComponent title="Sales by Month" data={lineChartData} />
	</div>
	<div class="col-span-3">
		<EChartsComponent title="Sales by Product" data={multiSeriesData} />
	</div>
</div>
