# Calculating Monthly Gym RevenueScenario: A gym owner wants to forecast monthly revenue to optimize budget allocation.Input Features ($X$):$X_1$: Total number of active premium members$X_2$: Monthly digital marketing expenditure (in dollars)Target Variable ($Y$): Total monthly revenue (in dollars)Practice Goal: Determine the baseline revenue (intercept) when membership growth and ad spend are zero.

import numpy as np
from sklearn.linear_model import LinearRegression

# create dataset (Active premium members, Monthly digital ad spend in $)

gym_data = np.array([
    [120, 500], [180, 800], [250, 1200], [310, 1500], [90, 300],
    [210, 950], [350, 1800], [140, 600], [280, 1350], [400, 2100],
    [110, 450], [195, 850], [260, 1250], [330, 1650], [130, 550],
    [225, 1050], [370, 1950], [80, 250], [160, 700], [295, 1400],
    [115, 480], [185, 820], [240, 1150], [320, 1600], [150, 650],
    [230, 1100], [360, 1900], [95, 350], [175, 750], [285, 1380],
    [105, 420], [200, 900], [255, 1220], [340, 1700], [135, 580],
    [220, 1000], [380, 2000], [75, 200], [165, 720], [300, 1450],
    [125, 520], [190, 860], [245, 1180], [315, 1550], [145, 620],
    [215, 980], [365, 1920], [85, 280], [170, 740], [290, 1420]
])

# output dataset (Total monthly revenue in $)
revenue = np.array([
    10250.0, 14700.0, 19950.0, 24500.0, 7900.0,
    16850.0, 27600.0, 11750.0, 22250.0, 31400.0,
    9500.0, 15800.0, 20750.0, 26050.0, 11000.0,
    18050.0, 29150.0, 7150.0, 13250.0, 23400.0,
    9850.0, 15050.0, 19200.0, 25250.0, 12500.0,
    18450.0, 28400.0, 8300.0, 14350.0, 22650.0,
    9100.0, 16200.0, 20350.0, 26800.0, 11400.0,
    17650.0, 29900.0, 6750.0, 13600.0, 23800.0,
    10600.0, 15450.0, 19600.0, 24900.0, 12100.0,
    17250.0, 28750.0, 7550.0, 14000.0, 23050.0
])

# create model
model = LinearRegression()

# model train
model.fit(gym_data, revenue)

# practice goal: extract baseline revenue (intercept) and feature weights


# prediction for a mid-sized branch (200 members, $1,000 ad spend)
mid_gym = np.array([[200, 1000]])
print(f"Forecasted revenue for 200 members and $1,000 ad spend: $model.predict(mid_gym)")

# prediction under zero growth / zero ad spend (evaluates baseline intercept)
zero_input = np.array([[0, 0]])
print(f"Forecasted revenue with 0 members and $0 ad spend: $model.predict(zero_input)")

