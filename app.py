import streamlit as st
import joblib
import numpy as np
model = joblib.load("model.pkl")
st.title("House Price Prediction")
st.divider()
st.write("this ml app helps you predict the cost of house you want to purchase according different parameterw")

st.divider()
bedrooms= st.number_input("Number of bedrooms", min_value = 0,value= 0)
bathrooms =st.number_input("Number of bathrooms", min_value = 0,value =0)
living_area=st.number_input("size of living area", min_value = 0, value =2000)
condition = st.number_input("house was built how many years ago", min_value = 0,value = 3)
numberofschools = st.number_input("Numbers of schools nearby", min_value = 0,value = 3)

st.divider()

x =[[bedrooms, bathrooms,living_area,condition,numberofschools]]
predictbutton = st.button("Predict")

if predictbutton:
    st.balloons()
    x_array =np.array(x)
    prediction = model.predict(x_array)
    st.write(f"The predicted price is {prediction}")
else : st.write("click the predict button")

# 'number of bedrooms', 'number of bathrooms', 'living area',
    #    'condition of the house', 'Number of schools nearby'