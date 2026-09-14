import pandas as pd


def load_data():

    df = pd.read_excel("dataset/student_performance_project_100k.xlsx")

    X = df[
        [
            "weekly_self_study_hours",
            "attendance_percentage",
            "class_participation"
        ]
    ]

    y = df["total_score"]

    return X, y