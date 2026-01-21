import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    # Remove duplicates
    df = df.drop_duplicates()

    # Strip column names
    df.columns = df.columns.str.strip()

    # Handle missing values
    for col in df.columns:
        if df[col].dtype == 'object':
            df[col] = df[col].fillna(df[col].mode()[0] if not df[col].mode().empty else "Unknown")
            df[col] = df[col].str.strip()
        else:
            df[col] = df[col].fillna(df[col].median())

    # Convert possible date columns
    for col in df.columns:
        try:
            df[col] = pd.to_datetime(df[col])
        except:
            pass

    return df
