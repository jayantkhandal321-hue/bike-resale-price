import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# --- Sample dataset ---
data = {
    'brand': [0, 1, 2, 3, 4, 5, 6, 7, 8],
    'owner': [1, 2, 1, 3, 1, 2, 1, 3, 1],
    'age': [1, 3, 5, 2, 4, 6, 3, 1, 5],
    'kms_driven': [10000, 25000, 40000, 15000, 30000, 50000, 20000, 12000, 35000],
    'power': [15, 20, 35, 25, 30, 40, 22, 18, 28],
    'engine': [150, 350, 500, 200, 250, 400, 180, 160, 300],
    'price': [60000, 85000, 130000, 75000, 90000, 140000, 82000, 70000, 95000]
}

# --- Create DataFrame ---
df = pd.DataFrame(data)

X = df[['brand', 'owner', 'age', 'kms_driven', 'power', 'engine']]
y = df['price']

# --- Train simple model ---
model = LinearRegression()
model.fit(X, y)

# --- Save model file ---
joblib.dump(model, 'bike_price_model.pkl')

print("✅ Model trained and saved successfully as 'bike_price_model.pkl'")
