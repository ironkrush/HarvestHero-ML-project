import pandas as pd
import numpy as np
import streamlit as st
import pickle as pk

model = pk.load(open("Crop_recommendation.pkl", "rb"))

data = pd.read_csv('Crop_recommendation.csv')

st.header('HarvestHero')

n = st.number_input("Enter Nitrogen content value:")
p = st.number_input("Enter Phosphorous content value:")
k = st.number_input("Enter Potassium content value:")
temp = st.number_input("Enter temperature in degree Celsius:")
hum = st.number_input("Enter relative humidity in %:")
ph = st.number_input("Enter PH value of the soil:")
rain = st.number_input("Enter rainfall value in mm:")

input = np.array([[n,p,k,temp,hum,ph,rain]])

output = model.predict(input)

if st.button('Predict'):
            st.markdown(output)