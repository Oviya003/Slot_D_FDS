import pandas as pd
from sklearn.linear_model import LinearRegression

house_data = pd.read_csv("house_data.csv")
X = house_data[['size']]
y = house_data['price']
model = LinearRegression().fit(X, y)
print("House Price Prediction (Size)")
print("Coefficient:", model.coef_[0])
print("Intercept:", model.intercept_)