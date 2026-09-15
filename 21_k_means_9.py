# Banking Credit Card Transaction Grouping

# Features 4

#  Transaction Amount 
#  Time Since Previous Transaction seconds
#  Distance from Usual Location km
#  POS Entry Mode


# Clusters k  4

#  Cluster 1  Normal Transactions Small or medium transactions made at regular intervals and familiar locations

#  Cluster 2  Travel Transactions Larger transactions made far away from the customers usual location

#  Cluster 3  Card Testing Very small transactions made repeatedly in a short period

#  Cluster 4  Suspicious Transactions Large transactions made quickly from unusual locations or using manual entry


import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler


# create dataset

X = np.array([[45,3600,2,1],[80,4200,4,1],[120,3000,3,2],[65,2800,5,1],[150,5000,7,2],[95,3200,2,1],[210,4500,6,2],[55,3900,3,1],[130,3400,5,2],[175,4100,4,1],[90,3700,6,2],[140,4600,3,1],[70,3100,4,2],[185,5200,7,1],[110,3500,2,2],[850,7200,250,1],[1200,9000,480,2],[650,6800,320,1],[1500,10800,600,2],[950,8400,410,1],[1800,12000,750,2],[720,7600,280,1],[1350,9600,520,2],[1100,8200,390,1],[1600,10200,680,2],[2,8,1,1],[5,12,2,1],[1,15,1,2],[8,20,3,1],[3,10,2,1],[6,18,1,2],[4,7,2,1],[9,25,3,1],[2,11,1,2],[7,16,2,1],[1800,45,350,3],[2500,60,520,3],[3200,35,700,4],[2100,80,450,3],[4000,50,850,4],[2750,70,600,3],[3500,40,900,4],[2200,90,500,3],[4500,55,1000,4],[3000,65,750,3]])


# scale the data

scaler = MinMaxScaler()

X_scaled = scaler.fit_transform(X)


# create model

model = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=5
)


# train model

model.fit(X_scaled)


# extract labels

labels = model.labels_


# print labels

print("labels = ", labels)


# print centroids

print("Centroids = ")

print(model.cluster_centers_)


# display data

transactions = [
    "Transaction01","Transaction02","Transaction03","Transaction04","Transaction05",
    "Transaction06","Transaction07","Transaction08","Transaction09","Transaction10",
    "Transaction11","Transaction12","Transaction13","Transaction14","Transaction15",
    "Transaction16","Transaction17","Transaction18","Transaction19","Transaction20",
    "Transaction21","Transaction22","Transaction23","Transaction24","Transaction25",
    "Transaction26","Transaction27","Transaction28","Transaction29","Transaction30",
    "Transaction31","Transaction32","Transaction33","Transaction34","Transaction35",
    "Transaction36","Transaction37","Transaction38","Transaction39","Transaction40",
    "Transaction41","Transaction42","Transaction43","Transaction44","Transaction45",
    "Transaction46","Transaction47","Transaction48","Transaction49","Transaction50"
]


for transaction, data, label in zip(transactions, X, labels):

    print(
        f"Transaction : {transaction} "
        f"Amount = {data[0]} "
        f"Time = {data[1]} sec "
        f"Distance = {data[2]} km "
        f"POS Entry Mode = {data[3]} "
        f"label = {label}"
    )


# create chart

plt.scatter(labels, X[:,0], s=10)

plt.xticks(
    ticks=range(0,4),
    labels=range(0,4)
)

plt.ylabel("Transaction Amount")
plt.xlabel("Labels")

plt.show()
