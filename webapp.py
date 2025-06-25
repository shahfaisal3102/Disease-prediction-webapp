import streamlit as st
from streamlit_option_menu import option_menu
import pickle
import os
import numpy as np
import pandas as pd

# Loading the model

Diabetes_model = pickle.load(open('D:\Disease prediction\Saved Models\Diabetes_model.sav', 'rb'))
Heart_model = pickle.load(open('D:\Disease prediction\Saved Models\Heart_model.sav', 'rb'))
Ckd_model = pickle.load(open('D:\Disease prediction\Saved Models\CKD_model.sav', 'rb'))
scalar = pickle.load(open('D:\Disease prediction\Saved Models\Ckd_scalar.sav', 'rb'))

# Set page configuration
st.set_page_config(page_title="Health Assistant",
                   page_icon="🩺",layout="centered")

# st.title("Health Assistant")
# st.image("D:\Disease prediction\icons\kidney.png", width=80)  # Optional icon image
st.markdown("""
    <h1 style='text-align: center; color: white;'>
        🩺 Health Assistant
    </h1>
    <hr>
""", unsafe_allow_html=True)

# getting the working directory of the main.py

os.system('pip install streamlit-option-menu')
working_dir = os.path.dirname(os.path.abspath(__file__))

# Sidebar for navigation
with st.sidebar:
    selected = option_menu('Multiple Disease Prediction System Menu',
                           ['Diabetes', 'Heart Disease', 'Kidney Disease'],
                           menu_icon='hospital-fill',
                           icons=['activity', 'heart', 'person'],
                           default_index=0)

# Input fields

