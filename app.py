import streamlit as st
import pandas as pd
import subprocess
import os



def run_prediction(input_file):
    """Runs the BandGapPredictor model and returns output."""
    try:
        command = f"python predict.py --input {input_file}"
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return str(e)

st.title("BandGap Predictor GUI")

st.markdown("Upload your input CSV file to predict band gaps.")

uploaded_file = st.file_uploader("Choose a CSV file", type=["csv"])

if uploaded_file is not None:
    file_path = os.path.join("input.csv")
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    
    st.success("File uploaded successfully.")
    
    if st.button("Run Prediction"):
        st.text("Running model...")
        output = run_prediction(file_path)
        st.text_area("Prediction Output", output, height=300)
