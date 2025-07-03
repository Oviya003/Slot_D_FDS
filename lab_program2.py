import numpy as np
sales_data = np.array([
    [100, 120, 110],  
    [90, 95, 85],     
    [130, 125, 140]   
])
average_price = np.mean(sales_data)
print(f"Average price of all products sold: {average_price:.3f}")

