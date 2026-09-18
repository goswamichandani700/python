# Macro-Market SplittingScenario: A global streaming service wants to divide its single massive global user base into distinct regional cohorts by repeatedly splitting the largest, most diverse groups.Input Features ($X$):$X_1$: Average daily watch time (in minutes)$X_2$: Preference score for localized content (1-10)Target Variable ($Y$): Regional cohort grouping (Cluster)Practice Goal: Start with all users in one cluster and split them top-down to find 2 highly cohesive viewer markets.

# ============================================================
# DIVISIVE HIERARCHICAL CLUSTERING
# Example: Macro-Market Splitting
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
    "User": [
        "User1",
        "User2",
        "User3",
        "User4",
        "User5",
        "User6",
        "User7",
        "User8",
        "User9",
        "User10",
        "User11",
        "User12"
    ],

    # Average daily watch time in minutes
    "Watch_time": [
        45,
        50,
        55,
        60,
        48,
        52,
        120,
        130,
        140,
        125,
        135,
        145
    ],

    # Preference score for localized content (1-10)
    "Localized_content": [
        2,
        3,
        2,
        4,
        3,
        2,
        8,
        9,
        8,
        10,
        9,
        8
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
        "Watch_time",
        "Localized_content",
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

def devisive_clustering(X, users, no_of_clusters=2):

    clusters = {
        0: list(range(len(users)))
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
    df["User"].to_list(),
    2
)

print(clusters)


# ============================================================
# Step 7: Display cluster id and user name
# ============================================================

for cluster_id, indexes in clusters.items():

    print(cluster_id)

    for index in indexes:

        print(df.loc[index, "User"])


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
    df["Watch_time"],
    df["Localized_content"],
    c=df["cluster"],
    s=100
)


# Add user names to the graph
for i in range(len(df)):

    plt.annotate(
        df.loc[i, "User"],
        (
            df.loc[i, "Watch_time"],
            df.loc[i, "Localized_content"]
        ),
        xytext=(5, 5),
        textcoords="offset points"
    )


plt.xlabel("Average Daily Watch Time (Minutes)")
plt.ylabel("Localized Content Preference (1-10)")
plt.title("Divisive Clustering of Streaming Users")

plt.show()