import pandas as pd

# Load temperature data
temp_data = pd.read_csv("city_temperature.csv")

# Group by city and calculate statistics
grouped = temp_data.groupby('city')['temperature']
mean_temp = grouped.mean()
std_temp = grouped.std()
range_temp = grouped.max() - grouped.min()

# Output statistics
print("Temperature Statistics")
print("\nMean Temperature:\n", mean_temp)
print("\nStandard Deviation:\n", std_temp)
print("\nTemperature Range:\n", range_temp)
print("\nMost Consistent City (Lowest Std Dev):", std_temp.idxmin())
print("City with Highest Temperature Range:", range_temp.idxmax())
