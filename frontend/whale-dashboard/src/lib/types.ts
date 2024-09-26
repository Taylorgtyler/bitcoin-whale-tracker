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
	input_value: number;
	output_value: number;
	fee: number;
	is_coinbase: boolean;
	block_hash: string;
	block_time: string;
}

export interface TableDataItem {
	[key: string]: string | number | boolean | null | undefined;
}

export type TableData = TableDataItem[];

export interface PageData {
	transactions: CryptoData[];
	error?: string;
}
