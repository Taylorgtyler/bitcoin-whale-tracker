import duckdb
from dotenv import load_dotenv
import os

class MotherDuck:
    def __init__(self, database):
        self.database = database
        self.connection = self.motherduck_connect()

    def motherduck_connect(self):
        try:
            load_dotenv()
            motherduck_key = os.environ.get('MOTHERDUCK_KEY')
            
            if not motherduck_key:
                raise ValueError("MOTHERDUCK_KEY not found in environment variables")
            
            connection_string = f'md:{self.database}?motherduck_token={motherduck_key}'
            
            conn = duckdb.connect(connection_string)
            
            print(f"Successfully connected to MotherDuck database: {self.database}")
            return conn
        except Exception as e:
            print(f"Error connecting to MotherDuck: {str(e)}")
            return None

    def write_dataframe(self, df, table_name, if_exists='replace'):
        if not self.connection:
            print("No connection to MotherDuck")
            return
        
        self.connection.register('df', df)
        if if_exists == 'replace':
            self.connection.execute(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM df")
        elif if_exists == 'append':
            self.connection.execute(f"INSERT INTO {table_name} SELECT * FROM df")
        else:
            raise ValueError("if_exists must be 'replace' or 'append'")
        print(f"Data written to MotherDuck table: {table_name}")

    def execute_query(self, query):
        if not self.connection:
            print("No connection to MotherDuck")
            return None
        return self.connection.execute(query).df()

    def close(self):
        if self.connection:
            self.connection.close()
            print(f"Disconnected from MotherDuck database: {self.database}")
