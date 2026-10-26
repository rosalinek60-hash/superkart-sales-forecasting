
import streamlit as st
import requests

st.title("SuperKart Sales Prediction")
st.write("Enter product and store details to predict sales.")

# Input fields
Product_Weight = st.number_input(
    "Product Weight", min_value=0.0, value=12.66
)

Product_Sugar_Content = st.selectbox(
    "Product Sugar Content",
    ["Low Sugar", "Regular", "No Sugar"]
)

Product_Allocated_Area = st.number_input(
    "Allocated Area Ratio", min_value=0.0, value=0.027
)

Product_MRP = st.number_input(
    "Product MRP", min_value=0.0, value=117.08
)

Store_Size = st.selectbox(
    "Store Size",
    ["Small", "Medium", "High"]
)

Store_Location_City_Type = st.selectbox(
    "City Tier",
    ["Tier 1", "Tier 2", "Tier 3"]
)

Store_Type = st.selectbox(
    "Store Type",
    [
        "Departmental Store",
        "Supermarket Type1",
        "Supermarket Type2",
        "Food Mart"
    ]
)

Product_Id_char = st.text_input(
    "Product ID Prefix", "FD"
)

Store_Age_Years = st.number_input(
    "Store Age (Years)", min_value=0, value=16
)

Product_Type_Category = st.selectbox(
    "Product Type Category",
    ["Perishables", "Non Perishables"]
)

# Backend API address inside the Docker network
api_url = "http://superkart-backend:7860/v1/predict"

if st.button("Predict Sales"):

    payload = {
        "Product_Weight": Product_Weight,
        "Product_Sugar_Content": Product_Sugar_Content,
        "Product_Allocated_Area": Product_Allocated_Area,
        "Product_MRP": Product_MRP,
        "Store_Size": Store_Size,
        "Store_Location_City_Type": Store_Location_City_Type,
        "Store_Type": Store_Type,
        "Product_Id_char": Product_Id_char,
        "Store_Age_Years": Store_Age_Years,
        "Product_Type_Category": Product_Type_Category
    }

    try:
        response = requests.post(
            api_url,
            json=payload,
            timeout=30
        )

        if response.status_code == 200:
            predicted_sales = response.json()["predicted_sales"]
            st.success(
                f"Predicted Sales: {predicted_sales:.2f}"
            )
        else:
            st.error(
                f"API Error: {response.status_code}"
            )

    except requests.exceptions.RequestException as error:
        st.error(f"Unable to connect to the prediction API: {error}")
