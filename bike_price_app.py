import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Page setup
# -----------------------------
st.set_page_config(page_title="🏍️ Used Bike Price Predictor", page_icon="🏍️")

st.title("🏍️ Used Bike Price Prediction App")
st.caption("Estimate the resale value of your motorcycle 💰")

# -----------------------------
# Load trained model
# -----------------------------
try:
    model = joblib.load("bike_price_model.pkl")
except FileNotFoundError:
    st.error("❌ Model file not found! Please make sure 'bike_price_model.pkl' is in the same folder.")
    st.stop()

# -----------------------------
# User Inputs
# -----------------------------
with st.form("bike_form"):
    col1, col2 = st.columns(2)

    with col1:
        brand = st.selectbox("Brand", [
            'TVS', 'Royal Enfield', 'Yamaha', 'Honda', 'Hero', 'Bajaj', 'Suzuki', 'KTM', 'BMW'
        ])
        owner = st.selectbox("Owner Type", [
            "First Owner", "Second Owner", "Third Owner", "Fourth Owner Or More"
        ])
        age = st.number_input("Age of Bike (in years)", min_value=0, max_value=30, value=3)

    with col2:
        # ✅ FIX: Make sure kilometers field is smooth & responsive
        kms_driven = st.number_input("Kilometers Driven (in km)", min_value=0, max_value=300000, step=500, value=20000)
        power = st.number_input("Power (in bhp)", min_value=1.0, max_value=200.0, step=0.5, value=15.0)
        engine = st.number_input("Engine Capacity (in cc)", min_value=50, max_value=2000, step=10, value=150)

    submitted = st.form_submit_button("Predict Price 💰")

# -----------------------------
# Validation checks
# -----------------------------
def validate_inputs(age, kms_driven, power, engine):
    warnings = []
    if age > 25:
        warnings.append("⚠️ Age seems too high! Please check the bike's age.")
    if kms_driven > 200000:
        warnings.append("⚠️ That's a lot of kilometers! Check if the number is correct.")
    if power > 100:
        warnings.append("⚠️ Power seems unusually high for a bike — please verify.")
    if engine > 1000:
        warnings.append("⚠️ Engine capacity above 1000cc is rare for regular bikes.")
    if age == 0 and kms_driven > 5000:
        warnings.append("⚠️ A new bike usually doesn’t have this many kilometers driven.")
    return warnings

# -----------------------------
# Mapping
# -----------------------------
owner_map = {
    "First Owner": 1,
    "Second Owner": 2,
    "Third Owner": 3,
    "Fourth Owner Or More": 4
}

brand_map = {
    'TVS': 0,
    'Royal Enfield': 1,
    'Yamaha': 2,
    'Honda': 3,
    'Hero': 4,
    'Bajaj': 5,
    'Suzuki': 6,
    'KTM': 7,
    'BMW': 8
}

# -----------------------------
# Prediction Logic
# -----------------------------
if submitted:
    warnings = validate_inputs(age, kms_driven, power, engine)

    # ✅ FIX: Make sure kilometer value is integer and not float
    kms_driven = int(kms_driven)

    # Prepare dataframe
    data = pd.DataFrame({
        'brand': [brand_map.get(brand, 0)],
        'owner': [owner_map.get(owner, 1)],
        'age': [age],
        'kms_driven': [kms_driven],
        'power': [power],
        'engine': [engine]
    })

    # Match columns with model
    if hasattr(model, "feature_names_in_"):
        expected_cols = list(model.feature_names_in_)
        for col in expected_cols:
            if col not in data.columns:
                data[col] = 0
        data = data[expected_cols]

    # Display warnings
    if warnings:
        st.warning("⚠️ Some values seem unusual:")
        for w in warnings:
            st.write("- " + w)

    # Predict
    try:
        price = model.predict(data)[0]
        price = max(price, 0)
        st.success(f"🏍️ Estimated Resale Price: ₹{price:,.2f}")
    except Exception as e:
        st.error(f"⚠️ Prediction error: {e}")
