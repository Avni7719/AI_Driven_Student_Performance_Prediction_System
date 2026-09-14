import os
import pandas as pd
import matplotlib.pyplot as plt

# ==================================================
# Create outputs folder
# ==================================================
os.makedirs("outputs", exist_ok=True)

# ==================================================
# Load Dataset
# ==================================================
df = pd.read_excel("dataset/student_performance_project_100k.xlsx")

# ==================================================
# Create Grade Column
# ==================================================
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

df["grade"] = df["total_score"].apply(get_grade)

# ==================================================
# Style
# ==================================================
plt.style.use("ggplot")

print("=" * 60)
print("Dataset Shape :", df.shape)
print("=" * 60)

# ==================================================
# 1. Total Score Distribution
# ==================================================
plt.figure(figsize=(8,5))

plt.hist(
    df["total_score"],
    bins=25,
    edgecolor="black"
)

plt.title("Distribution of Total Score")
plt.xlabel("Total Score")
plt.ylabel("Number of Students")

plt.tight_layout()
plt.savefig("outputs/01_total_score_distribution.png", dpi=300)
plt.close()

# ==================================================
# 2. Grade Distribution
# ==================================================
grade_count = df["grade"].value_counts().sort_index()

plt.figure(figsize=(7,5))

plt.bar(
    grade_count.index,
    grade_count.values
)

plt.title("Grade Distribution")
plt.xlabel("Grade")
plt.ylabel("Students")

plt.tight_layout()
plt.savefig("outputs/02_grade_distribution.png", dpi=300)
plt.close()

# ==================================================
# 3. Grade Pie Chart
# ==================================================
plt.figure(figsize=(7,7))

plt.pie(
    grade_count.values,
    labels=grade_count.index,
    autopct="%1.1f%%",
    startangle=90
)

plt.title("Grade Percentage")

plt.savefig("outputs/03_grade_pie_chart.png", dpi=300)
plt.close()

# ==================================================
# 4. Study Hours Distribution
# ==================================================
plt.figure(figsize=(8,5))

plt.hist(
    df["weekly_self_study_hours"],
    bins=20,
    edgecolor="black"
)

plt.title("Weekly Study Hours Distribution")
plt.xlabel("Study Hours")
plt.ylabel("Students")

plt.tight_layout()
plt.savefig("outputs/04_study_hours_distribution.png", dpi=300)
plt.close()

# ==================================================
# 5. Attendance Distribution
# ==================================================
plt.figure(figsize=(8,5))

plt.hist(
    df["attendance_percentage"],
    bins=20,
    edgecolor="black"
)

plt.title("Attendance Distribution")
plt.xlabel("Attendance Percentage")
plt.ylabel("Students")

plt.tight_layout()
plt.savefig("outputs/05_attendance_distribution.png", dpi=300)
plt.close()

# ==================================================
# 6. Participation Distribution
# ==================================================
plt.figure(figsize=(8,5))

plt.hist(
    df["class_participation"],
    bins=10,
    edgecolor="black"
)

plt.title("Class Participation Distribution")
plt.xlabel("Participation")
plt.ylabel("Students")

plt.tight_layout()
plt.savefig("outputs/06_participation_distribution.png", dpi=300)
plt.close()

# ==================================================
# 7. Study Hours vs Total Score
# ==================================================
plt.figure(figsize=(8,5))

plt.scatter(
    df["weekly_self_study_hours"],
    df["total_score"],
    alpha=0.2
)

plt.title("Study Hours vs Total Score")
plt.xlabel("Weekly Study Hours")
plt.ylabel("Total Score")

plt.tight_layout()
plt.savefig("outputs/07_study_hours_vs_score.png", dpi=300)
plt.close()

# ==================================================
# 8. Attendance vs Total Score
# ==================================================
plt.figure(figsize=(8,5))

plt.scatter(
    df["attendance_percentage"],
    df["total_score"],
    alpha=0.2
)

plt.title("Attendance vs Total Score")
plt.xlabel("Attendance Percentage")
plt.ylabel("Total Score")

plt.tight_layout()
plt.savefig("outputs/08_attendance_vs_score.png", dpi=300)
plt.close()

# ==================================================
# 9. Participation vs Total Score
# ==================================================
plt.figure(figsize=(8,5))

plt.scatter(
    df["class_participation"],
    df["total_score"],
    alpha=0.2
)

plt.title("Participation vs Total Score")
plt.xlabel("Class Participation")
plt.ylabel("Total Score")

plt.tight_layout()
plt.savefig("outputs/09_participation_vs_score.png", dpi=300)
plt.close()

# ==================================================
# 10. Total Score Box Plot
# ==================================================
plt.figure(figsize=(6,5))

plt.boxplot(df["total_score"])

plt.title("Box Plot of Total Score")
plt.ylabel("Score")

plt.tight_layout()
plt.savefig("outputs/10_boxplot_total_score.png", dpi=300)
plt.close()

# ==================================================
# 11. Correlation Heatmap
# ==================================================
corr = df[
    [
        "weekly_self_study_hours",
        "attendance_percentage",
        "class_participation",
        "total_score"
    ]
].corr()

plt.figure(figsize=(7,6))

plt.imshow(corr, cmap="coolwarm")

plt.xticks(
    range(len(corr.columns)),
    corr.columns,
    rotation=30,
    ha="right"
)

plt.yticks(
    range(len(corr.columns)),
    corr.columns
)

for i in range(len(corr.columns)):
    for j in range(len(corr.columns)):
        plt.text(
            j,
            i,
            f"{corr.iloc[i,j]:.2f}",
            ha="center",
            va="center",
            fontsize=9,
            color="black"
        )

plt.colorbar()

plt.title("Correlation Heatmap")

plt.tight_layout()

plt.savefig("outputs/11_correlation_heatmap.png", dpi=300)

plt.close()

# ==================================================
# Finish
# ==================================================
print("\n" + "=" * 60)
print("All visualizations generated successfully!")
print("=" * 60)

print("\nSaved in outputs folder:")
print("""
01_total_score_distribution.png
02_grade_distribution.png
03_grade_pie_chart.png
04_study_hours_distribution.png
05_attendance_distribution.png
06_participation_distribution.png
07_study_hours_vs_score.png
08_attendance_vs_score.png
09_participation_vs_score.png
10_boxplot_total_score.png
11_correlation_heatmap.png
""")