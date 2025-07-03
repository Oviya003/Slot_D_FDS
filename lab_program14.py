import pandas as pd
data = {
    'CustomerID': [101, 102, 103, 104, 105, 106, 107, 108],
    'Age': [25, 30, 22, 25, 30, 40, 22, 25],
    'PurchaseAmount': [200, 150, 180, 210, 160, 300, 190, 220]
}
df = pd.DataFrame(data)
age_frequency = df['Age'].value_counts().sort_index()
print("Frequency distribution of customer ages:")
print(age_frequency)
