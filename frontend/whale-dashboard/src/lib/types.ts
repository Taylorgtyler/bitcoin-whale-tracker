export interface ChartData {
	xAxis: string[];
	series: {
		name: string;
		type: 'bar' | 'line' | 'pie';
		data: number[];
	}[];
}

export interface ChartProps {
	title: string;
	data: ChartData;
	width?: string;
	height?: string;
}
