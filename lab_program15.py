import pandas as pd
data = {
    'PostID': [201, 202, 203, 204, 205, 206, 207, 208],
    'Likes': [10, 15, 10, 20, 15, 10, 25, 20]
}
df = pd.DataFrame(data)
like_frequency = df['Likes'].value_counts().sort_index()
print("Frequency distribution of likes among posts:")
print(like_frequency)
