import pandas as pd
import string
from collections import Counter
import matplotlib.pyplot as plt
from nltk.corpus import stopwords
import nltk
nltk.download('stopwords')
df = pd.read_csv('data.csv')
stop_words = set(stopwords.words('english'))
df['feedback'] = df['feedback'].str.lower()
df['feedback'] = df['feedback'].apply(lambda x: x.translate(str.maketrans('', '', string.punctuation)))
def preprocess_text(text):
    words = text.split()
    return [word for word in words if word not in stop_words]

df['processed_feedback'] = df['feedback'].apply(preprocess_text)
all_words = [word for feedback in df['processed_feedback'] for word in feedback]
word_freq = Counter(all_words)
N = int(input("Enter the number of top frequent words to display: "))
top_n_words = word_freq.most_common(N)
print(f"\nTop {N} most frequent words:")
for word, freq in top_n_words:
    print(f"{word}: {freq}")
words, frequencies = zip(*top_n_words)
plt.figure(figsize=(10, 6))
plt.bar(words, frequencies, color='skyblue')
plt.title(f"Top {N} Most Frequent Words in Customer Feedback")
plt.xlabel('Words')
plt.ylabel('Frequency')
plt.xticks(rotation=45)
plt.show()