if selected == "Diabetes":
    
    # Page Title
    st.subheader("Diabetes Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        preg = st.number_input("No. of Pregnancies", 0, 20)
    
    with col2:
        glucose = st.number_input("Glucose Level", 0, 200)
    
    with col3:
        bp = st.number_input("Blood Pressure value", 0, 140)
    
    with col1:
        skin = st.number_input("Skin Thickness Value", 0, 100)
    
    with col2:
        insulin = st.number_input("Insulin Level", 0, 900)
    
    with col3:
        bmi = st.number_input("BMI value", 0.0, 70.0)
    
    with col1:
        dpf = st.number_input("Diabetes Pedigree Function value", 0.0, 3.0)
    
    with col2:
        age = st.number_input("Age of a person", 10, 100)

# Prediction 

    if st.button("Predict",key="predict_diabetes"):
        input_data = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
        prediction = Diabetes_model.predict(input_data)
        st.success("Positive for Diabetes" if prediction[0] == 1 else "Negative for Diabetes")


# For Heart disease 
if selected == "Heart Disease":

    st.header("Heart Disease prediction")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input("Age of a person", min_value=1, max_value=120)
        
    with col2:
        sex = st.selectbox("Select sex", ["M", "F"])

    with col3:
        cp_map = {
                  "TA: Typical Angina": "TA",
                  "ATA: Atypical Angina": "ATA",
                  "NAP: Non-Anginal Pain": "NAP",
                  "ASY: Asymptomatic": "ASY"
                  }
    
        ChestPainType_display = st.selectbox("Select Chest Pain type", list(cp_map.keys()))
    
        ChestPainType = cp_map[ChestPainType_display]  # Now a clean short string

    with col1:
        RestingBP = st.number_input("Resting Blood Pressure mm Hg", min_value=0, max_value=300)
    
    with col2:
        Cholesterol = st.number_input("Serum cholesterol [mm/dl]", min_value=0, max_value=1000)
    
    with col3:
        FastingBS_raw = st.selectbox("Fasting Blood Sugar", ["1: if FBS > 120 mg/dl", "0: otherwise"])
        FastingBS = int(FastingBS_raw.split(":")[0])
    
    with col1:
        RestingECG = st.selectbox("Resting ECG", ["Normal", "ST", "LVH"])
    
    with col2:
        MaxHR = st.number_input("Maximum Heart Rate", min_value=60, max_value=220)
    
    with col3:
        ExerciseAngina = st.selectbox("Exercise Induced Angina", ["Y", "N"])
    
    with col1:
        Oldpeak = st.number_input("Oldpeak", min_value=0.0, max_value=10.0, step=0.1)
    
    with col2:
        ST_Slope = st.selectbox("ST Slope", ["Up", "Flat", "Down"])

    # Prediction
    if st.button("Predict", key="predict_heart"):
        input_data = [
            float(age),
            1 if sex == "M" else 0,
            ["TA", "ATA", "NAP", "ASY"].index(ChestPainType),
            float(RestingBP),
            float(Cholesterol),
            FastingBS,
            ["Normal", "ST", "LVH"].index(RestingECG),
            float(MaxHR),
            1 if ExerciseAngina == "Y" else 0,
            float(Oldpeak),
            ["Up", "Flat", "Down"].index(ST_Slope)
        ]
    
        prediction = Heart_model.predict([input_data])
        st.success("Heart Disease: YES" if prediction[0] == 1 else "Heart Disease: NO")
    
            

# Chronic Kidney Disease 

if selected == "Kidney Disease":

    st.header("Kidney Disease Prediction")

    col1, col2, col3 = st.columns(3)

    with col1:
        serum_creatinine = st.number_input("Serum Creatinine",0.000000, 5.000000)

    with col2:
        gfr = st.number_input("GFR", 0.000000,150.000000)
    
    with col3:
        bun = st.number_input("Blood Urea Nitrogen (BUN)",0.000000, 150.000000)
    
    with col1:
        serum_calcium = st.number_input("Serum Calcium", 0.000000, 20.000000)
    
    with col2:
        ana = st.selectbox("ANA (Antinuclear Antibody)", [0, 1])
    
    with col3:
        c3_c4 = st.number_input("C3 C4", 0.000000,200.000000)

    with col1:
        hematuria = st.selectbox("Hematuria", [0, 1])
    
    with col2:
        oxalate_levels = st.number_input("Oxalate Levels",0.000000, 5.000000)
    
    with col3:
        urine_ph = st.number_input("Urine pH",0.000000 , 8.000000)
    
    with col1:
        blood_pressure = st.number_input("Blood Pressure", 0.000000, 180.000000)
    
    with col2:
        physical_activity = st.selectbox("Physical Activity", ['daily', 'weekly', 'rarely'])
    
    with col3:
        diet = st.selectbox("Diet", ['high protein', 'low salt', 'balanced'])
    
    with col1:
        water_intake = st.number_input("Water Intake (liters per day)", 0.000000, 4.000000)
    
    with col2:
        smoking = st.selectbox("Smoking", ['yes', 'no'])
    
    with col3:
        alcohol = st.selectbox("Alcohol", ['daily', 'occasionally', 'never'])
    
    with col1:
        painkiller_usage = st.selectbox("Painkiller Usage", ['yes', 'no'])
    
    with col2:
        family_history = st.selectbox("Family History of CKD", ['yes', 'no'])
    
    with col3:
        weight_changes = st.selectbox("Weight Changes", ['stable', 'gain', 'loss'])
    
    with col1:
        stress_level = st.selectbox("Stress Level", ['low', 'medium', 'high'])

    if st.button("Predict", key = "predict kidney"):

        sample_input = [serum_creatinine, gfr, bun, serum_calcium, [0,1].index(ana),
                        c3_c4, [0,1].index(hematuria), oxalate_levels, urine_ph, blood_pressure,["daily","weekly","rarely"].index(physical_activity),
                        ['high protein', 'low salt', 'balanced'].index(diet), water_intake, ['yes', 'no'].index(smoking), ['daily', 'occasionally', 'never'].index(alcohol),
                        ['yes', 'no'].index(painkiller_usage), ['yes', 'no'].index(family_history), ['stable', 'gain', 'loss'].index(weight_changes),
                        ['low', 'medium', 'high'].index(stress_level)]
        
        sample_input = np.array(sample_input).reshape(1, -1)
        scaled_input = scalar.transform(sample_input)
        prediction = Ckd_model.predict(scaled_input)
        st.success(f"CKD Prediction: YES" if prediction[0][0] == 0 else "CKD Prediction: NO" )
        st.info(f"Predicted Stage: {prediction[0][1]}")

