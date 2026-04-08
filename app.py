import streamlit as st
import pickle
import numpy as np

model = pickle.load(open(r"data\models\model.pkl", "rb"))

st.title("House Price Predictor")

bed = st.number_input("Bedrooms")
bath = st.number_input("Bathrooms")
area = st.number_input("Area")

if st.button("Predict"):
    result = model.predict([[bed, bath, area]])
    st.success(f"Price: ₹ {int(result[0])}")