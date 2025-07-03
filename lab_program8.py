import pandas as pd
df = pd.read_csv('sales_data.csv')
top_5 = df.groupby('product_name')['quantity_sold'].sum().sort_values(ascending=False).head(5)
print(top_5)
