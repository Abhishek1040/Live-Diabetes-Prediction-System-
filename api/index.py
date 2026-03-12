from flask import Flask, render_template, request
import numpy as np
import pickle
import os

app = Flask(__name__)

# Load the trained model and scaler
# Make sure model.py has been run first to generate these files
 
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

MODEL_PATH = os.path.join(BASE_DIR, "model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "scaler.pkl")

if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH):
    with open(MODEL_PATH, 'rb') as f:
        model = pickle.load(f)
    with open(SCALER_PATH, 'rb') as f:
        scaler = pickle.load(f)
else:
    model = None
    scaler = None
    print("Warning: Model or scaler not found. Please run model.py first.")

@app.route('/', methods=['GET'])
def home():
    # Show a simple webpage titled "Diabetes Prediction System"
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if model is None or scaler is None:
        return "Model not initialized. Please run model.py to generate the model.", 500

    try:
        # Accept form input values
        pregnancies = float(request.form['Pregnancies'])
        glucose = float(request.form['Glucose'])
        blood_pressure = float(request.form['BloodPressure'])
        skin_thickness = float(request.form['SkinThickness'])
        insulin = float(request.form['Insulin'])
        bmi = float(request.form['BMI'])
        dpf = float(request.form['DiabetesPedigreeFunction'])
        age = float(request.form['Age'])

        # Convert them to a numpy array
        input_data = np.array([[pregnancies, glucose, blood_pressure, skin_thickness, insulin, bmi, dpf, age]])

        # Apply the same StandardScaler transformation
        input_data_scaled = scaler.transform(input_data)

        # Predict using the trained SVM model
        prediction = model.predict(input_data_scaled)

        # Output Message: Display the prediction result
        if prediction[0] == 0:
            result = "The person is not diabetic"
        else:
            result = "The person is diabetic"

        return render_template('index.html', result=result)

    except Exception as e:
         return render_template('index.html', result=f"Error: {str(e)}")

if __name__ == '__main__':
    # Run the application
    app.run(debug=True, use_reloader=False)
