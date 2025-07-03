import pandas as pd
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt

customer_data = pd.read_csv("customer_segmentation.csv")
X = customer_data[['total_spent', 'visits']]
model = KMeans(n_clusters=3, random_state=42).fit(X)
customer_data['segment'] = model.labels_

plt.scatter(X['total_spent'], X['visits'], c=model.labels_, cmap='viridis')
plt.xlabel('Total Spent')
plt.ylabel('Visits')
plt.title('Customer Segmentation')
plt.show()
