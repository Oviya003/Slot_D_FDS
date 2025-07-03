import pandas as pd
import matplotlib.pyplot as plt

# Load player data
players = pd.read_csv("soccer_players.csv")

# Top 5 players by goals
top_goals = players.sort_values('goals', ascending=False).head(5)

# Top 5 players by salary
top_salary = players.sort_values('salary', ascending=False).head(5)

# Average age
avg_age = players['age'].mean()
above_avg_age = players[players['age'] > avg_age]

# Print outputs
print("Top 5 Goal Scorers:\n", top_goals[['name', 'goals']])
print("\nTop 5 Salaries:\n", top_salary[['name', 'salary']])
print("\nPlayers above average age (%.2f):\n" % avg_age, above_avg_age[['name', 'age']])

# Plot player distribution by position
players['position'].value_counts().plot(kind='bar', title='Player Distribution by Position')
plt.xlabel("Position")
plt.ylabel("Number of Players")
plt.tight_layout()
plt.show()
