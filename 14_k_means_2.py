#  ECommerce  Retail Customer Segmentation

# Features 3

#  Annual Spending 
#  Purchase Frequency ordersyear
#  Average Return Rate 

# Finding the value of k Elbow Method
# First standardize all three features using zscore Then run KMeans for k  1 to 8 and calculate WCSS From the elbow graph a clear bend can be seen at k  4

# Clusters k  4

#  Cluster 1  VIP Customers Spend a lot purchase frequently and have a low return rate

#  Cluster 2  HighRisk Customers Spend a lot but return many products

#  Cluster 3  Regular Budget Customers Spend less but purchase frequently and usually keep their products

#  Cluster 4  Occasional Customers Spend less and purchase only a few times

import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

#create dataset
X = np.array([[85000,45,5],[92000,50,4],[78000,42,6],[88000,48,5],[95000,55,3],[82000,44,5],[90000,52,4],[87000,47,6],[98000,58,3],[91000,51,4],[90000,40,32],[95000,45,35],[88000,42,30],[102000,48,38],[97000,44,34],[85000,39,31],[110000,52,40],[93000,43,33],[99000,46,36],[87000,41,29],[35000,35,5],[42000,40,6],[38000,37,4],[45000,42,5],[30000,32,7],[48000,45,4],[40000,38,6],[46000,41,5],[33000,34,6],[44000,39,4],[25000,8,8],[18000,6,10],[32000,10,7],[22000,7,9],[28000,9,6],[15000,5,8],[35000,12,7],[20000,6,9],[30000,11,5],[27000,8,7],[83000,46,5],[94000,53,4],[37000,36,5],[29000,9,8],[89000,49,4],[41000,40,5],[23000,7,9],[96000,54,3],[34000,33,6],[26000,8,7]])

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
customers = ["Aarav", "Aditi", "Rohan", "Priya", "Arjun", "Neha", "Rahul", "Sneha", "Vikram", "Pooja", "Karan", "Ananya", "Rajesh", "Kavita", "Amit", "Nisha", "Suresh", "Riya", "Manish", "Divya", "Akash", "Simran", "Nitin", "Pallavi", "Ravi", "Shreya", "Vivek", "Isha", "Sanjay", "Meera", "Harsh", "Komal", "Deepak", "Swati", "Yash", "Tanvi", "Prakash", "Anjali", "Mohit", "Payal", "Abhishek", "Kajal", "Rakesh", "Mansi", "Dhruv", "Sonal", "Pankaj", "Bhavna", "Kunal", "Radhika"]

for customer,data,label in zip(customers,X,labels):
    print(f"Name : {customer} data = {data} label = {label}")

#create chart
plt.scatter(labels,X[:,0],s=10)
plt.xticks(ticks=range(0,4),labels=range(0,4))
plt.ylabel("Annual Spending")
plt.xlabel("Labels")
plt.show()