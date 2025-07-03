import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Load retail data
retail_data = pd.read_csv("retail_data.csv")

# Clustering based on total spent and visit frequency
X = retail_data[['total_spent', 'visit_freq']]
model = KMeans(n_clusters=2, random_state=42).fit(X)
retail_data['segment'] = model.labels_

# Plotting the clusters
plt.scatter(X['total_spent'], X['visit_freq'], c=model.labels_, cmap='plasma')
plt.title("Retail Customer Clusters")
plt.xlabel("Total Spent")
plt.ylabel("Visit Frequency")
plt.grid(True)
plt.show()
