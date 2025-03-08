from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import pandas as pd

app = FastAPI()

# Define input data model
class ModelInput(BaseModel):
    longitude: float
    latitude: float
    housing_median_age: int
    total_rooms: int
    total_bedrooms: float
    population: int
    households: int
    median_income: float
    ocean_proximity: int

# Load the trained model
reg_model = pickle.load(open("model.pkl", "rb"))

# Define API endpoint for prediction
@app.post("/predict")
def predict_price(input_data: ModelInput):
    # Convert input data to DataFrame
    input_df = pd.DataFrame([input_data.dict()])
    
    # Make prediction
    prediction = reg_model.predict(input_df)
    predicted_price = prediction[0]
    
    return {"predicted_house_price": predicted_price}
