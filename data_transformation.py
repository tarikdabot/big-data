import pandas as pd
import os

def clean_data(df):
    """
    Clean the DataFrame by handling missing values, duplicates, and type formatting.

    Args:
    - df (pd.DataFrame): Raw dataset.

    Returns:
    - pd.DataFrame: Cleaned dataset.
    """
    # 2.1 Handle Missing Values
    df.ffill(inplace=True)  # Forward fill for missing values

    # 2.2 Remove Duplicates
    df.drop_duplicates(inplace=True)

    # 2.3 Format Data Types
    # Ensure 'event_time' is in datetime format
    df['event_time'] = pd.to_datetime(df['event_time'], errors='coerce')

    # Ensure 'price' is numerical
    df['price'] = pd.to_numeric(df['price'], errors='coerce')

    # Handle inconsistencies and errors
    df['category_code'] = df['category_code'].fillna('Unknown')  # Avoid inplace=True

    print("Data cleaning completed.")
    return df

def add_sentiment_scores(df):
    """
    Generate sentiment scores based on 'event_type' (example approach).

    Args:
    - df (pd.DataFrame): Cleaned dataset.

    Returns:
    - pd.DataFrame: Dataset with sentiment scores.
    """
    sentiment_dict = {'purchase': 1, 'view': 0, 'click': 0.5}  # Example sentiment logic
    df['sentiment_score'] = df['event_type'].map(sentiment_dict).fillna(0)
    return df

if __name__ == "__main__":
    # Assuming the DataFrame is loaded in the previous step
    file_path = "../data/bigdatasate.csv"
    df = pd.read_csv(file_path)
    
    # Clean and transform the data
    df_cleaned = clean_data(df)  # Apply cleaning function
    df_cleaned = add_sentiment_scores(df_cleaned)  # Add sentiment scores

    # Ensure the output directory exists
    output_dir = "../output"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Save the cleaned data
    cleaned_file_path = os.path.join(output_dir, "cleaned_data.csv")
    df_cleaned.to_csv(cleaned_file_path, index=False)
    print(f"Cleaned data saved to {cleaned_file_path}")
    
    # Optionally, print the first few rows to verify
    print(df_cleaned.head())
