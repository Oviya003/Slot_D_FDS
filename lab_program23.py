import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ttest_ind

np.random.seed(42)
control = np.random.normal(50, 10, 30)
treatment = np.random.normal(55, 10, 30)

t_stat, p_value = ttest_ind(treatment, control, equal_var=False)
print(f"T-statistic: {t_stat:.3f}, P-value: {p_value:.4f}")

plt.boxplot([control, treatment], labels=['Placebo', 'Treatment'])
plt.title('Clinical Trial Results')
plt.ylabel('Measurement')
plt.text(1.5, max(control.max(), treatment.max()) + 2, f'p = {p_value:.4f}', ha='center')
plt.show()
