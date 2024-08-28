import pandas as pd
import numpy as np

# Function for Feature Engineering


def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # radius of Earth in kilometers
    phi1 = np.radians(lat1)
    phi2 = np.radians(lat2)
    delta_phi = np.radians(lat2 - lat1)
    delta_lambda = np.radians(lon2 - lon1)
    a = np.sin(delta_phi / 2) ** 2 + np.cos(phi1) * \
        np.cos(phi2) * np.sin(delta_lambda / 2) ** 2
    res = R * (2 * np.arctan2(np.sqrt(a), np.sqrt(1 - a)))
    return np.round(res, 2)  # returns distance in kilometers


def feature_engineering(data: pd.DataFrame) -> pd.DataFrame:
    df = data.copy()
    # Only take the necessary columns:
    # ['pickup_datetime', 'pickup_longitude', 'pickup_latitude', 'dropoff_longitude', 'dropoff_latitude', 'passenger_count']
    df['pickup_datetime'] = df['pickup_datetime'].apply(
        lambda x: x[: len('2015-05-07 19:52:06')])
    df['pickup_datetime'] = pd.to_datetime(
        df['pickup_datetime'], format='%Y-%m-%d %H:%M:%S')
    df['Year'] = df['pickup_datetime'].dt.year
    df['Month'] = df['pickup_datetime'].dt.month
    df['Date'] = df['pickup_datetime'].dt.day
    df['Hour'] = df['pickup_datetime'].dt.hour
    df['Day_of_week'] = df['pickup_datetime'].dt.dayofweek
    df.drop('pickup_datetime', axis=1, inplace=True)

    # Computing distance
    df['distance'] = haversine_distance(
        df['pickup_latitude'], df['pickup_longitude'], df['dropoff_latitude'], df['dropoff_longitude'])

    # Drop columns used for distance calculation
    df.drop(['pickup_latitude', 'pickup_longitude',
             'dropoff_latitude', 'dropoff_longitude'], axis=1, inplace=True)

    return df
