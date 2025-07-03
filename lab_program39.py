import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load data
data = pd.read_csv("customer_transactions.csv")  # Ensure this file exists in your directory

# Extract relevant features
X = data[['total_spent', 'items_purchased']]

# Build KMeans model
k = 3  # Number of clusters
model = KMeans(n_clusters=k, random_state=42)
data['cluster'] = model.fit_predict(X)

# Plotting the clusters
plt.figure(figsize=(8, 6))
colors = ['red', 'green', 'blue']
for i in range(k):
    cluster_data = data[data['cluster'] == i]
    plt.scatter(cluster_data['total_spent'], cluster_data['items_purchased'],
                label=f'Cluster {i}', color=colors[i])

plt.xlabel('Total Amount Spent')
plt.ylabel('Number of Items Purchased')
plt.title('Customer Segmentation using K-Means')
plt.legend()
plt.grid(True)
plt.show()
