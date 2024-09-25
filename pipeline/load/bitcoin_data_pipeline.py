from dune import Dune
from motherduck import MotherDuck
import polars as pl
import logging

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def pandas_to_polars(df):
    return pl.from_pandas(df)

def main():
    try:
        dune = Dune()
        motherduck = MotherDuck("my_db")

        query_id = 4075803
        logging.info(f"Executing Dune query with ID: {query_id}")
        results_df = dune.run_query_dataframe(query_id)

        if results_df is None or results_df.empty:
            logging.error("No data returned from Dune query")
            return

        logging.info(f"Received data from Dune. Shape: {results_df.shape}")

        polars_df = pandas_to_polars(results_df)
        logging.info("Converted Pandas DataFrame to Polars DataFrame")

        table_name = "last_10000_bitcoin_transactions"
        logging.info(f"Writing data to MotherDuck table: {table_name}")
        motherduck.write_dataframe(polars_df, table_name)

        logging.info("Executing sample query on MotherDuck")
        result = motherduck.execute_query(f"SELECT * FROM {table_name} LIMIT 10")
        
        if result is None or result.empty:
            logging.warning("No results returned from MotherDuck query")
        else:
            logging.info("Sample data from MotherDuck:")
            print(result)

    except Exception as e:
        logging.error(f"An error occurred: {str(e)}")
    finally:
        if 'motherduck' in locals():
            logging.info("Closing MotherDuck connection")
            motherduck.close()

if __name__ == "__main__":
    main()