from flask import Flask, render_template, request
import pandas as pd
import joblib

app = Flask(__name__)

model = joblib.load("models/best_model.pkl")


def get_grade(score):
    if score >= 90:
        return "A+"
    elif score >= 80:
        return "A"
    elif score >= 70:
        return "B"
    elif score >= 60:
        return "C"
    elif score >= 50:
        return "D"
    else:
        return "F"


def get_performance(score):
    if score >= 90:
        return "Outstanding"
    elif score >= 80:
        return "Excellent"
    elif score >= 70:
        return "Very Good"
    elif score >= 60:
        return "Good"
    elif score >= 50:
        return "Average"
    else:
        return "Needs Improvement"


def get_recommendation(score):
    if score >= 90:
        return "Excellent work! Keep it up."
    elif score >= 80:
        return "Very good. Stay consistent."
    elif score >= 70:
        return "Increase study hours slightly."
    elif score >= 60:
        return "Focus more on attendance."
    elif score >= 50:
        return "Practice regularly and participate more."
    else:
        return "Create a study plan and seek help."

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predict", methods=["POST"])
def predict():

    try:

        study = float(request.form["study_hours"])
        attendance = float(request.form["attendance"])
        participation = float(request.form["participation"])

        sample = pd.DataFrame({

            "weekly_self_study_hours": [study],
            "attendance_percentage": [attendance],
            "class_participation": [participation]

        })

        score = model.predict(sample)[0]
        score = round(max(0, min(100, score)), 2)

        return render_template(

            "result.html",

            score=score,

            grade=get_grade(score),

            performance=get_performance(score),

            recommendation=get_recommendation(score),

            confidence=95,

            study_hours=study,

            attendance=attendance,

            participation=participation

        )

    except Exception as e:

        return str(e)


if __name__ == "__main__":
    app.run(debug=True)