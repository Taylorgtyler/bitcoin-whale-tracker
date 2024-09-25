import os
from dotenv import load_dotenv
from dune_client.client import DuneClient
from dune_client.query import QueryBase

class Dune:
    def __init__(self):
        self.client = self.create_dune_client()

    def create_dune_client(self):
        load_dotenv()
        dune_key = os.environ.get('DUNE_KEY')
        if not dune_key:
            raise ValueError("DUNE_KEY not found in environment variables")
        return DuneClient(dune_key)

    def run_query_dataframe(self, query_id, params=None):
        query = QueryBase(query_id=query_id)
        if params:
            for key, value in params.items():
                setattr(query, key, value)
        return self.client.run_query_dataframe(query)
    
    def get_last_results(self, query_id):
        result =  DuneClient.get_latest_result(query_id, max_age_hours=8) 

        return result