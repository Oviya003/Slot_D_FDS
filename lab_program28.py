from sklearn.cluster import KMeans
import numpy as np

# Example data
X = np.array([[5, 500], [15, 1500], [7, 700], [20, 2000]])
model = KMeans(n_clusters=2, random_state=0).fit(X)

features = list(map(float, input("Enter shopping_feature1, shopping_feature2: ").split(",")))
cluster = model.predict([features])[0]

print(f"Assigned to cluster {cluster}")
