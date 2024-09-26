import { fetchLastTransactions } from '$lib/api/fetchCryptoData';
import type { PageServerLoad } from './$types';
import type { CryptoData } from '$lib/types'; // Assuming you have a types file

export const load: PageServerLoad = async () => {
	try {
		const transactions: CryptoData[] = await fetchLastTransactions();
		return {
			transactions
		};
	} catch (error) {
		console.error('Failed to load recent transactions:', error);
		return {
			transactions: [],
			error: 'Failed to load recent transactions'
		};
	}
};
