from sklearn.preprocessing import MinMaxScaler

def scale_sensors(df, sensor_cols):
    """Normalize sensor columns between 0 and 1"""
    scaler = MinMaxScaler()
    df[sensor_cols] = scaler.fit_transform(df[sensor_cols])
    return df, scaler
