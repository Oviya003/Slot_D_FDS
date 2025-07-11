import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
data = {
    'age': [23, 23, 27, 27, 39, 41, 47, 49, 50, 
            52, 54, 54, 56, 57, 58, 58, 60, 61],
    '%fat': [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2,
             34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
}
df = pd.DataFrame(data)
stats = df.agg(['mean', 'median', 'std'])
plt.figure(figsize=(15, 10))
plt.subplots_adjust(hspace=0.4, wspace=0.3)
plt.subplot(2, 2, 1)
df.boxplot(column='age')
plt.title('Age Distribution')
plt.subplot(2, 2, 2)
df.boxplot(column='%fat')
plt.title('Body Fat Percentage')
plt.subplot(2, 2, 3)
plt.scatter(df['age'], df['%fat'], c='teal', alpha=0.7)
plt.xlabel('Age')
plt.ylabel('% Fat')
plt.grid(True, linestyle='--', alpha=0.7)
plt.subplot(2, 2, 4)
sm.qqplot(df['age'], line='s', label='Age')
sm.qqplot(df['%fat'], line='s', label='% Fat')
plt.legend()
plt.title('Q-Q Plot Comparison')
plt.tight_layout()
plt.show()
print("Statistical Summary:\n", stats.round(2))
