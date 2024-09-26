package database

import "fmt"

func (ctx *DBContext) ExecuteQuery(query string, args ...interface{}) ([]map[string]interface{}, error) {
	rows, err := ctx.DB.Query(query, args...)
	if err != nil {
		return nil, fmt.Errorf("failed to execute query: %w", err)
	}
	defer rows.Close()

	columns, err := rows.Columns()
	if err != nil {
		return nil, fmt.Errorf("failed to get column names: %w", err)
	}

	var result []map[string]interface{}
	for rows.Next() {
		values := make([]interface{}, len(columns))
		pointers := make([]interface{}, len(columns))
		for i := range values {
			pointers[i] = &values[i]
		}

		if err := rows.Scan(pointers...); err != nil {
			return nil, fmt.Errorf("failed to scan row: %w", err)
		}

		row := make(map[string]interface{})
		for i, column := range columns {
			row[column] = values[i]
		}
		result = append(result, row)
	}

	if err := rows.Err(); err != nil {
		return nil, fmt.Errorf("error iterating rows: %w", err)
	}

	return result, nil
}

// Add more specific query methods as needed, for example:

func (ctx *DBContext) GetRecentWhaleTransactions(limit int) ([]map[string]interface{}, error) {
	query := `
		select * from main.last_10000_bitcoin_transactions
		order by block_time DESC
		LIMIT ?
	`
	return ctx.ExecuteQuery(query, limit)
}

// Get largest whale transaction this week
func (ctx *DBContext) GetLargestWhaleTransactionThisWeek() (map[string]interface{}, error) {
    query := `
        SELECT *
        FROM main.last_10000_bitcoin_transactions
        where strptime(block_time, '%Y-%m-%d %H:%M:%S.%f UTC') >= date_trunc('week', current_date)
        order by input_value desc
        limit 1
    `
    results, err := ctx.ExecuteQuery(query)
    if err != nil {
        return nil, err
    }
    if len(results) == 0 {
        return nil, nil
    }
    return results[0], nil
}