from dash import Dash, html, dcc, callback, Output, Input
import plotly.express as px
import pandas as pd
from dotenv import load_dotenv
import os
import duckdb

# Dune Packages
from dune_client.types import QueryParameter
from dune_client.client import DuneClient
from dune_client.query import QueryBase

# Function to load environment variables
def load_credentials():
    result = load_dotenv()
    print("Credentials loaded successfully" if result else "Failed to load credentials")

# Function to start the motherduck client
def motherduck_connect(database):
    try:
        # Set the motherduck key
        motherduck_key = os.environ.get('MOTHERDUCK_KEY')
        
        if not motherduck_key:
            raise ValueError("MOTHERDUCK_KEY not found in environment variables")
        
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
def create_dune_client():
    try:
        # Set Dune api key
        dune_key = os.environ.get('DUNE_KEY')
        
        if not dune_key:
            raise ValueError("DUNE_KEY not found in environment variables")
        
        # Attempt to connect to Dune
        dune = DuneClient(dune_key)
        
        print(f"Successfully connected to Dune")
        return dune 
    except Exception as e:
        print(f"Error connecting to Dune: {str(e)}")
        return None

# Load credentials at the start of the script
load_credentials()

database = "sample_data"

# Connect to MotherDuck
connection = motherduck_connect(database)
if connection:
    print("Connected to MotherDuck successfully")
else:
    print("Failed to connect to MotherDuck")
    exit(1)  # Exit if connection fails

# Initialize the dash app
app = Dash(__name__)

# Retrieve data from motherduck using the established connection
try:
    df = connection.execute("SELECT * FROM nyc.rideshare").df()
    df['request_datetime'] = pd.to_datetime(df['request_datetime'])
    print("Data retrieved successfully")
except Exception as e:
    print(f"Error retrieving data: {str(e)}")
    exit(1)  # Exit if data retrieval fails

# Create dash app layout
app.layout = html.Div([
    html.H1(children='NYC Rideshare', style={'textAlign':'center'}),
    dcc.Graph(id='rideshare-graph'),
    dcc.Dropdown(
        id='metric-dropdown',
        options=[
            {'label': 'Trip Duration', 'value': 'trip_duration'},
            {'label': 'Trip Distance', 'value': 'trip_distance'},
            {'label': 'Total Amount', 'value': 'total_amount'}
        ],
        value='trip_duration',
        style={'width': '50%'}
    )
])

@callback(
    Output('rideshare-graph', 'figure'),
    Input('metric-dropdown', 'value')
)
def update_graph(selected_metric):
    fig = px.line(df, x='request_datetime', y=selected_metric, title=f'NYC Rideshare - {selected_metric.replace("_", " ").title()}')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)