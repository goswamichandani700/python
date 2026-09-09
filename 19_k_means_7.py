# Cybersecurity Network Traffic Grouping

# Features 3

#  Packet Frequency packetssec
#  Average Packet Size bytes
#  Unique Destination IP Ratio

# Finding the value of k
# We choose k  3 to separate normal network traffic from two common types of unusual traffic

# Clusters k  3

#  Cluster 1  Normal Traffic Normal packet frequency with different packet sizes and normal IP usage

#  Cluster 2  Port Scanning Many packets are sent to different IP addresses usually with small and similar packet sizes

#  Cluster 3  Heavy Data Transfer Large packets are sent repeatedly usually to one main destination

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#create dataset
X = np.array([[12,450,0.25],[15,520,0.30],[18,600,0.28],[20,480,0.35],[22,550,0.32],[25,620,0.30],[28,700,0.27],[30,580,0.33],[32,650,0.31],[35,720,0.29],[14,490,0.24],[17,560,0.29],[21,610,0.34],[24,530,0.31],[27,680,0.28],[31,590,0.32],[34,640,0.30],[36,750,0.27],[19,510,0.35],[23,570,0.33],[420,60,0.92],[480,55,0.95],[520,70,0.91],[600,65,0.94],[680,75,0.96],[750,58,0.93],[820,80,0.97],[900,62,0.95],[470,68,0.90],[550,72,0.94],[630,60,0.96],[710,78,0.92],[790,66,0.98],[850,74,0.95],[920,59,0.93],[500,63,0.91],[670,69,0.96],[760,61,0.94],[880,77,0.97],[950,64,0.92],[45,1400,0.08],[50,1600,0.10],[55,1800,0.07],[60,1500,0.09],[65,2000,0.06],[70,1700,0.08],[75,2200,0.05],[80,1900,0.07],[85,2100,0.06],[90,2300,0.05]])

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
customers = ["Aarav","Vivaan","Aditya","Arjun","Rohan","Krish","Ishaan","Kabir","Aryan","Vihaan","Rahul","Raj","Dev","Yash","Dhruv","Kunal","Aman","Harsh","Nikhil","Manav","Anaya","Diya","Ira","Myra","Sara","Kiara","Riya","Avni","Tara","Meera","Aanya","Pihu","Navya","Siya","Aadhya","Pari","Anika","Ishita","Mahi","Kavya","Jay","Rajesh","Mihir","Nirav","Bhavin","Parth","Meet","Yug","Darsh","Devansh"]

for customer,spending,label in zip(customers,X.flatten(),labels):
    print(f"Name : {customer} spending score = {spending} label = {label}")

#create chart
plt.scatter(labels,X[:,0],s=10)
plt.xticks(ticks=range(0,3),labels=range(0,3))
plt.ylabel("Packet Frequency")
plt.xlabel("Labels")
plt.show()