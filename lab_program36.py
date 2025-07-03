import pandas as pd

# Load stock price data
stock_data = pd.read_csv("stock_data.csv")

# Calculate standard deviation of closing prices
std_dev = stock_data['closing_price'].std()

# Output
print("Stock Price Variability")
print("Standard Deviation:", std_dev)
