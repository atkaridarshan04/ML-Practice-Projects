import requests
import json

# Define the API URL
url = "http://127.0.0.1:8000/predict"

# Sample input data
sample_data = {
    "longitude": -122.23,
    "latitude": 37.88,
    "housing_median_age": 41,
    "total_rooms": 880,
    "total_bedrooms": 129.0,
    "population": 322,
    "households": 126,
    "median_income": 8.3252,
    "ocean_proximity": "0"
}

# Send a POST request
response = requests.post(url, json=sample_data)

# Print the response
print("Response Status Code:", response.status_code)
print("Predicted House Price:", response.json())