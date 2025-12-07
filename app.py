import streamlit as st
import pandas as pd
import joblib

model = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")

st.title(" Customer Segmentation RFM Clustering")

st.write("Enter RFM values and get the customer segment")

# user inputs
r = st.number_input("Recency (days)", min_value=0)
f = st.number_input("Frequency", min_value=0)
m = st.number_input("Monetary Value", min_value=0)

if st.button("Predict"):
    df = pd.DataFrame([[r, f, m]], columns=["Recency","Frequency","Monetary"])
    scaled = scaler.transform(df)
    cluster = model.predict(scaled)[0]

    st.success(f"Customer falls into Cluster: {cluster}")

    mapping = {
        0: " VIP / High Value",
        1: " Frequent Buyers",
        2: " At-Risk Customers",
        3: " New / Occasional Customers"
    }

    st.write(mapping.get(cluster, "Unknown Segment"))
