import pandas as pd
order_data = pd.read_csv('order_data.csv')  
order_data['order_date'] = pd.to_datetime(order_data['order_date'])
orders_per_customer = order_data.groupby('customer_id').size()
average_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()
earliest_date = order_data['order_date'].min()
latest_date = order_data['order_date'].max()
print("Orders per customer:\n", orders_per_customer)
print("\nAverage quantity per product:\n", average_quantity_per_product)
print("\nEarliest order date:", earliest_date)
print("Latest order date:", latest_date)

