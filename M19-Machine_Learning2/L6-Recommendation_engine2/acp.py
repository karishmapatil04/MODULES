# Step 1: Import required libraries

import pandas as pd
import numpy as np

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ---------------------------------------------------------
# Step 2: Load the datasets
# ---------------------------------------------------------

recipes = pd.read_csv("recipes.csv")
interactions = pd.read_csv("interactions.csv")

print("Recipes Dataset:")
print(recipes.head())

print("\nInteractions Dataset:")
print(interactions.head())


# ---------------------------------------------------------
# Step 3: Display dataset information
# ---------------------------------------------------------

print("\nRecipes Information:")
print(recipes.info())

print("\nInteractions Information:")
print(interactions.info())


# ---------------------------------------------------------
# Step 4: Select required columns
# ---------------------------------------------------------

# Food.com datasets can use different column names.
# Rename them if necessary.

recipes = recipes.rename(columns={
    "id": "recipe_id",
    "name": "recipe_name",
    "ingredients": "ingredients",
    "tags": "tags"
})

interactions = interactions.rename(columns={
    "user_id": "user_id",
    "recipe_id": "recipe_id",
    "rating": "rating"
})


# ---------------------------------------------------------
# Step 5: Handle missing values
# ---------------------------------------------------------

recipes["ingredients"] = recipes["ingredients"].fillna("")
recipes["tags"] = recipes["tags"].fillna("")


# ---------------------------------------------------------
# Step 6: Convert ingredients and tags into text
# ---------------------------------------------------------

recipes["ingredients"] = recipes["ingredients"].astype(str)
recipes["tags"] = recipes["tags"].astype(str)

recipes["meal_features"] = (
    recipes["ingredients"] + " " + recipes["tags"]
)


# ---------------------------------------------------------
# Step 7: Clean the text
# ---------------------------------------------------------

recipes["meal_features"] = (
    recipes["meal_features"]
    .str.lower()
    .str.replace("[^a-zA-Z0-9 ]", " ", regex=True)
    .str.replace(r"\s+", " ", regex=True)
    .str.strip()
)


# ---------------------------------------------------------
# Step 8: Create TF-IDF representation
# ---------------------------------------------------------

vectorizer = TfidfVectorizer(
    stop_words="english"
)

meal_matrix = vectorizer.fit_transform(
    recipes["meal_features"]
)

print("\nMeal Feature Matrix Shape:")
print(meal_matrix.shape)


# ---------------------------------------------------------
# Step 9: Select a user
# ---------------------------------------------------------

user_id = interactions["user_id"].iloc[0]

print("\nSelected User:", user_id)


# ---------------------------------------------------------
# Step 10: Get meals rated by the selected user
# ---------------------------------------------------------

user_interactions = interactions[
    interactions["user_id"] == user_id
]

print("\nUser Interactions:")
print(user_interactions.head())


# ---------------------------------------------------------
# Step 11: Keep positively rated meals
# ---------------------------------------------------------

# Assuming ratings of 4 or 5 represent positive feedback

liked_meals = user_interactions[
    user_interactions["rating"] >= 4
]

print("\nMeals liked by the user:")
print(liked_meals.head())


# ---------------------------------------------------------
# Step 12: Get the recipe IDs of liked meals
# ---------------------------------------------------------

liked_recipe_ids = liked_meals["recipe_id"].tolist()


# ---------------------------------------------------------
# Step 13: Find the corresponding meal vectors
# ---------------------------------------------------------

liked_indices = recipes[
    recipes["recipe_id"].isin(liked_recipe_ids)
].index


# ---------------------------------------------------------
# Step 14: Build the user's taste profile
# ---------------------------------------------------------

if len(liked_indices) > 0:

    user_profile = meal_matrix[
        liked_indices
    ].mean(axis=0)

else:

    print("No positively rated meals found.")
    user_profile = np.zeros(
        (1, meal_matrix.shape[1])
    )


# ---------------------------------------------------------
# Step 15: Calculate similarity between user
# profile and every meal
# ---------------------------------------------------------

similarity_scores = cosine_similarity(
    user_profile,
    meal_matrix
).flatten()


# ---------------------------------------------------------
# Step 16: Add similarity score to recipes
# ---------------------------------------------------------

recipes["similarity_score"] = similarity_scores


# ---------------------------------------------------------
# Step 17: Remove meals already rated by the user
# ---------------------------------------------------------

recommended_meals = recipes[
    ~recipes["recipe_id"].isin(
        user_interactions["recipe_id"]
    )
]


# ---------------------------------------------------------
# Step 18: Sort meals by similarity
# ---------------------------------------------------------

recommended_meals = recommended_meals.sort_values(
    by="similarity_score",
    ascending=False
)


# ---------------------------------------------------------
# Step 19: Display top recommendations
# ---------------------------------------------------------

print("\nRecommended Meals:")

print(
    recommended_meals[
        [
            "recipe_id",
            "recipe_name",
            "similarity_score"
        ]
    ].head(10)
)