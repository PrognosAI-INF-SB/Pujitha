import pandas as pd

def load_cmapss_dataset(file_path):
    """Load NASA CMAPSS dataset into a DataFrame"""
    col_names = ['unit_number', 'time_in_cycles'] + \
                [f'operational_setting_{i}' for i in range(1,4)] + \
                [f'sensor_{i}' for i in range(1,22)]
    
    df = pd.read_csv(file_path, sep=' ', header=None)
    df = df.dropna(axis=1, how='all')  # remove empty columns
    df.columns = col_names
    return df
