#  Healthcare Patient Risk Grouping

# Features 3

#  Systolic Blood Pressure mmHg
#  Fasting Blood Glucose mgdL
#  LDL Cholesterol mgdL

# Finding the value of k
# For this example we use k  3 because patients can be divided into three simple groups Low Risk Medium Risk and High Risk

# Clusters k  3

#  Cluster 1  Low Risk Normal blood pressure normal glucose level and low LDL cholesterol

#  Cluster 2  Medium Risk Slightly high blood pressure increased glucose level and high LDL cholesterol

#  Cluster 3  High Risk High blood pressure very high glucose level and very high LDL cholesterol


import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#create dataset
X = np.array([[118,88,85],[120,90,90],[115,85,82],[122,92,88],[119,87,84],[117,86,80],[121,89,86],[116,84,81],[123,91,89],[120,88,87],[135,105,125],[138,110,130],[132,102,120],[140,108,135],[136,104,128],[134,100,122],[142,112,138],[130,98,118],[137,106,132],[133,101,124],[160,145,180],[168,155,195],[172,160,210],[165,150,185],[175,165,220],[162,148,190],[180,170,230],[158,142,175],[170,158,205],[177,168,215],[119,89,86],[136,103,127],[164,152,188],[121,91,92],[139,109,134],[166,154,200],[116,83,79],[131,97,116],[173,162,218],[120,86,83],[141,111,136],[159,145,178],[135,102,121],[169,157,208],[118,87,85],[178,169,225],[129,95,110],[163,149,192],[143,113,140],[171,159,212]])

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
patients = ["Aarav", "Aditi", "Rohan", "Priya", "Arjun", "Neha", "Rahul", "Sneha", "Vikram", "Pooja", "Karan", "Ananya", "Rajesh", "Kavita", "Amit", "Nisha", "Suresh", "Riya", "Manish", "Divya", "Akash", "Simran", "Nitin", "Pallavi", "Ravi", "Shreya", "Vivek", "Isha", "Sanjay", "Meera", "Harsh", "Komal", "Deepak", "Swati", "Yash", "Tanvi", "Prakash", "Anjali", "Mohit", "Payal", "Abhishek", "Kajal", "Rakesh", "Mansi", "Dhruv", "Sonal", "Pankaj", "Bhavna", "Kunal", "Radhika"]

for patient,data,label in zip(patients,X,labels):
    print(f"Name : {patient} data = {data} label = {label}")

#create chart
plt.scatter(labels,X[:,0],s=10)
plt.xticks(ticks=range(0,3),labels=range(0,3))
plt.ylabel("Systolic Blood Pressure")
plt.xlabel("Labels")
plt.show()