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

## Model Training

The following Python libraries and steps were used to train the machine learning model:

### Libraries Used
- NumPy
- pandas
- scikit-learn (StandardScaler, train_test_split, SVM, accuracy_score)
- pickle

### Training Steps
1. Load and preprocess the dataset.
2. Split the data into training and testing sets using `train_test_split`.
3. Standardize the feature set using `StandardScaler`.
4. Train a Support Vector Machine (SVM) model.
5. Evaluate the model's accuracy using `accuracy_score`.
6. Save the trained model and scaler using `pickle` for later use in predictions.

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

<img width="1708" alt="image" src="https://github.com/user-attachments/assets/ae06fc3b-4d4c-4672-9e0e-7745c51fe9d5" />


### Prediction Result:

<img width="1710" alt="image" src="https://github.com/user-attachments/assets/f10abda7-d280-4d2b-9d46-89d8c4b3b673" />

---

## Credits

- **Dataset**: [Pima Indians Diabetes Database](https://www.kaggle.com/datasets/uciml/pima-indians-diabetes-database)
- **Developed By**: Aman Chand

