from sklearn.linear_model import LogisticRegression
import numpy as np

# Example data
X = np.array([[100, 12], [200, 24], [150, 6], [300, 36]])
y = np.array([0, 1, 0, 1])

model = LogisticRegression().fit(X, y)

features = list(map(float, input("Enter usage_minutes, contract_duration_months: ").split(",")))
pred = model.predict([features])[0]

print("Customer will churn." if pred else "Customer will NOT churn.")
