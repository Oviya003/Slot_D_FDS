from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()
X, y = iris.data, iris.target
model = DecisionTreeClassifier().fit(X, y)

features = list(map(float, input("Enter sepal_length, sepal_width, petal_length, petal_width: ").split(",")))
pred = model.predict([features])[0]

print(f"Predicted species: {iris.target_names[pred]}")
