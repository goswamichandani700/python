# Real Estate Housing Area Segmentation

# Features 3

#  Price per Square Foot ft
#  Distance from Transit Hub km
#  School Rating 110

# Finding the value of k
# For this example we choose k  4 to divide housing areas into four groups based on price transportation and school quality

# Clusters k  4

#  Cluster 1  Premium Areas High property prices and very close to public transport

#  Cluster 2  Family Areas Higher property prices but farther from transport with very good schools

#  Cluster 3  Average Areas Medium property prices reasonably close to transport and average schools

#  Cluster 4  Budget Areas Low property prices far from transport and lower school ratings

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#create dataset
X = np.array([[8500,1,9],[9200,1.5,10],[8800,2,9],[9500,1.2,10],[9000,1.8,9],[9800,2.1,10],[8700,1.3,9],[9400,1.7,10],[9100,2.2,9],[9900,1.5,10],[7000,5,9],[7600,6,10],[7200,5.5,9],[8000,7,10],[7400,6.5,9],[8200,5.8,10],[7800,7.2,9],[7500,6.2,10],[8100,5.4,9],[7700,6.8,10],[5000,3,6],[5500,4,7],[5800,3.5,6],[6200,4.2,7],[5300,3.8,6],[6000,4.5,7],[5700,3.2,6],[6500,4.8,7],[5900,3.7,6],[6100,4.1,7],[2800,8,4],[3200,9,5],[3500,10,4],[3000,8.5,3],[3800,11,5],[2600,9.5,4],[3400,10.5,5],[2900,8.8,3],[3600,12,4],[3100,9.2,5],[8600,1.6,9],[7300,6,10],[5200,3.6,6],[3300,10,4],[9300,1.9,10],[5600,4.3,7],[2700,9,3],[7900,6.6,9],[3700,11.5,5],[6300,4.6,7]])

model = KMeans(n_clusters=4,random_state=42,n_init=5)

#train model
model.fit(X)

#extract labels
labels = model.labels_

#print(label)
print("labels = ",labels)

# print centeriods
print(model.cluster_centers_)

#display data
areas = ["Area 1", "Area 2", "Area 3", "Area 4", "Area 5",
"Area 6", "Area 7", "Area 8", "Area 9", "Area 10",
"Area 11", "Area 12", "Area 13", "Area 14", "Area 15",
"Area 16", "Area 17", "Area 18", "Area 19", "Area 20",
"Area 21", "Area 22", "Area 23", "Area 24", "Area 25",
"Area 26", "Area 27", "Area 28", "Area 29", "Area 30",
"Area 31", "Area 32", "Area 33", "Area 34", "Area 35",
"Area 36", "Area 37", "Area 38", "Area 39", "Area 40",
"Area 41", "Area 42", "Area 43", "Area 44", "Area 45",
"Area 46", "Area 47", "Area 48", "Area 49", "Area 50"]
for area,data,label in zip(areas,X,labels):
    print(f"Name : {area} data = {data} label = {label}")

#create chart
plt.scatter(labels,X[:,0],s=10)
plt.xticks(ticks=range(0,4),labels=range(0,4))
plt.ylabel("Price per Square Foot")
plt.xlabel("Labels")
plt.show()