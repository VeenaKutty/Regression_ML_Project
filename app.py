import streamlit as st
import pandas as pd
from src.utils import load_object
import numpy as np

model = load_object("artifacts/model.pkl")
features = load_object("artifacts/features.pkl")

st.title("Car Price Prediction")

# Take only few inputs (important ones)
engine = st.number_input("Engine Size")
hp = st.number_input("Horsepower")
weight = st.number_input("Curb Weight")
mpg = st.number_input("Highway MPG")

if st.button("Predict"):

    # Create full input with all features
    input_dict = {feature: 0 for feature in features}

    # Fill only known ones
    input_dict["engine-size"] = engine
    input_dict["horsepower"] = hp
    input_dict["curb-weight"] = weight
    input_dict["highway-mpg"] = mpg

    input_df = pd.DataFrame([input_dict])

    pred = model.predict(input_df)

    st.success(f"Predicted Price: {pred[0]:.2f}")