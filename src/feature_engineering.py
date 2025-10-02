import numpy as np

def add_rul_column(df):
    """Compute Remaining Useful Life (RUL) for each engine"""
    rul = df.groupby('unit_number')['time_in_cycles'].max().reset_index()
    rul.columns = ['unit_number', 'max_cycle']
    df = df.merge(rul, on='unit_number')
    df['RUL'] = df['max_cycle'] - df['time_in_cycles']
    return df.drop('max_cycle', axis=1)

def create_sequences(df, sequence_length=30, feature_cols=None, target_col='RUL'):
    """Create rolling window sequences for time-series models"""
    X, y = [], []
    for engine_id in df['unit_number'].unique():
        engine_data = df[df['unit_number'] == engine_id]
        features = engine_data[feature_cols].values
        targets = engine_data[target_col].values

        for i in range(len(engine_data) - sequence_length):
            X.append(features[i:i+sequence_length])
            y.append(targets[i+sequence_length])
    return np.array(X), np.array(y)
