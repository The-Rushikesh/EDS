# OpinRank Review Dataset Analysis using Numpy and Pandas

import pandas as pd
import numpy as np
from collections import Counter

# Load the dataset
file_path = 'ModelTrain.csv'
df = pd.read_csv(file_path)

# Helper functions
def word_count(text):
    return len(str(text).split())

def all_words(series):
    words = []
    for review in series:
        words.extend(str(review).lower().split())
    return words

# 1. Total number of reviews
total_reviews = df.shape[0]

# 2. Count of POSITIVE and NEGATIVE reviews
sentiment_counts = df['Sentiment'].value_counts()

# 3. Percentage of POSITIVE reviews
positive_percentage = (sentiment_counts['POSITIVE'] / total_reviews) * 100

# 4. Percentage of NEGATIVE reviews
negative_percentage = (sentiment_counts['NEGATIVE'] / total_reviews) * 100

# 5. Average length of reviews (characters)
avg_length_chars = df['Review'].apply(len).mean()

# 6. Average length of positive reviews
avg_length_positive = df[df['Sentiment'] == 'POSITIVE']['Review'].apply(len).mean()

# 7. Average length of negative reviews
avg_length_negative = df[df['Sentiment'] == 'NEGATIVE']['Review'].apply(len).mean()

# 8. Review with maximum characters
max_length_review = df.loc[df['Review'].apply(len).idxmax(), 'Review']

# 9. Review with minimum characters
min_length_review = df.loc[df['Review'].apply(len).idxmin(), 'Review']

# 10. Total number of words across all reviews
total_words = df['Review'].apply(word_count).sum()

# 11. Average number of words per review
avg_words_per_review = df['Review'].apply(word_count).mean()

# 12. Most common word across all reviews
all_words_list = all_words(df['Review'])
most_common_word = Counter(all_words_list).most_common(1)[0]

# 13. Most common word in positive reviews
positive_words_list = all_words(df[df['Sentiment'] == 'POSITIVE']['Review'])
most_common_word_positive = Counter(positive_words_list).most_common(1)[0]

# 14. Most common word in negative reviews
negative_words_list = all_words(df[df['Sentiment'] == 'NEGATIVE']['Review'])
most_common_word_negative = Counter(negative_words_list).most_common(1)[0]

# 15. Number of reviews containing the word "clean"
reviews_with_clean = df['Review'].str.lower().str.contains('clean').sum()

# 16. Positive reviews containing the word "excellent"
positive_with_excellent = df[(df['Sentiment'] == 'POSITIVE') & (df['Review'].str.lower().str.contains('excellent'))].shape[0]

# 17. Negative reviews containing the word "poor"
negative_with_poor = df[(df['Sentiment'] == 'NEGATIVE') & (df['Review'].str.lower().str.contains('poor'))].shape[0]

# 18. Top 5 most frequent words
top_5_words = Counter(all_words_list).most_common(5)

# 19. Reviews having more than 100 words
reviews_more_than_100_words = df[df['Review'].apply(word_count) > 100].shape[0]

# 20. Average word length across all reviews
all_word_lengths = [len(word) for word in all_words_list]
average_word_length = np.mean(all_word_lengths)

# Displaying results
print("Total Reviews:", total_reviews)
print("Sentiment Counts:\n", sentiment_counts)
print(f"Positive %: {positive_percentage:.2f}")
print(f"Negative %: {negative_percentage:.2f}")
print(f"Average Review Length (chars): {avg_length_chars:.2f}")
print(f"Average Positive Review Length (chars): {avg_length_positive:.2f}")
print(f"Average Negative Review Length (chars): {avg_length_negative:.2f}")
print("Review with Maximum Characters (preview):", max_length_review[:300], "...")
print("Review with Minimum Characters:", min_length_review)
print("Total Words:", total_words)
print(f"Average Words per Review: {avg_words_per_review:.2f}")
print("Most Common Word (All Reviews):", most_common_word)
print("Most Common Word (Positive Reviews):", most_common_word_positive)
print("Most Common Word (Negative Reviews):", most_common_word_negative)
print("Reviews with 'clean':", reviews_with_clean)
print("Positive Reviews with 'excellent':", positive_with_excellent)
print("Negative Reviews with 'poor':", negative_with_poor)
print("Top 5 Frequent Words:", top_5_words)
print("Reviews > 100 Words:", reviews_more_than_100_words)
print(f"Average Word Length: {average_word_length:.2f}")
