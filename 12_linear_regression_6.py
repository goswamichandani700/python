# Software Developer Salary PredictionScenario: A tech recruitment platform wants to build a pricing model to estimate fair market salaries for software engineers.Input Features ($X$):$X_1$: Years of professional coding experience$X_2$: Number of specialized technical certifications earnedTarget Variable ($Y$): Annual salary (in thousands of dollars)Practice Goal: Evaluate how much value a certification adds to a developer's salary compared to an extra year of experience.

import numpy as np
from sklearn.linear_model import LinearRegression

# create dataset (Years of coding experience, Technical certifications)
developer_data = np.array([
    [1.0, 0], [3.5, 1], [6.0, 2], [9.0, 3], [0.5, 0],
    [4.0, 2], [8.0, 3], [12.0, 4], [2.5, 1], [10.5, 3],
    [1.5, 1], [5.0, 2], [7.5, 2], [11.0, 4], [3.0, 1],
    [6.5, 3], [13.0, 5], [0.8, 0], [4.5, 2], [9.5, 4],
    [2.0, 1], [5.5, 2], [7.0, 3], [10.0, 3], [3.2, 1],
    [6.8, 2], [12.5, 4], [1.2, 0], [4.2, 2], [8.5, 3],
    [2.2, 1], [5.2, 2], [7.8, 3], [10.2, 4], [3.8, 1],
    [6.2, 2], [14.0, 5], [0.6, 0], [4.8, 2], [9.2, 3],
    [2.8, 1], [5.8, 3], [7.2, 2], [11.5, 4], [3.6, 1],
    [6.0, 3], [13.5, 5], [1.0, 1], [4.6, 2], [8.8, 4]
])

# output dataset (Annual salary in thousands of dollars)
salaries = np.array([
    62.5, 84.0, 108.5, 137.0, 58.0,
    91.0, 128.5, 166.0, 75.5, 151.0,
    69.0, 99.5, 121.0, 158.0, 80.0,
    115.5, 178.0, 60.5, 96.0, 145.5,
    72.0, 103.5, 119.0, 146.0, 81.5,
    113.0, 171.5, 63.0, 93.0, 134.0,
    74.0, 101.0, 125.5, 152.0, 86.5,
    109.0, 187.0, 59.0, 98.0, 140.0,
    78.5, 110.0, 118.0, 162.5, 85.0,
    112.5, 183.0, 67.0, 97.0, 139.0
])

# create model
model = LinearRegression()

# model train
model.fit(developer_data, salaries)

#prediction
salary_1 = np.array([[13.5,5]])
print("salary with 13.5 year experiance and 5 technical certification ",model.predict(salary_1))

salary_2 = np.array([[6.0,2]])
print("salary with 6.0 year experiance and 2 technical certification ",model.predict(salary_2))
