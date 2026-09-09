#  Agriculture Soil Fertility Grouping

# Features 4

#  Soil pH
#  Nitrogen mgkg
#  Phosphorus mgkg
#  Electrical Conductivity dSm

# Finding the value of k Elbow Method
# Run KMeans for k  1 to 7 and calculate WCSS The elbow appears at k  3

# Clusters k  3

#  Cluster 1  Poor Soil Low pH and low nitrogen and phosphorus The soil may need additional treatment

#  Cluster 2  Good Agricultural Soil Balanced pH with good levels of nitrogen and phosphorus

#  Cluster 3  Salty Soil High pH high phosphorus and high electrical conductivity The soil may have excess fertilizer or salt


import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#create dataset
X = np.array([[5.2,35,18,0.4],[5.5,40,22,0.5],[5.0,30,15,0.3],[5.7,45,25,0.6],[5.3,38,20,0.4],[5.1,32,17,0.3],[5.6,42,23,0.5],[5.4,36,19,0.4],[5.8,48,27,0.6],[5.2,34,16,0.3],[6.5,80,45,0.8],[6.7,85,50,0.9],[6.2,75,40,0.7],[6.8,90,55,1.0],[6.4,78,48,0.8],[6.6,88,52,0.9],[6.3,82,46,0.8],[6.9,92,58,1.1],[6.5,84,49,0.9],[6.7,86,54,1.0],[7.2,70,90,2.5],[7.5,75,100,3.0],[7.8,80,110,3.5],[7.4,72,95,2.8],[7.9,85,120,3.8],[7.3,68,88,2.4],[8.0,90,125,4.0],[7.6,78,105,3.2],[7.7,82,115,3.6],[7.4,74,98,2.9],[5.4,37,21,0.4],[6.6,83,47,0.9],[7.5,77,102,3.1],[5.1,31,14,0.3],[6.3,79,44,0.8],[7.8,88,118,3.7],[5.6,43,24,0.5],[6.8,91,56,1.0],[7.2,71,92,2.6],[5.3,33,17,0.4],[6.5,81,50,0.9],[7.9,87,122,3.9],[5.7,46,26,0.6],[6.4,76,43,0.8],[7.6,80,108,3.4],[5.0,29,13,0.3],[6.9,89,57,1.1],[7.3,73,96,2.7],[5.5,39,20,0.4],[7.7,84,112,3.5]])

model = KMeans(n_clusters=3,random_state=42,n_init=5)

#train model
model.fit(X)

#extract labels
labels = model.labels_

#print(label)
print("labels = ",labels)

# print centeriods
print(model.cluster_centers_)

#display data
soils = ["Aarav", "Aditi", "Rohan", "Priya", "Arjun", "Neha", "Rahul", "Sneha", "Vikram", "Pooja", "Karan", "Ananya", "Rajesh", "Kavita", "Amit", "Nisha", "Suresh", "Riya", "Manish", "Divya", "Akash", "Simran", "Nitin", "Pallavi", "Ravi", "Shreya", "Vivek", "Isha", "Sanjay", "Meera", "Harsh", "Komal", "Deepak", "Swati", "Yash", "Tanvi", "Prakash", "Anjali", "Mohit", "Payal", "Abhishek", "Kajal", "Rakesh", "Mansi", "Dhruv", "Sonal", "Pankaj", "Bhavna", "Kunal", "Radhika"]

for soil,data,label in zip(soils,X,labels):
    print(f"Name : {soil} data = {data} label = {label}")

#create chart
plt.scatter(labels,X[:,0],s=10)
plt.xticks(ticks=range(0,3),labels=range(0,3))
plt.ylabel("Soil pH")
plt.xlabel("Labels")
plt.show()