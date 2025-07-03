import numpy as np
fuel_efficiency = np.array([25.5, 30.2, 27.8, 35.0, 33.1])
average_efficiency = np.mean(fuel_efficiency)
print("Average Fuel Efficiency:", round(average_efficiency, 2), "MPG")
model_old = fuel_efficiency[0]
model_new = fuel_efficiency[3]
percentage_improvement = ((model_new - model_old) / model_old) * 100
print("Percentage Improvement from Model 0 to Model 3:", round(percentage_improvement, 2), "%")

