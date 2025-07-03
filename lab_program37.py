import pandas as pd
import matplotlib.pyplot as plt

# Load study time and exam score data
study_data = pd.read_csv("study_scores.csv")

# Scatter plot to visualize correlation
plt.scatter(study_data['study_hours'], study_data['exam_score'])
plt.xlabel('Study Hours')
plt.ylabel('Exam Score')
plt.title('Study Hours vs Exam Score')
plt.grid(True)
plt.show()
