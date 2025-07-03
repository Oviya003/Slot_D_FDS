import pandas as pd
from collections import Counter
import string
data = {
    'ReviewID': [1, 2, 3, 4],
    'ReviewText': [
        "Great product, really loved it!",
        "Good quality, but too expensive.",
        "Amazing product, worth the price.",
        "Not bad, but expected better quality."
    ]
}
df = pd.DataFrame(data)
all_reviews = ' '.join(df['ReviewText'].str.lower())
all_reviews = all_reviews.translate(str.maketrans('', '', string.punctuation))
words = all_reviews.split()
word_freq = Counter(words)
print("Frequency distribution of words in customer reviews:")
print(word_freq)
