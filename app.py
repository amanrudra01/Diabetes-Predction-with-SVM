from flask import Flask, request, render_template
import numpy as np
import pickle

# Load the model and scaler
model_filename = 'Diabetes_Prediction_Model.pkl'
scaler_filename = 'scaler.pkl'

with open(model_filename, 'rb') as model_file:
    model = pickle.load(model_file)

with open(scaler_filename, 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

# Initialize the Flask application
app = Flask(__name__)


# Home route
@app.route('/')
def home():
    return render_template('index.html', prediction=None)  # Pass None initially for prediction


# Prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get input data from the form
    input_data = request.form.to_dict()

    # Convert input data to a numpy array
    input_data = np.array([float(input_data['Pregnancies']),
                           float(input_data['Glucose']),
                           float(input_data['BloodPressure']),
                           float(input_data['SkinThickness']),
                           float(input_data['Insulin']),
                           float(input_data['BMI']),
                           float(input_data['DiabetesPedigreeFunction']),
                           float(input_data['Age'])]).reshape(1, -1)

    # Standardize the input data
    standardized_data = scaler.transform(input_data)

    # Make prediction
    prediction = model.predict(standardized_data)

    # Interpret the prediction
    result = 'The person is diabetic' if prediction[0] == 1 else 'The person is not diabetic'

    # Render the result on the same page
    return render_template('index.html', prediction=result)


# Run the application
if __name__ == '__main__':
    app.run(debug=True)
