#  Manufacturing Machine Bearing Condition

# Features 2

#  Vibration Level g
#  Operating Temperature C

# Clusters k  3

#  Cluster 1  Healthy Machine Low vibration and normal operating temperature

#  Cluster 2  Machine Wear Higher vibration and temperature which may indicate mechanical problems

#  Cluster 3  Critical Condition Very high vibration and temperature indicating that the machine may fail soon

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# create dataset

X = np.array([
    [0.18,48],
    [0.22,50],
    [0.25,52],
    [0.20,49],
    [0.28,53],
    [0.24,51],
    [0.19,47],
    [0.27,54],
    [0.23,50],
    [0.21,48],
    [0.29,55],
    [0.26,52],
    [0.17,46],
    [0.30,54],
    [0.25,53],
    [0.31,55],
    [0.20,49],
    [0.27,51],
    [0.24,50],
    [0.22,48],

    [0.75,68],
    [0.82,70],
    [0.88,72],
    [0.79,69],
    [0.91,74],
    [0.85,71],
    [0.73,67],
    [0.95,75],
    [0.81,70],
    [0.87,73],
    [0.92,74],
    [0.78,68],
    [0.84,72],
    [0.89,71],
    [0.76,69],
    [0.94,76],
    [0.80,70],
    [0.86,73],
    [0.90,75],
    [0.77,68],

    [1.55,88],
    [1.68,91],
    [1.75,94],
    [1.62,90],
    [1.85,97],
    [1.72,93],
    [1.58,89],
    [1.92,99],
    [1.66,92],
    [1.80,96]
])


# create model

model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=5
)


# train model

model.fit(X)


# extract labels

labels = model.labels_


# print labels

print("labels = ", labels)


# print centroids

print("Centroids = ")
print(model.cluster_centers_)


# display data

machines = [
    "Machine01","Machine02","Machine03","Machine04","Machine05",
    "Machine06","Machine07","Machine08","Machine09","Machine10",
    "Machine11","Machine12","Machine13","Machine14","Machine15",
    "Machine16","Machine17","Machine18","Machine19","Machine20",
    "Machine21","Machine22","Machine23","Machine24","Machine25",
    "Machine26","Machine27","Machine28","Machine29","Machine30",
    "Machine31","Machine32","Machine33","Machine34","Machine35",
    "Machine36","Machine37","Machine38","Machine39","Machine40",
    "Machine41","Machine42","Machine43","Machine44","Machine45",
    "Machine46","Machine47","Machine48","Machine49","Machine50"
]


for machine, data, label in zip(machines, X, labels):

    print(
        f"Machine : {machine} "
        f"Vibration = {data[0]} g "
        f"Temperature = {data[1]} C "
        f"label = {label}"
    )


# create chart

plt.scatter(labels, X[:,0], s=10)

plt.xticks(
    ticks=range(0,3),
    labels=range(0,3)
)

plt.ylabel("Vibration Level (g)")
plt.xlabel("Labels")

plt.show()