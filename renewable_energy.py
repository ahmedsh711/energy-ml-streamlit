
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline

st.set_page_config(page_title="Energy Production Predictor", page_icon="⚡")

st.title("⚡ Energy Production Predictor")
st.write("Predict renewable energy production based on your project details")

@st.cache_resource
def load_model():
    try:
        model = joblib.load('model_compressed.pkl')
        return model
    except:
        st.error("Model file not found. Please make sure 'model_compressed.pkl' is in the same directory.")
        return None

model = load_model()

if model is not None:
    st.header("Enter Project Details")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Technical Specs")
        installed_capacity = st.number_input("Installed Capacity (MW)", min_value=1.0, value=100.0)
        energy_consumption = st.number_input("Energy Consumption (MWh)", min_value=10.0, value=1000.0)
        energy_storage = st.number_input("Energy Storage Capacity (MWh)", min_value=0.0, value=200.0)
        storage_efficiency = st.slider("Storage Efficiency (%)", 50.0, 98.0, 85.0)

        st.subheader("Financial Details")
        investment = st.number_input("Initial Investment (USD)", min_value=100000.0, value=10000000.0, step=100000.0)
        incentives = st.number_input("Financial Incentives (USD)", min_value=0.0, value=500000.0, step=10000.0)

    with col2:
        st.subheader("Environmental Impact")
        ghg_reduction = st.number_input("GHG Emission Reduction (tCO2e)", min_value=0.0, value=1000.0)
        air_pollution = st.slider("Air Pollution Reduction Index", 0.0, 10.0, 5.0)
        jobs_created = st.number_input("Jobs Created", min_value=0, value=50)

        st.subheader("Project Type")
        energy_type = st.selectbox("Renewable Energy Type", 
                                  ['Solar', 'Wind', 'Hydroelectric', 'Geothermal', 'Biomass', 'Tidal', 'Wave'])

        funding_source = st.selectbox("Funding Source", 
                                     ['Government', 'Private', 'Public-Private Partnership'])

        grid_integration = st.selectbox("Grid Integration Level", 
                                       ['Fully Integrated', 'Partially Integrated', 'Minimal Integration', 'Isolated Microgrid'])

    if st.button("🔮 Predict Energy Production", type="primary"):

        # Create input dataframe
        input_data = pd.DataFrame({
            'Installed_Capacity_MW': [installed_capacity],
            'Energy_Consumption_MWh': [energy_consumption],
            'Energy_Storage_Capacity_MWh': [energy_storage],
            'Storage_Efficiency_Percentage': [storage_efficiency],
            'Initial_Investment_USD': [investment],
            'Financial_Incentives_USD': [incentives],
            'GHG_Emission_Reduction_tCO2e': [ghg_reduction],
            'Air_Pollution_Reduction_Index': [air_pollution],
            'Jobs_Created': [jobs_created],
            'Type_of_Renewable_Energy': [energy_type],
            'Funding_Sources': [funding_source],
            'Grid_Integration_Level': [grid_integration]
        })

        # Add engineered features
        input_data['Storage_per_MW'] = input_data['Energy_Storage_Capacity_MWh'] / input_data['Installed_Capacity_MW']
        input_data['Jobs_per_MW'] = input_data['Jobs_Created'] / input_data['Installed_Capacity_MW']
        input_data['GHG_Reduction_per_MW'] = input_data['GHG_Emission_Reduction_tCO2e'] / input_data['Installed_Capacity_MW']
        input_data['Storage_per_Dollar'] = input_data['Energy_Storage_Capacity_MWh'] / input_data['Initial_Investment_USD']
        input_data['Incentive_Ratio'] = input_data['Financial_Incentives_USD'] / input_data['Initial_Investment_USD']
        input_data['Storage_to_Consumption_Ratio'] = input_data['Energy_Storage_Capacity_MWh'] / input_data['Energy_Consumption_MWh']

        try:
            prediction = model.predict(input_data)[0]

            st.success("✅ Prediction Complete!")

            col3, col4 = st.columns(2)

            with col3:
                st.metric("🎯 Predicted Energy Production", f"{prediction:,.0f} MWh/year")

            with col4:
                efficiency = prediction / installed_capacity
                st.metric("⚡ Production per MW", f"{efficiency:,.0f} MWh/MW/year")

            st.info(f"Your {energy_type.lower()} project is expected to produce **{prediction:,.0f} MWh** of clean energy per year!")

        except Exception as e:
            st.error(f"Error making prediction: {str(e)}")

else:
    st.warning("Please ensure the trained model file 'model_compressed.pkl' is available to make predictions.")
