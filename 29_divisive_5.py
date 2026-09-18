# Organizing a Broad E-commerce CatalogScenario: An online retailer wants to take a massive "All Products" inventory and repeatedly split it into finer sub-categories.Input Features ($X$):$X_1$: Product weight (in kg)$X_2$: Average retail price (in USD)Target Variable ($Y$): Department sub-category (Cluster)Practice Goal: Split the master product list iteratively to form 3 distinct department categories based on physical size and cost.

# ============================================================
# DIVISIVE HIERARCHICAL CLUSTERING
# Example: Organizing a Broad E-commerce Catalog
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
    "Product": [
        "Smart_Watch",
        "Wireless_Earbuds",
        "Smartphone",
        "Gaming_Laptop",
        "4K_Smart_TV",
        "Washing_Machine",
        "Refrigerator",
        "Cotton_TShirt",
        "Ceramic_Mug",
        "Water_Bottle",
        "Notebook_Pack",
        "Ballpoint_Pens"
    ],

    # X1: Product weight (in kg)
    "Product_Weight": [0.05, 0.04, 0.18, 2.40, 15.50, 68.00, 85.00, 0.20, 0.35, 0.30, 0.45, 0.08],

    # X2: Average retail price (in USD)
    "Retail_Price": [250, 130, 899, 1450, 750, 620, 1100, 22, 12, 18, 15, 6]
}

# create dataframe
df = pd.DataFrame(data)
# print(df)


# ============================================================
# Step 3: Select input features
# ============================================================

X = df[
    [
        "Product_Weight",
        "Retail_Price",
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
# Step 6: Apply Divisive Clustering (Split into 3 Departments)
# ============================================================

clusters = devisive_clustering(
    X_scaled,
    df["Product"].to_list(),
    3
)

print("Clusters dictionary:", clusters)


# ============================================================
# Step 7: Display cluster id and product name
# ============================================================

for cluster_id, indexes in clusters.items():

    print("Cluster",cluster_id)

    for index in indexes:

        print(df.loc[index,"Product"])


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
    df["Product_Weight"],
    df["Retail_Price"],
    c=df["cluster"],
    cmap="viridis",
    s=100
)

# Add product names to the graph
for i in range(len(df)):

    plt.annotate(
        df.loc[i, "Product"],
        (
            df.loc[i, "Product_Weight"],
            df.loc[i, "Retail_Price"]
        ),
        xytext=(6, 6),
        textcoords="offset points",
        fontsize=9
    )

plt.xlabel("Product Weight (kg)")
plt.ylabel("Average Retail Price (USD)")
plt.title("Divisive Clustering for E-commerce Catalog (Target = 3 Departments)")

plt.show()