from sklearn.linear_model import LinearRegression
import numpy as np

# Example data (replace with your dataset)
X = np.array([[1000, 3], [1500, 4], [800, 2], [1200, 3]])
y = np.array([300000, 450000, 200000, 350000])

model = LinearRegression().fit(X, y)

features = list(map(float, input("Enter area, number_of_bedrooms: ").split(",")))
price = model.predict([features])[0]

print(f"Predicted price: ${price:.2f}")
