import os
from dotenv import load_dotenv
from dune_client.types import QueryParameter
from dune_client.client import DuneClient

class Dune:
    def __init__(self):
        self.client = None
        self.load_credentials()
        self.create_dune_client()

    def load_credentials(self):
        result = load_dotenv()
        if result:
            print("Credentials loaded successfully")
        else:
            print("Failed to load credentials")

    def create_dune_client(self):
        try:
            dune_key = os.environ.get('DUNE_KEY')
            
            if not dune_key:
                raise ValueError("DUNE_KEY not found in environment variables")
            
            self.client = DuneClient(dune_key)
            print("Successfully connected to Dune")
        except Exception as e:
            print(f"Error connecting to Dune: {str(e)}")

    def execute_query(self, query_id, params=None):
        if not self.client:
            print("Dune client not initialized")
            return None

        try:
            query_parameters = []
            if params:
                for key, value in params.items():
                    query_parameters.append(QueryParameter(key, value))

            result = self.client.refresh(query_id, query_parameters)
            return result.result
        except Exception as e:
            print(f"Error executing query: {str(e)}")
            return None

    def get_latest_result(self, query_id):
        if not self.client:
            print("Dune client not initialized")
            return None

        try:
            result = self.client.get_latest_result(query_id)
            return result.result
        except Exception as e:
            print(f"Error getting latest result: {str(e)}")
            return None

    def get_query_results(self, query_id):
        if not self.client:
            print("Dune client not initialized")
            return None

        try:
            result = self.client.get_result(query_id)
            return result.result
        except Exception as e:
            print(f"Error getting query results: {str(e)}")
            return None