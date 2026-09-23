# Import required libraries
from importlib.metadata import files

import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Import file upload tool for Google Colab
#from google.colab import files


# --------------------------------------------------
# 1. Upload the Titanic CSV file
# --------------------------------------------------

uploaded = files.upload()

# Get the uploaded file name
filename = list(uploaded.keys())[0]

#
# --------------------------------------------------
# 2. Load the dataset
# --------------------------------------------------
# The Titanic file is tab-separated, so we use sep="\t"

Titanic = pd.read_csv(filename, sep="\t")


# --------------------------------------------------
# 3. Display the first few rows
# --------------------------------------------------

Titanic.head()


# --------------------------------------------------
# 4. Check the column names
# --------------------------------------------------

Titanic.columns


# --------------------------------------------------
# 5. Check the shape of the dataset
# --------------------------------------------------

Titanic.shape


# --------------------------------------------------
# 6. Check for missing values
# --------------------------------------------------

Titanic.isnull().sum()


# --------------------------------------------------
# 7. Visualize missing values using a heatmap
# --------------------------------------------------

plt.figure(figsize=(10, 6))

sns.heatmap(Titanic.isnull(), cmap="spring")

plt.show()


# --------------------------------------------------
# 8. Drop the Cabin column
# --------------------------------------------------
# Cabin contains a large number of missing values,
# so we remove this column.

Titanic.drop("Cabin", axis=1, inplace=True)


# Display the dataset after dropping Cabin
Titanic.head()


# --------------------------------------------------
# 9. Remove rows containing missing values
# --------------------------------------------------

Titanic.dropna(inplace=True)


# --------------------------------------------------
# 10. Check for missing values again
# --------------------------------------------------

Titanic.isnull().sum()


# --------------------------------------------------
# 11. Visualize missing values after cleaning
# --------------------------------------------------

plt.figure(figsize=(10, 6))

sns.heatmap(Titanic.isnull(), cbar=False)

plt.show()


# --------------------------------------------------
# 12. Convert Sex into dummy variables
# --------------------------------------------------
# Dummy variables convert categorical values into
# numerical values that can be used for analysis.

pd.get_dummies(Titanic["Sex"]).head()


# --------------------------------------------------
# 13. Create the Sex dummy variable
# --------------------------------------------------

sex = pd.get_dummies(Titanic["Sex"], drop_first=True)

sex.head(4)


# --------------------------------------------------
# 14. Check the Embarked categories
# --------------------------------------------------

pd.get_dummies(Titanic["Embarked"]).head(4)


# --------------------------------------------------
# 15. Create Embarked dummy variables
# --------------------------------------------------

embarked = pd.get_dummies(
    Titanic["Embarked"],
    drop_first=True
)

embarked.head(4)


# --------------------------------------------------
# 16. Create Pclass dummy variables
# --------------------------------------------------

pclass = pd.get_dummies(
    Titanic["Pclass"],
    drop_first=True
)

pclass.head(4)


# --------------------------------------------------
# 17. Combine the new dummy variables
#    with the original dataset
# --------------------------------------------------

Titanic = pd.concat(
    [Titanic, sex, embarked, pclass],
    axis=1
)


# --------------------------------------------------
# 18. Display the final updated dataset
# --------------------------------------------------

Titanic.head()