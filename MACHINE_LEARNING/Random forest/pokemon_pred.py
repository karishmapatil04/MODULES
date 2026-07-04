import pandas as pd
import matplotlib.pyplot as plt

#from google.colab import files
#file = files.upload()

# Load data
data = pd.read_csv(
    r'C:\Users\samai\OneDrive\Documents\Codingal_Learn\webdev course\MODULES\MACHINE_LEARNING\Random forest\Pokemon Data.csv'
)

print(data.head())
print(data.info())

# Fill missing values
data['Type 2'] = data['Type 2'].fillna('None')

print(data.isnull().sum())

# Visualizations
data['Type 1'].value_counts().plot.bar()
plt.show()

data['Type 2'].value_counts().plot.bar()
plt.show()

data['Legendary'].value_counts().plot.bar()
plt.show()

# Encode target column
from sklearn.preprocessing import LabelEncoder

lb = LabelEncoder()
data['Legendary'] = lb.fit_transform(data['Legendary'])

# Drop Name column
data.drop('Name', axis=1, inplace=True)

# One-hot encoding
data = pd.get_dummies(data)

# Split features and target
y = data.pop('Legendary')
X = data

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Random Forest Model
from sklearn.ensemble import RandomForestClassifier

rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)

# Prediction
ypred1 = rf.predict(X_test)

# Accuracy
from sklearn.metrics import accuracy_score

print("Accuracy:", accuracy_score(y_test, ypred1))