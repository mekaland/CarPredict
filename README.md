Car Prediction Application

🔗 Live App Link
https://fl4vqykkd9hhrjo3a24ndp.streamlit.app/

Car Price Prediction App

🚗 Features

Predicts car prices using machine learning.

User-friendly interface built with Streamlit.

Accepts various car attributes, including:

Make: Manufacturer.

Model: Specific car model.

Trim: Detailed model specs.

Mileage: Kilometers traveled.

Type: Car type (e.g., sedan, SUV).

Cylinder: Engine cylinders.

Liter: Engine size in liters.

Doors: Number of doors.

Cruise Control: Has cruise control (True/False).

Sound System: Has premium sound (True/False).

Leather Seats: Has leather seats (True/False).

🛠 How It Works

1️⃣ Data Preparation

Dataset: Reads data from cars.xls.

Preprocessing:

Numerical data standardized using StandardScaler.

Categorical data encoded with OneHotEncoder.

2️⃣ Model Training

Algorithm: Linear Regression via scikit-learn.

Pipeline: Combines preprocessing and model training.

Evaluation: Assessed using:

Mean Squared Error (MSE).

R-squared (R²).

3️⃣ Streamlit UI

Interactive UI allows input of car features.

Predicts price based on user inputs.

🌐 Deployment

Hosted on Streamlit Cloud.

Access the app here: Car Price Prediction App.
