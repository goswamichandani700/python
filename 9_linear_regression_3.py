# Estimating Car Fuel EfficiencyScenario: An automotive blog wants to predict a vehicle's fuel economy to help consumers evaluate fuel costs.Input Features ($X$):$X_1$: Engine displacement size (in liters)$X_2$: Total vehicle weight (in pounds or kilograms)Target Variable ($Y$): Fuel efficiency (Miles Per Gallon - MPG)Practice Goal: Observe how both engine size and weight negatively correlate with fuel efficiency (negative coefficients).


import numpy as np
from sklearn.linear_model import LinearRegression

# create dataset (Engine displacement size in L, Vehicle weight in lbs)
car_data = np.array([
    [1.5, 2450], [2.0, 3100], [2.5, 3400], [3.5, 4100], [1.2, 2150],
    [1.8, 2800], [3.0, 3850], [5.0, 4800], [2.4, 3350], [4.0, 4400],
    [1.6, 2600], [2.0, 3200], [3.6, 4250], [1.4, 2300], [2.5, 3500],
    [3.0, 3900], [5.7, 5200], [2.2, 3150], [4.6, 4650], [1.5, 2500],
    [1.8, 2900], [2.8, 3700], [3.8, 4300], [1.3, 2200], [2.0, 3050],
    [3.5, 4150], [6.2, 5400], [2.3, 3300], [4.4, 4550], [1.6, 2650],
    [2.1, 3250], [3.2, 4000], [1.5, 2400], [2.7, 3600], [3.7, 4200],
    [5.0, 4900], [1.8, 2850], [4.0, 4350], [1.4, 2350], [2.2, 3100],
    [2.9, 3800], [3.6, 4100], [1.2, 2100], [2.0, 3150], [3.4, 3950],
    [5.3, 5100], [2.4, 3450], [4.2, 4500], [1.6, 2550], [2.5, 3550]
])

# output dataset (Fuel efficiency in Miles Per Gallon - MPG)
mpg = np.array([
    36.2, 30.1, 27.4, 21.0, 40.5,
    32.8, 23.5, 15.8, 28.0, 18.9,
    34.5, 29.2, 20.1, 38.0, 26.5,
    22.8, 14.1, 29.8, 16.9, 35.5,
    31.9, 24.6, 19.8, 39.2, 30.6,
    20.5, 12.8, 28.3, 17.5, 34.0,
    29.0, 22.4, 37.1, 25.2, 20.4,
    15.2, 32.1, 19.2, 37.5, 30.2,
    24.0, 21.2, 41.2, 29.7, 23.0,
    14.6, 27.1, 18.2, 35.0, 26.0
])

# create model
model = LinearRegression()

# model train
model.fit(car_data, mpg)

# prediction for a compact commuter car (1.5L engine, 2400 lbs)
compact_car = np.array([[1.5, 2400]])
print("Predicted MPG for compact car (1.5L, 2400 lbs):", model.predict(compact_car))

# prediction for a large full-size SUV (5.0L engine, 4800 lbs)
large_suv = np.array([[5.0, 4800]])
print("Predicted MPG for large SUV (5.0L, 4800 lbs):", model.predict(large_suv))

