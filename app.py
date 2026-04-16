import streamlit as st
import pandas as pd
from src.utils import load_object

model = load_object("artifacts/model.pkl")

st.title(" Car Price Prediction")

engine = st.number_input("Engine Size")
hp = st.number_input("Horsepower")
weight = st.number_input("Curb Weight")
mpg = st.number_input("Highway MPG")

if st.button("Predict"):
    data = pd.DataFrame([[engine, hp, weight, mpg]],
                        columns=["engine-size", "horsepower", "curb-weight", "highway-mpg"])

    pred = model.predict(data)
    st.success(f"Predicted Price: {pred[0]:.2f}")