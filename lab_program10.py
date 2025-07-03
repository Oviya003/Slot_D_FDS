import matplotlib.pyplot as plt
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [1000, 1200, 1100, 1500, 1700, 1600]
plt.figure(figsize=(10, 4))
plt.subplot(1, 2, 1)
plt.plot(months, sales, marker='o', linestyle='-', color='b')
plt.title('Monthly Sales (Line Plot)')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.subplot(1, 2, 2)
plt.bar(months, sales, color='pink')
plt.title('Monthly Sales (Bar Plot)')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.tight_layout()
plt.show()
