import type { CryptoData } from '$lib/types';

export async function fetchCryptoData(cryptoSymbol: string): Promise<CryptoData[]> {
	const apiUrl = `http://localhost:8080/api/crypto/${cryptoSymbol}`;

	try {
		const response = await fetch(apiUrl);
		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`);
		}
		const data: CryptoData[] = await response.json();
		return data;
	} catch (error) {
		console.error(`Error fetching data for ${cryptoSymbol}:`, error);
		throw error;
	}
}

export async function fetchLastTransactions(): Promise<CryptoData[]> {
	const apiUrl = `http://localhost:8080/api/whale-transactions/recent?limit=10000`;

	try {
		const response = await fetch(apiUrl);
		if (!response.ok) {
			throw new Error(`HTTP error! status: ${response.status}`);
		}
		const data: CryptoData[] = await response.json();
		return data;
	} catch (error) {
		console.error(`Error fetching data:`, error);
		throw error;
	}
}
