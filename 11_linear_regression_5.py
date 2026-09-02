# Estimating Daily Ice Cream SalesScenario: An ice cream parlor owner wants to forecast daily product demand to prevent shortages or food waste.Input Features ($X$):$X_1$: Maximum daily temperature (in Fahrenheit or Celsius)$X_2$: Estimated daily foot traffic count passing the shopTarget Variable ($Y$): Number of ice cream cones sold per dayPractice Goal: Make a prediction for an upcoming hot weekend day with high projected foot traffic.

import numpy as np
from sklearn.linear_model import LinearRegression

# create dataset (Max temperature in °F, Daily foot traffic count)
sales_data = np.array([
    [72.0, 1150], [84.5, 1820], [90.0, 2400], [68.5, 950],  [95.0, 2750],
    [78.0, 1400], [88.5, 2150], [65.0, 820],  [82.0, 1650], [92.5, 2500],
    [75.5, 1300], [86.0, 1950], [70.0, 1050], [91.0, 2350], [80.5, 1580],
    [87.0, 2050], [96.5, 2900], [66.0, 880],  [79.0, 1480], [93.0, 2600],
    [74.0, 1220], [85.0, 1880], [71.5, 1100], [89.0, 2220], [81.0, 1600],
    [88.0, 2100], [94.0, 2700], [67.5, 920],  [77.0, 1380], [91.5, 2450],
    [73.5, 1200], [83.5, 1750], [69.0, 1000], [90.5, 2300], [82.5, 1700],
    [86.5, 2000], [97.0, 2950], [64.5, 800],  [78.5, 1450], [92.0, 2520],
    [76.0, 1320], [84.0, 1800], [72.5, 1180], [89.5, 2280], [80.0, 1550],
    [87.5, 2080], [95.5, 2800], [65.5, 850],  [79.5, 1500], [93.5, 2650]
])

# output dataset (Number of ice cream cones sold per day)
cones_sold = np.array([
    240, 425, 560, 185, 665,
    315, 510, 150, 385, 595,
    285, 460, 210, 550, 365,
    485, 705, 165, 335, 620,
    260, 440, 225, 525, 375,
    500, 645, 175, 305, 580,
    250, 405, 195, 540, 390,
    475, 715, 140, 325, 600,
    295, 420, 245, 530, 355,
    490, 675, 155, 345, 630
])

# create model
model = LinearRegression()

# model train
model.fit(sales_data, cones_sold)

# practice goal: prediction for a hot weekend day with high foot traffic (e.g., 98.0°F, 3,200 people)
hot_weekend = np.array([[98.0, 3200]])
print("price of cones with 98.0°F and 3200 people ",model.predict(hot_weekend))

# prediction for a mild weekday (e.g., 70.0°F, 1,000 foot traffic)
mild_day = np.array([[70.0, 1000]])

print("price of cones with 70.0°F and 1000 people ",model.predict(mild_day))


