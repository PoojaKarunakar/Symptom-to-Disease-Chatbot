# ✅ 1. Import libraries
import streamlit as st
import pandas as pd
import joblib

# ✅ 2. Load saved model files
model = joblib.load("disease_model.pkl")
mlb = joblib.load("mlb.pkl")
le = joblib.load("label_encoder.pkl")

# ✅ 3. Disease info (you can expand this)
disease_info = {
    "AIDS": {
        "description": "Weakens immune system",
        "precautions": ["Avoid unsafe contact", "Regular testing"]
    },
    "Flu": {
        "description": "Viral infection",
        "precautions": ["Rest", "Drink fluids"]
    },
    "Hepatitis C": {
        "description": "Liver infection",
        "precautions": ["Avoid alcohol", "Consult doctor"]
    }
}

# ✅ 4. Prediction function (Top 3 results)
def predict_disease_full(symptoms):
    input_data = [0] * len(mlb.classes_)

    for symptom in symptoms:
        if symptom in mlb.classes_:
            index = list(mlb.classes_).index(symptom)
            input_data[index] = 1

    input_df = pd.DataFrame([input_data], columns=mlb.classes_)

    probs = model.predict_proba(input_df)[0]
    top3 = probs.argsort()[-3:][::-1]

    diseases = le.inverse_transform(top3)
    confidence = probs[top3]

    return list(zip(diseases, confidence))

# ✅ 5. Streamlit UI
st.title("🤖 Disease Prediction Chatbot")

user_input = st.text_input("Enter symptoms (comma separated):")

if st.button("Predict"):
    symptoms = [s.strip().lower().replace(" ", "_") for s in user_input.split(",")]

    results = predict_disease_full(symptoms)
    
    st.subheader("Top Predictions:")

    for disease, conf in results:
        st.write(f"**{disease} ({conf*100:.2f}%)**")

        if disease in disease_info:
            st.write("Description:", disease_info[disease]["description"])
            st.write("Precautions:", ", ".join(disease_info[disease]["precautions"]))

        st.write("---")