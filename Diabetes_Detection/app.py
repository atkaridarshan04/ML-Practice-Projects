# Importing Dependencies
import numpy as np
import pickle
import streamlit as st

# Loading saved model
loaded_model = pickle.load(open('C:/Users/atkar/Desktop/Programing/AIML/Projects/Diabetes_Detection/trained_model.sav', 'rb'))

# Prediction Code
def prediction(input_data):

    input_array = np.asarray(input_data)

    input_array_reshaped = input_array.reshape(1,-1)

    prediction = loaded_model.predict(input_array_reshaped)
    print(prediction)

    if (prediction[0] == 0):
        return 'The person is not diabetic'
    else:
        return 'The person is diabetic'

# Main Function
def main():
    st.title("Diabetes Detection Web Interface")

    Pregnancies = st.text_input("Number of Pregnancies: ")
    Glucose = st.text_input("Glucose Level: ")
    BloodPressure = st.text_input("BloodPressure Value: ")
    SkinThickness = st.text_input("SkinThickness Value: ")
    Insulin = st.text_input("Insulin Level: ")
    BMI = st.text_input("BMI Level: ")
    DiabetesPedigreeFunction = st.text_input("DiabetesPedigreeFunction: ")
    Age = st.text_input("Age: ")

    result = ''

    if st.button('Get test results'):
        # Convert input values to float
        input_data = (float(Pregnancies), float(Glucose), float(BloodPressure), 
                          float(SkinThickness), float(Insulin), float(BMI), 
                          float(DiabetesPedigreeFunction), float(Age))

        try:
            result = prediction(input_data)
        except ValueError:
            result = "Please enter valid numeric values."

    st.success(result)

# Running web app
if __name__ == '__main__':
    main()
