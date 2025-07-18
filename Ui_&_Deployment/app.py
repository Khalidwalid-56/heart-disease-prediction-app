# import streamlit as st
# import numpy as np
# import pickle

# # Load the trained model
# with open("models/final_model.pkl", "rb") as f:
#     model = pickle.load(f)

# st.title("Heart Disease Prediction")
# st.markdown("Provide the patient's details to predict the risk of heart disease.")

# # Input fields
# age = st.number_input("Age (years)", min_value=0, max_value=120, value=30)
# sex = st.selectbox("Sex", ["Male", "Female"])
# cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
# trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=250, value=120)
# chol = st.number_input("Cholesterol (mg/dl)", min_value=0, max_value=600, value=200)
# fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl?", ["Yes", "No"])
# restecg = st.selectbox("Resting ECG", ["Normal", "ST-T wave abnormality", "Left Ventricular Hypertrophy"])
# thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)
# exang = st.selectbox("Exercise-Induced Angina", ["Yes", "No"])
# oldpeak = st.number_input("Oldpeak (ST depression)", min_value=0.0, max_value=10.0, step=0.1, value=1.0)
# slope = st.selectbox("ST Slope", ["Upsloping", "Flat", "Downsloping"])
# ca = st.slider("Number of Major Vessels Colored by Fluoroscopy", min_value=0, max_value=3, value=0)
# thal = st.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect"])

# # Mapping categorical values to numeric
# sex_map = {"Male": 1, "Female": 0}
# cp_map = {
#     "Typical Angina": 0,
#     "Atypical Angina": 1,
#     "Non-Anginal Pain": 2,
#     "Asymptomatic": 3
# }
# fbs_map = {"Yes": 1, "No": 0}
# restecg_map = {
#     "Normal": 0,
#     "ST-T wave abnormality": 1,
#     "Left Ventricular Hypertrophy": 2
# }
# exang_map = {"Yes": 1, "No": 0}
# slope_map = {
#     "Upsloping": 0,
#     "Flat": 1,
#     "Downsloping": 2
# }
# thal_map = {
#     "Normal": 1,
#     "Fixed Defect": 2,
#     "Reversible Defect": 3
# }

# # Prepare input array
# input_data = np.array([[
#     age,
#     sex_map[sex],
#     cp_map[cp],
#     trestbps,
#     chol,
#     fbs_map[fbs],
#     restecg_map[restecg],
#     thalach,
#     exang_map[exang],
#     oldpeak,
#     slope_map[slope],
#     ca,
#     thal_map[thal]
# ]])

# # Predict
# if st.button("Predict"):
#     prediction = model.predict(input_data)[0]
#     if prediction == 1:
#         st.error("⚠️ High risk of heart disease detected.")
#     else:
#         st.success("✅ No sign of heart disease detected.")

import streamlit as st
import numpy as np
import pickle
import plotly.graph_objects as go

# Load trained model
with open(r"C:\Users\DELL\Downloads\‏‏Heart_Disease_Project - 2\Models\final_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Heart Disease Prediction")
st.markdown("Provide the patient's details to predict the risk of heart disease.")

# Inputs
age = st.number_input("Age (years)", min_value=0, max_value=120, value=30)
sex = st.selectbox("Sex", ["Male", "Female"])
cp = st.selectbox("Chest Pain Type", ["Typical Angina", "Atypical Angina", "Non-Anginal Pain", "Asymptomatic"])
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=0, max_value=250, value=120)
chol = st.number_input("Cholesterol (mg/dl)", min_value=0, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl?", ["Yes", "No"])
restecg = st.selectbox("Resting ECG", ["Normal", "ST-T wave abnormality", "Left Ventricular Hypertrophy"])
thalach = st.number_input("Maximum Heart Rate Achieved", min_value=60, max_value=220, value=150)
exang = st.selectbox("Exercise-Induced Angina", ["Yes", "No"])
oldpeak = st.number_input("Oldpeak (ST depression)", min_value=0.0, max_value=10.0, step=0.1, value=1.0)
slope = st.selectbox("ST Slope", ["Upsloping", "Flat", "Downsloping"])
ca = st.slider("Number of Major Vessels Colored by Fluoroscopy", min_value=0, max_value=3, value=0)
thal = st.selectbox("Thalassemia", ["Normal", "Fixed Defect", "Reversible Defect"])

# Mappings
sex_map = {"Male": 1, "Female": 0}
cp_map = {"Typical Angina": 0, "Atypical Angina": 1, "Non-Anginal Pain": 2, "Asymptomatic": 3}
fbs_map = {"Yes": 1, "No": 0}
restecg_map = {"Normal": 0, "ST-T wave abnormality": 1, "Left Ventricular Hypertrophy": 2}
exang_map = {"Yes": 1, "No": 0}
slope_map = {"Upsloping": 0, "Flat": 1, "Downsloping": 2}
thal_map = {"Normal": 1, "Fixed Defect": 2, "Reversible Defect": 3}

# Prepare input
input_data = np.array([[
    age,
    sex_map[sex],
    cp_map[cp],
    trestbps,
    chol,
    fbs_map[fbs],
    restecg_map[restecg],
    thalach,
    exang_map[exang],
    oldpeak,
    slope_map[slope],
    ca,
    thal_map[thal]
]])

# Predict
if st.button("Predict"):
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1] * 100  # Probability of heart disease

    # Show result
    if prediction == 1:
        st.error(f"⚠️ High risk of heart disease detected.")
    else:
        st.success(f"✅ No sign of heart disease detected.")

    # Plot gauge chart
    fig = go.Figure(go.Indicator(
        mode="gauge+number+delta",
        value=probability,
        domain={'x': [0, 1], 'y': [0, 1]},
        title={'text': "Heart Disease Risk (%)", 'font': {'size': 24}},
        delta={'reference': 50, 'increasing': {'color': "red"}, 'decreasing': {'color': "green"}},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "darkblue"},
            'bar': {'color': "darkred" if probability > 50 else "green"},
            'steps': [
                {'range': [0, 50], 'color': 'lightgreen'},
                {'range': [50, 100], 'color': 'lightcoral'}
            ],
            'threshold': {
                'line': {'color': "red", 'width': 4},
                'thickness': 0.75,
                'value': probability
            }
        }
    ))
    st.plotly_chart(fig)
