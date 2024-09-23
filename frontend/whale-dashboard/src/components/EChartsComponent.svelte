<script lang="ts">
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

	interface ChartData {
		xAxis: string[];
		series: {
			name: string;
			type: 'bar' | 'line' | 'pie';
			data: number[];
		}[];
	}

	export let title: string;
	export let data: ChartData;
	export let width = '100%';
	export let height = '400px';

	let options: EChartsOption;

	$: updateOptions(title, data);

	function updateOptions(chartTitle: string, chartData: ChartData) {
		options = {
			title: {
				text: chartTitle
			},
			tooltip: {
				trigger: 'axis'
			},
			legend: {
				data: chartData.series.map((s) => s.name)
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
	}
</script>

<div style="width: {width}; height: {height};">
	<Chart {init} {options} />
</div>
