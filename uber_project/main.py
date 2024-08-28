from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import pandas as pd
from uber_project.predict import predict_uber_fare_price

app = FastAPI()

# Define the input data model


# Define the input data model
class UberFarePriceRequest(BaseModel):
    pickup_datetime: List[str]
    pickup_longitude: List[float]
    pickup_latitude: List[float]
    dropoff_longitude: List[float]
    dropoff_latitude: List[float]
    passenger_count: List[int]

# Define the prediction endpoint


@app.post("/predict")
def predict_eta_endpoint(request: UberFarePriceRequest):
    try:
        # Convert input features to a pandas DataFrame
        features_df = pd.DataFrame({
            'pickup_datetime': request.pickup_datetime,
            'pickup_longitude': request.pickup_longitude,
            'pickup_latitude': request.pickup_latitude,
            'dropoff_longitude': request.dropoff_longitude,
            'dropoff_latitude': request.dropoff_latitude,
            'passenger_count': request.passenger_count
        })

        # Make the prediction
        prediction = predict_uber_fare_price(features_df)

        # Convert numpy array to list for JSON serialization
        return {"predicted_uber_fare_price": prediction.tolist()}
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))
