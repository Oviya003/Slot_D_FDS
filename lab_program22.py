import pandas as pd
from scipy.stats import sem, t

df = pd.read_csv('customer_reviews.csv')
ratings = df['rating']
n = len(ratings)
mean = ratings.mean()
margin = sem(ratings) * t.ppf(0.975, n - 1)  # 95% CI

print(f"Count: {n}\nMean: {mean:.3f}\n95% CI: [{mean - margin:.3f}, {mean + margin:.3f}]")
