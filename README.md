# AI-Driven Student Performance Prediction System

> **IBM PBL Internship Project**

A Machine Learning project developed as part of the **IBM PBL (Project-Based Learning) Internship**. The system predicts the **total score** of a student based on study habits and academic performance using multiple regression models.

The project compares **Linear Regression**, **Decision Tree Regressor**, and **Random Forest Regressor** to identify the best-performing model. It provides predictions for a **random student from the test dataset** through both a Python script and a Flask web application.

---

# Project Overview

This project was developed as part of the **IBM PBL Internship** to apply Machine Learning concepts to an educational performance prediction problem.

Educational institutions can use predictive analytics to estimate student performance and identify learning trends. This project trains multiple machine learning models on a large student performance dataset and predicts the final score of unseen students.

The project covers the complete Machine Learning workflow, including:

- Data preprocessing
- Exploratory Data Analysis (EDA)
- Feature selection
- Train-test splitting
- Model training
- Model comparison
- Model evaluation
- Model serialization
- Prediction
- Flask web application integration

---

# Internship Information

| Details | Information |
|---------|-------------|
| **Program** | IBM PBL Internship |
| **Project** | AI-Driven Student Performance Prediction System |
| **Domain** | Machine Learning / Artificial Intelligence |
| **Student** | Avni Gupta |
| **Technology** | Python, Machine Learning, Flask |

---

# Features

- Predict student total score
- Predict performance for a **random student** from the test dataset
- Compare multiple ML algorithms
- Automatically save the best-performing model
- Evaluate model performance using regression metrics
- Flask web application
- Clean and modular project structure
- Easy to extend with additional features

---

# Dataset

- **Source:** Kaggle
- **Rows:** 1,000,000
- **Columns:** 6

## Features

| Column | Description |
|--------|-------------|
| `student_id` | Unique student ID |
| `weekly_self_study_hours` | Weekly study hours |
| `attendance_percentage` | Attendance percentage |
| `class_participation` | Class participation score |
| `total_score` | Final score (Target) |
| `grade` | Student grade |

---

# Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Scikit-learn
- Joblib
- Flask

---

# Machine Learning Models

The project uses and compares the following regression algorithms:

### 1. Linear Regression

A statistical model used to predict the target variable based on the relationship between input features and the target.

### 2. Decision Tree Regressor

A tree-based machine learning algorithm that makes predictions by splitting the dataset based on feature values.

### 3. Random Forest Regressor

An ensemble learning algorithm that combines multiple decision trees to improve prediction performance.

The project automatically compares all models and saves the model with the highest **R² Score**.

---

# Project Structure

```text
Student_Performance_Prediction/
│
├── dataset/
│   └── student_performance.csv
│
├── models/
│   ├── best_model.pkl
│   ├── X_test.csv
│   └── y_test.csv
│
├── src/
│   ├── train.py
│   ├── predict.py
│   ├── preprocessing.py
│   └── visualize.py
│
├── static/
│   └── css/
│       └── style.css
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py
├── requirements.txt
└── README.md
Workflow
Dataset
   │
   ▼
Data Cleaning
   │
   ▼
Exploratory Data Analysis (EDA)
   │
   ▼
Feature Selection
   │
   ▼
Train-Test Split
   │
   ▼
Train Multiple Models
   │
   ▼
Model Evaluation
   │
   ▼
Best Model Selection
   │
   ▼
Save Model
   │
   ▼
Prediction
   │
   ▼
Flask Web Application
Evaluation Metrics

The models are evaluated using the following regression metrics:

Mean Absolute Error (MAE)
Mean Squared Error (MSE)
Root Mean Squared Error (RMSE)
R² Score

These metrics are used to compare the prediction performance of the different regression models.

Installation
Clone the Repository
git clone https://github.com/Avni7719/AI_Driven_Student_Performance_Prediction_System.git

cd AI_Driven_Student_Performance_Prediction_System
Create Virtual Environment
Windows
python -m venv venv

Activate the virtual environment:

venv\Scripts\activate
macOS/Linux
python3 -m venv venv

Activate:

source venv/bin/activate
Install Dependencies

Install all required Python packages using:

pip install -r requirements.txt
Train the Model

Run the following command:

python src/train.py

This will:

Train all machine learning models
Compare their performance
Select the best-performing model
Save the best model
Save test data for prediction
Predict a Random Student

Run:

python src/predict.py

The program selects a random student from the test dataset and generates a performance prediction.

Example Output
=======================================================
         STUDENT PERFORMANCE REPORT
=======================================================

Weekly Study Hours   : 18.5 hrs
Attendance           : 91.2 %
Class Participation  : 8

Actual Score         : 88.70
Predicted Score      : 89.31

Actual Grade         : B
Predicted Grade      : B

Prediction Error     : 0.61

Model Used           : Linear Regression
=======================================================
Run Flask Application

Start the Flask web application using:

python app.py

The application will run locally at:

http://127.0.0.1:5000

Open the URL in your browser.

Click Predict Random Student to generate a prediction for a randomly selected student from the test dataset.

Results

The project compares the performance of the three machine learning models using the R² Score.

Model	R² Score
Linear Regression	0.6600
Decision Tree	0.4320
Random Forest	0.6550

The model comparison is based on the reported R² scores from the project.

Best Model based on the reported results: Linear Regression

Future Enhancements

The following improvements can be added to the project in the future:

Student performance dashboard
Feature importance visualization
SHAP Explainable AI
Model hyperparameter tuning
User authentication
Database integration
Student report generation
Model deployment on Render or Railway
Docker support
REST API using Flask/FastAPI
Requirements

The project requires the following Python libraries:

pandas
numpy
matplotlib
scikit-learn
joblib
flask

Install all dependencies using:

pip install -r requirements.txt
Learning Outcomes

This project provides practical experience in:

Data preprocessing
Exploratory Data Analysis (EDA)
Regression algorithms
Model training
Model evaluation
Model comparison
Model serialization using Joblib
Flask integration
Predicting unseen data
Building an end-to-end Machine Learning project
IBM PBL Internship

This project was developed as part of the IBM PBL Internship by Avni Gupta.

The project demonstrates the practical application of Machine Learning techniques to predict student academic performance using educational data.

Author
Avni Gupta

IBM PBL Internship Project

GitHub

https://github.com/Avni7719

LinkedIn

https://www.linkedin.com/in/avni-gupta-186366281

License

This project is licensed under the MIT License.

⭐ If you found this project useful, consider giving it a star on GitHub!

This keeps the original project's dataset, models, metrics, workflow, structure, and implementation details while adding the **IBM PBL Internship** context and Avni Gupta's profile information. :contentReference[oaicite:0]{index=0}
