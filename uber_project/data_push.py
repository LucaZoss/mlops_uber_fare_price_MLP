import pandas as pd
import numpy as np
import json
import requests
import time
from datetime import datetime
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Go one directory up from BASE_DIR
UP_DIR = os.path.dirname(BASE_DIR)

# Construct the full path
original_csv_path = os.path.join(UP_DIR, 'ds/uber.csv')

df_source = pd.read_csv(original_csv_path)

# Filter original data to get only the features needed for prediction
df = df_source[['pickup_datetime', 'pickup_longitude', 'pickup_latitude',
                'dropoff_longitude', 'dropoff_latitude', 'passenger_count']]

# Data Dump Path
data_dump_path = os.path.join(UP_DIR, 'ds/data_preds_5s.json')

# Updated sampling function


def sample_from_dataframe(df, n_samples=1, random_state=None) -> str:
    rng = np.random.default_rng(seed=random_state)
    sampled_data = {
        'pickup_datetime': rng.choice(df['pickup_datetime'].astype(str), size=n_samples, replace=True).tolist(),
        'pickup_longitude': rng.choice(df['pickup_longitude'], size=n_samples, replace=True).tolist(),
        'pickup_latitude': rng.choice(df['pickup_latitude'], size=n_samples, replace=True).tolist(),
        'dropoff_longitude': rng.choice(df['dropoff_longitude'], size=n_samples, replace=True).tolist(),
        'dropoff_latitude': rng.choice(df['dropoff_latitude'], size=n_samples, replace=True).tolist(),
        'passenger_count': rng.choice(df['passenger_count'], size=n_samples, replace=True).tolist()
    }

    json_string = json.dumps(sampled_data)
    return json_string

# Function to send data to the FastAPI endpoint


def send_data_to_api(sampled_json) -> requests.Response:
    endpoint = 'http://localhost:8000/predict'
    try:
        # Convert JSON string back to Python object before sending
        data = json.loads(sampled_json)
        response = requests.post(endpoint, json=data)
        response.raise_for_status()
        print(f"[{datetime.now()}] Data sent successfully: {response.json()}")
    except requests.exceptions.RequestException as e:
        print(f"[{datetime.now()}] Error sending data to API: {e}")

    return response


def main():
    all_data = []  # Initialize an empty list to store all JSON objects

    while True:
        new_data = sample_from_dataframe(df, n_samples=1)
        print(f"[{datetime.now()}] Generated new data:\n{new_data}")

        # Send the generated data to the API
        results = send_data_to_api(new_data)

        if results is not None:
            # Parse input data and add predicted fare to it
            input_data = json.loads(new_data)

            # Extract the fare prediction value from the nested dictionary
            try:
                # Access the nested fare value directly
                predicted_fare = results.json(
                )["predicted_uber_fare_price"][0][0]
                input_data['predicted_uber_fare_price'] = predicted_fare
            except (KeyError, IndexError, TypeError) as e:
                print(f"[{datetime.now()}] Error processing prediction result: {e}")
                continue

            # Append the JSON object to the list
            all_data.append(input_data)

            # Save all collected data to a JSON file as a proper JSON array
            with open(data_dump_path, 'w') as f:
                json.dump(all_data, f, indent=4)

        # Wait for 5 secs before generating and sending new data
        time.sleep(5)


if __name__ == "__main__":
    main()
