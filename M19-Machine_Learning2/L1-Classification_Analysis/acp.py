# Step 1: Import required libraries
import pandas as pd

# Step 2: Load the dataset
df = pd.read_csv("dataset.csv")

# Step 3: Display the first 5 rows
print("First 5 rows of the dataset:")
print(df.head())

# Step 4: Display information about the dataset
print("\nDataset Information:")
print(df.info())

# Step 5: Select the target/output column
# Change 'Target' to the actual target column name
target_column = 'Target'

# Step 6: Find the unique classes
classes = df[target_column].unique()

print("\nUnique Classes:")
print(classes)

# Step 7: Count the number of classes
number_of_classes = df[target_column].nunique()

print("\nNumber of Classes:", number_of_classes)

# Step 8: Determine the type of classification
if number_of_classes == 2:
    print("The dataset is a BINARY CLASSIFICATION problem.")
elif number_of_classes > 2:
    print("The dataset is a MULTI-CLASS CLASSIFICATION problem.")
else:
    print("The dataset does not have enough classes for classification.")