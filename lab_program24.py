from sklearn.neighbors import KNeighborsClassifier
import numpy as np

X = np.array([[1,0,3],[2,1,0],[0,1,1],[3,0,2],[2,2,1],[0,0,0]])
y = np.array([1,0,0,1,1,0])

k = int(input("Enter k: "))
knn = KNeighborsClassifier(n_neighbors=k)
knn.fit(X, y)

features = np.array([float(x) for x in input("Enter features (comma separated): ").split(",")]).reshape(1, -1)
print("Patient has condition." if knn.predict(features)[0] else "Patient does NOT have condition.")
