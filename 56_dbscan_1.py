# Exercise 1.1: Ride-Sharing Pickup Hotspot and Dead-Zone Mapping
# Task Type: Clustering / Geospatial Analytics
# Business Problem: Cluster raw GPS pickup coordinates (Latitude, Longitude) to identify high-density surge-pricing zones and isolate remote, unprofitable pickup requests as noise.
# Portfolio Value: Demonstrates ability to apply the Haversine distance metric on geospatial data for logistics, food delivery, and mobility companies.
# Dataset Name: Uber Pickups in New York City (Kaggle)
# Dataset Link: https://raw.githubusercontent.com/fivethirtyeight/uber-tlc-foil-response/master/uber-trip-data/uber-raw-data-apr14.csv

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

# 1. Download Uber pickup data
url = "https://raw.githubusercontent.com/fivethirtyeight/uber-tlc-foil-response/master/uber-trip-data/uber-raw-data-apr14.csv"

# load data
df = pd.read_csv(url, nrows=5000)

# filter column
X = df[
    ["Lat",
        "Lon"
    ]
]

# remove blank rows
X = X.dropna()
print(len(X))
print(X.head(20))

# create model
model = DBSCAN(min_samples=10, eps=0.002)

# train model
model.fit_predict(X)

labels = model.labels_

# add labels into dataframe
X['labels'] = labels

print("Cluster wise count")
print(X['labels'].value_counts())
print(X.head(20))

# create scatter plot
plt.figure(figsize=(10,8))

# create chart
plt.scatter(X['Lat'], X['Lon'], c=X['labels'], s=10)
plt.title("Uber Pickup Hotspot and Dead-Zone Mapping")
plt.xlabel("Latitude")
plt.ylabel("Longitude")
plt.grid(True)
plt.show()