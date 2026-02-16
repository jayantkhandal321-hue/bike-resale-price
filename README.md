# 🏍️ Used Bike Price Prediction App

## 📘 Overview
This project is a **Machine Learning-based Web Application** that predicts the resale price of a used motorcycle.  
The app is built with **Streamlit**, and the model is trained using **scikit-learn**’s `LinearRegression` algorithm.

---

## 📁 Project Structure
```
├── bike_price_app.py
├── train_bike_model.py
├── bike_price_model.pkl
├── Used_Bikes.csv
├── Untitled0 (2).ipynb
└── README.md
```

---

## ⚙️ Files Description

### 🧠 train_bike_model.py
This script is used to train and save the machine learning model.
- The dataset is created manually as a Python dictionary.
- **Features:** `brand`, `owner`, `age`, `kms_driven`, `power`, `engine`
- **Target:** `price`
- **Model Used:** `LinearRegression` from scikit-learn
- The trained model is saved as `bike_price_model.pkl` using `joblib`.

---

### 💾 bike_price_model.pkl
- Pre-trained Linear Regression model.
- Used by the Streamlit app to predict the resale value of bikes.
- Generated from `train_bike_model.py`.

---

### 🌐 bike_price_app.py
This is the **Streamlit Web App** that provides an interactive interface for users to estimate bike prices.

#### ✨ Features:
- Collects user input for:
  - Brand
  - Owner Type
  - Age of the Bike (in years)
  - Kilometers Driven
  - Power (in bhp)
  - Engine Capacity (in cc)
- Performs input validation and shows warnings for unusual values.
- Loads the saved model (`bike_price_model.pkl`) for prediction.
- Displays the predicted resale price in a user-friendly format.

#### 🚀 Run Command:
```bash
streamlit run bike_price_app.py
```
This will open the app in your default web browser.

---

### 📊 Used_Bikes.csv
- A sample dataset containing real-world used bike listings.
- Can be used for further training or improving the model.
- Includes features such as brand, owner type, kilometers driven, engine, power, and price.

---

### 📓 Untitled0 (2).ipynb
- Jupyter Notebook file for experimentation or data exploration.
- Useful for trying out new preprocessing or visualization techniques.

---

## 🧠 How It Works
1. **Model Training** → Run `train_bike_model.py` to train and save the model.  
2. **App Launch** → Run `bike_price_app.py` using Streamlit.  
3. **Prediction** → Enter the bike details; the app predicts the estimated resale price.

---

## 📦 Requirements
Install the required Python libraries using:

```bash
pip install streamlit pandas scikit-learn joblib
```

---

## 💡 Future Enhancements
- Train the model on a larger real-world dataset (`Used_Bikes.csv`).
- Experiment with more advanced algorithms like RandomForest or XGBoost.
- Use one-hot encoding for categorical variables instead of label encoding.
- Add image upload or automatic bike-spec data fetching features.

---

## 👨‍💻 Author
**Developed by:** *[JAYANT KHANDAL]*  
**Language:** Python 🐍  
**Framework:** Streamlit  
**ML Library:** scikit-learn  

---

### ⭐ If you like this project, don’t forget to star the repo on GitHub!


