# Exercise 1.2: Credit Card Fraud and Erratic Spending Anomaly Detection
# Task Type: Clustering / Anomaly Detection
# Business Problem: Group cardholders by spending behavior (cash advance frequency, credit limit utilization, payment ratios) and flag isolated noise points (label = -1) for fraud review.
# Portfolio Value: Shows recruiters how to detect novel fraud patterns when labeled fraud data is unavailable.
# Dataset Name: Credit Card Dataset for Clustering (Kaggle)
# Dataset Link: https://www.kaggle.com/datasets/arjunbhasin2013/ccdata



import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import DBSCAN

# 1. Download Credit Card data
url = "https://raw.githubusercontent.com/RAHULKASHYAP02/Credit-Card-Segmentation/master/CC%20GENERAL.csv"

# load data
df = pd.read_csv(url)

# filter column
X = df[
    ["CASH_ADVANCE_FREQUENCY",
        "CREDIT_LIMIT",
        "PRC_FULL_PAYMENT"
    ]
]

# remove blank rows
X = X.dropna()
print(len(X))
print(X.head(20))

# create model
model = DBSCAN(min_samples=10, eps=0.5)

# train model
model.fit_predict(X)

labels = model.labels_

# add labels into dataframe
X['labels'] = labels

print("Cluster wise count")
print(X['labels'].value_counts())
print(X.head(20))

# create scatter plot
plt.figure(figsize=(10,8))

# create chart
plt.scatter(X['CASH_ADVANCE_FREQUENCY'],
            X['CREDIT_LIMIT'],
            c=X['labels'], s=10)

plt.title("Credit Card Fraud and Erratic Spending Anomaly Detection")
plt.xlabel("Cash Advance Frequency")
plt.ylabel("Credit Limit")
plt.grid(True)
plt.show()
