import pandas as pd
from scipy import stats

# Load the dataset
df = pd.read_csv("ab_test_conversion_data.csv")

# Split into two groups
group_a = df[df["Design"] == "A"]["ConversionRate"]
group_b = df[df["Design"] == "B"]["ConversionRate"]

# Perform independent two-sample t-test (assuming unequal variances)
t_stat, p_value = stats.ttest_ind(group_a, group_b, equal_var=False)

# Print results
print(f"T-statistic: {t_stat:.4f}")
print(f"P-value: {p_value:.4f}")

# Interpretation
alpha = 0.05
if p_value < alpha:
    print("Conclusion: There is a statistically significant difference in the mean conversion rates between designs A and B.")
else:
    print("Conclusion: There is NO statistically significant difference in the mean conversion rates between designs A and B.")
