import streamlit as st
import pandas as pd
import numpy as np
import pickle

# Load model
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

st.set_page_config(page_title="Salary Predictor", page_icon="💰")

st.title("💼 AI Salary Predictor")
st.markdown("Enter the employee details to predict estimated salary 💸")

# Dropdown options
education_levels = ['High School', 'Bachelor', 'Master', 'PhD']
locations = ['Urban', 'Suburban', 'Rural']
job_titles = ['Manager', 'Analyst', 'Director', 'Engineer', 'Consultant']
genders = ['Male', 'Female']

# User Inputs
education = st.selectbox("📘 Education Level", education_levels)
experience = st.number_input("⌛ Years of Experience", min_value=0, max_value=50, step=1)
location = st.selectbox("📍 Location", locations)
job_title = st.selectbox("🧑‍💼 Job Title", job_titles)
age = st.number_input("🎂 Age", min_value=18, max_value=70, step=1)
gender = st.radio("👤 Gender", genders)

# Encode like training
def encode_inputs(education, experience, location, job_title, age, gender):
    le_dict = {
        'Education': {'High School': 0, 'Bachelor': 1, 'Master': 2, 'PhD': 3},
        'Location': {'Urban': 2, 'Suburban': 1, 'Rural': 0},
        'Job_Title': {'Manager': 2, 'Analyst': 0, 'Director': 1, 'Engineer': 3, 'Consultant': 4},
        'Gender': {'Male': 1, 'Female': 0}
    }
    return np.array([[
        le_dict['Education'][education],
        experience,
        le_dict['Location'][location],
        le_dict['Job_Title'][job_title],
        age,
        le_dict['Gender'][gender]
    ]])

# Predict button
if st.button("🎯 Predict Salary"):
    input_data = encode_inputs(education, experience, location, job_title, age, gender)
    predicted_salary = model.predict(input_data)[0]
    st.success(f"💰 Estimated Salary: ₹ {predicted_salary:,.2f}")
