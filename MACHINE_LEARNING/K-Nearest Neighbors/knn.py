import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  

# Load dataset
data = pd.read_csv(r'C:\Users\samai\OneDrive\Documents\Codingal_Learn\webdev course\MODULES\MACHINE_LEARNING\K-Nearest Neighbors\sample_data.csv')  
print(data.head())

# Split data
from sklearn.model_selection import train_test_split

y = data.pop('TARGET CLASS')
X = data

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Apply KNN
from sklearn.neighbors import KNeighborsClassifier

error_rates = []

for k in range(1, 40):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    preds = knn.predict(X_test)
    
    # Correct error calculation
    error_rates.append(np.mean(preds != y_test))

# Plot graph
plt.figure(figsize=(10, 7))
plt.plot(range(1, 40), error_rates, linestyle='dashed', marker='o')
plt.title('Error Rate vs. K Value')
plt.xlabel('K')
plt.ylabel('Error Rate')
plt.show()