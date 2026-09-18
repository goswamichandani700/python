#  Codebase Microservices RefactoringScenario: A software architect needs to break down a giant monolithic application into smaller microservices by separating distinct functional modules.Input Features ($X$):$X_1$: Number of shared database tables utilized$X_2$: Frequency of cross-module API calls per minuteTarget Variable ($Y$): Microservice boundary (Cluster)Practice Goal: Partition the monolith top-down into 2 independent microservices with minimal overlap.

# ============================================================
# DIVISIVE HIERARCHICAL CLUSTERING
# Example: Codebase Microservices Refactoring
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
    "Module": [
        "Auth_Module",
        "User_Profile",
        "Session_Manager",
        "Role_Permission",
        "Payment_Gateway",
        "Invoice_Billing",
        "Order_Checkout",
        "Subscription_Engine"
    ],

    # X1: Number of shared database tables utilized
    "Shared_DB_Tables": [12, 14, 11, 13, 2, 3, 1, 2],

    # X2: Frequency of cross-module API calls per minute
    "Cross_API_Calls": [150, 160, 145, 155, 20, 25, 15, 30]
}

# create dataframe
df = pd.DataFrame(data)
# print(df)


# ============================================================
# Step 3: Select input features
# ============================================================

X = df[
    [
        "Shared_DB_Tables",
        "Cross_API_Calls",
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

def devisive_clustering(X, items, no_of_clusters=2):

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
# Step 6: Apply Divisive Clustering (Split into 2 Microservices)
# ============================================================

clusters = devisive_clustering(
    X_scaled,
    df["Module"].to_list(),
    2
)

print("Clusters dictionary:", clusters)


# ============================================================
# Step 7: Display cluster id and module name
# ============================================================

for cluster_id, indexes in clusters.items():

    print(f"\nMicroservice Cluster {cluster_id}:")

    for index in indexes:

        print(f" - {df.loc[index, 'Module']}")


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
    df["Shared_DB_Tables"],
    df["Cross_API_Calls"],
    c=df["cluster"],
    cmap="viridis",
    s=100
)

# Add module names to the graph
for i in range(len(df)):

    plt.annotate(
        df.loc[i, "Module"],
        (
            df.loc[i, "Shared_DB_Tables"],
            df.loc[i, "Cross_API_Calls"]
        ),
        xytext=(6, 6),
        textcoords="offset points",
        fontsize=9
    )

plt.xlabel("Number of Shared DB Tables Utilized")
plt.ylabel("Frequency of Cross-Module API Calls / min")
plt.title("Divisive Clustering for Microservices Refactoring (Target = 2 Services)")

plt.show()