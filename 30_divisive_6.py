# Network Traffic Anomaly SegregationScenario: A cybersecurity system logs all incoming server traffic as one large dataset and needs to split it sequentially to isolate normal traffic from distinct types of DDoS attacks.Input Features ($X$):$X_1$: Requests per second from source IP$X_2$: Average packet size (in bytes)Target Variable ($Y$): Traffic classification group (Cluster)Practice Goal: Isolate malicious traffic by continuously splitting the most anomalous subgroups top-down until the "normal" baseline is separated from the attacks.

# ============================================================
# DIVISIVE HIERARCHICAL CLUSTERING
# Example: Network Traffic Anomaly Segregation
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
    "Traffic_Source": [
        "Normal_User_1",
        "Normal_User_2",
        "Normal_User_3",
        "Normal_User_4",
        "Normal_User_5",
        "HTTP_Flood_Bot_1",
        "HTTP_Flood_Bot_2",
        "HTTP_Flood_Bot_3",
        "UDP_Amplification_1",
        "UDP_Amplification_2",
        "UDP_Amplification_3"
    ],

    # X1: Requests per second from source IP
    "Requests_Per_Sec": [15, 22, 18, 30, 25, 1200, 1350, 1100, 850, 920, 890],

    # X2: Average packet size (in bytes)
    "Avg_Packet_Size": [512, 480, 530, 600, 450, 128, 115, 140, 1450, 1480, 1420]
}

# create dataframe
df = pd.DataFrame(data)
# print(df)


# ============================================================
# Step 3: Select input features
# ============================================================

X = df[
    [
        "Requests_Per_Sec",
        "Avg_Packet_Size",
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

def devisive_clustering(X, items, no_of_clusters=3):

    clusters = {
        0: list(range(len(items)))
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
            random_state=42,
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
# Step 6: Apply Divisive Clustering (Split into 3 Traffic Groups)
# ============================================================

clusters = devisive_clustering(
    X_scaled,
    df["Traffic_Source"].to_list(),
    3
)

print("Clusters dictionary:", clusters)


# ============================================================
# Step 7: Display cluster id and traffic source name
# ============================================================

for cluster_id, indexes in clusters.items():

    print(f"\nTraffic Cluster {cluster_id}:")

    for index in indexes:

        print(f" - {df.loc[index, 'Traffic_Source']}")


# ============================================================
# Step 8: Add cluster into original dataframe
# ============================================================

df["cluster"] = 0

# add data into original dataframe
for cluster_id, indexes in clusters.items():

    for index in indexes:

        df.loc[index, "cluster"] = cluster_id

print("\nFinal Dataframe:")
print(df)


# ============================================================
# Step 9: Plot the clusters
# ============================================================

plt.figure(figsize=(10, 6))

plt.scatter(
    df["Requests_Per_Sec"],
    df["Avg_Packet_Size"],
    c=df["cluster"],
    cmap="viridis",
    s=100
)

# Add traffic source names to the graph
for i in range(len(df)):

    plt.annotate(
        df.loc[i, "Traffic_Source"],
        (
            df.loc[i, "Requests_Per_Sec"],
            df.loc[i, "Avg_Packet_Size"]
        ),
        xytext=(6, 6),
        textcoords="offset points",
        fontsize=9
    )

plt.xlabel("Requests per Second (RPS)")
plt.ylabel("Average Packet Size (Bytes)")
plt.title("Divisive Clustering for Network Traffic Anomaly Segregation (Target = 3 Groups)")

plt.show()