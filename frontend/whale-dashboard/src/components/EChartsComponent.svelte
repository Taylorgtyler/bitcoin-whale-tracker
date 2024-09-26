<script lang="ts">
	import { onMount, onDestroy } from 'svelte';
	import { Chart } from 'svelte-echarts';
	import { init, use } from 'echarts/core';
	import { BarChart, LineChart, PieChart } from 'echarts/charts';
	import {
		GridComponent,
		TitleComponent,
		TooltipComponent,
		LegendComponent
	} from 'echarts/components';
	import { CanvasRenderer } from 'echarts/renderers';
	import type { EChartsOption } from 'echarts';
	import type { ChartData } from '$lib/types';

	// Register the required components
	use([
		BarChart,
		LineChart,
		PieChart,
		GridComponent,
		TitleComponent,
		TooltipComponent,
		LegendComponent,
		CanvasRenderer
	]);

	export let title: string;
	export let data: ChartData;
	export let width = '100%';
	export let height = '100%';
	export let colors: string[] = [];

	let options: EChartsOption;
	let chartInstance: echarts.ECharts | null = null;
	let chartContainer: HTMLElement;
	let isLoading = true;
	let error: string | null = null;

	$: updateOptions(title, data, colors);

	function updateOptions(chartTitle: string, chartData: ChartData, chartColors: string[]) {
		isLoading = true;
		error = null;

		try {
			if (!chartData || !chartData.xAxis || !chartData.series) {
				throw new Error('Invalid chart data');
			}

			options = {
				color: chartColors.length > 0 ? chartColors : undefined,
				title: {
					text: chartTitle
				},
				tooltip: {
					trigger: 'axis'
				},
				legend: {
					data: chartData.series.map((s) => s.name),
					orient: 'horizontal',
					bottom: 0
				},
				xAxis: {
					type: 'category',
					data: chartData.xAxis
				},
				yAxis: {
					type: 'value'
				},
				series: chartData.series
			};

			isLoading = false;
		} catch (e) {
			error = e instanceof Error ? e.message : 'An error occurred';
			isLoading = false;
		}
	}

	onMount(() => {
		const resizeObserver = new ResizeObserver(() => {
			if (chartInstance) {
				chartInstance.resize();
			}
		});

		resizeObserver.observe(chartContainer);

		return () => {
			resizeObserver.disconnect();
		};
	});

	function handleChartInit(e: CustomEvent<echarts.ECharts>) {
		chartInstance = e.detail;
	}

	onDestroy(() => {
		if (chartInstance) {
			chartInstance.dispose();
		}
	});
</script>

<div bind:this={chartContainer} class="chart-container" style="width: {width}; height: {height};">
	{#if isLoading}
		<div class="loading-overlay">
			<span class="loading-spinner"></span>
			<p>Loading chart...</p>
		</div>
	{:else if error}
		<div class="error-message">
			<p>Error: {error}</p>
		</div>
	{:else}
		<Chart {init} {options} on:init={handleChartInit} />
	{/if}
</div>
