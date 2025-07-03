import pandas as pd
import numpy as np
from scipy.stats import sem, t

data = pd.read_csv('rare_elements.csv').iloc[:, 0].values

def conf_interval(sample, conf):
    n = len(sample)
    mean = np.mean(sample)
    margin = sem(sample) * t.ppf((1 + conf) / 2, n - 1)
    return mean, mean - margin, mean + margin

def main():
    n = int(input("Sample size (≤ total data): "))
    conf = float(input("Confidence level (e.g., 0.95): "))
    precision = float(input("Desired margin of error: "))
    if n > len(data):
        print(f"Sample size too large! Max: {len(data)}"); return
    sample = np.random.choice(data, n, replace=False)
    mean, lower, upper = conf_interval(sample, conf)
    margin = (upper - lower) / 2
    print(f"\nMean: {mean:.4f}")
    print(f"{int(conf*100)}% CI: [{lower:.4f}, {upper:.4f}]")
    print(f"Margin of Error: {margin:.4f}")
    print("Desired precision achieved." if margin <= precision else "Precision NOT achieved. Increase sample size.")

if __name__ == "__main__":
    main()
