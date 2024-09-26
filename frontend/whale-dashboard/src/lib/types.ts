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

export interface CryptoData {
	id: string;
	size: number;
	inputValue: number;
	outputValue: number;
	fee: number;
	isCoinbase: boolean;
	block_hash: string;
	block_time: string;
}
