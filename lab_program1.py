import numpy as np

# Example: 4 students × 4 subjects
student_scores = np.array([
    [85, 90, 78, 92],  # Student 1
    [88, 76, 85, 80],  # Student 2
    [90, 88, 84, 86],  # Student 3
    [75, 85, 89, 91]   # Student 4
])
# Average of each column (subject)
subject_averages = np.mean(student_scores, axis=0)
# Index of the subject with highest average
highest_avg_index = np.argmax(subject_averages)

# Subject names for reference
subjects = ["Math", "Science", "English", "History"]

# Get the subject name with highest average
top_subject = subjects[highest_avg_index]
print("Average scores per subject:", subject_averages)
print("Subject with highest average score:", top_subject)
