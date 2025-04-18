import streamlit as st
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Load trained model and encoders
model = joblib.load("downtime_model.pkl")
encoders = joblib.load("label_encoders.pkl")

st.title("🛠️ Downtime Prediction for Manufacturing Machines")

# Input fields
machine = st.selectbox("Select Machine", encoders['Machine_ID'].classes_)
operator = st.selectbox("Select Operator", encoders['Operator_ID'].classes_)
product = st.selectbox("Select Product Type", encoders['Product_Type'].classes_)
shift = st.selectbox("Select Shift", encoders['Shift'].classes_)
units = st.number_input("Units Produced in this hour", min_value=0, value=120)
defects = st.number_input("Number of Defects", min_value=0, value=2)

# Convert inputs to model format
input_data = pd.DataFrame({
    'Machine_ID': [encoders['Machine_ID'].transform([machine])[0]],
    'Operator_ID': [encoders['Operator_ID'].transform([operator])[0]],
    'Product_Type': [encoders['Product_Type'].transform([product])[0]],
    'Units_Produced': [units],
    'Defects': [defects],
    'Shift': [encoders['Shift'].transform([shift])[0]]
})

# Predict
if st.button("Predict Downtime Risk"):
    result = model.predict(input_data)[0]
    prob = model.predict_proba(input_data)[0][1]
    if result == 1:
        st.error(f"⚠️ High risk of downtime! ({prob*100:.2f}% confidence)")
    else:
        st.success(f"✅ No downtime expected. ({(1 - prob)*100:.2f}% confidence)")
