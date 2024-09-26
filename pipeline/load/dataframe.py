import polars as pl

def pandas_to_polars(df):
    return pl.from_pandas(df)