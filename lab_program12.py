import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
          'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
temperature = [4, 6, 10, 15, 20, 25, 28, 27, 22, 16, 9, 5]
rainfall = [78, 60, 72, 55, 48, 35, 30, 40, 58, 70, 85, 90]
plt.figure(figsize=(8, 5))
plt.plot(months, temperature, marker='o', color='red')
plt.title('1.Monthly Temperature (Line Plot)')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()
plt.figure(figsize=(8, 5))
plt.scatter(months, rainfall, color='blue')
plt.title('2.Monthly Rainfall (Scatter Plot)')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.show()
