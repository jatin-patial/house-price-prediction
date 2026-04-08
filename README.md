# 🏠 House Price Prediction System

## 📌 Overview

This project is an end-to-end Machine Learning application that predicts house prices based on various features such as area, number of bedrooms, bathrooms, and more. The model is trained on real-world housing data and deployed using an interactive web interface.

---

## 🚀 Features

* Data Cleaning & Preprocessing
* Feature Engineering (house age, total area, etc.)
* Multiple ML Models (Linear Regression, Random Forest)
* Hyperparameter Tuning using GridSearchCV
* Interactive Web App using Streamlit
* Real-time Price Prediction

---

## 🛠️ Tech Stack

* Python
* Pandas
* Scikit-learn
* Streamlit

---

## 📂 Project Structure

```
house-price-prediction/
│
├── data/
│   └── data.csv
│
├── notebook/
│   └── model.py
│
├── models/
│   ├── model.pkl
│   └── scaler.pkl
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## ⚙️ Installation & Setup

### 1. Clone the repository

```
git clone https://github.com/jatin-patial/house-price-prediction.git
cd house-price-prediction
```

### 2. Create virtual environment

```
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

---

## ▶️ Run the Project

### Step 1: Train the model

```
python notebook/model.py
```

### Step 2: Run Streamlit app

```
streamlit run app.py
```

---

## 📊 Model Details

* Input Features: Bedrooms, Bathrooms, Area, Floors, etc.
* Output: Predicted House Price
* Algorithm Used: Random Forest Regressor
* Optimization: GridSearchCV

---

## 📈 Future Improvements

* Add XGBoost for better accuracy
* Deploy on cloud (Render/Streamlit Cloud)
* Add location-based prediction using maps
* Improve UI/UX of web app

---

## 👨‍💻 Author

**Jatin Patial**
📧 [jatinpatial4433@gmail.com](mailto:jatinpatial4433@gmail.com)

---

## ⭐ Show Your Support

If you like this project, give it a ⭐ on GitHub!
