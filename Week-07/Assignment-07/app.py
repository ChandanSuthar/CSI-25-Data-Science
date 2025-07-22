import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

model = joblib.load("placement_model.joblib")
le_internship = joblib.load("le_internship.joblib")
le_placement = joblib.load("le_placement.joblib")

st.set_page_config(
    page_title="Campus Placement Predictor",
    page_icon=None,
    layout="wide"
)

st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #1f1c2c, #928dab);
        color: white;
        font-family: 'Arial';
    }
    div.stButton > button {
        background-color: #ff4b1f;
        color: white;
        border-radius: 10px;
        padding: 10px 20px;
        border: none;
    }
    div.stButton > button:hover {
        background-color: #ff9068;
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color: white;'>🎓 Campus Placement Prediction Portal</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center;'>Experience the future of student placement insights with a tap.</p>", unsafe_allow_html=True)
st.write("---")

st.subheader("📄 Fill in Student Details")

with st.form("placement_form"):
    iq = st.slider("IQ Score", 70, 160, 100)
    prev_sem = st.slider("Previous Semester Result", 0.0, 10.0, 6.0)
    cgpa = st.slider("CGPA", 0.0, 10.0, 6.5)
    academic_performance = st.selectbox("Academic Performance Score (Internal Metric)", list(range(1, 11)))
    internship = st.radio("Internship Experience", ["Yes", "No"])
    extra_curricular = st.slider("Extra Curricular Score", 0, 10, 5)
    communication_skills = st.slider("Communication Skills", 0, 10, 5)
    projects_done = st.number_input("Number of Projects Completed", 0, 20, 1)

    submit = st.form_submit_button("🔍 Predict Placement")

if submit:
    internship_encoded = le_internship.transform([internship])[0]
    input_data = np.array([[iq, prev_sem, cgpa, academic_performance, internship_encoded,
                            extra_curricular, communication_skills, projects_done]])
    
    prediction = model.predict(input_data)[0]
    prediction_label = le_placement.inverse_transform([prediction])[0]
    pred_proba = model.predict_proba(input_data)[0]

    st.write("---")
    st.subheader("📢 Prediction Result:")
    st.success(f"**Placement Chance: {prediction_label}**")

    fig, ax = plt.subplots()
    labels = le_placement.inverse_transform([0, 1])
    ax.pie(pred_proba, labels=labels, autopct='%1.1f%%', startangle=90, colors=['#ff9999','#66b3ff'])
    ax.axis('equal')
    st.pyplot(fig)

    st.write("---")
    st.subheader("📊 Feature Summary")
    st.json({
        "IQ": iq,
        "Prev Semester": prev_sem,
        "CGPA": cgpa,
        "Academic Performance": academic_performance,
        "Internship": internship,
        "Extra Curricular": extra_curricular,
        "Communication": communication_skills,
        "Projects": projects_done
    })

st.markdown("<br><hr><center>Created for Celebal Summer Internship</center>", unsafe_allow_html=True)
