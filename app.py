import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load('klasifikasi_obesitas.pkl')

st.title('Obesity Level Classification')

# Input pengguna
height = st.number_input('Height (in meters)', min_value=0.5, max_value=2.5, value=1.75)
weight = st.number_input('Weight (in kg)', min_value=20, max_value=200, value=70)
gender = st.selectbox('Gender', ('Female', 'Male'))

# Konversi gender ke bentuk numerik
gender_num = 0 if gender == 'Female' else 1

# Prediksi
if st.button('Predict'):
    st.write("Button clicked.")
    input_data = np.array([[height, weight, gender_num]])
    prediction = clf.predict(input_data)
    st.write("Prediction made.")

# Tampilkan hasil
obesity_level = ['Extremely Weak','weak','Normal', 'Overweight', 'Obese','Extremely Obese']
st.write(f'The predicted obesity level is: {obesity_level[prediction[0]]}')
