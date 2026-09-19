#  Factory Machine Failure ModesScenario: An engineer wants to group individual machine breakdown incidents to find common root causes by linking the most similar failure metrics first.Input Features ($X$):$X_1$: Operating temperature at time of failure (in Celsius)$X_2$: Vibration frequency anomaly (in Hz)Target Variable ($Y$): Failure mode prototype (Cluster)Practice Goal: Use bottom-up clustering to merge incidents until 3 distinct types of machine failure modes are identified.

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering

from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram

# ============================================
# 1. Create machine failure dataset
# ============================================

data = {
    "Incident": [
        "M1", "M2", "M3",
        "M4", "M5", "M6",
        "M7", "M8", "M9",
        "M10", "M11", "M12"
    ],

    "Temperature": [
        85, 88, 90,
        60, 62, 58,
        110, 115, 112,
        82, 86, 89
    ],

    "VibrationFreq": [
        450, 470, 460,
        120, 130, 125,
        210, 220, 205,
        480, 465, 475
    ]
}

# create dataframe
df = pd.DataFrame(data)
# print(df)
#select input features
x = df[[
    "Temperature",
    "VibrationFreq",
]]

print(x)

#data scale
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
print(x_scaled)

ward_linkage = linkage(x_scaled, method='ward')

plt.figure(figsize=(10,12))
#create dendrogram 
dendrogram(ward_linkage, labels=df["Incident"].values)

plt.title("Hierarchical Clustering Dendrogram - Ward Method")
plt.xlabel("Data Points")
plt.ylabel("Euclidean Distance")
plt.show()

model = AgglomerativeClustering(n_clusters=3, linkage="ward")
model.fit_predict(x_scaled)

print(model.labels_)
df['clusters'] = model.labels_
print(df)

#create chart
plt.figure(figsize=(10,8))
plt.title("agglomerative hierarchical clustering")
plt.scatter(df['Temperature'], df['VibrationFreq'], c=df['clusters'])
plt.xlabel("Operating Temperature (°C)")
plt.ylabel("Vibration Frequency Anomaly (Hz)")
#add label for each and every circle
for index in range(len(df)):
    plt.annotate(df.loc[index, 'Incident'], (
        df.loc[index, 'Temperature'],
        df.loc[index, 'VibrationFreq']
    ), xytext=(5,5), textcoords="offset points")
plt.show()
exit()