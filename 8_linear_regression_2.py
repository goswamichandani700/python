# Predicting Student Exam ScoresScenario: An education researcher wants to analyze how student study habits and class engagement impact final exam performance.Input Features ($X$):$X_1$: Hours studied per week$X_2$: Attendance rate (percentage)Target Variable ($Y$): Final exam score (out of 100)Practice Goal: Train a model to find out whether study hours or attendance has a stronger weight on the final score.

import numpy as np
from sklearn.linear_model import LinearRegression

# create dataset (Hours studied per week, Attendance rate %)
# 50 rows of student data
student_data = np.array([
    [5.0, 62.0], [12.5, 78.0], [18.0, 85.0], [22.5, 92.0], [8.0, 70.0],
    [15.0, 80.0], [25.0, 95.0], [6.5, 65.0], [10.0, 72.0], [20.0, 88.0],
    [7.0, 68.0], [14.0, 82.0], [19.5, 90.0], [24.0, 94.0], [9.5, 74.0],
    [16.5, 84.0], [27.0, 98.0], [5.5, 60.0], [11.0, 75.0], [21.0, 89.0],
    [8.5, 71.0], [13.0, 79.0], [17.5, 86.0], [23.0, 93.0], [10.5, 76.0],
    [15.5, 83.0], [26.0, 96.0], [6.0, 64.0], [11.5, 77.0], [20.5, 87.0],
    [7.5, 69.0], [13.5, 81.0], [18.5, 88.0], [23.5, 91.0], [9.0, 73.0],
    [16.0, 82.0], [28.0, 99.0], [4.5, 58.0], [12.0, 76.0], [19.0, 87.0],
    [8.0, 67.0], [14.5, 80.0], [17.0, 84.0], [22.0, 90.0], [10.0, 75.0],
    [15.0, 85.0], [25.5, 97.0], [5.0, 63.0], [12.5, 79.0], [21.5, 91.0]
])

# output dataset (Final exam score out of 100)
exam_scores = np.array([
    45.0, 62.0, 74.5, 85.0, 52.0,
    68.0, 92.5, 48.0, 57.0, 80.0,
    50.5, 66.0, 78.0, 88.5, 56.0,
    71.0, 96.0, 44.0, 59.5, 82.0,
    53.0, 64.0, 73.0, 86.0, 58.5,
    70.0, 94.0, 47.0, 61.0, 81.0,
    51.0, 65.5, 75.0, 87.0, 55.0,
    72.0, 98.0, 41.5, 62.5, 77.0,
    52.5, 67.0, 72.5, 84.0, 57.5,
    71.5, 93.0, 46.0, 63.5, 83.5
])

# create model
model = LinearRegression()

# model train
model.fit(student_data, exam_scores)

# prediction
student_1 = np.array([[25.0, 95.0]])
print("Predicted score for 25 study hours and 95% attendance:", model.predict(student_1))

# prediction for a low-effort student (5 hours/week, 60% attendance)
student_2 = np.array([[5.0, 60.0]])
print("Predicted score for 5 study hours and 60% attendance:", model.predict(student_2))