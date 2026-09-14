# AI-Driven Student Performance Prediction System

A Machine Learning project that predicts the **total score** of a student based on study habits and academic performance using multiple regression models. The project compares **Linear Regression**, **Decision Tree Regressor**, and **Random Forest Regressor** to identify the best-performing model and provides predictions for a **random student from the test dataset** through both a Python script and a Flask web application.

---

# Project Overview

Educational institutions can use predictive analytics to estimate student performance and identify learning trends. This project trains multiple machine learning models on a large student performance dataset and predicts the final score of unseen students.

---

# Features

* Predict student total score
* Predict for a **random student** from the test dataset
* Compare multiple ML algorithms
* Automatically save the best model
* Evaluate model performance using regression metrics
* Flask web application
* Clean and modular project structure
* Easy to extend with more features

---

# Dataset

* **Source:** Kaggle
* **Rows:** 1,000,000
* **Columns:** 6

### Features

| Column                  | Description               |
| ----------------------- | ------------------------- |
| student_id              | Unique student ID         |
| weekly_self_study_hours | Weekly study hours        |
| attendance_percentage   | Attendance percentage     |
| class_participation     | Class participation score |
| total_score             | Final score (Target)      |
| grade                   | Student grade             |

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Scikit-learn
* Joblib
* Flask

---

# Machine Learning Models

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor

The project automatically compares all models and saves the one with the highest **R² Score**.

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
```

---

# Workflow

```text
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
```

---

# Evaluation Metrics

The models are evaluated using:

* Mean Absolute Error (MAE)
* Mean Squared Error (MSE)
* Root Mean Squared Error (RMSE)
* R² Score

---

# Installation

## Clone the Repository

```bash
git clone https://github.com/your-username/Student_Performance_Prediction.git

cd Student_Performance_Prediction
```

---

## Create Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

### macOS/Linux

```bash
python3 -m venv venv
```

Activate

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Train the Model

```bash
python src/train.py
```

This will:

* Train all models
* Compare performance
* Save the best model
* Save test data for prediction

---

# Predict a Random Student

```bash
python src/predict.py
```

Example Output

```text
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
```

---

# Run Flask Application

```bash
python app.py
```

Open your browser:

```
http://127.0.0.1:5000
```

Click **Predict Random Student** to generate a prediction for a randomly selected student from the test dataset.

---

# Results

| Model             | R² Score |
| ----------------- | --------- |
| Linear Regression | 0.6600    |
| Decision Tree     | 0.4320    |
| Random Forest     | 0.6550    |

**Best Model:** Linear Regression

---

# Future Enhancements

* Student performance dashboard
* Feature importance visualization
* SHAP Explainable AI
* Model hyperparameter tuning
* User authentication
* Database integration
* Student report generation
* Model deployment on Render or Railway
* Docker support
* REST API using Flask/FastAPI

---

# Requirements

```text
pandas
numpy
matplotlib
scikit-learn
joblib
flask
```

Install all dependencies using:

```bash
pip install -r requirements.txt
```

---

# Learning Outcomes

By completing this project, you will learn:

* Data preprocessing
* Exploratory Data Analysis (EDA)
* Regression algorithms
* Model evaluation
* Model comparison
* Model serialization using Joblib
* Flask integration
* Predicting unseen data
* Building an end-to-end Machine Learning project

---

# Author

**Your Name**

GitHub: [github.com/rakesh2163yadav-pixel](https://github.com/rakesh2163yadav-pixel)

LinkedIn: [www.linkedin.com/in/rakesh-yadav-0372a633a?utm_source=share_via&amp;utm_content=profile&amp;utm_medium=member_android](https://www.linkedin.com/in/rakesh-yadav-0372a633a?utm_source=share_via&utm_content=profile&utm_medium=member_android)

---

# License

This project is licensed under the **MIT License**.

---

⭐ **If you found this project useful, consider giving it a star on GitHub!**
