import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
import pickle
import os

# 1. Load the diabetes dataset from a CSV file
# Use pandas to read the dataset
try:
    df = pd.read_csv('diabetes.csv')
    print("Dataset loaded successfully.")
except FileNotFoundError:
    print("Error: diabetes.csv not found. Please ensure the dataset exists in the directory.")
    exit(1)

# 2. Separate features (X) and target variable (Y)
X = df.drop(columns=['Outcome'])
Y = df['Outcome']

# 3. Use StandardScaler to standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Split the dataset using train_test_split (80% training, 20% testing)
X_train, X_test, Y_train, Y_test = train_test_split(X_scaled, Y, test_size=0.2, random_state=42)

# 5. Train a Support Vector Machine model using SVC with linear kernel
print("Training Support Vector Machine (SVM) model...")
model = SVC(kernel='linear')
model.fit(X_train, Y_train)

# 6. Print model accuracy
accuracy = model.score(X_test, Y_test)
print(f"Model Accuracy: {accuracy * 100:.2f}%")

# Save the trained model and scaler for the Flask app to use
with open('model.pkl', 'wb') as f:
    pickle.dump(model, f)
    
with open('scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

print("Model (model.pkl) and scaler (scaler.pkl) saved successfully for use by Flask app.")
