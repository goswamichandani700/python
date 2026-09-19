#  Genomic Sequence GroupingScenario: A biologist has individual DNA samples and wants to construct a phylogenetic tree by pairing the most genetically similar sequences step-by-step.Input Features ($X$):$X_1$: Genetic Marker A expression level$X_2$: Genetic Marker B expression levelTarget Variable ($Y$): Phylogenetic clade (Cluster)Practice Goal: Group samples bottom-up using Ward's linkage to find the evolutionary branches of the samples.

import pandas as pd
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import AgglomerativeClustering

from scipy.cluster.hierarchy import linkage
from scipy.cluster.hierarchy import dendrogram

# ============================================
# 1. Create DNA sample dataset
# ============================================

data = {
    "Sample": [
        "S1", "S2", "S3",
        "S4", "S5", "S6",
        "S7", "S8", "S9",
        "S10", "S11", "S12"
    ],

    "Marker_A": [
        2.1, 2.4, 2.0,
        7.8, 8.2, 8.0,
        14.5, 15.1, 14.8,
        3.0, 3.2, 2.9
    ],

    "Marker_B": [
        9.5, 9.1, 9.8,
        4.2, 4.5, 4.0,
        1.2, 1.0, 1.5,
        8.8, 8.5, 8.9
    ]
}

# create dataframe
df = pd.DataFrame(data)
# print(df)
#select input features
x = df[[
    "Marker_A",
    "Marker_B",
]]

print(x)

#data scale
scaler = StandardScaler()
x_scaled = scaler.fit_transform(x)
print(x_scaled)

ward_linkage = linkage(x_scaled, method='ward')

plt.figure(figsize=(10,12))
#create dendrogram 
dendrogram(ward_linkage, labels=df["Sample"].values)

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
plt.scatter(df['Marker_A'], df['Marker_B'], c=df['clusters'])
plt.xlabel("Marker A Expression")
plt.ylabel("Marker B Expression")
#add label for each and every circle
for index in range(len(df)):
    plt.annotate(df.loc[index, 'Sample'], (
        df.loc[index, 'Marker_A'],
        df.loc[index, 'Marker_B']
    ), xytext=(5,5), textcoords="offset points")
plt.show()
exit()