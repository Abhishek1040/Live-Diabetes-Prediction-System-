# Live Working Diabetes Prediction System

# Created using Antigravity

# Hosted on the Vercel cloud platform
 live-link:- https://live-diabetes-prediction-system.vercel.app/


# Full Name: Abhishek Pawar

# skill track: AI & Machine Learning - Python

# Email ID: abhishek.p.pawar1999@gmail.com

# College Name: Sambhram academy of management studies, Bengaluru
 
A complete Machine Learning web application using Python, Flask, and Scikit-learn to predict diabetes.

## Project Structure
```
project/
│
├── app.py             # Main Flask application with routing
├── diabetes.csv       # Pima Indians Diabetes Dataset
├── model.py           # ML Model training script (runs SVM)
├── templates/
│   └── index.html     # Frontend HTML form UI
└── README.md          # Project documentation
```

## Setup Instructions

1. Install dependencies:
   ```bash
   pip install flask pandas scikit-learn numpy
   ```

2. Train the model:
   This will read `diabetes.csv`, train a Support Vector Machine (SVM) model using a linear kernel, print the accuracy, and save the model (`model.pkl`) and scaler (`scaler.pkl`).
   ```bash
   python model.py
   ```

3. Run the Flask web application:
   ```bash
   python app.py
   ```

4. Open your web browser and go to:
   https://live-diabetes-prediction-system.vercel.app/
