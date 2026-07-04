# =========================
# Water Potability Prediction
# =========================

# Import Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Upload Dataset (Google Colab)
#from google.colab import files
#uploaded = files.upload()

# Load Dataset
df = pd.read_csv(r'C:\Users\samai\OneDrive\Documents\Codingal_Learn\webdev course\MODULES\MACHINE_LEARNING\WQP using ML algo\water_potability.csv')

# =========================
# Exploratory Data Analysis
# =========================

print("First 5 Rows:")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset Information:")
print(df.info())

print("\nStatistical Summary:")
print(df.describe())

# =========================
# Data Preprocessing
# =========================

# Fill missing values with column mean
df.fillna(df.mean(), inplace=True)

print("\nMissing Values After Imputation:")
print(df.isnull().sum())

# Target Distribution
print("\nPotability Counts:")
print(df['Potability'].value_counts())

# =========================
# Data Visualization
# =========================

# Count Plot
plt.figure(figsize=(6,4))
sns.countplot(x='Potability', data=df)
plt.title('Water Potability Distribution')
plt.show()

# pH Distribution
plt.figure(figsize=(8,5))
sns.histplot(df['ph'], kde=True, bins=30)
plt.title('Distribution of pH')
plt.show()

# Histograms
df.hist(figsize=(14,14))
plt.tight_layout()
plt.show()

# Correlation Heatmap
plt.figure(figsize=(13,8))
sns.heatmap(df.corr(), annot=True, cmap='terrain')
plt.title('Correlation Heatmap')
plt.show()

# Boxplots
plt.figure(figsize=(14,7))
df.boxplot()
plt.xticks(rotation=45)
plt.show()

# =========================
# Feature Selection
# =========================

X = df.drop('Potability', axis=1)
Y = df['Potability']

# =========================
# Feature Scaling
# =========================

from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
X = scaler.fit_transform(X)

# =========================
# Train-Test Split
# =========================

from sklearn.model_selection import train_test_split

X_train, X_test, Y_train, Y_test = train_test_split(
    X,
    Y,
    test_size=0.2,
    random_state=101,
    shuffle=True
)

# =========================
# Model Evaluation Function
# =========================

from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

def evaluate_model(model, X_test, Y_test):
    prediction = model.predict(X_test)

    print(f"\nAccuracy Score = {accuracy_score(Y_test, prediction)*100:.2f}%")
    print("\nConfusion Matrix:")
    print(confusion_matrix(Y_test, prediction))

    print("\nClassification Report:")
    print(classification_report(Y_test, prediction))

# =========================
# Decision Tree Classifier
# =========================

from sklearn.tree import DecisionTreeClassifier

dt = DecisionTreeClassifier(
    criterion='gini',
    min_samples_split=10,
    splitter='best',
    random_state=42
)

dt.fit(X_train, Y_train)

print("="*50)
print("DECISION TREE RESULTS")
print("="*50)

evaluate_model(dt, X_test, Y_test)

# =========================
# K-Nearest Neighbors
# =========================

from sklearn.neighbors import KNeighborsClassifier

knn = KNeighborsClassifier(n_neighbors=10)

knn.fit(X_train, Y_train)

print("\n" + "="*50)
print("KNN RESULTS")
print("="*50)

evaluate_model(knn, X_test, Y_test)

# =========================
# Logistic Regression
# =========================

from sklearn.linear_model import LogisticRegression

log = LogisticRegression(
    random_state=0,
    max_iter=1000
)

log.fit(X_train, Y_train)

print("\n" + "="*50)
print("LOGISTIC REGRESSION RESULTS")
print("="*50)

evaluate_model(log, X_test, Y_test)

# =========================
# Accuracy Comparison
# =========================

dt_acc = accuracy_score(Y_test, dt.predict(X_test))
knn_acc = accuracy_score(Y_test, knn.predict(X_test))
log_acc = accuracy_score(Y_test, log.predict(X_test))

results = pd.DataFrame({
    'Model': ['Decision Tree', 'KNN', 'Logistic Regression'],
    'Accuracy (%)': [
        dt_acc * 100,
        knn_acc * 100,
        log_acc * 100
    ]
})

print("\nModel Comparison:")
print(results)

# Visualization of Accuracy Comparison
plt.figure(figsize=(8,5))
sns.barplot(
    x='Model',
    y='Accuracy (%)',
    data=results,
    palette='viridis'
)

plt.title('Model Accuracy Comparison')
plt.ylim(0, 100)

for index, value in enumerate(results['Accuracy (%)']):
    plt.text(index, value + 1, f"{value:.2f}%", ha='center')

plt.show()

# =========================
# Best Model
# =========================

best_model = results.loc[results['Accuracy (%)'].idxmax()]

print("\nBest Performing Model:")
print(best_model)