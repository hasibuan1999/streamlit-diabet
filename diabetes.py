import streamlit as st
import pandas as pd
import numpy as np
import pickle

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))
st.title('Prediksi Terkena Diabetes')

Pregnancies = st.text_input('Kehamilan')
Glucose = st.text_input('Kadar Glukosa Dalam Darah')
BloodPressure = st.text_input('Ukuran Tekanan Darah')
SkinThickness = st.text_input('Ketebalan Kulit')
Insulin = st.text_input('Kadar Insulin Dalam Darah')
BMI = st.text_input('Indeks Masa Tubuh')
DiabetesPedigreeFunction = st.text_input('Presentase Diabetes')
Age = st.text_input('Inputkan Usia')

diab_diagnosis = ''

if st.button('Prediksi Ibu Hamil Terkena Diabetes  adalah'):
    diab_prediction = diabetes_model.predict([[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age,]])
    if(diab_prediction[0] == 1):
        diab_diagnosis = 'Pasien Terkena Diabetes'
    else :
        diab_diagnosis = "Pasien Tidak Terkena Diabetes"
    st.success(diab_diagnosis)
