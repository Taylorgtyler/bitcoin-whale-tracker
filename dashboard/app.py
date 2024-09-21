from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from dotenv import load_dotenv
import os
import duckdb

## Dune Packages
from dune_client.types import QueryParameter
from dune_client.client import DuneClient
from dune_client.query import QueryBase


# Function to load environment variables

def load_credentials():
    try:
        # Load environment variables from the .env file
        load_dotenv()

        # Set motherduck api key
        motherduck_key = os.environ.get('MOTHERDUCK_KEY')

        # Set Dune api key
        dune_key = os.environ.get('DUNE_KEY')


        if not motherduck_key:
            raise ValueError("MOTHERDUCK_KEY not found in environment variables")
        
        if not dune_key:
            raise ValueError("DUNE_KEY not found in environment variables")
        
        return motherduck_key, dune_key
    except Exception as e:
        print(f"Error loading credentials: {str(e)}")


# Function to start the motherduck client

def motherduck_connect(motherduck_key, database):
    try:
        # Construct the connection string
        connection_string = f'md:{database}?motherduck_token={motherduck_key}'
        
        # Attempt to connect to MotherDuck
        conn = duckdb.connect(connection_string)
        
        print(f"Successfully connected to MotherDuck database: {database}")
        return conn
    except Exception as e:
        print(f"Error connecting to MotherDuck: {str(e)}")
        return None
    
    # Start Dune Client
def create_dune_client(dune_key):
        try:

            # Attempt to connect to Dune
            dune = DuneClient(dune_key)

            print(f"Successfully connected to Dune")

        except Exception as e:
            print(f"Error connecting to Dune: {str(e)}")

            return dune



# Run Dune Query and save output to pandas dataframe
    


database = "sample_data"

# Load credentials and connect to MotherDuck
motherduck_key = load_credentials()
if motherduck_key:
    connection = motherduck_connect(motherduck_key, database)
    if connection:
        print("Connected to MotherDuck successfully")
    else:
        print("Failed to connect to MotherDuck")
else:
    print("Failed to load credentials")


# Initialize the dash app
app = Dash()

# Create dash app layout
app.layout = [
    html.H1(children='NYC Rideshare', style={'textAlign':'center'})
]


if __name__ == '__main__':
    app.run(debug=True)