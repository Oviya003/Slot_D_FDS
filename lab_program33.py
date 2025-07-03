import pandas as pd
from sklearn.linear_model import LinearRegression

# Load car data
car_data = pd.read_csv("car_data.csv")

# Features and target
X = car_data[['engine_size', 'horsepower', 'fuel_efficiency']]
y = car_data['price']

# Train model
model = LinearRegression().fit(X, y)

# Output model performance
print("Car Price Prediction")
print("Score:", model.score(X, y))
