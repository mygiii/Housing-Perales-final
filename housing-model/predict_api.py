import mlflow
import mlflow.sklearn
import pandas as pd
from fastapi import FastAPI
from pydantic import BaseModel

# Connect to MLflow
mlflow.set_tracking_uri("http://mlflow_server:5000")

# Load latest model from MLflow
model_name = "California_Housing_Model"
model = mlflow.sklearn.load_model(f"models:/{model_name}/latest")

# Define expected input structure
class HouseFeatures(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: float
    total_rooms: float
    total_bedrooms: float
    population: float
    households: float
    median_income: float
    ocean_proximity_INLAND: int = 0
    ocean_proximity_NEAR_BAY: int = 0
    ocean_proximity_NEAR_OCEAN: int = 0
    ocean_proximity_ISLAND: int = 0

app = FastAPI()

@app.post("/predict")
def predict(features: HouseFeatures):
    # Convert input data to DataFrame
    data = pd.DataFrame([features.dict()])

    # Make prediction
    prediction = model.predict(data)

    return {"predicted_value": float(prediction[0])}
