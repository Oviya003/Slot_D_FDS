import pandas as pd
import scipy.stats as stats

# Load the dataset
df = pd.read_csv("blood_pressure_data.csv")

# Function to calculate 95% confidence interval for a given group
def compute_confidence_interval(data, confidence=0.95):
    n = len(data)
    mean = data.mean()
    std_err = stats.sem(data)  # Standard error of the mean
    margin = std_err * stats.t.ppf((1 + confidence) / 2, df=n-1)
    return (mean - margin, mean + margin)

# Separate groups
drug_data = df[df['Group'] == 'Drug']['BP_Reduction']
placebo_data = df[df['Group'] == 'Placebo']['BP_Reduction']

# Compute confidence intervals
drug_ci = compute_confidence_interval(drug_data)
placebo_ci = compute_confidence_interval(placebo_data)

# Display results
print(f"95% Confidence Interval for Drug Group: {drug_ci}")
print(f"95% Confidence Interval for Placebo Group: {placebo_ci}")
