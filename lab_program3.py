import numpy as np
house_data = np.genfromtxt('house_data.csv', delimiter=',', skip_header=1)
filtered_data = house_data[house_data[:, 0] > 4]
sale_prices = filtered_data[:, 2]
average_price = np.mean(sale_prices)
print("Average sale price of houses with more than 4 bedrooms:", average_price)
