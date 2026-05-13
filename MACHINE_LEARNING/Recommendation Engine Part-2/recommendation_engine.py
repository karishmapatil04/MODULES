# IMPORT LIBRARIES AND DATASET

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import sqrt

# Importing Dataset
ratings_df = pd.read_csv(r'C:\Users\samai\OneDrive\Documents\Codingal_Learn\webdev course\MODULES\MACHINE_LEARNING\Recommendation Engine Part-2\ratings.csv')
movies_df = pd.read_csv(r'C:\Users\samai\OneDrive\Documents\Codingal_Learn\webdev course\MODULES\MACHINE_LEARNING\Recommendation Engine Part-2\movies.csv')

# ==============================
# DATA PREPROCESSING
# ==============================

# Extract year
movies_df['year'] = movies_df.title.str.extract(r'(\(\d{4}\))', expand=True)

# Remove parentheses
movies_df['year'] = movies_df.year.str.extract(r'(\d{4})', expand=True)

# Remove year from title  ✅ FIX: regex=True
movies_df['title'] = movies_df.title.str.replace(r'(\(\d{4}\))', '', regex=True)

# Remove whitespace
movies_df['title'] = movies_df['title'].apply(lambda x: x.strip())

# Convert Genres into list
movies_df['genres'] = movies_df.genres.str.split('|')

# ==============================
# ONE HOT ENCODING
# ==============================

movies_copy = movies_df.copy()

for index, row in movies_df.iterrows():
    for genre in row['genres']:
        movies_copy.at[index, genre] = 1

# Fill NaN
movies_copy = movies_copy.fillna(0)

# ==============================
# CLEAN RATINGS DATA
# ==============================

ratings_df = ratings_df.drop(['timestamp'], axis=1, errors='ignore')

# ==============================
# USER INPUT
# ==============================

user_input = [
    {'title': 'Grand Slam', 'rating': 5.6},
    {'title': 'Zero', 'rating': 7},
    {'title': 'Jumanji', 'rating': 8.5},
    {'title': 'Toy Story', 'rating': 4.5}
]

movies_input = pd.DataFrame(user_input)

# ==============================
# MATCH MOVIES
# ==============================

input_id = movies_df[movies_df['title'].isin(movies_input['title'].tolist())]

# ✅ FIX: Handle missing movies
if input_id.empty:
    print("⚠️ Some movies not found in dataset. Proceeding with available ones.")

# Merge  ✅ FIX: specify 'on'
movies_input = pd.merge(input_id, movies_input, on='title')

# ✅ FIX: reset index (VERY IMPORTANT)
movies_input = movies_input.reset_index(drop=True)

# Drop unnecessary columns
movies_input = movies_input.drop(['genres', 'year'], axis=1, errors='ignore')

# ==============================
# USER MOVIES DATA
# ==============================

movies_user = movies_copy[movies_copy['movieId'].isin(movies_input['movieId'].tolist())]

movies_user = movies_user.reset_index(drop=True)

# ==============================
# USER PROFILE
# ==============================

UserGenreTable = movies_user.drop(['movieId', 'title', 'genres', 'year'], axis=1, errors='ignore')

UserProfile = UserGenreTable.transpose().dot(movies_input['rating'])

# ==============================
# GENRE TABLE
# ==============================

# ✅ FIX: correct set_index
GenreTable = movies_copy.set_index('movieId')

GenreTable = GenreTable.drop(['title', 'genres', 'year'], axis=1, errors='ignore')

# ==============================
# RECOMMENDATION SCORE
# ==============================

# ✅ FIX: avoid division by zero
if UserProfile.sum() == 0:
    raise ValueError("User profile is empty!")

Recommendation_df = ((GenreTable * UserProfile).sum(axis=1)) / UserProfile.sum()

# Sort values
Recommendation_df = Recommendation_df.sort_values(ascending=False)

# ==============================
# FINAL OUTPUT
# ==============================

# ✅ FIX: use .index instead of .keys()
top_ids = Recommendation_df.head(20).index

RecommendationTable = movies_df[movies_df['movieId'].isin(top_ids)]

print("\nTop Recommended Movies:\n")
print(RecommendationTable[['title', 'genres', 'year']])