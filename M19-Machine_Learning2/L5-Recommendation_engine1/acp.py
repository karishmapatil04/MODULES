# Step 1: Install/Import required libraries

import nltk
import pandas as pd
import re
import numpy as np

from nltk.corpus import gutenberg
from sklearn.preprocessing import StandardScaler
from sklearn.metrics.pairwise import cosine_similarity


# Step 2: Download the Gutenberg corpus

nltk.download('gutenberg')


# Step 3: Get the list of available books

book_files = gutenberg.fileids()

print("Available Books:")
for book in book_files:
    print(book)

print("\nTotal Number of Books:", len(book_files))


# Step 4: Create a list to store book information

book_data = []


# Step 5: Extract information from each book

for book in book_files:

    # Get the complete text of the book
    text = gutenberg.raw(book)

    # Get words from the book
    words = gutenberg.words(book)

    # Convert words to lowercase
    words = [word.lower() for word in words]

    # Keep only alphabetic words
    clean_words = [
        word for word in words
        if word.isalpha()
    ]

    # Calculate total words
    total_words = len(clean_words)

    # Calculate unique words
    unique_words = len(set(clean_words))

    # Calculate average word length
    if total_words > 0:
        average_word_length = np.mean(
            [len(word) for word in clean_words]
        )
    else:
        average_word_length = 0

    # Store the information
    book_data.append({
        "Book": book,
        "Total_Words": total_words,
        "Unique_Words": unique_words,
        "Average_Word_Length": average_word_length
    })


# Step 6: Create a Pandas DataFrame

df = pd.DataFrame(book_data)


# Step 7: Display the DataFrame

print("\nBook DataFrame:")
print(df)


# Step 8: Display basic information

print("\nDataFrame Information:")
print(df.info())


# Step 9: Display statistical information

print("\nStatistical Summary:")
print(df.describe())


# Step 10: Calculate vocabulary richness

df["Vocabulary_Richness"] = (
    df["Unique_Words"] / df["Total_Words"]
)

print("\nUpdated DataFrame:")
print(df)


# Step 11: Sort books by total number of words

print("\nBooks sorted by Total Words:")

sorted_books = df.sort_values(
    by="Total_Words",
    ascending=False
)

print(
    sorted_books[
        ["Book", "Total_Words"]
    ]
)


# Step 12: Prepare features for similarity calculation

features = df[
    [
        "Total_Words",
        "Unique_Words",
        "Average_Word_Length",
        "Vocabulary_Richness"
    ]
]


# Step 13: Standardize the features

scaler = StandardScaler()

scaled_features = scaler.fit_transform(features)


# Step 14: Calculate cosine similarity

similarity_matrix = cosine_similarity(
    scaled_features
)


# Step 15: Create a function to find similar books

def find_similar_books(book_name, number_of_books=3):

    # Find the index of the selected book
    book_index = df[
        df["Book"] == book_name
    ].index[0]

    # Get similarity scores
    similarity_scores = similarity_matrix[
        book_index
    ]

    # Sort books according to similarity
    similar_indices = similarity_scores.argsort()[::-1]

    # Remove the selected book itself
    similar_indices = [
        i for i in similar_indices
        if i != book_index
    ]

    # Select top similar books
    similar_indices = similar_indices[
        :number_of_books
    ]

    # Display results
    print("\nBooks similar to:", book_name)

    for i in similar_indices:

        print(
            df.loc[i, "Book"],
            " | Similarity:",
            round(similarity_scores[i], 3)
        )


# Step 16: Test the recommendation system

find_similar_books(
    book_files[0],
    3
)