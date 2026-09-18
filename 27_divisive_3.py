# Supply Chain Logistics HubsScenario: A national delivery company wants to split a massive country-wide delivery zone into smaller, localized fulfillment regions to reduce shipping times.Input Features ($X$):$X_1$: Delivery coordinate (Latitude)$X_2$: Delivery coordinate (Longitude)Target Variable ($Y$): Assigned localized logistics region (Cluster)Practice Goal: Divide the entire national map top-down into 3 sub-regions by continually splitting the cluster with the highest spatial variance.


# ============================================================
# DIVISIVE HIERARCHICAL CLUSTERING
# Example: Supply Chain Logistics Hubs
# ============================================================

# Step 1: Import required libraries
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler


# ============================================================
# Step 2: Create the dataset
# ============================================================

data = {
    "Delivery": [
        "Delivery1",
        "Delivery2",
        "Delivery3",
        "Delivery4",
        "Delivery5",
        "Delivery6",
        "Delivery7",
        "Delivery8",
        "Delivery9",
        "Delivery10",
        "Delivery11",
        "Delivery12"
    ],

    # Delivery coordinate Latitude
    "Latitude": [
        28.61,
        28.70,
        28.55,
        28.65,
        19.07,
        19.12,
        19.00,
        18.95,
        12.97,
        13.05,
        12.90,
        13.10
    ],

    # Delivery coordinate Longitude
    "Longitude": [
        77.20,
        77.10,
        77.25,
        77.30,
        72.88,
        72.95,
        72.85,
        73.00,
        77.59,
        77.65,
        77.55,
        77.70
    ]
}


# create dataframe
df = pd.DataFrame(data)
# print(df)


# ============================================================
# Step 3: Select input features
# ============================================================

X = df[
    [
        "Latitude",
        "Longitude",
    ]
]


# ============================================================
# Step 4: Scaling
# ============================================================

scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# print(X_scaled)


# ============================================================
# Step 5: Divisive Clustering Function
# ============================================================

def devisive_clustering(X, deliveries, no_of_clusters=3):

    clusters = {
        0: list(range(len(deliveries)))
    }

    next_key = 1

    while len(clusters) < no_of_clusters:

        # findout key with maximum sized list
        max_key = max(
            clusters,
            key=lambda cluster_id: len(clusters[cluster_id])
        )

        # get indexes
        indexes = clusters[max_key]

        # get data
        data = X[indexes]

        # create model
        model = KMeans(
            n_clusters=2,
            random_state=2,
            n_init=10
        )

        model.fit_predict(data)

        labels = model.labels_

        list_1 = []
        list_2 = []

        for index, label in zip(indexes, labels):

            if label == 0:
                list_1.append(index)

            else:
                list_2.append(index)

        clusters[next_key] = list_1
        next_key = next_key + 1

        clusters[next_key] = list_2
        next_key = next_key + 1

        del clusters[max_key]

    return clusters


# ============================================================
# Step 6: Apply Divisive Clustering
# ============================================================

clusters = devisive_clustering(
    X_scaled,
    df["Delivery"].to_list(),
    3
)

print(clusters)


# ============================================================
# Step 7: Display cluster id and delivery name
# ============================================================

for cluster_id, indexes in clusters.items():

    print(cluster_id)

    for index in indexes:

        print(df.loc[index, "Delivery"])


# ============================================================
# Step 8: Add cluster into original dataframe
# ============================================================

df["cluster"] = 0

# add data into original dataframe
for cluster_id, indexes in clusters.items():

    print(cluster_id)

    for index in indexes:

        df.loc[index, "cluster"] = cluster_id


print(df)


# ============================================================
# Step 9: Plot the clusters
# ============================================================

plt.figure(figsize=(10, 6))

plt.scatter(
    df["Longitude"],
    df["Latitude"],
    c=df["cluster"],
    s=100
)


# Add delivery names to the graph
for i in range(len(df)):

    plt.annotate(
        df.loc[i, "Delivery"],
        (
            df.loc[i, "Longitude"],
            df.loc[i, "Latitude"]
        ),
        xytext=(5, 5),
        textcoords="offset points"
    )


plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Divisive Clustering of Supply Chain Logistics Hubs")

plt.show()