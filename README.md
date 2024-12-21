# Diabetes-Predction-with-SVM


# Diabetes Prediction System

A web application to predict the likelihood of diabetes based on user inputs using the **Pima Indians Diabetes Database** and a machine learning model trained with the dataset.

---

## Features

- **User-friendly Form**: Input details like glucose level, BMI, age, and more through an intuitive web form.
- **Machine Learning**: Utilizes a trained logistic regression model for predictions.
- **Real-time Results**: Displays the prediction result dynamically on the same page.
- **Scalable Backend**: Built with Flask for simplicity and extensibility.

---

## Dataset

This project uses the **Pima Indians Diabetes Database (PIDD)**, which includes diagnostic features and target labels for predicting diabetes. The dataset contains 768 entries with the following features:
- Pregnancies
- Glucose
- Blood Pressure
- Skin Thickness
- Insulin
- BMI
- Diabetes Pedigree Function
- Age

The target output:
- `1`: Diabetic
- `0`: Non-diabetic

---

## Requirements

### Python Libraries
- Flask
- NumPy
- pandas
- scikit-learn
- pickle

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/diabetes-prediction.git
   ```
2. Navigate to the project directory:
   ```bash
   cd diabetes-prediction
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## Usage

1. Run the Flask app:
   ```bash
   python app.py
   ```
2. Open your browser and navigate to:
   ```
   http://127.0.0.1:5000/
   ```
3. Fill in the form with the required details and click **Predict** to see the results.

---

## File Structure

```
project/
├── app.py                 # Flask application
├── templates/
│   ├── index.html         # Frontend HTML
├── static/
│   ├── css/
│       ├── styles.css     # CSS for styling
├── Diabetes_Prediction_Model.pkl  # Trained model
├── scaler.pkl                     # Scaler for standardization
├── README.md              # Project documentation
└── requirements.txt       # Python dependencies
```

---

## Screenshots

### Input Form:
![Input Form](https://via.placeholder.com/800x400?text=Add+your+form+screenshot)

### Prediction Result:
![Prediction Result](https://via.placeholder.com/800x400?text=Add+your+result+screenshot)

---

## Credits

- **Dataset**: [Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- **Developed By**: Aman Chand

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

