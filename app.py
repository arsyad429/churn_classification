import streamlit as st
import joblib
import numpy as np
import pandas as pd

# Load model
model = joblib.load('random_forest_model.pkl')
scaler = joblib.load('scaler.pkl') 

# Application title
st.title("Customer Churn Prediction")
st.write("Input the customer's data too predict churn or not ")

# Input from user
credit_score = st.number_input("Credit Score", min_value=300, max_value=900, value=600)
geography = st.selectbox("Geography", ["France", "Spain", "Germany"])
gender = st.selectbox("Gender", ["Female", "Male"])
age = st.slider("Age", min_value=18, max_value=100, value=35)
tenure = st.slider("Tenure (lama menjadi pelanggan)", min_value=0, max_value=10, value=3)
balance = st.number_input("Balance", min_value=0.0, value=50000.0)
num_of_products = st.selectbox("Jumlah Produk", [1, 2, 3, 4])
has_cr_card = st.selectbox("Memiliki Credit Card?", ["Ya", "Tidak"])
is_active_member = st.selectbox("Status Keaktifan Member", ["Aktif", "Tidak Aktif"])
estimated_salary = st.number_input("Estimated Salary", min_value=0.0, value=100000.0)

# Encode the categorical features
geography_encoded = {'France': 0, 'Germany': 1, 'Spain': 2}
gender_encoded = {'Female': 0, 'Male': 1}
has_cr_card_encoded = 1 if has_cr_card == "Ya" else 0
is_active_member_encoded = 1 if is_active_member == "Aktif" else 0


# Make an Array Input
input_data = pd.DataFrame([{
    'CreditScore': credit_score,
    'Geography': geography_encoded[geography],
    'Gender': gender_encoded[gender],
    'Age': age,
    'Tenure': tenure,
    'Balance': balance,
    'NumOfProducts': num_of_products,
    'HasCrCard': has_cr_card_encoded,
    'IsActiveMember': is_active_member_encoded,
    'EstimatedSalary': estimated_salary
}])

# Scale the numerical features
numeric_columns = ['CreditScore', 'Age', 'Tenure', 'Balance', 'NumOfProducts', 
                   'HasCrCard', 'IsActiveMember', 'EstimatedSalary']

input_data[numeric_columns] = scaler.transform(input_data[numeric_columns])


# Prediction
if st.button("Prediksi"):
    prediction = model.predict(input_data)
    result = "CHURN (Akan Keluar)" if prediction[0] == 1 else "TIDAK CHURN"
    st.success(f"Hasil Prediksi: {result}")