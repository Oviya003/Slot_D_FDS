from sklearn.tree import DecisionTreeRegressor
import numpy as np

# Example data: mileage (k km), age (years), brand_encoded
X = np.array([[50, 3, 1], [80, 5, 2], [30, 2, 1], [100, 7, 3]])
y = np.array([15000, 12000, 17000, 9000])

model = DecisionTreeRegressor().fit(X, y)

features = list(map(float, input("Enter mileage_km, age_years, brand_encoded: ").split(",")))
pred_price = model.predict([features])[0]

# Get decision path
node_indicator = model.decision_path([features])
feature = model.tree_.feature
threshold = model.tree_.threshold

print(f"Predicted price: ${pred_price:.2f}")
print("Decision path:")
node_index = node_indicator.indices[node_indicator.indptr[0]:node_indicator.indptr[1]]
for node_id in node_index:
    if feature[node_id] != -2:
        feat = features[feature[node_id]]
        thresh = threshold[node_id]
        condition = "<=" if feat <= thresh else ">"
        print(f"Node {node_id}: feature[{feature[node_id]}] = {feat} {condition} {thresh:.2f}")
