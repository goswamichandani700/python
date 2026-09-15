# Environmental Science Air Quality Zone Grouping

# Features 3

# PM25 ug/m3
# Nitrogen Dioxide NO2
# Ozone O3


# Finding the value of k
# We choose k = 3 because air quality zones
# can be grouped into three common conditions


# Clusters k = 3

# Cluster 1 = Traffic Pollution Areas
# High NO2 and PM25 levels mainly because of vehicle traffic

# Cluster 2 = Smog Areas
# High ozone and PM25 levels usually found in sunny and polluted areas

# Cluster 3 = Clean Areas
# Low PM25 and NO2 levels usually found near parks or green areas


import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# create dataset

X = np.array([[85,72,35],[92,80,38],[78,68,32],[105,88,40],[95,75,36],[88,82,34],[110,90,42],[82,70,30],[98,85,39],[115,92,44],[90,78,35],[100,86,41],[87,74,33],[108,89,43],[94,81,37],[102,84,40],[80,69,31],[72,35,82],[68,30,90],[75,38,95],[82,42,88],[70,32,92],[90,45,105],[78,36,98],[85,40,110],[95,48,115],[72,34,87],[88,43,102],[80,39,108],[92,46,112],[76,35,96],[86,41,104],[98,50,118],[84,37,100],[18,12,35],[22,15,38],[15,10,32],[25,18,40],[20,13,36],[12,9,30],[28,20,42],[16,11,34],[24,16,39],[19,12,33],[14,8,29],[27,19,41],[21,14,37],[17,10,31],[23,15,36],[13,9,28]])


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

zones = [
    "Zone01","Zone02","Zone03","Zone04","Zone05",
    "Zone06","Zone07","Zone08","Zone09","Zone10",
    "Zone11","Zone12","Zone13","Zone14","Zone15",
    "Zone16","Zone17","Zone18","Zone19","Zone20",
    "Zone21","Zone22","Zone23","Zone24","Zone25",
    "Zone26","Zone27","Zone28","Zone29","Zone30",
    "Zone31","Zone32","Zone33","Zone34","Zone35",
    "Zone36","Zone37","Zone38","Zone39","Zone40",
    "Zone41","Zone42","Zone43","Zone44","Zone45",
    "Zone46","Zone47","Zone48","Zone49","Zone50"
]


for zone,data,label in zip(zones,X,labels):

    print(
        f"Zone : {zone} "
        f"PM25 = {data[0]} ug/m3 "
        f"NO2 = {data[1]} "
        f"O3 = {data[2]} "
        f"label = {label}"
    )


# create chart

plt.scatter(labels,X[:,0],s=10)

plt.xticks(
    ticks=range(0,3),
    labels=range(0,3)
)

plt.ylabel("PM2.5 (ug/m3)")
plt.xlabel("Labels")

plt.show()