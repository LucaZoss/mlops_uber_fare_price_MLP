# MLOps Uber Fare Prediction API

## Project Overview
This project aims to develop a machine learning-based solution for predicting Uber fare prices. It encompasses the entire lifecycle, from data preprocessing and model development to API deployment.

**Personal Goal:**
The objective of this repository is to create a production-ready machine learning solution, wrapping the code into an API, containerizing it with Docker, and eventually setting up a CI/CD pipeline using GitHub Actions.

The repository contains two branches:

- **main**: Stable branch.
- **feature/production-ready-api**: Development branch for creating a simple MLP model to predict Uber fare prices.

### Project Setup

To run the project locally, ensure you have Python 3.11 installed. Follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/LucaZoss/mlops_uber_fare_price_MLP.git
   cd mlops_uber_fare_price_MLP
   ```

Alternatively, you can use Docker to run the project by copying the provided Dockerfile.

This project uses Python Poetry for dependency management and environment setup.

To run the app and make predictions:

1. Open a terminal and run:
   ```bash
   cd ./uber_project
   uvicorn main:app --reload
   ```

2. Open a second terminal and run:
   ```bash
   cd ./uber_project
   python run data_push
   ```
   Or, use the Poetry shell.

### Key Components

1. **Jupyter Notebooks for Prototyping**:
   - Conducted quick feature engineering, such as calculating distances using geo-based latitude and longitude data.
   - **Model Development**: Created a fully connected neural network using TensorFlow Keras.
   - Note: There's room for deeper exploratory data analysis (EDA), experimenting with different ML/DL models, and strengthening the model evaluation framework.

2. **API Development**:
   - Developed a RESTful API using `FastAPI` to provide real-time fare predictions. Access the Swagger documentation at [http://localhost:8000/docs](http://localhost:8000/docs).

### Future Improvements

- Implement a CI/CD pipeline using GitHub Actions.
- Develop unit and integration tests with `pytest`.
- Create a more comprehensive `model_train.py` script for model enhancements.
- Build a Streamlit app for improved user experience.
- Integrate real-time data streaming capabilities.