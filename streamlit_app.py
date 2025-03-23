import streamlit as st
import requests

st.title('Loan Approval Predictor')

credit_score = st.number_input('Enter Credit Score', min_value=300, max_value=850, step=1)

if st.button('Predict'):
    url = "http://127.0.0.1:5000/predict"
    data = {"credit_score": credit_score}
    response = requests.post(url, json=data)

    if response.status_code == 200:
        result = response.json()
        st.success(f"Prediction: {result['prediction']}")
    else:
        st.error("Error connecting to the API.")
