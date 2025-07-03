import pandas as pd
data = {
    'property ID': [101, 102, 103, 104, 105],
    'location': ['Downtown', 'Suburb', 'Downtown', 'Suburb', 'Countryside'],
    'number of bedrooms': [3, 5, 4, 6, 2],
    'area in square feet': [1200, 2500, 1600, 3000, 1100],
    'listing price': [250000, 450000, 300000, 500000, 200000]
}
property_data = pd.DataFrame(data)
average_price_per_location = property_data.groupby('location')['listing price'].mean()
print("1. Average listing price per location:")
print(average_price_per_location)
print()
num_properties_gt_4_bedrooms = property_data[property_data['number of bedrooms'] > 4].shape[0]
print("2. Number of properties with more than 4 bedrooms:", num_properties_gt_4_bedrooms)
print()
largest_area_property = property_data.loc[property_data['area in square feet'].idxmax()]
print("3. Property with the largest area:")
print(largest_area_property)
