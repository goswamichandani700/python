# Sports Analytics Football Midfielder Grouping

# Features 3

# Progressive Passes per 90 minutes
# Defensive Pressures per 90 minutes
# Distance Covered km/match


# Finding the value of k
# We choose k = 3 because midfielders can be grouped
# into three common playing styles


# Clusters k = 3

# Cluster 1 = Playmakers
# Make many forward passes but apply less defensive pressure

# Cluster 2 = Defensive Midfielders
# Make fewer forward passes but apply strong defensive pressure

# Cluster 3 = Box-to-Box Players
# Contribute in both attack and defence and cover a large distance


import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# create dataset

X = np.array([[8,12,9.2],[10,14,9.5],[12,13,9.8],[15,16,10.0],[18,15,9.7],[20,18,10.2],[22,17,10.1],[25,19,10.4],[14,12,9.6],[16,15,9.9],[19,16,10.0],[23,18,10.3],[27,20,10.5],[11,13,9.4],[17,14,9.8],[21,17,10.1],[24,19,10.2],[4,28,10.0],[6,32,10.2],[7,35,10.4],[5,38,10.1],[8,40,10.5],[9,36,10.3],[6,34,10.0],[10,42,10.6],[7,30,9.9],[5,37,10.2],[8,39,10.4],[9,35,10.1],[6,41,10.5],[10,38,10.3],[7,33,10.0],[5,40,10.2],[8,36,10.4],[12,25,11.2],[15,28,11.5],[18,30,11.8],[20,32,12.0],[16,35,11.7],[22,31,12.1],[25,34,12.3],[19,29,11.6],[23,36,12.2],[17,33,11.9],[21,30,12.0],[26,35,12.4],[14,27,11.3],[24,32,12.1],[18,34,11.8],[20,37,12.2]])


# create model

model = KMeans(n_clusters=3,random_state=42,n_init=5)


# train model

model.fit(X)


# extract labels

labels = model.labels_


# print labels

print("labels = ",labels)


# print centroids

print("Centroids = ")

print(model.cluster_centers_)


# display data

players = [
    "Player01","Player02","Player03","Player04","Player05",
    "Player06","Player07","Player08","Player09","Player10",
    "Player11","Player12","Player13","Player14","Player15",
    "Player16","Player17","Player18","Player19","Player20",
    "Player21","Player22","Player23","Player24","Player25",
    "Player26","Player27","Player28","Player29","Player30",
    "Player31","Player32","Player33","Player34","Player35",
    "Player36","Player37","Player38","Player39","Player40",
    "Player41","Player42","Player43","Player44","Player45",
    "Player46","Player47","Player48","Player49","Player50"
]


for player,data,label in zip(players,X,labels):

    print(
        f"Player : {player} "
        f"Progressive Passes = {data[0]} "
        f"Defensive Pressures = {data[1]} "
        f"Distance = {data[2]} km "
        f"label = {label}"
    )


# create chart

plt.scatter(labels,X[:,0],s=10)

plt.xticks(
    ticks=range(0,3),
    labels=range(0,3)
)

plt.ylabel("Progressive Passes per 90")
plt.xlabel("Labels")

plt.show()