import streamlit as st
import joblib

# Load the trained model
model = joblib.load("house_price_model.pkl")

# Page Config
st.set_page_config(page_title="🏡 House Price Predictor", layout="centered")

st.title("🏡 House Price Predictor")

st.markdown(
    """
    Enter the property details below to estimate the house price.
    """
)

# Input form
with st.form("prediction_form"):
    col1, col2 = st.columns(2)

    with col1:
        bedrooms = st.number_input("Bedrooms", min_value=0, step=1)
        bathrooms = st.number_input("Bathrooms", min_value=0.0, step=0.25)
        living_area = st.number_input("Living Area (sq ft)", min_value=0.0)
        lot_area = st.number_input("Lot Area (sq ft)", min_value=0.0)
        floors = st.number_input("Floors", min_value=0.0, step=0.5)
        waterfront = st.selectbox("Waterfront (0/1)", [0, 1])
        condition = st.slider("Condition (1–5)", 1, 5, 3)
        grade = st.slider("Grade (1–13)", 1, 13, 7)

    with col2:
        area_excl_basement = st.number_input("Area excl. Basement", min_value=0.0)
        area_basement = st.number_input("Basement Area", min_value=0.0)
        built_year = st.number_input("Built Year", min_value=1800, max_value=2025, step=1)
        renov_year = st.number_input("Renovation Year", min_value=0, max_value=2025, step=1)
        living_area_renov = st.number_input("Living Area (Renov)", min_value=0.0)
        lot_area_renov = st.number_input("Lot Area (Renov)", min_value=0.0)
        schools_nearby = st.number_input("Schools Nearby", min_value=0, step=1)
        distance_airport = st.number_input("Distance to Airport (km)", min_value=0.0)

    submitted = st.form_submit_button("💰 Predict Price")

if submitted:
    try:
        inputs = [
            int(bedrooms), float(bathrooms), float(living_area), float(lot_area),
            float(floors), int(waterfront), int(condition), int(grade),
            float(area_excl_basement), float(area_basement), int(built_year),
            int(renov_year), float(living_area_renov), float(lot_area_renov),
            int(schools_nearby), float(distance_airport)
        ]
        price = model.predict([inputs])[0]
        st.success(f"🏷 Estimated Price: ₹{price:,.2f}")
    except Exception as e:
        st.error(f"Prediction Error: {e}")
