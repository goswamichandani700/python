#  City Neighborhood ZoningScenario: A city planner wants to group adjacent small blocks into larger municipal zones based on crime rates and property values.Input Features ($X$):$X_1$: Median property value (in thousands of dollars)$X_2$: Crime incidents per 1,000 residentsTarget Variable ($Y$): Assigned municipal zone (Cluster)Practice Goal: Merge similar blocks bottom-up until 2 distinct zones emerge, representing "High-Value/Low-Crime" and "Low-Value/High-Crime" areas.

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering

from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram

# ============================================
# 1. Create neighborhood dataset
# ============================================

data = {
    "Block": [
        "B1", "B2", "B3",
        "B4", "B5", "B6",
        "B7", "B8", "B9",
        "B10", "B11", "B12"
    ],

    "PropertyValue": [
        350, 380, 410,
        120, 140, 130,
        450, 480, 500,
        150, 160, 180
    ],

    "CrimeRate": [
        12, 10, 8,
        65, 70, 68,
        5, 4, 6,
        55, 58, 52
    ]
}

# create dataframe
df = pd.DataFrame(data)
# print(df)
#select input features
x = df[[
    "PropertyValue",
    "CrimeRate",
]]

print(x)

#data scale
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
print(x_scaled)

ward_linkage = linkage(x_scaled, method='ward')

plt.figure(figsize=(10,12))
#create dendrogram 
dendrogram(ward_linkage, labels=df["Block"].values)

plt.title("Hierarchical Clustering Dendrogram - Ward Method")
plt.xlabel("Data Points")
plt.ylabel("Euclidean Distance")
plt.show()

model = AgglomerativeClustering(n_clusters=2, linkage="ward")
model.fit_predict(x_scaled)

print(model.labels_)
df['clusters'] = model.labels_
print(df)

#create chart
plt.figure(figsize=(10,8))
plt.title("agglomerative hierarchical clustering")
plt.scatter(df['PropertyValue'], df['CrimeRate'], c=df['clusters'])
plt.xlabel("Property Value ($k)")
plt.ylabel("Crime Incidents (per 1k residents)")
#add label for each and every circle
for index in range(len(df)):
    plt.annotate(df.loc[index, 'Block'], (
        df.loc[index, 'PropertyValue'],
        df.loc[index, 'CrimeRate']
    ), xytext=(5,5), textcoords="offset points")
plt.show()
exit()