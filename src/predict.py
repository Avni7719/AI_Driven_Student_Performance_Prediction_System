import joblib
import pandas as pd

model = joblib.load("models/best_model.pkl")

study = float(input("Weekly Study Hours : "))
attendance = float(input("Attendance Percentage : "))
participation = float(input("Class Participation (1-10): "))

sample = pd.DataFrame({

    "weekly_self_study_hours": [study],
    "attendance_percentage": [attendance],
    "class_participation": [participation]

})

prediction = model.predict(sample)[0]

prediction = round(max(0, min(100, prediction)), 2)

if prediction >= 90:
    grade = "A+"
elif prediction >= 80:
    grade = "A"
elif prediction >= 70:
    grade = "B"
elif prediction >= 60:
    grade = "C"
elif prediction >= 50:
    grade = "D"
else:
    grade = "F"

print()

print("=" * 40)
print("Predicted Score :", prediction)
print("Grade :", grade)
print("=" * 40)