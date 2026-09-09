#  Telecommunications Mobile User Segmentation

# Features 4

#  Monthly Data Usage GB
#  Domestic Call Minutes
#  International SMS Count
#  OffPeak Data Usage Ratio

# Finding the value of k Elbow Method
# Run KMeans for different values of k and calculate inertia The elbow graph shows a clear bend at k  3

# Clusters k  3

#  Cluster 1  Heavy Data Users Use a large amount of mobile data but make fewer calls

#  Cluster 2  Calling Users Use less data but make many phone calls and send many SMS messages

#  Cluster 3  Night Users Use a moderate amount of data especially during offpeak hours

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#create dataset
X = np.array([[18,250,20,0.20],[22,280,18,0.18],[25,300,22,0.25],[20,260,15,0.22],[28,320,25,0.20],[24,290,19,0.24],[30,350,28,0.18],[26,310,21,0.23],[32,370,30,0.20],[27,330,24,0.21],[3,650,55,0.10],[5,720,60,0.08],[4,680,52,0.12],[6,750,65,0.09],[7,700,58,0.11],[3,620,50,0.13],[8,780,70,0.08],[5,690,62,0.10],[6,730,57,0.12],[4,660,54,0.11],[15,400,25,0.75],[18,420,30,0.82],[20,450,28,0.78],[16,380,24,0.80],[22,470,32,0.85],[14,390,26,0.72],[19,440,29,0.79],[17,410,27,0.83],[21,460,31,0.77],[16,430,25,0.81],[35,300,20,0.18],[2,800,75,0.07],[12,360,23,0.76],[29,340,22,0.19],[4,710,59,0.09],[18,405,28,0.84],[23,315,20,0.21],[6,760,68,0.08],[15,395,26,0.74],[31,380,25,0.22],[5,670,56,0.10],[20,425,29,0.80],[27,325,21,0.20],[7,740,64,0.09],[17,415,27,0.78],[33,360,24,0.19],[3,690,61,0.11],[19,445,30,0.82],[24,305,19,0.23],[5,730,66,0.08]])

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
customers = ["Aarav", "Aditi", "Rohan", "Priya", "Arjun", "Neha", "Rahul", "Sneha", "Vikram", "Pooja", "Karan", "Ananya", "Rajesh", "Kavita", "Amit", "Nisha", "Suresh", "Riya", "Manish", "Divya", "Akash", "Simran", "Nitin", "Pallavi", "Ravi", "Shreya", "Vivek", "Isha", "Sanjay", "Meera", "Harsh", "Komal", "Deepak", "Swati", "Yash", "Tanvi", "Prakash", "Anjali", "Mohit", "Payal", "Abhishek", "Kajal", "Rakesh", "Mansi", "Dhruv", "Sonal", "Pankaj", "Bhavna", "Kunal", "Radhika"]

for customer,data,label in zip(customers,X,labels):
    print(f"Name : {customer} data = {data} label = {label}")

#create chart
plt.scatter(labels,X[:,0],s=10)
plt.xticks(ticks=range(0,3),labels=range(0,3))
plt.ylabel("Monthly Data Usage GB")
plt.xlabel("Labels")
plt.show()