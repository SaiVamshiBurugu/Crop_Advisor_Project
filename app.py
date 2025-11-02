import streamlit as st
import numpy as np
import joblib

pipeline = joblib.load("Crop_Pridictor_Model.joblib")
encoder = joblib.load("crop_pridctor_label_encoder.joblib")

st.set_page_config(page_title="Crop Advisor", layout="centered")
st.title("🌾 Smart Crop Recommendation System")
st.write("This app predicts the most suitable crop based on soil and weather conditions.")

st.header("Enter Soil and Weather Details")

N = st.number_input("Nitrogen (N)", 0, 140, 50)
P = st.number_input("Phosphorus (P)", 0, 140, 50)
K = st.number_input("Potassium (K)", 0, 200, 50)
temperature = st.number_input("Temperature (°C)", 0.0, 50.0, 25.0)
humidity = st.number_input("Humidity (%)", 0.0, 100.0, 70.0)
ph = st.number_input("pH Value", 0.0, 14.0, 6.5)
rainfall = st.number_input("Rainfall (mm)", 0.0, 300.0, 100.0)

if st.button("🌱 Recommend Crop"):
    # Prepare input
    input_data = np.array([[N, P, K, temperature, humidity, ph, rainfall]])

    # Predict
    pred = pipeline.predict(input_data)
    crop_name = encoder.inverse_transform(pred)[0]

    st.success(f"✅ Recommended Crop: **{crop_name}**")