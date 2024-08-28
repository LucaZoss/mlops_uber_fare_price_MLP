import os
# This is the Keras function for loading a model
from keras.models import load_model  # type: ignore
from joblib import load
import pandas as pd

from uber_project.feature_engineering import feature_engineering


# Define the base directory for the project inside the Docker container
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Construct the full path for the scaler file
scaler_path = os.path.join(BASE_DIR, 'scaler.pkl')
scaler = load(scaler_path)

# Load the model using the absolute path
model_path = os.path.join(BASE_DIR, 'model.keras')
model = load_model(model_path)


def predict_uber_fare_price(data: pd.DataFrame) -> float:
    df = feature_engineering(data)
    scaled_features = scaler.transform(df)
    prediction = model.predict(scaled_features)
    return prediction


if __name__ == "__main__":
    example_data = pd.DataFrame({
        'pickup_datetime': ['2012-04-05 18:10:00 UTC'],
        'pickup_longitude': [-73.971503],
        'pickup_latitude': [40.760135],
        'dropoff_longitude': [-73.961437],
        'dropoff_latitude': [40.768975],
        'passenger_count': [1]
    })
    # here result should be 5.3

    prediction = predict_uber_fare_price(example_data)
    print("Prediction:", prediction)
