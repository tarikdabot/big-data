import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def check_table_exists(engine, table_name):
    """
    Check if the table exists in the PostgreSQL database.
    """
    query = f"""
        SELECT EXISTS (
            SELECT 1
            FROM information_schema.tables
            WHERE table_name = '{table_name}'
        );
    """
    with engine.connect() as connection:
        result = connection.execute(query).fetchone()
        return result[0]  # True if table exists, False otherwise

def load_data_to_postgres(df, db_url, table_name):
    """
    Load the DataFrame into the PostgreSQL database after checking if the table exists.
    """
    engine = create_engine(db_url)
    
    try:
        # Check if the table exists
        if check_table_exists(engine, table_name):
            print(f"Table '{table_name}' exists. Data will be loaded into it.")
        else:
            print(f"Table '{table_name}' does not exist. It will be created.")
        
        # Load data into the table, create if doesn't exist
        df.to_sql(table_name, engine, index=False, if_exists='replace')  # 'replace' will create or replace the table
        print(f"Data loaded into {table_name} successfully.")
        
    except Exception as e:
        print(f"Error loading data: {e}")

if __name__ == "__main__":
    # Load data from the transformed DataFrame (previous step)
    file_path = "../data/bigdatasate.csv"
    df = pd.read_csv(file_path)
    
    # Assume that data is already cleaned and sentiment scores are added
    df_cleaned = pd.read_csv("../output/cleaned_data.csv")  # Path to cleaned data
    
    # Get the database URL from the environment variable
    db_url = os.getenv("DB_URL")
    
    # Load data into PostgreSQL
    load_data_to_postgres(df_cleaned, db_url, 'ecommerce_data')
