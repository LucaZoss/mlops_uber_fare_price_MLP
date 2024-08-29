# MLOps UBER FARE PREDICTION API

This repository contains a production-ready API for predicting Uber fares using a machine learning model. The API is designed to be deployed for real-time fare predictions based on various input features.

## Project Overview

The goal of this project is to develop a machine learning-based solution that can predict Uber fare prices. The solution involves data preprocessing, model development, and API deployment.

### Key Components

1. **Data Preprocessing**:  
   - Data cleaning and feature engineering on Uber ride data.
   - Handling missing values, encoding categorical variables, and normalizing numerical features.

2. **Model Development**:  
   - Implemented a Multi-Layer Perceptron (MLP) model using Python and popular libraries such as `scikit-learn` and `TensorFlow`.
   - Hyperparameter tuning and model evaluation to optimize performance.

3. **API Development**:  
   - Built a RESTful API using `FastAPI` to expose the model for real-time fare prediction.
   - API endpoints allow users to input ride details and receive fare predictions.

### Project Setup

To run the project locally, ensure you have Python 3.11 installed. Follow the steps below:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/LucaZoss/mlops_uber_fare_price_MLP.git
   cd mlops_uber_fare_price_MLP


# SECTIONS TO ADD

-> Deeplearning Model
-> Docker File
-> FastAPI url for testing : uvicorn main:app --reload