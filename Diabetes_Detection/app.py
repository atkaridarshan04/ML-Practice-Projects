# Import Dependencies
import numpy as np
import pickle
import streamlit as st

# Load the trained model
loaded_model = pickle.load(open('C:/Users/atkar/Desktop/Programing/AIML/Projects/Diabetes_Detection/trained_model.sav', 'rb'))

# Function to make predictions
def prediction(input_data):
    input_array = np.asarray(input_data).reshape(1, -1)
    pred = loaded_model.predict(input_array)

    if pred[0] == 0:
        return "✅ The person is **not diabetic**"
    else:
        return "❌ The person **is diabetic**"

# Streamlit Web App
def main():
    # Set page title & icon
    st.set_page_config(page_title="Diabetes Detection App", page_icon="🩺", layout="centered")

    # Add custom CSS styling
    st.markdown("""
        <style>
            body {
                background-color: #f7f9fc;
            }
            .main {
                background: white;
                padding: 20px;
                border-radius: 10px;
                box-shadow: 2px 2px 10px rgba(0, 0, 0, 0.1);
            }
            .stTextInput>div>div>input {
                font-size: 18px;
                padding: 10px;
            }
            .stButton>button {
                background-color: #4CAF50;
                color: white;
                font-size: 18px;
                padding: 10px;
                border-radius: 5px;
            }
        </style>
    """, unsafe_allow_html=True)

    # Title and description
    st.title("🩺 Diabetes Detection Web App")
    st.markdown("Enter the required health details below to check for **diabetes risk**.")

    # Create columns for better layout
    col1, col2 = st.columns(2)

    with col1:
        Pregnancies = st.text_input("Number of Pregnancies", key="pregnancies")
        Glucose = st.text_input("Glucose Level", key="glucose")
        BloodPressure = st.text_input("Blood Pressure", key="bloodpressure")
        SkinThickness = st.text_input("Skin Thickness", key="skinthickness")

    with col2:
        Insulin = st.text_input("Insulin Level", key="insulin")
        BMI = st.text_input("BMI", key="bmi")
        DiabetesPedigreeFunction = st.text_input("Diabetes Pedigree Function", key="dpf")
        Age = st.text_input("Age", key="age")

    result = ''

    # Button to get results
    if st.button('🔍 Get Test Results'):
        try:
            # Convert inputs to float
            input_data = [float(Pregnancies), float(Glucose), float(BloodPressure),
                          float(SkinThickness), float(Insulin), float(BMI),
                          float(DiabetesPedigreeFunction), float(Age)]
            result = prediction(input_data)
        except ValueError:
            result = "⚠️ Please enter valid **numeric values**."

    # Display result with appropriate color
    if result:
        if "not diabetic" in result:
            st.success(result)
        else:
            st.error(result)

    # Sidebar for additional info
    with st.sidebar:
        st.header("ℹ️ About This App")
        st.info("This app uses machine learning to predict diabetes risk based on medical parameters.")
        st.markdown("Developed with **Streamlit** & **Scikit-learn**.")

# Run the Streamlit app
if __name__ == '__main__':
    main()
