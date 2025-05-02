# src/data_processor.py

import pandas as pd

def load_data(uploaded_file):
    """
    Attempts to read a CSV file with UTF-8 encoding first, 
    then falls back to Latin-1 if necessary.
    """
    try:
        df = pd.read_csv(uploaded_file, encoding='utf-8')
    except UnicodeDecodeError:
        try:
            df = pd.read_csv(uploaded_file, encoding='latin1')
        except Exception as e:
            print(f"⚠️ Failed to load data even with Latin-1: {e}")
            return None
    except Exception as e:
        print(f"⚠️ General data loading error: {e}")
        return None

    # Basic sanity check
    if df is not None and df.empty:
        print("⚠️ Loaded data is empty.")
        return None
    
    return df


def summarize_data(df):
    """
    Summarizes the structure and health of the dataset.
    Returns a vertically formatted summary DataFrame.
    """
    try:
        summary_data = {
            "Total Rows": [df.shape[0]],
            "Total Columns": [df.shape[1]],
            "Missing Values": [df.isnull().sum().sum()],
            "Numeric Columns": [len(df.select_dtypes(include='number').columns)],
            "Categorical Columns": [len(df.select_dtypes(include='object').columns)],
            "Date Columns": [len(df.select_dtypes(include='datetime').columns)],
        }
        summary_df = pd.DataFrame(summary_data).T.rename(columns={0: "Value"})
        return summary_df
    except Exception as e:
        print(f"⚠️ Failed to summarize data: {e}")
        return pd.DataFrame({"Error": [str(e)]})
